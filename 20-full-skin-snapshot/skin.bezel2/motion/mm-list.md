# MM list (Main Menu strip) — mm-list

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `mm-list` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/mm-list.md) · [layout](../layout/mm-list.md) · [state](../state/mm-list.md) · [motion](../motion/mm-list.md) · [art](../art/mm-list.md) · [input](../input/mm-list.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Left or Back at the top of a section list, or M, opens the Main Menu with the strip focused. Back closes it. Select opens a destination and closes it.

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

**See screen:** [mm-list baselines](../port-refs/mm-list/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/mm-list.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/mm-list.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|
| 6894 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="1500" tween="sine" easing="inout">Hidden</animation>` |
| 6894 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="0" end="100" time="200" tween="sine" easing="out">Visible</animation>` |
| 6897 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="35" time="350" tween="sine" easing="inout" condition="!ControlGroup($PARAM[group]).HasFocus">Conditional</animation>` |
| 6996 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,120" time="0" condition="Player.HasMedia">Conditional</animation>` |
| 6996 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="-390,0" end="0,0" time="210" tween="cubic" easing="out" condition="String.IsEmpty(Window(Home).Property(bz_pwrswap))">Visible</animation>` |
| 6996 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="390,0" time="180" tween="cubic" easing="in" condition="!Window.IsVisible(1118) + String.IsEmpty(Window(Home).Property(bz_pwrswap))">Hidden</animation>` |

**Timings named in behavior:** 1500 ms, 180 ms, 200 ms, 210 ms, 300 ms, 600 ms
