# MM warm (WARM 2.0.1) — LOCKED

> **Warm 2.0.1 (5.33.211):** feature version tracked like Bezel builds. 2.0.1 = Warm 2.0 locked enter/exit + hold last WARM art behind MM for other sections (Favourites/Pictures/Add-ons/Settings/Search/Media Sources). Music/Movies/TV unchanged.

**Object:** Main Menu warm underlay (`scripts/bz_flip.py` → `mm_warm`, `ab_clock`, `_ABLane`) + cold-start warm gate (`scripts/bz_warmgate.py`)  
**Where:** Under `$EXP[bz_navmenu]` (`String.IsEqual(Window(Home).Property(bz_nav),true)`, `Includes_Bezel.xml` line ~348), strip `6996` focused  
**Last updated:** 2026-11-02 · 5.33.309
**Poster slot family split (5.33.227):** the poster-slot live images (section twin and MM live twin) are each two controls — a Videos one (`$VAR[BezelPoster60V]`, `!Window.IsActive(music)`) and a Music one (`$VAR[BezelPoster60M]`, `Window.IsActive(music)`). Kodi image `fadetime` crossfades from whatever texture the control last held, so one shared control carried the last Music album into the next poster crossfade on a section switch. Each family now has its own texture memory; Music art never enters a poster control. The intended Music→video album fade-out is still only `bz_xalb` / the `bz_mart` Hidden fade.  
**Idle (5.33.217):** Background dim (mmdim) is gated off while `bz_mmidle=1` — art goes full opacity during MM idle fade; restored on wake (see mm-list.md).  
**Status:** LOCKED. Live since 5.33.203 (Rob approved Oct 31 2026). **Section enter/exit (mirror-enter) locked Oct 31 2026 evening** after Rob confirmed the black flash was fixed on 5.33.207. This file describes how things work now. It is not a changelog. Any change needs Rob's approval.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end and what stops flashes and races), and **Wiring** (property names, conditions, functions, timings and files).

---

## Locked summary (live 5.33.207)

**Simple:** These are the fixed numbers and switches for the whole warm system.

**How it works:** Two Python threads run inside `bz_flip.py`. They are started with `_bzstart(...)` and stay alive while `Home.bz_flip_running == 'true'`. `mm_warm` checks every 50 ms and loads the section you are parked on under the Main Menu. `ab_clock` also checks every 50 ms and feeds the MM-only A/B art lanes. `bz_warmgate.py` runs once at startup, from `Startup.xml`.

**Wiring:**
| Setting | Live value | Source |
|---|---|---|
| mm_warm poll | 50 ms (`mon.waitForAbort(0.05)`) | bz_flip.py `mm_warm` |
| Park delay | `park = clamp(0.2 × int(Skin.String(bz_at_mmwarm) or 1), 0.2, 2.0)` s. Default 0.2 s | `mm_warm` |
| Window-switch park | Needs at least `max(park, 0.5)` s parked when the target window is not already active. An in-place swap needs only `park` | `mm_warm` |
| Warm targets (`WARM`) | music → (`Music`, `musicdb://artists/`) · movies → (`Videos`, `videodb://movies/titles/`) · tv → (`Videos`, `videodb://tvshows/titles/`) | `mm_warm` |
| Music underlay guard | `Home.bz_music_underlay=1` is set whenever a music warm starts. Select goes back to `Home.bz_lastmusic` | `mm_warm` |
| Section swap | Fade-in only. `bz_arthold` holds the art, then `_arel` releases it once the new list has an item and family art: up to 45 × 20 ms ≈ 0.9 s, and after 30 tries (about 0.6 s) it stops waiting for art. No `bz_xfin`/`bz_xfade` dim-out | `_ahold`/`_arel` |
| Family split (BUG-010) | Music ↔ video: the poster lane is cleared straight away and only fanart is held. Exception: video → music keeps the poster lane so it can fade out (see the last section). Movies ↔ TV: poster and fanart are held (`bz_hold_poster` = `poster` / `tvshow.poster` only) | `_ahold` |
| A/B lanes | `fan`, `pos`, `clr`: settle 0.25 s → LOAD_WAIT 0.5 s → side flip → 1500 ms sine Visible/Hidden crossfade | `_ABLane`, `ab_clock` |
| `bz_ab_live` | Set 0.3 s after `bz_nav=='true'` is first seen. Cleared when MM closes and when `ab_clock` starts. Gates the **Visible** fade on the fan and pos A/B images only. The clr lane always fades | `ab_clock` |
| MM-open seed | While MM is closed and music/videos is active (and nothing is updating and no modal is open), every lane runs `seed()`. With 1107/1117 active, only `fan` is seeded | `ab_clock` |
| Lane not fed | Live MM twin image is shown (`fadetime` 3000) | Includes_Bezel |
| Backdrop cycle | `BDW = 10.0` s parked → new random image from `special://skin/extras/backdrop/` | `mm_warm` |
| Music playing | `$EXP[bz_mmmushide]` (any strip section with a Videos underlay: Movies, TV, Favourites/other held-WARM sections) hides the MM poster lane and shows `$VAR[BzWarmMusicArt]` as a square 600×600 framed album in the BezelVPLPoster slot (5.33.222; hidden in Music artists/albums/songs where BezelMusicPlayingArt draws; visible = `$EXP[bz_mmmushide]`; 5.33.218 removed `!String.IsEmpty($VAR[..])`, a boolean parse error that kept the slot dead outside Music): Visible 600 / Hidden 300 / fadetime 600. Re-latch is a 400 ms Conditional on `bz_mushref` | Includes_Bezel |
| Warm gate | `MIN=5.0` · `CAP=15.0` · `FADE=3.0` s. Each section warms a random 400-item `Files.GetDirectory` window | bz_warmgate.py |
| GBD | `BezelGlobalBackdrop` is hidden while `Home.bz_warm_gate` is set | Includes_Bezel |
| Tuner WARM 2.0.1 rows | `bz_at_warmsplash` (Startup splash, empty = On) · `bz_at_warmmusicposters` (Album art during music, empty = On) · `bz_at_abfade` (A/B fade length, **not wired**: XML is fixed at 1500 ms) | Includes_Tuner |
| Section-fade Tuner value | `bz_at_mmsecfade` is read into `_xf` (table `0,0,0.15,0.25,0.35,0.5,0.7,1.0`, default index 4 → 0.35). **Only logged.** No warm-swap fade uses it | `mm_warm` |
| Debug | `Skin.HasSetting(bz_debug_mm)` → `_dbgmm` verbose log lines `warm-start` / `warm-done` / `warm2 restore|cycle|randstart` | bz_flip.py |

