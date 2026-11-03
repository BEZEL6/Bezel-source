# Artwork group (global artwork stage) — dialog 1122, group 6400
Version: 5.33.402 · Files: `xml/Custom_1122_BigAlbum.xml`, `xml/Includes_Bezel.xml` (BezelVPLPoster / BezelVPLPosterTap / BezelPoster60S), `scripts/bz_flip.py` (poster_clock → v60_mirror)

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
`bz_pready`, `bz_pswayon`, `bz_ppulse(2)` unchanged in timing; since 5.33.391 the poster's sway anchor is phase-locked to the album sway clock (`_art_sw_anchor`, Home `bz_art_t0`) so 6401 and 6402 swing on ONE clock and stay in phase through the crossfade (see `sway-animations.md`). All mirror props clear on bz_flip exit.

## Opacity — one shared gate (5.33.392 A2P)

- **5.33.394:** fade time (6401, 6402, handoff pre-warm) is driven by Tuner `bz_at_a2pfade` (ALBUM / POSTER > Poster ↔ album fade): 7 mutually exclusive Conditional fades per layer, 200/250/300/**400**/500/600/800 ms. "400 ms" below = default step.
- `$EXP[bz_artposter]` (Includes_Bezel) = `bz_vpl_on` | Videos handoff (`Window.IsActive(videos)` + `bz_tovideo=fade` / `bz_m2v_flat`) | `bz_tomusic`.
- **6401 poster:** 100 when `bz_artposter`, else 0 — 400 ms sine. Never Visible=false → texture + sway stay warm.
- **6402 album:** 0 when `bz_artposter` (except during `bz_tomusic`, return trip unchanged) **or** (`!bz_railvis` and no `bz_a2p_hold`), else 100 — **400 ms sine** (was 300). Same gate + same frame + same duration as 6401 → album→poster is ONE dissolve.
- `bz_a2p_hold` (bz_flip `_a2p_tick`, after v60_mirror each ~50 ms): when the Music window has just left (≤1.5 s) for Videos / a tovideo/m2v handoff and `bz_vpl_on` isn't up yet, the album is held at 100 so there's no gap; clears the moment the poster gate rises (or 1.5 s failsafe, or `bz_setopen`).
- Old album inner non-reversible fades (tovideo 600 / m2v_flat 500) removed — no album jump-back.
- Handoff pre-warm image: only during the handoff (bridges the gap before `bz_pready` arms the swaying stack).

## Per-screen
`View_60_BezelInfoList` and `View_60_BezelVideoPosterList` no longer draw the poster; they mount only `BezelVPLPosterTap` (button 6280, long-press → extended info) because nothing focusable may live in 1122.

## Restart
.py change → FULL restart.

## 5.33.368 — Music dual prewarm (DUALM)
- `bz_flip.py m_mirror()` (same poll as v60_mirror, after modal freeze): `bz_m_np_art` = Player.Art(thumb) while audio (not viz); `bz_m_idle_art` = Music list 60 focus (parent→NoWrap(1) thumb, thumb, icon), fallback `bz_cov_last`. Both hold last value.
- 5.33.369 MMHOLD: on MM open `under_adv` sets `bz_m_idle_lock` → `m_mirror` stops updating `bz_m_idle_art` (focused Music cover holds through warm/path churn). Lock clears on the first UADVRAND step (after `bz_uadv_hold`, default 5 s, min 3 s; then every `bz_uadv_delay` 8 s) or on MM close. Random only under MM with strip focus (+ RANDSTART at startup); never while browsing list 60.
- 5.33.401 UADVFOCUS: `under_adv` also requires `Control.HasFocus(6996)`. Focus off the MM strip → no Control.Move on list 60; last idle/warm item stays held until strip focus returns (then hold timer restarts via `opened = None`).
- 5.33.370 SETPOSTER latch: MM Settings/Add-ons set Home `bz_setopen` before `ClearProperty(bz_nav)`; while set, `v60_mirror` forces `bz_vpl_on` empty so 6401 stays at opacity 0 over the held `bz_v60_art`. Cleared by `v60_mirror` once 1130/1131/1117 is active (2 s failsafe).

## 5.33.372 — Poster hold (POSTERHOLD)
- `v60_mirror` never writes an undecoded path into `bz_v60_art`. New art → `bz_v60_next` (hidden preload image, colordiffuse 01FFFFFF, same size as the poster) → after 0.6 s promoted to `bz_v60_art`; the poster images then crossfade old→new from the decoded cache. Empty art = hold old path.
- List 60 gone in Videos while `bz_vpl_on` is set: hold `bz_vpl_on` + art for 1.5 s grace, or as long as MM is open (`bz_nav`) / `bz_tovideo` / `bz_m2v_flat` handoff runs. `bz_setopen` (370) still forces clear.
- Idle sync: the mirror reads list 60, which under MM is the random idle row (UADVRAND steps / WARM RANDSTART / saved session row), so the held poster is always the last random idle item shown; returning to Movies/TV restores that same row. Music `bz_m_*` / 369 MMHOLD untouched.


