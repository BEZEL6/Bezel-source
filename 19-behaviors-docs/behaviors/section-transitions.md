# Section transitions (STANDARD)

**Object:** `bz_secload` / `bz_secfade` (MyVideoNav / MyMusicNav section parent group) · `bz_cmd.py _bz_load_then_close` · includes `BezelSecFadeIn`, `BezelSecFadeInDialog`, `BezelWindowFade`, `BezelOpenCloseSet`, `BezelSecDim` (Includes_Animations / Includes_Bezel ~L3548)
**Where:** Every section and sub-page opened from the main menu
**Last updated:** 2026-10-31
**Status:** Standard (Rob voice Oct 30 2026). Fade in only, 400 ms sine out. No fade-out, zoom or slide on close. Section↔MM art handoff is LOCKED with Warm 2.0 mirror-enter (5.33.207; see mm-warm.md → Section enter / exit).
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## The standard (reference = MM → TV Shows)

### Simple
Every screen you open from the main menu appears with one quick, gentle fade-in, and nothing else. Screens don't fade out, zoom or slide when they close. The library sections (Movies, TV, Music, Recently Played) wait until their list and picture are ready, so you never see them half-loaded.

### How it works
- **Library sections** load behind the MM:
  1. `bz_cmd.py` sets `bz_secload` and activates the window. A 0 ms Conditional fade holds the section parent group at opacity 0.
  2. The script waits for the window and the new folder path, re-issuing `Container.Update(…,replace)` if Kodi kept a drilled subfolder, then polls until the focused item's poster, thumb or icon is known. Then it pauses 0.15 s for the texture loader. The code comment puts the overall cap at about 3 s, so a slow Shield never hangs.
  3. In one step it sets `bz_secfade`, clears `bz_secload`, and clears `bz_nav`/`bz_navtune`/`bz_navbez`, so the MM closes as the section fades in. The fade is a non-reversible 400 ms sine-out Conditional.
  4. 0.6 s later, `bz_secfade` is cleared.
- **Warm shortcut:** if the exact list is already active under the MM and not updating, the script clears `bz_secload` and the nav props and returns, so the menu just closes.
- **Everything else** uses a WindowOpen-only fade include. With no WindowClose animation, closing is an instant swap back to the window below, which is already drawn.
- **TV↔Movies A/B art lanes** (1.5 s / 300 ms, BUG-015 hold) are a separate art crossfade and aren't part of this standard.

### Wiring
| Piece | Value |
|---|---|
| Hold | section parent: `fade 100→0 time 0` Conditional on `!String.IsEmpty(Window(Home).Property(bz_secload))` (MyVideoNav also on `bz_gpend`) |
| Fade | `fade 0→100 time 400 sine out reversible=false` Conditional on `bz_secfade` |
| Script | `bz_cmd.py _bz_load_then_close(win, path)` (~L400–433), called by `tomusic` (Music) and `go` (Videos) |
| `BezelSecFadeIn` | WindowOpen fade 0→100, 400 ms sine out |
| `BezelSecFadeInDialog` | same + `DepthDialog` |
| `BezelOpenCloseSet` | same (Settings / SettingsCategory) |
| `BezelWindowFade` | same (Includes_Bezel ~L3548) |

---

## Coverage

### Simple
Every level gets the same fade: Settings and its sub-pages, Add-ons, Pictures, Search, Favourites, Media Sources and file pages, Power, Playlists, PVR, Weather, Programs, Games and Event log. Pop-ups that aren't section menus (notifications, keyboards, OSDs, info dialogs) keep their own animations.

### How it works
Each window includes exactly one of the four fade includes. Pictures and Playlists also wrap their parent group in `BezelSecDim`, so the MM global dim applies:
- **gdim:** `bz_at_gdim` 1–6 → 30–60 %, !navmenu.
- **mmdim:** `bz_at_mmdim` 1–11, default 2 = 10 %, navmenu.

Both dims use 600 ms fades.

### Wiring
| Include | Windows |
|---|---|
| `BezelSecFadeIn` | AddonBrowser, 1100, 1117, 1118, EventLog, FileManager, Includes_MediaMenu, MyMusicPlaylistEditor, PVR*, SettingsProfile, SystemInfo, SkinSettings |
| `BezelSecFadeInDialog` | 1101, 1107, DialogAddonSettings, DialogMediaSource, DialogSettings, FileBrowser |
| `BezelOpenCloseSet` | Settings, SettingsCategory |
| `BezelWindowFade` | MyFavourites, MyGames, MyPics, MyPlaylist, MyPrograms, MyWeather |
| `BezelSecDim` | section parent groups (MyVideoNav, MyMusicNav, MyPics, MyPlaylist, 1112) |

Not covered (not section menus): notifications, keyboard / numeric / slider / volume, OSDs (VideoOSD has its own 300 ms fade), info dialogs.

---

## Section ↔ MM art (LOCKED with Warm 2.0 — 5.33.207 mirror-enter)

Full detail: **mm-warm.md → Section enter / exit**. Summary:
**Applies to ALL main-menu sections** (Music, Movies, TV, Recently Played, Search, Media Sources seeded; Favourites, Pictures, Add-ons, Settings, Power = art N/A). Audit table in mm-warm.md.

| Path | What happens |
|------|----------------|
| **Enter** | Section art pops in at full opacity underneath; MM lane art fades out 1500 ms over it |
| **Exit** | Lanes pre-seeded with on-screen art while MM closed; MM opens on that image at full opacity same frame (`bz_ab_live` gates Visible fade — fade only for side flips while MM already open). No timed hold. No black flash |

Shared Music / Movies / TV. Code: `bz_flip.py` seed + `Includes_Bezel.xml` conditional Visible. Do not change without Rob approval.

## Related
mm-list.md · mm-warm.md · settings.md · video-osd.md
