# BEZEL (skin.bezel2) — open bugs

### BUG-027 — Left/Back from Music/Movies/TV: Main Menu underlay pops (no soft fade) (2026-10-31, Rob voice; noted on 5.33.167)
**Symptom:** Left or Back from Music, Movies, or TV makes Main Menu load with a flash/pop instead of a smooth fade-in. Other sections do not require this unbroken fade. Used to be smooth before 5.33.162.
**Cause:** 5.33.162 BUG-012 set MM A/B lane-a Visible fade to 300ms (fast under outgoing b). On MM open, lane a is usually the active side with nothing underneath, so art pops in 300ms instead of the old 1500ms sine.
**Status:** FIXED 5.33.185 — lane-a Visible → 1500ms sine inout (fan + 3 pos pairs). Hidden 1500ms hold on lane-a kept for A/B crossfade. Soft restart. bak_5.33.184_pre185_lanea_mmfade_Includes_Bezel.xml.

Filed from Rob (voice). Newest at the top. Fix when approved; move resolved notes to `/workspace/BEZEL_BREAKS.md` with a K-id.

## Open

### BUG-025 — TV fanart block: bold show title upper-left when no clear art (2026-10-30, Rob voice; feature) — FIXED 5.33.180
No clearlogo / tvshow.clearlogo / clearart / tvshow.clearart (or Clearart off via bz_tvclear_off) -> bold show title (BzTVShowName) upper-left of section fanart block (150,146). Label in BezelVPLContent, Includes_Bezel.xml, reusing t4153 strip gates. Hidden under Info and while video plays in the box. Strip fallback unchanged.

### BUG-026 — Back from section flashes Main Menu / section (Left fades clean) (2026-10-31, Rob voice; 5.33.182)
**Where:** Movies / TV / Music list Back-at-root → Main Menu.  
**Expected:** Same smooth MM fade-in as Left / normal open.  
**Got:** MM or section flashes / pops when Back opens MM.  
**Cause:** List `onback` at root does `SetProperty(bz_nav)` then focuses sink `6299` (BezelBackTrap) to eat Kodi PreviousMenu. Trap always `onfocus→SetFocus(60)`, so focus bounced list↔strip while bz_flip also `SetFocus(6996)` — stolen-focus re-grab flashed strip/section under the Visible fade. Left only sets `bz_nav` (no 6299 trip).  
**Status:** FIXED 5.33.183 — BezelBackTrap: if `$EXP[bz_navmenu]` → SetFocus(6996), else SetFocus(60). Soft restart. bak_5.33.182_pre183_backflash_Includes_Bezel.xml.

### BUG-024 — Back from non-media MM sections stops on underlay before Main Menu (2026-10-30, Rob voice; BUG-013 pattern)
**Where:** Pictures, Add-ons, Search 1107, Media Sources 1117, Power 1118, File Manager, Weather, System info; arming lag on Favourites/Programs/Games.
**Symptom:** Back from the section root closes to the underlay section first, then MM.
**Status:** FIXED 5.33.179 (code-read, not device-tested) — same mechanism as BUG-013: root-level onback `SetProperty(bz_nav,true,home)` so MM is already up when the window closes. Favourites/Programs/Games: bz_flip arms bz_rootarm immediately on a fresh window open (no 0.6 s wait). FULL restart (bz_flip.py).

### BUG-023 — Black bar drawn when Options / context menu opens (2026-10-30, Rob voice)
**Where:** Options / context menu openings (skin.bezel2).  
**Symptom:** A **black bar** is drawn on the **left side of the screen, off the fanart stage**, during option context menu openings.  
**Wanted:** No black bar flash/draw when opening the Options / context menu.  
**Related:** BUG-003 (Options/Info black box left of colour strip past fanart stage — similar left/off-stage area; keep separate until diagnosed).  
**Session:** Logged open; keep log open. Detail added: left side, off fanart stage.  
**Status:** open — logged only, no fix yet.

