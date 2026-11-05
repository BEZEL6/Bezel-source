# Artwork group (global art stage)

**Object:** the one place all right-side artwork lives · Kodi: dialog `1122` group `6400` · poster layer `6401` (under) · album layer `6402` (over) · includes `BezelVPLPoster`, `BezelVPLPosterTap`, `BezelPoster60S` · `bz_flip.py` `poster_clock` → `v60_mirror`, `m_mirror`, `_a2p_tick`
**Where:** right of the strip (x 1140), over every section
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none (the MM warm art lanes it borrows from are LOCKED, see [mm-warm](mm-warm.md))

## Simple
The swaying Movies / TV poster and the big Music album share one stage on the right. Only one shows at a time, and switching between them is a single dissolve: the album fades out exactly while the poster fades in, both already swaying in step. The stage never empties when you open Settings, Add-ons or other tools from the menu: it keeps the last picture. Poster changes crossfade only after the new picture is fully loaded, so you never see black.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Album | Music lists; any MM row while audio plays | poster wanted | big album (layer over) |
| Poster | Movies / TV lists (or info lists in Music / playlists / favourites / programs) | album wanted | swaying poster (layer under) |
| Handoff | Music ↔ Movies / TV | 400 ms | both at once, crossfading |
| Held | Settings / Add-ons / Media sources / Files / Kodi info opened from the MM | back | last poster or album, unchanged |
| Hidden | a screen asks for no art (`hide`) | — | nothing |

### Timeline
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| album → poster | album fades out, poster fades in, same frame | 400 (Tuner 200–800) | sine |
| new poster | loaded hidden; after ≥ 600 ms promoted; old → new crossfade | 600 + image fade | — |
| MM Movies ↔ TV row change | held poster of that type crossfades in | 1000 | sine |
| leaving Music for Movies | album held at 100 % until the poster is up (≤ 1500 failsafe) | — | — |
| MM idle album A/B | album dissolve between idle picks | 400 (Tuner 200–800) | sine |

### Interruptions
- Scrolling fast: only the last decoded poster is promoted; intermediate ones never flash.
- A new item with no art: the old picture stays.
- A modal dialog / busy / info page opens: the mirror freezes; the stage keeps what it shows.

### Continuity
- Both layers are always present and swaying on the same clock; changes are opacity only.
- Movies and TV each keep their last poster, ready decoded, for instant MM row switches.
- Returning to Movies / TV restores the same row and poster.

### Layering
Poster layer (under): poster sway stack, cast, glare, badge, frame, blur placeholder, preload images · Album layer (over): big album, leaf / sway, cast, compact NP. Both under MM chrome and fullscreen chrome.

### Geometry
Album 1140, 220, 600 × 600. Poster: same column, 2:3 portrait (600 × 900 preload size), rotation axis x 1290.

### Art
- Poster: focused item's poster (parent folder → next item's poster / show poster; poster; show poster; icon).
- Album: playing cover while audio, else the focused Music item's thumb (or the last cover).
- No art → keep the last; never a placeholder; Music art never appears in the poster frame.

### Input
None (display only). The screens keep only a tap target over the poster (long-press → extended info).

### Speed targets
Album ↔ poster dissolve 400 ms; first poster of a session within ~0.6 s.

### Never
- No dip to black between album and poster (392, 413 P2BHOLD).
- No visibility toggling of art layers; opacity only (399 ONEART).
- No blank poster under Settings kids (399, 370).
- No Music album in the poster frame (382).
- No fade-to-black on MM Movies ↔ TV row changes (385, 419).

### Acceptance checks
1. Music → MM → Movies: one 400 ms dissolve album → poster, both mid-swing in step.
2. Scroll a movie list fast: poster updates without black frames.
3. MM → Settings → Back: poster unchanged all the way.
4. MM: move between Movies and TV rows: each row's last poster appears instantly.

## Kodi implementation (sandbox)

