# Touch / tap inputs

**Object:** Cross-object: logo-back button (`Includes_Bezel.xml`), tap targets in `MusicVisualisation.xml` / `Custom_1120_PlayNext.xml`, double-tap service `scripts/bz_dtap.py` + Tuner rows `dtap` / `dtapwin`  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194; touch master toggle NOT found in tree (see below)

## Rule
Touch only does what Rob specified per object; each object's file lists its touch.

## Live touch / tap map
| Where | Tap | Result |
|---|---|---|
| Any window (not FS video/OSD) | Bezel logo | Back (bezel-logo-back.md) |
| Music strip | FS pill 6886 | Fanart FS |
| Fanart FS | Big album / fanart | Play Next / Up Next (fanart-fs.md) |
| 1120 | Prev/next tiles 6405/6406 | Play offset ∓1 |

## Double-tap Select (remote "touch")
Tuner **Double-tap Select = menu** (`dtap` → `bz_dtap_off`) and **Double-tap window** (`dtapwin` → `bz_at_dtapwin`, 15 steps 150–600 ms). While on: one tap = Select after the window; two taps = Options+Info / 1119 / Kodi ContextMenu (context-menu.md). Windows only, never dialogs, keyboard, OSD or FS video.

## Unknown / flagged
Earlier docs said a "Touch master On/Off" lives in the Tuner. No touch master row or skin setting exists in the live tree (grep of Includes_Tuner.xml / scripts). Treat it as not present.

## Related
keymaps.md · skin-settings-tuner.md · context-menu.md