### BUG-022 — Fanart FS key map correction (2026-10-30, Rob voice) — FIXED 5.33.172
- Old (5.33.138 doc): block Select = pause (1 s delay), double-Select = Play Next, L/R = prev/next song, Up = pill, pill Select/L/R cycle, Down from pill = controls.
- Rob wants in fanart view (MusicVisualisation, Play Next off / bz_pnoff=1): Up focuses pill; Select cycles pill; Left/Right cycle pill.
- Fix: Includes_Bezel 6390 viz+bz_pnoff=1 Select/Left/Right → SendClick(6391) (cycle pill: Visualizer>Bio>Fanart>Lyrics>Up Next>Controls). Up→6391 and pill keys unchanged. Viz Play Next mode, Dialogue FS 1120, Music section untouched. ReloadSkin.
- Residual: in fanart FS pause/prev/next now via pill → Controls (Down/Select → 1115) or M/RED; double-Select Play Next gone (touch tap big album still opens Play Next).

### BUG-021 — Stub album cast shadows out of sync with sway until stub reset (2026-10-30, noted on 5.33.168) — FIXED 5.33.170
- 5.33.171: cast opacity = sway-clock phase (bz_castL/R, timing unchanged) × Tuner › Fullscreen Music › Viz opacity (bz_at_fsvizop, same setting as stub/side albums). Not tied to album-art brightness. Low steps 0/5/10 added to cast XML. FULL restart.
**Where:** Dialogue FS + Play Next / fanart FS stub albums — cast shadow vs sway animation.  
**Symptom:** Stub album cast shadows are **not staying in sync** with the sway animation. Cast sequence was wrong until the user **reset the stub**, after which sync went the right way and the cast looked correct. Something between cast and sway is not started/kept together.  
**Related:** BUG-009 (wrong sway phase), BUG-019 (cast sequence needs switched).  
**Session:** Logged alongside BUG-015–020; keep log open.  
**Status:** FIXED 5.33.170 — shared clock. Removed both stub casts' own Conditional/pulse fade timers (BezelFSPlayNext, Includes_Bezel). bz_flip.py sway_clock now computes cast opacity from the sway's own t0 (same go 2.4 s / pulse 7.4 s / hold D / 10 s swing / pulse-reverse timeline; D read from the Tuner-patched sway pulse in the skin XML; Short sway 5.5 s 0→−30 handled) and publishes Home bz_castL / bz_castR (15–100, 5% steps, blank = 100). XML maps each level with a static Conditional fade. Left bright at −13, right bright at +13, as 5.33.74. A stub load mid-cycle now just reads the current value — no re-zero, no visible restart. FULL restart. bak_5.33.169_pre170_bug021.

### BUG-020 — Music section: Right does not open player controls (2026-10-30, noted on 5.33.168)
**Where:** Music section (list / underlay browse) — remote Right.  
**Symptom:** Navigating **Right** in Music does **not** open player controls.  
**Wanted:** Right opens player controls.  
**Session:** Logged alongside BUG-015–019; keep log open.  
**Status:** FIXED 5.33.174 — Custom_1115_MusicControls.xml was malformed (5.33.165 fsslide edit): 52 broken `<onright>` tags across 13 buttons (6401–6413 rows) — missing `<` + doubled `condition="` + stray quote after `$EXP[bz_pndlg_ok]`. Kodi failed to load 1115 ("Line 26"), so Includes_Bezel Right→`ActivateWindow(1115)` did nothing. Repaired, xmllint OK. ReloadSkin. bak_5.33.173_pre174_bug020.

### BUG-019 — Stub album cast shadows: wrong sequence — need switched (2026-10-30, noted on 5.33.168)
**Where:** Dialogue FS + Play Next / fanart FS stub albums (`BezelFSPlayNext`) — cast shadow sway/fade sequence.  
**Symptom:** Stub album cast shadows play in the **wrong sequence**; they need to be **switched** (left/right or phase reverse).  
**Related:** BUG-009 (stub cast wrong sway phase / needs reverse); BUG-014 (right stub missing cast).  
**Note 5.33.170:** the most likely cause was BUG-021 drift (own timers out of phase after mid-cycle load). Cast is now on the shared sway clock; retest before any L/R swap.  
**Session:** Logged alongside BUG-015–018; keep log open.  
**Status:** open — logged only, no fix yet.

