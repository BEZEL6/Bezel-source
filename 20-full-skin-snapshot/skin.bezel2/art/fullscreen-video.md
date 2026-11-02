# Fullscreen video — fullscreen-video

**Object:** `fullscreen-video` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/fullscreen-video.md) · [layout](../layout/fullscreen-video.md) · [state](../state/fullscreen-video.md) · [motion](../motion/fullscreen-video.md) · [art](../art/fullscreen-video.md) · [input](../input/fullscreen-video.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Plain full-screen video with BEZEL chrome. Video starts in fullscreen. Select pauses and shows the controls. Back peels away whatever is on screen one layer at a time, and only then stops.

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/mm_round.png` | 64×64 | xml/Custom_1116_PauseScreen.xml, xml/Includes_Bezel.xml, xml/VideoOSD.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/fullscreen-video.md) line refs. Global inventory: [media-map](media-map.md).