### Startup random row (5.33.204 RANDSTART)
**Simple:** The first time you open each section, it starts on a random row instead of the top.

**5.33.218:** window-switch warm (Music/Movies/TV via ActivateWindow) now waits up to 4 s for `Container.FolderPath == path` + `!Container.IsUpdating` + NumItems>0 before `_restore` (load screen may hold longer — intended). Row 0 is a valid row (`r is None` check). `_snap` only saves a row for a section already seeded/restored this session, so an unseeded first pass no longer pins row 0. `_restore` sets `bz_warmrow`=path so the grid sync keeps the list item instead of resetting to item 0. **5.33.219 Music apply path:** when `_restore` runs for Music it also starts `_defer(row)`: a daemon thread (≤120 s) that re-issues `SetFocus(60,row,absolute)` the moment `Control.IsVisible(60)` and `!Container.IsUpdating`, with the same-frame `_bzstrip` bounce while MM is open (strip 6996 keeps focus). It stops when the row lands (`warm2 defer landed`), the folder changes, a Select is made (`bz_mmpick`), or — with MM closed — the user moves the list themselves. Note: `xbmcgui…getControl(60).selectItem()` on a skin container **crashes Kodi** — never use it. Movies/TV land the random row directly.

**How it works:** At cold start, `bz_warmgate.randstart()` runs as soon as the first section's list lands. In MM, `_restore` calls `_randrow()` when a section has no session row yet. Both keep focus on strip 6996.

**Wiring:**
- `lo = 1` if `Container(60).ListItemAbsolute(0).Label == '..'`, else 0. `hi = NumItems − 1 + lo`. If `ListItemAbsolute(lo).FolderPath` contains `/-1/` (the *All row), `lo += 1`. Pick `random.randint(lo, hi)`.
- `SetFocus(60,r,absolute)`. In the warm gate, if 6996 had focus and neither `bz_navtune` nor `bz_navbez` is set, it runs `SetFocus(6996)` in the same frame. In mm_warm, `_restore` stores `SS[sec].row/path` and then focuses (see Position map).

---

## Section enter / exit — LOCKED (5.33.207 mirror-enter)

Rob confirmed Oct 31 2026: the black flash on exit is fixed. **Do not change this method** without approval. It is shared by Music, Movies and TV and is the **standard for all main-menu sections**. There is no timed Hidden hold and no K40.

### Simple
- **Enter (MM → section):** the section's art is already on screen at full strength, and the menu's art fades away on top of it. You see art dissolve into art, never black.
- **Exit (section → MM):** while you are in the section, the menu's art slots are quietly filled with the same picture you are looking at. When the menu opens, it opens on that exact picture at full strength, so nothing flashes.

### How it works
1. **Two sets of images (twins).** Each art stage in `Includes_Bezel.xml` is drawn twice. **Section twins** have `<visible>!$EXP[bz_navmenu]</visible>`. **MM twins** have `<visible>$EXP[bz_navmenu] …</visible>`. MM twins come in two kinds: the live MM twin (used when the lane is not fed) and the A/B lane images (`bz_<p>_a` / `bz_<p>_b`).
2. **Enter.** Clearing `bz_nav` makes `$EXP[bz_navmenu]` false. Section twins have no Visible animation, so they appear at 100% in the same frame. The texture is already loaded because the warm underlay was showing that list. The MM A/B images lose visibility and play their **Hidden** fade (100→0, 1500 ms sine) over the section art.
3. **Exit seed.** While MM is closed, `ab_clock` calls `_ABLane.seed(target)` every 50 ms for each lane. That writes the art currently on screen into the lane's **front** side `bz_<p>_<side>` and forces `bz_<p>_on=true`. It clears `bz_<p>_empty` when there is art and sets it when there is none (pos and clr lanes only). The lane's internal `shown`/`seen` are set to the target and any `stage` is dropped. So when MM opens, the lane's `tick()` sees `target == shown` and does nothing. There is no re-stage and no flip.
4. **Exit open.** `bz_nav=true`, so the section twins hide straight away (they have no Hidden animation). The MM A/B front image becomes visible. Its Visible fade only runs when `!String.IsEmpty(Window(Home).Property(bz_ab_live))`, and `bz_ab_live` is still empty on the first frame. So the image appears at 100% in the same frame.
5. **Arming.** 0.3 s after `ab_clock` first sees `bz_nav=='true'`, it sets `bz_ab_live=1`. Side flips after that point crossfade over 1500 ms as normal. When MM closes, `bz_ab_live` is cleared, the lanes `stop()`, and seeding starts again.
6. **What prevents black:** (a) section twins never fade in; (b) the front lane already holds the on-screen texture before the open frame; (c) the first-open Visible fade is gated off; (d) the Hidden fade on MM images always plays, so enter is art over art.
7. **Cold enter** (section not warm, through `bz_cmd.py` `_bz_load_then_close`) is separate from the art lanes. `Home.bz_secload` holds the section parent group at alpha 0 until the list and the focused art are ready (hard cap 3 s). Then MM closes and `bz_secfade` fades the parent group from 0 to 100 over 400 ms (sine, out). This lives in `MyMusicNav.xml` and `MyVideoNav.xml` (parent group with `BezelSecDim`).

### Wiring

**ab_clock state machine** (`bz_flip.py`, 50 ms tick):
| State | Condition | Action |
|---|---|---|
| Start | thread start | `clearProperty('bz_ab_live')`, `armed=False` |
| MM open, first tick | `bz_nav=='true'` and not armed | `armed=True`, `open_t=now` |
| MM open, armed | `now − open_t ≥ 0.3` and `bz_ab_live` empty | `setProperty('bz_ab_live','1')` |
| MM open, idle | `!Container.IsUpdating + !System.HasModalDialog` | `ln.tick(rf(), now)` for fan, pos, clr |
| MM close | `bz_nav != 'true'` and armed | `armed=False`, clear `bz_ab_live`, `ln.stop()` for each lane |
| MM closed, music/videos | `!Container.IsUpdating + !System.HasModalDialog + [Window.IsActive(music) \| Window.IsActive(videos)]` | `ln.seed(rf(), now)` for all three lanes |
| MM closed, 1107/1117 | `!Container.IsUpdating + [Window.IsActive(1107) \| Window.IsActive(1117)]` (no modal check, because 1107 is a dialog) | `lanes[0]` (fan) `.seed(getInfoLabel('$VAR[BezelFanart]'))` only |