## Poster warm on Music→Movies/TV (5.33.382)
The poster layer only ever draws `bz_v60_art` (held last Videos poster, staged via `bz_v60_next`). In Music the mirror does not touch `bz_v60_art`, so it stays warm/decoded; when 6401 fades up for Movies/TV it already has the poster texture — opacity crossfade only, no texture swap. First Videos visit of a session (no held poster yet) shows the poster after the 0.6 s preload promote.

## Idle album A/B (current, 5.33.384)

## Dual poster holds (5.33.385 DUALHOLD)
- `bz_v60_mov` = last Movies poster, `bz_v60_tv` = last TV poster. Written by `v60_mirror` (`_v60_dualrec`) right after list-60 art is staged, only when the Videos list type (movies/sets vs tvshows/seasons/episodes) equals the target and the container is not updating.
- Target (`_v60_target`): MM open on strip 6996 → highlighted row `sec` (movies/tv; music/other = no target, nothing changes). MM closed → current Videos list type.
- `_v60_dualpick`: if the list is not the target type yet (on Music, on the other Videos type, or loading), list-60 staging is skipped and `bz_v60_art` is set straight to the matching hold (already decoded on its earlier visit). 6401 / BezelVPLPoster still reads only `bz_v60_art` → opacity-only layer swap, never Music art.
- No hold yet for that type (first visit this session) → keeps whatever `bz_v60_art` held; list 60 preload fills it (~0.6 s) as before.
- Both props cleared on Bezel leave with the other `bz_v60_*` props.

## Settings tree (5.33.389 Rob t2725) — single source of truth
One parent node owns the global artwork; kids only register membership.

```
MM (6996 strip, held poster/album lane)
└── SETTINGS  = $EXP[bz_setkids]   ← ONLY node artwork reads (bz_railvis album, bz_flip v60_mirror poster 6401)
    ├── hub   = $EXP[bz_set_hub]   1130 Settings · 1131 Add-ons · 1117 Media Sources · addonbrowser
    ├── kodi  = $EXP[bz_set_kodi]  settings · systemsettings · servicesettings · playersettings · mediasettings · interfacesettings · profiles · skinsettings
    └── tools = $EXP[bz_set_tools] systeminfo · eventlog · filemanager
```
- Membership lives in `xml/Includes_Bezel.xml` (bz_set_* branches); python mirror `SETTINGS_TREE` in `scripts/bz_flip.py` builds `_SETKIDS` from it.
- `python3 scripts/bz_tree_check.py` must print OK (branch-for-branch match).
- New kid (e.g. tuner 1140s): add window to ONE branch in both places → inherits held poster↔album opacity, idle random + Now Playing, no per-window art.

## Art state tree (5.33.390 Rob t2728) — single source of truth
The artwork HOME (1122 / group 6400) branched by STATE. Registry = `ART_TREE` in `scripts/bz_flip.py`; `bz_tree_check.py` asserts every prop is live code. Leave-clear derives from `poster.*` (same 12 props as 389; album.* holds as before).

```
ART HOME (1122 · 6400 · bz_rail=hide is the only hard hide)
├── POSTER layer 6401 (under) — draws only bz_v60_art
│   ├── live   bz_v60_next → (0.6 s decode) → bz_v60_art · gate bz_vpl_on
│   ├── hold   bz_v60_mov (Movies) · bz_v60_tv (TV) — picked by MM row / list type
│   └── meta   lbl · parent · scroll · watched · resume · episodes · m60_art
├── ALBUM layer 6402 (over) — opacity $EXP[bz_railvis]
│   └── np     bz_m_np_art (over idle while Player.HasAudio)
└── GATES (opacity only, 400 ms sine — never Visible remount)
    ├── setkids  $EXP[bz_setkids] + bz_setopen latch → poster 0, album holds
    ├── a2p      $EXP[bz_artposter] + bz_a2p_hold → album down / poster up together, 400 ms sine (5.33.392)
    └── handoff  bz_tovideo / bz_m2v_flat / bz_tomusic → poster 100 during crossfade
```
New art state = add a branch/prop to ART_TREE + draw it in 1122; never a per-window art copy.


## MM → Settings kids latch (5.33.395)

**Simple.** Opening Settings, Add-ons, Files or Kodi info from MM keeps the held poster/album up — no fade to black.