### BUG-018 — Fullscreen pill still visible in fanart FS / Kodi fullscreen (2026-10-30, noted on 5.33.168) — FIXED 5.33.169
**Where:** Main Menu / Music colour strip — Fullscreen pill (6886 / cycle-pill style); fanart FS (visualisation) and Kodi fullscreen.  
**Symptom:** The Fullscreen pill remains **visible** while in full screen fan art / Kodi full screen mode.  
**Wanted:** Pill must **not** be visible in fanart FS / Kodi fullscreen.  
**Related:** 5.33.154 hid pill 6886 in fanart FS — regression or incomplete coverage.  
**Session:** Logged alongside BUG-015/016/017; keep log open.  
**Status:** FIXED 5.33.169 — pill 6886 group gate adds !Window.IsVisible(visualisation), !Window.IsActive(fullscreenvideo), !Window.IsActive(1120) on top of .154 !IsActive(visualisation). Clarified by Rob: pill is CORRECT on section colour strips (Music/Movies/TV); hide ONLY in fullscreen contexts (Kodi FS music / fanart FS viz). Section strips untouched. XML only → ReloadSkin.


- **5.33.173 hardening (BUG-018b):** 6886 exists in one place only (View_60_BezelInfoList inside BezelFSLeftStage, MyMusicNav). Leak: the .169 gate used IsActive only, so the pill could draw while 1120 / fullscreenvideo were opening/closing, during the bz_fsret return-slide latch (~1 s after Back from Dialogue FS, stage sliding back in), and around viz load before IsActive flips. Gate now also requires !IsVisible(1120), !IsVisible(fullscreenvideo), !IsVisible(1112), bz_pnoff!=1, bz_fsret!=true. Section colour strip unchanged. ReloadSkin. BUG-017 untouched.

### BUG-017 — MM mini-player → Fullscreen opens section behind / last section instead of fanart FS (2026-10-30, noted on 5.33.168)
**Where:** Main Menu mini-player — Fullscreen pill / path into fanart FS.  
**Symptom:** Triggering full screen from the main menu mini player first opens the **section behind** the menu or the **last previous section**, instead of loading full screen fan art.  
**Wanted (clarified 2026-10-30):** When the fullscreen pill in the main menu mini player is triggered, **fanart FS should open directly from the main menu**. It must **not** open the section behind or the last previous section first.  
**Session:** Logged alongside BUG-015/016; keep log open.  
**Status:** open — logged only, no fix yet (clarification only; not being coded in this pass).


### BUG-016 — Music MM warm: album shows as background after album browse; always want artist underlay (2026-10-30, noted on 5.33.167)
**Where:** Main Menu Music warm underlay — open MM from inside Music after browsing into an album.  
**Symptom:** Main Menu cold-start correctly shows the **artist** section as background. But if you enter Music, open an album, then trigger Main Menu, the **album** appears as the MM background instead of artists.  
**Wanted:** Artist section is **always** the MM Music background, no matter where you were inside Music.  
**Agreed rule (earlier today):** artist underlay on highlight; resume last page on Select. What shipped focuses the album and shows it as the background (violates the highlight/underlay half).  
**Session:** Logged alongside BUG-015; Rob may add more this session — keep log open.  
**Status:** FIXED 5.33.168 — mm_warm open-row check (`done[0]` on MM open) treated any `Window.IsActive(music)` as already-warm, so album browse stayed as underlay. Music now counts as warm only when FolderPath is `musicdb://artists/`; otherwise parked Music re-warms in place to artists. Select still resumes `bz_lastmusic`. FULL restart (.py).


