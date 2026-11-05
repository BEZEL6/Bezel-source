# BEZEL Port Blueprint — master index

**Last updated:** 2026-11-04 · 5.33.473 · **Status:** current-state

## Simple
This is the blueprint for Bezel (skin.bezel2). It does two jobs: (1) the living reference for Bezel as it ships today in Kodi (the sandbox), and (2) the instruction set to rebuild Bezel on another framework without losing its feel or look. Since 5.33.473 the blueprint is **one file per object** in [behaviors/](behaviors/README.md). Each file has:
- **Simple** — what a user sees and does;
- **Feel contract (any framework)** — states, timelines (ms + curves), interruptions, continuity, layering, geometry (1920×1080), art, input, speed targets, the Never list (rejected looks, with the build that taught it) and acceptance checks;
- **Kodi implementation (sandbox)** — the live mechanism, ids and properties, and the Kodi-only workarounds a port must not copy.

Global tokens (canvas, layout columns, curves with cubic-bezier values, default timings, global layering and the global Never list) are in [behaviors/README.md](behaviors/README.md).

## Retired layers
`layout/ state/ motion/ art/ input/ theme/` were generated at 5.33.267 and are **retired**: each file carries a banner and may be out of date. `port-refs/` (screen baselines) is not in the tree. The behavior files replace all of them.

## Standing rules (Rob)
- Current state only, never a changelog; a file is updated in the same build as the change it describes.
- If a file and the code disagree, the code wins and the file is fixed in the same build.
- Locked objects (`mm-warm`, `leaf-flip`, `idle-big-album-fold`) change only when Rob asks; their files are still kept current.

## Reading order for a porter
1. [behaviors/README.md](behaviors/README.md) — tokens, format, global rules.
2. [section-transitions](behaviors/section-transitions.md) · [mm-list](behaviors/mm-list.md) · [mm-warm](behaviors/mm-warm.md) · [home-splash](behaviors/home-splash.md).
3. [big-album](behaviors/big-album.md) · [artwork-group](behaviors/artwork-group.md) · [sway-animations](behaviors/sway-animations.md) · [dust](behaviors/dust.md).
4. [music-list](behaviors/music-list.md) · [movies-list](behaviors/movies-list.md) · [tv-list](behaviors/tv-list.md).
5. [music-fanart-fs](behaviors/music-fanart-fs.md) · [dialogue-fs](behaviors/dialogue-fs.md) · [play-next](behaviors/play-next.md) · [np-bar](behaviors/np-bar.md) · [music-controls](behaviors/music-controls.md).
6. Everything else in the object map.

## Source of truth
Until a native rebuild exists, the Kodi XML + Python in this tree are the truth; the behavior files abstract feel and geometry from it and cite names (includes, ids, expressions, functions), not line numbers.

