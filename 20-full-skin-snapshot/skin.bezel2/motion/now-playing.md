# Now playing (dialog 1112) — now-playing

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `now-playing` · **Layer:** motion (timing) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/now-playing.md) · [layout](../layout/now-playing.md) · [state](../state/now-playing.md) · [motion](../motion/now-playing.md) · [art](../art/now-playing.md) · [input](../input/now-playing.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** how long each move takes and what easing curve it uses; copy these numbers exactly to keep the feel.

**See screen:** [now-playing baselines](../port-refs/now-playing/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/now-playing.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Durations/easing pulled from the controls in [layout](../layout/now-playing.md) plus any ms/sec values named in the behavior. Shared tokens: [tokens](tokens.md).

| source | animation |
|---|---|
| 6387 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="0" end="0" time="0" condition="String.IsEqual(Skin.String(bz_at_fsvizop),1)">Conditional</animation>` |
| 6387 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="10" end="10" time="0" condition="String.IsEqual(Skin.String(bz_at_fsvizop),2)">Conditional</animation>` |
| 6387 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="20" end="20" time="0" condition="String.IsEqual(Skin.String(bz_at_fsvizop),3)">Conditional</animation>` |
| 6387 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="30" end="30" time="0" condition="String.IsEqual(Skin.String(bz_at_fsvizop),4)">Conditional</animation>` |
| 6387 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="40" end="40" time="0" condition="String.IsEqual(Skin.String(bz_at_fsvizop),5)">Conditional</animation>` |
| 6387 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="50" end="50" time="0" condition="String.IsEqual(Skin.String(bz_at_fsvizop),6)">Conditional</animation>` |
| 6387 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="60" end="60" time="0" condition="String.IsEqual(Skin.String(bz_at_fsvizop),7)">Conditional</animation>` |
| 6387 `xml/Includes_Bezel.xml` | `<animation effect="fade" start="70" end="70" time="0" condition="String.IsEqual(Skin.String(bz_at_fsvizop),8)">Conditional</animation>` |

**Timings named in behavior:** 1000 ms
