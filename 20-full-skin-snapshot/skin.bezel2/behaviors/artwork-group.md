# Artwork group (global artwork stage) — dialog 1122, group 6400
Version: 5.33.367 · Files: `xml/Custom_1122_BigAlbum.xml`, `xml/Includes_Bezel.xml` (BezelVPLPoster / BezelVPLPosterTap / BezelPoster60S), `scripts/bz_flip.py` (poster_clock → v60_mirror)

## What it is
One always-open modeless dialog (1122) holds **all** right-side artwork in group **6400**, so nothing remounts when you change section:
- **6401 poster layer (under)** — the one Movies/TV poster: full `BezelVPLPoster` (sway, cast, glares, LOOK, watched/resume badge, frame, blur placeholder, MM live twins + A/B lanes) inside `BezelSecDim`, plus a flat handoff pre-warm image.
- **6402 album layer (over)** — big album + leaf-flip/sway + cast + Compact NP (rides 6397/FS rails), inside BezelSecDim. Opacity-gated by `$EXP[bz_railvis]`.
- Colour strip and MM Warm underlay are **not** in this group. `bz_rail=hide` is the only hard hide (6400 Visible).

## Data: list-60 Home mirror
1122 cannot read `Container(60)` (it only resolves in the control's own window — t4097). `bz_flip.py` `poster_clock` calls `v60_mirror()` every ~50 ms, **after** the modal/busy/info freeze (so dialogs never blank the stage), and writes Window(Home) props:
| prop | source |
|---|---|
| `bz_v60_art` | Videos poster = old `$VAR[BezelPoster60V]` (parent `..` → next item poster/tvshow.poster; poster; tvshow.poster; bz_hold_poster when bz_arthold; Icon) |
| `bz_m60_art` | Music twin art = old `$VAR[BezelPoster60M]` (thumb / next-item thumb / Icon) |
| `bz_v60_lbl` / `bz_v60_parent` / `bz_v60_scroll` | label non-empty / IsParentFolder / Scrolling |
| `bz_v60_watched` / `bz_v60_resume` | PlayCount>0 / IsResumable (badge) |
| `bz_v60_episodes` | Container.Content(episodes) (cast hide) |
| `bz_vpl_on` | old mount gates: Videos = list 60 visible + !bz_gridv + !episodes + !actors; Music/playlist/favourites/programs/games info-list = list 60 visible + !(music artists/albums/songs) + !episodes |
`bz_pready`, `bz_pswayon`, `bz_ppulse(2)` unchanged (same shared sway clock — no second sway system). All mirror props clear on bz_flip exit.

## Opacity (6401)
- 100 when `bz_vpl_on` **or** a Music↔Videos handoff runs (`Window.IsActive(videos)` + `bz_tovideo=fade` / `bz_m2v_flat`, or `bz_tomusic`); else 0 (400 ms sine). Never Visible=false → texture + sway stay warm.
- Handoff pre-warm image: only during the handoff (bridges the gap before `bz_pready` arms the swaying stack).
- Album 6402 rules unchanged (railvis, tovideo 600 / m2v_flat 500 fades).

## Per-screen
`View_60_BezelInfoList` and `View_60_BezelVideoPosterList` no longer draw the poster; they mount only `BezelVPLPosterTap` (button 6280, long-press → extended info) because nothing focusable may live in 1122.

## Restart
.py change → FULL restart.

## 5.33.368 — Music dual prewarm (DUALM)
- `bz_flip.py m_mirror()` (same poll as v60_mirror, after modal freeze): `bz_m_np_art` = Player.Art(thumb) while audio (not viz); `bz_m_idle_art` = Music list 60 focus (parent→NoWrap(1) thumb, thumb, icon), fallback `bz_cov_last`. Both hold last value.
- Big album base image in `BezelMusicPlayingArt` is now two stacked always-drawn images (idle under, NP over), same rect/zoom/sway parent. NP fades 0 on `!Player.HasAudio`; idle fades 0 on `Player.HasAudio` (400 ms sine). No Visible remount. `BezelBigArt` var kept but unused there.
- 5.33.369 MMHOLD: on MM open `under_adv` sets `bz_m_idle_lock` → `m_mirror` stops updating `bz_m_idle_art` (focused Music cover holds through warm/path churn). Lock clears on the first UADVRAND step (after `bz_uadv_hold`, default 5 s, min 3 s; then every `bz_uadv_delay` 8 s) or on MM close. Random only under MM (+ RANDSTART at startup); never while browsing list 60.
