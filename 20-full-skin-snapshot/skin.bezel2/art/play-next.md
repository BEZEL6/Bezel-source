# Play Next (1120 non-album mode) — play-next

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `play-next` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/play-next.md) · [layout](../layout/play-next.md) · [state](../state/play-next.md) · [motion](../motion/play-next.md) · [art](../art/play-next.md) · [input](../input/play-next.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/mm_pill.png` | 92×46 | xml/Custom_1115_MusicControls.xml, xml/Includes_BezelDialogs.xml, xml/Includes_Buttons.xml, xml/Includes_DialogSelect.xml |
| `bezel/np_pill32.png` | 64×32 | xml/Custom_1117_MediaSources.xml, xml/Custom_1121_MusicFanartFS.xml, xml/Custom_1130_BzSettings.xml, xml/Custom_1131_BzAddons.xml |
| `bezel/np_playlist.png` | 96×96 | xml/Custom_1115_MusicControls.xml |
| `bezel/np_prev.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml |
| `bezel/np_repeat.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml |
| `bezel/np_rew.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/VideoOSD.xml |
| `bezel/np_shuffle.png` | 96×96 | xml/Custom_1115_MusicControls.xml |
| `bezel/np_stop.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/VideoOSD.xml |
| `bezel/view_ic_grid.png` | 20×20 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/play-next.md) line refs. Global inventory: [media-map](media-map.md).
