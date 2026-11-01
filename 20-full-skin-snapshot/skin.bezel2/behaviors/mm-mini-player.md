# MM mini-player

**Object:** `Includes_Bezel.xml` audio row `6957` Prev · `6958` Play/Pause · `6959` Next · `6960` FULL; video group (t4304, `Player.HasVideo`) `6966` Play/Pause · `6967` Stop  
**Where:** Above the MM strip (the strip slides down 120 when `Player.HasMedia`)  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## What it is

**Simple.** While something plays, a small player sits on top of the Main Menu. Press Up from MUSIC to reach it. Down goes back to the strip.

**How it works.** List 6996 is shifted 0,120 by a Conditional slide when `Player.HasMedia`, which frees the top band. 6996 `onup` from the first row goes to `6966` when video plays and to `6958` when audio plays (mm-list.md). WARM 2.0: while audio plays under the MM, the poster lane hides (`bz_mmmushide`, latch ≥ 2.5 s, K22, see mm-warm.md).

## Audio row

**Wiring.** Buttons at top 80, 44×46, no textures. Icon images are 28×28 and a 24×3 white underline shows on focus.
| id | left | Icon | onclick | left / right |
|---|---|---|---|---|
| 6957 | 128 | `np_prev.png` | `PlayerControl(Previous)` | noop / 6958 |
| 6958 | 176 | `np_pause.png` (`!Player.Paused`) / `np_play.png` (Paused) | `PlayerControl(Play)` | 6957 / 6959 |
| 6959 | 224 | `np_next.png` | `PlayerControl(Next)` | 6958 / 6960 |
| 6960 | 286, top 86, 86×34 | label FULL, font `bz_mm17`, `mm_full_ol.png` / `mm_full.png` (border 12, "FULL pill B") | see below | 6959 / noop |

- 6957–6959 extra clicks: 1120 active → `Dialog.Close(1120)`. Otherwise `ClearProperty(bz_np,home)` + `Action(Back)`.
- 6960: 1112 active → `Dialog.Close(1112,true)`. Clear `bz_nav` / `bz_navtune` / `bz_navbez`. `Player.HasVideo` → `ActivateWindow(fullscreenvideo)`, else `ActivateWindow(visualisation)`. From any section, Music included, this lands on real Fanart FS (`MusicVisualisation.xml`) with the `<visualisation>` keymap — no Music bounce (removed t1584).
- A 350×2 divider (40% white) sits at top 140.

## Video group

**Wiring.** Group visible on `Player.HasVideo`, fade-in 200 ms. Poster `VideoPlayer.Art(poster)` 80×120 at 20,12. Title (`bz_mm22b`) at 116,12. Line 2 (`bz_mm17`, AA white) = year · time / duration.
| id | Pos | Label | onclick | left / right |
|---|---|---|---|---|
| 6966 | 112,78 122×44 | `$VAR[BzOSDPlayLbl]` | `PlayerControl(Play)` + the same 1120 / `bz_np` + Back clicks | noop / 6967 |
| 6967 | 242,78 122×44 | Stop | `PlayerControl(Stop)` only | 6966 / noop |
Focus shows a `mm_round.png` pill (border 20, 150 ms fade). Without focus there is a faint 1 px underline. Text F0 white, focused `FF23160E`.

## Keys (all buttons)

| Key | Behavior |
|---|---|
| Up | noop |
| Down | 6996 |
| Back | clear `bz_nav` / `bz_navtune` / `bz_navbez` (close MM) → 60 |

## Related
mm-list.md · np-bar.md · mm-warm.md
