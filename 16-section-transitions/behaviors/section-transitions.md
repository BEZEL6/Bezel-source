# Section transitions — STANDARD

**Object:** `bz_secload`/`bz_secfade` (MyVideoNav/MyMusicNav parent) · includes `BezelSecFadeIn`, `BezelSecFadeInDialog`, `BezelWindowFade`, `BezelOpenCloseSet` (Includes_Animations / Includes_Bezel)
**Last updated:** 2026-10-31 · 5.33.194 (catch-up sync to live tree)  
**Status:** standard (Rob voice Oct 30 2026)

## The standard (reference = MM → TV Shows)
- Fade **in only**: opacity 0 → 100, **400 ms, sine, easing out**.
- **No fade-out**, no zoom, no slide on close (since 5.33.132).
- Movies/TV/Music/Recently Played: section parent held hidden (`bz_secload`) until list+art load, then one `bz_secfade` Conditional 400 ms sine out (bz_cmd `_bz_load_then_close`).
- Every other window / sub-page: `WindowOpen` fade 0→100 400 sine out via `BezelSecFadeIn` (dialogs: `BezelSecFadeInDialog`, keeps DepthDialog).
- TV↔Movies A/B art lanes (1.5 s / 300 ms, BUG-015 hold) are a separate art crossfade — not changed.

## Coverage
All levels incl. Settings sub-pages (SettingsCategory, Profile, SystemInfo, SkinSettings, settings dialogs), Add-ons (browser, launcher, addon settings), Pictures, Search (1107), Favourites, Media Sources/Files (1117, FileManager, MediaSource, FileBrowser), Power (1118), Playlists, PVR, Weather, Programs, Games, Event log, media side menu.
Not covered (not section menus): notifications, keyboard/numeric/slider/volume, OSDs, info dialogs.

## Related
mm-list.md · mm-warm.md · settings.md