**Target functions** (what "on screen now" means):
- `_ab_fanart()`: first non-empty of `Control.GetLabel(9880)` (skipped when `Skin.HasSetting(bezel_norotate)`), `Container(60).ListItem.Art(fanart)`, `…Art(artist.fanart)`, `…Art(albumartist.fanart)`, `…Art(tvshow.fanart)`, `Window(Home).Property(script.grab.fanart.Global.FanArt)`. Movies only: falls back to `Home.bz_movfanart_hold`.
- `_ab_poster()`: returns `''` unless `Window.IsActive(videos)` (BUG-010: never Music). On a parent row (`..`) it uses `ListItemNoWrap(1).Art(poster|tvshow.poster)`. Otherwise it uses `ListItem.Art(poster)`, then `bz_movposter_hold` (movies content/path), then `ListItem.Art(tvshow.poster)`, then `bz_hold_poster` while `bz_arthold` is set. A basename starting with `Default` counts as empty.
- `_ab_clear()`: videos + tvshows/seasons/episodes content, `!Skin.HasSetting(bz_tvclear_off)`, not a parent row. First of `clearlogo`, `tvshow.clearlogo`, `clearart`, `tvshow.clearart`.

**`_ABLane.seed(target, now)`:** `side = bz_<p>_side or 'a'`. If there is a target: set `bz_<p>_<side>` when it differs, set `bz_<p>_on=true` when empty, and (if `empty_flag`) clear `bz_<p>_empty`. If there is no target and `empty_flag` is on: set `bz_<p>_empty=1`. Then `shown = seen = target`, `seen_t = now`, `stage = None`.

**Twin conditions (`Includes_Bezel.xml`):**
| Stage | Section twin | MM live twin (lane unfed) | MM A/B image a / b |
|---|---|---|---|
| Fanart (BezelFanartLayer ~L675–710) | `!$EXP[bz_navmenu]`. Fanart Pop: `!$EXP[bz_navmenu] + $EXP[bz_fpop]` | `$EXP[bz_navmenu] + String.IsEmpty(Home.bz_fan_on)`, fadetime 3000, `$VAR[BezelFanart]` | `$EXP[bz_navmenu] + !Empty(bz_fan_on) + bz_fan_side != b` (a) / `== b` (b). Visible 0→100 1500 sine **cond `!Empty(bz_ab_live)`**. Hidden 100→0 1500 sine. fadetime 0. LOOK fanart-opacity Conditionals kept |
| Album flip face A (~L1125–1150) | `!$EXP[bz_navmenu]` | `$EXP[bz_navmenu] + ![!Empty(bz_pos_on) + !Player.HasAudio + Empty(bz_cov_a) + Empty(bz_pos_empty)]`, `$VAR[BezelFlipA]`, fadetime 3000 | `$EXP[bz_navmenu] + !Empty(bz_pos_on) + !Player.HasAudio + Empty(bz_cov_a) + Empty(bz_pos_empty) + side a/b`. Same gated Visible and plain Hidden 1500. 1140,220 600×600, `art_mask` |
| Album flip face B (~L1196–1220) | `!$EXP[bz_navmenu]` | as above with `bz_cov_b` | as above with `bz_cov_b` |
| MM poster slot (~L2549–2570) | section poster twins: `!$EXP[bz_navmenu]` | `$EXP[bz_navmenu] + Empty(bz_pos_on) + !$EXP[bz_mmmushide]`, `$VAR[BezelPoster60]`, fadetime 3000 | `$EXP[bz_navmenu] + !$EXP[bz_mmmushide] + !Empty(bz_pos_on) + Empty(bz_pos_empty) + side`. Gated Visible 1500, Hidden 1500, `bz_mushref` 400 ms Conditional |
| TV clear header (~L2405–2414) | `!$EXP[bz_navmenu] + [has clear art] + !bz_tvclear_off` | `$EXP[bz_navmenu] + Empty(bz_clr_on) + [has clear art]` | `$EXP[bz_navmenu] + !Empty(bz_clr_on) + Empty(bz_clr_empty) + side`. Visible/Hidden 1500 **not** gated by `bz_ab_live` |

`bz_ab_live` appears 8 times in XML: fan a/b, face A a/b, face B a/b, poster slot a/b.

**Exit / open sequence (frame order):**
1. MM is closed. Every 50 ms the front side holds the current art and `bz_<p>_on=true`.
2. `bz_nav=true` → `$EXP[bz_navmenu]` true. Section twins drop to 0 (no anim). MM front A/B shows at 100 (Visible fade gated off). The back side stays hidden.
3. At t ≥ 0.3 s, `bz_ab_live=1`. A target change after that settles 0.25 s, is staged to the back side, waits 0.5 s, flips `bz_<p>_side`, and crossfades over 1500 ms.

### Standard for ALL main-menu sections (Rob, Oct 31 2026)
**Simple:** Every strip-6996 section that has background art uses mirror-enter. Sections without art have nothing to hand off.

**How it works:** Music, Movies, TV and Recently Played use MyMusicNav/MyVideoNav, so the closed-MM music/videos seed covers all three lanes. Search (1107, a dialog) and Media Sources (1117) only draw `BezelFanartLayer`, so only the fan lane is seeded, from `$VAR[BezelFanart]`. Without that seed, the MM would fade up the unfed live twin (fadetime 3000) from black.

**Wiring:**
| Section (6996 `sec`) | Opens | Art stage | Seeding |
|---|---|---|---|
| MUSIC `music` | MyMusicNav (`bz_mm.py` tomusic) | BezelFanartLayer + album faces A/B | fan + pos + clr seed() (pos/clr return '' in music → `bz_pos_empty`/`bz_clr_empty`=1) |
| MOVIES `movies` | MyVideoNav | BezelFanartLayer + poster | all lanes |
| TV SHOWS `tv` | MyVideoNav | BezelFanartLayer + poster + clear | all lanes |
| RECENTLY PLAYED `recent` | MyMusicNav `musicdb://recentlyplayedalbums/` | same as Music | music window seed |
| SEARCH `search` | Custom_1107_SearchDialog | BezelFanartLayer | none with WARM HOLD on (last WARM kept); fan seed from `$VAR[BezelFanart]` only when `bz_at_warmhold=Off` |
| MEDIA SOURCES `mediasources` | Custom_1117 (BezelStdFrame → BezelFanartLayer) | fanart | as Search |
| FAVOURITES `fav` / PICTURES `pictures` / ADD-ONS `addons` / SETTINGS `settings` | MyFavourites / MyPics / AddonBrowser / Settings | `BezelWarmHold` (MM-only fan lane) | none — draws last WARM lane |
| POWER `power` | Custom_1118 over the open MM (`bz_nav` kept) | MM art stays | N/A: MM never closes |

Shield smoke test for 1107/1117 is still pending.

