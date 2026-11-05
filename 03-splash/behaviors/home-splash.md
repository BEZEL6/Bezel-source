# Startup splash and first MM

**Object:** cold start chain · Kodi: `Startup.xml` onload, `Home.xml` onload, `scripts/bz_warmgate.py` (warm gate), `bz_cmd.py start`, overlay `BezelWarmGateOverlay` / `BezelWarmGate` (also `Custom_1113_WarmGate.xml`)
**Where:** app start, and every Home load
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** the splash is the warm gate of the LOCKED warm system ([mm-warm](mm-warm.md))

## Simple
At start a near-black splash shows the Bezel logo, BEZEL and the version, and a small credit at the bottom. Behind it Bezel builds the menu and loads artwork. After at least 5 seconds (never more than 15) it fades over 3 seconds straight onto the main menu, open over the start section with its row highlighted, and the big album / poster dissolve in with the fade. Nothing pops, nothing flashes blank. Back on the Home screen does nothing (so a stray repeat Back can't open the power menu).

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Splash | app start (Tuner Startup splash on) | ≥ 5 s and art ready, or 15 s | splash |
| Fading | dismiss | 3 s | splash fades; art + MM dissolve in together |
| First MM | fade done | user input | MM open over the start section (Music / Movies / TV, Tuner), start row on a random item |
| Splash off | Tuner Startup splash Off | — | art shows at once |

### Timeline
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| 0 | splash on; first section loads; random start row; art for all three sections warms | — | — |
| ≥ 5000 (≤ 15 000) | splash fades out; big album / poster fade in | 3000 | sine |
| fade end | dust starts | its own fade | — |
| +6000 | start-fade state ends | — | — |

### Interruptions
- An add-on update dialog at boot: after the splash, Bezel waits (≤ 120 s) for it to close and re-opens the start screen once.
- Input during the splash: ignored by the MM until it is live.

### Continuity
- The first frame after the splash is the finished MM with art (no half-built screen).
- Dust never draws under the splash.

### Layering
Section (black first paint) < art layer (held at 0 %) < MM < splash overlay (top).

### Geometry
| Piece | Value |
|---|---|
| Backdrop | full screen, #0A0B0E |
| Logo | 280 × 280 at 820, 340, 50 % |
| Version | y 714, h 36, "v<version>", Montserrat Medium 28, #C8C8CD |
| Credit | y 1000, h 28, centred, gap 12: "Design by Robert Politano" Montserrat Regular 20 at 50 % + US flag 27 × 14 at 50 % |

### Art
Static logo (no glow, no pulse).

### Input
Back on Home: nothing.

### Speed targets
Splash between 5 and 15 s; fade 3 s.

### Never
- No art pop after the splash (412 ARTUNDERSPLASH); art never left invisible (417).
- No logo glow / pulse (316).
- No blank Startup window after an add-on update (312).
- No power menu from repeated Back on Home (321).

### Acceptance checks
1. Cold start: splash ≥ 5 s, then one 3 s fade to the MM with art already there.
2. Tuner Startup splash Off: no splash, art at once.
3. Press Back on Home several times: nothing happens.

## Kodi implementation (sandbox)

### How it works
- **Warm gate** (`bz_warmgate.py`): `MIN=5.0`, `CAP=15.0`, `FADE=3.0`; guard `bz_warmgate_running`; first section from `bz_at_mmdef` (1 Music / 2 Movies / 3-empty TV); ready flags `bz_warm_ready_<sec>`; `randstart()`; watchdog forces dismiss at CAP. `dismiss()` clears `bz_warm_gate`, closes 1113, waits FADE, sets `bz_splash_done=1`. `rescue_startup()` re-issues `ReplaceWindow(System.StartupWindow)` once if still on Startup.
- Overlay visible `!String.IsEmpty(Window(Home).Property(bz_warm_gate)) + !String.IsEqual(Skin.String(bz_at_warmsplash),Off)`, 3 s Hidden fade. `BezelGlobalBackdrop` hidden while `bz_warm_gate`.
- **Art under the splash:** 1122 opens at startup; group 6400 held at alpha 0 while `bz_warm_gate`, then 3000 ms fade (see [big-album](big-album.md)).
- **Home.xml onload:** `bz_defseed ≠ 5.0.20` → `bz_tune.py seed`; `bz_fastseed ≠ 5.33.471` (after the DEF seed) → `bz_tune.py fastseed`; `bz_flip.py` unless running; `bz_precache.py` unless running; `bz_cmd.py start`.
- **`bz_cmd.py start`:** one-time View-All defaults, `_bz_showall_sync()`, restore `bz_mmsub_*`, outline default; first entry → `bz_started`, `bz_startfade`, pills reset to 1; unless `bz_nomenustart`: `bz_mmstartrow`, `bz_mmstartsec`, clear `bz_navgrace`, `bz_mmstart=1`, `bz_nav=true`; wait for music (300 × 50 ms), re-assert `bz_nav`, wait for `bz_splash_done` (240 × 50 ms), re-assert, +6 s clear `bz_startfade`. 4.0.1 migration (`bz_tunever ≠ 401`) once.
- **Home Back:** `bezel2_np_tab.xml` `<home>` maps Back (keyboard, remote, gamepad, joystick) to `noop`.

### Wiring
| Item | Value |
|---|---|
| Includes | `BezelWarmGateOverlay`, `BezelWarmGate`, `BezelGlobalBackdrop` |
| Home | `bz_warm_gate`, `bz_splash_done`, `bz_warmgate_running`, `bz_warm_ready_*`, `bz_started`, `bz_startfade`, `bz_mmstart`, `bz_mmstartrow`, `bz_mmstartsec` |
| Skin | `bz_at_warmsplash`, `bz_at_mmdef`, `bz_defseed`, `bz_fastseed`, `bz_nomenustart` |
| Fonts | `bz_splash28m`, `bz_splash20r` (Font.xml, both fontsets) |
| Media | `bezel/logo.png`, `bezel/us_flag.png` |

### Kodi workarounds (do not port)
- The MIN / CAP timers and re-asserting `bz_nav`: Kodi gives no "ready" signal and the Music window can take > 3 s on the Shield.
- `rescue_startup()`: Kodi add-on dialogs can swallow the start window switch.
- Home Back = noop: Kodi maps Back on Home to its shutdown menu.

## Related
[mm-warm](mm-warm.md) · [mm-list](mm-list.md) · [big-album](big-album.md) · [dust](dust.md) · [skin-settings-tuner](skin-settings-tuner.md)
