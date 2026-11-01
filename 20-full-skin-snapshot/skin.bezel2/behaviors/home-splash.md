# Home / startup splash

**Object:** `Startup.xml` onload · `Home.xml` onload · `scripts/bz_warmgate.py` (warm gate) · `scripts/bz_cmd.py start` · overlay `BezelWarmGateOverlay` (Includes_Bezel ~3617)  
**Where:** Cold start of Kodi on BEZEL, and every Home load  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** live. The splash is the warm gate of WARM 2.0, which is **LOCKED** (mm-warm.md). Any change needs Rob's approval. This file only describes the startup chain around it.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Splash = warm gate

**Simple.** At start, a splash covers the screen while BEZEL builds its windows and warms artwork. It stays at least 5 s and at most 15 s, then fades over 3 s straight onto the Main Menu. Nothing pops and nothing flashes blank.

**How it works.** The full spec is in **mm-warm.md → Warm gate**. In short: the gate prop is set before the startup window, the underlay section lands, a random start row is focused (RANDSTART), art for all three sections is warmed, and then the overlay is dismissed. A watchdog forces the dismiss at CAP even if warming is not done. `bz_splash_done=1` is set only after the 3 s fade, and dust and the start menu wait on it.

**Wiring.**
- `Startup.xml` onload: `bz_at_warmsplash≠Off` → `SetProperty(bz_warm_gate,1,home)` · `ClearProperty(bz_splash_done)` · `RunScript(bz_warmgate.py)` · `ReplaceWindow($INFO[System.StartupWindow])`.
- `bz_warmgate.py`: `MIN=5.0`, `CAP=15.0`, `FADE=3.0`. Guard `bz_warmgate_running`. First section from `bz_at_mmdef` (1 Music / 2 Movies / 3/empty TV). Ready flags `bz_warm_ready_<sec>`. `dismiss()` clears `bz_warm_gate`, closes 1113 if visible, waits FADE, then sets `bz_splash_done=1` and clears `bz_warmgate_running`.
- Overlay visible: `!String.IsEmpty(Window(Home).Property(bz_warm_gate)) + !String.IsEqual(Skin.String(bz_at_warmsplash),Off)`.
- While `bz_warm_gate` is set, `BezelGlobalBackdrop` (inside `BezelBlack`) is hidden, so Music/Videos first paint is solid black under the splash rather than the glow backdrop.

## Home.xml onload

**Simple.** Every Home load starts the background helpers once and runs the start routine.

**Wiring.** `bz_defseed≠5.0.20` → `bz_tune.py seed` · `bz_flip.py` unless `bz_flip_running=true` · `bz_precache.py` unless `bz_precache_running=true` · `bz_cmd.py start`.

## bz_cmd.py start (MM-first)

**Simple.** On the very first start, the Main Menu is open over Music when the splash fades, with the startup row highlighted.

**How it works.** The menu is armed **before** Music opens. On Shield the music window can take more than 3 s, and before 4.7.11 `bz_nav` was never set under the splash. Music opens at `musicdb://` and then updates to Artists, so Back steps up one level instead of to the sources root. After the splash it re-asserts `bz_nav`, in case something closed the menu early under the splash (4.7.8+). After a further 6 s it clears `bz_startfade`.

**Wiring.**
- One-time: View All Albums/Seasons defaults (`bz_showall_inited`), `_bz_showall_sync()`, restore `bz_mmsub_*` from `bz_last_mmsub_*`, outline default (`bz_attn_outline`).
- First entry (`bz_started` empty) → `bz_started=true`, `bz_startfade=true`. Pills reset to 1 (Artists / Titles / Shows) in both Home and Skin.String (t5012).
- Unless `bz_nomenustart`: `bz_mmstartrow`, `bz_mmstartsec` from `bz_at_mmdef`, clear `bz_navgrace`, `bz_mmstart=1`, `bz_nav=true`.
- `ActivateWindow(Music,musicdb://)` → wait up to 60×50 ms → `Container.Update(musicdb://artists/)` (t5011).
- Wait for music (300×50 ms) → set `bz_nav` if missing → wait for `bz_splash_done` (240×50 ms) → re-assert → wait 6 s → clear `bz_startfade`.
- A 4.0.1 migration (`bz_tunever≠401`) re-maps old tuner steps once and may `ReloadSkin()`.

## Related
mm-warm.md · mm-list.md · section-transitions.md · dust.md
