# TV Shows list — tv-list

**Object:** `tv-list` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/tv-list.md) · [layout](../layout/tv-list.md) · [state](../state/tv-list.md) · [motion](../motion/tv-list.md) · [art](../art/tv-list.md) · [input](../input/tv-list.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

**See screen:** [tv-list baselines](../port-refs/tv-list/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/tv-list.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 150 | `` | `` | `130` | `170` | `` |
| 6100 | `60` | `60` | `` | `` | `` |
| 6299 | `60` | `60` | `60` | `60` | `` |
| 6500 | `SetProperty(bz_nav,true,home)` | `60` | `` | `` | `` |
| 6600 | `60` | `` | `` | `` | `60` |
| 6600 | `SetProperty(bz_nav,true,home)` | `` | `` | `` | `60` |
| 6996 | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMPrev_music])` | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMNext_music])` | `6966` | `SetFocus(6996,0,absolute)` | `` |

**Semantics from behavior (verbatim lines):**
- Status:** Live in 5.33.207. Shares the Movies list nav (edge-to-ALL, no wrap, Left/Back → MM). Seasons never rest on `..`. Clearlogo/title sits on the colour strip with Year/Genre underneath. Known open issue: the Movies→TV highlight can jump back to Movies. Draft: not Rob-approved.
- Up / Down** move through the list. At the top or bottom edge, focus jumps to the **ALL** row if it's showing. Otherwise it stays put and doesn't wrap around to the far end.
- Left** opens the main menu whenever the A–Z bar isn't on screen.
- Back** steps out of folders, and at the section's home level it opens the main menu.
- Kodi's native wrap is caught by `bz_flip.py`. When a poll sees the list jump from the top row to the bottom, it focuses ALL if that's shown, or snaps back to the top row (`SetFocus(60,0,absolute)`).
- A folder change (open/Back) is never counted as a wrap.
- Left:**
- 1. `bz_vback` set (video back-face) → `bz_vback_close`.
- Right:** `bz_vback` → 6291. If the grid entry 6600 is visible → `bz_cmd gridenter`.
- Back, first match wins:**
- 1. `bz_vback` → close the back-face.
- Otherwise → 6299, which is Kodi's normal parent-folder Back.