### WARM HOLD — non-Music/Movies/TV sections (5.33.211, Rob Oct 31 2026)
**Simple:** Leave Favourites, Pictures, Add-ons, Settings, Search or Media Sources for the Main menu and the menu shows the last Music/Movies/TV WARM art, not a plain/cleared background. Unless Rob says otherwise per section, this is the rule for every non-M/M/TV section. Music, Movies and TV mirror-enter above is unchanged.

**How it works:** The fan A/B lane already keeps its last shown art when MM closes (`stop()` keeps `shown`; nothing seeds it outside music/videos). `BezelWarmHold` draws that lane under the open MM in the four windows that had no art stage. While MM is open over any of the six hold windows, `ab_clock` skips `tick()` so the lane does not re-target to that window's own art; once you park on Music/Movies/TV, `mm_warm` swaps the window and ticks resume normally (A/B 0.25/0.5/1500 unchanged). Search/Media Sources skip the old .207 fan seed, so their MM twins also show last WARM. Cold start with nothing warmed (`bz_fan_on` empty): hold draws nothing → plain background as before.

**Wiring:**
| Piece | Value |
|---|---|
| Expression | `bz_warmhold` = `$EXP[bz_navmenu] + !String.IsEqual(Skin.String(bz_at_warmhold),Off) + !String.IsEmpty(Home.bz_fan_on)` |
| Include | `BezelWarmHold` (Includes_Bezel, before BezelFanartLayer): group visible `$EXP[bz_warmhold]` → `BezelFanartLayer` 120,120 840×900 |
| Call sites | MyFavourites / MyPics / AddonBrowser after `DefaultBackground`; Settings after `BezelBlack` — all inside the `BezelSecDim` parent group (Global Dim applies) |
| Python | `bz_flip.py`: `_WHWIN` = favouritesbrowser · pictures · addonbrowser · settings · 1107 · 1117; `_whold()` = `Skin.String(bz_at_warmhold) != 'Off'`. MM open + `_whold()` + `_WHWIN` → no lane tick. MM closed 1107/1117 seed runs only when `not _whold()` |
| Kill switch | Tuner WARM 2.0.1 › **Hold last art (other sections)** (`id warmhold`, `bz_at_warmhold` On/Off, default On, info `mm_warm_hold.png`). Off = exact 5.33.210 behaviour |
| Only fan lane | Poster/clear lanes are not drawn in hold windows |

### Not this method
- Timed Hidden hold or AlarmClock delay on section art: rejected.
- K40 / t4892 open-anim gates: banned.
- Changing the in-MM A/B settle (0.25 s), LOAD_WAIT (0.5 s) or 1500 ms crossfade: not allowed.

---

## Warm park

**Simple:** Rest on Music, Movies or TV in the menu for a moment, and that section quietly loads behind the menu, so opening it is instant.

**How it works:** Each tick, `mm_warm` reads the focused strip row. When you move to a new row, it records `last=[sec, t]` and waits. Once you have been parked for `park` seconds (or 0.5 s if the window has to change), it either updates the list in place (same window) or runs `ActivateWindow` for the new one. All the while it holds focus on strip 6996 and keeps `bz_nav=true`, so the menu never closes.

**Wiring:**
| Gate (skip tick) | Condition |
|---|---|
| Not open / not on strip | `bz_nav != 'true'` or `!Control.HasFocus(6996)` → reset `last`/`done` |
| Pick made | `bz_mmpick` set → reset and skip (t5030). `_pk()` latches the pick for the rest of the warm |
| Busy | `bz_mmstart`, `bz_secload`, `bz_navsub`, `bz_navset`, `bz_navtune`, or `Window.IsActive(1113)|(1112)`, `System.HasModalDialog`, `Player.HasVideo + Window.IsActive(fullscreenvideo)` |
| List loading | `Container.IsUpdating` → skip (FREEZE t3461) |
| Already warm | First tick after open: `done=sec` when the underlay already matches (music = artists root only, BUG-016. movies = movies/sets content or `videodb://movies/` path. tv = tvshows/seasons/episodes) |
| No-op | target window active and `Container.FolderPath == path` |

