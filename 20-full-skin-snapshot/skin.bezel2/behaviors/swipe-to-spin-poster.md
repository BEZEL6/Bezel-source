# swipe-to-spin poster (PARKED)

**Last updated:** 2026-10-31 · 5.33.194 (catch-up sync to live tree)  

**Object:** design only — no code in tree
**Status:** parked — Parked — not approved. Design exploration of Bezel / Kodi platform limits. Do not build unless Rob asks.

## Concept
Flat movie poster on screen. Sliding a finger (or a slider) back and forth drives the poster’s `rotatey` in real time: Python reads the touch/slider position and sets the image’s rotatey directly — no Kodi animation timeline. Once the finger/slider crosses a chosen threshold, Python flips a condition that triggers a real Kodi animation (spin or flip). The handoff must be seamless: the flip’s starting angle must match where the poster already sits, or there is a visible jump.

**Goal:** Illusion of swiping a poster and making it spin — direct manipulation like on an iPad.

## Constraints
- Kodi animations cannot be paused, scrubbed, or seeked to a frame
- Conditional / WindowOpen anims only play forward and reverse from the ends (if reversible)
- Python can approximate scrubbing by setting control properties from a slider value
- One slider can drive multiple effects at once
- Python can toggle conditions to start or reverse anims from the ends

## Related
Earlier park: anim scrubber / stepped keyframes via Tuner slider (Kodi can’t true-scrub Conditional anims).

Logged voice 2026-10-31.
