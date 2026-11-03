# Search (dialog 1107) — search

**Object:** `search` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/search.md) · [layout](../layout/search.md) · [state](../state/search.md) · [motion](../motion/search.md) · [art](../art/search.md) · [input](../input/search.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/search.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|
| 9000 | `9000` | `9000` | `9000` | `9000` | `SetProperty(bz_nav,true,home)` |

**Semantics from behavior (verbatim lines):**
- Status:** Live in 5.33.207. Three search rows; Back returns to the MM. Draft: not Rob-approved.
- Pick SEARCH on the main menu and a small panel offers three kinds of search. Back closes it and puts you back on the main menu.
- 3. Focus is pinned to list 9000. Every direction points back at 9000, so you can't wander off the list.
- 4. Back sets `bz_nav=true` (the MM reopens on its row), then `Dialog.Close(1107,true)` closes the dialog (a control onback consumes Back, so Kodi will not close it by itself).
- If an add-on is missing, Select installs it. If it's disabled, Select enables it. After that, press Select again to search.
- Header label "SEARCH". Footer "OK select   BACK close". Detail labels: `Container(9000).ListItem.Label` / `Label2`.
- | Up / Down | Move in 9000 (all directions stay in 9000) |
- | Select | Run row |
- | Back | `bz_nav=true` → close → MM |
- ## Touch
