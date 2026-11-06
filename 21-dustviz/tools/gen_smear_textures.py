#!/usr/bin/env python3
"""Write the six DustViz smear style textures (white RGB, shaped alpha).

Original pack textures (bar_soft, smear_fall, glow_disc) are left untouched.
Re-run from 21-dustviz: python3 tools/gen_smear_textures.py
"""
import math
import os
import shutil
import struct
import zlib

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PACK = os.path.join(ROOT, "viz.addons", "topbar_smear", "textures")
ADDON_PACK = os.path.join(
    ROOT, "visualization.bezel", "visualization.bezel", "resources", "packs", "topbar_smear"
)


def write_png(path, w, h, rgba):
    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    raw = bytearray()
    for y in range(h):
        raw.append(0)
        raw.extend(rgba[y * w * 4 : (y + 1) * w * 4])
    ihdr = struct.pack(">IIBBBBB", w, h, 8, 6, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b"")
    with open(path, "wb") as f:
        f.write(png)


def buf(w, h):
    return bytearray(w * h * 4)


def put(px, w, x, y, a):
    a = 0 if a < 0 else 255 if a > 255 else int(a)
    i = (y * w + x) * 4
    px[i] = px[i + 1] = px[i + 2] = 255
    px[i + 3] = a


def cascade(w=64, h=256):
    px = buf(w, h)
    for y in range(h):
        v = (y + 0.5) / h  # 0 at image top (root, sits on the bar)
        for x in range(w):
            u = abs((x + 0.5) / w - 0.5) * 2
            wob = 0.86 + 0.14 * math.sin(v * 22.0 + u * 5.0)
            edge = math.exp(-(u * u) * (2.4 + 1.6 * v))
            fall = math.exp(-v * 1.15) * (1.0 - 0.15 * v)
            core = math.exp(-(u * u) * 14.0) * math.exp(-v * 0.65)
            a = (edge * fall * wob * 0.85 + core * 0.55) * 255
            put(px, w, x, y, a)
    return w, h, px


def whip(w=256, h=48):
    px = buf(w, h)
    for y in range(h):
        v = abs((y + 0.5) / h - 0.5) * 2
        for x in range(w):
            u = (x + 0.5) / w  # 1 = head (right), 0 = tail
            along = u * u * (0.25 + 0.75 * u)
            vert = math.exp(-(v * v) * (5.5 + 3.0 * (1.0 - u)))
            head = math.exp(-((u - 1.0) ** 2) / 0.012) * math.exp(-(v * v) * 8.0)
            a = min(255, (along * vert * 0.95 + head * 0.9) * 255)
            put(px, w, x, y, a)
    return w, h, px


def rain(w=16, h=128):
    px = buf(w, h)
    for y in range(h):
        v = (y + 0.5) / h
        along = math.exp(-((v - 0.12) ** 2) / 0.08) * 0.35 + math.exp(-v * 0.85) * 0.9
        if v < 0.02 or v > 0.97:
            along *= 0.2
        for x in range(w):
            u = abs((x + 0.5) / w - 0.5) * 2
            core = math.exp(-(u * u) / (2 * 0.07 * 0.07))
            glow = math.exp(-(u * u) / (2 * 0.28 * 0.28)) * 0.35
            a = min(255, (core * 0.95 + glow) * along * 255)
            put(px, w, x, y, a)
    return w, h, px


def fog(w=256, h=256):
    px = buf(w, h)
    for y in range(h):
        v = abs((y + 0.5) / h - 0.5) * 2
        for x in range(w):
            u = abs((x + 0.5) / w - 0.5) * 2
            d = math.sqrt(u * u + v * v)
            blob = math.exp(-(d * d) / (2 * 0.42 * 0.42))
            soft = math.exp(-(d * d) / (2 * 0.72 * 0.72)) * 0.45
            a = (blob * 0.75 + soft) * 210
            put(px, w, x, y, a)
    return w, h, px


def mirror(w=48, h=256):
    px = buf(w, h)
    for y in range(h):
        v = (y + 0.5) / h
        sigma = 0.18 + 0.42 * (1.0 - v)  # wide at the root, needle at the inward tip
        fall = (1.0 - v) ** 1.65
        for x in range(w):
            u = abs((x + 0.5) / w - 0.5) * 2
            taper = math.exp(-(u * u) / (2 * sigma * sigma))
            a = fall * taper * 255
            put(px, w, x, y, a)
    return w, h, px


def stagger(w=64, h=192):
    px = buf(w, h)
    for y in range(h):
        v = (y + 0.5) / h
        cap = math.exp(-((v - 0.06) ** 2) / 0.0045)
        body = math.exp(-v * 1.35)
        for x in range(w):
            u = abs((x + 0.5) / w - 0.5) * 2
            edge = math.exp(-(u * u) * 3.4)
            core = math.exp(-(u * u) * 16.0)
            a = min(255, (body * edge * 0.8 + cap * core * 0.95 + cap * edge * 0.35) * 255)
            put(px, w, x, y, a)
    return w, h, px


def main():
    os.makedirs(PACK, exist_ok=True)
    for name, fn in (
        ("cascade_trail", cascade),
        ("whip_streak", whip),
        ("rain_line", rain),
        ("fog_bloom", fog),
        ("mirror_trail", mirror),
        ("stagger_pulse", stagger),
    ):
        w, h, px = fn()
        path = os.path.join(PACK, name + ".png")
        write_png(path, w, h, px)
        print(f"wrote {path} {w}x{h} ({os.path.getsize(path)} bytes)")
    os.makedirs(os.path.dirname(ADDON_PACK), exist_ok=True)
    if os.path.isdir(ADDON_PACK):
        shutil.rmtree(ADDON_PACK)
    shutil.copytree(os.path.dirname(PACK), ADDON_PACK)
    print("copied pack ->", ADDON_PACK)


if __name__ == "__main__":
    main()
