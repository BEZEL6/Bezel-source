# Music controls (dialog 1115) — music-controls

**Object:** `music-controls` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-controls.md) · [layout](../layout/music-controls.md) · [state](../state/music-controls.md) · [motion](../motion/music-controls.md) · [art](../art/music-controls.md) · [input](../input/music-controls.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
The music controls panel is the "remote control" menu for music: play/pause, skip, shuffle, repeat, Up next, choose a visualisation, tweak its settings, or jump to the Tuner. It opens automatically when Kodi would show its music OSD, and from the fan art pill or the music list. Left always closes it.

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/mm_pill.png` | 92×46 | xml/Custom_1115_MusicControls.xml, xml/Includes_BezelDialogs.xml, xml/Includes_Buttons.xml, xml/Includes_DialogSelect.xml |
| `bezel/np_ff.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/VideoOSD.xml |
| `bezel/np_next.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml |
| `bezel/np_pill32.png` | 64×32 | xml/Custom_1117_MediaSources.xml, xml/Custom_1121_MusicFanartFS.xml, xml/Custom_1130_BzSettings.xml, xml/Custom_1131_BzAddons.xml |
| `bezel/np_playlist.png` | 96×96 | xml/Custom_1115_MusicControls.xml |
| `bezel/np_prev.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml |
| `bezel/np_repeat.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml |
| `bezel/np_rew.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/VideoOSD.xml |
| `bezel/np_shuffle.png` | 96×96 | xml/Custom_1115_MusicControls.xml |
| `bezel/np_stop.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/VideoOSD.xml |
| `bezel/view_ic_grid.png` | 20×20 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/music-controls.md) line refs. Global inventory: [media-map](media-map.md).
