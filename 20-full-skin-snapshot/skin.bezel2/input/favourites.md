# Favourites — favourites

**Object:** `favourites` · **Layer:** input (actions) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/favourites.md) · [layout](../layout/favourites.md) · [state](../state/favourites.md) · [motion](../motion/favourites.md) · [art](../art/favourites.md) · [input](../input/favourites.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
FAVOURITES in the Main Menu opens Kodi Favourites as a BEZEL list with a random backdrop. Back opens the Main Menu.

**This layer in one line:** what each remote key / touch does on this object, as edges between controls.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/favourites.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Navigation edges from live controls (Kodi actions → port action names in [keymap-overview](keymap-overview.md)).

| control | Left | Right | Up | Down | Back |
|---|---|---|---|---|---|

**Semantics from behavior (verbatim lines):**
- Simple.** FAVOURITES in the Main Menu opens Kodi Favourites as a BEZEL list with a random backdrop. Back opens the Main Menu.
- How it works.** GO `fav` closes the MM and opens the window. Backdrop pick and save work as in add-ons (addons.md). Favourites has no XML `onback`. The open-MM-on-Back at the root is done by `bz_flip.py`'s root-arm logic. A folder normally has to have been shown for 0.6 s (`bz_rootarm`) before Back opens the MM, so a held Back that arrives during the open cannot bounce you straight into the MM. Freshly opened windows 10060 (Favourites), 10001 and 10820 arm at once (5.33.179 BUG-024).
- Back: `bz_flip.py` ~884 root-arm (`bz_rootarm`, `bz_navroot` / `bz_atnavroot`).
- Simple.** Up and Down move. Select runs the favourite. Left opens the MM. Back opens the MM. A double-tap opens the Options menu where the window supports it.
- Wiring.** List 60 comes from `View_60_BezelInfoList` (shared section list behavior, including the MM focus bounces). I did not re-trace the Left→MM handler inside that include for this doc. The dtap hint is from `BezelDtapHint`.
- How it works.** `bz_fav.py` toggles the current playing file through Kodi's `Favourites.AddFavourite` and stores the path in Home `bz_favpath`, so the star state can be shown. `bz_ctx.py fav` builds the right favourite type for the focused item.
