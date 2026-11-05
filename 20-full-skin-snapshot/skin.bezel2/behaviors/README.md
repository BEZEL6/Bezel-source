# BEZEL behavior files

**Last updated:** 2026-11-04 · 5.33.473 · **Status:** current-state

**What these are.** One file per Bezel object (a screen, dialog, list, pill or animation system). Each file says what the object must feel and look like on **any** framework, then how it is built today in **Kodi**, which is the current sandbox. A porter should be able to rebuild an object from its file without reading Kodi XML. Someone fixing the Kodi skin should find every id, property and file name in the same place.

**Standing rules (Rob)**
- Every time a system changes, its behavior file is updated **in the same build** to match the new current state. The file documents how it works now, not a changelog. History lives in `CLAUDE_CHANGELOG.md`; a file only keeps the build numbers that explain a Never rule.
- One file per object (kebab-case filename = object id). Never merge objects (MM ≠ Music list).
- If a file and the code disagree, the code wins and the file is fixed in the same build.
- Locked objects (`mm-warm`, `leaf-flip`, `idle-big-album-fold`) change only when Rob asks. Their files are still kept current.
- `.bak_*` files are history: never edit or delete.
- These files are the whole port blueprint. The older layers `layout/ state/ motion/ art/ input/ theme/` (5.33.267) are retired: see [PORT_INDEX](../PORT_INDEX.md).
- Master copy: `skin.bezel2/behaviors/`. The copies in the repo's section folders (`02-…/behaviors` to `19-behaviors-docs/behaviors`, `20-full-skin-snapshot/behaviors`) are exact copies made at build time; edit only the master.

---

## File format (every file, every heading)

```
# Object name
**Object:** ids / files · **Where:** where it lives on screen
**Last updated:** date · build · **Status:** live | parked | retired · **Lock:** none | LOCKED (Rob)

## Simple                      what a user sees and does, plain words
## Feel contract (any framework)
### States                     table: state · how you get in · how you leave · what is on screen
### Timeline                   per transition: t (ms) · what · duration · curve
### Interruptions              what happens when input or events arrive mid-transition
### Continuity                 what must never restart, jump, reset or drift out of step
### Layering                   back → front stacking order
### Geometry                   1920×1080 coordinates + the rules behind them
### Art                        sources, size, scale mode, masks, opacity, fallbacks
### Input                      generic actions → result (no key codes)
### Speed targets              how fast it must feel; budgets
### Never                      rejected looks and behaviours, with the build that taught it
### Acceptance checks          tests anyone can run on any framework
## Kodi implementation (sandbox)
### How it works               the live Kodi mechanism
### Wiring                     ids, properties, conditions, files, scripts
### Kodi workarounds (do not port)  parts that exist only because of Kodi
## Related
```

A heading that does not apply keeps its place and says `—` or one line why, so a reader knows it was considered.

**Writing rules**
- The Feel contract never names a Kodi id, property, window number or file. It uses plain names (the stage, the strip, the big album, the MM). The Kodi section maps those names to ids.
- Timings are milliseconds; positions are pixels on the 1920×1080 canvas; opacity is 0–100 %.
- Curves use the names in the table below. "sine out" means decelerate.
- Kodi references use names (include, control id, expression, function), not line numbers, because line numbers rot.
- Tags in the Kodi section: **Intent** (port it) and **Workaround** (Kodi only, do not port).

---

## Global feel tokens

### Canvas
- Design canvas **1920 × 1080**, 16:9, origin top-left. All numbers are in this space; scale uniformly to the real screen (Kodi does this itself).
- Content band: top **120**, height **900** (y 120–1020).

### Main layout (every section with a strip)
| Name | x | width | Notes |
|---|---|---|---|
| Stage (fanart / poster area) | 120 | 930 (to 1050) | the art "stage"; fanart fills it |
| Colour strip (list column) | 660 | 390 (to 1050) | rows, pills, strip art; sits on the stage's right part |
| Stage fill | 120 | 540 | stage edge to strip |
| Gap | 1050 | 90 | strip to big album |
| Big album / poster | 1140 | 600 (to 1740) | square album or poster, its own layer |
| List column (no strip) | 120 | — | Kodi-list fallback position |

