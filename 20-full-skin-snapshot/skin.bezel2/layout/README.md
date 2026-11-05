# layout/ — BEZEL port blueprint layer

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Last updated:** 2026-11-01 · 5.33.267 · part of the one blueprint: [PORT_INDEX](../PORT_INDEX.md)

## Simple
This layer is the blueprint's **geometry — where things sit and where focus goes**. It is an equal peer of behaviors/ (feel), layout/, state/, motion/, art/, input/, theme/ and port-refs/ (screens). One file per object id (`<id>.md`, same name as `behaviors/<id>.md`).

## Deep — format rules
- Header: title · **Object** id · **Layer** · **Last updated** (date · build) · **Status** · sibling links (behavior/layout/state/motion/art/input/theme/PORT_INDEX).
- Two tiers in every file: `## Simple` (plain overview, may say "see screen") then `## Deep (rebuild detail)`.
- Content: Control sections: id · type · file Lnnn, then left/top/right/bottom/width/height, camera, onleft/onright/onup/ondown/onback, visible. Coords in 1920×1080 units ([resolution.md](resolution.md)). Visibility strings are context; their prop names are owned by state/.
- Current state only, never a changelog. Never copy another layer's content — link by object id.
- **Standing rule:** when the live object changes, update this file in the **same build** as the behavior file (and the port-refs baseline if the look changed).
- Regenerate extracted tables with `python3 /workspace/portgen/gen.py` (per-object) / `globals_gen.py` (globals), then re-apply hand-verified sections (kept below an `## Hand-verified` heading).
