# port-refs/ — screen baselines

**Last updated:** 2026-11-01 · 5.33.267 · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Pictures of what each screen must look like. Two uses: **(1) smoke baseline** — after a Bezel build, put the same screen in the same state and compare; **(2) port diff** — render the native rebuild at 1920×1080 in the same state and diff against these.

## Deep
Folder per object id: `port-refs/<id>/<state>.png`. Source smoke dir noted below. *Candidate* = copied from an existing smoke run, needs Rob's approval / recapture on current build before it is the official baseline.

**Older candidates — stale vs 5.33.267:**

| object | file | source | build | state shown | PASS criteria |
|---|---|---|---|---|---|
| mm-list | baseline-mm-open.png | b401/dim215 | ~.215 | MM open, gdim 7 / mmdim 11 | strip 6996 focused; list chrome/badges/A–Z hidden; mmdim (not gdim) applied (K23–K38) |
| mm-warm | baseline-warm-music.png | b401/smoke222 | .222 | MM open on Music, audio | underlay = highlighted section; no flash; crossfade only while MM open |
| movies-list | baseline-mm-movies.png | b401/smoke222 | .222 | MM on Movies | underlay Movies, pills TITLES… |
| tv-list | baseline-mm-tv.png | b401/smoke218 | .218 | TV under MM | underlay TV; no jump back to Movies |
| music-list | baseline-music-list.png | smoke139 | .139 | Music list 60 | big album 1140,220 600×600; list 60 focused |
| now-playing | baseline-mm-with-np.png | b401/stress_20261027_t5015 | Oct 27 | MM + Now Playing | mini-player/NP visible, latch ≥2.5 s |
| skin-settings-tuner | baseline-tuner.png | bug007_smoke | — | Tuner 6970 | info panel x≈1010+, readable |
| home-splash | baseline-splash.png | bezel-warmgate-196 | .196 | splash | MM-first under splash, no key eat |
| idle-big-album-fold | fold-mid-259.png | b401/live_album_anim_259 | .259 (**pre-lock**) | mid-fold | locked spec: edge-on at 90°, no glare pop, frames sliced; **recapture on 267** |

## 5.33.267 recapture (Nov 1 2026, ~3:30 PM ET)
Captured on live **5.33.267** (version read via JSON-RPC) with an isolated Kodi: `HOME=/tmp/bz2home`, own Xvfb **:178** (not :77 — another Kodi with HOME=/home/box was already on :77 and was left alone), webserver 8099. Launcher: `/workspace/portgen/kr.sh`; helpers `/workspace/portgen/fvlib178.sh`. Status: **candidate (267)** until Rob approves; older files in each folder are **stale**.

| object | file | build | state shown | PASS criteria |
|---|---|---|---|---|
| idle-big-album-fold | 267-fold-mid-a.png | 5.33.267 | Daft Punk → Discovery, page mid-turn | locked spec: leaf hinged at slit x1440, half-frames sliced, no glare pop |
| idle-big-album-fold | 267-fold-hold.png | 5.33.267 | 10 s hold after a turn | full 600×600 cover at 1140,220, frame whole |
| idle-big-album-fold | 267-fold-mid-b.png | 5.33.267 | Discovery → RAM, mid-turn | as mid-a |
| music-list | 267-music-list.png | 5.33.267 | Artists list 60, Daft Punk focused, idle | big album 1140,220 600×600; info panel; list 60 focused |
| mm-list | 267-mm-open-tv.png | 5.33.267 | startup MM-first, TV SHOWS highlighted | strip 6996 focused, list chrome hidden |
| tv-list | 267-mm-on-tv.png | 5.33.267 | same frame as above (TV underlay) | underlay TV poster |
| movies-list | 267-mm-on-movies.png | 5.33.267 | MM on MOVIES | underlay Movies |
| mm-warm | 267-mm-on-music-warm.png | 5.33.267 | MM on MUSIC, no audio | underlay = Music section, dimmed |

**Blocked on 267 (old candidates kept, labeled stale):**
- **now-playing** — harness has no working audio decoder (`PAPlayer … Failed to create the decoder`), so nothing plays.
- **skin-settings-tuner** — MM SETTINGS → Right did not open Tuner 6970 in the driven run; entry path not found in time. Old `baseline-tuner.png` stays stale.
- **home-splash** — splash finished before the first grab; needs a capture loop started before Kodi launch.

General PASS (Rob): open-MM screenshot required; real Left/flip smoke; exclusive HOME. Objects with no folder have no baseline yet — capture on next smoke (r.sh → screenshot) and add a row.

## 5.33.267 captures (formerly blocked)
| screen | file | how captured |
|---|---|---|
| home-splash | `home-splash/267-splash-logo.png`, `267-splash-version.png`, `267-splash-handoff-mm.png` | `portgen/kr2.sh` starts a 4 fps x11grab loop *before* Kodi launches |
| skin-settings-tuner | `skin-settings-tuner/267-tuner.png` | Power menu 1118 → list 7800 item 3 TUNER (focus 6970); `ClearProperty(bz_mmidle,home)` immediately before the shot |
| tv-list | `tv-list/267-tv-list.png` | list 60, The Mandalorian |
| now-playing | `now-playing/267-music-list-np.png` | plays `portgen/np_test.mp3` (180 s tagged sine) by path; library test mp3s are ~2 s. Cover shows folder icon: test file has no art |
| now-playing (MM) | `now-playing/267-mm-idle-faded-np.png` | **MM idle state only** — bz_mmidle re-arms instantly under JSON-RPC input, so strip is faded and “PRESS ANY BUTTON” shows. An MM-awake+NP shot is still blocked (needs real key input) |
