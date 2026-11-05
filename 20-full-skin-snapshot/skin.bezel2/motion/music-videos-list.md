# Music videos list — music-videos-list

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `music-videos-list` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-videos-list.md) · [layout](../layout/music-videos-list.md) · [state](../state/music-videos-list.md) · [motion](../motion/music-videos-list.md) · [art](../art/music-videos-list.md) · [input](../input/music-videos-list.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/music-videos-list.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/music-videos-list.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|
| 6098 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,60" time="0" condition="String.IsEqual(Container(60).ListItemAbsolute(0).Label,..)">Conditional</animation>` |
| 6098 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,-60" time="0" condition="$EXP[bz_allpull60]">Conditional</animation>` |
| 6098 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,-120" time="0" condition="$EXP[bz_allpull120]">Conditional</animation>` |
| 6098 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,-60" time="0" condition="$EXP[bz_allpull_inall]">Conditional</animation>` |
| 6098 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,60" time="0" condition="Integer.IsEqual(Container(60).NumItems,1)">Conditional</animation>` |
| 6098 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,120" time="0" condition="Integer.IsEqual(Container(60).NumItems,2)">Conditional</animation>` |
| 6098 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,180" time="0" condition="Integer.IsEqual(Container(60).NumItems,3)">Conditional</animation>` |
| 6098 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,240" time="0" condition="Integer.IsEqual(Container(60).NumItems,4)">Conditional</animation>` |
| 6100 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="150" condition="$EXP[bz_infoup]">Conditional</animation>` |
| 6100 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="0" end="100" time="400" tween="sine" easing="inout">Visible</animation>` |
| 6100 `xml/Includes_Bezel.xml` | `<animation effect="zoom" start="100" end="107" center="96,570" time="350" tween="sine" easing="inout" condition="ControlGroup(6100).HasFocus">Conditional</animation>` |
| 6100 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="$EXP[bz_np]">Conditional</animation>` |
| 6100 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="400" tween="sine" easing="inout">Hidden</animation>` |
| 6500 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="150" condition="$EXP[bz_infoup]">Conditional</animation>` |
| 6500 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="0" end="100" time="400" tween="sine" easing="inout">Visible</animation>` |
| 6500 `xml/Includes_Bezel.xml` | `<animation effect="zoom" start="100" end="107" center="96,570" time="350" tween="sine" easing="inout" condition="ControlGroup(6500).HasFocus">Conditional</animation>` |
| 6500 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="400" tween="sine" easing="inout">Hidden</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="0" end="100" time="300" tween="sine" easing="inout">Visible</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout">Hidden</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="1250" tween="sine" easing="inout" reversible="false" condition="String.IsEqual(Window(Home).Property(bz_tomusic),true)">Conditional</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="500" tween="sine" easing="inout" reversible="false" condition="String.IsEqual(Window(Home).Property(bz_m2v_flat),true)">Conditional</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="0" end="100" time="300" tween="sine" easing="inout">Visible</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout">Hidden</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="1250" tween="sine" easing="inout" reversible="false" condition="String.IsEqual(Window(Home).Property(bz_tomusic),true)">Conditional</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="500" tween="sine" easing="inout" reversible="false" condition="String.IsEqual(Window(Home).Property(bz_m2v_flat),true)">Conditional</animation>` |
| 6996 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,120" time="0" condition="Player.HasMedia">Conditional</animation>` |
| 6996 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="-390,0" end="0,0" time="210" tween="cubic" easing="out" condition="String.IsEmpty(Window(Home).Property(bz_pwrswap))">Visible</animation>` |
| 6996 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="390,0" time="180" tween="cubic" easing="in" condition="!Window.IsVisible(1118) + String.IsEmpty(Window(Home).Property(bz_pwrswap))">Hidden</animation>` |

**Timings named in behavior:** —
