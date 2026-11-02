# Artwork group (global artwork stage) — dialog 1122, group 6400
Version: 5.33.385 · Files: `xml/Custom_1122_BigAlbum.xml`, `xml/Includes_Bezel.xml` (BezelVPLPoster / BezelVPLPosterTap / BezelPoster60S), `scripts/bz_flip.py` (poster_clock → v60_mirror)

## What it is
One always-open modeless dialog (1122) holds **all** right-side artwork in group **6400**, so nothing remounts when you change section:
- **6401 poster layer (under)** — the one Movies/TV poster: full `BezelVPLPoster` (sway, cast, glares, LOOK, watched/resume badge, frame, blur placeholder, MM live twins + A/B lanes) inside `BezelSecDim`, plus a flat handoff pre-warm image.
- **6402 album layer (over)** — big album + leaf-flip/sway + cast + Compact NP (rides 6397/FS rails), inside BezelSecDim. Opacity-gated by `$EXP[bz_railvis]`.
- Colour strip and MM Warm underlay are **not** in this group. `bz_rail=hide` is the only hard hide (6400 Visible).

## Data: list-60 Home mirror
1122 cannot read `Container(60)` (it only resolves in the control's own window — t4097). `bz_flip.py` `poster_clock` calls `v60_mirror()` every ~50 ms, **after** the modal/busy/info freeze (so dialogs never blank the stage), and writes Window(Home) props:
| prop | source |
|---|---|
| `bz_v60_next` | 5.33.372 preload slot: new Videos poster path staged here first (near-invisible 600×900 image in 6401) |
| `bz_v60_art` | Videos poster (promoted from `bz_v60_next` after ≥0.6 s; empty new art keeps the old path) = old `$VAR[BezelPoster60V]` (parent `..` → next item poster/tvshow.poster; poster; tvshow.poster; bz_hold_poster when bz_arthold; Icon) |
| `bz_m60_art` | Music list thumb (still mirrored; **not drawn by 6401** since 5.33.382 — the poster layer's Music twins, Music A/B lanes (bz_mart_a/b) + BezelPoster60S LOOK read `bz_v60_art`, so Music album art never appears in the poster frame; album art lives only in 6402) |
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
- 5.33.370 SETPOSTER latch: MM Settings/Add-ons set Home `bz_setopen` before `ClearProperty(bz_nav)`; while set, `v60_mirror` forces `bz_vpl_on` empty so 6401 stays at opacity 0 over the held `bz_v60_art`. Cleared by `v60_mirror` once 1130/1131/1117 is active (2 s failsafe).

## 5.33.372 — Poster hold (POSTERHOLD)
- `v60_mirror` never writes an undecoded path into `bz_v60_art`. New art → `bz_v60_next` (hidden preload image, colordiffuse 01FFFFFF, same size as the poster) → after 0.6 s promoted to `bz_v60_art`; the poster images then crossfade old→new from the decoded cache. Empty art = hold old path.
- List 60 gone in Videos while `bz_vpl_on` is set: hold `bz_vpl_on` + art for 1.5 s grace, or as long as MM is open (`bz_nav`) / `bz_tovideo` / `bz_m2v_flat` handoff runs. `bz_setopen` (370) still forces clear.
- Idle sync: the mirror reads list 60, which under MM is the random idle row (UADVRAND steps / WARM RANDSTART / saved session row), so the held poster is always the last random idle item shown; returning to Movies/TV restores that same row. Music `bz_m_*` / 369 MMHOLD untouched.


## Poster warm on Music→Movies/TV (5.33.382)
The poster layer only ever draws `bz_v60_art` (held last Videos poster, staged via `bz_v60_next`). In Music the mirror does not touch `bz_v60_art`, so it stays warm/decoded; when 6401 fades up for Movies/TV it already has the poster texture — opacity crossfade only, no texture swap. First Videos visit of a session (no held poster yet) shows the poster after the 0.6 s preload promote.
- 5.33.383 IDLERESET: MM auto-hide wake now restarts the idle album/poster hold — the cover on screen at wake is re-locked (bz_m_idle_lock) and the UADVRAND timer restarts (bz_uadv_hold, default 5 s, min 3 s) before random resumes every bz_uadv_delay. Before: random timer kept running through hide, so a step could swap art right as the strip faded back in. bz_flip.py under_adv. FULL restart.

## Idle album A/B (current, 5.33.384)
Idle Music big album in the 1122 album layer draws two always-loaded images: `bz_m_idle_a` / `bz_m_idle_b`; `bz_m_idle_side` (a|b, empty=a) picks the shown one. Each has a Conditional 400 ms sine fade-out when `Player.HasAudio` or it is not the shown side; the NP layer (`bz_m_np_art`) is unchanged. `bz_flip.py` `_m_idle_stage()` (called from `m_mirror`): first cover goes straight into the shown slot; later covers go to the hidden slot, wait 0.6 s to decode, then flip side and set `bz_m_idle_art` (= cover on screen, used by MMHOLD/IDLERESET locks). Hidden slot is not written until 0.45 s after a flip. Random steps (UADVRAND, MM + startup only) therefore crossfade, never pop; after MM wake the 383 hold applies, then the next random step crossfades.

## Dual poster holds (5.33.385 DUALHOLD)
- `bz_v60_mov` = last Movies poster, `bz_v60_tv` = last TV poster. Written by `v60_mirror` (`_v60_dualrec`) right after list-60 art is staged, only when the Videos list type (movies/sets vs tvshows/seasons/episodes) equals the target and the container is not updating.
- Target (`_v60_target`): MM open on strip 6996 → highlighted row `sec` (movies/tv; music/other = no target, nothing changes). MM closed → current Videos list type.
- `_v60_dualpick`: if the list is not the target type yet (on Music, on the other Videos type, or loading), list-60 staging is skipped and `bz_v60_art` is set straight to the matching hold (already decoded on its earlier visit). 6401 / BezelVPLPoster still reads only `bz_v60_art` → opacity-only layer swap, never Music art.
- No hold yet for that type (first visit this session) → keeps whatever `bz_v60_art` held; list 60 preload fills it (~0.6 s) as before.
- Both props cleared on Bezel leave with the other `bz_v60_*` props.