### Curves
| Name | CSS / cubic-bezier | Where Bezel uses it |
|---|---|---|
| sine in-out | `cubic-bezier(0.37, 0, 0.63, 1)` | default for fades and sways (~4,000 uses) |
| sine out | `cubic-bezier(0.61, 1, 0.88, 1)` | section fade-ins, slides into place |
| sine in | `cubic-bezier(0.12, 0, 0.39, 0)` | rare: fades away |
| quadratic in-out | `cubic-bezier(0.45, 0, 0.55, 1)` | some list motion |
| cubic in-out / out | `cubic-bezier(0.65, 0, 0.35, 1)` / `cubic-bezier(0.33, 1, 0.68, 1)` | row scroll (Tuner default "cubic") |
| back out | `cubic-bezier(0.34, 1.56, 0.64, 1)` | small overshoot pops (few) |
| linear | `linear` | spin layers, dust drift, clocks |

### Default timings (Tuner defaults, 5.33.472)
| Token | Value | Tunable |
|---|---|---|
| Section fade-in | 400 ms sine out, no fade-out of the old section | code |
| Warm section switch crossfade (MM row → section behind it) | 500 ms | Tuner Main menu › Section fade |
| Menu (MM) open / close | 286 / 250 ms | Tuner Main menu |
| MM-open art crossfade | 500 ms | Tuner Main menu |
| MM warm A/B art swap | 1500 ms, fixed | **LOCKED** |
| Fanart image fade | 150 ms | Tuner List › Fanart fade |
| Row scroll | 271 ms, cubic | Tuner List (Rob: "floaty", 0.7×) |
| Row cascade | 286 ms per row, 30 ms stagger (15th row lands ≈ 0.69 s) | Tuner List |
| Section-entry row hold | 350 ms | code |
| Fullscreen music in / out | 300 ms fade | code |
| Sway pause between swings | 4 s | Tuner Album |
| Leaf flip phase | 1400 ms × 2, 10 s hold | **LOCKED** |
| Double-tap window | 1 s | code |
| Pill idle return | 5 s without input | code |

### Global layering (back → front)
1. The current section window (lists, strip, stage fanart).
2. The big album layer: big album / poster, sway, glare, lit dust, cast shadows. Always present.
3. Fullscreen music chrome (pills, Up Next, NP bar) when fullscreen music is up.
4. Small menus over it (power menu, music controls).
5. System dialogs (confirm, keyboard, busy).

### Global Never (applies to every object)
- No black dip, flash or pop when art changes: new art dissolves over the old (426, 427, 430, 431, 458/460).
- No restart of a continuous animation (sway, glare, dust, spin, the fanart stage) on play, stop, track change, section change or opening fullscreen (452, 453, 472).
- Sections fade **in**; the old section does not fade out first (177, 458). No zooms on section change.
- No slides, except the big album moving to / from centre (454 "keep slides for big album"; 469 MM slide removed).
- No hitch or flash while navigating a list (426).
- No visible waits that look broken (458 "the 1.5 delay makes it look broke"; 317 "remove the wait").
- No "no art" placeholders: when art is missing, nothing is drawn (276 "take it all out, it never worked").
- Fullscreen music opens only when asked; no idle auto-open (5.33.311).
- Performance work never trades feel: 446 (5 s section pauses) and 459 (felt "very bad") were reverted. 457 is the reference for "very smooth and responsive".

---