## Object map
| id | Object | Status | Lock | File |
|---|---|---|---|---|
| `addons` | Add-ons | live | — | [behaviors/addons.md](behaviors/addons.md) |
| `artwork-group` | Artwork group (global art stage) | live | partly locked | [behaviors/artwork-group.md](behaviors/artwork-group.md) |
| `bezel-logo-back` | Bezel logo (Back) | live | — | [behaviors/bezel-logo-back.md](behaviors/bezel-logo-back.md) |
| `big-album-pill` | Big album pill | live | — | [behaviors/big-album-pill.md](behaviors/big-album-pill.md) |
| `big-album` | Big album layer | live | — | [behaviors/big-album.md](behaviors/big-album.md) |
| `context-menu` | Section menu (context) | live | — | [behaviors/context-menu.md](behaviors/context-menu.md) |
| `dialog-busy` | Busy indicator | live | — | [behaviors/dialog-busy.md](behaviors/dialog-busy.md) |
| `dialog-confirm` | Confirm (Yes / No) | live | — | [behaviors/dialog-confirm.md](behaviors/dialog-confirm.md) |
| `dialogue-fs` | Dialogue FS | live | — | [behaviors/dialogue-fs.md](behaviors/dialogue-fs.md) |
| `dust` | Dust | live | — | [behaviors/dust.md](behaviors/dust.md) |
| `fanart-fs` | Fanart FS (Kodi visualisation window) | live (fallback) | — | [behaviors/fanart-fs.md](behaviors/fanart-fs.md) |
| `favourites` | Favourites | live | — | [behaviors/favourites.md](behaviors/favourites.md) |
| `filebrowser` | File browser | live | — | [behaviors/filebrowser.md](behaviors/filebrowser.md) |
| `files-filemanager` | File manager | live | — | [behaviors/files-filemanager.md](behaviors/files-filemanager.md) |
| `fullscreen-pill` | FULLSCREEN pill (Music list) | live | — | [behaviors/fullscreen-pill.md](behaviors/fullscreen-pill.md) |
| `fullscreen-video` | Fullscreen video | live | — | [behaviors/fullscreen-video.md](behaviors/fullscreen-video.md) |
| `home-splash` | Startup splash and first MM | live | LOCKED | [behaviors/home-splash.md](behaviors/home-splash.md) |
| `idle-big-album-fold` | Idle big album fold (book-page leaf) | live, **off by default** (Tuner › Album / Poster › Leaf flip) | LOCKED | [behaviors/idle-big-album-fold.md](behaviors/idle-big-album-fold.md) |
| `info-options` | Options + Info | live | — | [behaviors/info-options.md](behaviors/info-options.md) |
| `keyboard` | Keyboard | live | — | [behaviors/keyboard.md](behaviors/keyboard.md) |
| `keymaps` | Keymaps | live | — | [behaviors/keymaps.md](behaviors/keymaps.md) |
| `leaf-flip` | Leaf flip (family index) | idle use live (off by default), other uses not shipped | LOCKED | [behaviors/leaf-flip.md](behaviors/leaf-flip.md) |
| `media-sources` | Media sources | live | — | [behaviors/media-sources.md](behaviors/media-sources.md) |
| `mm-autohide` | MM auto-hide and pill idle return | live | — | [behaviors/mm-autohide.md](behaviors/mm-autohide.md) |
| `mm-list` | Main menu (MM) strip | live (approved) | LOCKED | [behaviors/mm-list.md](behaviors/mm-list.md) |
| `mm-mini-player` | MM mini player | live | — | [behaviors/mm-mini-player.md](behaviors/mm-mini-player.md) |
| `mm-warm` | MM warm (WARM 2.0.1 + VWARM) | live | LOCKED | [behaviors/mm-warm.md](behaviors/mm-warm.md) |
| `movies-list` | Movies list | live | — | [behaviors/movies-list.md](behaviors/movies-list.md) |
| `music-controls` | Music controls | live | — | [behaviors/music-controls.md](behaviors/music-controls.md) |
| `music-fanart-fs` | Music Fanart FS (Bezel fullscreen music) | live | — | [behaviors/music-fanart-fs.md](behaviors/music-fanart-fs.md) |
| `music-list` | Music list | live | — | [behaviors/music-list.md](behaviors/music-list.md) |
| `music-videos-list` | Music videos list | live (reachable from Kodi paths / sources only) | — | [behaviors/music-videos-list.md](behaviors/music-videos-list.md) |
| `music-viz-settings` | Music OSD settings (Kodi popup) | present, unreachable from Bezel (no opener) | — | [behaviors/music-viz-settings.md](behaviors/music-viz-settings.md) |
| `now-playing` | Now Playing (routes) | live (routes); old Now Playing dialog retired | — | [behaviors/now-playing.md](behaviors/now-playing.md) |
| `np-bar` | Now Playing bars and NP mode | live | — | [behaviors/np-bar.md](behaviors/np-bar.md) |
| `pause-overlay` | Pause screen | live | — | [behaviors/pause-overlay.md](behaviors/pause-overlay.md) |
| `pictures` | Pictures | live | — | [behaviors/pictures.md](behaviors/pictures.md) |
| `play-next` | Play Next and Up Next | live | — | [behaviors/play-next.md](behaviors/play-next.md) |
| `playlists` | Playlists | live | — | [behaviors/playlists.md](behaviors/playlists.md) |
| `power-menu` | Power menu | live | — | [behaviors/power-menu.md](behaviors/power-menu.md) |
| `recently-played` | Recently played | live | — | [behaviors/recently-played.md](behaviors/recently-played.md) |
| `search` | Search | live | — | [behaviors/search.md](behaviors/search.md) |
| `section-transitions` | Section transitions (standard) | live (Rob standard, Oct 30 2026) | LOCKED | [behaviors/section-transitions.md](behaviors/section-transitions.md) |
| `settings` | Settings | live | — | [behaviors/settings.md](behaviors/settings.md) |
| `skin-settings-tuner` | BEZEL Tuner | live (rail layout approved 439) | — | [behaviors/skin-settings-tuner.md](behaviors/skin-settings-tuner.md) |
| `sway-animations` | Sway animations | live | — | [behaviors/sway-animations.md](behaviors/sway-animations.md) |
| `swipe-to-spin-poster` | Swipe-to-spin poster (PARKED) | **PARKED** (not approved, not shipped; don't build unless Rob asks) | — | [behaviors/swipe-to-spin-poster.md](behaviors/swipe-to-spin-poster.md) |
| `touch-group` | Touch and double-tap | live | — | [behaviors/touch-group.md](behaviors/touch-group.md) |
| `tv-list` | TV list | live | — | [behaviors/tv-list.md](behaviors/tv-list.md) |
| `video-osd` | Video OSD | live | — | [behaviors/video-osd.md](behaviors/video-osd.md) |
