# CLAUDE CHANGELOG — skin.bezel2 5.33.424 → 5.33.444

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
