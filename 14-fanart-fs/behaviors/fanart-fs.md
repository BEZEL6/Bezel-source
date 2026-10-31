# Fanart FS (visualisation)

**Object:** `MusicVisualisation.xml` · default `6390` · FS pill `6391` · bounce/redirect buttons `6297`,`6299`,`6385`,`60` · Play Next sides `6407`/`6408`, `6409`/`6410`  
**Last updated:** 2026-10-31 · live (code-only; not zipped)  
**Status:** draft — matches live after Fanart FS viz keymap + L/R-on-6390 prev/next; not Rob-approved, not re-smoked

## Open / close
Fullscreen music (viz). Window: Kodi `visualisation` / `MusicVisualisation.xml`.

## Keys (Rob correction, 5.33.172 / BUG-022 + viz-scoped map + Oct 31 L/R)
| Key | Behavior |
|-----|----------|
| Up | Focus cycle pill (6391) |
| Select (on 6390) | Cycle pill mode (normal FS); Play Next mode = pause |
| Left / Right (on 6390, pill unfocused) | **Previous / next song** |
| On pill: Select / L / R | Cycle mode (Controls: Select opens 1115) |
| Down on pill | **Only when mode = Controls:** Music controls 1115; otherwise back to 6390 |
| M / RED | Open Music controls 1115 (viz-scoped keymap) |

Pause / prev / next: L/R on fanart (6390), or pill → Controls (1115), or **M / RED**. Old map (5.33.138: Select pause, double-Select Play Next) retired for normal FS Select; Play Next mode still Select pause + L/R skip.

## Keymap (profile)
Source: `resources/keymaps/bezel2_np_tab.xml` → installed `zz_bezel2_np_tab.xml`.
`<visualisation>` section only: routes pad/Select to plain nav so **6390** owns them; **M/RED → ActivateWindow(1115)**; Back → `SetFocus(6297)`. Cycle / Down-on-Controls / L/R-prev-next live on controls in `Includes_Bezel`, not in the keymap XML.
Installed/refreshed by `bz_cmd.py keymap` (Music + MusicVisualisation onload).

## Touch
Tap big album (6409) → Play Next; tap fanart → Up Next list (bz_npmode=upnext).

## Pill 6391 (code)
Select cycles `bz_npmode` vis → bio → fanart → lyrics → upnext → controls and flashes `bz_npmlabel` for 2 s. In controls mode Select opens 1115. Down → 1115 **only** when `$EXP[bz_npm_ctl]`; else 6390. Up → 6390. Left/Right in viz = cycle (SendClick 6391); otherwise Left → 6390, Right → 6392.
6390 Select in viz + Play Next toggles pause; normal FS Select = SendClick(6391). 6390 Left/Right in viz = PlayerControl Previous/Next (pill unfocused).

## Window props (code)
- **onload:** coming from music / musicplaylist / 1112 → `bz_fsbounce` (1 s), `bz_cmd.py vistoggle`, `ReplaceWindow(Music)` (bounce back). Always: `bz_cmd.py keymap`, `bz_pnoff=1` (Play Next sides off), default `bz_dfs_mode=album`. Opened fresh: `bz_fsnp`, `bz_np`, `AlarmClock` SetFocus(6390), start `bz_flip` if not running, `bz_sway_restart`.
- **onunload:** clears `bz_np` if `bz_fsnp`; if MM is closed, focuses 60; clears `bz_fsnp`/`bz_pnoff`/`bz_pnfoc`/`bz_vdtap`; sets `bz_gridret` for 1 s.
- Focus guards: 6297/6385/60 bounce to 6390, and 6299 = clear `bz_np` + Back.

## Play Next sides (code)
`bz_pnoff=1` = off. 6409 clears it (sides on), 6410 → `bz_npmode=upnext`. 6407/6408 = PlayOffset ∓1, visible only when that track exists.

## Code notes
Rob voice Oct 31 2026: viz-scoped keymap + Down only in Controls mode + M/RED in FS; L/R on 6390 (pill unfocused) = prev/next.

## Related
play-next.md · fullscreen-pill.md · music-controls.md · keymaps.md
