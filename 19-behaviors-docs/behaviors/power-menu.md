# Power menu

**Object:** `Custom_1118_PowerMenu.xml` dialog `1118` (zorder 2) · list `7800` (SHUTDOWN / QUIT KODI / SUSPEND / SLEEP / TUNER)  
**Last updated:** 2026-10-31 · 5.33.203 (code; not shipped)
**Status:** draft — first-Down handoff fix in tree (not Rob-smoked, not zipped)

## Open / close
Select POWER in MM. onload clears `bz_tunesrc` and sets `bz_pwrswap` (swap animation). onunload: unless `bz_tunesrc=pwr`, it refocuses MM strip `6996`, then clears `bz_pwrswap` after 1 s.


## Focus (5.33.203)
Opens over MM with 6996 hidden the same frame. `defaultcontrol` is **7800** without `always="true"`. Onload also runs `SetFocus(7800,0,absolute)` so list focus is real on SHUTDOWN before the first Down — avoids the handoff that ate the first Down (Shutdown looked focused, Quit needed a second press).

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Rows of 7800 |
| Left / Right | noop |
| Select | SHUTDOWN `Shutdown()` · QUIT KODI `Quit()` · SUSPEND / SLEEP `Suspend()` · TUNER (below) |
| Back | `bz_nav=true` → close back to MM |

## TUNER row (BUG-005, 5.33.150)
4th list item with the same item/focused layout as the other rows (outline = `BzATHiTex` image in focusedlayout). There is no separate button 7801. A decorative separator sits between rows 3 and 4. Select: `bz_tunesrc=pwr`, `bz_navtune=true`, clears `bz_navbez`/`bz_navset`, closes 1118 and focuses Tuner `6970`.

## Touch
None specified.

## Related
mm-list.md · skin-settings-tuner.md