### How it works
- **Why a mirror (Workaround).** 1122 can't read `Container(60)` of another window, so `poster_clock` runs `v60_mirror()` every ~50 ms (after the modal / busy / info freeze) and writes Home props; `m_mirror()` does the same for Music. Writes go through `_v60_set` (467 OWNSHADOW: skips an unchanged value it wrote; 472: trusts the copy for 1 s, then re-reads Kodi).
- **Poster props:** `bz_v60_next` (preload slot, alpha 01) → promoted to `bz_v60_art` after ≥ 0.6 s; `bz_v60_lbl` / `_parent` / `_scroll` / `_watched` / `_resume` / `_episodes`; `bz_vpl_on` (mount gate); holds `bz_v60_mov` / `bz_v60_tv` (`_v60_dualrec`, `_v60_dualpick`, `_v60_target`), both kept decoded by alpha-01 images (419 HOLDWARM).
- **Music props:** `bz_m_np_art` (playing thumb), `bz_m_idle_art` (focused Music thumb; locked on MM open by `bz_m_idle_lock` until the first random step), `bz_m60_art` (mirrored, not drawn).
- **Gates:** `$EXP[bz_artposter]` = `bz_vpl_on` | Videos handoff (`bz_tovideo=fade` / `bz_m2v_flat`) | `bz_tomusic`. 6401 = 100 when `bz_artposter`; 6402 = 0 when `bz_artposter` (except `bz_tomusic`) or (`!bz_railvis` and no `bz_a2p_hold`). Fade time `bz_at_a2pfade` (7 steps 200 / 250 / 300 / **400** / 500 / 600 / 800). `bz_a2p_hold` (`_a2p_tick`): album held ≤ 1.5 s after leaving Music until the poster gate rises. `$EXP[bz_mmaudio]` (MM + audio) forces album up, poster down. `$EXP[bz_pshow]` = `bz_pready` or `bz_setkids`, not `bz_mmmushide`; `bz_pready` holds once armed (413).
- **Settings tree:** `$EXP[bz_setkids]` = hub (1130, 1131, 1117, addonbrowser) | kodi settings windows | tools (systeminfo, eventlog, filemanager); Python mirror `SETTINGS_TREE`; `scripts/bz_tree_check.py` must print OK. `bz_setopen` latch (set by `bz_mm.py` before closing the MM; ends when a kid window is active or after 2 s) holds the art.
- **Art state registry:** `ART_TREE` in bz_flip; leave-clear derives from it.
- **Warm swaps:** while `bz_mmwarm` is set, no lane ticks and no list-60 staging (400 WARMLANE).
- **Startup:** group 6400 alpha 0 while `bz_warm_gate`, then 3000 ms fade (see [home-splash](home-splash.md)).

### Wiring
| Item | Value |
|---|---|
| Layers | 6400 group (`bz_rail=hide` = only hard hide), 6401 poster, 6402 album |
| Tap target | `BezelVPLPosterTap` button 6280 in `View_60_BezelInfoList` / `View_60_BezelVideoPosterList` |
| Expressions | `bz_artposter`, `bz_railvis`, `bz_mmaudio`, `bz_pshow`, `bz_setkids`, `bz_set_hub`, `bz_set_kodi`, `bz_set_tools` |
| Tuner | `bz_at_a2pfade`, `bz_at_midlefade` (idle album A/B, default 400 ms), `bz_at_warmmusicposters` |
| Python | `v60_mirror`, `m_mirror`, `_a2p_tick`, `_v60_set`, `_v60_dualrec`, `_v60_dualpick`, `ART_TREE`, `SETTINGS_TREE` |
| Restart | Python change → full Kodi restart |

### Kodi workarounds (do not port)
- The Home-property mirror of list 60, the preload slot and alpha-01 warm images: Kodi has no cross-window data binding and no "texture decoded" event. A port binds the stage to the focused item and crossfades on image-loaded.
- The `bz_setopen` / `bz_a2p_hold` latches: cover Kodi window switches that briefly have no list.
- Nothing focusable inside 1122: modeless dialogs get no keys.

## Related
[big-album](big-album.md) · [sway-animations](sway-animations.md) · [mm-warm](mm-warm.md) · [movies-list](movies-list.md) · [tv-list](tv-list.md) · [home-splash](home-splash.md)
