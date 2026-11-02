# Music controls (dialog 1115) — music-controls

**Object:** `music-controls` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-controls.md) · [layout](../layout/music-controls.md) · [state](../state/music-controls.md) · [motion](../motion/music-controls.md) · [art](../art/music-controls.md) · [input](../input/music-controls.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
The music controls panel is the "remote control" menu for music: play/pause, skip, shuffle, repeat, Up next, choose a visualisation, tweak its settings, or jump to the Tuner. It opens automatically when Kodi would show its music OSD, and from the fan art pill or the music list. Left always closes it.

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/music-controls.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/music-controls.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="0" end="100" time="300" tween="sine" easing="inout">Visible</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout">Hidden</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="1250" tween="sine" easing="inout" reversible="false" condition="String.IsEqual(Window(Home).Property(bz_tomusic),true)">Conditional</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="500" tween="sine" easing="inout" reversible="false" condition="String.IsEqual(Window(Home).Property(bz_m2v_flat),true)">Conditional</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="0" end="100" time="300" tween="sine" easing="inout">Visible</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout">Hidden</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="1250" tween="sine" easing="inout" reversible="false" condition="String.IsEqual(Window(Home).Property(bz_tomusic),true)">Conditional</animation>` |
| 6600 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="100" end="0" time="500" tween="sine" easing="inout" reversible="false" condition="String.IsEqual(Window(Home).Property(bz_m2v_flat),true)">Conditional</animation>` |

**Timings named in behavior:** 250 ms, 420 ms