**In-place path** (window already active): set `bz_mmwarm=true` and `bz_navroot=path`, clear `bz_xfin`/`bz_xfade`, run `Container.Update(path,replace)`. Loop up to 40 × 25 ms re-asserting `bz_nav=true`, tracking `bz_mmlive` from `Container(6996).Position` and calling `_bzstrip` if focus slips. Exit early after 12 tries once 6996 is focused and the list is not updating. If the path did not land, retry once (another 40 × 25 ms). Then `_restore`. `finally`: `_arel()`, clear `bz_mmwarm` and `bz_xfade`.  
**Window-switch path:** set `bz_mmpos = bz_mmlive or pos or '0'` (the new window's onload restores this strip row; FLASH t3430), `bz_mmwarm=true`, `bz_navroot`, then `ActivateWindow(win,path)`. Run `_hold()` up to 80 times (stop after ≥4 once the window is active), each pass setting `bz_nav`, `bz_mmpos` and `bz_mmlive` and re-focusing the strip. Then `Container.Update` if the path differs, up to 20 × 50 ms of focus confirmation, and `_restore`. `finally`: 15 × 20 ms `_hold`, `_arel()`, clear `bz_mmwarm`, `bz_mmpos`, `bz_xfade`.  
**Music last-browse tracker** (runs every tick while MM is closed, music is active and not updating): if the path is artists root and `bz_music_underlay` is set, it is ignored. Otherwise a real `musicdb://` / `library://music/` path (not root, not recentlyplayed) clears `bz_music_underlay` and sets `bz_lastmusic`.

---

## Session store

**Simple:** While the menu is open, it remembers your row and backdrop for each section. Closing the menu forgets them.

**How it works:** The store is a Python dict `SS` held in memory inside `mm_warm`. It is never written to Skin.String. It is cleared on any tick where `bz_nav` is empty.

**Wiring:**
| Key | Fields |
|---|---|
| `music` · `movies` · `tv` | `row` (0-based absolute for `SetFocus(60,N,absolute)`), `path` (`Container.FolderPath`), `backdrop` (`Home.bz_backdrop`), `timer_on` (bool), `parked_since` (epoch s) |

Clear: `if not home.getProperty('bz_nav') and SS: SS.clear()`.

## (1) Position map

**Simple:** Come back to a section and you land on the same row you left.

**How it works:** Before every swap, `_snap` saves the leaving section's row, path and backdrop. After the new list settles, `_restore` focuses the saved row on list 60 and then bounces focus straight back to the strip in the same frame, so the menu keeps focus.

**Wiring:**
- `_snap(s2)` runs on `done[0]` if it is in WARM, otherwise on the first WARM key whose `_SECM` condition is true. It sets `timer_on=False`. If `_SECM[s2]` holds and the list is not updating: `row = max(0, Container(60).CurrentItem − (0 if absolute(0) is '..' else 1))`, `path = Container.FolderPath`. It always stores `backdrop` when one is set.
- `_restore(s2, p2, spos)`: if there is no row, no pick, the path matches and the list is not updating → `_randrow()` seeds `row/path`. It aborts when `not r` (row 0 or None), `_pk()`, the stored path ≠ `p2`, the current path ≠ `p2`, or the list is updating. Otherwise `SetFocus(60,r,absolute)` and then `_bzstrip(home, bz_mmlive or spos)` (back to 6996).
- Movies and TV share the Videos window, so their lists are not kept alive and the row always comes from `SS`. Music needs both path and row to match. Row 0 never restores.

## (2) Backdrop cache

**Simple:** Each section keeps its own backdrop, so going back fades to the same picture instead of a new random one.

**How it works:** Before the swap, the cached image is pushed into `Home.bz_backdrop`. The window onloads only pick a random image when `bz_backdrop` is empty, so the cached image wins.

**Wiring:** `if SS[sec].backdrop: home.setProperty('bz_backdrop', SS[sec]['backdrop'])` runs right after `done[0]=sec`, before `_ahold`. `MyMusicNav`/`MyVideoNav` onload pick only when empty (5.33.142). With no cache, the normal first pick runs and is stored on the next `_snap` or timer start.

## (3) Gated backdrop cycle

**Simple:** Stay parked on a warm section for 10 seconds and the backdrop changes to a new random picture.

**How it works:** The timer only runs when the parked section is already warm. Scrolling away freezes it. Coming back restarts the 10 s count.

**Wiring:**
| Step | Code |
|---|---|
| Run condition | `sec in WARM and sec == done[0] and not bz_mmwarm` (all the open/strip/busy gates above apply) |
| Start | `timer_on` false → `timer_on=True`, `parked_since=now`, `backdrop=bz_backdrop` |
| Fire | `now − parked_since ≥ BDW (10.0)` and `!Container.IsUpdating` → `_bdpick()`, `parked_since=now`. If it returns a path: set `bz_backdrop` and update `SS.backdrop` |
| `_bdpick()` | `xbmcvfs.listdir('special://skin/extras/backdrop/')` files ending png/jpg/jpeg/webp/gif. Returns None when there are fewer than 2 files or `Skin.String(bz_bdimg)` (fixed Tuner image) is set. Otherwise a random choice that is not the current image |
| Scroll away | row change → leaving `SS[last].timer_on=False` and backdrop snapshot |

## Rules
- Strip `6996` always owns focus under MM. List 60 is only used for the one-frame restore.
- No K40 open-anim gates.

---

## Section fade

**Simple:** Changing sections in the menu never dims to black. The old art stays until the new art is ready, then the new art fades in.

**How it works:** Both swap paths clear `bz_xfin` and `bz_xfade` before swapping, so the `BezelSecDim` parent zero→100 fade never arms. `_ahold` sets `bz_arthold` (`_ab_poster` falls back to `bz_hold_poster` while it is set). `_arel` waits for the new item and its family art, then clears `bz_xfade`, `bz_xfin` and `bz_arthold` together.

**Wiring:** `_arel` loop: up to 45 × 20 ms. It breaks when `Container(60).ListItem.Label` is non-empty, the list is not updating, and (i ≥ 30 or any family art is set). Music family art = `ListItem.Art(thumb|icon)`. Video family art = `Art(poster|tvshow.poster)`. `_ahold` also sets `bz_hold_fanart` = first of `Control.GetLabel(9880)`, `ListItem.Art(fanart)`, `script.grab.fanart.TV.FanArt`. `bz_at_mmsecfade` is read but unused (logged only).

---

## MM-only A/B preload

**Simple:** Menu art never pops. The next image loads hidden, then crossfades over the current one.

**How it works:** Each lane has two image slots, a and b. The new target has to stay the same for 0.25 s (so scrolling does not churn), is written into the hidden slot, gets a fixed 0.5 s to load (Kodi gives Python no texture-ready signal), and then the side flips. The visible image's Hidden fade and the new image's Visible fade make a 1500 ms crossfade. The first art goes straight onto the front slot.

**Wiring:**
- `_ABLane(p, settle=0.25, load_wait=0.5, empty_flag)` fields: `seen`, `seen_t`, `shown`, `stage`, `stage_t`. Lanes: `fan` (empty_flag False), `pos` (True), `clr` (True).
- `tick(target, now)`: (1) a changed target resets `seen_t`. (2) If staged and `now − stage_t ≥ load_wait`: flip `bz_<p>_side` a↔b, `shown=stage`, return. (3) Return if `now − seen_t < settle` or `target == shown`. (4) Empty target: when `empty_flag`, set `bz_<p>_empty=1`, `shown=''`. (5) When `empty_flag`, clear `bz_<p>_empty`. (6) If `bz_<p>_on` is empty or there is no `shown`: write the front side and set `bz_<p>_on=true` (no flip). (7) Otherwise write the back side and `stage=target`, `stage_t=now`.
- `stop()` (MM close): if something was staged, reset the back side to `shown`. `stage=seen=None`. Last shown art and `bz_<p>_on` are kept. Nothing is cleared.
- Gates: ticks only run while `bz_nav=='true'` and `!Container.IsUpdating + !System.HasModalDialog`.
- Properties: `bz_fan_a/b/side/on` · `bz_pos_a/b/side/on/empty` · `bz_clr_a/b/side/on/empty`.
- Album faces reuse the `pos` lane only when `!Player.HasAudio` and `bz_cov_<face>` is empty and `bz_pos_empty` is empty. A playing cover (`bz_cov_a/b` flip) always wins. In Music, `_ab_poster` returns '', so `bz_pos_empty=1` and the face live twin (`BezelFlipA/B`) shows.
- Not touched: section (`!bz_navmenu`) twins, list rows and grids, in-section art.

---

## Music playing under MM (mushide)

**Simple:** When music is playing and you open the menu, the movie/TV poster is replaced by the album art of the song that is playing.

**How it works:** A single expression hides every MM poster-slot image (live twin and A/B) and shows one album-art image in the same rect. The Tuner row turns this off. When the toggle changes, `bz_mushref` re-latches the images with a short fade without restarting the sway.

**Wiring:**
- `<expression name="bz_mmmushide">Player.HasAudio + !Player.HasVideo + $EXP[bz_navmenu] + !String.IsEqual(Skin.String(bz_at_warmmusicposters),Off)</expression>`
- Hidden while true: MM poster live twin (`$VAR[BezelPoster60]`) and pos A/B (`!$EXP[bz_mmmushide]` in their visible). In BezelVPLPoster the gate also covers cast shadow (animated and static), blur/frame, LOOK, glare and lit dust. The fanart lane is never gated. The music album flip group is not affected (playing cover already wins).
- Album image (5.33.222): square Music-style album, not poster aspect. `<visible>$EXP[bz_mmmushide] + !(Music/MusicPlaylist window with artists/albums/songs content)</visible>` — in Music content the real Music sway album (BezelMusicPlayingArt) is the only album; this slot never doubles it. Rect 990, 270, 600 × 600 (centred on the poster sway pivot 1290,570, rides the poster sway), aspect `scale`, `art_mask` diffuse, plus a `bz_frame_soft` 602×602 frame with the same gate, fadetime 600, Visible 0→100 600 ms sine, Hidden 100→0 300 ms sine, plus Conditional 0→100 400 ms (`reversible=false`) on `!Empty(Home.bz_mushref)`.
- `BzWarmMusicArt`: `Player.Art(thumb)` > `Player.Art(album.thumb)` > `MusicPlayer.Cover` > `Player.Icon`, else empty (5.33.276: no `DefaultAlbumCover.png` placeholder).
- Tuner row "Album art during music" (`Includes_Tuner.xml`, `id=warmmusicposters`): Left/Right set `Skin.String(bz_at_warmmusicposters)` to `Off` or On/empty, and set `bz_mushref` (AlarmClock clears it after 1 s).
- Known limitation: switching it Off while music is already playing waits for the next A/B refresh. Setting it before playback works straight away.
- `bz_at_abfade` slider exists but is not wired. Fades are fixed at 1500 ms.

---

## Warm gate — cold-start splash (MIN 5 s / CAP 15 s / FADE 3 s)

**Simple:** At startup you see a black Bezel logo screen. Behind it the menu and sections build and the artwork loads. After at least 5 seconds (never more than 15) it fades out over 3 seconds, so you never see a half-built screen.

**How it works:** The splash is a non-modal overlay group (`BezelWarmGateOverlay`) drawn last on Startup, Music and Videos, controlled by `Home.bz_warm_gate`. Because nothing modal is open, `ReplaceWindow` to the startup section succeeds and builds underneath. The script waits for that section's list to land, focuses a random row, then warms artwork for the three sections on a background thread. Dismissing clears the property, which starts the 3 s Hidden fade, and then sets `bz_splash_done`. A watchdog thread forces dismissal at CAP. Dialog 1113 is never opened (as a modal it blocked the underlay: 5.33.196–198 blank screen).

**Wiring:**
- **Startup.xml onload order:** (1) `SetProperty(bz_warm_gate,1,home)` when `!String.IsEqual(Skin.String(bz_at_warmsplash),Off)`. (2) `ClearProperty(bz_splash_done,home)`. (3) `RunScript(special://skin/scripts/bz_warmgate.py)`. (4) `ReplaceWindow($INFO[System.StartupWindow])`. Controls: `<include>BezelWarmGateOverlay</include>`. The same include sits last in `MyMusicNav.xml` (~L117) and `MyVideoNav.xml` (~L124).
- **`BezelWarmGateOverlay`:** group `<visible>!String.IsEmpty(Window(Home).Property(bz_warm_gate)) + !String.IsEqual(Skin.String(bz_at_warmsplash),Off)</visible>`, Hidden fade 100→0 **3000 ms** sine, contains `BezelWarmGate`.
- **`BezelWarmGate`:** 1920×1080 black (`colors/white.png` diffuse FF000000). 600×600 group at 660,240 with multiimage `bezel/logoglow` (100 ms/frame, loop) and `bezel/logo.png` 256×256 at 172,172 pulsing 100↔80 (1400 ms each way). Label `BEZEL $INFO[System.AddonVersion(skin.bezel2)]` at top 850 (font bz_mm28, WindowOpen fade 900 ms after a 700 ms delay). Credit "designed by Robert Politano" + `bezel/us_flag.png` at top 1030 (80% white).
- **Script (`bz_warmgate.py`):**
  1. Re-entry guard `bz_warmgate_running`, then set it. `t0=now`. `vis = Skin.String(bz_at_warmsplash) != 'Off'`. Off → clear `bz_warm_gate`. On → make sure it is `1`.
  2. Clear `bz_warm_ready_music/_movies/_tv`. First section = `['music','movies','tv'][clamp(int(Skin.String(bz_at_mmdef) or 3),1,3)−1]` (default **tv**).
  3. Watchdog thread: polls every 0.1 s until `t0+CAP`, then if not done: `hold_until(t0,MIN)` → `dismiss(vis)`.
  4. Land: up to CAP, every 50 ms check `LAND[first]`: music `Window.IsActive(music) + !Container(60).IsUpdating + NumItems>0`. movies: videos + movies|sets content + same. tv: videos + tvshows + same. On land → `randstart()`.
  5. Art warm thread: `warm(first)` then the other two. `warm(sec)`: probe `Files.GetDirectory` (`limits 0–1`) for `total`. If total > 400, `start = randint(0, total−400)`, else `randint(0, total−1)`. Then GetDirectory `{start, start+400}` with `properties ['thumbnail','art']`. Always sets `bz_warm_ready_<sec>=1` (success or fail). Paths: `musicdb://artists/` (music), `videodb://movies/titles/`, `videodb://tvshows/titles/` (video). The main thread waits until all three are ready or CAP.
  6. `finally`: `hold_until(t0, MIN)` → `dismiss(vis)`. Then it lets late warms finish quietly up to CAP.
  7. `dismiss(vis)` (under a lock, no-op if `bz_splash_done=='1'`): clear `bz_warm_gate` (fade starts). If 1113 is visible, `Dialog.Close(1113,true)` (legacy safety). If vis, wait `FADE` 3.0 s. Then set `bz_splash_done=1` (releases `bz_cmd.py start`) and clear `bz_warmgate_running`.
- **Other actors:** `bz_precache.py` stays idle while `bz_warm_gate` is set. `bz_flip.py` still treats a visible 1113 as busy (harmless). Keys reach the underlay while the overlay is up.
- **GBD flash fix:** `BezelGlobalBackdrop` (nested in `BezelBlack` on Home/Music/Videos) group visible = `!String.IsEqual(Skin.String(bz_at_gbdsty),off) + String.IsEmpty(Window(Home).Property(bz_warm_gate))`. `BezelBlack` solid black still paints under the splash, and the glow returns under the 3 s fade.
- `xml/Custom_1113_WarmGate.xml` is kept only so id 1113 stays reserved. It is never opened.

### Tuner toggle: Startup splash
**Simple:** Turns the splash screen on or off. Artwork warming always runs.

**How it works:** Off skips the property and the overlay. The script still lands, warms and dismisses, without the visual fade wait.

**Wiring:** `Skin.String(bz_at_warmsplash)` `On`/`Off`, empty = On. With Off: Startup.xml does not set `bz_warm_gate`, the overlay's visible also fails on the Off string, and the script clears `bz_warm_gate`. `dismiss(False)` skips the 3 s wait. `bz_splash_done=1` is still set only after `hold_until(t0, MIN)`, so it comes at ≥5 s once ready, or at CAP 15 s.

---

## Music ↔ Movies/TV artwork fade (live tree, after 5.33.203 — not yet zipped)

**Simple:** Moving between Music and Movies/TV in the menu, the album and the poster crossfade (old fades out while new fades in) and never leave the wrong art behind. Movies ↔ TV still holds the poster as before.

**How it works:**
- **Video → Music:** `_ahold` keeps the poster A/B textures and `bz_pos_on`, clears `bz_hold_poster`, sets `bz_arthold`, and returns early, so the poster lane is not cleared. `_arel` (once the new list has an item) calls `_xfade_out(True)`. That clears `bz_pos_on` and `bz_hold_poster`, so the poster plays its 1500 ms Hidden fade while the Music album appears (texture fadetime 3000). After 1.7 s, if `bz_pos_on` is still empty, `bz_pos_a/b/side/empty` are cleared (BUG-010 guard: no video poster stays on Music).
- **Music → Video:** `_ahold` saves the outgoing album (`ListItem.Art(thumb)`, otherwise `ListItem.Icon`, skipping `Default*`) as `bz_xalb`, sets `bz_xalb_on=1`, then clears the poster lane (`bz_hold_poster`, `bz_pos_a/b/on/side/empty`) and sets `bz_arthold` (fanart-only hold). In Videos, the held-album image sits under the poster A/B lane. `_arel` → `_xfade_out(False)` clears `bz_xalb_on`, so the album fades out over 1500 ms while the new poster lane fills (first art goes straight to the front side). After 1.7 s, `bz_xalb` is cleared if `bz_xalb_on` is still empty.
- **Movies ↔ TV:** `bz_hold_poster` = `poster`/`tvshow.poster` only (never Icon/thumb), plus `bz_arthold`.

**Wiring:**
- Code: `bz_flip.py` `mm_warm` inner `_clear_poster_lane` / `_xfade_out(enter_music)` / `_ahold` / `_arel`. `_arel` calls `_xfade_out` when `enter_music or bz_xalb_on`. The 1.7 s cleanup runs on a daemon thread (`_late`).
- XML held album (`Includes_Bezel.xml` ~L2549, placed before the MM poster slot): `<visible>$EXP[bz_navmenu] + Window.IsActive(videos) + !String.IsEmpty(Window(Home).Property(bz_xalb_on)) + !String.IsEmpty(Window(Home).Property(bz_xalb))</visible>`, Hidden 100→0 1500 ms sine, no Visible animation, rect `bz_art_x`/`bz_top` 600×`bz_h`, `art_mask`, texture `$INFO[Window(Home).Property(bz_xalb)]`.
- Does not use the `bz_xfin` dim-out. Fanart, strip, dim and labels are unchanged.

### Background dim under MM — poster and fanart together (5.33.213)
| Item | Current state |
|---|---|
| Mechanism | MAIN MENU › **Background dim level** (`bz_at_mmdim`) fades the whole section parent group (`BezelSecDim`, Includes_Bezel.xml ~582). Fanart, poster/album, list all sit in that group and dim by the same %. Right = brighter, Left = darker (5.33.212). |
| Stops (5.33.214) | `bz_at_mmdim` 1–11 → section fade end 5 / 10 / 20 / 30 / 40 / 50 / 60 / 70 / 80 / 90 / 100%. Empty = 2 (10%, default). Stop **11 = "No dim (100%)"**: fade end 100 = full opacity, art exactly as with MM closed. Right steps up to it, Left steps down. Labels `BzATVal_mmdim` (Includes_Tuner ~202). |
| No art cover under MM | `BezelRootArtHide` no longer draws the old 3.1.2 MM-open black panel over the right art window (x 962–1920). Only the library-root black (`bz_libroot`) is left. |
| Why it was removed | That panel sat in its own `BezelSecDim` group, so Background dim faded the **cover** too. The poster showed at about (1 − dim) and the fanart at dim: the two moved in opposite directions and crossed around 50–60%. Measured on 5.33.212: poster 2→12→17→24→31 vs fanart 24→21→18→15→11 at 100/80/60/40/20%. |

### Settings stays in the Warm system (5.33.215)
MM → SETTINGS opens dialog 1130 over the section instead of replacing it, so Warm/poster/section stay loaded under it; Back returns to MM with no poster reload. Stock pages reached from it do replace the section (normal Kodi windows); on return the section reloads, then 1130 reopens. See settings.md.

### Music A/B art lane (5.33.216)
| Item | Current state |
|---|---|
| Lane | `_ABLane('mart', settle 0.25, load 0.5, empty_flag)` in `bz_flip.py` `ab_clock`, fed by `_ab_mart()`: Music window only; `Container(60).ListItem.Art(thumb)` else `.Icon` (parent folder `..` → next item), `Default*` skipped. Same preload-hidden → side flip as the Videos poster lane. |
| Properties | `bz_mart_a` / `bz_mart_b` / `bz_mart_side` / `bz_mart_on` / `bz_mart_empty`. Music never writes `bz_pos_*` (BUG-010 kept: Videos owns `bz_pos`). |
| XML | Includes_Bezel.xml poster group, after the MM pos A/B twins: two images gated `$EXP[bz_navmenu] + !$EXP[bz_mmmushide] + Window.IsActive(music) + bz_mart_on + !bz_mart_empty` + side. Visible 0→100 1500 ms sine (only while `bz_ab_live`, so MM open = full opacity same frame), Hidden 100→0 1500 ms sine, texture fadetime 0. |
| Live twin | `BezelPoster60` MM twin (fadetime 3000) now yields in Music whenever the mart lane has art; it still covers no-art items (blank — no stand-ins, 5.33.276) and Videos before `bz_pos_on`. |
| Leaving Music | `_ab_mart` returns empty → `bz_mart_empty=1` → lane hidden in Videos. Mirror-enter seed keeps the front side on the current Music item while MM is closed. Music playing (mushide) path unchanged. |

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/mm-warm.md) · [state](../state/mm-warm.md) · [motion](../motion/mm-warm.md) · [art](../art/mm-warm.md) · [input](../input/mm-warm.md) · [theme](../theme/tokens.md) · [screens](../port-refs/mm-warm/) · [PORT_INDEX](../PORT_INDEX.md)


