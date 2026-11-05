# Swipe-to-spin poster (PARKED)

**Object:** design only, not in the tree · would be the Movies / TV poster (`BezelVPLPoster` in 1122)
**Where:** not built
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** **PARKED** (not approved, not shipped; don't build unless Rob asks) · **Lock:** none

## Simple
A design idea: drag a finger (or a slider) across the poster and it turns with you, like an iPad cover; push past a point and it lets go and spins or flips by itself with no jump. Nothing of this exists in the skin.

## Feel contract (any framework)
Proposed contract, for when it's built.

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Resting | — | drag | poster swaying (normal sway) |
| Scrubbing | drag | release / threshold | poster angle follows the finger 1:1 |
| Released | release below threshold | settled | eases back to the sway angle |
| Spinning | past the threshold | spin ends | free spin / flip, starting at the current angle |

### Timeline
Scrub: no timeline (angle = input). Release / spin durations to be chosen with Rob.

### Interruptions
A new drag during a spin catches the poster at its current angle.

### Continuity
The spin must start exactly at the scrubbed angle (no jump); after it, the poster rejoins the shared sway clock in phase.

### Layering
As the poster today.

### Geometry
Poster rotation axis x 1290 (as the sway).

### Art
As the poster today.

### Input
Touch drag / slider value.

### Speed targets
Scrub latency one frame.

### Never
No jump at the scrub → spin handoff.

### Acceptance checks
(when built) drag slowly: angle follows; flick past the threshold: spin starts from the same angle.

## Kodi implementation (sandbox)

### How it works
Not built. The design notes below record why it is hard in Kodi (no input-driven animation values).

### Wiring
None in the tree.

### Kodi workarounds (do not port)
Everything below is a Kodi workaround sketch; a native port gets direct gesture-driven transforms.

### Design detail (proposed, not live)
#### Concept

##### Simple
- A flat movie poster sits on the screen.
- Slide your finger (or a slider) back and forth and the poster turns with it, like on an iPad.
- Push far enough and it "lets go" and spins or flips by itself, smoothly, with no jump.

##### How it works (proposed)
- **Scrub phase.** Python reads the finger or slider position and sets the poster's `rotatey` angle directly. No Kodi animation timeline is involved: the angle simply follows the input.
- **Handoff.** Once the input crosses a chosen threshold, Python flips a condition that starts a real Kodi animation (a spin or a flip).
- **No jump.** The flip has to start at the angle where the poster already sits, or you'd see a visible jump.
- **Goal.** The feel of directly grabbing a poster and making it spin.

##### Wiring (sketch only, not in the tree)
| Piece | Idea |
|---|---|
| Input | touch drag or a Tuner-style slider value |
| Scrub | Python sets the poster image's rotatey (or chooses between stepped pre-rotated states) from the value |
| Trigger | Python sets a Home property that gates a Conditional rotatey animation |
| Handoff | the animation's `start` angle must equal the last scrubbed angle |

---

#### Platform constraints (why it's parked)

##### Simple
Kodi can play an animation forward or backward, but it can't hold one halfway or drag it to a point. So the "follow your finger" part has to be faked.

##### How it works
- Kodi animations can't be paused, scrubbed or seeked to a frame.
- Conditional and WindowOpen animations only play forward, and in reverse from their ends (if reversible).
- Python can approximate scrubbing by setting control properties from a slider value.
- One slider can drive several effects at once.
- Python can toggle conditions to start or reverse animations, but only from their ends.

##### Wiring
No live wiring. The nearest live mechanism is the sway clock (Python sets flags, and XML Conditional rotatey reacts); see sway-animations.md.

---

#### Related
- An earlier parked idea: an animation scrubber / stepped keyframes driven by a Tuner slider (Kodi can't truly scrub Conditional animations).
- sway-animations.md
- Logged from voice, 2026-10-31.

## Related
[sway-animations](sway-animations.md) · [artwork-group](artwork-group.md)
