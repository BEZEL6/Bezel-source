# BEZEL Port Blueprint — master index

**Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state · Rob ask t2001u

## Simple
This is **one blueprint** for Bezel (skin.bezel2), in seven peer layers plus screen baselines. It does two jobs: (1) the **living UI reference** for Bezel as it ships today, and (2) the **instruction set** to rebuild Bezel natively (e.g. SwiftUI + AVPlayer, Kodi removed). Every object has one kebab-case **object id**; the same id names its file in every layer. Every file has two tiers: **Simple** (plain overview) then **Deep** (rebuild detail: IDs, coords, props, ms, pixels, keys).

## The blueprint layers (all equal peers)
| layer | answers | folder |
|---|---|---|
| **behaviors** | *feel* — what it does, how it flows, why (Simple / How it works / Wiring) | [behaviors/](behaviors/README.md) |
| **layout** | *where* — controls, x/y/w/h, focus edges, camera/pivot, z-order | [layout/](layout/README.md) |
| **state** | *when* — Home props / flags, conditions, transitions, resets | [state/](state/README.md) |
| **motion** | *how fast* — durations, easing, delays, holds; locked vs tunable | [motion/](motion/README.md) |
| **art** | *with what* — every image, px size, mask, colordiffuse, stacking | [art/](art/README.md) |
| **input** | *by which key* — keys/touch → platform-agnostic actions | [input/](input/README.md) |
| **theme** | *what colour/font* — palette, packs, fonts, dim/glare tokens | [theme/](theme/README.md) |
| **port-refs** | *what it must look like* — approved screen baselines for smoke + visual diff | [port-refs/](port-refs/README.md) |

## Standing update rule (Rob)
Current state only, never a changelog. Any live change updates **every affected layer file for that object in the same build** (behavior + layout/state/motion/art/input/theme + baseline screen if the look changed). Locked objects (e.g. `idle-big-album-fold`, `mm-warm`) change only when Rob asks.

## Source of truth
Until a native rebuild exists, **Kodi XML + Python in this tree are the truth**; these docs abstract feel and geometry from it. If a doc and the code disagree, the code wins and the doc is fixed in the same build. Deep tiers cite `file Lnnn` so you can jump to the code. Layout/state/motion/art/input Deep tiers were extracted from live code by `/workspace/portgen/gen.py` (re-run after big changes) and hand-verified for core objects.

## Reading order for a porter
1. [layout/resolution.md](layout/resolution.md) — canvas 1920×1080, coordinate model, anchors.
2. [theme/tokens.md](theme/tokens.md) · [motion/tokens.md](motion/tokens.md) — design tokens.
3. [state/home-properties.md](state/home-properties.md) — the global store.
4. [input/keymap-overview.md](input/keymap-overview.md) — action vocabulary.
5. [art/media-map.md](art/media-map.md) — asset catalog.
6. Core objects in order: `home-splash` → `mm-list` → `mm-warm` → `section-transitions` → `music-list` → `idle-big-album-fold` → `movies-list` → `tv-list` → `now-playing` → `dialogue-fs` → `dust` → `skin-settings-tuner`; then the rest. For each: behavior → layout → state → motion → art → input → port-refs.

## How layers relate
behavior says **what/why** and links down; layout gives **where**; state names the **switches** layout's visibility uses; motion times the transitions those switches trigger; art lists what's drawn at those coords; input says which key flips which switch; theme supplies colours/fonts/dim. port-refs is the acceptance test. Never copy one layer's content into another — link by object id.

## Smoke + port diff
Baselines in `port-refs/<id>/` are what the screen must look like. Use them (a) to **smoke** each Bezel build (same screen, same state → compare) and (b) to **visual-diff** the native rebuild against Bezel at 1920×1080. PASS criteria per object in `port-refs/README.md`.

## Object map
Core objects first. `—` = that layer has no object-specific data (uses globals).