## No-art (5.33.276)

**Simple:** No fake art anywhere. If an item has no art, its slot just shows empty.

**How it works:** stand-ins never display (extras/standins/ left on disk, unwired); no `DefaultAlbumCover.png` in `BzWarmMusicArt`; idle big album and poster window no longer fade out for no-art.

**Wiring:** `bz_noart60` / `bz_vnoart` expressions and their two Conditional fades deleted from Includes_Bezel.xml.

## Music warm = the big-album rail, unbroken (5.33.281)
**Simple:** With music playing, opening the menu over Music keeps the exact same big album + compact NP (album rail 6367/6377/6397/6382, whichever `bz_at_fsslide` picks) on screen. No second warm copy, no re-fade.

**How it works:** The rail lives in `View_60_BezelInfoList` (Music artists/albums/songs group) and was never hidden by MM. The break was inside `BezelMusicPlayingArt` cover faces A/B: the playing face was a twin pair — section image `!$EXP[bz_navmenu]` (fadetime 0) and MM image `$EXP[bz_navmenu]` (fadetime 3000, BZMMXF). Opening MM swapped controls, so the album re-loaded and faded in over 3 s. Both faces sit inside the `Player.HasAudio` group, so the section image now has no MM gate and the MM twin + pos A/B lanes are `false` (they could only show with `!Player.HasAudio`, which is impossible there). Dust: ambient (BELOW include + 1114 ABOVE) no longer fades out under MM while Music artists/albums/songs is the underlay; Tuner (`bz_navtune`) still fades it. Glare rides the faces (no MM gate). `bz_mmmushide` is for Videos-family underlays only and does not touch the Music rail.