## Kodi sandbox — global notes
- **Windows and dialogs.** Kodi screens are windows (one at a time) and dialogs (stack over windows). A dialog's `zorder` sets its stack place. Bezel keeps dialog **1122** (big album layer, zorder 0) open all the time; **1121** fullscreen music has zorder 1; **1118** power menu and **1115** music controls zorder 2.
- **Modal dialogs block their caller.** `ActivateWindow(modal)` runs that dialog's loop inside the call, so actions written after it in the same list run only after the dialog closes (GUIDialog `Open_Internal`). All action conditions are evaluated before any action runs (GUIAction). Several Bezel orderings exist only because of this — **Workaround**.
- **Home properties** (`Window(Home).Property(x)`) are the shared state store between XML and Python. The Python service `scripts/bz_flip.py` runs several threads (poster_clock, sway_clock, nav_menu, mm_warm, ab_clock, mm_autohide …) that poll Kodi and set these properties.
- **Animations.** Kodi animations are XML: `Visible` / `Hidden` (on show / hide), `Conditional` (while a condition is true; reverses from where it is when the condition flips), `WindowOpen` / `WindowClose`, `Focus` / `Unfocus`. Image changes crossfade by `fadetime`. Kodi cannot do arithmetic in constants, so paired constants exist (`bz_strip_nx` = −`bz_strip_x`).
- **Tuner.** `scripts/bz_tune.json` holds every Tuner row (P steps, V values, TOG toggles, DEF defaults, FAST one-time seed). `bz_tune_patch.patch()` bakes chosen timings into the XML and the skin reloads.
- **Keymaps.** Bezel installs `zz_bezel2_*` keymaps into the Kodi profile while the skin is active and removes them when another skin loads (`keymaps.md`).

---

## Index
| File | Object |
|---|---|
| addons.md | Add-ons browser |
| artwork-group.md | Global artwork group in the big album layer (album + NP + poster layers) |
| bezel-logo-back.md | Bezel logo as Back (touch) |
| big-album.md | Big album layer (dialog 1122): home / centre / hidden |
| big-album-pill.md | Big album pill (ALBUM / PREV-NEXT) in fullscreen music |
| context-menu.md | Section menu (replaces Kodi's context menu) |
| dialog-busy.md | Busy spinner |
| dialog-confirm.md | Yes / No and OK dialogs |
| dialogue-fs.md | Dialogue FS (1120): big album centred with side albums, from the Music list |
| dust.md | Dust layers (MM dust, ambient, distant, spin, lit dust) |
| fanart-fs.md | Kodi Fanart FS (visualisation window) |
| favourites.md | Favourites |
| filebrowser.md | File browser dialog |
| files-filemanager.md | File manager |
| fullscreen-pill.md | FULLSCREEN pill on the strip |
| fullscreen-video.md | Fullscreen video |
| home-splash.md | Startup splash and first MM |
| idle-big-album-fold.md | Idle big album page fold — **LOCKED** |
| info-options.md | Options + Info pages |
| keyboard.md | On-screen keyboard |
| keymaps.md | Bezel keymaps (install / remove) |
| leaf-flip.md | Leaf flip family — **LOCKED** |
| media-sources.md | Media sources window |
| mm-autohide.md | MM auto-hide (removed) and pill idle return |
| mm-list.md | Main menu (MM) strip |
| mm-mini-player.md | MM mini player |
| mm-warm.md | MM warm system: background art behind the MM — **LOCKED** |
| movies-list.md | Movies list |
| music-controls.md | Music controls dialog |
| music-fanart-fs.md | Music Fanart FS (1121): Bezel's fullscreen music |
| music-list.md | Music list |
| music-videos-list.md | Music videos list |
| music-viz-settings.md | Visualisation settings page |
| now-playing.md | Now Playing (old dialog removed; routes) |
| np-bar.md | Now Playing bar (compact and full) |
| pause-overlay.md | Pause screen |
| pictures.md | Pictures |
| play-next.md | Up Next / Play Next side albums |
| playlists.md | Playlists |
| power-menu.md | Power menu |
| recently-played.md | Recently played |
| search.md | Search dialog |
| section-transitions.md | Section open / switch standard |
| settings.md | Kodi Settings under Bezel |
| skin-settings-tuner.md | BEZEL Tuner |
| sway-animations.md | Shared sway clock: album / poster sway, glare, cast |
| swipe-to-spin-poster.md | PARKED design |
| touch-group.md | Touch targets and double-tap |
| tv-list.md | TV list |
| video-osd.md | Video OSD |
