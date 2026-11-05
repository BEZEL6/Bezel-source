# Skin settings / BEZEL Tuner — skin-settings-tuner

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `skin-settings-tuner` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/skin-settings-tuner.md) · [layout](../layout/skin-settings-tuner.md) · [state](../state/skin-settings-tuner.md) · [motion](../motion/skin-settings-tuner.md) · [art](../art/skin-settings-tuner.md) · [input](../input/skin-settings-tuner.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

**See screen:** [skin-settings-tuner baselines](../port-refs/skin-settings-tuner/) — smoke baseline + port diff target.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/info/mm_autohide.png` | 880×580 | xml/Includes_Tuner.xml |
| `bezel/mm_pill.png` | 92×46 | xml/Custom_1115_MusicControls.xml, xml/Includes_BezelDialogs.xml, xml/Includes_Buttons.xml, xml/Includes_DialogSelect.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/skin-settings-tuner.md) line refs. Global inventory: [media-map](media-map.md).