### BUG-015 — WARM 2.0: TV Shows → Movies fade hitch — TV art pops out before Movies underlay (2026-10-30, noted on 5.33.167)
**Where:** Main Menu strip — focus on TV Shows, scroll Up to Movies (warm underlay swap).  
**Symptom:** The fade itself works, but there is a hitch: TV show art **pops out** (disappears/snaps away) before the Movies underlay takes over.  
**Session:** Rob will handle this in the current session and may add more items — keep this log open for additions.  
**Status:** FIXED 5.33.175 — cause: poster A/B lane (`_ABLane pos`, empty_flag) set `bz_pos_empty` after only 0.25 s of empty poster read. On TV→Movies the Movies list's art loads lazily; `_arel` releases `bz_arthold` after ~0.6 s even with no art, so `_ab_poster` read '' → empty flag hid both A/B sides → TV poster popped out before Movies faded in (and Movies then came in as 'first art', no fade-over). Fix (bz_flip.py, in place): empty flag only after the empty read persists 1.5 s when a poster is shown, so outgoing TV art stays until Movies art fades over it. A/B fade times unchanged. FULL restart. bak_5.33.174_pre175_bug015.

### BUG-014 — WARM 2.0 / FS: right stub album missing cast shadow; need casts above stub overlays + title tags (2026-10-30, noted on 5.33.165)
**Where:** WARM 2.0 / skin.bezel2 — Dialogue FS + Play Next / fanart FS stub albums (`BezelFSPlayNext`).  
**Symptom:** (1) Stub album on the **right** has no cast shadow; left stub does. (2) Want cast shadows **above** the stub album overlays, including the title tags (not only the album-edge cast).  
**Notes (investigation):** Left stub uses `pn_cast.png` flipx at left=270; right uses unflipped `pn_cast.png` at left=0. Both gated on Cover+Title. Sway-phase fades differ (right often sits near fade-out — see also BUG-009). Cast controls are siblings after frame but **under** nothing for titles — title/grad labels have no cast/drop shadow layer above them.  
**Status:** open — logged only, no fix yet.

### BUG-013 — WARM 2.0: Back from Kodi Settings does not return straight to Main Menu (2026-10-30, noted on 5.33.163)
**Where:** WARM 2.0 / skin.bezel2 — Kodi Settings → Back.  
**Symptom:** Backing out of the Kodi settings menu does not return straight to the Main Menu. It first lands on the section that was active before Settings opened, then opens the Main Menu.  
**Wanted:** Back from Settings returns **directly** to the Main Menu (no intermediate section stop).  
**Status:** FIXED 5.33.176 — Settings.xml list 9000 onback now sets bz_nav immediately (was only a 1 s AlarmClock, so the section window showed first). ReloadSkin.

### BUG-011 — WARM 2.0: startup list focus jumps around / fights Music instead of following Tuner startup selection (2026-10-30, noted on 5.33.161)
**Where:** WARM 2.0 / skin.bezel2 — startup (Main Menu warm + Tuner startup selection), Music section.  
**Symptom:** On startup, list focus jumps around instead of following the Tuner startup selection; it fights with Music.  
**Wanted (Rob, corrected intent):** Startup focus respects the Tuner startup selection. When Music is the highlighted main-menu section, only the Music **artist list** is the default highlighted item. The Music button itself must **not** be focused on startup.  
**Cause:** `bz_flip.py` MM-start release (ControlGroup 6899 focused) queued `SetFocus(6996,startrow)` and cleared `bz_mmstart` in the same tick, and latched `bz_mmlive` from the pre-focus row (Music row 0). Warm/MMHIDE then ran against row 0 (Music) before the strip reached the Tuner row → focus jump / Music fight.  
**Status:** fixed 5.33.186; regress when warm rolled to 151 in 5.33.187; **re-fixed 5.33.188** — same Tuner-row hold restored.

