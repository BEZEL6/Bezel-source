# Home / startup splash

**Object:** `Startup.xml` onload · `Home.xml` onload · `scripts/bz_warmgate.py` (warm gate) · `scripts/bz_cmd.py start` · overlay `BezelWarmGateOverlay` (Includes_Bezel ~3617)  
**Where:** Cold start of Kodi on BEZEL, and every Home load  
**Last updated:** 2026-11-03 · 5.33.417
**Status:** live. The splash is the warm gate of WARM 2.0, which is **LOCKED** (mm-warm.md). Any change needs Rob's approval. This file only describes the startup chain around it.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Splash = warm gate

**Simple.** At start, a splash covers the screen while BEZEL builds its windows and warms artwork. It stays at least 5 s and at most 15 s, then fades over 3 s straight onto the Main Menu. Nothing pops and nothing flashes blank.

**How it works.** The full spec is in **mm-warm.md → Warm gate**. In short: the gate prop is set before the startup window, the underlay section lands, a random start row is focused (RANDSTART), art for all three sections is warmed, and then the overlay is dismissed. A watchdog forces the dismiss at CAP even if warming is not done. `bz_splash_done=1` is set only after the 3 s fade, and dust and the start menu wait on it. The artwork dialog 1122 (group 6400) is already open under the splash at alpha 0 and fades in 3 s with the splash fade (hold anim 100→0 so it releases — 5.33.417).

**Wiring.**
- `Startup.xml` onload: `bz_at_warmsplash≠Off` → `SetProperty(bz_warm_gate,1,home)` · `ClearProperty(bz_splash_done)` · `RunScript(bz_warmgate.py)` · `ReplaceWindow($INFO[System.StartupWindow])`.
- `bz_warmgate.py`: `MIN=5.0`, `CAP=15.0`, `FADE=3.0`. Guard `bz_warmgate_running`. First section from `bz_at_mmdef` (1 Music / 2 Movies / 3/empty TV). Ready flags `bz_warm_ready_<sec>`. `dismiss()` clears `bz_warm_gate`, closes 1113 if visible, waits FADE, then sets `bz_splash_done=1` and clears `bz_warmgate_running`.
- Overlay visible: `!String.IsEmpty(Window(Home).Property(bz_warm_gate)) + !String.IsEqual(Skin.String(bz_at_warmsplash),Off)`.
- While `bz_warm_gate` is set, `BezelGlobalBackdrop` (inside `BezelBlack`) is hidden, so Music/Videos first paint is solid black under the splash rather than the glow backdrop.

## Splash look (5.33.316, approved tighter mock pt2395u)

**Simple.** Near-black screen, one Bezel logo in the middle at half opacity, **BEZEL** and the version under it, and a small half-opacity credit "Design by Robert Politano" with a tiny US flag at the bottom. Nothing else.

**Wiring.** `BezelWarmGate` (Includes_Bezel, also used by Custom_1113_WarmGate.xml), wrapped by `BezelWarmGateOverlay` (visibility + 3 s Hidden fade, unchanged).
- Backdrop `colors/white.png` colordiffuse `FF0A0B0E`, 1920×1080.
- Logo `bezel/logo.png` 280×280 at x820 y340, colordiffuse `80FFFFFF` (50%). Static: logoglow multiimage and 80↔100 pulse removed.
- `BEZEL` label y650 h64, font `bz_splash68b` (Montserrat-Bold 68), `FFFFFFFF`.
- Version label y714 h36, `v$INFO[System.AddonVersion(skin.bezel2)]`, font `bz_splash28m` (Montserrat-Medium 28), `FFC8C8CD`.
- Credit grouplist y1000 h28 centred, gap 12: label "Design by Robert Politano" font `bz_splash20r` (Montserrat-Regular 20) `80FFFFFF` + `bezel/us_flag.png` (54×28 source) drawn 27×14, colordiffuse `80FFFFFF`.
- Fonts added to both fontsets in Font.xml.

## Art under the splash (5.33.412 ARTUNDERSPLASH)

**Simple.** Big album and poster (dialog 1122, group 6400) load **behind** the splash and dissolve in **with** the 3 s splash fade — no art pop after the splash closes. Dust (1114) still waits for `bz_splash_done`.

**Wiring.** 1122 `<visible>` has no `bz_splash_done` term (opens at startup, zorder 0, modeless). Group 6400 carries two Conditional fades: alpha 0 (time 0) while `bz_warm_gate` is set, and 0→100 over 3000 ms sine when `bz_warm_gate` clears (same moment `bz_warmgate.py dismiss()` starts the overlay's 3 s Hidden fade). Splash Off → gate never set → art shows at once. List-60 section art (Music/Videos windows) already rendered under the overlay.

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


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/Startup.xml`

_No id’d controls in this file (layout comes from includes)._

Actions (`onclick`/`onload`/`onback`) found:
- `ClearProperty(bz_splash_done,home)`
- `ReplaceWindow($INFO[System.StartupWindow])`
- `RunScript(special://skin/scripts/bz_warmgate.py)`
- `SetProperty(bz_warm_gate,1,home)`

**Source:** `xml/Home.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 9999 | button | -100,-100 | 10×10 | `—/—/—/—` | `—` |

Actions (`onclick`/`onload`/`onback`) found:
- `RunScript(special://skin/scripts/bz_cmd.py,start)`
- `RunScript(special://skin/scripts/bz_flip.py)`
- `RunScript(special://skin/scripts/bz_precache.py)`
- `RunScript(special://skin/scripts/bz_tune.py,seed)`

**Source:** `xml/Includes_Bezel.xml` include `BezelWarmGateOverlay`

_No id’d controls in this file (layout comes from includes)._

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/home-splash.md) · [state](../state/home-splash.md) · [motion](../motion/home-splash.md) · [art](../art/home-splash.md) · [input](../input/home-splash.md) · [theme](../theme/tokens.md) · [screens](../port-refs/home-splash/) · [PORT_INDEX](../PORT_INDEX.md)

## Startup add-on install rescue (5.33.312)
If Kodi auto-installs/updates an add-on at boot, its dialog can swallow Startup.xml's `ReplaceWindow(System.StartupWindow)`, leaving a blank Startup window. `bz_warmgate.py` `rescue_startup()` (after splash dismiss) waits up to 120s for modal/progress/busy dialogs to close; if still on Startup it re-issues `ReplaceWindow` once. No-op on normal boots.

## Home Back ignored (5.33.321, Rob t2408 — current)
- `bezel2_np_tab.xml` `<home>` maps Back to `noop`: keyboard escape/backspace/browser_back, remote back, gamepad b/back, joystick b (default + shield). Quick or HDMI-CEC repeat Back while the Home bounce pad is active no longer reaches Kodi default ShutdownMenu → Power 1118. MM POWER row → 1118 unchanged. Installed as `zz_bezel2_np_tab.xml` on start (FULL restart).