**Wiring.** `bz_mm.py` sets `bz_setopen` for settings/addons/files/kodi. `bz_flip.v60_mirror`: while latched, it returns early and holds `bz_vpl_on` + `bz_v60_art` (no clear). Latch ends when any `$EXP[bz_setkids]` window is active (then the SETKIDS branch stages the held MM lane) or after 2 s.
- SETHOLD: while the MM strip is on the SETTINGS row (`Container(6996).ListItem.Property(sec)` = settings, e.g. after Back from a Settings kid such as FILE MANAGER), `under_adv` does no UADVRAND step, so the held Settings/Files art stays fixed while MM stays open. Scrolling to another row or closing MM ends the hold. bz_flip.py under_adv. FULL restart.
- MMAUDIO (5.33.397): while the MM is open and audio is playing (no video), `$EXP[bz_mmaudio]` keeps the big album (6402) up on every strip row — Music, Movies, TV, Recent, Favourites, Search, Pictures, Add-ons, Settings, Media Sources, Power. It forces `bz_railvis` true and `bz_artposter` false, so the poster layer 6401 stays down. With no audio, or with MM closed, the existing Music album / A2P poster rules apply. Includes_Bezel.xml.

**No MM auto-hide (5.33.398 NOAUTOHIDE, Rob t2799u):** the strip 6996 / group 6894 stays visible and focusable the whole time MM is open. There is no idle fade, no park button 6897, no `bz_mmidle`, no idle label / clearart stage, no wake path (WAKEGRACE/IDLEPARK/IDLERESET), and no Tuner Auto-hide row. mmdim and the colour backdrop follow plain MM-open rules. MMHOLD on MM open is unchanged.

## ONE art style (5.33.399 ONEART, Rob t2809–t2814) — current state, supersedes any Visible-gate notes above
**Simple.** Every art layer (poster 6401 stack, album 6402, MM A/B poster/fanart/music lanes, held fanart under 1117 / Add Source / Pictures) is always mounted. Python (`bz_flip.py`) owns the state as Home properties; XML only draws and fades **opacity** (Conditional fade, sine). No art control uses `<visible>` to come and go, and focus never drives art.
**Rules.** Navigation (strip 6996, lists, buttons, Tuner rows) = focus. Chrome (panels, dims, frames, labels) may use Visible. Art = opacity only. The only hard hide left is group 6400 `bz_rail=hide`.
**Wiring.**
- `$EXP[bz_pshow]` = `bz_pready` (Videos sway armed) **or** `$EXP[bz_setkids]`, and not `bz_mmmushide`. It is the one gate for the swaying poster stack (400 ms opacity) and its frame. Before .399 the stack was `<visible>bz_pready</visible>`, and `bz_pready` only arms inside Videos, so every SETTINGS kid (1117 Media Sources first) remounted the stack empty → blank poster with `bz_vpl_on=1`.
- SETTINGS kids (1117, 1130, 1131, addonbrowser, Kodi settings, systeminfo/eventlog/filemanager): `v60_mirror` stages the held MM lane if there is one, otherwise **holds the last `bz_v60_art`** and keeps `bz_vpl_on=1` (it used to clear the gate when `bz_pos_on` was empty). With audio only playing, `bz_vpl_on` is cleared → the album owns the slot (unchanged).
- Lane images that were `<visible>C</visible>` + Visible/Hidden fades are now `Conditional` fade 100→0 on `![C]`, using the old Hidden time (1500 ms lanes, 300/400 elsewhere). The live-only 1500 ms Visible variants (`bz_ab_live`) fold into the single Conditional time.
- Dead `<visible>false</visible>` art images removed (4).
- By design (not art layers, kept Visible): NP prev/next cover chips (`MusicPlayer.offset(±1).Cover`), poster frame/blur chrome, black under-cover in 1117. Search/Pictures with no art stay empty — no art invented.

## 5.33.400 — WARMLANE (F2: Music→Movies under the MM)
- While `bz_mmwarm` is set (a warm swap/restore is in flight), list 60 still sits on Kodi's remembered row (e.g. a stale Oppenheimer/Inception). In that window:
  - `ab_clock` does not tick the A/B lanes, so the art holds.
  - `_v60_dualpick` keeps the per-type hold (`bz_v60_mov` / `bz_v60_tv`) and doesn't stage list-60 art.
  - `_v60_dualrec` doesn't record a hold.
- The art retargets only after `_restore` lands the session row. The opacity-hold style is unchanged.
- Known residual: on the first Movies visit of a session there is no `bz_v60_mov` hold yet, so the last poster on screen (which can be a TV poster) can show for about 0.4 s before the correct poster.
