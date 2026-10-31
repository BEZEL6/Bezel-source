# Fanart FS (visualisation)

**Object:** `MusicVisualisation.xml` · default `6390` · fan art pill `6391` (fanart only) · **big album pill `6401`** (album viz) · bounce/redirect `6297`,`6299`,`6385`,`60` · sides `6407`/`6408`, `6409`/`6410`  
**Last updated:** 2026-10-31 · big album pill on album viz · sides fade 3s/2s · live (code-only; not zipped)  
**Status:** draft — fan art pill `6391` + big album pill `6401` (album viz / `bz_dfs_mode`). Select single=pause / double=FS album viz

## Open / close
Fullscreen music (viz). Window: Kodi `visualisation` / `MusicVisualisation.xml`.

## Keys (Rob correction, Oct 31 2026)
| Key | Behavior |
|-----|----------|
| Up | Plain FS (`bz_pnoff=1`): fan art pill `6391`. Album viz (`bz_pnoff` cleared): big album pill `6401` |
| Select / Enter (on 6390, pill unfocused) | **Single tap:** play/pause after ~1 s · **Double tap:** full screen album viz (`ClearProperty(bz_pnoff)` — centered album; sides follow big album pill / `bz_dfs_mode`; no NextPreset) |
| Left / Right (on 6390, pill unfocused) | Previous / next song |
| On fan art pill: Select / L / R | Cycle mode (Controls: Select opens 1115) |
| Down on fan art pill | **Only when mode = Controls:** Music controls 1115; otherwise back to 6390 |
| M / RED | Open Music controls 1115 (viz-scoped keymap) |

Pause / prev / next: Select pause on fanart, L/R songs, or fan art pill → Controls (1115), or **M / RED**. Play Next mode (sides on): Select still pause; L/R prev/next.

## Keymap (profile)
Source: `resources/keymaps/bezel2_np_tab.xml` → installed `zz_bezel2_np_tab.xml`.
`<visualisation>` section: routes pad/Select to plain nav so **6390** owns them; **M/RED → ActivateWindow(1115)**; Back → `SetFocus(6297)`. Single/double Select, cycle, Down-on-Controls, L/R-prev-next live on controls in `Includes_Bezel` (`bz_vdtap` 1 s window).
Installed/refreshed by `bz_cmd.py keymap` (Music + MusicVisualisation onload).

## Touch
Tap big album (6409) → Play Next; tap fanart → Up Next list (bz_npmode=upnext).

## Fan art pill 6391 (bound to Fanart FS)
**Naming:** Call control `6391` the **fan art pill** going forward (not “cycle pill” / “FS pill”). ID stays `6391`.
**Canonical fan art pill** (Oct 31 2026 bind): control `6391` in `BezelNPInPlace`, string `bz_npmode`. Visible only in full screen **fanart** (`bz_pnoff=1` on visualisation). Hidden in full screen **album viz** (`bz_pnoff` cleared) — big album pill `6401` owns that mode.

Select cycles `bz_npmode` vis → bio → fanart → lyrics → upnext → controls and flashes `bz_npmlabel` for 2 s. In controls mode Select opens 1115. Down → 1115 **only** when `$EXP[bz_npm_ctl]`; else 6390. Up → 6390. Left/Right in viz = cycle (SendClick 6391); otherwise Left → 6390, Right → 6392.

## 6390 Select (code)
Normal FS (`bz_pnoff=1`): first Select arms `AlarmClock(bz_vdtapgo,PlayerControl(Play),1s)` then `bz_vdtap=1`; second Select within window cancels alarm and runs `ClearProperty(bz_pnoff,home)` (FS album viz / Play Next sides on). `bz_vdtap` cleared after 1 s. No `Action(NextPreset)`. Play Next (`bz_pnoff≠1`): Select = pause (immediate). Left/Right in viz = PlayerControl Previous/Next.

## Window props (code)
- **onload:** coming from music / musicplaylist / 1112 → `bz_fsbounce` (1 s), `bz_cmd.py vistoggle`, `ReplaceWindow(Music)` (bounce back). Always: `bz_cmd.py keymap`, `bz_pnoff=1` (Play Next sides off), default `bz_dfs_mode=album`. Opened fresh: `bz_fsnp`, `bz_np`, `AlarmClock` SetFocus(6390), start `bz_flip` if not running, `bz_sway_restart`.
- **onunload:** clears `bz_np` if `bz_fsnp`; if MM is closed, focuses 60; clears `bz_fsnp`/`bz_pnoff`/`bz_pnfoc`/`bz_vdtap`; sets `bz_gridret` for 1 s.
- Focus guards: 6297/6385/60 bounce to 6390, and 6299 = clear `bz_np` + Back.

## Play Next / album viz sides (code)
`bz_pnoff=1` = plain Fanart FS (sides off). Double-Select / 6409 clears `bz_pnoff` → album viz. **Big album pill `6401`** (include `BezelBigAlbumPill`) shows upper-right while `!bz_pnoff`; toggles `bz_dfs_mode` ALBUM ↔ PREV/NEXT. `BezelFSPlayNext` sides param = `!album` (match 1120). 6407/6408 = PlayOffset ∓1 when PREV/NEXT + track exists. Side fade-in: **3 s delay, 2 s fade**. Fan art pill `6391` remains in the window.


## Code notes
Rob voice Oct 31 2026: viz-scoped keymap; Down only in Controls; M/RED→1115; L/R on 6390 = prev/next song; Select single=pause, double=FS album viz only (ClearProperty bz_pnoff; pill unfocused). NextPreset removed from double-tap path.

## Related
big-album-pill.md · play-next.md · fullscreen-pill.md · music-controls.md · keymaps.md

## Naming (Oct 31 2026)
- **Fan art pill** = `6391` only (6-mode `bz_npmode`) — full screen **fanart** only (hidden in album viz).
- **Big album pill** = `6401` / `bz_dfs_mode` on Dialogue FS **and** FS album viz (shared `BezelBigAlbumPill`). Same position and toggle behavior.
