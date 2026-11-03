# Kodi Settings — settings

**Object:** `settings` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/settings.md) · [layout](../layout/settings.md) · [state](../state/settings.md) · [motion](../motion/settings.md) · [art](../art/settings.md) · [input](../input/settings.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/settings.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/settings.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|
| 6996 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,120" time="0" condition="Player.HasMedia">Conditional</animation>` |
| 6996 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="-390,0" end="0,0" time="210" tween="cubic" easing="out" condition="String.IsEmpty(Window(Home).Property(bz_pwrswap))">Visible</animation>` |
| 6996 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="390,0" time="180" tween="cubic" easing="in" condition="!Window.IsVisible(1118) + String.IsEmpty(Window(Home).Property(bz_pwrswap))">Hidden</animation>` |
| 9000 `xml/Settings.xml` | `<animation effect="slide" start="0,0" end="0,120" time="0" condition="Player.HasMedia">Conditional</animation>` |

**Timings named in behavior:** 400 ms, 600 ms
