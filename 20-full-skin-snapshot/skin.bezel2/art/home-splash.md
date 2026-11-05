# Home / startup splash — home-splash

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `home-splash` · **Layer:** art (media) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/home-splash.md) · [layout](../layout/home-splash.md) · [state](../state/home-splash.md) · [motion](../motion/home-splash.md) · [art](../art/home-splash.md) · [input](../input/home-splash.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
At start, a splash covers the screen while BEZEL builds its windows and warms artwork. It stays at least 5 s and at most 15 s, then fades over 3 s straight onto the Main Menu. Nothing pops and nothing flashes blank.

**This layer in one line:** every image file this object draws, its pixel size, and which windows use it.

**See screen:** [home-splash baselines](../port-refs/home-splash/) — smoke baseline + port diff target.

## Deep (rebuild detail)
| path | px | used in |
|---|---|---|
| `bezel/logo.png` | 256×256 | xml/DialogNotification.xml, xml/Includes.xml, xml/Includes_Bezel.xml, xml/Includes_DialogSelect.xml |
| `bezel/white.png` | 8×8 | xml/AddonBrowser.xml, xml/Custom_1107_SearchDialog.xml, xml/Custom_1115_MusicControls.xml, xml/Custom_1116_PauseScreen.xml |

colordiffuse/mask per control: see texture tags in live XML at the [layout](../layout/home-splash.md) line refs. Global inventory: [media-map](media-map.md).