## Big album rail on non-Music underlays (5.33.289)
- The Music big album rail (grouplists 6367/6377/6397/6382 + compact NP) is ONE shared include `BezelMusicRail` (Includes_Bezel.xml, defined just above `View_60_BezelInfoList`).
- Music view: mounted in `View_60_BezelInfoList` with the original gate `[music|musicplaylist] + [artists|albums|songs]` — unchanged.
- Other View_60 underlays (Programs/Games/Favourites/Playlist): same include, extra OR gate `$EXP[bz_mmmushide] + !music + !musicplaylist`.
- Movies/TV (MyVideoNav): mounted after `View_60_BezelVideoPosterList`, gate `$EXP[bz_mmmushide]` (= audio, no video, MM open, warm music posters not Off). Closes with MM → normal section UI when you Select into Movies/TV.
- The old framed 600×600 `BzWarmMusicArt` stand-in (+ its frame) in `BezelVPLPoster` is retired (`visible=false`); poster lane still hides under mushide.
- Caveat: Kodi tears down window controls on Music↔other window swaps, so the rail remounts → album/NP cut + sway restart (accepted by Rob).


## Big album (5.33.309 P1)
The big album, its sway, next-song fade, cast and compact NP no longer live in this screen. They live in the always-open dialog **1122** — see [big-album.md](big-album.md). This screen only decides where the album sits (Home prop `bz_rail`: `home` / `centre` / `hide`). The old album grouplists 6367/6377/6397/6382 and their focus buttons (6368/6369, 6378/6379, 6398/6399, 6383/6384) are deleted; nothing focuses into an album rail any more.

