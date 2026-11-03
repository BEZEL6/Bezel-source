import ctypes, struct, sys, os
from PIL import Image
xbt, media, lib = sys.argv[1:4]
lz = ctypes.CDLL(lib)
d = open(xbt,'rb').read(); assert d[:5]==b'XBTF2'
n = struct.unpack_from('<I', d, 5)[0]; p = 9; bad = 0; raw = 0; png = 0
for i in range(n):
    path = d[p:p+256].split(b'\0')[0].decode(); p += 256
    loop, nf = struct.unpack_from('<II', d, p); p += 8
    w, h, fmt, ps, us, dur, off = struct.unpack_from('<IIIQQIQ', d, p); p += 40
    blob = d[off:off+ps]
    if ps < us:
        out = ctypes.create_string_buffer(us); ol = ctypes.c_size_t(us)
        r = lz.lzo1x_decompress_safe(blob, ctypes.c_size_t(ps), out, ctypes.byref(ol), None)
        assert r == 0 and ol.value == us; blob = out.raw
    # find source file case-insensitively
    src = None
    for r_, ds, fs in os.walk(media):
        for f in fs:
            if os.path.relpath(os.path.join(r_, f), media).replace('\\','/').lower() == path: src = os.path.join(r_, f)
        if src: break
    im = Image.open(src).convert('RGBA'); ref = im.tobytes('raw','BGRA')
    raw += us; png += os.path.getsize(src)
    op = im.getchannel('A').getextrema()==(255,255)
    if blob != ref or (w,h)!=im.size or bool(fmt & 0x10000)!=op or (fmt & 0xffff)!=0x10: bad += 1; print('BAD', path)
print('entries', n, 'bad', bad, 'raw MB %.1f' % (raw/1e6), 'loose png MB %.1f' % (png/1e6))
