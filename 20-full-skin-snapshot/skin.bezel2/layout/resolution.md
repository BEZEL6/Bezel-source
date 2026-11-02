# Design resolution & anchors

**Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Bezel is drawn on a fixed **1920×1080 (16:9)** canvas; Kodi scales it to the screen. Every x/y/w/h in `layout/` is in these units. A port should lay out on the same virtual canvas and scale uniformly (letterbox other aspects) so coords copy 1:1.

## Deep (rebuild detail)
### addon.xml `<res>` entries (all use folder `xml`)
| w×h | aspect | default |
|---|---|---|
| 1920×1080 | 16:9 | **true** |
| 1920×1440 | 4:3 | — |
| 1920×1280 | 3:2 | — |
| 1920×1200 | 16:10 | — |
| 2040×1080 | 17:9 | — |
| 2160×1080 | 18:9 | — |
| 2338×1080 | 19.5:9 | — |
| 2560×1080 | 21:9 | — |
All share one xml folder → layouts are authored at 1920×1080; other aspects get extra width/height, not re-layout.

### Coordinate model (Kodi → native)
- Origin top-left; `left/top` relative to parent group; `right/bottom` = inset from parent edge. Groups without w/h fill parent.
- `camera x y` on a group = 3D vanishing point for rotatex/rotatey inside it (default = screen centre 960,540).
- `center="x,y"` on zoom/rotate = pivot in absolute canvas units.
- `aspectratio scale|keep|stretch` + `align` = content mode (fill/fit) + alignment.

### Common anchors
| anchor | value | used by |
|---|---|---|
| Big album rect | 1140,220 600×600 | music-list, idle-big-album-fold, glare |
| Album slit | x1440 (camera 1440,520) | idle-big-album-fold |
| Big album zoom centre | 1440,420 | music-list |
| Art column constant `bz_art_x` | 990 (+ `bz_top`, `bz_h`) | mm-warm underlay art |
| Tuner info panel | x≈1010+, ~860×560 | skin-settings-tuner |
| MM strip | control 6996 | mm-list (see layout/mm-list.md) |
| Section list | control 60 (Music/Movies/TV) | *-list |
