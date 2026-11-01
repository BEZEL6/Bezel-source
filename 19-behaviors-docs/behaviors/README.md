# BEZEL behavior files

**Last updated:** 2026-10-31

**Standing rule (Rob):** every time a system changes, its behavior file is updated in the same build to match the new **current state** — the file documents how the system works now, not a changelog.

- One Markdown file per object / screen (kebab-case). Never merge objects (MM ≠ Music list).
- Header: title · Object (paths/IDs) · Last updated (date · build) · Status (`approved` / `draft` / `parked`).
- **Standing format rule:** every behavior file uses the three layers **Simple** / **How it works** / **Wiring** for each major section, taken from the **live code** (XML, Python), at the detail level of `mm-warm.md`. Thin or stub objects still get all three layers. PARKED designs say clearly that they're not shipped.
- `.bak_*` files are history — never edit or delete.

## Index
| File | Purpose (current state) |
|---|---|
| addons.md | Add-ons browser under MM |
| bezel-logo-back.md | Bezel logo acts as Back (touch) |
| context-menu.md | Section menu 1119 (replaces Kodi context menu) |
| dialog-busy.md | Busy spinner dialog |
| dialog-confirm.md | Yes/No confirm dialog |
| big-album-pill.md · dialogue-fs.md | Big album pill 6401 (1120 + album viz); Dialogue FS album mode; album strip 6397 |
| dust.md | Dust 2.0 dialog 1114 + Dust3; all dust tuner rows incl. size 90/100/125% |
| fanart-fs.md | Fanart FS / visualisation keys and touch |
| favourites.md | Favourites under MM |
| filebrowser.md | File browser dialog |
| files-filemanager.md | File manager |
| fullscreen-pill.md | FS pill 6886 on section strip / hidden in FS contexts |
| fullscreen-video.md | Fullscreen video |
| home-splash.md | Home splash / MM-first startup |
| info-options.md | Options+Info (Video/Music info, bz_ci_more pages) |
| keymaps.md | zz_bezel2_* profile keymaps: install on Bezel, delete all three + reload on leave (5.33.194) |
| media-sources.md | Media sources window 1117 |
| mm-list.md | MM strip 6996: rows, Up/Down wrap, pill cycles, SETTINGS Select-only (approved, live) |
| mm-mini-player.md | MM mini-player 6958 |
| mm-warm.md | WARM 2.0 underlay, A/B lanes fixed 1500ms, mushide, artists underlay |
| movies-list.md | Movies list 60, Up wrap→6098, pills, poster hold |
| music-controls.md | Music controls dialog 1115 |
| music-list.md | Music list 60, Up wrap→6097, big album + NP grouplist 6397 |
| music-videos-list.md | Music videos list |
| music-viz-settings.md | Music visualisation settings |
| now-playing.md | Now Playing 1112 + compact Music NP |
| np-bar.md | NP bar |
| pause-overlay.md | Pause screen 1116 |
| pictures.md | Pictures |
| play-next.md | 1120 Play Next mode (bz_dfs_mode toggle), Fanart sides |
| playlists.md | Playlists |
| power-menu.md | Power menu dialog 1118, list 7800: SHUTDOWN/QUIT/SUSPEND/SLEEP/TUNER, BEZEL version label |
| recently-played.md | Recently played |
| search.md | Search dialog 1107 |
| section-transitions.md | Fade-in-only section open standard; Section ↔ MM art (LOCKED) → mm-warm.md |
| settings.md | Kodi Settings, Back → MM opener row |
| skin-settings-tuner.md | BEZEL Tuner 6970 (group 6975): open/back by opener, value steps, presets, batched reload, dtap rows |
| sway-animations.md | Shared sway clock, album/poster rotatey, stub cast |
| swipe-to-spin-poster.md | PARKED design — not approved |
| touch-group.md | Tap targets + double-tap Select (no touch master in live tree) |
| tv-list.md | TV list 60, Up wrap→6098, pills |
| video-osd.md | Video OSD |

- `music-fanart-fs.md` — Music Fanart FS dialog 1121
