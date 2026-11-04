# CLAUDE CHANGELOG — skin.bezel2 5.33.424 → 5.33.470

**For:** review by the main BEZEL project agent
**Author:** Claude (this session, 2026-11-03, with Rob)
**Base:** `skin.bezel2-5.33.423.zip` (Downloads). Every build is 423 plus the changed files listed per version. All builds are in Downloads as `skin.bezel2-5.33.42x.zip`, and each one's changed files are in `Downloads\bezel42x-patch\` (cumulative from 423).
**Testing status:** static checks only. All XML parses, every `.py` compiles, a reference audit showed no new undefined includes/vars/exps/fonts/textures, and the new Python logic was exercised against a mocked xbmc. **No build was device-smoked by Claude.** Rob reported on device: 425 still flashed, 426/427 "much better", 428 had a landing issue (fixed in 429).
**429:** the zip build was interrupted, so use 430, which contains all of 429. To build (in the device VM home): `cp -rn bezel429-patch/. bezel430-patch/` then `python3 ~/build_bezel.py 5.33.430 bezel430-patch`. The script reads the 423 zip, overlays the patch folder, and drops `bak_*`, `port-refs/`, `__pycache__/`.

---

## Summary of intent

| Version | Rob request | What changed |
|---|---|---|
| 424 | "MM MOVIES ROW FLASHES ON HIGHLIGHT"; "ON MUSIC STOP FROM MINI PLAYER FOCUS FIRST ITEM IN LIST" | Focus bounce removed from warm row landing; mini-player Stop → MM row 0; cleanup; lean zip |
| 425 | "STILL FLASH … AFTER A SWITCH FROM MUSIC TO VIDEOS" | Strip row draws focused while a warm window switch passes focus through list 60 |
| 426 | "I DONT WANT THE LIST TO HITCH OR FLASH WHEN NAVIGATING"; "THE BACKGROUND SHOULD REFLECT THE ROW HIGHLIGHTED"; chose "Rebuild MM" | **VWARM**: no window switch while navigating the MM; library-fed art for rows whose window is not behind |
| 427 | "WHEN SWITCHING FROM ALBUM TO POSTER THERE IS A POP" (MM rows) | **A2PONE**: album↔poster is one dissolve onto the final art |
| 428 | "Movie/TV row will flash on first new focus only … unless you focus Music again"; fresh auto-hide ("old system was glitchy and broken") | **POSKEEP** fix; **MMHIDE** new auto-hide + Tuner row |
| 470 | "NP BAR SHOWN WHEN BIG ALBUM IS CENTER IN BOTH FULLSCREEN, BIG ALBUM NP BAR HIDE WHEN SWITCH BACK TO FANART STAGE" (+ remove the Up Next fanart bar); new dust defaults; "BEZEL FEELS SLOW WHEN NEW LISTS ARE LOADED" (all four: wait, cascade, big lists, folder open) | **CENTREBAR**, revert 463 **UPNNPBAR**, **DUSTDEF**, **ENTRYHOLD** (0.6 → 0.35 s), **LISTTIME** (`BEZEL list` log) |
| 469 | "EXIT FROM TUNER THEN ATTEMPT TO RE ENTER TUNER DOES NOT WORK"; "DISABLE THE MM MENU SLIDE"; "AUTO UNFOCUS PILLS, AFTER 5 SECONDS OF INACTIVITY FOCUS RETURNS TO LAST POSITION" (all pills + A-Z bar, back to where focus came from) | **TUNERREOPEN** (no Tuner-flag clears after a modal opens), **MMNOSLIDE**, **PILLIDLE** (mm_autohide, 4 Hz) |
| 468 | "CAST SHADOW ONLY VISIBLE WHEN MUSIC IS PLAYING, IT SHOULD BE ACTIVE ALL TIMES"; "DONT NEED THE FIXED, JUST THE DEFAULT GROW AND FADE"; "CAN WE ADD ANOTHER LAYER TO THE LIT DUST?" → second spin, album + poster, "same texture as mm dust", "all in 468" | **CASTIDLE** (no bz_audio_latch gate on the cast fades / stub casts), **CASTFIXEDDEL** (static cast copies + Tuner row removed), **LITSPIN2** (mirrored counter-rotating spin disc) |
| 467 | "THE COLOR STRIP IS NOT DRAWN WHEN EXIT FROM TUNER MENU"; P2.6 ("I WILL GIVE YOU A LOG"); "INCLUDE ALL TOGETHER" | **TUNERPWR** (1118 clears bz_navtune on load) + revert 465 **TUNERHIDE**; rewrite **P2.6a OWNSHADOW** (`_v60_set` skips the read of an unchanged value it wrote) |
| 466 | "MUSIC ALBUM SECTION USES AN OLD LIST AND NOT THE NEWER ALBUM LIST", "AS WELL AS RECENT PLAYED"; "MUSIC GENRES HAS UNWANTED META DATA DRAWN BEHIND THE LIST" (screenshot) | **ALBUMCOVER** (covercol for every music albums list, no bz_albumlist), **ALBUMPILL**, **GENREMETA** (old strip info card hidden whenever list 60 is up) |
| 465 | "TUNER MENU EXITS BUT IS STILL DRAWN"; "OLD FULLSCREEN FANART VIZ IS LEFT IN THE CODE" (fanart overlay + cycle pill at the old upper-right spot, back from the big album) → "REMOVE ANYTHING OLD"; "ANY REWRITE OPTIMIZATION" | **TUNERHIDE**, **DEL1104**, **OLDPILL**, **OLDNP** (old Now Playing dialog 1112 + routes → 1121 / Kodi FS), rewrite **P3.4–P3.6** (parked controls, grid 6600 conditions, grid script actions) |
| 464 | "CAN CLOCK AND EVENT BE TRIED NEXT?" → "CLOCK" | rewrite **P2.4 SWAYEPOCH**: poster sway epoch = album idle clock bt0 (was its own art0). Event-driven playback (P2.5) dropped: ~25 mostly compound checks, ~2–3% saving, timing risk |
| 463 | "MUSIC CONTROLS GET STUCK IN VIS SETTINGS"; "QUICK BACK FROM TUNER MENU DROPS IN RANDOM WINDOW"; "ADD A NP BAR WHEN UP NEXT IS TRIGGER IN KODI FULLSCREEN" | **VIZSETRESET** (bz_vizset by window id + cleared on load), **TUNERBACKQ** (power menu before Tuner hides), **UPNNPBAR** (compact NP bar under the home album with Up Next, viz + 1121) |
| 462 | "TUNER ROWS HAVE DAYS AND MONTHS"; "HIDE"; "BACK ON LEVEL 2 → LEVEL 1"; "BACK ON LEVEL 1 → POWER MENU"; "SAME LOOK AS MM DUST IN THE ALBUM AND POSTER LIT DUST" | **TUNERRAILNUM** (rail counts were localized ids; hidden), **TUNERBACK** (6970 → 7001; 7001 → power menu), **LITMM** (lit dust default = textures cut from MM Dust 2.0) |
| 461 | "NEXT" (rewrite P3, dead code) | rewrite **P3.1–P3.3**: 32 unused includes, 14 expressions, 317 variables removed; audit clean; zero geometry change |
| 460 | "457 VERY SMOOTH AND RESPONSIVE"; 458 MM bg "ROW SWITCH / OPEN-CLOSE LOOKS BAD"; picked "QUICK DIM, NO WAIT" | **MMDIMQUICK**: 458 MMNODIM reverted, mmdim fades without the 456 delay (= 455); keeps P2.1 + P2.3; no P2.2 |
| 459 | "P2.2 NEXT" "THEN BUILD" → "459 VERY BAD", "458 GOOD" | **REJECTED, reverted** rewrite **P2.2**: one `slow_watch` thread for km_leave_watch / fpop_clock / allcnt / album_id / cw_clock (A/B against 458) |
| 458 | "THE 1.5 DELAY MAKES IT LOOK BROKE"; "JUST HAVE IT FADE IN QUICK. NO FADE OUT OF SECTION"; "START P2" | **MMNODIM** (no section dim under the MM), rewrite **P2.1** (grid_sync removed), **P2.3** (bz_big_* no longer set) |
| 457 | "P1 THEN IF USAGE PERMITS DO P2" (rewrite, layout first) | rewrite **P1B** (strip content relative to `bz_strip_x`), **P1C** (stage fill / stage / art constants); zero visual change |
| 456 | "SMALL BLACK PULSE ON BIG ALBUM ON MUSIC START"; "TRANSPORT BAR LABELS … CENTERED"; "MM FADES BLACK THEN BACK"; "TUNER … REMOVE NAV LEGEND"; "GLOW TEXTURES"; "TITLE ON THE FANART STAGE … HIDDEN" | **IDLEHOLD**, **TRANSCENTRE**, **MMCLEANFADE**, **TUNERCLEAN**, **GLOWSHIFT**, **FSTITLE**, rewrite **P1A** |
| 455 | "EXTEND THE FANART STAGE RIGHT … KEEP LIST AND COLOR STRIP SAME SIZE"; "MM MUST MOVE"; "DELETE THE GRID VIEWS" | **STAGEWIDE** (stage 120–1050, strip 660–1050, gap 90), **GRIDDEL** |
| 454 | "ADD RECOMMENDED SPEEDS TO BUILD"; "CAN THE LIST FEEL MORE FLOATY"; "I PREFER FADE INS FOR ALL TRANSITIONS"; "KEEP SLIDES FOR BIG ALBUM" | **SPEEDS** (317 ms list, 300 ms idle cover), **FADEINS** |
| 453 | "USE ONLY 1 CONTINUOUS UNBROKEN SWAY ANIM"; "THE PLAYING STYLE AND TEXTURES SHOULD BE FOR BOTH"; "NO RESET ON PLAY" | **ONESWAY**: one big album sway rig + one glare/dust/shadow set for idle and playing |
| 452 | "SONG START RESTARTS GLARE AND DUST ON BIG ALBUM? IT SHOULD BE UNBROKEN ANIMATION" | **GLARECONT**: playing-album glare lead-in only while the sway leads in |
| 451 | "SOME ARTIST DONT SHOW THE ALL ALBUM FOLDER EVEN WITH MULTI ALBUMS, SCROLL TO END OF LIST NAVS TO HOME"; L2 screenshot (gap under small album, ALL over last album) | **ALLCOUNT**, **L2PULL**, **NOWRAPGUARD** |
| 450 | "ADD NP BAR TO KODI FULLSCREEN VIZ WHEN BIG ALBUM IS CENTER" ("only the FS fanart dialogue fullscreen") | **VIZNPBAR**: compact NP bar under the centred album in Kodi FS viz, drawn in 1122 |
| 449 | "2 AND 5" (optimizations: texture packing, list conditions) | **XBTPACK**: media/Textures.xbt with the 1128 small textures |
| 448 | "BIG ALBUM SWAY ANIM LOOKS LIKE ITS WRONG SEQUENCE AGAIN WITH GLARE AND DUST" | **IDLESEQ**: idle glare + lit dust follow the playing album sequence |
| 447 | "VERY LONG PAUSES WHEN ENTERING SECTIONS" (from MM, 5+ s) on 446; "ISSUE WAS CAUSED BY YOUR CHANGE" | **TICKCACHE reverted**: bz_flip.py = 445 |
| 446 | Rob sent the 445 kodi.log (perf lines) | **TICKCACHE**: per-thread, per-tick cache for Home property / condition / infolabel reads in bz_flip.py |
| 445 | "START WITH THE ONE THAT WILL OPTIMIZE BEZEL THE MOST"; "SYNCING THE SWAY SHADOWS, GLARE, LIT DUST… THE LAST FIX SEEMS TO OF LOST SYNC AGAIN" | **SYNCANCHOR** (stub cast clock re-anchors on 1122 reopen + full album gate); **PERFCOUNT** (optimization #1 step 1: per-thread Kodi call counts in kodi.log) |
| 444 | Rob batch: auto-hide dim (poster + fanart only), Movies fanart showing Music labels, album stretch on rail slide, idle lit dust, quick-nav pick opening the warm section, music-playing landing, L1 ARTIST caption, Tuner Back | **ALLFIX**, **MMHIDEART/FAN**, **RAILXFADE**, **IDLELIT**, **VPICKLOAD**, **M2VLAND**, L1 caption |
| 443 | "1 14 ROW IS NOT A RULE, 2 ALWAYS BOTTOM, 3 GROUPED, 4 LIST ONLY, 5 HIDE, 6 COUNT" | **ALLROW2**: no cap (long lists → bottom pill 6088/6089), grouped ALL ALBUMS, single-season/album hide, counts |
| 442 | "TAKE A LOOK AT THE BEZEL ALL SEASON ALL ALBUM CUSTOM FOLDERS MAKE BETTER AND FIX IF NEEDED" | **ALLTOGGLE**: BEZEL ALL rows follow the View All toggles; no blank `..` slot with All Albums off |
| 441 | "CAST SHADOW SYSTEM, COLOR STRIP BIG ALBUM, COLOR STRIP POSTER, BIG ALBUM STUBS" | **STUBPHASE**: stub casts anchored to the real start of the album pulse; poster cast audited (no split) |
| 440 | "CAST SHADOW SYSTEM LOSES SYNC WITH ITS PARENT" | **CASTPHASE**: album cast motion anims no longer gated on `bz_audio_latch` (album sway isn't) |
| 439 | "NEW TUNER MENU STYLE WAS APPROVED" (mockup B, section rail) | **TUNERRAIL**: rail 7001 | section rows | info panel; rows keyed on the rail |
| 438 | "ALBUM VIEW LEAF FLIP … MAKE IT WORK BETTER IF NEEDED"; "REMOVE THE SPOTLIGHT" | **LEAFTUNE** (no snap/hitch on arm, 50 ms abort, glare only off around the fold); **Spotlight removed** |
| 437 | Picked MM→section storyboard \#6 "Spotlight title"; "Fade after ~1.5 s", "Every row that opens a section" | **SPOTLIGHT**: picked row label lifts to the title spot, turns accent blue, fades; Tuner On/Off |
| 436 | Screenshot: last list row cut under the double-tap hint; "THE LIST ROW IS CLIPPED IT CAN BE SHORTER" | **LISTROW**: list + clip heights to whole rows (video 960, music 975) |
| 435 | "MINI PLAYER BRIEFLY HIDES WHEN NEXT TRACK BUTTON IS SELECTED" | **MPKEEP**: 1.5 s media hold for the MM mini player / strip offset / Up routing |
| 434 | "I MOVED THE POSTER POSITION … POSTER LIT DUST [DIDN'T] FOLLOW" | **PLITMOVE**: poster lit dust +150 px to the moved poster |
| 433 | "BIG ALBUM LIT DUST SYNC IS NOT CORRECT … LIT SECTIONS ARE SWAPPED FOR THE GLARES" | **LITSWAP**: album lit dust boxes swapped to sit under their own glare |
| 432 | "CONFIRM SKIN CHANGE POPUP HAS NO FOCUS ON THE LIST" (shared Yes/No) | **CONFIRMFOCUS**: script SetFocus dropped while Yes/No or OK is visible |
| 431 | "POSTER DIMS THEN GETS BRIGHT THEN BACK TO DIM" (on 430) | **MMSWAP0**: instant same-texture swap section twin ↔ MM lane on MM open (replaces 430's hold) |
| 430 | "MOVIES TV POSTER DIP TO BLACK WHEN EXIT TO MM" | **MMEXITHOLD**: section poster twin holds under the MM lane on MM open |
| 429 | "Current shown item in MM background doesn't land in the same spot when you open the section" | **VLANDPICK**: landing target snapshotted at Select; index-hinted search |

**Rule touched:** `behaviors/mm-warm.md` is marked LOCKED. Rob explicitly approved the restructure ("open to structure changes as long as nothing visually changes or breaks systems"). The doc has a VWARM note at the top.

---

## 5.33.424

### MMBARFLASH — no focus bounce when landing the warm row
- **Root cause:** `mm_warm._restore2`, `_defer`, and `bz_warmgate.randstart` landed list 60 with `SetFocus(60,r,absolute)` and then `SetFocus(6996)`. Kodi could render a frame with 60 focused, so the 6996 row bar (`Control.HasFocus(6996)`) blinked.
- **Change:** while the MM is open, list 60 is moved with `Control.Move(60, r − current)` (the same command UADVRAND uses), so focus never leaves 6996. With the MM closed, the old `SetFocus` path still runs.
  - `bz_flip.py`: new `_move60(r, c=None)` inside `mm_warm`.
  - `_restore2` and `_defer` use it when `bz_nav=true`.
  - `bz_warmgate.randstart`: when the strip is focused, uses `Control.Move`; the parent-row offset uses its own `par` flag.
- **Risk:** if `CurrentItem` is unreadable (−1), Movies/TV keep Kodi's row. Music `_defer` retries until the row lands.

### MMSTOPTOP — Stop from the mini player
- `Includes_Bezel.xml`: 6961 (audio Stop) and 6967 (video Stop) add `SetProperty(bz_mmlive,0,home)` and `SetFocus(6996,0,absolute)`.
- `bz_flip.py nav_menu`: if `bz_nav=true` and `!Player.HasMedia` with focus on 6957–6961 / 6966 / 6967 (not in a submenu, Tuner, BEZEL settings or a modal), it runs `SetFocus(6996,0,absolute)`. This covers playback ending while focus sits on a mini-player button.
- Id 6961 is also the TV submenu "Shows" button, hence the `!bz_navsub` guard.

### Cleanup
- Removed the undefined `<include>ListThumbInfoPanel</include>` from MyFavourites, MyPlaylist, MyGames, MyPics and MyPrograms.
- Removed the undefined `InfoWallMusicLayout` from Includes.xml (×2).
- `font16` (never defined) → `font13` in Includes_DialogSelect (what Kodi already fell back to).
- **Packaging:** install zips exclude `bak_*`, `port-refs/`, `__pycache__/` (~85 MB unpacked, zip 60 → 35 MB). These folders aren't referenced at runtime; there are comment mentions only.

### Audit findings not changed (for the main agent)
- `BzATLk_*` (10 vars) used in `BezelATLook` are undefined, and no Tuner row sets `bz_at_lk*`. The LOOK overlays are dead code.
- `bezel/at/bar_11_0.png` is referenced in the `BzATBar_fschromeop` fallback but missing.
- Dead code: 316 unused variables, 32 unused includes, 8 unused expressions, 25 unused fonts. Not removed, because Python may read some via `getInfoLabel`.
- **Performance ideas:** pack textures into `Textures.xbt`; review the number and speed of `bz_flip` polling threads (many 10–50 ms loops).
- Open bugs still listed in `bugs.md`: BUG-023 (black bar on Options/context open) and BUG-017 (MM mini-player Fullscreen opens the section first).

## 5.33.425

### MMBARFLASH2
- **Root cause (from Kodi Omega source):** a warm `ActivateWindow` creates a new window instance. `RestoreControlStates` focuses `defaultcontrol always=60`, so for a frame 6996 is unfocused (its onload `SetFocus` is synchronous, but bz_flip's bounce isn't).
- **Change:** new `$EXP[bz_mmwarmfoc]` (`bz_mmwarm` + `bz_nav` + no Tuner/BEZEL settings + no modal + focus on 60 or none) and `$EXP[bz_mmfoc]` (`Control.HasFocus(6996) | bz_mmwarmfoc`).
  - The 6996 focusedlayout uses `bz_mmfoc`.
  - `BezelMMRowBar` gained the param `warmfoc` (default `false`; 6968 unchanged).
- Superseded in practice by 426, which removes the window switch during navigation. Kept as a safety net (startup splash, kill switch).

## 5.33.426 — VWARM (MM restructure)

**Root cause of the hitch:** a cross-family MM highlight (Music ↔ Movies/TV) did `ActivateWindow` under the MM. Kodi then:
1. tears down and rebuilds the window, including a new copy of the strip and all art controls;
2. runs `CGUIMediaWindow::OnInitWindow → Refresh()` *before* `m_backgroundLoad=true`, which loads the whole directory **on the render thread** (the hitch);
3. draws the new controls with textures still loading (the flash).

**New model:**
- **Virtual row.** In `mm_warm`, if the row's window is not active (and `!Skin.HasSetting(bz_vwarm_off)` and `bz_splash_done=1`), there's no `ActivateWindow`. It sets `Home.bz_vsec=<music|movies|tv>` and `done[0]=sec`, and snaps the real underlay row first.
  - `bz_vsec` clears when the MM closes (stamps `bz_vsec_t`) or when a row's window is behind.
  - Non-WARM rows keep `bz_vsec`, matching the old behaviour where the warmed window stayed behind.
- **New thread `vwarm`** in `bz_flip.py`:
  - JSON-RPC `VideoLibrary.GetMovies` / `GetTVShows` / `AudioLibrary.GetArtists` with `properties:['art']`.
  - Fetches a 40-item window from a random start, sorted by label, then shuffled locally. A count probe comes first. There's no `sort:random`, which made Kodi read art for the whole library.
  - Art is unwrapped from `image://…/` to the plain path so it matches `ListItem.Art()` (same texture key).
  - Publishes `bz_vart_fanart`, `bz_vart_poster` (video), `bz_vart_thumb` (music), `bz_vart_clear` (tv), `bz_vart_logo`, `bz_vart_title`, and `bz_vland = sec|dbid|ix`.
  - Sets `bz_pready` if the poster stack was never armed.
  - Remembers the item per section for the session (cleared on MM close). Cycles with UADVRAND's `bz_uadv_hold` (min 3) / `bz_uadv_delay` / `bz_uadv_off` and the same pauses.
- **Hooks:**
  - `_ab_fanart` → `bz_vart_fanart`.
  - `_ab_poster` → `''` on Movies/TV virtual rows (since 428: Music virtual keeps the list poster). `_ab_mart` → `''`. `_ab_clear` → `''`.
  - `ab_clock` ticks the lanes on virtual rows in any window, ahead of the WARM HOLD / `bz_mmwarm` holds, and clears `bz_pos_on` outside Videos so the 1122 poster live twins draw.
  - `v60_mirror` has a virtual branch: Movies/TV → `bz_v60_art` / DUALHOLD hold / `bz_vpl_on`; Music → poster off.
  - `m_mirror`: Music virtual → `_m_idle_stage(bz_vart_thumb)`; Movies/TV virtual → idle album left alone.
  - `under_adv` paused on virtual rows.
- **XML:**
  - `$EXP[bz_railvis]` adds `[$EXP[bz_navmenu] + bz_vsec=music + !Empty(bz_vmus)]` (`bz_vmus` from 427).
  - 6996 `onback` and 6898 `onclick` / `onback` / `onright` on a virtual row run `RunScript(bz_mm.py,$INFO[bz_vsec])`, so Back or tap-outside still enters the highlighted section as when it was warmed. Normal closes are gated `String.IsEmpty(bz_vsec)`.
- **Select:** `bz_cmd._vw_land()` is called inside `_bz_load_then_close` after the list loads (section still held by `bz_secload`). It moves list 60 onto the shown item with `Control.Move`, only on the root list the art came from (`videodb://movies/titles`, `videodb://tvshows/titles`, `musicdb://artists`).
- **Startup:** under the splash the old window warm still runs, so the warm gate lands as before. `bz_warmgate` also accepts `bz_vsec == first` as landed.
- **Exit cleanup** clears `bz_vsec`, `bz_vmus`, `bz_vsec_t`, `_VW_KEYS` and the MMHIDE props.
- **Known limits:**
  - The TV clearlogo header (BezelVPLContent, Videos window) isn't drawn on a virtual TV row over Music.
  - Music→Movies/TV Select with music playing keeps the m2v transition, with no landing (MM shows the album under MMAUDIO anyway).
  - Mini-player Back on a virtual row closes to the window actually behind.
- **Kill switch:** `Skin.SetBool(bz_vwarm_off)` restores the old window warm everywhere. No Tuner row exists for it.

## 5.33.427 — A2PONE (one dissolve album↔poster)
- **MUSIC → MOVIES/TV (virtual):**
  - `ab_clock` sets `bz_mart_empty=1` immediately. Before, the 0.25 s settle let the square artist thumb (mart lane) show stretched in the poster frame while 6401 rose.
  - `v60_mirror` no longer does hold-then-swap. While 6401 is at 0, the pick goes straight into `bz_v60_art` (`_vw_rt` records it), and `bz_vpl_on` rises 1.05 s later, after the 1000 ms image fadetime has finished unseen.
  - While the poster is already up, picks are staged through the preload slot and crossfade inside 6401 as before.
- **MOVIES/TV → MUSIC (virtual):**
  - The poster holds (`bz_vpl_on`) until the artist thumb is the idle album and its A/B dissolve has finished (`_mi['flip'] + _mi_guard()`). Then `Home.bz_vmus=1`, and `railvis` rises and the poster falls in the same tick (`m_mirror` runs before `v60_mirror`).
  - `_ab_mart` returns `''` for 1.2 s after `bz_vsec` clears.
- Virtual Movies/TV picks require a poster.

## 5.33.428
### POSKEEP
On a MUSIC virtual row over Videos, `_ab_poster` keeps returning the list poster. In 427 the pos lane emptied, so the first Movies/TV focus after MUSIC raised 6401 empty and the pos A/B faded in 0.25 s + 1.5 s late (Rob: flash on first focus only).

### MMHIDE — fresh MM auto-hide
- **Tuner MAIN MENU › Auto-hide menu** (`Includes_Tuner.xml`): `BzATVal_mmhide` / `BzATBar_mmhide` (bar_4_0..4), the item after "Close speed", and 8 L/R handlers next to the mmwarm handlers. `Skin.String(bz_at_mmhide)`: empty/0 = Off, 1 = 30 s, 2 = 1 min, 3 = 2 min, 4 = 5 min. The info image `media/bezel/info/mm_autohide.png` was redrawn.
- **Thread `mm_autohide`:**
  - Hides when `xbmc.getGlobalIdleTime() ≥ delay`, with 6996 focused, `bz_nav=true`, splash done, no Tuner/BEZEL settings/navset/navsub/kset/mmstart/mmpick/secload, no modal, not fullscreen video. Then it sets `Home.bz_mmhide=1` and records the row.
  - Wakes when the idle counter drops: `bz_mmwake` latch 0.35 s, and if the row changed or focus left the strip, `SetFocus(6996,row,absolute)`.
  - `mm_warm` skips while `bz_mmhide` / `bz_mmwake` are set.
- **XML (opacity only, no focus moves, no park control):**
  - `$EXP[bz_mmhid]` drives fade pairs (1500 ms out / 250 ms back, reversible=false) on group 6894 (strip, colour strip chrome, glow, dust, mini player), the MM veil group, and BezelGlobalBackdrop.
  - New stage group at the end of `BezelNavMenu`: "PRESS ANY / BUTTON" at 108,36 / 108,58 (bz_mm17, `80FFFFFF`); clear logo `bz_mmh_logo` 150,660 640×250; title `bz_mmh_title` 150,920 (bz_b46 alone, bz_mm24 under a logo).
  - All 6996 header and item actions gated with `+ String.IsEmpty(bz_mmhide)`, so the wake key does nothing.
- **Stage feed** `_mmh_stage()`: on a virtual row, `bz_vart_logo` / `bz_vart_title`; otherwise list 60 clearlogo / tvshow.clearlogo / artist.clearlogo / clearart and Label (TVShowTitle for seasons/episodes).
- The MM dim (`bz_at_mmdim`) is intentionally **not** lifted, so the section list behind doesn't show.
- Doc: `behaviors/mm-autohide.md`.

## 5.33.429 — VLANDPICK
- **Root cause:** Music→Movies/TV Select (no audio) clears `bz_nav` (`bz_tovideo` fade) *before* `_bz_load_then_close`. `vwarm` then wiped `bz_vland` on MM close, so `_vw_land` had no target.
- **Change:**
  - `bz_mm.py` snapshots `bz_vland` → `bz_vpick` at Select (only when the key matches the virtual sec); `_vw_land` reads `bz_vpick`.
  - `bz_vland` now carries the library-order index (`st + i` of the label-sorted JSON window). The search starts at that index (+1 for a `..` row), spirals ±400, then scans the rest. Cap is 2.0 s.
  - Mock-tested on a 2,000-item list: exact hint, missing hint, and a hint 20 off all land correctly.

## 5.33.430 — MMEXITHOLD
- Root cause (pre-existing since 5.33.399 OPACITYHOLD, not from 424-429): in 1122 BezelVPLPoster the section twins (`bz_v60_art`, Videos / Music) faded 100->0 in 400 ms on MM open while the MM pos A/B lane image (Conditional, reversible) reverses 0->100 over 1500 ms. Overlap = dip toward black on Movies/TV -> MM.
- Change (XML only, Includes_Bezel BezelVPLPoster): each twin's old fade `![!navmenu + (!)music]` split into (a) `$EXP[bz_navmenu]` fade 100->0 400 ms **delay 1500 reversible=false** (holds under the lane until it is in; MM close resets to 100 instantly = mirror-enter unchanged) and (b) the window-family part `!navmenu + (!)music` as the old reversible 400 ms fade. Twins draw below the lanes.
- Check: Movies/TV -> MM (Back/Left/logo), MM -> section enter (still art-over-art), Music section with poster content.

## 5.33.431 — MMSWAP0 (replaces 430's hold)
- Rob on 430: poster dims, gets brighter, dims again. Cause: the poster sits inside the MM dim (BezelSecDim fade on the 6401 group); Kodi applies the group alpha to each child, so the section twin and the lane stacked at alpha g read 1-(1-g)^2 > g (brighter) for the 1.5 s hold.
- Change: no overlap on MM open.
  - **pos A/B lanes:** the old condition `![navmenu + videos + !mushide + pos_on + !pos_empty + side]` (1500, reversible) is split into (a) the same condition without `navmenu` (1500, reversible = the side-flip crossfade) and (b) `!navmenu` 1500 **reversible=false**. MM open resets (b) to 100 in the same frame, and the front side is already at 100 in (a) because `ab_clock.seed` keeps it on the on-screen poster while the MM is closed. MM close plays (b) out over 1500 as before.
  - **Section twins:** the 430 delayed fade becomes `$EXP[bz_navmenu]` time 0 reversible=false (instant out on open, instant 100 on close).
- Not changed (pre-existing): on MM **close** the lane still fades out over 1500 above the twin at 100. With LOOK Global dim on (gdim, closed-MM dim), that overlap can brighten the poster briefly on section enter. If Rob reports it, the same trick applies: make (b)'s close instant when the textures match.

## 5.33.432 — CONFIRMFOCUS
- Root cause (Kodi Omega `GUIWindow.cpp`, `GUI_MSG_SETFOCUS`): the `SetFocus` builtin targets `GetActiveWindowOrDialog()` (the topmost **modal** dialog). The window first sends LOSTFOCUS to its focused control and only then looks up the requested id. A script `SetFocus(60/6996/…)` while DialogConfirm was up therefore left No/Yes with no focus. That's the shared Yes/No: keep-skin, Remove from library, resets, Media Sources and so on. 5.33.420 MODALGUARD guarded only the strip reclaims.
- Change: `_bz_fg_install(xbmc)` is inlined right after the xbmc import in bz_flip, bz_cmd, bz_warmgate, bz_set, bz_dtap, bz_artist, bz_firstalbum and bz_tune. It wraps `xbmc.executebuiltin` and drops `SetFocus(`/`Control.SetFocus(` while `Window.IsVisible(yesnodialog) | Window.IsVisible(okdialog)`. Idempotent, try-guarded, and everything else passes (mock-tested).
- Not covered: XML `AlarmClock(…SetFocus…)` and window `onload` SetFocus firing while a Yes/No is up. Windows can't activate under a modal, so only delayed AlarmClocks (1117 `bzmsf`, MusicVisualisation `bz_fsfoc`, 1118) could. DialogSelect / context menu aren't guarded, because scripts may legitimately focus inside them.
- Doc: `behaviors/dialog-confirm.md` focus note.

## 5.33.433 — LITSWAP
- Measured the glare alpha: `glare_soft.png` (BzAGLTexA, glare A) is mostly upper-left; `glare2_br.png` (BzAGLTexB, glare B) is mostly lower-right.
- In BezelMusicPlayingArt (playing album, long sway `!bz_swayright`, cover A and cover B), the `BezelLitDust` include inside glare A used the right-half box (`bl 1500, ix -360, lx 1390, ly 45, sx -210`). The one inside glare B used the left-half box (`bl 1080, ix 60, lx 790, ly 645, sx -150`). Rob: the lit sections were swapped for the glares.
- Change: the box/placement param sets are swapped (4 includes). Each include keeps its own `mask` (its glare's texture) and stays inside its glare group, so the dust still fades with that glare's pulse.
- Not changed: Short sway (`bz_swayright`) groups (glare A + right-half box, "right peak only" by design comment) and poster `BezelLitDustP`.

## 5.33.434 — PLITMOVE
- 5.33.402/404 POSTERCENTER moved the poster frame 990 → 1140 (glare images at left 1146, 588×888). The two `BezelLitDustP` mounts in BezelVPLPoster were missed: they kept `bl 1350` / `left 996`, so the dust image (`bl + ix(-354)`) sat at 996, which is 150 px left of the poster.
- Change: both mounts now use `bl 1500`, `left 1146`. The dust image starts at 1146 and the box covers 1500–1734 (poster right side, the same relative spot as before the move). `bw/bh/sx/sy/sd/ix/iy/mask` are unchanged. Verified by render.
- Open question for Rob: both poster glares (A upper-left, B lower-right) share this right-side box, like the album did before 433 LITSWAP. Left as designed unless Rob wants the poster split the same way.

## 5.33.435 — MPKEEP
- Cause: on Next/Prev Kodi stops the current track before the next one starts, so `Player.HasMedia` is false for a moment. In BezelNavMenu that toggled:
  - the audio mini-player group (`Player.HasMedia + !Player.HasVideo`, 200 ms Visible fade), so it blinked;
  - the 6996 list and sub-chip groups' `+120` Conditional slides (×4), so the strip jumped;
  - 6996 `onup` routing;
  - 424's MMSTOPTOP stranded-focus check (`!Player.HasMedia` with focus on 6957–6961), which could move focus to MUSIC mid-skip.
- Change:
  - `mm_autohide` loop (always runs, 50 ms) keeps `Home.bz_mpkeep=1` while media plays and clears it 1.5 s after the last `Player.HasMedia`.
  - New `$EXP[bz_mpup] = [Player.HasMedia | !Empty(bz_mpkeep)]` replaces `Player.HasMedia` in those XML gates.
  - MMSTOPTOP additionally requires `String.IsEmpty(bz_mpkeep)`.
  - Exit cleanup clears it.
- Not changed: the section mini player (`BezelMiniPlayer` in the windows), video mini-player group (`Player.HasVideo`), and `bz_mmaudio` / `bz_mmmushide` (Player.HasAudio) art gates. If the big album or poster also blinks on Next, the same hold can be applied there.

## 5.33.436 — LISTROW
- 5.33.422 LISTCLIP5 set the list 60 clip grouplist and list to 984 (under the 86.67% list scale that gives a visual end of ~y973, 5 px above the dtap hint at y978). 984 isn't a multiple of the row height (video 60, music 75), so a partial last row showed with its text cut, touching the hint.
- Change: View_60_BezelVideoPosterList list + clip 984 → 960 (16 rows). View_60_BezelInfoList list + clip 984 → 975 (13 rows). The hint itself is unchanged.
- 5.33.435 (MPKEEP) was never zipped on its own. 436 is the first build that contains it.

## 5.33.437 — SPOTLIGHT (MM → section title lift) — REMOVED in 438
- **Rob, after 437: "REMOVE THE SPOTLIGHT".** Everything below was taken out again in 438; those files are back to their 436 state for this feature. Kept here for history only.
- **Look:** on a Main-menu pick that opens a section, the highlighted row label (bz_mm28 white, x606, y160+row×56, +120 with the mini player) slides up to the title spot above the colour strip (y60) in 420 ms cubic-out, shrinks to 79% (≈22 pt), crossfades to accent `#8FC4FF` (250 ms after 300 ms), holds, and fades out at 1.5 s (gone by 1.9 s). The rest of the MM fades as before.
- **Where:** new group at the end of `xml/Custom_1122_BigAlbum.xml` (global modeless dialog, so it draws over the closing MM and the new section). 22 per-row conditional Visible slides (11 rows × with/without the mini-player offset).
- **Trigger:**
  - `bz_mm.py` at Select (with 6996 or 6898 focused, `!bz_spot_off`) records Home `bz_spot_t` (Container(6996).ListItem.Label), `bz_spot_r` (Container(6996).Position), `bz_spot_m` (mini player up) and `bz_spot_pend` (time).
  - `bz_flip mm_autohide` loop (50 ms): when `bz_nav` goes true→false within 6 s of a pending pick, sets `bz_spot=1`; clears it at 2.1 s or as soon as the MM reopens. Submenu rows (POWER etc.) never close the MM, so they never fire it. Skipped into fullscreen video / visualisation.
- **Tuner:** MAIN MENU › Spotlight title (toggle, after Auto-hide menu). `Skin.HasSetting(bz_spot_off)` = Off. Info image `media/bezel/info/mm_spotlight.png` (new).
- **Exit cleanup** clears `bz_spot`, `bz_spot_t`, `bz_spot_r`, `bz_spot_m`, `bz_spot_pend`.
- **Check:** each row from top/bottom, with and without music playing (start position must match the row); rows that go through `_bz_load_then_close` (label must still be on screen while the section fades in); POWER / submenus (no lift); Off in Tuner.
- **Risk:** `Container(6996).Position` is the on-screen offset; the strip fits all 11 rows so it equals the row index. If rows are ever added past the visible height, use `CurrentItem` minus scroll offset.

## 5.33.470 — CENTREBAR + revert UPNNPBAR + DUSTDEF + ENTRYHOLD + LISTTIME
Branch `claude/5.33.470` (469 + one commit per item). Rob: "go for all".
- **CENTREBAR** (Rob: "up next fanart is the cycle pill for the up next list in the fanart stage, big album upnext is when big album is center, i want np bar shown when big album is center in both fullscreen, big album np bar hide when switch back to fanart stage"):
  - 450 VIZNPBAR (1122, `BezelNPCompactBar` shifted −480 under the centred album) gate `Window.IsActive(visualisation)` → `[Window.IsActive(visualisation) | Window.IsVisible(1121)]`; `bz_fsnp` (set by 1121 onload too), `bz_railc` (true in 1121 with `bz_pnoff` empty) and `Player.HasAudio` unchanged. Back to the fanart stage (`bz_pnoff` = 1) → `bz_railc` false → its 300 ms fade out; fade in 600 ms after 480 ms as before.
- **Revert 463 UPNNPBAR** (Rob picked "remove"): the bar under the home album with the Up Next fanart list (1122 + 1121 copies) is gone; `git revert` of the 463 commit.
- **DUSTDEF** (Rob: "ambient dust on, distant dust on density med size 90 opacity 60 fade mid slide fast. amb spin on density med size 90 spin 180s"):
  - `bz_tune.json` DEF (Rob's picks; seeded once per DEF ver, applied by every Tuner Reset): `bz_amb_off`, `bz_d3l0_off`, `bz_spin_off` moved from "on" (= set = off) to "off"; `bz_at_d20ssize` 2 → 1 (90%). Already matching: distant Med / 90% / 60% / Mid / Fast, spin Med, spin speed 180 s.
  - DEF ver not bumped (that would re-seed every Tuner setting on existing installs). Rob's box: Tuner > Dust > Reset. Only these 4 values changed (JSON diff checked; compact format kept).
- **ENTRYHOLD** (Rob: "bezel feels slow when new lists are loaded" → all four: wait before rows show, rows animate in slowly, big lists lag, opening a folder):
  - `nav_menu`: the section-entry row hold (`casc_pend`, rows hidden while the old window fades out and the new one fades in; 0.6 s since beta2.2) is `_ENTRYHOLD` = 0.35 s. Folder opens inside a section had no hold and still don't. If rows flash during a section switch, raise it again.
- **LISTTIME:** one `BEZEL list <entry|open> <path> rows after <s> n=<items>` kodi.log line per folder change, once its rows may show (includes up to one 0.1 s poll). Kodi's own library query time is in kodi.log only with debug logging on (Settings > System > Logging), as the music / video database "query took" / "Time to retrieve" lines.
- **Cascade (not changed):** Tuner > List > Cascade speed (1x) / stagger (60 ms → 15th row lands at ~1.2 s) can be tried live; Rob's picks become the defaults.
- **Big lists / folder open (not changed yet):** per-row layouts carry ~30 conditional cascade animations each; trimming them is an XML job, decided after the LISTTIME / debug log shows whether the time is Kodi's query or the skin.
- **Mock:** folder open → `rows after 0.00s`; section entry → ~0.45–0.5 s (0.35 s hold + poll).
- **Check:** big album centred in fanart FS → NP bar under it; back to fanart → it fades; Up Next fanart list → no bar under the home album; entering Music / Movies / TV → rows a bit sooner, no row flash; Tuner > Dust > Reset → ambient + distant dust and the spin layer on.
- **Static checks + mock.** Not device-tested.

## 5.33.469 — TUNERREOPEN + MMNOSLIDE + PILLIDLE
Branch `claude/5.33.469` (468 + one commit per item). Rob's 468 kodi.log: poster_clock getProperty 284/s (465) → ~186/s, so 467 OWNSHADOW saves ~100 Kodi calls/s (mock said 86); no skin errors. Rob: controls / info "minimized Kodi issue", A-Z stage shift "disregard".
- **TUNERREOPEN** (Rob: "exit from tuner then attempt to re enter tuner does not work"; since 463 TUNERBACKQ):
  - Kodi runs a modal dialog's render loop inside `ActivateWindow`, so the rail Back actions after `ActivateWindow(1118)` (and the FS path's `ActivateWindow(1121)` / `ActivateWindow(1115)`) only run once those close. The old trailing `ClearProperty(bz_navtune)` / `ClearProperty(bz_tunesrc)` then ran after the power menu TUNER row (or the 1115 Tuner button 6413) had just reopened the Tuner, and switched it off.
  - Power path: only `ActivateWindow(1118)`; 1118's onload clears both flags (467 TUNERPWR). FS controls path: `ClearProperty(bz_nav / bz_navtune / bz_tunesrc)` first, then 1121 / viz + 1115. The trailing clears are gone.
- **MMNOSLIDE** (Rob: "disable the mm menu slide"; confirmed "keep"): list 6996's Visible slide (−390 → 0, 210 ms) and Hidden slide (0 → +390, 180 ms) removed. The mini-player 120 px shift (`bz_mpup`) and every fade stay.
- **PILLIDLE** (Rob: "auto unfocus pills, after 5 seconds of in activity focus returns to last position"; all pills + the A-Z bar; "where focus came from"):
  - `mm_autohide` (already reads `getGlobalIdleTime` at 20 Hz) calls `_pill_idle` every 5th tick (4 Hz): `System.CurrentControlId` + current window / dialog id.
  - Pills: list FULLSCREEN 6886, cycle 6391 (Kodi FS) / 6421 (fanart FS), big album 6401, MM header 6958–6961 / 6910 (only while the MM is up and no submenu, since a submenu row reuses 6961), A-Z letters 6101–6127. Not pills: dialog buttons (OK / Cancel, keyboard, Settings tabs), the ALL rows.
  - Off a pill, the focused control and window are remembered. On a pill with idle ≥ 5 s: `SetFocus` the remembered control if it was in the same window, else the pill's home (60, 6390 / 6420 / 6400, 6996). One shot per idle period (re-armed on input or focus change). List 60 / 6996 keep their row.
  - Cost: ~8 Kodi calls/s.
  - Mock: focus 60 → 6886, idle 6 s → one `SetFocus(60)`.
- **Static checks + mock.** Not device-tested.
- **Check:** Tuner → Back → power menu → TUNER → the Tuner opens; Music Controls → Tuner → Back → Tuner button → opens. MM opens / closes without the row slide. Leave focus on FULLSCREEN, a cycle pill, the big album pill, an MM header pill or an A-Z letter for 5 s → focus back where it was.

## 5.33.468 — CASTIDLE + CASTFIXEDDEL + LITSPIN2
Branch `claude/5.33.468` (467 + one commit per fix). Rob: all three in one build.
- **CASTIDLE** (Rob: "cast shadow only visible when music is playing, it should be active all times"):
  - `BezelAlbumCast` (1122): the 4 cast copies each had a 200 ms fade to 0 unless `bz_audio_latch` + no `bz_sway_hold` + `bz_sway_go` (/ `bz_sway_pulse`). 453 ONESWAY left the latch term so the cast stayed at 0 with no music, while the one sway rig runs idle too. The latch term is removed; the hold / go terms stay, so the cast still waits for the sway lead-in and hides during a sway restart.
  - `_bz_cast` (bz_flip sway_clock, stub cast L/R opacity) no longer needs the latch either: with no music `t0` is the idle clock `bt0`, and the 441/445 stub anchor (`_sway_anchor`) already tracks the album pulse without music since ONESWAY.
  - Unchanged: the cast hides under the Tuner and under 1120 / 1121 / Kodi FS as before.
- **CASTFIXEDDEL** (Rob: "dont need the fixed, just the default grow and fade"):
  - The 2 static cast copies (`bz_acast_static`, "Animated OFF", classic + right swing) removed from `BezelAlbumCast`; the 2 moving copies no longer test `!bz_acast_static`, so an old ON value can't hide the cast.
  - Tuner: the "Cast shadow animated" row (ALBUM SHADOW), its Left / Right actions and `BzATVal_acanim` removed; `bz_tune.json` TOG entry removed (export / import). The `bz_tune.py` reset of the bool and the DEF map entry stay (they only reset an unused bool).
  - Poster cast (`bz_pcast_static`) not touched.
- **LITSPIN2** (Rob: "can we add another layer to the lit dust?" → "Second spin", album + poster, "same texture as mm dust?" → yes):
  - `BezelLitDust` / `BezelLitDustP` (Includes_Dust3): a second image in the spin group: the same `$VAR[BzD3LSpin]` / `$VAR[BzD3PLSpin]` (default = MM Dust 2.0 spin, `litmm_*_spin`), `flipx` + `flipy`, the 60 speed / direction rotate conditions copied with the direction swapped and the period ×1.3 (default 30 s → 39 s). Same disc mask, colour (`BzD3L_mid` / `BzD3PL_mid`), position, and spin On/Off (`bz_lspin_off` / `bz_plspin_off`).
  - The two discs together are brighter than one; if it's too much, the second disc can take its own lower colour.
- **Checks:** XML parses, bz_flip compiles, audit clean; geometry vs 467: 4 static cast images gone, 8 new spin discs on the existing disc boxes, every other control identical; mock run of bz_flip starts and runs.
- **Check on device:** no music: the big album cast grows and fades with the sway; play / stop: the cast keeps going; Tuner Album / Poster: no "Cast shadow animated" row; album + poster glare: two spin layers turning opposite ways.
- **Not device-tested.**

## 5.33.467 — TUNERPWR + revert TUNERHIDE + rewrite P2.6a OWNSHADOW
Branch `claude/5.33.467` (466 + 3 commits). Rob: "include all together".
- **TUNERPWR** (Rob: "the color strip is not drawn when exit from tuner menu"; caused by 465 TUNERHIDE):
  - The MM strip chrome (BezelNavMenu) is alpha 0 while `bz_navtune` is set; the Tuner card draws its own copy. 465 hid the whole card while 1118 was up, and `bz_navtune` stayed set (the rail's ClearProperty waits for modal 1118 to close), so no strip was drawn.
  - 1118 now runs `ClearProperty(bz_navtune,home)` in its onload, before its first frame (GUIDialog `Open_Internal`: WINDOW_INIT, then the render loop). The screen is exactly the normal power menu from the MM (strip chrome, dust); the Tuner is gone; 1118 already holds the keys, so 463 quick Back stays safe. 1118 is never opened with the Tuner meant to stay.
  - 465 TUNERHIDE (`!Window.IsVisible(1118)` on group 6975) reverted as its own commit; no longer needed.
- **P2.6a OWNSHADOW** (Rob's 465 kodi.log, 10 min, 15 perf lines: ~2,930 Kodi calls/s idle; poster_clock 780, ab_clock 575, nav_menu 565, sway_clock 443, mm_warm 270, mm_autohide 96; getProperty the largest share):
  - `_v60_set(k, v)` (get-compare-set for the 1122 poster / album mirror: `bz_v60_*`, `bz_vpl_on`, `bz_m60_art`, `bz_m_idle_*`, `bz_m_np_art`, `bz_a2p_hold`, `bz_vmus`, `bz_mmh_logo/title`, `bz_v60_mov/tv`) keeps a dict of the last value it wrote. Same value again → no Kodi read, no write. First use in a run or a changed value → reads Kodi first, as before.
  - Safe because every one of these keys is written only through `_v60_set`: no XML Set/ClearProperty, no other script. The one direct write (`bz_vmus` clear in `m_mirror`) now goes through `_v60_set`; the exit cleanup runs after the threads stop. A skin reload drops `bz_flip_running`, so a new bz_flip (fresh dict) takes over.
  - Not 446 TICKCACHE: that cached reads of state other code changes; this only remembers the script's own writes. No timing or poll interval changed.
  - Mock A/B (6 s, Movies list focused): poster_clock getProperty 285/s → 199/s (the real log shows 284/s); the same keys written the same number of times.
  - Left for later P2.6 steps: sway_clock's own flags, nav_menu. ab_clock / mm_warm (locked mm-warm system) not touched.
- **Check:** Tuner: Back on the rail → power menu with the colour strip, no Tuner; Back → MM. Posters / album art / MM art behave as 466. Next kodi.log: poster_clock gp ≈ 200/s.
- **Static checks + mock A/B.** Not device-tested.

## 5.33.466 — ALBUMCOVER + ALBUMPILL + GENREMETA
Branch `claude/5.33.466` (465 + one commit per fix). P2.6 waits for Rob's 465 kodi.log.
- **ALBUMCOVER** (Rob: "music album section uses an old list and not the newer album list", "as well as recent played"; confirmed the cover list):
  - `bz_covercol` (list 60's cover-list mode: 450 cover on top of the column, 75 px rows under it) applied to the root Albums node only with `Skin.HasSetting(bz_albumlist)`. bz_flip sets that bool on entering `musicdb://albums/`, but on Rob's box it was off and stayed off, so Albums and Recently played drew the plain 60 px list.
  - The clause is now `Window.IsActive(music) + Container.Content(albums) + !bz_artistalbums` (artist albums keep their own clause). Covers Albums, Recently played / added, Genres / Years → albums, compilations. `!bz_grid_music` dropped (reset at start since 455 GRIDDEL). The bz_flip SetBool is left (harmless; no Python change in this build).
- **ALBUMPILL:** `BezelViewName` / `BezelViewPillText` show ALBUM LIST / ALBUMS on `Container.Content(albums)` instead of the bool.
- **GENREMETA** (Rob screenshot: Genres showed GENRE 80S / ARTIST ALBUMS 812 / ARTIST SONGS 13380 over the rows):
  - The old strip info card in `View_60_BezelInfoList` (music info pairs, biography header + text, album year pairs, album text: 9 parts at strip x+30) was alpha-0 only for `bz_mstrip` (artists / albums / songs, 278 STRIPLIST). Every music folder draws list 60 in the strip, so in genres / years / roles / sources the card painted under the rows.
  - The 9 fades are now `$EXP[bz_mstrip] | Control.IsVisible(60)`. Video already hides its card for folders (`bz_vfold` in `bz_vstrip`).
- **Check:** Music → Albums and Recently played: cover on top, rows under it; Genres: rows only, no info text behind them; artist → albums and album tracks as before.
- **Static checks:** XML parses; geometry identical to 465; audit clean. Not device-tested.

## 5.33.465 — TUNERHIDE + DEL1104 + OLDPILL + OLDNP + rewrite P3.4–P3.6
Branch `claude/5.33.465` (464 + one commit per item, 7 commits).
- **TUNERHIDE** (Rob: "tuner menu exits but is still drawn on exit from tuner"; caused by 463 TUNERBACKQ):
  - 463 put `ActivateWindow(1118)` before `ClearProperty(bz_navtune)`. 1118 is a modal dialog, and Kodi runs a modal dialog's render loop inside `ActivateWindow` (GUIDialog.cpp `Open_Internal`), so the later ClearProperty only ran after the power menu closed. The Tuner card stayed drawn under 1118.
  - Tuner group 6975 now also needs `!Window.IsVisible(1118)`. The 463 order stays (the power menu takes the keys first, so quick Back is still safe). When 1118 closes, the held ClearProperty runs before the next frame. 1118 never opens the Tuner.
- **DEL1104:** `Custom_1104_Fanart.xml` (Estuary fullscreen fanart window) deleted; nothing opened it.
- **OLDPILL** (Rob: "a fanart overlay with the cycle pill in the old upper right fanart stage position … kodi fullscreen when return from big album back to the fanart … for a while now in many builds"):
  - `BezelNPInPlace` is drawn in the music list (View_60, default params: pill at 620 right-aligned = the old upper-right spot) and in MusicVisualisation (pill at 140,136). Under 1121 the music copy is the current fanart stage; its pill hid only while 1121 was visible, so it faded in around 1121 opening / closing.
  - The pill grouplist (6391) and the "press down to open" hint now need `Window.IsActive(visualisation)`. Kodi FS pill: same position and the same effective condition (viz + `bz_pnoff` = 1). 1121 keeps its own pill 6421. Geometry for MusicVisualisation and 1121: identical to 464.
- **OLDNP** (Rob picked "old pill + routes"; "remove the old code so I won't see the wrong screen"):
  - The old Now Playing (in-place panel as a screen of its own, and dialog 1112) is removed. `bz_cmd.py` `np` / `nptoggle` / `tab` / `vistoggle` are one block that opens the current fullscreen like the MM FULL pill: 1121 from the music window (kill switch `bz_m1121_off` respected), else Kodi FS.
  - Routes this covers: auto Now Playing after idle (Tuner `bz_at_autonp`, off by default), tap / Select on the playing song, Info with no album (`xinfo`), and Tab pressed while Kodi was busy (`bz_flip.py` bz_tabq, now `ActivateWindow(1121)` like the Tab keymap).
  - `Custom_1112_NowPlaying.xml` and the `<window1112>` keymap section deleted. The ~60 remaining `Window.IsActive(1112)` / `Dialog.Close(1112)` references are conditions / no-ops (false / nothing to close), left for a later pass. The MM menu itself is drawn elsewhere (`BezelNavMenu` in Includes_Bezel).
  - The music window's in-place panel stays: it is the fanart stage under 1121.
- **P3.4:** 18 parked `<visible>false</visible>` controls with no ids inside (so no focus / navigation target) removed, plus the 2 variables they used (`BezelMenuVidArt`, `BezelStats`). Kept: TUNERCLEAN's 5 labels and every hidden control holding an id (Kodi-required ids like 50 / 60 / 10, and nav targets such as 6891 / 6392 / 6880). Geometry: 156 resolved controls gone (all inside the removed ones), every other control identical.
- **P3.5:** the always-false grid conditions removed (control 6600 gone since 455 GRIDDEL; `bz_gridfirst` was `false`): the grid title value, `bz_listbar`'s 6600 term, two focus-visible terms, 4 grid fades, 2 gridenter onrights, 2 `!Control.IsVisible(6600)` terms, the MyMusicNav / MyVideoNav grid onloads, then `bz_gridfirst`. Geometry identical.
- **P3.6:** `bz_cmd.py` actions with no caller removed: `gridfocus`, `gridenter`, `gridclick`, `gstyle_removed_beta11` (65 lines).
- **Totals:** 49 lines added, 325 removed; XML 4,602 KB; audit 0 unused includes / expressions / variables.
- **Check:**
  - Tuner: Back on the rail → power menu with no Tuner under it; Back → MM.
  - Kodi FS and fanart FS: big album → Back to fanart: no pill at the upper right; the upper-left cycle pill works as before (six modes).
  - Music list: Tab → fanart FS; with Tuner auto Now Playing on, idle → fanart FS; Select on the playing song → fanart FS.
  - Everything else looks as 464.
- **Static checks + mock run of the new route block.** Not device-tested.

## 5.33.464 — rewrite P2.4 SWAYEPOCH (one sway epoch)
Branch `claude/5.33.464` (463 + one commit). A/B against 463.
- **Rob:** "can clock and event be tried next?", then "clock".
- **P2.5 event-driven playback: not built.** bz_flip.py has ~25 playback checks in total, most compound with window / focus terms (`Player.HasAudio + Window.IsActive(music) + Control.HasFocus(6996)` …), so the Kodi call stays.
  - Replacing the pure ones saves ~50–100 of ~3,000 calls/s (2–3%).
  - Kodi's play / stop events don't reproduce the brief `Player.HasMedia` drop on Next / Prev that 435 MPKEEP relies on.
- **P2.4 finding:** the sway clocks were already merged in 391 SHARED ART CLOCK / 406 ALWAYSSWAY / 415 SWAYCONT. The poster flags (`bz_pswayon` / `bz_ppulse` / `bz_ppulse2`) are scheduled onto the album pulse grid (t0 + 7.4 + k·24.5 s) by `_art_sw_anchor` from `_art_epoch()`.
  - poster_clock's ~520 Kodi calls/s are its list-60 nav guards (ALL / hidden `..` / TV seasons bounces), poster key tracking, movie holds and `m_mirror` / `v60_mirror` / `_a2p_tick`, not the sway. So no call saving from a clock merge.
- **SWAYEPOCH (the one gap):** with no music, `_art_epoch()` fell back to its own `sway['art0']`, while sway_clock used `sway['bt0']`, each set at start-up by a different thread.
  - The poster grid sat off the album grid by that gap, and kept it after music started (the 415 latch continues bt0).
  - `_art_epoch()` now falls back to `bt0`, created there if poster_clock asks first; `art0` is gone.
  - Mock run: `bz_art_t0` == `sway['bt0']` at start-up.
  - Not covered: after a real sway restart (`bz_sway_restart`, viz / playlist onload) the album re-zeroes, while the poster pulse keeps its original phase (it is never re-armed, by design since 406).
- **Check:** album and poster sway as before; MM crossfades between an album row and a poster row stay in step.
- **Static checks + mock run.** Not device-tested.
- **Next for performance:** per-tick checks in nav_menu (~1,110 calls/s) and poster_clock's nav guards (~520). Needs a kodi.log (`BEZEL perf` lines) from Rob's device.

## 5.33.463 — VIZSETRESET + TUNERBACKQ + UPNNPBAR
Branch `claude/5.33.463` (on 462, one commit per fix).
- **VIZSETRESET** (Rob: "music controls get stuck in vis settings and does not reset to level 1 after close"):
  - The viz settings page in 1115 is shown by the window property `bz_vizset`. It was set and cleared with `SetProperty` / `ClearProperty` without a window id, which act on the focused window.
  - The `onunload` clear runs while 1115 closes, when the focused window can be the one underneath. So `bz_vizset` could stay set, and the next open showed the viz page with focus on the level-1 control (`defaultcontrol` 6401).
  - Now every set / clear names window 1115 (13 actions), the page condition reads `Window(1115).Property(bz_vizset)`, and 1115 also clears it on load.
- **TUNERBACKQ** (Rob: "quick back from tuner menu drops in random window??"; follows 462 TUNERBACK):
  - Back on the rail ran `ClearProperty(bz_navtune)` (hides the Tuner and its focused control) before `ActivateWindow(1118)`. In between, focus sat on the window underneath, and a fast second Back ran that window's Back.
  - The two actions are swapped: the power menu takes focus first. Kodi evaluates all action conditions up front, so only the order changes.
- **UPNNPBAR** (Rob: "add a np bar when up next is trigger in kodi fullscreen"; picked compact NP bar, under the big album, "fades in with upnext. back to fanart fades it out", Kodi FS + 1121):
  - Up Next keeps the big album at home (`bz_pnoff` = 1, `bz_railc` off), so `BezelNPCompactBar` is drawn unshifted: album 1140–1740, y 892–1004. 450 VIZNPBAR stays the copy for the centred album.
  - **Kodi FS:** a new group in 1122 after VIZNPBAR (1122 renders above the viz window), gate `Window.IsActive(visualisation) + bz_fsnp + bz_np + bz_npm_upn + !1121 + !bz_railc + Player.HasAudio`.
  - **1121:** a new group right after its `BezelFSUpNext`, with the same gate as that list (`bz_npm_upn + bz_pnoff = 1`) + `Player.HasAudio`.
  - Fades 300 / 300, the same as the Up Next list. No overlap with BezelFSPlayNext's bar (that one needs `bz_pnoff` ≠ 1).
- **Check:**
  - Music Controls: open viz settings, close, reopen → level 1.
  - Tuner: Back, Back, Back fast → power menu → MM.
  - Kodi FS and fanart FS: cycle to Up Next → the bar fades in under the album; back to fanart → it fades out.
- **Static checks only:** XML parses; resolved positions checked for the new bars. Not device-tested.

## 5.33.462 — TUNERRAILNUM + TUNERBACK + LITMM
Branch `claude/5.33.462` (on 461, one commit per fix).
- **TUNERRAILNUM** (Rob: "tuner menu rows have days and months?? and random labels??", also on 460; then "hide"):
  - The 13 rail items (7001, since 439 TUNERRAIL) held their settings count as `<label2>29</label2>`. Kodi reads a bare number in a static item label as a localized string id (11–17 weekdays, 21–32 months, small ids e.g. "Music").
  - The count now lives in `<property name="n">` (properties are never localized). Per Rob, the 3 rail count labels are then removed, so no count shows.
- **TUNERBACK** (Rob: "back from tuner level 2 takes you back to level 1" → should; "back on level 1 back to power menu"):
  - Rows list 6970: its 11 onback actions (a copy of the rail's) are replaced by `<onback>SetFocus(7001)</onback>`.
  - Rail 7001: the power-menu branch (ClearProperty bz_navtune + `ActivateWindow(1118)`) now runs for every `bz_tunesrc` except `fsctrl`. The FS controls source still returns to 1121 / visualisation + 1115. The BEZEL Settings (6968) / MM (6996) focus targets are dropped.
  - No script intercepts Back here (the bz_dtap Back keymap covers only Kodi settings windows).
- **LITMM** (Rob: "does lit dust have other textures or layers available? i dont like the look. i want the same look as mm dust in the album and poster lit dust"; picked "Make it the default"):
  - 8 new textures cut from the MM Dust 2.0 sheets at their MM on-screen scale. Mid / far sheets draw stretched 1.1× horizontally in the MM; spin draws 1:1.
    - `d20_mid_med` → slots 1–2, `d20_far_med` → slot 3, `d20_spin_med` → spin.
    - `litmm_a_1..3` 600×600 + `litmm_a_spin` 660 (album slots).
    - `litmm_p_1..3` 588×888 + `litmm_p_spin` 920 (poster).
    - All > 512 px, so loose files; `Textures.xbt` is unchanged.
  - `BzD3LS_*` / `BzD3LSpin` / `BzD3PLS_*` / `BzD3PLSpin` (Includes_Dust3) default to them. `Skin.String(bz_at_alitset / bz_at_plitset)`: empty = MM, 1 = V1.0 specks (+ size rows), 2 = V2.0 bake.
  - Lit layers, drift / spin animations, glare masks and brightness are unchanged.
  - Tuner rows "Album / Poster lit dust Version": MM / V1.0 / V2.0, cycled by OK / Left / Right. Kodi evaluates all action conditions before running any (GUIAction.cpp), so the cycle doesn't chain. The old `bz_alit20` / `bz_plit20` bools are no longer read; "Reset dust" also clears the two strings (bz_tune.py).
  - The new look is much finer / sparser than V1 (same as the MM). The low / high MM sheets can be cut instead if it's too subtle.
- **Check:**
  - Tuner rail shows section names only.
  - Back on a settings row → rail; Back on the rail → power menu.
  - Album and poster glare: lit dust looks like the MM dust.
  - Tuner lit dust rows cycle MM → V1.0 → V2.0.
- **Static checks only:** XML parses, bz_tune.py compiles, geometry unchanged apart from the 69 removed count labels (3 × 23 windows). Not device-tested.

## 5.33.461 — rewrite P3.1–P3.3 (dead definitions)
Branch `claude/5.33.461` (on 460, one commit per pass).
- **P3.1:** 31 unused includes + 14 unused expressions. Among them: the `bz_gsm_*` / `bz_gsv_*` / `bz_gridlistlit` grid leftovers, Estuary Weather / submenu / button includes, `BezelXInfo`, `BezelSwingPoster`, `BezelRainbowRow`, `BezelNavLogoGlow`, `BzCIStripUnder`.
- **P3.2:** 313 unused variables + 1 include (`UserRatingContent`, freed by P3.1). Mostly Estuary `Variables.xml`, the pre-TUNERRAIL Tuner sets (`BzATStep_` / `BzATVal_` / `BzATBar_` / `BzTSec_`, each appearing only at its own definition), old Dust3 and NP-card vars.
- **P3.3:** the last 4 variables freed by P3.2. The audit is now clean: 0 unused includes, expressions or variables.
- **How:** `tools/rewrite/audit.py` counts uses in all XML (`<include>NAME</include>`, `content=`, `$EXP[…]`, `$VAR[…]` incl. `$VAR[NAME,prefix,suffix]`), all `scripts/*.py` / `*.json`, and include param values. No name is built from `$PARAM` or a Python format string. `tools/rewrite/rmdefs.py` removes the definitions at text level; everything else stays byte-identical.
- **Checks (static):** XML parses; no dangling reference; all 19,243 resolved controls identical; `bz_tune_patch.patch` run on a copy still applies to the same files and parses, as on 460. ~220 KB less XML.
- **Check on device:** Kodi starts and the skin loads without errors (kodi.log: no "Skin has invalid include" / "unknown variable"); Tuner rows still change values; MM, sections, info / settings dialogs, FS music look as 460.
- **Static checks only.** Not device-tested.

## 5.33.460 — MMDIMQUICK (on 458 without P2.2)
Branch `claude/5.33.460` (from `claude/5.33.459` with P2.2 reverted, so bz_flip.py = 458).
- **MMDIMQUICK** (Rob: 457 "very smooth and responsive"; 458 MM backgrounds "row switch looks bad, open / close looks bad"; picked "Quick dim, no wait"):
  - 458 MMNODIM is reverted (its own commit), and the 456 MMCLEANFADE `delay="1500"` is removed from the 22 `bz_at_mmdim` fades.
  - The 22 fades are now identical to 455 (600 ms sine in-out, no delay; checked against `claude/5.33.455`). Only comments differ.
  - To watch: this is the 455 timing, which caused Rob's original "fades black then back" report. If the dip shows, the next option is the dim running over the same 1.5 s as the MM art lane, starting at once.
- Keeps **P2.1** (`grid_sync` removed) and **P2.3** (`bz_big_*` no longer set) from 458. **P2.2 is not included** (459 rejected).
- **Check:** open / close the MM and switch MM rows from Music / Movies / TV. It should feel like 457, with no 1.5 s wait.
- **Static checks only:** XML parses. Not device-tested.

## 5.33.459 — rewrite P2.2 (A/B against 458)
**RESULT: REJECTED on device.** Rob: "457 great", "458 good", "459 very bad" (backgrounds perform poorly). P2.2 is reverted on `claude/5.33.459`; use 458. Not retried without a 459 kodi.log.
Branch `claude/5.33.459` (458 + one commit).
- **P2.2:** `km_leave_watch` (1 s), `fpop_clock` (1 s), `allcnt` (0.4 s), `album_id` (0.5 s) and `cw_clock` (1 s) were five threads. Each is now a generator that yields its own wait instead of `mon.waitForAbort`, so its body and poll interval are unchanged. One `slow_watch` thread schedules them.
  - A watcher that raises is logged (`BEZEL bz_flip watcher <name> crashed`) and restarted, max 5, like `_bzstart`.
  - `cw_clock`'s Continue-watching library queries run in a short-lived `cw_build` thread, so they never delay the others. Its 2 s wait after a video stop is a scheduled yield.
  - Known difference: a slow file check in `fpop_clock` (only with fanart_pop on, on a folder change, e.g. a sleeping NFS share) or a slow JSON-RPC in `allcnt` / `album_id` now delays the other two by that long. Before, they were independent.
  - bz_flip helper threads: 18 → 13 (plus the short-lived `cw_build`).
- **Mock run** (stub xbmc, 8 s): album_id every 0.5 s, fpop every 1.0 s, allcnt every 0.4 s (first after its wait), cw every 1.0 s; the start-up Continue-watching build ran, and a second build ran 2.0 s after a simulated video stop while the other watchers kept running.
- **Check (A/B with 458):** ALL row count label (N SONGS / N EPISODES) appears as fast as before; the playing album's content path works (album id); TV Continue watching updates after stopping an episode; switching to another skin still removes BEZEL keymaps; no stalls entering sections. The `BEZEL perf` lines in kodi.log now show `slow_watch` instead of the five names.
- **Static checks only + mock run.** Not device-tested.

## 5.33.458 — MMNODIM + rewrite P2.1, P2.3
Branch `claude/5.33.458` (one commit each, on 457).
- **MMNODIM** (Rob on 457: the 456 MMCLEANFADE 1.5 s dim delay "makes it look broke"; "just have it fade in quick. no fade out of section"):
  - The 22 `bz_at_mmdim` Background-dim Conditional fades (11 steps each in `BezelSecDim` and `BezelSecDimArt`, gated on `$EXP[bz_navmenu]`) are removed. The section stays at full opacity under the MM, and the MM fades in over it.
  - Unchanged: Global dim (`bz_at_gdim`, outside the MM), the Dust3 MM-dim lit levels, the 1117 MediaSources static dims, and the MM art lane fade (1500 ms; it belongs to the locked mm-warm system).
  - Side effects: the Tuner "Background dim" row has no MM effect now; on MM rows with no art the section shows undimmed.
- **P2.1** (rewrite): `grid_sync` thread deleted (140 lines). Control 6600 doesn't exist since 455 GRIDDEL, so the thread only ran its idle branch (0.3 s poll, clears `bz_gslot` / `bz_gpend`).
  - `bz_gpend` is set only with `bz_grid_video` (reset at start) and is still cleared by the MyVideoNav onload AlarmClock (2 s).
  - Left for P3: bz_cmd `gridenter`/`gridclick`/`gridfocus` (only run when called), the 41 always-false XML `6600` conditions. Left for P2.6: nav_menu `bz_grid_*` checks.
- **P2.3** (rewrite): `sway_clock` no longer sets `bz_big_go` / `bz_big_pulse` (no XML has read them since 453 ONESWAY). Saves ~40 Home calls/s. The exit cleanup still clears them.
- **Check:** open the MM from Music / Movies / TV and close it again: the MM fades in over the section with no dim, delay or dark dip. Video sections still appear after loading. The album sway is unchanged.
- **Static checks only:** XML parses, bz_flip.py compiles. Not device-tested.

## 5.33.457 — rewrite P1B + P1C (layout from constants, no visual change)
Branch `claude/rewrite-p1b` (one commit per step), built as `claude/5.33.457`. Plan and tools: `REWRITE_PLAN.md` section 5.
- **P1B part 1** (98 containers): the warm-strip dialogs, main menu, Tuner and MusicControls wrapped their strip in a group still at the pre-455 strip x **570** with children +90. Those groups now sit at `bz_strip_x`; every direct child is compensated (left −90, include-param origins, own animation centres; position-less wrapper groups pass it down). Full-screen dims and the stage panel inside the strip use two new companion constants, `bz_strip_nx` −660 and `bz_strip_tostage` −540.
- **P1B part 2** (29 groups): groups at x 0 holding only strip content (or full-screen / stage anchors) now sit at `bz_strip_x`, children −660. Outermost group only.
- **P1B part 3** (165 elements, 640 uses): strip elements placed with absolute lefts (690, 819, 984, 1002 …) are wrapped in `<control type="group"><left>bz_strip_x</left><!-- P1B -->` with their left −660. Skipped on purpose: BigAlbum casts (strip in 1122, art elsewhere), grouplist children, legacy PVR windows.
- **P1C:** new `bz_fill_w` 540 on the 18 stage fills (120–660); 60 screen-level lefts 120 → `bz_stage_x`; 31 screen-level 1140 → `bz_art_x`. The old unused `bz_block_x`/`bz_block_w` (390) are the strip in the old naming, left for P3.
- **Moving the strip now:** change `bz_strip_x` and, with it, `bz_strip_nx` (= −bz_strip_x), `bz_strip_tostage` (= bz_stage_x − bz_strip_x) and `bz_fill_w` (= bz_strip_x − bz_stage_x), all on Includes_Bezel ~2570 (Kodi constants can't do arithmetic). Strip+1 simulation: 4,829 of 4,885 strip controls follow.
- **Checks (static):** all 18,603 drawn controls and absolute animation centres unchanged against 456 (geom resolver; wrapper groups filtered); no rotation without a centre exists (Kodi uses the parent origin there); zoom without a centre uses the control's own rect; Kodi focus/default-control lookup is recursive (GUIControlGroup.cpp), so id-less wrappers change nothing. XML parses; every position value is a number or a defined constant. **Not device-tested.** Device check: every strip window (MM, sections, settings, sources, context, info, select, keyboard, Tuner, MusicControls) looks and animates exactly as 456.

## 5.33.456 — fixes on 455 + rewrite P1A
One commit per fix, so each can be reverted on its own with `git revert` (branches `claude/5.33.456-wip`, then `claude/rewrite-p1`, built as `claude/5.33.456`):
- **IDLEHOLD** (Rob: "small black pulse on big album on music start"):
  - The idle A/B slots (`BezelMusicPlayingArt` idle stack) faded out on `Player.HasAudio` with `bz_at_midlefade` (300 ms since 454). That ran under the NP layer's 400 ms fade-in, so the crossfade dipped and the dark backing showed.
  - The 14 slot conditions are now side-flip only (`bz_m_idle_side`). The NP layer fades over the opaque slots, and the idle group still hides at 1200 ms under the opaque playing cover.
- **TRANSCENTRE** (Rob: "transport bar labels need to be centered for the new stage"):
  - The `BezelNPInPlace` transport bar: STAGEWIDE had moved only its right half (+90).
  - The left label and icon and the centre control moved +45, the right label and icon −45, so they are symmetric about x 585. The prev/next pills stay at 128 and 816–1042. 6 copies each, including the live shadows.
- **MMCLEANFADE** (Rob: "transition in out from mm fades black then back can we just do a clean fade"):
  - The section Background dim (`bz_at_mmdim`, 600 ms) ran while the MM art lane was still fading in (1500 ms), so the screen went dark and came back.
  - The 22 mmdim fades (`BezelSecDim` + `MMHIDE` variants) now have `delay="1500"`. The exit reverse is immediate (Kodi reverses don't wait for the delay), and the lane fades out over the undimmed section.
- **TUNERCLEAN** (Rob: "tuner menu remove nav legend and section labels that show in the art window on right"):
  - 5 labels hidden in `Includes_Tuner` (`<visible>false</visible>`): both UP/DOWN legends, the rail section name (7001 Label) and its "N settings" line.
- **GLOWSHIFT** (Rob: "glow textures need to be redone for new larger stage position"):
  - The 17 `media/bezel/glow/mm_glow_*.png` textures are 960×540, drawn 1920×1080 at screen x 0. Each carries a soft strip-shaped panel baked at the old strip.
  - They are shifted 45 px (90 on screen), with the left column replicated.
  - Removing the panel was tried and dropped: the light effects (starburst, streaks, prism, rings) are painted through it. Rob: "skip glow".
  - They aren't bundled (>512), so no xbt repack.
- **FSTITLE** (Rob: "title displayed on the fanart stage in kodi music fullscreen … hidden all the time, only cycle pill on fanart should hide it"):
  - In `MusicVisualisation.xml`, `BezelFSMeta` was included before `BezelNPInPlace`, whose block (`bg=true`: black + artist fanart, 120–1050) is opaque. The meta was always covered. The panel's own title is off in viz by design.
  - The meta is now included after the panel. Its FANART-pill hide (`bz_npm_fan`, Tuner override `bz_fschrome_fan`) is unchanged.
- **P1A** (rewrite step 1):
  - New constants `bz_stage_x` 120, `bz_stage_w` 930, `bz_strip_x` 660 and `bz_strip_w` 390. The unused `bz_block_x` is now 660.
  - 395 exact-value literals and include params use them.
  - `tools/geom455`: 18,603 resolved controls, 0 boxes changed, and no constant appears outside position tags.
- **Not changed:** the Up Next "playing item drawn multiple times" report and the glow remake (Rob: skip).
- **Plan for the rewrite:** `REWRITE_PLAN.md` (repo root on `claude/5.33.456`, project `claude/REWRITE_PLAN.md`, Downloads).
- **Check:**
  - Start and stop a song (no dark blink).
  - Fullscreen music transport centred.
  - MM in and out is a plain fade.
  - Tuner art window has no legend or section name.
  - MM glow sits behind the strip.
  - Kodi fullscreen music shows the title and progress on the fanart stage, hidden only with the cycle pill on FANART.
- **Static checks only:** XML parses, reference audit clean, geometry diffed. Not device-tested.

## 5.33.455 — STAGEWIDE + GRIDDEL
- **STAGEWIDE** (Rob: "extend the fanart stage right to lessen the gap to the artwork, keep list and color strip same size give extra space to fanart"; picked "Strip moves right", "Gap 90 (+90)"; "mm must move to new fanart stage position"):
  - **New layout:** fanart stage x 120–1050 (930 wide, was 840). Colour strip x 660–1050 (390, was 570–960). Gap to the art (x 1140) is 90 (was 180). The art itself does not move.
  - **How it was done:** a static geometry resolver (`tools/geom455/geom.py` in the repo) expands every window's includes, params and constants and computes each control's absolute x box. `plan.py` then shifts the topmost strip-column controls (boxes inside 570–960, or 570–1020 for the wider context-menu strip) by +90 and widens stage boxes (120–960) by +90. It edits the element that holds the value (the literal, or the include param that feeds it). `diff.py` re-resolves and checks that every control moved exactly as expected. 0 unexpected moves remain, apart from the intentional manual ones below.
  - **Moved +90, same size:** the MM strip and rows, section strips and lists, the small album, the ALL rows and pills, and every strip dialog (settings family, sources, add-ons, search, power, context, info, select, keyboard, confirm, PVR, file browser, Tuner list).
  - **Section lists:** they sit in a zoom group, so the static slide `517,0` → `620.84,0` (×3: music list, video list, 6098). Visual x ≈ 658.2, the same 1.9 px inset as before.
  - **Widened +90:** stage layers (`BezelFanartLayer` 840 call sites, `stagew`, viz / in-place NP block), 3 px stage frames (846 → 936; right line 960 → 1050), and block-left dims (120–570 fills 450 → 540, incl. the `listw` default).
  - **In-place NP / FS meta / Up Next** (`BezelFSUpNext`, `BezelFSMeta`, `BezelNPInPlace`): the 150–930 column becomes 150–1020 (list and layouts 779 → 869). Right-aligned and right-column items +90.
  - **Right panels that started in the old gap** (Rob: "scale for the new fanart area"): start +90 with the same right edge (width −90). This covers the section-settings description (515), the MM/Tuner info panel (501–503, 523), SettingsCategory, SettingsProfile, SkinSettings, the dialog info panel (3787/3791) and the mini-player tap target 6160. The 130 px icons only shift.
  - **TV episode drum:** 900×506 @ 990 → 810×455 @ 1080 (uniform 0.9 about the centred face). Drum slides `0,±526` → `0,±473` (`BezelATEpSlideDown/Up`).
  - **Casts:** the album cast (`BezelAlbumCast`, 1122) clip goes 570 → 660, the inner group −570 → −660, the images 480 → 570 and the zoom centres 960,520 → 1050,520. The poster cast images 480 → 570 and centres 960,570 → 1050,570. Both stay pinned to the strip's right edge.
  - **Other:** the playing-video box in Movies/TV is recentred (+45, covers 655 → 610). `BezelRootArtHide` 962 → 1052. `BezelShadow` 554 → 644. The MyPics scrollbar 952 → 1042. The 1114 dust void clips that ended or started at 930/950/960 move +90; two 80 px strips between the strip and the album no longer exist and are hidden.
  - **Not changed:** the big album / poster position, the FS transport and the centred album (rail centre), the PVR guide timeline (legacy, x 570–1800) and the top bar.
- **GRIDDEL** (Rob: "delete the grid views we will make new ones at a later date"):
  - `BezelGridMusic/Video`, `BezelGridOverlayM/V`, `BezelGridBounceAnim` and the grid poster/style vars are deleted.
  - `bz_gridm`, `bz_gridv`, `bz_gridset` and `bz_gridfirst` are now `false`.
  - The view-pill grid toggle is removed.
  - `bz_flip` resets `bz_grid_video` at start, as it already did for `bz_grid_music`.
  - The reference audit shows no new missing include, var or exp.
- **Commits** (branch `claude/5.33.455`, both repos): `455 STAGEWIDE`, `455 GRIDDEL`, then the version and changelog commit. Either feature can be reverted on its own.
- **Check:**
  - MM, Music, Movies, TV, Pictures and Settings: the strip sits at 660–1050 with fanart filling 120–1050, and the art is 90 px to the right.
  - Small album and ALL rows sit flush in the strip. Context menu, info and select dialogs are in the strip.
  - Album and poster cast shadows fall from the strip edge and sway as before.
  - TV episodes: the drum turns at the new size.
  - FS music / viz: the stage fades and Up Next / meta use the wider column.
  - Dust doesn't paint over the strip.
  - No grid toggle.
- **Static checks only:** all XML parses, `bz_flip.py` compiles, and geometry was diffed across 18,942 resolved controls. Not device-tested.

## 5.33.454 — SPEEDS + FADEINS
- **SPEEDS** (Rob: "add recommended speeds to build"; "can the list feel more floaty?"; he didn't pick from the options, so I used my floaty pick):
  - `bz_flip.py` sets, once (flag `Skin.String(bz_spd454)`): `bz_at_rowscroll=3` (0.6x = 317 ms, cubic-out ease unchanged) and `bz_at_midlefade=3` (300 ms).
  - The shipped `bzt="row"` scrolltimes are 271 → 317, so XML and the Tuner agree with no repatch or ReloadSkin.
  - The Tuner can change both afterwards.
  - **Not set:** the Tuner "A/B fade" row (`bz_at_abfade`, 800–2500 ms) has no consumer; no XML or Python reads it, and the MM A/B lanes use a fixed 1500 ms. Wiring it up is a separate change.
  - Known display quirk (not changed): `BzATVal_rowscroll` labels an *empty* string "1x" while the patch default is step 4 (0.7x = 271 ms). This build sets an explicit step, so the label is correct.
- **FADEINS** (Rob: "I prefer fade ins for all transitions"; picked art changes, menus & dialogs, section changes and fullscreen screens; "keep slides for big album"):
  - `Includes_Animations.xml`: the 18 zoom effects in window/dialog open/close and visible/hidden anims are removed. Fades and timings are kept.
  - `Includes.xml`: four grow-zoom WindowOpen/Close pairs → fades (same delay and time).
  - Slides → fades: 1115 Music Controls (open 250 / close 420), 1116 Pause Screen (600), `Includes_BezelDialogs` 579 (300), DialogNotification (300, the existing late fade-out is kept).
  - Main-menu row cascade: the 18 `slide 0,-20` drop-ins are removed; the fades and stagger are kept.
  - Section list cascade: 480 `slide 0,-40` → `0,0` (no movement), so the Tuner cascade speed and stagger still apply. The `bz_tune_patch` cascade anchor now accepts `0,-40 | 0,0`; 480 anchors are verified to match.
  - Fullscreen stage: every `slide 0,0 → −1100,0` Conditional → `fade 100 → 0` (same time, condition and reversibility), and the `−1100 → 0` WindowClose → fade `0 → 100`, in MusicVisualisation, Custom_1112 NowPlaying and Includes_Bezel.
  - Not changed: the big album rail slide (centre / home), the leaf flip (locked), the Tuner drum `eposlide` option, the MM dust drift, and the A/B art lanes (they already crossfade; their `fadetime 0` slots are faded by the lane anims on purpose).
- **Check:**
  - Open and close Settings / info / context dialogs, Music Controls, Pause, notifications: fade only.
  - Main menu opens with rows fading in, no drop.
  - Enter Music / Movies / TV: rows fade in, no drop.
  - Fullscreen music → Play Next / album viz: the stage fades away while the album slides to centre; back: the stage fades in.
  - List scroll feels floatier.
- **Rollback:** the files from 5.33.453.

## 5.33.453 — ONESWAY (one continuous big album sway, idle + playing)
- **Rob:** "use only 1 continuous unbroken sway anim, if I want a diff style later I will work on it"; "the playing style and textures should be for both"; "no reset on play".
- **Before:** `BezelMusicPlayingArt` (1122, home + centre copies) had two rigs.
  - Idle rig: L1081, camera 1440,570, rotatey on `bz_big_go` / `bz_big_pulse`, excluded in 1120 / viz. It held the idle art, leaf hinge, frame and its own glare/dust copy (`BzATGlareTex` @ `BzATGlare8C`, IDLELIT dust).
  - Playing rig: L1164, camera 1440,520, `<visible>Player.HasAudio</visible>`, rotatey on `bz_sway_go` / `bz_sway_pulse`. It held the covers, with a glare/dust/shadow copy inside each cover layer.
  - Because the playing rig was hidden while idle, its pulse started at the first play (Kodi starts a pulse when the control is first processed), so the two rigs were never in phase. Each held different glare art.
- **After (one rig, the old playing rig, camera 1440,520, always processed):**
  1. **Idle stack:** the old L1081 children (shadows, `!Player.HasAudio` art group with A/B slots, np-art, leaf hinge, frame, ATLook), unchanged inside.
  2. **Playing stack:** a new group carrying the old rig's `<visible>Player.HasAudio</visible>` and its Visible 150/1100 / WindowOpen / Hidden 450 fades. It holds the preload image and cover layers A and B with their glare copies removed. Cover B is never shown (no code sets `bz_cov_side=b` since 301).
  3. **ONE glare set:** cover A's glare wrapper (flip / `Container.Scrolling` fades), short-sway glares, glare A + left dust, and glare B + sway shadow + right dust. It sits inside the idle Jumbo zoom group (150 idle / 100 playing, the same anims as the idle art) and the LEAFTUNE fold gate (`![music + bz_hf_a + bz_hf_g]`). The `Player.HasAudio +` term is dropped from its inner gates.
  4. **Paused overlay:** unchanged, drawn last.
  - **Removed:** the idle rig (camera + `bz_big_*` rotatey) and the idle glare/dust group (448 IDLESEQ / 444 IDLELIT; the unreleased IDLEMATCH edit is superseded).
  - `bz_flip` still sets `bz_big_*`; no XML reads them now.
  - **Cast (`BezelAlbumCast`):** the two animated groups drop `Player.HasAudio +` from `<visible>` so their pulse starts with the rig. When idle, the existing latch 200 ms fade keeps them at 0.
  - **Stub anchor (`_sway_anchor`):** "album drawn" no longer needs `Player.HasAudio` (it uses the top gate `!HasAudio | !bz_navtune`).
- **Sync lint:** one rotatey lead-in and pulse, one cast set, one glare pulse pair (per copy).
- **Visible differences, on purpose:**
  - Idle now uses the playing glare (100% default, `glare2_br` at the right end, Tuner style and tint) plus the sway shadow.
  - Idle perspective centre is y520 (was 570).
  - Short sway and glare-off-while-scrolling apply to idle too.
  - Idle also sways under 1120 / viz (not normally visible).
- **Check:**
  - Idle album swings. Start a song: art crossfades and zooms down, with no jump, restart or dark gap in the swing, glare or dust. Stop: the same in reverse.
  - Leaf flip (locked): unchanged, glare out/in around the fold.
  - Album change while playing: crossfade.
  - Rail slide centre/home, Play Next / viz / 1121, stub casts in step.
- **Rollback:** restore `xml/Includes_Bezel.xml` and `scripts/bz_flip.py` from 5.33.452.

## 5.33.452 — GLARECONT (playing big album glare + lit dust unbroken on song start)
- **Cause:** in BezelMusicPlayingArt, the 4 long-sway glare groups (glare A + glare B, cover layers A and B, lit dust inside) carry a lead-in `Conditional fade 0→100 time 2700 delay 4700` on `String.IsEmpty(bz_sway_hold)` only.
  - It was built for the pre-415 sway, which restarted from flat on every play (glare dark through the 2.4 s hold + 5 s lead-in).
  - Since 415 SWAYCONT, `bz_sway_go` / `bz_sway_pulse` stay on, so at a song start the album resumes or starts its pulse at once. The glare lead-in, however, ran (first draw / 1122 reopen) and multiplied the pulse by 0 for 4.7 s, then faded it in: glare and dust "restarted" while the album kept swinging.
  - The colour-strip cast lead-in already had `+ String.IsEmpty(bz_sway_pulse)`.
- **Change:** the 4 lead-ins get `+ String.IsEmpty(Window(Home).Property(bz_sway_pulse))`.
  - While the pulse runs, they don't play. reversible=false, so when the pulse arrives at 7.4 s the lead-in (already at 100) just drops.
  - A real sway restart (`bz_sway_restart`: viz / playlist onload, hold → clock re-zeroed → pulse cleared) still plays the lead-in as before.
  - The pulse anims, shapes and the short sway are unchanged.
- **Check:** start a song from stopped, from the list, MM and FS. Glare A and the left dust are lit at the −13 hold and follow the swing with no dark gap. Next / Prev and album change: no glare dip. Stop, then play again: same.

## 5.33.451 — ALLCOUNT + L2PULL + NOWRAPGUARD
- **ALLCOUNT:** Kodi 21 `GUIBaseContainer::GetLabel(CONTAINER_NUM_ITEMS)` returns `size − 1` when item 0 is the parent folder. So `Container(60).NumItems` never counts `..`, but `ListItemAbsolute(n)` does index it.
  - 443's `bz_all2` assumed `..` was counted. For `[.., A1, A2]` (NumItems 2) and `[.., *All, A1, A2]` (NumItems 3) it returned false, so 2-album artists got no ALL row.
  - New rule: `NumItems > 2 | [NumItems == 2 + !bz_allhas]` (real rows = NumItems − stock *All ≥ 2).
  - Truth table checked:

    | List | Row |
    |---|---|
    | `[..,A1,A2]` | ✓ |
    | `[..,*All,A1,A2]` | ✓ |
    | `[*All,A1,A2]` | ✓ |
    | `[A1,A2]` | ✓ |
    | `[..,A1]` | ✗ |
    | `[..,*All,A1]` | ✗ |
    | `[A1]` | ✗ |

  - Other `NumItems` uses (6097 slide tables, `bz_alllong >14`, seasons/discs `>1`) were tuned on device with Kodi's real count and are not changed.
- **L2PULL** (Rob's screenshot, Daft Punk, 2 albums, no `..`):
  - The list started half a row below the small album's bottom edge, so ALL ALBUMS (6097, already at the right y ≈ 600) sat over the second album.
  - Cause: `bz_allpull60` (hidden stock *All at row 0, no `..`) slides −60 inside the cover-column 50% zoom (−30 on screen), but an L2 row is 150 in that space (75 on screen). The `..` pull right above it already uses −150.
  - Change in the View_60_BezelInfoList list: −60 stays for every other context; `bz_allpull60 + bz_covercol + bz_artistalbums` → −150.
  - The 6097 button tables are not changed (measured from the screenshot: the button top already sat where the last album ends after the fix).
  - **Not changed / to watch:** L2 with `..` *and* *All (`bz_allpull120`) totals −270 (−135 on screen) for two hidden slots of 75; that may leave a 15 px gap. It wasn't in the screenshot, so left as is (the 6097 comment says it was tuned flush).
- **NOWRAPGUARD** (`bz_flip.py` list-60 watcher):
  - Two branches assumed Kodi's native list wrap: (a) "last poll on the top row, now on the last row" = Up-wrap, then SetFocus ALL or `SetFocus(60,0,absolute)`; (b) "last poll on the last row, now row ≤ 1" = Down-wrap, then SetFocus ALL.
  - Both lists (music 1540, video 2945) have `onup` / `ondown` actions at both edges (ALL row or `bz_topedge` / `bz_bottomedge`, read by nothing), so Kodi never wraps them. The branches only fired on real moves: a fast Down to the end of a short list (≤ 4 rows, or the last 3 of a 7+ row list) jumped to the top ("navs to home"), and Up in a 2-row list jumped to ALL.
  - Both are now gated on `Skin.HasSetting(bz_wrapguard)` (off by default).
  - The hidden *All / `..` bounces and Back-to-ALL (`bz_allret`) are unchanged.
- **Check:**
  - Artists with 2, 3 and 15+ albums: ALL ALBUMS shows. The first album sits flush on the small album's bottom edge, and ALL ALBUMS sits right under the last album.
  - Hold Down to the end of short and long lists: focus stays on the last row, or goes to ALL / the bottom pill.
  - Up from the first row goes to ALL when shown, else stays.
  - TV seasons: same checks.

## 5.33.450 — VIZNPBAR (compact NP bar in Kodi FS viz)
- **Rob:** the NP bar under the centred big album showed on the FS fanart dialog (1121) but not in Kodi's fullscreen visualisation.
- **Cause (from structure, not device-verified):**
  - Both screens mount `BezelNPCompactBar` through `BezelFSPlayNext` (−480 → x660–1260, y892–1004).
  - In viz, though, that copy belongs to the **window** `visualisation`, and dialog **1122** (always open; draws the big album at centre via `bz_railc`) renders *above* windows, so its layers sat over the bar.
  - 1121 is a dialog opened after 1122, so its copy draws on top. That's why the bar was only seen on the fanart dialog.
- **Change:**
  - `Includes_Bezel.xml` `BezelFSPlayNext`: the NP bar group gate `!Window.IsActive(music)` becomes `!Window.IsActive(music) + !Window.IsActive(visualisation)`.
  - `Custom_1122_BigAlbum.xml`: a new group at the end of 6400 (above the album/cast layers, inside the `bz_rail != hide` gate) with `left −480` holding `BezelNPCompactBar`.
    - Visible on `Window.IsActive(visualisation) + bz_fsnp + $EXP[bz_railc] + Player.HasAudio`.
    - Fades: Visible 600 ms delay 480 (after the slide to centre), Hidden 300.
  - 1120 / 1121 are unchanged (gate false there).
- **Check:**
  - Kodi FS viz → album/Play Next mode (album at centre): artist, title, progress and time under the album. Back to fanart mode: the bar fades out.
  - 1121 and 1120 look as before.
  - No double or brighter text in viz.
- **Revert:** drop the 1122 group and the `+ !Window.IsActive(visualisation)` term.

## 5.33.449 — XBTPACK (optimization #2, texture bundle)
- **What:** `media/Textures.xbt` (XBTF v2, Kodi 21 format) holds every `.png` under `media/` that is ≤ 512×512: 1,128 files, 1,011 unique. It's 5.6 MB, against 5.2 MB of PNG and 220.8 MB decoded.
  - Kodi's texture manager checks the bundle before loose files (`CGUITextureManager::HasTexture`), so these load as pre-decoded BGRA plus a fast LZO unpack, with no PNG inflate/unfilter.
- **Why large images stay loose:** for an image with `background="true"`, `CGUITexture::AllocResources` first tries the bundle *synchronously* (`Load(name, checkBundleOnly=true)`) and only falls back to the async large-texture loader when the file isn't bundled. Packing the 410 images over 512×512 (1.16 GB decoded: dust sheets 2208², `mmd20_*` 1920×1080, maps, info art, backdrops) would move their load onto the render thread, a hitch risk, so they aren't packed.
- **Loose files:** all kept. The bundle wins for packed names. The one full-path reference (`special://skin/media/colors/black.png`, bz_wipe) and any future full-path use still find the file. Zip +5.6 MB.
- **Built with** `tools/xbt_pack.py` (repo; Python + Pillow + LZO 2.10 via ctypes). It mirrors Kodi's TexturePacker:
  - A8R8G8B8 = BGRA bytes, not premultiplied;
  - `XB_FMT_OPAQUE` when all alpha is 255;
  - `lzo1x_999` compression, stored raw when it doesn't shrink the frame;
  - md5 dedupe;
  - lower-case `/` paths relative to `media/` (`CTextureBundleXBT::Normalize`).
- **Verified:** `tools/xbt_verify.py` decodes every entry with `lzo1x_decompress_safe` (Kodi's call) and compares pixels, size and the opaque flag with a fresh decode of the PNG: 1,128 / 1,128 identical.
- **BUILD RULE (main agent):** after any change to a file in `media/`, re-run `python3 tools/xbt_pack.py <skin>/media <skin>/media/Textures.xbt <liblzo2.so>`. Otherwise Kodi keeps drawing the old bundled copy of a ≤ 512² image. Deleting `media/Textures.xbt` reverts to loose loading.
- **Expected gain:** faster first draw of skin chrome (window opens, Tuner, MM) and less CPU per texture load. It's modest on a fast PC and more on low-end boxes. No visual change.
- **Check:** start Kodi, open MM / Tuner / Music / Movies / TV / fullscreen music. Everything should look the same (no missing or black icons, bars, frames, glares). If anything is missing, kodi.log shows `Error loading texture`.

## 5.33.448 — IDLESEQ (idle big album glare + lit dust sequence)
- **Found:** the idle big album sway (`bz_big_go` 0→−13 in 5 s, then `bz_big_pulse` 12250 pulse: hold −13 for 2 s, −13→+13 over 10 s) is identical to the playing album's sway, but its glare/dust ran a different sequence:
  - **Mirrored:** at −13 the *flipped* glare (`BzATGlareTex` flipx, upper-right by default) and the *right* dust box. The playing album (433 LITSWAP, confirmed by Rob) shows the upper-left glare A + left box at −13 and glare B + right box at +13. 444 IDLELIT copied the idle glare's side mapping, so the new idle dust was mirrored too.
  - **Shape:** the idle glare pulses were one 12250 sine crossfade (100→0 / 0→100 over the whole half, both ~50% mid-swing). The playing album is dark mid-swing: A `100→100 12250` + `100→0 3450 delay 2000`, B `100→100 12250` + `0→100 3450 delay 8550`.
- **Change (Includes_Bezel line of the idle glare group, XML only):**
  - `flipx` moved from glare image 1 (A timing) to image 2 (B timing).
  - The two IDLELIT `BezelLitDust` include blocks swapped between the A and B groups; each box keeps its mask.
  - The 4 idle pulse anims now use the playing album's two-effect shape; conditions and reversibility are unchanged.
  - Lead-ins (`bz_big_go` 5000) are unchanged.
  - Sync lint: all idle family pulses share `bz_big_pulse` with 12250 / 3450 timing.
- **Check:** no music, Music list with the idle big album. At the left end (−13), the upper-left glare and left dust are lit; they go dark as it swings; at the right end (+13), the right side lights. Compare with the playing album.

## 5.33.447 — TICKCACHE reverted
- Rob on 446: very long pauses (5+ s) entering sections from the MM, which started with 446. `scripts/bz_flip.py` is restored byte-for-byte to 5.33.445. The 446 file is kept outside the skin (`tools/bz_flip.446_tickcache.py` in the repo) for study.
- **446 log for the record:**
  - One full stall, 17:10:33–17:10:53. No bz_flip thread made a Kodi call, so the 60 s perf line came 20 s late.
  - A TV in-place warm took 20.99 s (445: 0.35–1.45 s).
  - Real Kodi calls fell from ~3,000/s to ~1,400–2,650/s.
  - The log also shows Kodi failing to open 4 movie files over NFS for thumbnail extraction (Lincoln, Return of the Jedi 4K83, Stand by Me, The Wanderers), with one open taking 16 s during the stall. The 445 log has the same failures without pauses.
  - Exactly how the cache produced the stall isn't proven. Any future version of this optimization needs a device A/B before it ships.
- Rule for the next steps of optimization #1: one change per build, with Rob A/B'ing it against the previous build.

## 5.33.446 — TICKCACHE (REVERTED in 447) (optimization #1, step 2)
- **445 measurement** (Rob's kodi.log, 15 min, MM open most of the time, music played once):
  - bz_flip.py made **~2,950–3,000 Kodi calls/s** steady, about 65% Home `getProperty`, 22% `getCondVisibility`, 13% `getInfoLabel`. Writes and builtins were only a few per second.
  - Per thread (calls/s): `nav_menu` ~1,110 (≈55 per 50 ms tick), `poster_clock` ~520, `sway_clock` ~475, `ab_clock` ~265, `mm_autohide` ~190, `mm_warm` ~120, `vwarm` ~97. The rest are under 60 each. The top four are 80%.
  - No BEZEL errors or helper crashes in the log.
- **Change:** the 445 wrappers in `bz_flip.py` now also cache, per thread, for one tick:
  - Within one tick (from one `mon.waitForAbort` to the next), a repeated `home.getProperty(k)`, `xbmc.getCondVisibility(c)` or `xbmc.getInfoLabel(l)` returns the first answer.
  - The cache is dropped on `mon.waitForAbort`, `xbmc.sleep` and `xbmc.executebuiltin`.
  - The thread's own `setProperty` / `clearProperty` updates that key and drops its cached conditions and labels.
  - Other threads see a change on their next tick (≤50–100 ms, the same as their poll).
  - `mon` is wrapped (`_TCMon`).
  - Audit: no loop in bz_flip.py polls without a `mon.waitForAbort` (AST check; the only two waitless loops are local list/random loops), and there's only one Monitor.
- **Kill switch:** `Skin.SetBool(bz_nocache)` before the script starts gives 445 behaviour (counting only).
- **Perf log:** `hit=` now shows cache hits. `total` and the per-thread figures count real Kodi calls only. Compare with 445 to see the saving.
- **Mock-tested:** repeats are cached; own writes are seen at once; external changes are seen after a wait; SetFocus then HasFocus is fresh; threads are isolated.
- **Risk:** a code path that reads, expects another thread or the skin to change a value, and reads again *without* waiting would now see the old value until its next wait. None found.
- **Next (step 3):** with real call counts, cut `nav_menu` / `poster_clock` / `sway_clock` work that runs every tick while it isn't needed (e.g. Settings-family and Media-Sources window checks on every 50 ms tick).

## 5.33.445 — SYNCANCHOR + PERFCOUNT
- **SYNCANCHOR** (`bz_flip.py _sway_anchor`). The FS prev/next stub casts (`bz_castL/R`) are driven by Python, which has to copy the phase of the 1122 album pulse. Two gaps in 441:
  1. 1122 is a dialog with its own `<visible>` (it closes under screensaver, slideshow and fullscreen video). On reopen, Kodi restarts every animation in it, so the album, its colour-strip cast and the glares all restart together. The Python anchor kept the old start, so the stubs drifted after a screensaver. Now, when `Window.IsVisible(1122)` is false, the anchor is dropped and taken again the first time the album is drawn.
  2. "Album drawn" is now the album's full gate chain: HasAudio, no Tuner, `bz_rail != hide`, and `!bz_gridm | bz_np` (both expanded inline). Before, it was only HasAudio plus no Tuner, so a play started under the music grid anchored too early.
- **PERFCOUNT** (optimization #1, step 1, measuring only):
  - `xbmc.getCondVisibility/getInfoLabel/executebuiltin/executeJSONRPC` and Home `get/set/clearProperty` are wrapped with a per-thread counter.
  - `_bzstart` threads are named after their helper.
  - One `BEZEL perf` line per 60 s goes to kodi.log, for the first 15 min after start. Then it stops logging; the counting itself is a dict increment.
  - Purpose: pick which loops to merge, based on data. There are ~18 helper threads, many polling at 20 Hz, and every call takes Kodi's GUI lock.
- **Sync lint** (repo `tools/sync_lint.py`, not in the zip): groups every sway-family animation by condition and timing.
  - In 1122 today, all members use the same triggers.
  - Only one cosmetic difference: the album long pulse has `+ !Skin.HasSetting(bz_swayright)` and the cast/glare long pulses don't. Their parent groups already gate on it, so nothing to fix.
- **Check:** play music, let the screensaver start, wake, open Play Next / Viz. The stub casts brighten/dim with the album swing. Same check with the music grid on at play start. Then send kodi.log (`BEZEL perf` lines) after ~10 min of normal use.

## 5.33.444 — batch (Rob's answers 15:13 + bugs)
- **ALLFIX:** 443 shipped `$EXP[bz_all2]` with two unfilled `%s` placeholders (a Python format slip), so the ALL-row condition was broken. Now `String.IsEqual(Container(60).ListItemAbsolute(0).Label,..)`. Rob's rule: the ALL row shows only for TV shows with 2+ seasons, artists with 2+ albums, and albums with 2+ discs.
- **MMHIDEART / MMHIDEFAN:** Rob: "just poster and fanart", plus "Movies fanart has Music labels" when the menu is hidden.
  - New include `BezelSecDimArt` (BezelSecDim with `+ !$EXP[bz_mmhid]` on the mmdim fades), used on 1122 poster layer 6401 only. Album layer 6402 keeps `BezelSecDim`.
  - The MMHIDE stage group now starts with a `$EXP[bz_mmhid]` group: `BezelFanartLayer` 120,120 840×900 (black backing + MM lanes, not under a SecDim), fade 0→100 1500 on Visible and 100→0 250 on Hidden. It is an undimmed fanart drawn opaque over the dimmed section, so the Music window's labels underneath no longer show over Movies fanart.
- **RAILXFADE:** Rob: the big album stretches on the slide to centre and back home.
  - Kodi keeps each copy's sway camera at its layout spot (camera += origins, not animation transforms). The sliding copy is seen off-axis and looks stretched.
  - Both copies were at alpha 100 for the whole slide (the cut came at the end).
  - The 8 rail fades (`fade 100→0 time 0 delay T`) are now `time T sine`, so the copies crossfade over the slide. Reversal gives the reverse crossfade.
- **IDLELIT:** Rob: "lit dust at idle also". Two groups (`!Player.HasAudio`) inside the idle glare group copy the two idle glare pulses (`bz_big_go` 5000 lead-in / `bz_big_pulse` 12250 fade pair), each holding the playing album's `BezelLitDust` box (right box with the flipx glare, left box with the plain one; same params). `bz_adust_off` / `bz_dust_off` are still honoured inside the include.
- **VPICKLOAD:** Rob: quick nav plus Select on a row that isn't warm opened the warm section, then the chosen one.
  - `bz_cmd go` / `tomusic` now begin with: if `bz_nav=true` and the target window isn't active (a VWARM virtual row), go to `_bz_load_then_close` directly (the section is held by `bz_secload`, the list loads, `_vw_land` runs, then the MM closes).
  - The old pre-close transitions (`bz_tovideo` fade, m2v, `bz_tomusic`) are kept for picks with the menu closed.
- **M2VLAND** (built earlier in this version): Rob: entering the TV section with music playing didn't land on the warm item. The music-playing m2v and tomusic paths wait for the list and call `_vw_land()`.
- **L1 caption:** `BzMMetaSmall` artists value emptied (Rob: remove the ARTIST label above the artist name).
- **Tuner Back:** the 439 rows→rail Back change never applied (the onbacks weren't contiguous, so the replace missed). Back closes straight to where the Tuner was opened (the Power menu from Power), which is what Rob asked for. Hint text corrected to "BACK close". The 439 notes above are wrong on this point.

## 5.33.443 — ALLROW2 (Rob's ALL spec)
Rob's answers: 1 "14 row is not a rule", 2 always bottom, 3 ALL ALBUMS grouped, 4 ALL SEASONS list only, 5 hide on single season, 6 show a count.
- **No cap (1, 2):** `bz_allrow` drops `!NumItems>14`.
  - Lists of 14 or fewer keep 6097 / 6098 under the last row (those two buttons now carry the ≤14 test themselves, so their slide tables are untouched).
  - Longer lists: new bottom pills **6088** (music, sibling of the 86.67% list group in View_60_BezelInfoList) and **6089** (video, next to 6098) at screen 576,972 378×46, in the strip foot. They are always focusable (`$EXP[bz_alllong]`) and drawn only while `$EXP[bz_alllongshow]` (last row focused = `ListItemNoWrap(1)` empty, or a pill focused). The dtap hint hides while a pill shows.
  - Navigation: list / grouplist `ondown`/`onup` `Control.IsVisible(6088|6089)`. In `bz_flip` the wrap guard, Up-off-first and Back-from-All use `_ab` = the pill when it is visible.
- **Grouped (3):** `$EXP[bz_allgrp]` = `bz_m13 + FolderPath contains /-1/` (artist ALL song list).
  - The two parked MERGED13 75px layouts (`condition="false" height="75"`) now use `condition="$EXP[bz_allgrp]"`.
  - `bz_discbar` gained an OR branch: on `bz_allgrp`, each album's track 1 (and disc ≥2 of multi-disc albums) draws the header bar (`BzDiscBarLabel` m13 branch: ALBUM · YEAR / ALBUM · DISC n · YEAR).
  - `bz_cmd allrow` waits for the list to load (≤4 s) and runs `Container.SetSortMethod(12)` (SortByAlbum: album, then track; MERGED13 used the same call).
  - **Risk:** these layouts were last live at 5.33.272, before the strip moves (304) and LISTROW (436). They need a device look. To roll back, put back `condition="false"`.
- **List only (4):** ALL SEASONS is unchanged.
- **Hide single (5):** new `$EXP[bz_all2]` = 2+ real rows (`..` and Kodi *All not counted; uses `bz_allhas`). Replaces the old item-count clause, including the seasons `NumItems>1` clause that let a one-season show get ALL SEASONS.
- **Count (6):** `BzAllRowLabel` + `$INFO[Window(Home).Property(bz_allcnt),  ·  ,]`.
  - New `bz_flip` thread `allcnt` (0.4 s, only while an ALL row or pill is visible; one RPC per folder change): `VideoLibrary.GetEpisodes {tvshowid}` (from `?tvshowid=` or the last numeric path segment), `AudioLibrary.GetSongs {albumid}` (musicdb://albums/ID) or `{artistid}` (other musicdb, last numeric segment), using `limits.total`.
  - Gives N EPISODES / N SONGS. Exit cleanup clears it.
  - **Note:** on genre → artist paths the song count is the artist's whole library, not genre-filtered.

## 5.33.442 — ALLTOGGLE (BEZEL ALL SEASONS / ALL ALBUMS / ALL DISCS rows)
- **Finding 1:** the BEZEL settings toggles View All Seasons / View All Albums only drove Kodi `videolibrary` / `musiclibrary.showallitems` (`bz_cmd showall`). ALLHIDE always hides Kodi's stock *All row, and the BEZEL ALL rows 6097 / 6098 (`$EXP[bz_allrow]`) did not read the toggles, so switching Off changed nothing visible. **Change:** `bz_allrow` += `[[Container.Content(seasons) + Skin.HasSetting(bz_allseasons)] | [Window.IsActive(music) + !Container.Content(seasons) + Skin.HasSetting(bz_allalbums)]]`. Music covers ALL ALBUMS and ALL DISCS.
- **Finding 2:** artist albums (L2) hid `..` unconditionally (`!ListItem.IsParentFolder | !bz_artistalbums`, 8 layouts), but `bz_allpull120` only removes that slot when Kodi's *All is at index 1 (showallitems on). With View All Albums Off this left a blank, focusable top row. **Change:** that hide also needs `System.GetBool(musiclibrary.showallitems)` (the same rule 5.33.342 used for seasons). Off = `..` shows at the top.
- **Text:** both toggle descriptions now describe the BEZEL row.
- **Unchanged / open:** row placement and labels, Select → `<path>-1/` (`bz_cmd allrow`), Back → ALL row (`bz_allret`), wrap → ALL (`bz_flip`). Lists over 14 items still get no ALL row, because the row would sit below y1020. That needs a layout call from Rob (for example, pin the row in the last slot when the list is at its end).

## 5.33.441 — STUBPHASE (FS prev/next stub casts)
- **Cause:** `_bz_cast` (bz_castL/R → stub `pn_cast` opacity steps) assumed the big album pulse began at `t0 + 7.4 s`. Since 415 SWAYCONT `t0` is the Home-startup clock, but Kodi starts the 1122 album pulse only when its group is drawn (`Player.HasAudio`) with the condition true, normally the first play, then keeps wall-clock phase (hidden = frozen, condition not re-read). So the stubs were offset by `(first play − startup − 7.4) mod 24.5 s`.
- **Change:** new `_sway_anchor()` (called each `sway_clock` tick) mirrors that rule: while the album is drawn (`Player.HasAudio` + not Tuner), it records when the long-pulse condition (`!hold + bz_sway_pulse + !swayright`) or the short-pulse condition (`!hold + bz_sway_go + swayright`) turns true, and clears the anchor when it turns false. While not drawn, nothing changes. `_bz_cast` uses the anchor for the long and short branches; the lead-in branch and the opacity / step logic are unchanged.
- **Poster cast (colour strip):** audited. The animated cast image sits inside the poster sway group in BezelVPLPoster (1122, single mount since 367) with identical lead-in / pulse conditions (`bz_pswayon` / `bz_ppulse`) and counter-rotation, so I found no clock split in code. The only other poster cast (BezelXInfo) is retired. Needs Rob's on-screen description if it still drifts.

## 5.33.440 — CASTPHASE (big album cast shadow vs album sway)
- **Cause:** in `BezelAlbumCast` (1122) the three cast motion anims (Short pulse 5500, Long lead-in 3500/1200, Long pulse 12250) had `bz_audio_latch` in their conditions; the album sway anims they mirror (`!hold + go/pulse (+ swayright)`) do not. Since 415 SWAYCONT, `bz_sway_pulse` stays on across stop/play, so at play start the album group (visible on `Player.HasAudio`) resumed its running pulse while the cast saw the latch still false (bz_flip sets it ~0.15 s+ later), reset, and restarted from zero, out of step for the rest of the session.
- **Change:** removed `String.IsEqual(…bz_audio_latch),true) + ` from those 3 conditions only (now identical to the album's). The latch still hides the cast through its existing 200 ms fade gate. XML only.
- **Not changed:** fullscreen stub cast `bz_castL/R` (Python `_bz_cast` phase from t0). If Rob means that one, it needs its own anchor.

## 5.33.439 — TUNERRAIL (Tuner mockup B, approved)
- **Layout:** x120-570 rail list **7001** (BEZEL TUNER title; ALBUM / POSTER, POSTER, LIST, WARM 2.0.1, MAIN MENU, MUSIC, AMBIENT DUST, LOOK, FULLSCREEN MUSIC, SYSTEM, MAPS, ABOUT / VERSIONS, ALL, RESET SYSTEM; static row counts). Strip = section header (accent) + list 6970 (top 196, h 812). Right 1040-1800 = info art box 760x500 (every existing per-row info image + BezelArtworkPanel wrapped in an 83% zoom / -20,-150 slide), title + value, description, key hints. MAPS keeps its 1000,210 map.
- **Row filter:** inside 6970 content, `Skin.HasSetting(bz_topen_<head>)` → `String.IsEqual(Container(7001).ListItem.Property(id),<head>)` for the 13 heads. Head rows `<visible>false`. Sub-section bools (`bz_topen_al_glare` etc.) unchanged. The two ABOUT milestone rows with no `<visible>` (drawn in every state) got an ABOUT condition.
- **Nav:** entries (1118 Power, 1115 Music controls, 1130 ×2, `bz_tune resetui` cancel) `SetFocus(7001)`. Rail RIGHT/OK → `SetFocus(6970,0,absolute)`; rail BACK = the old 6970 close chain verbatim (Power / fsctrl / BEZEL / MM). 6970 BACK → rail (old chain kept behind `bz_topen_resetsys` for Reset System mode). 6970 LEFT on a `sub` row or id-less `btn` → rail (and no `bz_tune_dirty`); all per-id LEFT/RIGHT value handlers unchanged.
- **Deviation from the mockup (for Rob):** BACK from a row goes to the rail first (the mockup hint said BACK = close). Value rows use LEFT to change, so they need another way out. Option chips not built; the value shows as text.
- **Not changed:** every row's id / handlers / desc / info, `bz_tune_dirty` reload on close, BEZEL Settings card 6968.

## 5.33.438 — LEAFTUNE (idle Big Album leaf flip) + Spotlight removal
- **Look/timing unchanged** (LOCKED: 1400 ms × 2, shadows, frames, geometry).
- **Snap/hitch on scroll (main fix):** `idle_hinge()` used to set `bz_hf_a/b` ~0.2 s after a list 60 focus change. The opaque hinge stack (non-background textures) then covered the base idle album mid-way through its 0.6 s promote + 400 ms A/B dissolve, so the cover snapped instead of dissolving, and the new thumb loaded on the render thread (hitch while scrolling with the leaf on). Now the hinge arms only when `bz_m_idle_art` equals the cover and `_mi_guard()` has passed since the flip (MM-warm path unchanged).
- **Textures:** the 5 hinge images with `bz_hf_a/b` load `background="true"`, the same large-texture cache as the base idle slots, so arm and A:=B are instant.
- **Mid-fold focus change:** checked every 50 ms (was once per 1.4 s phase, so the old covers stayed up to 1.4 s); the fold aborts and clears.
- **Glare:** since 414 GLAREONE the glare group was hidden whenever `bz_hf_a` was set, i.e. the whole hold on any row with 2+ covers, popping on/off with focus. New Home `bz_hf_g`: set 0.5 s before ph1 (glare fades out 500 ms), cleared at landing (fades back 600 ms). Hold check is `HOLD − 0.5`, so the cadence is the same.
- **Grace:** 0.3 s before clearing on a one-frame `ok()` drop.
- **RPC album thumbs** unwrapped (`_vw_unwrap`) to the plain path, for texture reuse and dedupe against `ListItem.Art`.
- Mock-tested: no arm before the base settles; arm → glare out → ph1 → ph2 → A:=B; focus change clears within 0.1 s.
- **Known, not changed:** after a fold, the stack shows album N while the base shows the list cover. If the leaf stops (focus leaves list 60, MM opens), the base cover shows again.
- **Spotlight (437) removed:** 1122 overlay, `bz_mm.py` pick record, `bz_flip` trigger and cleanup keys, Tuner row + handlers + `BzATVal_spot`, `mm_spotlight.png`.

---

## Files changed (cumulative vs 423)
`addon.xml`, `changelog.txt`, `behaviors/mm-warm.md`, `behaviors/mm-autohide.md` (new), `media/bezel/info/mm_autohide.png`, `scripts/bz_flip.py`, `scripts/bz_cmd.py`, `scripts/bz_mm.py`, `scripts/bz_warmgate.py`, `scripts/bz_set.py`, `scripts/bz_dtap.py`, `scripts/bz_artist.py`, `scripts/bz_firstalbum.py`, `scripts/bz_tune.py`, `behaviors/dialog-confirm.md`, `xml/Includes.xml`, `xml/Includes_Bezel.xml`, `xml/Includes_Tuner.xml`, `xml/Includes_DialogSelect.xml`, `xml/MyFavourites.xml`, `xml/MyGames.xml`, `xml/MyPics.xml`, `xml/MyPlaylist.xml`, `xml/MyPrograms.xml`, `behaviors/leaf-flip.md`, `behaviors/skin-settings-tuner.md`, `xml/Custom_1118_PowerMenu.xml`, `xml/Custom_1115_MusicControls.xml`, `xml/Custom_1130_BzSettings.xml`, `behaviors/music-list.md`, `behaviors/tv-list.md`.

## New Home properties
`bz_vsec`, `bz_vsec_t`, `bz_vmus`, `bz_vart_fanart`, `bz_vart_poster`, `bz_vart_thumb`, `bz_vart_clear`, `bz_vart_logo`, `bz_vart_title`, `bz_vland`, `bz_vpick`, `bz_mmhide`, `bz_mmwake`, `bz_mmh_logo`, `bz_mmh_title`, `bz_mpkeep`, `bz_hf_g`, `bz_allcnt`.
**New include:** `BezelSecDimArt` (1122 poster).
**New skin settings:** `bz_at_mmhide` (string), `bz_vwarm_off` (bool, no UI).

## Suggested review / smoke list
1. **Startup:** splash timing unchanged; MM opens on the Tuner startup row; the startup warm under the splash still lands.
2. **With Music behind:** MUSIC → MOVIES → TV → MUSIC. No hitch, no bar flash, one dissolve album↔poster; art cycles on the UADVRAND timing.
3. **With Videos behind (after startup on TV):** TV → MOVIES (in-place, unchanged) → MUSIC (album dissolves in on artist art) → MOVIES (poster back with no empty frame).
4. **Select, Back and tap-outside on a virtual row:** the section opens on the item shown (titles, shows, artists pills). Other pills open as before.
5. **Music playing:** MMAUDIO album on every row; m2v / tomusic transitions unchanged.
6. **Auto-hide:** each step; the wake key doesn't Select, Back or change rows; Up from MUSIC with media playing returns to the strip; the Tuner open blocks hiding; Settings, Add-ons and Search rows show no logo or title.
7. **Mini-player Stop** → MUSIC row.
8. **Leaf flip (Tuner › ALBUM / POSTER › Leaf flip On):** scroll the Music list fast — covers dissolve, no snap/hitch; glare stays on during the hold and fades only around the turn; move focus mid-turn — old covers gone at once.
9. **Tuner rail:** open from Power, Music controls and BEZEL settings → lands on the rail; UP/DOWN previews each section; RIGHT/OK into rows; values change as before; BACK closes to where it came from (Power menu from Power); Reset System Yes/No; MAPS.
10. **Cast shadow:** play → stop (> 3 s) → play again, several times; the cast grows/shrinks exactly with the album swing each time (Long and Short sway).
11. **ALL rows:** BEZEL settings View All Seasons / Albums On: ALL SEASONS under seasons, ALL ALBUMS under artist albums, ALL DISCS under multi-disc; Off: no row, and artist albums show `..` at the top (no blank slot); Select / Back / wrap as before.
12. **ALL long lists / grouped / count:** an artist with 15+ albums and a show with 15+ seasons → Down off the last row shows the bottom ALL pill (hint hidden), OK opens All, Back returns to the pill; ALL ALBUMS list = album header bars, songs grouped by album in track order; one-season show = no ALL SEASONS; labels carry the count.
13. **Kill switch:** `Skin.SetBool(bz_vwarm_off)` gives the 425 behaviour.
