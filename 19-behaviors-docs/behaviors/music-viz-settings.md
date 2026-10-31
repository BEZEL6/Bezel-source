# Music OSD / viz settings

**Object:** `Custom_1105_MusicOSDSettings.xml` dialog `1105` · grouplist `5000` · `5001`,`5002`,`5004–5009`  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## Rows
Hide background fanart 5001 (`hide_background_fanart`) · Animate fanart 5002 (`animate_background_fanart`) · Choose visualisation 5004 · Viz settings 5005 · Presets 5006 (if `Visualisation.HasPresets`) · Lyrics add-on 5007 (`LyricScript_Path`) · Lyrics settings 5008 · Get more 5009 (close all → viz repo).

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move; top/bottom stay (onup/ondown = 5000) |
| Select | Toggle / run row |
| Back | Close |

## Note
Per-viz parameter stepping in BEZEL lives in Music controls 1115 (`bz_vizset.py`, rows 6420–6429), not here.

## Related
music-controls.md · fanart-fs.md