| object id | status | behavior | layout | state | motion | art | input | theme | screens |
|---|---|---|---|---|---|---|---|---|---|
| `mm-list` | approved | [behaviors](behaviors/mm-list.md) | [layout](layout/mm-list.md) | [state](state/mm-list.md) | [motion](motion/mm-list.md) | [art](art/mm-list.md) | [input](input/mm-list.md) | [tokens](theme/tokens.md) | [screens](port-refs/mm-list/) |
| `mm-warm` | LOCKED | [behaviors](behaviors/mm-warm.md) | [layout](layout/mm-warm.md) | [state](state/mm-warm.md) | [motion](motion/mm-warm.md) | [art](art/mm-warm.md) | [input](input/mm-warm.md) | [tokens](theme/tokens.md) | [screens](port-refs/mm-warm/) |
| `music-list` | Live in 5 | [behaviors](behaviors/music-list.md) | [layout](layout/music-list.md) | [state](state/music-list.md) | [motion](motion/music-list.md) | [art](art/music-list.md) | [input](input/music-list.md) | [tokens](theme/tokens.md) | [screens](port-refs/music-list/) |
| `movies-list` | Live in 5 | [behaviors](behaviors/movies-list.md) | [layout](layout/movies-list.md) | [state](state/movies-list.md) | [motion](motion/movies-list.md) | [art](art/movies-list.md) | [input](input/movies-list.md) | [tokens](theme/tokens.md) | [screens](port-refs/movies-list/) |
| `tv-list` | Live in 5 | [behaviors](behaviors/tv-list.md) | [layout](layout/tv-list.md) | [state](state/tv-list.md) | [motion](motion/tv-list.md) | [art](art/tv-list.md) | [input](input/tv-list.md) | [tokens](theme/tokens.md) | [screens](port-refs/tv-list/) |
| `now-playing` | Live in 5 | [behaviors](behaviors/now-playing.md) | [layout](layout/now-playing.md) | [state](state/now-playing.md) | [motion](motion/now-playing.md) | [art](art/now-playing.md) | [input](input/now-playing.md) | [tokens](theme/tokens.md) | [screens](port-refs/now-playing/) |
| `idle-big-album-fold` | **APPROVED — LOCKED 100% (Rob, Nov 1 202 | [behaviors](behaviors/idle-big-album-fold.md) | [layout](layout/idle-big-album-fold.md) | [state](state/idle-big-album-fold.md) | [motion](motion/idle-big-album-fold.md) | [art](art/idle-big-album-fold.md) | [input](input/idle-big-album-fold.md) | [tokens](theme/tokens.md) | [screens](port-refs/idle-big-album-fold/) |
| `dialogue-fs` | draft | [behaviors](behaviors/dialogue-fs.md) | [layout](layout/dialogue-fs.md) | [state](state/dialogue-fs.md) | [motion](motion/dialogue-fs.md) | [art](art/dialogue-fs.md) | [input](input/dialogue-fs.md) | [tokens](theme/tokens.md) | — |
| `dust` | draft | [behaviors](behaviors/dust.md) | [layout](layout/dust.md) | [state](state/dust.md) | [motion](motion/dust.md) | [art](art/dust.md) | [input](input/dust.md) | [tokens](theme/tokens.md) | — |
| `skin-settings-tuner` | Live in 5 | [behaviors](behaviors/skin-settings-tuner.md) | [layout](layout/skin-settings-tuner.md) | [state](state/skin-settings-tuner.md) | [motion](motion/skin-settings-tuner.md) | [art](art/skin-settings-tuner.md) | [input](input/skin-settings-tuner.md) | [tokens](theme/tokens.md) | [screens](port-refs/skin-settings-tuner/) |
| `home-splash` | live | [behaviors](behaviors/home-splash.md) | [layout](layout/home-splash.md) | [state](state/home-splash.md) | [motion](motion/home-splash.md) | [art](art/home-splash.md) | [input](input/home-splash.md) | [tokens](theme/tokens.md) | [screens](port-refs/home-splash/) |
| `section-transitions` | Standard (Rob voice Oct 30 2026) | [behaviors](behaviors/section-transitions.md) | [layout](layout/section-transitions.md) | [state](state/section-transitions.md) | [motion](motion/section-transitions.md) | [art](art/section-transitions.md) | [input](input/section-transitions.md) | [tokens](theme/tokens.md) | — |
| `addons` | draft | [behaviors](behaviors/addons.md) | [layout](layout/addons.md) | [state](state/addons.md) | [motion](motion/addons.md) | [art](art/addons.md) | [input](input/addons.md) | [tokens](theme/tokens.md) | — |
| `bezel-logo-back` | draft | [behaviors](behaviors/bezel-logo-back.md) | [layout](layout/bezel-logo-back.md) | [state](state/bezel-logo-back.md) | [motion](motion/bezel-logo-back.md) | [art](art/bezel-logo-back.md) | [input](input/bezel-logo-back.md) | [tokens](theme/tokens.md) | — |
| `big-album-pill` | live on both windows | [behaviors](behaviors/big-album-pill.md) | [layout](layout/big-album-pill.md) | [state](state/big-album-pill.md) | [motion](motion/big-album-pill.md) | [art](art/big-album-pill.md) | [input](input/big-album-pill.md) | [tokens](theme/tokens.md) | — |
| `context-menu` | draft | [behaviors](behaviors/context-menu.md) | [layout](layout/context-menu.md) | [state](state/context-menu.md) | [motion](motion/context-menu.md) | [art](art/context-menu.md) | [input](input/context-menu.md) | [tokens](theme/tokens.md) | — |
| `dialog-busy` | draft | [behaviors](behaviors/dialog-busy.md) | [layout](layout/dialog-busy.md) | [state](state/dialog-busy.md) | [motion](motion/dialog-busy.md) | [art](art/dialog-busy.md) | [input](input/dialog-busy.md) | [tokens](theme/tokens.md) | — |
| `dialog-confirm` | draft | [behaviors](behaviors/dialog-confirm.md) | [layout](layout/dialog-confirm.md) | [state](state/dialog-confirm.md) | [motion](motion/dialog-confirm.md) | [art](art/dialog-confirm.md) | [input](input/dialog-confirm.md) | [tokens](theme/tokens.md) | — |
| `fanart-fs` | draft | [behaviors](behaviors/fanart-fs.md) | [layout](layout/fanart-fs.md) | [state](state/fanart-fs.md) | [motion](motion/fanart-fs.md) | [art](art/fanart-fs.md) | [input](input/fanart-fs.md) | [tokens](theme/tokens.md) | — |
| `favourites` | draft | [behaviors](behaviors/favourites.md) | [layout](layout/favourites.md) | [state](state/favourites.md) | [motion](motion/favourites.md) | [art](art/favourites.md) | [input](input/favourites.md) | [tokens](theme/tokens.md) | — |
| `filebrowser` | draft | [behaviors](behaviors/filebrowser.md) | [layout](layout/filebrowser.md) | [state](state/filebrowser.md) | [motion](motion/filebrowser.md) | [art](art/filebrowser.md) | [input](input/filebrowser.md) | [tokens](theme/tokens.md) | — |
| `files-filemanager` | draft | [behaviors](behaviors/files-filemanager.md) | [layout](layout/files-filemanager.md) | [state](state/files-filemanager.md) | [motion](motion/files-filemanager.md) | [art](art/files-filemanager.md) | [input](input/files-filemanager.md) | [tokens](theme/tokens.md) | — |
| `fullscreen-pill` | draft | [behaviors](behaviors/fullscreen-pill.md) | [layout](layout/fullscreen-pill.md) | [state](state/fullscreen-pill.md) | [motion](motion/fullscreen-pill.md) | [art](art/fullscreen-pill.md) | [input](input/fullscreen-pill.md) | [tokens](theme/tokens.md) | — |
| `fullscreen-video` | draft | [behaviors](behaviors/fullscreen-video.md) | [layout](layout/fullscreen-video.md) | [state](state/fullscreen-video.md) | [motion](motion/fullscreen-video.md) | [art](art/fullscreen-video.md) | [input](input/fullscreen-video.md) | [tokens](theme/tokens.md) | — |
| `info-options` | draft | [behaviors](behaviors/info-options.md) | [layout](layout/info-options.md) | [state](state/info-options.md) | [motion](motion/info-options.md) | [art](art/info-options.md) | [input](input/info-options.md) | [tokens](theme/tokens.md) | — |
| `keyboard` | draft | [behaviors](behaviors/keyboard.md) | [layout](layout/keyboard.md) | [state](state/keyboard.md) | [motion](motion/keyboard.md) | [art](art/keyboard.md) | [input](input/keyboard.md) | [tokens](theme/tokens.md) | — |
| `keymaps` | draft | [behaviors](behaviors/keymaps.md) | [layout](layout/keymaps.md) | [state](state/keymaps.md) | [motion](motion/keymaps.md) | [art](art/keymaps.md) | [input](input/keymaps.md) | [tokens](theme/tokens.md) | — |
| `media-sources` | draft | [behaviors](behaviors/media-sources.md) | [layout](layout/media-sources.md) | [state](state/media-sources.md) | [motion](motion/media-sources.md) | [art](art/media-sources.md) | [input](input/media-sources.md) | [tokens](theme/tokens.md) | — |
| `mm-mini-player` | draft | [behaviors](behaviors/mm-mini-player.md) | [layout](layout/mm-mini-player.md) | [state](state/mm-mini-player.md) | [motion](motion/mm-mini-player.md) | [art](art/mm-mini-player.md) | [input](input/mm-mini-player.md) | [tokens](theme/tokens.md) | — |
| `music-controls` | Live in 5 | [behaviors](behaviors/music-controls.md) | [layout](layout/music-controls.md) | [state](state/music-controls.md) | [motion](motion/music-controls.md) | [art](art/music-controls.md) | [input](input/music-controls.md) | [tokens](theme/tokens.md) | — |
| `music-fanart-fs` | draft — built, not smoke-tested on devic | [behaviors](behaviors/music-fanart-fs.md) | [layout](layout/music-fanart-fs.md) | [state](state/music-fanart-fs.md) | [motion](motion/music-fanart-fs.md) | [art](art/music-fanart-fs.md) | [input](input/music-fanart-fs.md) | [tokens](theme/tokens.md) | — |
| `music-videos-list` | Live in 5 | [behaviors](behaviors/music-videos-list.md) | [layout](layout/music-videos-list.md) | [state](state/music-videos-list.md) | [motion](motion/music-videos-list.md) | [art](art/music-videos-list.md) | [input](input/music-videos-list.md) | [tokens](theme/tokens.md) | — |
| `music-viz-settings` | Present in the 5 | [behaviors](behaviors/music-viz-settings.md) | [layout](layout/music-viz-settings.md) | [state](state/music-viz-settings.md) | [motion](motion/music-viz-settings.md) | [art](art/music-viz-settings.md) | [input](input/music-viz-settings.md) | [tokens](theme/tokens.md) | — |
| `np-bar` | Live in 5 | [behaviors](behaviors/np-bar.md) | [layout](layout/np-bar.md) | [state](state/np-bar.md) | [motion](motion/np-bar.md) | [art](art/np-bar.md) | [input](input/np-bar.md) | [tokens](theme/tokens.md) | — |
| `pause-overlay` | Live in 5 | [behaviors](behaviors/pause-overlay.md) | [layout](layout/pause-overlay.md) | [state](state/pause-overlay.md) | [motion](motion/pause-overlay.md) | [art](art/pause-overlay.md) | [input](input/pause-overlay.md) | [tokens](theme/tokens.md) | — |
| `pictures` | Live in 5 | [behaviors](behaviors/pictures.md) | [layout](layout/pictures.md) | [state](state/pictures.md) | [motion](motion/pictures.md) | [art](art/pictures.md) | [input](input/pictures.md) | [tokens](theme/tokens.md) | — |
| `play-next` | Live | [behaviors](behaviors/play-next.md) | [layout](layout/play-next.md) | [state](state/play-next.md) | [motion](motion/play-next.md) | [art](art/play-next.md) | [input](input/play-next.md) | [tokens](theme/tokens.md) | — |
| `playlists` | Live in 5 | [behaviors](behaviors/playlists.md) | [layout](layout/playlists.md) | [state](state/playlists.md) | [motion](motion/playlists.md) | [art](art/playlists.md) | [input](input/playlists.md) | [tokens](theme/tokens.md) | — |
| `power-menu` | Live in 5 | [behaviors](behaviors/power-menu.md) | [layout](layout/power-menu.md) | [state](state/power-menu.md) | [motion](motion/power-menu.md) | [art](art/power-menu.md) | [input](input/power-menu.md) | [tokens](theme/tokens.md) | — |
| `recently-played` | Live in 5 | [behaviors](behaviors/recently-played.md) | [layout](layout/recently-played.md) | [state](state/recently-played.md) | [motion](motion/recently-played.md) | [art](art/recently-played.md) | [input](input/recently-played.md) | [tokens](theme/tokens.md) | — |
| `search` | Live in 5 | [behaviors](behaviors/search.md) | [layout](layout/search.md) | [state](state/search.md) | [motion](motion/search.md) | [art](art/search.md) | [input](input/search.md) | [tokens](theme/tokens.md) | — |
| `settings` | Live in 5 | [behaviors](behaviors/settings.md) | [layout](layout/settings.md) | [state](state/settings.md) | [motion](motion/settings.md) | [art](art/settings.md) | [input](input/settings.md) | [tokens](theme/tokens.md) | — |
| `sway-animations` | Live | [behaviors](behaviors/sway-animations.md) | [layout](layout/sway-animations.md) | [state](state/sway-animations.md) | [motion](motion/sway-animations.md) | [art](art/sway-animations.md) | [input](input/sway-animations.md) | [tokens](theme/tokens.md) | — |
| `swipe-to-spin-poster` | **PARKED, not approved, not shipped | [behaviors](behaviors/swipe-to-spin-poster.md) | — | — | — | — | — | [tokens](theme/tokens.md) | — |
| `touch-group` | Live in 5 | [behaviors](behaviors/touch-group.md) | [layout](layout/touch-group.md) | [state](state/touch-group.md) | [motion](motion/touch-group.md) | [art](art/touch-group.md) | [input](input/touch-group.md) | [tokens](theme/tokens.md) | — |
| `video-osd` | Live in 5 | [behaviors](behaviors/video-osd.md) | [layout](layout/video-osd.md) | [state](state/video-osd.md) | [motion](motion/video-osd.md) | [art](art/video-osd.md) | [input](input/video-osd.md) | [tokens](theme/tokens.md) | — |

`swipe-to-spin-poster` is **PARKED** (not shipped) — behavior only, no port layers.