## 5.33.314
- MM warm focus on Music no longer fires `bz_sway_restart` (MyMusicNav onload removed). Big album 1122 dims with BezelSecDim under MM like the section art.

## Poster watched/resume badge under MM music (5.33.323)
Rob t2414: the TV/movie poster corner badge (dot + check / play_badge, Includes_Bezel.xml ~2863, x1518 y136) drew on top of the big album when MM was open with music playing over a Videos screen. Its group was gated only `Window.IsActive(videos) + PlayCount/IsResumable`, while the poster frame beside it already had `!$EXP[bz_mmmushide]`. The badge group now has `+ !$EXP[bz_mmmushide]` too, so it hides with the poster lane under MM music and comes back on TV/Movies normally. The list-row badges are unchanged.

## Poster stack under mushide (current, 5.33.328)
While music plays under MM (`bz_mmmushide`), the entire poster-slot stack group (`bz_pready` group in Includes_Bezel: Videos/Music twins, live twins, MM A/B pos lanes, Music A/B art lanes) is hidden at the parent, so focusing Movies/TV never shows or fades a poster behind the 1122 big album. Frame, cast, LOOK, glare/dust, badges were already mushide-gated.

## Movies flash on MM pass-through (flagged 2026-11-02, t2446)
- Repro: MM open on TV SHOWS, press Up twice / Down twice at ~0.25 s per press. Movies sits between Music and TV, and the in-place park (Tuner Background warm delay, default step 1 = 0.2 s) runs out while you pass it. That fires an in-place `Container.Update(videodb://movies/titles/)` swap and MMWARM2 `_hold` (focus locked to 6996 during the repaint) → Movies list flashes in and input feels pulled. Log: label MUSIC while FolderPath already movies.
- Proposed fix (not applied; changes your 0.2 s tuning): in-place swap also gated at ≥0.5 s like window switches (bz_flip.py ~L622), or raise Tuner Background warm delay. Needs FULL restart if applied.

## 5.33.336 — Movies flash / pull-back fixed (t2453, supersedes earlier flagged diagnosis note)
- Root cause was focus, not the 0.2 s warm delay (unchanged). `_bzstrip` treated strip Position 0 (MUSIC row) as "fresh" and did SetFocus(6996,bz_mmlive=Movies,absolute), which yanked you back. It also re-SetFocused an already-focused strip, restarting the row focus anim (the flash).
- Fix: `_bzstrip` returns early when 6996 already has focus. `_restore2` reads the live strip row before bouncing and forces SetFocus(6996,live,absolute) directly. The `_defer` mm bounce is forced the same way.
- Smoke: TV→up,up (0.3 s) lands on MUSIC and stays; down,down lands on TV and stays; Movies→Music mid-warm stays on Music.

## 5.33.346 — t2488 album frame posters
MM A/B poster lane (bz_pos_a/bz_pos_b, 6 images in Includes_Bezel) is now gated `Window.IsActive(videos)`: Movies/TV posters never paint into the Music album frame after Movies→Music under MM. ReloadSkin.
