# Idle Big Album fold (book-page leaf)

**Object:** `xml/Includes_Bezel.xml` hinge group (~L1096, camera 1440,520) · `scripts/bz_flip.py` `idle_hinge()` (~L1458) · Home props `bz_hf_a` / `bz_hf_b` / `bz_hf_ph`
**Last updated:** 2026-11-02 · 5.33.355 (look = 5.33.266)
**Status:** **APPROVED — LOCKED 100% (Rob, Nov 1 2026, pt1992u "Leaf anim 100%. Lock in")**. Do not change timing, shadows, frames, glare or geometry without Rob asking.

> Part of the **leaf-flip** family — see [leaf-flip.md](leaf-flip.md) (own clock; not rock/sway, not `bz_cov_side`).

## Simple
When Music is idle (nothing playing) and list 60 is focused, the big album turns like a book page every 10 s. The cover is cut down the middle. The right half lifts off the slit and swings toward you, and the next cover shows underneath. Then the next cover's left half lands over the old left half. The page is solid, the shadows sell the lift and landing, the white border stays sliced and rides with the page, and the glare never pops.

## How it works
- **Book page, left 1 | right 2.** Each cover is two 300×600 half images meeting invisibly at the slit x1440 (group 1140,220 600×600). Layers: A-left static (1140), B-right next cover (1440), preloaded under the page during the hold.
- **Pivot at the slit.** Both leaves use rotatey centred at x1440. The camera is on the slit (1440,520), so 90° is exactly edge-on.
- **Two phases, 1400 ms sine in/out each:**
  - **ph1 (lift → centre):** A-right leaf rotatey 0→+90.
  - **ph2 (centre → land):** B-left leaf rotatey −90→0 lands over A-left. The back of the page is the next cover's front.
  - Then A:=B (same pixels, seamless) and `bz_hf_ph` is cleared.
- **Perspective away.** The free edge swings toward the viewer, so it grows taller past the frame top and bottom instead of shrinking into the album (5.33.251 sign flip).
- **Opaque leaf.** The leaf images have no alpha or colordiffuse. Global dim (`bz_at_gdim`) doesn't touch the big album.
- **Shadows, keyed to centre** (all hidden at rest, synced to `bz_hf_ph`, 1400 ms sine):
  - Static left: `hf_shd_grad_l` (darkest at slit) stays at 0 through ph1, then 0→70 in ph2. `hf_shd_hinge_l` stays at 0 in ph1, then 0→100 in ph2.
  - Under/next right: `hf_shd_grad_r` 70→0 in ph1 and 0 in ph2. `hf_shd_cast` 100→0 in ph1 and 0 in ph2. `hf_shd_grad_r_outer` (darkest at slit → light outer) 0→60 in ph1, 60→0 in ph2.
  - Leaf: darkens 0→45 while turning away (ph1). The landing leaf goes 45→0 (ph2).
- **Frames.** The full `bz_frame_soft` is hidden while the hinge stack shows. The static half-frames `bz_frame_half_l/r` are always on, so the back cover keeps its border with no pop. Each leaf carries its own half-frame that rides the rotatey (ph1: `_r`, ph2: `_l`).
- **Glare, continuous (5.33.266).** The static L/R half glares sit inside the hinge stack, under the leaves, with no `bz_hf_ph` conditions. Each leaf carries an exact copy of the matching static half glare (same texture, `BzATGlare8C`, same go/pulse anims). The opaque leaf hides the static glare under it, so only one glare shows per pixel and there's no handoff or pop. Outside the hinge stack, the old glare group draws the same static glares.
- **Hold:** 10 s between folds. A focus change, playback, `bz_nav`, `bz_randpend` or `bz_back` resets or clears it.

