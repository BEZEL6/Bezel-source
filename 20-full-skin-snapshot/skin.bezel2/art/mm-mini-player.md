# MM mini-player — mm-mini-player

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `mm-mini-player` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/mm-mini-player.md) · [layout](../layout/mm-mini-player.md) · [state](../state/mm-mini-player.md) · [motion](../motion/mm-mini-player.md) · [art](../art/mm-mini-player.md) · [input](../input/mm-mini-player.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
While something plays, a small player sits on top of the Main Menu. Press Up from MUSIC to reach it. Down goes back to the strip.

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/mm_full.png` | 86×34 | xml/Includes_Bezel.xml |
| `bezel/mm_full_ol.png` | 86×34 | xml/Includes_Bezel.xml |
| `bezel/mm_round.png` | 64×64 | xml/Custom_1116_PauseScreen.xml, xml/Includes_Bezel.xml, xml/VideoOSD.xml |
| `bezel/mm_round_a60.png` | 64×64 | xml/Custom_1107_SearchDialog.xml, xml/DialogAddonSettings.xml, xml/DialogMediaSource.xml, xml/DialogNumeric.xml |
| `bezel/np_next.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml |
| `bezel/np_pause.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml, xml/VideoOSD.xml |
| `bezel/np_pill32.png` | 64×32 | xml/Custom_1117_MediaSources.xml, xml/Custom_1121_MusicFanartFS.xml, xml/Custom_1130_BzSettings.xml, xml/Custom_1131_BzAddons.xml |
| `bezel/np_play.png` | 96×96 | xml/Includes_Bezel.xml |
| `bezel/np_prev.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/mm-mini-player.md) line refs. Global inventory: [media-map](media-map.md).