### BUG-012 — WARM 2.0: fan/poster art fades start from black (2026-10-30, noted on 5.33.161)
**Symptom:** All MM A/B fanart + poster transitions (both directions, same- and cross-section) dropped to black, then faded up.  
**Cause:** 5.33.160 fade-in-only set A/B `Hidden` to time=0 while the incoming side faded 0→100 over 1.5 s → outgoing art vanished the first frame, black showed through until the new side came up.  
**Status:** fixed 5.33.162 — side a (lower) holds 100 for 1.5 s on Hidden, Visible 0→100 in 300 ms; side b (upper) Visible 0→100 1.5 s over held a, Hidden 100→0 1.5 s revealing full a. New art fades in directly over the previous art. BUG-010 lane split untouched. ReloadSkin.

### BUG-010 — WARM 2.0: Music ↔ poster art cross-drawn into the wrong frame (stretch) (2026-10-30, noted on 5.33.160)
**Where:** Main Menu warm (`mm_warm` in `scripts/bz_flip.py`), Music ↔ Movies/TV underlay swap; poster frame (`BezelPoster60` / A/B `bz_pos_*`) vs Music album slot (`BezelFlipA/B` / 600×600).  
**Symptom:** Leaving Music for Movies/TV, album/artist art is drawn into the **poster** frame and stretched (`aspectratio` scale) before the real poster loads. Rob’s rule (bidirectional): Music art must **never** paint the poster frame; Movie/TV posters must **never** paint the Music album slot. Each section’s art stays in its own frame — hide or keep in-slot on section change; no cross-drawing either way.  
**Cause (investigation, no fix yet):**
1. **One shared “poster” pipeline for both families.** `_ab_poster()` and `BezelPoster60` feed Music thumb/Icon and video posters into the same properties/controls. `BezelFlipA` falls back to `$VAR[BezelPoster60]`, so Music flip art and video poster art share that variable. A/B lane `bz_pos_a/b` is the same MM preload for both.
2. **Warm hold is poster-shaped only.** `_ahold()` always writes `bz_hold_poster` from `Art(poster)` → `tvshow.poster` → **`Icon`**. On Music, that captures square album/artist Icon into `bz_hold_poster`. While `bz_arthold` is set, `BezelPoster60` and `_ab_poster` keep serving that URL into the **poster** controls (Videos layout uses `aspectratio` **scale** → stretch).
3. **Swap order.** Warm starts hold → path/window swap to Videos → poster chrome visible with held Music URL still in `bz_hold_poster` / stale `bz_pos_*` → then new movie poster arrives. Reverse path (Movies→Music) holds a movie poster URL and can feed it through the same shared variable/lane into the Music album slot.
4. Stretch is the symptom of (2)+(3) in a scale poster frame; the root rule break is **cross-drawing**, not aspect alone.
**Fix recommendation (when approved — fix in place, do not invent a new system):**
- Split hold / A/B by art family: e.g. `bz_hold_poster` only from video poster arts; Music uses album/cov hold only (or no hold into poster lane). Never set `bz_hold_poster` from Music Icon/thumb.
- Gate `_ab_poster` / `BezelPoster60` to Videos (poster arts only); Music album slot only from thumb/cov / Flip — no `$VAR[BezelPoster60]` fallback while leaving or entering Music across a section warm.
- On Music→video warm: clear or stop feeding Music URLs into `bz_pos_*` / poster hold immediately; hide album slot or leave it undrawn in the poster frame. On video→Music: clear poster hold/pos for the album slot; don’t show held poster in Flip/album.
- Optional: keep frames exclusive by window (`Window.IsActive(music)` vs `videos`) so the wrong control isn’t visible during the swap.
**Status:** fixed 5.33.161 — family split: `_clear_poster_lane` + cross-family `_ahold` (no Music→poster / poster→Music hold); `_ab_poster` Videos-only; BezelPoster60 / BezelPoster / BezelFlipA/B gated. Fade-in-only from .160 kept. FULL restart.