## Wiring
| Piece | Where |
|---|---|
| Loop | `bz_flip.py` `idle_hinge()`: `HOLD=10.0`; `ok()` = `!Player.HasAudio + Window.IsActive(music) + Control.HasFocus(60)` and no nav/randpend/back |
| Covers | Artist row: current + that artist's albums by year (wraps). Album row: album ↔ `artist.thumb`. `Default*` art skipped. Needs ≥2 |
| Props | `bz_hf_a` = current cover, `bz_hf_b` = next (set at hold start = preload), `bz_hf_ph` = `1`/`2` during phases, `waitForAbort(1.4)` each |
| XML | Hinge group visible `!Player.HasAudio + Window.IsActive(music) + !String.IsEmpty(bz_hf_a)`; camera 1440,520; FOLDLOCK marker comment |
| Media | `bezel/bz_frame_half_l/r.png`, `hf_shd_grad_l/r.png`, `hf_shd_grad_r_outer.png`, `hf_shd_hinge_l.png`, `hf_shd_cast.png`, `art_mask_hl/hr.png` |
| Restart | XML/media → ReloadSkin; `bz_flip.py` → FULL restart |

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/idle-big-album-fold.md) · [state](../state/idle-big-album-fold.md) · [motion](../motion/idle-big-album-fold.md) · [art](../art/idle-big-album-fold.md) · [input](../input/idle-big-album-fold.md) · [theme](../theme/tokens.md) · [screens](../port-refs/idle-big-album-fold/) · [PORT_INDEX](../PORT_INDEX.md)

## Current state — 5.33.279 (MMLEAF, Rob pt2150u)
- Gate `ok()` = idle path (`!Player.HasAudio + Window.IsActive(music) + Control.HasFocus(60)`, no bz_nav) **OR** `mmw()`: bz_nav=true, Music window warm under MM, focus 6996 (strip) or 6897 (MM idle park), no bz_mmwarm (mid-swap), no bz_navtune/bz_navbez submenu, no modal, no audio. bz_randpend/bz_back still block both.
- HOLD: 10.0 s idle list; 5.0 s under MM warm.
- Fold look unchanged (LOCKED .266/.267: 1400 ms/phase, shadows, glare, geometry). While-playing next-song anim stays PARKED.

## Under dim (5.33.313 LEAFDIM)
The fold lives inside the section parent group, so BezelSecDim's fade (mmdim with MM open, gdim 1–6 with MM closed) applies to it, and Kodi fades each layer separately, which made the stacked halves show through. Expression `bz_lfdim` is true whenever that fade is active. While it is true:
- the static B-right half and both leaf groups are hidden, a static A-right half shows, and the fold pauses visually, so A is a single opaque stack.
- the base `BezelBigArt` image under the fold is hidden.
- the fold shadow / landing overlays (all `bz_hf_ph`-driven) are hidden too.
- `idle_hinge()` `dim()` mirrors `bz_lfdim` (bz_nav && !bz_mmidle, or MM closed && gdim 1–6): the hold timer is paused and no phases run, so there is no glare/shadow-only ghost flip. If dim lands mid-fold the fold aborts and re-arms. A focus/artist change while dimmed just sets the new A (no fold).
When the dim lifts (e.g. MM auto-hide), the hold restarts and the next fold runs with the current cover (5 s under MM, 10 s idle list). (5.33.375 LEAFWAKE)

## Cold start (5.33.355 COLDLEAF, Rob pt2531u)
On cold start / first MM open, list 60 and its art + album RPC fill in late. `idle_hinge()` now:
- does not lock a key while `Container(60).ListItem.DBID` is empty (list not populated);
- for 6 s after a key locks (before the first fold), re-reads `covers()` about once a second and, if the list changed (late thumb / albums), takes the new list and restarts the hold from A. Fold look/timing unchanged (LOCKED).


## Enable gate (5.33.405 LEAFFLIP)
Leaf flip runs only when `Skin.HasSetting(bz_leafflip)` — **default OFF**. Toggle: Tuner › ALBUM / POSTER › Leaf flip (Idle rock row removed 5.33.408). Off → `idle_hinge()` `ok()` false → `bz_hf_*` cleared, no phases. Look/timing above unchanged (LOCKED).

## MM album fade (5.33.407 MIDLEFADE)
Idle Music big-album A/B dissolve (slots `bz_m_idle_a`/`bz_m_idle_b`, 6402 in Includes_Bezel) runs at `Skin.String(bz_at_midlefade)`: steps 1–7 = 200/250/300/400/500/600/800 ms, **default 400 ms** (empty|4). Tuner › ALBUM / POSTER › **MM album fade** (slider). bz_flip.py promote guard = fade + 50 ms (default 0.45 s). Separate from A2P (`bz_at_a2pfade`) and WARM art crossfade (`bz_at_mmxfade`). Reset art/everything clears it.
