# Fanart FS (visualisation)

**Object:** `MusicVisualisation.xml` · default `6390` · FS pill `6391` · bounce/redirect buttons `6297`,`6299`,`6385`,`60` · Play Next sides `6407`/`6408`, `6409`/`6410`  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — matches live 5.33.194 (IDs/files re-verified Oct 31); not Rob-approved, not re-smoked

## Open / close
Fullscreen music (viz).

## Keys (Rob correction, 5.33.172 / BUG-022)
| Key | Behavior |
|-----|----------|
| Up | Focus cycle pill (6391) |
| Select | Cycle pill mode |
| Left/Right | Cycle pill mode |
| On pill: Select / L / R | Cycle mode (Controls: Select/Down opens 1115) |
| Down on pill | Music controls 1115 |

Pause / prev / next: via pill → Controls (1115) or M / RED. Old map (5.33.138: Select pause, double-Select Play Next, L/R songs) retired.
Viz Play Next mode (sides active) keeps Select pause, L/R prev/next.

## Touch
Tap big album (6409) → Play Next; tap fanart → Up Next list (bz_npmode=upnext).

## Pill 6391 (code)
Select cycles `bz_npmode` vis → bio → fanart → lyrics → upnext → controls and flashes `bz_npmlabel` for 2 s. In controls mode Select opens 1115. Down → 1115 in controls/viz mode, else 6390. Up → 6390. Left/Right in viz = cycle (SendClick 6391); otherwise Left → 6390, Right → 6392.
6390 Select in viz toggles `bz_pnfoc=6403` (pause ghost).

## Window props (code)
- **onload:** coming from music / musicplaylist / 1112 → `bz_fsbounce` (1 s), `bz_cmd.py vistoggle`, `ReplaceWindow(Music)` (bounce back). Always: `bz_cmd.py keymap`, `bz_pnoff=1` (Play Next sides off), default `bz_dfs_mode=album`. Opened fresh: `bz_fsnp`, `bz_np`, start `bz_flip` if not running, `bz_sway_restart`.
- **onunload:** clears `bz_np` if `bz_fsnp`; if MM is closed, focuses 60; clears `bz_fsnp`/`bz_pnoff`/`bz_pnfoc`/`bz_vdtap`; sets `bz_gridret` for 1 s.
- Focus guards: 6297/6385/60 bounce to 6390, and 6299 = clear `bz_np` + Back.

## Play Next sides (code)
`bz_pnoff=1` = off. 6409 clears it (sides on), 6410 → `bz_npmode=upnext`. 6407/6408 = PlayOffset ∓1, visible only when that track exists.

## Code notes
Rob memory + MusicVisualisation.xml (re-read Oct 31).

## Related
play-next.md · fullscreen-pill.md · music-controls.md
