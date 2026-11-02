# Sway animations — shared clock, album, poster, stub cast — sway-animations

**Object:** `sway-animations` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/sway-animations.md) · [layout](../layout/sway-animations.md) · [state](../state/sway-animations.md) · [motion](../motion/sway-animations.md) · [art](../art/sway-animations.md) · [input](../input/sway-animations.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
- The big album (Music) and the poster (Movies/TV) slowly rock left and right, like a picture tilting on a wall.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/sway-animations.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 100 | `` | `` | `304` | `120` | `` |
| 146 | `` | `` | `126` | `166` | `` |

**Semantics from behavior (verbatim lines):**
- The big album (Music) and the poster (Movies/TV) slowly rock left and right, like a picture tilting on a wall.
- Sway is the slow left–right tip of the big Music album and the Movies/TV poster. It is not a one-shot animation Kodi runs and forgets. A small Python script keeps a shared **clock**, and the skin XML listens to flags that clock turns on. Stub side-cast shadows (the soft dark fall beside the album) also read that same clock so they brighten and fade in step with the tip.
- | Stub cast images | `Includes_Bezel.xml` — `bezel/pn_cast.png` 270×540 (left flipx, right unflipped) |
- Right-sway glares: 0→100 **1810 ms**, delay **3690**; held 0 until `bz_sway_go`
- Title changes never remount** (t4815). Cleared only when Videos is left.
- Geometry (current):** image `left=480`, `top=230`, `width=480`, `height=580` → **right edge x=960** = BezelColourBlock right edge (570+390). Grow/shrink Conditional zooms use **center="960,520"** so fade-in/out stay pinned to the strip edge (no drag toward the album). Was left=485 / center 965 (5px overhang).
- Left stub: `left=270`, `flipx=true`
- Right stub: `left=0`, unflipped
- q=\_sn\!\left(\frac{\min(w,\,11-w)}{5.5}\right)
- q=\_sn\!\left(\frac{u-2.4}{5}\right),\qquad
- L=100-85\cdot\_sn\!\left(\frac{f-D}{5}\right),\qquad
- R=15+85\cdot\_sn\!\left(\frac{f-D-5}{5}\right)
