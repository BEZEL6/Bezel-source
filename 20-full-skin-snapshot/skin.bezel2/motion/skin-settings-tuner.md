# Skin settings / BEZEL Tuner — skin-settings-tuner

**Object:** `skin-settings-tuner` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/skin-settings-tuner.md) · [layout](../layout/skin-settings-tuner.md) · [state](../state/skin-settings-tuner.md) · [motion](../motion/skin-settings-tuner.md) · [art](../art/skin-settings-tuner.md) · [input](../input/skin-settings-tuner.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

**See screen:** [skin-settings-tuner baselines](../port-refs/skin-settings-tuner/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/skin-settings-tuner.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/skin-settings-tuner.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|
| 6975 `xml/Includes_Tuner.xml` | `<animation effect="fade" start="0" end="100" time="200">Visible</animation>` |
| 6975 `xml/Includes_Tuner.xml` | `<animation effect="fade" start="100" end="0" time="0">Hidden</animation>` |
| 6996 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="0,120" time="0" condition="Player.HasMedia">Conditional</animation>` |
| 6996 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="-390,0" end="0,0" time="210" tween="cubic" easing="out" condition="String.IsEmpty(Window(Home).Property(bz_pwrswap))">Visible</animation>` |
| 6996 `xml/Includes_Bezel.xml` | `<animation effect="slide" start="0,0" end="390,0" time="180" tween="cubic" easing="in" condition="!Window.IsVisible(1118) + String.IsEmpty(Window(Home).Property(bz_pwrswap))">Hidden</animation>` |

**Timings named in behavior:** 1500 ms, 600 ms
