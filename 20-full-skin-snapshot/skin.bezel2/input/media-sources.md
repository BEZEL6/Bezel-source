# Media sources — media-sources

**Object:** `media-sources` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/media-sources.md) · [layout](../layout/media-sources.md) · [state](../state/media-sources.md) · [motion](../motion/media-sources.md) · [art](../art/media-sources.md) · [input](../input/media-sources.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
MEDIA SOURCES in the Main Menu opens a BEZEL page with Videos, Music and Pictures sources and their library tools. Pick one to open Kodi's sources for it. Back from there returns to this page on the same row. Back here opens the Main Menu.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/media-sources.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 120 | `` | `` | `100` | `140` | `` |
| 300 | `8` | `9603` | `9603` | `9603` | `` |
| 312 | `9601` | `9601` | `9601` | `9601` | `` |
| 6299 | `60` | `60` | `60` | `60` | `` |
| 7100 | `noop` | `noop` | `7131` | `7101` | `SetProperty(bz_nav,true,home)` |
| 7101 | `noop` | `noop` | `7100` | `7102` | `SetProperty(bz_nav,true,home)` |
| 7102 | `noop` | `noop` | `7101` | `7103` | `SetProperty(bz_nav,true,home)` |
| 7103 | `noop` | `noop` | `7102` | `7104` | `SetProperty(bz_nav,true,home)` |
| 7104 | `noop` | `noop` | `7103` | `7105` | `SetProperty(bz_nav,true,home)` |
| 7105 | `noop` | `noop` | `7104` | `7106` | `SetProperty(bz_nav,true,home)` |
| 7111 | `noop` | `noop` | `7110` | `7112` | `SetProperty(bz_nav,true,home)` |
| 7112 | `noop` | `noop` | `7111` | `7113` | `SetProperty(bz_nav,true,home)` |
| 7114 | `noop` | `noop` | `7113` | `7115` | `SetProperty(bz_nav,true,home)` |
| 7115 | `noop` | `noop` | `7114` | `7116` | `SetProperty(bz_nav,true,home)` |
| 7121 | `noop` | `noop` | `7120` | `7130` | `SetProperty(bz_nav,true,home)` |
| 7131 | `RunScript(special://skin/scripts/bz_set.py,cyc,videolibrary.` | `RunScript(special://skin/scripts/bz_set.py,cyc,videolibrary.` | `7130` | `7100` | `SetProperty(bz_nav,true,home)` |
| 9130 | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Contain` | `RunScript(special://skin/scripts/bz_set.py,cyc,$INFO[Contain` | `9130` | `9130` | `ClearProperty(bz_setx,home)` |
| 9150 | `noop` | `noop` | `9150` | `9150` | `Dialog.Close(1132)` |
| 9601 | `SetProperty(bz_kbcaps,1,home)` | `9602` | `9601` | `9601` | `` |
| 9602 | `9601` | `9603` | `9602` | `9602` | `` |
| 9603 | `9602` | `300` | `9603` | `9603` | `` |

**Semantics from behavior (verbatim lines):**
- Simple.** MEDIA SOURCES in the Main Menu opens a BEZEL page with Videos, Music and Pictures sources and their library tools. Pick one to open Kodi's sources for it. Back from there returns to this page on the same row. Back here opens the Main Menu.
- Simple.** Up and Down move through the rows and wrap. Left or Right goes to CANCEL / SETTINGS. Back opens the Main Menu.
- 7101: `bz_msret=1`, `bz_msfocus=7101`, `ActivateWindow(Videos,sources://video/,return)`. `onup` 7121 (wrap), `ondown` 7102, left/right 9001. Rows: 7101 VIDEOS SOURCES… · 7102 Update library · 7103 Clean library · 7104 Export library · 7105 Import library (`MediaSettings,library`) · 7111 MUSIC SOURCES… (`Music,sources://music/,return`) · 7112–7115 the same four library rows for music · 7121 PICTURES SOURCES… (`Pictures,sources://pictures/,return`). I did not re-trace the per-row actions of 7102–7104 / 7112–7114 for this doc.
- Back → MM unchanged. FileBrowser / add-source dialog are still stock.
- Art behind the strip:** 1117 draws the held MM warm lane (`bz_fan_a` / `bz_fan_b` by `bz_fan_side`, shown while `bz_fan_on` is set) at 120,120 840×900, right after `BezelStdFrame`, under the strip chrome. Same Tuner Fanart opacity (`bz_at_fanop`) as BezelFanartLayer. Not gated on `bz_navmenu`, so the art the MM row showed stays up after the window opens (it used to go black: StdFrame cover + empty `bz_backdrop`).
- Keys:** every row has explicit `onup`/`ondown` with `bz_msx` conditions. The grouplist of wrapper groups did not move focus on its own (Down was stuck on VIDEOS). Order: VIDEOS → (its 6 rows if open) → MUSIC → (6 rows if open) → PICTURES → (SOURCES if open) → ADD SOURCE → LIBRARY SCAN → wraps to VIDEOS. Select on a header opens or closes its rows. Left/Right do nothing except change ‹VALUE› pills.
- Simple.** Editing a path or the name in the Add Source dialog no longer opens Kodi's full-screen keyboard. A dark vbar keyboard slides in to the LEFT of the colour strip (x170–550, y120–1020); the strip stays put and the MM art stays behind.
- How it works.** `DialogKeyboard.xml` picks `BzStripKeyboard` while `Window.IsVisible(mediasource)` (and not musicinformation). Three wraplist bars float with the focused letter big in the centre: A–Z `9601`, 0–9 `9602`, symbols `9603` (`/ : . _ - @ \ ! # $ % & + = ?`). Up/Down slides a bar, Left/Right switches bars. Select runs `scripts/bz_kb.py <a|n|s>,<index>`, which reads the edit text (`Control.GetLabel(312).index(1)`) and sends text+char with JSON `Input.SendText` (done=false). Pills: SPACE (Kodi `32`), ← DEL (Kodi `8`), DONE (Kodi `300`, closes and writes the field). Caps: Left on A–Z `9601` toggles Home `bz_kbcaps` (letters show case; cleared on unload; caps pill removed 5.33.231). Back = cancel.
- Wiring.** Focus on open: `onload SetFocus(9601)` (mediasource only). Nav: A–Z Left = caps toggle (stays on bar); symbols Right → DONE (Select it to return to the strip); pills Up → bars, Down → bars (SPACE→A–Z, DEL→0–9, DONE→symbols); SPACE Left → DONE. Edit `312`/heading `311` are Kodi's own. Slide-in 300ms from the strip edge + fade; fade-out 200ms. Stock popup open/close anim skipped for mediasource. Source generated by `/workspace/b401/gen_kb229.py` into `Includes_BezelDialogs.xml`. Every other keyboard use is unchanged (BzStdKeyboard / BzRefreshKeyboard).
- Right panel (x1010+) shows no art (`showart=false`).
- SOURCES »** (7101 video / 7111 music / 7121 pictures) no longer opens Kodi's stock sources window. It sets `bz_srcpath` (`sources://video|music|pictures/`), `bz_srcwin` (Videos/Music/Pictures), `bz_srclab`, then opens dialog **1132** (`Custom_1132_BzSources.xml`): Warm strip box, title SOURCES, sub "MEDIA SOURCES · <type>", list 9150 filled from `<content>$INFO[bz_srcpath]</content>`, Bezel hi bar, » per row. 1132 has no window fade, no full-screen dim and no strip chrome of its own: 1117's strip chrome stays up underneath, only 1117's title/sub labels and grouplist 9000 hide while 1132 is active (5.33.243 — no blink, no double dim).
- Select a source → sets `bz_msret=1`, `ActivateWindow(<bz_srcwin>,<source path>,return)`, THEN `Dialog.Close(1132)` (nav before close, 5.33.243 — 1117 never draws a frame between); Back from that media window returns to 1117 (existing msret path). Back in 1132 → 1117 (same row).
