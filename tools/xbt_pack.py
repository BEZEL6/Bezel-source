#!/usr/bin/env python3
"""BEZEL Textures.xbt packer (XBTF v2, same layout as Kodi 21 TexturePacker).

Usage: xbt_pack.py <media_dir> <out.xbt> <liblzo2.so> [--max-pixels N] [--list packed.txt]

- Packs .png/.jpg/.jpeg under media_dir whose width*height <= max-pixels (default 512*512).
  Larger images stay loose on purpose: a bundled texture is always loaded on Kodi's render thread,
  even with background="true" (GUITexture.cpp: the large loader checks the bundle first and loads it
  synchronously), while a loose one with background="true" decodes on a worker thread.
- Pixels: A8R8G8B8 (BGRA bytes), not premultiplied, XB_FMT_OPAQUE when every alpha is 255.
- LZO1X-999 compressed (stored raw when compression does not shrink the frame), as TexturePacker.
- Identical images share one data block (TexturePacker dupecheck).
- Paths are relative to media_dir, lower case, '/' separators (CTextureBundleXBT::Normalize).
"""
import ctypes, hashlib, os, struct, sys
from multiprocessing import Pool
from PIL import Image

XB_FMT_A8R8G8B8 = 0x10
XB_FMT_OPAQUE = 0x10000
LZO1X_999_MEM_COMPRESS = 14 * 16384 * 2

_lzo = None
def _lzo_lib(path):
    global _lzo
    if _lzo is None:
        _lzo = ctypes.CDLL(path)
        # lzo_init() == __lzo_init_v2(LZO_VERSION, sizeof(short), sizeof(int), sizeof(long), sizeof(lzo_uint32_t),
        #                             sizeof(lzo_uint), lzo_sizeof_dict_t, sizeof(char*), sizeof(lzo_voidp), sizeof(lzo_callback_t))
        P = ctypes.sizeof(ctypes.c_void_p)
        r = _lzo.__lzo_init_v2(0x20a0, ctypes.sizeof(ctypes.c_short), ctypes.sizeof(ctypes.c_int), ctypes.sizeof(ctypes.c_long),
                               4, ctypes.sizeof(ctypes.c_size_t), P, P, P, 48)
        if r != 0:
            raise RuntimeError('lzo_init failed %d' % r)
    return _lzo

def _compress(data, libpath):
    lz = _lzo_lib(libpath)
    n = len(data)
    out = ctypes.create_string_buffer(n + n // 16 + 64 + 3)
    outlen = ctypes.c_size_t(len(out))
    wrk = ctypes.create_string_buffer(LZO1X_999_MEM_COMPRESS)
    r = lz.lzo1x_999_compress(data, ctypes.c_size_t(n), out, ctypes.byref(outlen), wrk)
    if r != 0 or outlen.value >= n:
        return None
    packed = out.raw[:outlen.value]
    # round-trip check (what Kodi does: lzo1x_decompress_safe)
    back = ctypes.create_string_buffer(n)
    blen = ctypes.c_size_t(n)
    r = lz.lzo1x_decompress_safe(packed, ctypes.c_size_t(len(packed)), back, ctypes.byref(blen), None)
    if r != 0 or blen.value != n or back.raw != data:
        raise RuntimeError('LZO round-trip failed')
    return packed

def _work(args):
    rel, full, libpath = args
    im = Image.open(full)
    im.load()
    w, h = im.size
    rgba = im.convert('RGBA')
    data = rgba.tobytes('raw', 'BGRA')
    opaque = rgba.getchannel('A').getextrema() == (255, 255)
    md5 = hashlib.md5(data).hexdigest()
    packed = _compress(data, libpath)
    return rel, w, h, opaque, md5, data if packed is None else packed, len(data)

def main():
    media, out, libpath = sys.argv[1:4]
    maxpx = 512 * 512
    listfile = None
    a = sys.argv[4:]
    if '--max-pixels' in a: maxpx = int(a[a.index('--max-pixels') + 1])
    if '--list' in a: listfile = a[a.index('--list') + 1]
    jobs = []
    for r, d, fs in os.walk(media):
        d.sort()
        for f in sorted(fs):
            if not f.lower().endswith(('.png', '.jpg', '.jpeg')): continue
            full = os.path.join(r, f)
            rel = os.path.relpath(full, media).replace('\\', '/').strip().lower()
            if len(rel.encode('utf-8')) > 255: continue
            try:
                w, h = Image.open(full).size
            except Exception:
                continue
            if w * h > maxpx: continue
            jobs.append((rel, full, libpath))
    with Pool() as p:
        res = p.map(_work, jobs, chunksize=4)
    res.sort(key=lambda x: x[0])
    # header size: magic 4 + version 1 + count 4 + per file (256 path + 4 loop + 4 nframes + frame 4+4+4+8+8+4+8)
    hdr = 4 + 1 + 4 + len(res) * (256 + 4 + 4 + 40)
    off = hdr; blobs = []; seen = {}; entries = []
    for rel, w, h, opaque, md5, blob, usize in res:
        if md5 in seen:
            o, psize = seen[md5]
        else:
            o, psize = off, len(blob); seen[md5] = (o, psize); blobs.append(blob); off += psize
        fmt = XB_FMT_A8R8G8B8 | (XB_FMT_OPAQUE if opaque else 0)
        entries.append((rel, w, h, fmt, psize, usize, o))
    with open(out, 'wb') as f:
        f.write(b'XBTF'); f.write(b'2'); f.write(struct.pack('<I', len(entries)))
        for rel, w, h, fmt, psize, usize, o in entries:
            f.write(rel.encode('utf-8').ljust(256, b'\0'))
            f.write(struct.pack('<II', 0, 1))
            f.write(struct.pack('<IIIQQIQ', w, h, fmt, psize, usize, 0, o))
        assert f.tell() == hdr
        for b in blobs: f.write(b)
    if listfile:
        with open(listfile, 'w') as f:
            for e in entries: f.write(e[0] + '\n')
    print('packed %d textures (%d unique), %.1f MB' % (len(entries), len(blobs), off / 1e6))

if __name__ == '__main__':
    main()
