# Media sources

**Object:** `Custom_1117_MediaSources.xml` window `1117` · group `9000` buttons `7101–7121`, grouplist `9001` (`9101` CANCEL, `9102` SETTINGS), focus bounce `6299`  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
BEZEL library/sources hub opened from MM MEDIA SOURCES. onload clears `bz_msret`. It restores focus to `bz_msfocus` (1 s alarm) or defaults to 7101.

## Rows (column 9000, Up/Down wraps 7121 ↔ 7101)
VIDEOS SOURCES… 7101 · Update 7102 · Clean 7103 · Export 7104 · Import 7105 (MediaSettings,library) · MUSIC SOURCES… 7111 · Update/Clean/Export/Import 7112–7115 · PICTURES SOURCES… 7121.
The SOURCES rows set `bz_msret=1` and `bz_msfocus=<id>`, then open `sources://video|music|pictures/` with `return`.

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move rows (wraps) |
| Left / Right | Switch 9000 ↔ 9001 |
| Select | Row action / CANCEL closes / SETTINGS → MediaSettings |
| Back | Straight to MM (`bz_nav=true`, 5.33.179 BUG-024) |

## Related
mm-list.md · settings.md · filebrowser.md
