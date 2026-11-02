# MM list (Main Menu strip) — mm-list

**Object:** `mm-list` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/mm-list.md) · [layout](../layout/mm-list.md) · [state](../state/mm-list.md) · [motion](../motion/mm-list.md) · [art](../art/mm-list.md) · [input](../input/mm-list.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Left or Back at the top of a section list, or M, opens the Main Menu with the strip focused. Back closes it. Select opens a destination and closes it.

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

**See screen:** [mm-list baselines](../port-refs/mm-list/) — smoke baseline + port diff target.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/info/mm_autohide.png` | 880×580 | xml/Includes_Tuner.xml |
| `bezel/mm_full_ol.png` | 86×34 | xml/Includes_Bezel.xml |
| `bezel/mm_pill.png` | 92×46 | xml/Custom_1115_MusicControls.xml, xml/Includes_BezelDialogs.xml, xml/Includes_Buttons.xml, xml/Includes_DialogSelect.xml |
| `bezel/mm_round.png` | 64×64 | xml/Custom_1116_PauseScreen.xml, xml/Includes_Bezel.xml, xml/VideoOSD.xml |
| `bezel/mm_round_a60.png` | 64×64 | xml/Custom_1107_SearchDialog.xml, xml/DialogAddonSettings.xml, xml/DialogMediaSource.xml, xml/DialogNumeric.xml |
| `bezel/mm_strip_shadow_c.png` | 470×980 | xml/Includes_Bezel.xml |
| `bezel/np_next.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml |
| `bezel/np_pause.png` | 96×96 | xml/Custom_1115_MusicControls.xml, xml/Includes_Bezel.xml, xml/VideoOSD.xml |
| `bezel/np_play.png` | 96×96 | xml/Includes_Bezel.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/mm-list.md) line refs. Global inventory: [media-map](media-map.md).