### BUG-009 — WARM 2.0 / FS: stub albums cast at wrong sway phase (needs reverse) (2026-10-30, noted on 5.33.151)
**Status:** fixed 5.33.152 — removed bz_movposter_hold entirely (Movies no longer has a poster hold; same as TV). Removed: bz_flip.py poster_clock t4813 set/clear block + `_ab_poster` hold fallback; Includes_Bezel.xml BezelPoster60 hold `<value>` + stand-in multiimage Movies-hold gate. Scope add: deleted extras/standins/posters/poster_A–E.jpg and removed every multiimage using standins/posters/ (15 controls, Includes_Bezel.xml).
**Where:** Dialogue FS (1120) and FS fanart — stub / side albums (Play Next cast).  
**Symptom:** Stub albums receive cast at the wrong part of the sway animation; cast timing needs to be reversed.  
**Note 5.33.170:** stub cast phase now comes from the shared sway clock (BUG-021); retest.  
**Status:** open — logged alongside BUG-008; not diagnosed yet.

### BUG-008 — WARM 2.0: TV Shows → Movies flashes poster + chrome (Movies → TV smooth) (2026-10-30, noted on 5.33.151)
**Where:** Main Menu (strip 6996) warm, Videos window, MOVIES ↔ TV SHOWS rows.  
**Symptom:** Movies → TV Shows is a smooth transition of posters, fanart and chrome. TV Shows → Movies gives a flash of the poster artwork and chrome.  
**Suspected cause (investigation, not fixed):** movies-only `bz_movposter_hold` (t4813) is cleared in `poster_clock` (scripts/bz_flip.py ~L322) as soon as the list is not movies/sets, i.e. while on TV. Returning to Movies, every movies empty-frame fallback keys on that hold — Includes_Bezel.xml L176 poster $VAR, stand-in multiimage L2545 (`!Container.Content(movies) ... | String.IsEmpty(bz_movposter_hold)`), `_ab_poster` L1170 — so the first empty-Art(poster) frames of the movies list have no held poster and the stand-in can show. TV never needs that hold (falls back to Art(tvshow.poster)). `_arel` (L542) also releases bz_arthold after 30 polls even with no art.  
**Status:** FIXED 5.33.189 — keep movies poster+fanart hold across TV (no clear-on-!movies); bridge empty Movies frames. Warm park/A/B settle untouched.

### BUG-007 — Back from Tuner: still drawn over Power menu (2026-10-30, noted on 5.33.145)
**Where:** Bezel Tuner (BezelTunerCard / list 6970) opened from Power menu TUNER → Back returns to Power (1118).  
**Symptom:** When returning from the Bezel Tuner, the Tuner still draws on top of the Power menu instead of the Power menu showing cleanly. (Caller: "still a bug.")  
**Suspected:** onback runs `ActivateWindow(1118)` before `ClearProperty(bz_navtune)`, so the Tuner group stays visible while Power reopens.  
**Status:** attempt 5.33.157 — BezelTunerCard wrapped as group id=6975 with Hidden time=0; onback from Power clears bz_navtune before ActivateWindow(1118). Smoke still needed.  

### BUG-006 — TV seasons folder: posters missing entirely (2026-10-30, noted on 5.33.145)
**Where:** TV Shows — after entering a show’s seasons folder.  
**Symptom:** Posters are not there at all when you enter a TV show seasons folder — missing entirely, not a gap or partial display.  
**Status:** open — not diagnosed yet.

### BUG-005 — Power menu: Tuner button has no outline (2026-10-30, noted on 5.33.145)
**Where:** Power menu list.  
**Symptom:** The Tuner button has no outline.  
**Status:** fixed 5.33.150 — TUNER folded into list 7800 as a 4th content row (inherits focusedlayout BzATHiTex); separate 7801 button and sibling focus Image removed.

### BUG-004 — MM background fade: TV clearart/logo snaps in (no fade) (2026-10-30, noted on 5.33.145)
**Where:** Main Menu background fade (TV underlay).  
**Symptom:** TV show clear art / logo does not fade with the rest of the art — it snaps in.  
**Status:** open — not diagnosed yet.

