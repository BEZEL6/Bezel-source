# Video OSD — video-osd

**Object:** `video-osd` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/video-osd.md) · [layout](../layout/video-osd.md) · [state](../state/video-osd.md) · [motion](../motion/video-osd.md) · [art](../art/video-osd.md) · [input](../input/video-osd.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/mm_pill.png` | 92×46 | xml/Custom_1115_MusicControls.xml, xml/Includes_BezelDialogs.xml, xml/Includes_Buttons.xml, xml/Includes_DialogSelect.xml |
| `bezel/mm_round.png` | 64×64 | xml/Custom_1116_PauseScreen.xml, xml/Includes_Bezel.xml, xml/VideoOSD.xml |
| `bezel/np_fav.png` | 96×96 | xml/Includes_Bezel.xml, xml/VideoOSD.xml |
| `bezel/np_ff.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/VideoOSD.xml |
| `bezel/np_info.png` | 96×96 | xml/Includes_Bezel.xml, xml/VideoOSD.xml |
| `bezel/np_lyrics.png` | 96×96 | xml/VideoOSD.xml |
| `bezel/np_presets.png` | 96×96 | xml/VideoOSD.xml |
| `bezel/np_rew.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/VideoOSD.xml |
| `bezel/np_stop.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/VideoOSD.xml |
| `bezel/np_volume.png` | 96×96 | xml/VideoOSD.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/video-osd.md) line refs. Global inventory: [media-map](media-map.md).
