# MM warm (WARM 2.0.1) — LOCKED — mm-warm

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `mm-warm` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/mm-warm.md) · [layout](../layout/mm-warm.md) · [state](../state/mm-warm.md) · [motion](../motion/mm-warm.md) · [art](../art/mm-warm.md) · [input](../input/mm-warm.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
These are the fixed numbers and switches for the whole warm system.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

**See screen:** [mm-warm baselines](../port-refs/mm-warm/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/mm-warm.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 100 | `` | `` | `304` | `120` | `` |
| 124 | `` | `` | `104` | `144` | `` |
| 300 | `8` | `9603` | `9603` | `9603` | `` |
| 6996 | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMPrev_music])` | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMNext_music])` | `6966` | `SetFocus(6996,0,absolute)` | `` |

**Semantics from behavior (verbatim lines):**
- | Music underlay guard | `Home.bz_music_underlay=1` is set whenever a music warm starts. Select goes back to `Home.bz_lastmusic` | `mm_warm` |
- | Section swap | Fade-in only. `bz_arthold` holds the art, then `_arel` releases it once the new list has an item and family art: up to 45 × 20 ms ≈ 0.9 s, and after 30 tries (about 0.6 s) it stops waiting for art. No `bz_xfin`/`bz_xfade` dim-out | `_ahold`/`_arel` |
- 5.33.218:** window-switch warm (Music/Movies/TV via ActivateWindow) now waits up to 4 s for `Container.FolderPath == path` + `!Container.IsUpdating` + NumItems>0 before `_restore` (load screen may hold longer — intended). Row 0 is a valid row (`r is None` check). `_snap` only saves a row for a section already seeded/restored this session, so an unseeded first pass no longer pins row 0. `_restore` sets `bz_warmrow`=path so the grid sync keeps the list item instead of resetting to item 0. **5.33.219 Music apply path:** when `_restore` runs for Music it also starts `_defer(row)`: a daemon thread (≤120 s) that re-issues `SetFocus(60,row,absolute)` the moment `Control.IsVisible(60)` and `!Container.IsUpdating`, with the same-frame `_bzstrip` bounce while MM is open (strip 6996 keeps focus). It stops when the row lands (`warm2 defer landed`), the folder changes, a Select is made (`bz_mmpick`), or — with MM closed — the user moves the list themselves. Note: `xbmcgui…getControl(60).selectItem()` on a skin container **crashes Kodi** — never use it. Movies/TV land the random row directly.
- `_ab_fanart()`: first non-empty of `Control.GetLabel(9880)` (skipped when `Skin.HasSetting(bezel_norotate)`), `Container(60).ListItem.Art(fanart)`, `…Art(artist.fanart)`, `…Art(albumartist.fanart)`, `…Art(tvshow.fanart)`, `Window(Home).Property(script.grab.fanart.Global.FanArt)`. Movies only: falls back to `Home.bz_movfanart_hold`.
- 2. `bz_nav=true` → `$EXP[bz_navmenu]` true. Section twins drop to 0 (no anim). MM front A/B shows at 100 (Visible fade gated off). The back side stays hidden.
- 3. At t ≥ 0.3 s, `bz_ab_live=1`. A target change after that settles 0.25 s, is staged to the back side, waits 0.5 s, flips `bz_<p>_side`, and crossfades over 1500 ms.
- How it works:** Music, Movies, TV and Recently Played use MyMusicNav/MyVideoNav, so the closed-MM music/videos seed covers all three lanes. Search (1107, a dialog) and Media Sources (1117) only draw `BezelFanartLayer`, so only the fan lane is seeded, from `$VAR[BezelFanart]`. Without that seed, the MM would fade up the unfed live twin (fadetime 3000) from black.
- In-place path** (window already active): set `bz_mmwarm=true` and `bz_navroot=path`, clear `bz_xfin`/`bz_xfade`, run `Container.Update(path,replace)`. Loop up to 40 × 25 ms re-asserting `bz_nav=true`, tracking `bz_mmlive` from `Container(6996).Position` and calling `_bzstrip` if focus slips. Exit early after 12 tries once 6996 is focused and the list is not updating. If the path did not land, retry once (another 40 × 25 ms). Then `_restore`. `finally`: `_arel()`, clear `bz_mmwarm` and `bz_xfade`.
- Window-switch path:** set `bz_mmpos = bz_mmlive or pos or '0'` (the new window's onload restores this strip row; FLASH t3430), `bz_mmwarm=true`, `bz_navroot`, then `ActivateWindow(win,path)`. Run `_hold()` up to 80 times (stop after ≥4 once the window is active), each pass setting `bz_nav`, `bz_mmpos` and `bz_mmlive` and re-focusing the strip. Then `Container.Update` if the path differs, up to 20 × 50 ms of focus confirmation, and `_restore`. `finally`: 15 × 20 ms `_hold`, `_arel()`, clear `bz_mmwarm`, `bz_mmpos`, `bz_xfade`.
- Simple:** Come back to a section and you land on the same row you left.
- How it works:** Before every swap, `_snap` saves the leaving section's row, path and backdrop. After the new list settles, `_restore` focuses the saved row on list 60 and then bounces focus straight back to the strip in the same frame, so the menu keeps focus.
- `_restore(s2, p2, spos)`: if there is no row, no pick, the path matches and the list is not updating → `_randrow()` seeds `row/path`. It aborts when `not r` (row 0 or None), `_pk()`, the stored path ≠ `p2`, the current path ≠ `p2`, or the list is updating. Otherwise `SetFocus(60,r,absolute)` and then `_bzstrip(home, bz_mmlive or spos)` (back to 6996).