### BUG-003 — Options/Info menu: black box left of colour strip past fanart stage — TV, Movies, Music (2026-10-30, noted on 5.33.145)
**Where:** TV, Movies, and Music sections (Options / Info menus).  
**Symptom:** The option / info menu draws a black box to the left of the colour strip that extends past the fan art stage.  
**Status:** open — not diagnosed yet.

### BUG-002 — File manager: context menu opens with no list focus / can't Back out (2026-10-30, noted on 5.33.143)
**Where:** File manager.  
**Symptom:** When a file is selected, the pop-up menu appears with no focus on its list, and the user cannot back out of it.  
**Cause:** DialogContextMenu only used the Estuary popup + grouplist slide for FileBrowser; File Manager fell through to BezelStdFrame. FileManager `defaultcontrol always="true"` also reclaimed focus from list 996.  
**Status:** fixed 5.33.145 — FileManager shares FileBrowser popup path; always= dropped on FM defaultcontrol.
**Status:** fixed 5.33.151 (follow-up) — template 1000 texturefocus literal `lists/focus.png` (no $VAR); BzCtxTxt on FM/FB = 99FFFFFF so focused FFFFFFFF differs; dismiss button onfocus SetFocus(996). .145 path untouched.

### BUG-001 — MM Movies row: two Ups to leave (2026-10-30, noted on 5.33.141)
**Where:** Main Menu only (strip list 6996).  
**Symptom:** When the **MOVIES** button is highlighted, it takes **two Up** presses to leave that row instead of one.  
**Not:** Does not happen outside the Main Menu.  
**Status:** open — not diagnosed yet.

### BUG-008 update — 5.33.153 (2026-10-30)
All Movies + Music fallbacks removed. bz_movposter_hold gone (verified); standins multiimages removed (36 grid/6600 album+artist + t4289 music fanart); 18 fallback="DefaultAlbumCover.png" attrs stripped; MusicInfoThumbVar album->DefaultAlbumCover value removed. Assets parked at /workspace/bezel-533-fork/parked_standins_bug008/ (see README).

- Note under BUG-008/BUG-015 (5.33.178): Movies→TV enter leak (Movies poster in TV) fixed — A/B poster lane never re-stages held outgoing poster; destination-empty drops it at _arel.

## 5.33.187 note
Warm rolled back to 151 (keeps BUG-010, BUG-016/.164). BUG-011, BUG-012(.185 lane), BUG-015/.178 fixes REMOVED by request — may regress (startup row jump, TV poster pop/leak on Movies↔TV, black-frame lane swap).

### BUG-028 — Tuner list focus dead (MM 6996 under Tuner) (2026-10-31, noted on 5.33.189)
**Where:** Bezel Tuner (list 6970) from Power → TUNER (or any bz_navtune open).  
**Seen:** Focus / whole Tuner list “don’t work” — Up/Down moves Main Menu rows (or fights) instead of Tuner rows.  
**Cause:** MM list 6996 stays visible at the same strip slot (left 570) while BezelTunerCard/6970 is open; focus lands on or steals to 6996.  
**Status:** FIXED 5.33.190 — hide 6996 while bz_navtune or bz_navbez; bz_flip `_bzstrip` + song-jump skip SetFocus(6996) while Tuner/Settings open.  
- 2026-10-31 5.33.191 WARM 2.0 (Rob voice): MM + music playing + toggle On → MM poster lane hidden, album art (Player.Art(thumb)) in its slot; fanart stage untouched. New Tuner section WARM 2.0: "Posters during music" Skin.String bz_at_warmmusicposters (On default/Off) + "A/B fade length" Skin.String bz_at_abfade (7 steps 2500/2000/1800/1500/1200/1000/800 ms, default 1500; drives MM fan+pos A/B Visible/Hidden fades). BUG-028 kept. ReloadSkin (FULL restart if installed from zip). bak *.bak_5.33.190_pre191_warm20.
