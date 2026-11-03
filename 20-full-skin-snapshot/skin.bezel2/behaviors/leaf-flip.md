# Leaf flip (book-page leaf — family index)

**Object:** leaf-flip family — `xml/Includes_Bezel.xml` hinge group (camera 1440,520, FOLDLOCK) · `scripts/bz_flip.py` `idle_hinge()` · Home props `bz_hf_a` / `bz_hf_b` / `bz_hf_ph`
**Last updated:** 2026-11-02 · 5.33.309
**Status:** idle use **approved / LOCKED** (see idle-big-album-fold.md) · while-play next-song **not leaf** — uses album sway next song fade (5.33.301) · FS stubs **PLANNED** (not shipped)

## Simple
Leaf flip is its own animation: the cover is cut at the slit (x1440) and the right half turns like a book page to reveal the next cover. It has its own clock (`bz_hf_ph`, 1400 ms per phase) and its own props. It is **not** the rock/sway tip and **not** the album-change full flip. Every place that wants a "page turn" uses this file's behaviour — nothing borrows from sway or `bz_cov_side`.

## How it works
- **Look source:** the locked idle Big Album fold — [idle-big-album-fold.md](idle-big-album-fold.md) is the single source for geometry, shadows, frames, glare (5.33.266 look / 267 lock). Do not restate or alter it here.
- **Core:** pivot rotatey at slit x1440 (group 1140,220 600×600), camera 1440,520. ph1 A-right 0→+90, ph2 B-left −90→0, 1400 ms sine in/out each, then A:=B and `bz_hf_ph` cleared.
- **Own clock:** phases are driven by Python (`bz_hf_ph` = 1/2, `waitForAbort(1.4)`), not by the sway go/pulse clock.
- **Uses:**
  | Use | Status | Trigger / hold |
  |---|---|---|
  | Idle Big Album (Music list 60, no audio) | **LIVE · LOCKED** | 10 s hold (5 s under MM warm, 5.33.279 MMLEAF) |
  | While-play next-song | **Not leaf** (5.33.301) | album change while playing = album sway next song fade inside the sway tree (`bz_cov_x`/`bz_cov_xf`, 900 ms); leaf on that path stays parked |
  | FS stubs leaf | **PLANNED** — not shipped | reuse same 1400 ms × 2 timing / slit model |
- **MUST NOT:**
  - share the rock/sway clock (`bz_sway_go`, `bz_big_go`/`bz_big_pulse`, `bz_audio_latch` lead-in, ±13° / −30° tips) — see [sway-animations.md](sway-animations.md);
  - reuse the `bz_cov_side` full flip (0→90 / −90→0 whole cover, ~1857 ms) — separate path, **parked for next-song since 5.33.301** (XML kept for the music → video path);
  - be triggered by play start (play start = rock lead-in only).

## Wiring
| Piece | Where |
|---|---|
| Props (owned) | `bz_hf_a` current cover · `bz_hf_b` next (preload at hold start) · `bz_hf_ph` 1/2 during phases |
| Driver | `bz_flip.py` `idle_hinge()` (gate `ok()` idle OR `mmw()`); future uses get their own entry point but same props/timing |
| XML | hinge group visible `!Player.HasAudio + Window.IsActive(music) + !String.IsEmpty(bz_hf_a)` |
| Not owned | `bz_cov_side` (album-change flip) · `bz_sway*` / `bz_big_*` / `bz_audio_latch` (rock/sway) |
| Restart | XML/media → ReloadSkin; `bz_flip.py` → FULL restart |

## Track-list flip — DELETED (5.33.309)
Rob (Nov 2 2026): "We don't use it anymore." The tap-to-flip track list is gone: list 6185, include `BezelFlipText`, `BezelNPHeader`, variable `BezelBackPath`, the black back-face panel, the 1112 album tap 6381, `bz_back` / `bz_backanim` / `bz_back_close` / `bz_back_pick` / `bz_back_fade`, and `back_face()` / `play_pick()` in `bz_flip.py` (only the `bz_albumid` tracker is kept, as `album_id()`).
**Kept, separate from the picker:** leaf flip (this file), sway, album next song fade, the `bz_flipping` glare fade and the `bz_cov_side` album flip.


## Enable gate (5.33.405 LEAFFLIP)
Leaf flip runs only when `Skin.HasSetting(bz_leafflip)` — **default OFF**. Toggle: Tuner › ALBUM / POSTER › Leaf flip (after Idle rock). Off → `idle_hinge()` `ok()` false → `bz_hf_*` cleared, no phases. Look/timing above unchanged (LOCKED).
