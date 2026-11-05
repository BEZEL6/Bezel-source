# Section transitions (standard)

**Object:** section open / switch standard for every screen opened from the MM · **Where:** all sections and their sub-pages
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live (Rob standard, Oct 30 2026) · **Lock:** the section ↔ MM art handoff is LOCKED (see [mm-warm](mm-warm.md))

## Simple
Every screen you open from the main menu (MM) appears with one quick, gentle fade-in and nothing else. Screens don't fade out, zoom or slide away. Library sections (Music, Movies, TV, Recently played) stay hidden until their list and the focused item's picture are ready, so you never see them half-loaded. The rows then drop in one after another (the cascade). The background picture never blinks: the section's art is already there under the menu, and the menu's art fades away over it.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| MM open, section behind | MM row focused | Select a row | MM chrome + MM art lanes over the section that row belongs to (warm) |
| Loading | Select a library row whose list is not ready | list + focused art ready, or 3 s cap | section held at 0 %; MM still drawn |
| Fading in | ready | 400 ms later | section fades 0 → 100 %, MM closes in the same step |
| Rows cascading | section entered | last row landed | rows hidden for the entry hold, then drop in one by one |
| Section live | cascade done | MM open (Back / Menu) | section, full opacity |
| Warm shortcut | Select a row whose exact list is already behind the MM | — | MM just closes; no fade, no load |
| Other screens (settings, add-ons, pictures …) | opened | closed | one window fade-in; closing is an instant swap to the screen below |

### Timeline
**Library section from the MM**
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| 0 | Select. Section window activates hidden (0 %) under the MM | — | — |
| 0 – ≤3000 | wait: window up, right folder, focused item's art known; then +150 ms for the texture | until ready | — |
| ready | section fades in; MM chrome closes at the same instant | 400 | sine out, not reversible |
| ready | MM art lanes fade out over the section's art (art already at 100 % underneath) | 1500 | sine in-out (LOCKED) |
| entry +350 | rows start to cascade | each row 286, stagger 30 | Tuner cascade |
| ≈ entry +1040 | 15th row landed | — | — |

**MM open over a section**
| t (ms) | What | Duration | Curve |
|---|---|---|---|
| 0 | MM chrome fades in over the section; MM art lanes are already at 100 % on frame 1 (seeded with the on-screen art) | 286 | sine out |
| close | MM chrome fades out | 250 | sine in |

**Switching between sections while the MM is open (warm switch)**: the MM row moves; after a 0.2 s park the section behind swaps under the MM; its art is held until the new list has art (≤ 0.9 s) and the MM art lanes cross over 1500 ms (LOCKED, see [mm-warm](mm-warm.md)). A Movies → TV switch measured ≈ 1.3 s on Rob's box (468 log).

**Other screens**: 400 ms fade-in on open, sine out. Close: none.

### Interruptions
- Back during Loading: the load is abandoned; the MM stays.
- A second Select while loading: ignored until the section is live.
- MM opened while rows are still cascading: rows keep their place; the cascade is not replayed when the MM closes again.
- MM warm swaps (section changes under an open MM) never replay the cascade.
- Load cap 3 s: if art never arrives the section fades in anyway (never hang).

### Continuity
- The section's background art must be on screen at full opacity before the MM art fades off it: no frame of black between (LOCKED handoff).
- Opening the MM shows exactly the art that was on screen, on the first frame.
- The big album layer (sway, glare, dust) runs through every section change untouched.

### Layering
Section window (fading in) < big album layer < MM art lanes < MM chrome < dialogs.

### Geometry
No movement. Everything appears in its final position; only opacity changes.

### Art
Section art is the focused item's fanart / poster / thumb. The section waits for it (≤ 3 s). No placeholder.

### Input
| Action | Result |
|---|---|
| Select on MM row | open that section (rules above) |
| Back / Menu in a section | MM opens over it |
| Back in a sub-page | previous page, instant swap |

### Speed targets
- Rows visible ≤ 0.45 s after the section is live (350 ms hold + one poll).
- Section live ≤ 0.6 s after Select when the library answers quickly.
- Never wait more than 3 s.

### Never
- No fade-out of the old section, no zoom, no slide (177 standard; 458 "no fade out of section").
- No dip to black under the MM on open or close (430, 431, 458 → 460 MMDIMQUICK).
- No visible 1.5 s wait on MM dim (458 "the 1.5 delay makes it look broke").
- No MM slide (469).
- No half-loaded section (list without art).

### Acceptance checks
1. MM → Movies: the list appears in one fade, poster already there, rows cascade; no black frame.
2. Movies → MM → Movies: the MM opens on the same art; closes with no cascade replay.
3. MM row TV ↔ Movies quickly: background swaps under the menu, no flash.
4. MM → Settings: one fade-in; Back: instant.
5. Pull the network share: the section still opens within 3 s.

## Kodi implementation (sandbox)

