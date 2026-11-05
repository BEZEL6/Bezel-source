# Recently played — recently-played

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `recently-played` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/recently-played.md) · [layout](../layout/recently-played.md) · [state](../state/recently-played.md) · [motion](../motion/recently-played.md) · [art](../art/recently-played.md) · [input](../input/recently-played.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/recently-played.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/recently-played.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|
| 6097 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,20" time="0" condition="$EXP[bz_artistalbums] + !$EXP[bz_mdiscpick]">Conditional</animation>` |
| 6097 `xml/Includes_Bezel.xml` | `<animation effect="slide" end="0,450" time="0" condition="$EXP[bz_covercol] + !$EXP[bz_allpick]">Conditional</animation>` |
| 6097 `xml/Includes_Bezel.xml` | `<animation effect="slide" end="0,390" time="0" condition="$EXP[bz_allpick]">Conditional</animation>` |
| 6097 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,45" time="0" condition="$EXP[bz_allpick] + String.Contains(Container(60).ListItemAbsolute(1).FolderPath,/-1/)">Conditional</animation>` |
| 6097 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,30" time="0" condition="$EXP[bz_allpick] + Integer.IsEqual(Container(60).NumItems,2)">Conditional</animation>` |
| 6097 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,45" time="0" condition="$EXP[bz_allpick] + Integer.IsEqual(Container(60).NumItems,3)">Conditional</animation>` |
| 6097 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,60" time="0" condition="$EXP[bz_allpick] + Integer.IsEqual(Container(60).NumItems,4)">Conditional</animation>` |
| 6097 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,75" time="0" condition="$EXP[bz_allpick] + Integer.IsEqual(Container(60).NumItems,5)">Conditional</animation>` |
| 6100 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="150" condition="$EXP[bz_infoup]">Conditional</animation>` |
| 6100 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="0" end="100" time="400" tween="sine" easing="inout">Visible</animation>` |
| 6100 `xml/Includes_Bezel.xml` | `<animation effect="zoom" start="100" end="107" center="96,570" time="350" tween="sine" easing="inout" condition="ControlGroup(6100).HasFocus">Conditional</animation>` |
| 6100 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="$EXP[bz_np]">Conditional</animation>` |
| 6100 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="400" tween="sine" easing="inout">Hidden</animation>` |
| 6500 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="150" condition="$EXP[bz_infoup]">Conditional</animation>` |
| 6500 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="0" end="100" time="400" tween="sine" easing="inout">Visible</animation>` |
| 6500 `xml/Includes_Bezel.xml` | `<animation effect="zoom" start="100" end="107" center="96,570" time="350" tween="sine" easing="inout" condition="ControlGroup(6500).HasFocus">Conditional</animation>` |
| 6500 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="400" tween="sine" easing="inout">Hidden</animation>` |

**Timings named in behavior:** 400 ms
