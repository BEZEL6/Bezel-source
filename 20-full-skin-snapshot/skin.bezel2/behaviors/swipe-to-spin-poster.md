# swipe-to-spin poster (PARKED)

**Object:** Design only. There is no code, XML or script for it in the tree.
**Where:** Would be the Movies/TV poster (`BezelVPLPoster`). Not built.
**Last updated:** 2026-10-31
**Status:** **PARKED, not approved, not shipped.** This is a design exploration of the limits of Bezel and Kodi's animation system. Don't build it unless Rob asks.
**Skin:** skin.bezel2

> Everything below describes a *proposed* design. None of it exists in the live skin. The "Wiring" layer is a sketch of how it *could* be wired, not live code.

---

## Concept

### Simple
- A flat movie poster sits on the screen.
- Slide your finger (or a slider) back and forth and the poster turns with it, like on an iPad.
- Push far enough and it "lets go" and spins or flips by itself, smoothly, with no jump.

### How it works (proposed)
- **Scrub phase.** Python reads the finger or slider position and sets the poster's `rotatey` angle directly. No Kodi animation timeline is involved: the angle simply follows the input.
- **Handoff.** Once the input crosses a chosen threshold, Python flips a condition that starts a real Kodi animation (a spin or a flip).
- **No jump.** The flip has to start at the angle where the poster already sits, or you'd see a visible jump.
- **Goal.** The feel of directly grabbing a poster and making it spin.

### Wiring (sketch only, not in the tree)
| Piece | Idea |
|---|---|
| Input | touch drag or a Tuner-style slider value |
| Scrub | Python sets the poster image's rotatey (or chooses between stepped pre-rotated states) from the value |
| Trigger | Python sets a Home property that gates a Conditional rotatey animation |
| Handoff | the animation's `start` angle must equal the last scrubbed angle |

---

## Platform constraints (why it's parked)

### Simple
Kodi can play an animation forward or backward, but it can't hold one halfway or drag it to a point. So the "follow your finger" part has to be faked.

### How it works
- Kodi animations can't be paused, scrubbed or seeked to a frame.
- Conditional and WindowOpen animations only play forward, and in reverse from their ends (if reversible).
- Python can approximate scrubbing by setting control properties from a slider value.
- One slider can drive several effects at once.
- Python can toggle conditions to start or reverse animations, but only from their ends.

### Wiring
No live wiring. The nearest live mechanism is the sway clock (Python sets flags, and XML Conditional rotatey reacts); see sway-animations.md.

---

## Related
- An earlier parked idea: an animation scrubber / stepped keyframes driven by a Tuner slider (Kodi can't truly scrub Conditional animations).
- sway-animations.md
- Logged from voice, 2026-10-31.