### How it works
- **Library sections (Intent).** `bz_cmd.py _bz_load_then_close(win, path)` (called by `tomusic` / `go`):
  1. sets Home `bz_secload`; activates the window; the section parent group has a 0 ms Conditional fade to 0 while `bz_secload` is set (MyVideoNav also on `bz_gpend`).
  2. polls (50 ms steps): window active, path right (re-issues `Container.Update(path,replace)` if Kodi kept a drilled subfolder), focused item's poster / thumb / icon known; then waits 0.15 s.
  3. in one step sets `bz_secfade`, clears `bz_secload` and `bz_nav` / `bz_navtune` / `bz_navbez` (MM closes as the section fades in). Fade: 400 ms sine out, `reversible=false`, Conditional on `bz_secfade`.
  4. clears `bz_secfade` 0.6 s later.
  - Warm shortcut: exact list already active and not updating → clear `bz_secload` + nav props, return.
- **Row cascade.** `bz_flip.py nav_menu`: on a section entry `casc_pend` holds the rows (`bz_casc_fp`) for `_ENTRYHOLD` = 0.35 s, then rows animate with the Tuner cascade speed / stagger (baked into list layouts by `bz_tune_patch`). Warm swaps under the MM (`bz_nav` / `bz_mmwarm`) never replay it (`bz_casc_force` overrides). LISTTIME logs `BEZEL list <entry|open> <path> rows after <s> n=<items>`.
- **Other windows.** Each includes one WindowOpen-only fade include; no WindowClose, so close is an instant swap.
- **MM enter / leave.** BezelNavMenu chrome uses `BezelATMenuAnim` (Visible fade in, Hidden fade out), times baked from Tuner Menu open / close (286 / 250 ms). Art lanes are not faded on MM enter: mirror-enter seeds them (mm-warm).
- **Dims.** `BezelSecDim` on section parents: `bz_at_gdim` (1–6 → 30–60 %, MM closed) and `bz_at_mmdim` (MM open; default 10 %); 600 ms fades, no delay (460).
- **Warm switch.** `bz_flip.py mm_warm` (LOCKED). It reads `bz_at_mmsecfade` into `_xf` (0 / 0 / 0.15 / 0.25 / 0.35 / 0.5 / 0.7 / 1.0 s) but only writes it to the debug log; no fade uses it, so the 471 FASTPACK Section fade pick has no visible effect.

### Wiring
| Piece | Value |
|---|---|
| Hold | section parent `fade 100→0 time 0` Conditional `!String.IsEmpty(Window(Home).Property(bz_secload))` |
| Fade | `fade 0→100 time 400 sine out reversible=false` Conditional `bz_secfade` |
| Script | `bz_cmd.py _bz_load_then_close`, actions `tomusic`, `go` |
| Entry hold | `bz_flip.py` `_ENTRYHOLD = 0.35`, `casc_pend`, `bz_casc_fp`, `bz_casc_force` |
| `BezelSecFadeIn` | WindowOpen fade 0→100, 400 ms sine out: AddonBrowser, 1100, 1117, 1118, EventLog, FileManager, Includes_MediaMenu, MyMusicPlaylistEditor, PVR*, SettingsProfile, SystemInfo, SkinSettings |
| `BezelSecFadeInDialog` | same + `DepthDialog`: 1101, 1107, DialogAddonSettings, DialogMediaSource, DialogSettings, FileBrowser |
| `BezelOpenCloseSet` | same: Settings, SettingsCategory |
| `BezelWindowFade` | same: MyFavourites, MyGames, MyPics, MyPlaylist, MyPrograms, MyWeather |
| `BezelSecDim` | MyVideoNav, MyMusicNav, MyPics, MyPlaylist parent groups |
| `BezelATMenuAnim` | baked by `bz_tune_patch._tuner` from `MOPEN` / `MCLOSE` tables |
| Tuner | `bz_at_mmsecfade`, `bz_at_menuopen`, `bz_at_menuclose`, `bz_at_cascspeed`, `bz_at_cascstag`, `bz_at_gdim`, `bz_at_mmdim` |

### Kodi workarounds (do not port)
- The "held at 0 % until ready" trick exists because Kodi shows a window before its list and textures load. A native port should simply build the screen off-screen and show it when ready.
- `Container.Update(…,replace)` re-issue: Kodi sometimes restores a previously drilled subfolder.
- The 0.15 s texture pause: Kodi's texture loader is asynchronous with no "loaded" event.
- `bz_secfade` cleared after 0.6 s only so the Conditional can fire again next time.
- `bz_cmd.py` still runs a harmless `Dialog.Close(1112,true)` (dialog removed in 465).

## Related
[mm-warm](mm-warm.md) · [mm-list](mm-list.md) · [settings](settings.md) · [skin-settings-tuner](skin-settings-tuner.md) · [video-osd](video-osd.md)
