- 2026-11-02 5.33.317 (Rob t2397 "Remove the wait"): stub/side albums (BezelFSPlayNext) no open wait — sdelay 3000→0 on 1120, MusicVisualisation, 1121 + include default; sfade 2000 kept. bak ../bak_5.33.316_pre317. ReloadSkin. No zip.
- 2026-11-02 5.33.311: Custom_1122 centre copy WindowOpen fade end=100 (was ending at 0 → centre invisible after slide, found in 310 smoke); centre opens full alpha after 600ms then slide owns it. Plus L3 meta: small artist / big album. Pushed skin.bezel2-5.33.311.zip → HPLaptop Downloads. FULL restart (bz_flip.py changed in 309).
- 2026-10-31 5.33.190 BUG-028 FIXED: hide MM list 6996 under Tuner/BEZEL Settings; guard bz_flip strip focus.
- 2026-10-31 5.33.188 BUG-011 (Rob voice): restore Tuner-row MM-start hold dropped in .187 warm-151 rollback (same as .186). Hold bz_mmstart until 6996 on bz_mmstartrow (6s cap); do not latch pre-start bz_mmlive; pin navstrip/mmlive/mmpos to start row during hold. Startup-only. FULL restart. bak scripts/bz_flip.py.bak_5.33.187_pre188_bug011. No zip.
- 2026-10-31: pushed skin.bezel2-5.33.187.zip → HPLaptop C:\Users\rober\Downloads\ (~32MB). Warm = 5.33.151 base + artists-only Music underlay + BUG-010 Music/poster lane split. FULL restart. Includes bloom cast / BackTrap / TV desc from .182–.186 non-warm work.
## 5.33.187 — Oct 31 2026 — Warm rolled back to 5.33.151 (Rob voice)
- bz_flip.py warm + Includes_Bezel warm lanes restored from 151; KEPT artists-only Music underlay (.164/.168 BUG-016) and BUG-010 family split (.161).
- Undone: .160 fade-in-only, .162/.185 lane fades, BUG-011 (.186) mmstart hold, BUG-015/.178 empty hold + drop gate. movposter_hold back.
- Non-warm kept: BUG-021 cast sway clock, BUG-024 rp arm, bloom .184, BackTrap 6299, FS pill, TV desc .182, .177 BezelWindowFade, stand-ins stay parked (BUG-008).
- Backup: rebuild/bak_5.33.186_pre187_warm151/. FULL restart. No zip.

- 2026-10-31: pushed skin.bezel2-5.33.186.zip → HPLaptop C:\Users\rober\Downloads\ (~32MB). BUG-011 FIXED — MM-start held until strip 6996 on Tuner start row; Music underlay artists. FULL restart. Includes .185 Left/Back MM soft fade + .184 bloom cast + .182–.183 TV desc / BackTrap.
- 2026-10-31: pushed skin.bezel2-5.33.185.zip → HPLaptop C:\Users\rober\Downloads\ (33MB). Includes .184 bloom cast + .185 Left/Back MM soft fade + .182–.183 TV desc / BackTrap.
- 2026-10-31 5.33.185 (Rob voice): Left/Back MM flash on Music/Movies/TV — lane-a Visible fade restored to 1500ms sine (was 300ms from 5.33.162 BUG-012). Fan+pos A/B side-a (4 controls). Hidden hold for A/B swap kept. Soft restart. bak_5.33.184_pre185_lanea_mmfade. No zip.
- 2026-10-31 5.33.184 (Rob voice): bloom wide soft haze approved → default poster cast for Movies+TV (BzCastTex_p → cast_mp_bloom.png; cast_mp_current.png bytes = bloom; bak cast_mp_current_pre184_bloom.png). All 4 poster cast slots use $VAR[BzCastTex_p]. Soft restart. No zip.
- 2026-10-31 5.33.183 BUG-026 (Rob voice): Back→MM flash — BezelBackTrap 6299 no longer SetFocus(60) while MM open (hands strip 6996); matches Left fade path. Soft restart. No zip.
- 5.33.181 (2026-10-31 Rob voice): double-tap Tuner infographics — icon centered on horizontal midline of "double-tap" label (cy match; fine-tuned +1px from bak). mm_dtap_toggle.png + mm_dtap_window.png only. ReloadSkin. Bak: bak_5.33.180_pre181_dtap_icon.
- 5.33.181 push (2026-10-31 Rob voice): zip → HPLaptop Downloads skin.bezel2-5.33.181.zip after cast peak shots + flash-check report + dtap icon midline fine-tune; also added behaviors/sway-animations.md (clock/cast math). No new flash fix in .178–.181.
- BUG-025 (2026-10-30 Rob voice): TV fanart upper-left bold show title when no clear art — FIXED 5.33.180.
- BUG-023 logged (2026-10-30 Rob voice): black bar drawn during Options/context menu openings — open, log only, no fix.

- 5.33.167 (2026-10-30): bake pause bars into ghost Bezel logo — new media/bezel/logo_pause.png (logo.png + centered solid pause in hollow; source glyph from approved mockups/pause-logo np_pause); both center-album pause overlays (Dialogue FS + Play Next) point at logo_pause.png; logo.png untouched for LOOK/home. ReloadSkin. Bak: bak_5.33.166_pre167_pausebake.
- 5.33.113 (t787): Dialogue FS/Play Next big album pill 6401 + NP bar + 1120 center controls WindowOpen fade delay 3800->800ms, time 1200->600ms.
- 5.33.113 (t790): Play Next NP bar + cycle pill + center controls WindowOpen delay 800→1000 (1s).

## 5.33.115 — t801/t802 Dialogue FS Select stops music (Oct 30 2026)
- Root cause: 6400 Select = SetFocus(6403) (pause). A second/repeated Select (CEC remote sends a held press as repeats) landed on 6403 → PlayerControl(Play) toggled PAUSE + Dialog.Close. Same path on prev/next 6402/6404 (PlayerControl Previous/Next + close).
- Fix (in place): 6400 onclick sets home bz_pnsel for 1 s (AlarmClock clear); all 6402/6403/6404 onclicks gated on String.IsEmpty(bz_pnsel). 1120 onunload clears bz_pnsel. Deliberate Select on pause/prev/next after 1 s works as before.
- Files: xml/Custom_1120_PlayNext.xml, xml/Includes_Bezel.xml (BezelFSPlayNext), addon.xml. XML-only → ReloadSkin. K40 untouched.

- 5.33.117 (Rob t811/t813): viz Play Next album 6390 matches 1120 6400: Select = PlayerControl(Play) + pause logo (bz_pnfoc=6403 when pausing, cleared on resume); Left/Right = PlayerControl(Previous/Next) (was SetFocus 6402/6404). Pill 6391 unchanged. Includes_Bezel.xml only. K40 untouched. t813: Music section (bz_pndlg_ok) click on 6390 opens Dialogue FS 1120 (SetFocus 6399 + ActivateWindow 1120, same as Right) instead of play/pause.
- 5.33.117 t815: tap big album = pause+logo in 1120 (6400) and viz Play Next (6390); side albums 6405/6406 (1120, PREV/NEXT mode) and 6407/6408 (viz Play Next) = Playlist.PlayOffset(music,-1/+1), mouse-only (onfocus bounces to centre). t816: BezelLogo include gets id-less 120x116 tap = Action(Back) for windows without BezelLogoButton.
- 5.33.116 (Rob t806/t807): Dialogue FS 1120 centre 6400: Select = PlayerControl(Play) (pause/resume) + pause logo (bz_pnfoc=6403 while paused, cleared on resume); Left/Right = PlayerControl(Previous/Next) directly (no hidden button row). Replaces 5.33.115 1 s bz_pnsel guard + SetFocus(6403). Cycle pill 6401 unchanged. K40 untouched.

- 5.33.118 (Rob t823/t820): pause overlay logo (1120 + viz Play Next, both copies) ghost: 117->111 px (~5% smaller, centred), 59FFFFFF (~35%). NP bar BezelNPCompactBar: artist own row above title (1040,892 h24, new font bz_b22 Ubuntu-Bold 22, CCFFFFFF, uppercase); title unchanged at 922. XML only -> ReloadSkin. K40 untouched.
- 5.33.119 (Rob t826u "shadow ok"): Play Next cast (BezelFSPlayNext, both sides, 1120 + viz) broader 144->270 (L left 396->270, R left 0); pn_cast.png alpha baked x1.6 (max 150->240; black tex so colordiffuse cannot densify). Sway fade anims/conditions untouched. XML+media -> ReloadSkin. K40 untouched.

## 5.33.135 (t968/t970 + parent steer, Oct 30 2026)
- Stub album chrome behind shadows, BOTH views (BezelFSPlayNext shared by 1120 Dialogue FS + viz Play Next): side frame bz_frame_soft drawn before pn_cast in prev+next side groups (was drawn after = chrome over cast).
- Fanart FS L/R/dtap dead: 6390 conditions used `!( ... )` — Kodi infobools only group with [ ]; 7 conditions rewritten to `![ ... ]` (incl. onleft Previous fallback, onclick fallbacks). Single-Select pause: AlarmClock(bz_vdtapgo) now armed BEFORE SetProperty(bz_vdtap,1) (old order made its own condition false → pause never fired). Backups /workspace/*.bak5.33.134. XML only -> ReloadSkin. No K40.

- 5.33.138 (Oct 30 2026, t980): Pause overlay unified to ghost Bezel logo (111px, 35%, .118 look) on big album for all pause paths (Select+touch): Dialogue FS 1120, fanart FS, viz Play Next centre. Gated on Player.Paused (was bz_pnfoc focus). Old rc_prev/pause/next nav-arrow overlay removed (1120 images) / textures blanked (6402-6404 buttons kept). XML -> ReloadSkin. Bak: bezel-533-fork/bak_5.33.137_prepauselogo

## 5.33.139 (Oct 30 2026, t987/t988)
- Music section tap/Select big album (6390) -> Dialogue FS 1120 restored: flattened nested `![..]` onclick/onleft gates to `$EXP[bz_pndlg_ok]` / `!Window.IsActive(visualisation) + !$EXP[bz_pndlg_ok]` / `!viz | bz_pnoff==1` (same logic). ReloadSkin. Zip /workspace/skin.bezel2-5.33.139.zip. Bak /workspace/Includes_Bezel.xml.bak5.33.138

## 5.33.151 (Oct 30 2026, BUG-002 follow-up)
- File Manager context menu focus/Back: DialogContextMenu template 1000 texturefocus literal lists/focus.png; dismiss button onfocus SetFocus(996); Includes_Bezel BzCtxTxt FM/FB 99FFFFFF (focused stays FFFFFFFF). ReloadSkin. No zip. Baks *.bak_pre151_bug002

- BUG-008 (Oct 30 2026, voice): WARM 2.0 TV→Movies flashes poster + chrome; Movies→TV smooth. Logged in bugs.md — investigate/open, no fix.
- BUG-009 (Oct 30 2026, voice): WARM 2.0 / Dialogue FS + FS fanart — stub albums cast at wrong sway phase (needs reverse). Logged in bugs.md — open, no fix.
- BUG-008 fix (Oct 30 2026, voice): removed bz_movposter_hold entirely (bz_flip.py + Includes_Bezel.xml) — Movies poster works like TV, no hold/fallback. 5.33.152.
- BUG-008 scope add (Oct 30 2026, voice): deleted extras/standins/posters/poster_A–E.jpg and removed all 15 standins/posters multiimage controls (Includes_Bezel.xml: MM list-60 poster + grid posters). Albums/artists stand-ins untouched. 5.33.152.

- 2026-10-30 5.33.153 BUG-008: stop Movies/Music fallbacks; stand-ins + DefaultAlbumCover.png parked at /workspace/bezel-533-fork/parked_standins_bug008/ (restore paths in README).
- 2026-10-30 5.33.154: hide FULLSCREEN pill (6886) when Window.IsActive(visualisation) — fanart FS. Includes_Bezel.xml colour-strip group visible.
- 2026-10-30 5.33.155: FULLSCREEN pill 6886 — remove VisibleChange fade so fanart FS hide is hard visibility only (!Window.IsActive(visualisation)).

## 5.33.156 — Viz opacity drives stub/side album opacity
- BezelFSPlayNext: prev/next 540 album stack (base FF101010 + cover + dim + glare) wrapped in group with 6387 bz_at_fsvizop fade ladder (1=0%..10=90%, empty/11=100%).
- 6387 ladder kept. Tuner desc updated. Backups *.bak_pre156_vizstubop. ReloadSkin.

- 2026-10-30 5.33.157 BUG-007 attempt: Bezel Tuner group id=6975 hard-hide on Back; ClearProperty(bz_navtune) before ActivateWindow(1118) when tunesrc=pwr.

- 2026-10-30 5.33.162 (Rob voice): BUG-011 logged (startup focus / Music artist list default, no fix). BUG-012 fixed: A/B fan+poster black-start removed (hold-under crossfade), BUG-010 kept. Dust size investigated (no code).

- BUG-013 (2026-10-30): Settings Back → section then MM; want direct MM. Logged open, no fix.
- 5.33.164 (2026-10-30): Music MM underlay always artists; Select keeps bz_lastmusic; underlay flag stops artists from poisoning last browse.
- 5.33.165 (2026-10-30): grouplist 6397 scroll follows bz_at_fsslide (4 rails 480/380/280/180); default mid-high keeps 6397/6398/6399.
- BUG-014 (2026-10-30): right stub missing cast; want casts above stub overlays + title tags. Logged open.
- 5.33.166 (2026-10-30): ghost pause logo centred on big album (245,245); was 27,27. ReloadSkin.
- BUG-015 (2026-10-30): TV→Movies fade hitch — TV art pops out before Movies underlay. Logged open; Rob session may add more; no fix.
- BUG-016 (2026-10-30): MM Music background after album browse shows album not artists; want artists always on highlight (Select resumes last). Logged open; no fix.
- 2026-10-30 5.33.168: BUG-016 fixed — MM Music underlay always artists even when MM opened from album browse (bz_flip mm_warm open-row check). FULL restart.
- BUG-017 (2026-10-30): MM mini-player Fullscreen opens section behind/last instead of fanart FS. Logged open; no fix.
- BUG-018 (2026-10-30): Fullscreen pill still visible in fanart FS / Kodi fullscreen. Logged open; no fix.
- BUG-019 (2026-10-30): stub album cast shadows wrong sequence — need switched. Logged open; no fix.
- BUG-020 (2026-10-30): Music section Right does not open player controls. Logged open; no fix.
- BUG-021 (2026-10-30): stub cast shadows out of sync with sway until stub reset. Logged open; no fix.
- 2026-10-30 5.33.169: BUG-018 FIXED — FULLSCREEN pill 6886 hidden in all FS states (viz active/visible, Dialogue FS 1120, fullscreenvideo). Includes_Bezel.xml gate only. ReloadSkin.

- 5.33.170 (Oct 30 voice): BUG-021 fix — stub Play Next cast reads shared sway clock (bz_flip sway_clock → bz_castL/bz_castR; own XML fade timers removed). FULL restart. bak_5.33.169_pre170_bug021.

- 5.33.171 (Oct 30 2026): BUG-021 follow-up — stub cast opacity = sway-clock phase × Tuner Viz/stub opacity (bz_at_fsvizop); no art-brightness wiring. bz_flip.py + Includes_Bezel.xml cast fades. FULL restart.

- 5.33.172 (Oct 30 voice): BUG-022 fanart FS keys — Select/L/R on block cycle pill (SendClick 6391), Up=pill unchanged; viz Play Next + Dialogue FS untouched. Includes_Bezel only. ReloadSkin. bak_5.33.171_pre172_fsfankeys.
- BUG-017 clarify (2026-10-30): MM mini-player Fullscreen pill must open fanart FS directly from MM — not section behind/last first. Logged only; no fix this pass.

- 2026-10-30 5.33.173 BUG-018b: harden 6886 FS hide (IsVisible 1120/fullscreenvideo/1112, bz_pnoff, bz_fsret latches). ReloadSkin. No zip. 017 untouched.

- 2026-10-30 5.33.174 BUG-020: repaired 52 malformed onright tags in Custom_1115_MusicControls.xml (13 buttons) — 1115 loads again, Music Right opens controls. XML only, ReloadSkin. No zip.

- 2026-10-30 5.33.175 BUG-015: poster A/B lane empty flag now needs 1.5 s persistent empty (was 0.25 s) — TV art no longer pops before Movies fade-in. bz_flip.py, FULL restart. No zip.
- 2026-10-30 5.33.177 (Rob voice): all section transitions standardized to MM→TV fade-in (0→100 400ms sine out, no fade-out/zoom) at every level incl. sub-pages: Settings (+Category/Profile/SysInfo/SkinSettings/dialogs), Add-ons, Pictures, Search, Favourites, Media Sources, Power, Playlists, PVR, etc. Includes BezelSecFadeIn/BezelSecFadeInDialog; BezelWindowFade/BezelOpenCloseSet redefined. Movies/TV/Music already matched. XML → ReloadSkin. No zip. bak_5.33.176_pre177_secfadein.
- 2026-10-30 5.33.179 BUG-024 (Rob voice): Back→MM direct for Pictures, Add-ons, Search, Media Sources, Power, File Manager, Weather, System info (root onback SetProperty(bz_nav,true,home), BUG-013 pattern); Favourites/Programs/Games root arm immediate on fresh open (bz_flip.py). FULL restart. No zip. bak_5.33.178_pre179_mmback.

- 2026-10-31 5.33.182: TV colour-strip Description matches Movies — BezelVPLContent shows/seasons pairs 176/468 + divider 652; episodes divider 652; DialogVideoInfo plot unified to 200. ReloadSkin. bak_5.33.181_pre182_tvdesc_*.

- 2026-10-31: behaviors/sway-animations.md rewritten — full math/formulas/current settings from live 5.33.182 tree (bz_flip + Includes_Bezel). Draft, not approved. No skin code change.

- 2026-10-31: behaviors/sway-animations.md — added plain-English “How it works” overview (clock, flags, hold/restart, Conditional XML, casts). Math sections unchanged. Draft.
- 2026-10-31: cast mockup cast_on_solid_fanart_stage.png — current cast on solid fanart-stage block (no poster); prior style/extended approaches discarded per Rob.

## 5.33.186 — BUG-011 startup focus (2026-10-31)
bz_flip.py MM-start: hold bz_mmstart until strip 6996 is on Tuner start row (bz_mmstartrow), don't latch pre-start row as bz_mmlive. Smoke t533f1: default TV → 6996 row 2, videodb://tvshows/titles/; Music → 6996 row 0, musicdb://artists/. FULL restart. No zip.

## 5.33.189 — Movies movposter/fanart hold across TV (2026-10-31)
Movies-only: keep `bz_movposter_hold` + new `bz_movfanart_hold` while on TV/other sections (removed clear-on-!movies). `_ab_poster` / `_ab_fanart` use holds under movies path/content so empty frames after TV do not blank the lane. mm_warm park/swap, A/B fades, settle timing untouched. TV unchanged. FULL restart. Zip → HPLaptop Downloads.
- 2026-10-31 5.33.191 WARM 2.0 (Rob voice): MM + music playing + toggle On → MM poster lane hidden, album art (Player.Art(thumb)) in its slot; fanart stage untouched. New Tuner section WARM 2.0: "Posters during music" Skin.String bz_at_warmmusicposters (On default/Off) + "A/B fade length" Skin.String bz_at_abfade (7 steps 2500/2000/1800/1500/1200/1000/800 ms, default 1500; drives MM fan+pos A/B Visible/Hidden fades). BUG-028 kept. ReloadSkin (FULL restart if installed from zip). bak *.bak_5.33.190_pre191_warm20.
- 5.33.192 (Oct 31 2026): restored fan/pos A/B fades to unconditional 1500ms Visible+Hidden (189 style), removed 7-step bz_at_abfade chains from Includes_Bezel.xml; Tuner WARM 2.0 rows + mmmushide poster gate untouched.
- 5.33.193 (Oct 31 2026, Rob voice): WARM 2.0 music-poster toggle fixes. (1) bz_mmmushide now also hides poster cast (animated+static), poster_blur/frame.png, BezelATLook and glare/lit-dust groups in BezelVPLPoster; album slot + fanart untouched. (2) Toggle refresh: Tuner warmmusicposters Left/Right also SetProperty(bz_mushref) + AlarmClock clear 1s; pos fallback/A/B + album images carry a 400ms Conditional re-latch fade on bz_mushref; no sway props (bz_pswayon/bz_ppulse) cleared, no .py change. (3) BzWarmMusicArt fallback thumb > album.thumb > MusicPlayer.Cover > Player.Icon > DefaultAlbumCover.png. (4) Polarity: chose rename, kept On=album/hide-posters — row now "Album art during music", label2 "On (album art, posters hidden)"/"Off (posters show)", desc updated. 1500ms unconditional A/B kept. ReloadSkin.

- Oct 31 2026: Tuner WARM 2.0 "Startup splash" toggle (`bz_at_warmsplash`, default On) — hides splash visuals only; warm-cache always runs. Source only, no zip, still 5.33.194.

## 5.33.196 — warm-gate splash hang fix (Oct 31 2026)
- bz_warmgate.py: all Files.GetDirectory off main thread; ready flags always set; early dismiss for Music/Movies/TV landing list 60; 5s watchdog + Dialog.Close(1113,true).
- Smoke: box t533f1 cold start.
- Startup.xml: removed ActivateWindow(1113) from onload (blocked RunScript/ReplaceWindow); script opens 1113.
- 5.33.203 (2026-10-31 Rob voice, code only not zipped): Power 1118 first-Down handoff — drop defaultcontrol always=true; onload SetFocus(7800,0,absolute). behaviors/power-menu.md updated. Bak: bak_5.33.202_pre_pwrfocus.

- 2026-10-31 10:45 PM ET — Rob: Background dim (mmdim) slider worked opposite of press direction. Swapped onleft/onright (Right=brighter). 5.33.212, on tree, not zipped.

- 2026-11-01 ~00:30 ET 5.33.215 Rob pt1691u: new BEZEL Settings (dialog 1130 over section, MM strip style, ▾ expand / » menus / ‹VALUE› pills, SERVICES sub-page, WARM 2.0.1 · TUNER row under INTERFACE). Back = MM, no poster reload. bz_mm.py + new bz_set.py → FULL restart. Docs settings.md + mm-warm.md. Bak b401/bak_5215_settingsmm_001550. Not zipped. Other stock pages to be done one by one.

- 5.33.217 (Rob t1709u, 2026-11-01): MM idle undim — BezelSecDim mmdim Conditionals (11) + `String.IsEmpty(Window(Home).Property(bz_mmidle))`; idle → art 100% opacity, wake → Background dim returns. gdim untouched. XML only → ReloadSkin. Docs mm-list.md, mm-warm.md. Not zipped/pushed.

## 5.33.218 (Nov 1 2026) — FULL restart (.py + XML)
- Rob t1712: album sway / poster-hide while music plays on every strip section, not only Music. Root cause: album slot visible had `!String.IsEmpty($VAR[BzWarmMusicArt])` → Kodi "Misplaced [" parse error → slot never showed in Videos underlay. Fixed (visible = `$EXP[bz_mmmushide]`). Smoke PASS: TV, Movies, Favourites show swaying album, posters hidden; stop → Star Wars poster returns.
- Rob t1713: Music Warm random start. bz_flip: window-switch wait ≤4s FolderPath+!IsUpdating; `r is None`; `_snap` no unseeded row; `bz_warmrow` grid-sync guard. Movies/TV randomize (smoke rows 31/8). Music: randstart picks row (log row=30/40) but list stays on '..' — SetFocus ignored on Music list under MM. OPEN. Tried Control.Move fallback → stole strip focus, reverted.
- 2026-11-01 5.33.220: Add-ons (new 1131) + Media Sources 1117 + AddonBrowser + DialogAddonInfo rebuilt as Warm strip menus (Rob t1727s5849 👍, t1729–t1731). FileBrowser stays stock.
- 2026-11-01 5.33.221 (Rob t1737/t1738/t1739/t1741): Warm strip menus (Add-ons 1131, Media Sources 1117, AddonBrowser zip/repo/category follow-ons, DialogAddonInfo, Settings 1130) now use Bezel list highlight bar ($VAR[BzATHiTex]/BzATHiCol, text BzATHiText) and Bezel np_pill32 pills (replaced mm_pill_ol outline + ad_pill_on/off). Buttons use HasFocus sibling image ($VAR in button texturefocus didn't render). Smoke /workspace/b401/smoke221/. Bak /workspace/bak221/. XML only → ReloadSkin (FULL restart recommended if coming from <220).
- 2026-11-01 5.33.221 (Rob 👍): Music big-album touch 6180 wired to Dialogue FS (6390 bz_pndlg_ok + fsslide onclicks → ActivateWindow(1120)). Docs music-list.md, dialogue-fs.md.

- 2026-11-01 ~02:40 ET 5.33.227 (Rob pt1804u) Music art briefly in poster crossfade on section switch. Cause: poster-slot live images (section twin fadetime 300 + MM live twin fadetime 3000) used shared $VAR[BezelPoster60] with Music thumb branches; the control kept the last Music album as its texture, so switching to Movies/TV crossfaded from that album into the poster. Fix in place: split each into a Videos control (BezelPoster60V) + Music control (BezelPoster60M) — separate texture memory. A/B lanes, mushide, BUG-010, mvidfade untouched; no K40. XML only → ReloadSkin. Bak /workspace/b401/bak_5.33.226_pre227_0240. Not zipped. Not device-smoked.
- Rob t1849u: first MM→Music focus after cold start still flashed row 1. 5.33.238 RANDFLASH3: bz_randpend 'w' watchdog 4s→15s fail-safe (cold DB load outlasted it); set after noop check; window-switch Music list wait ≤12s. FULL restart. Not zipped.

- 5.33.262 GLARESPLIT (Rob t1949u): idle fold glare split into L/R 300x600 halves (aspectratio align crop + art_mask_hl/hr half masks, no squash). Static L hidden ph2, static R hidden ph1; ph1 leaf carries R glare, ph2 leaf carries L glare. Rest: both static halves.

- 5.33.263 GLARESWAP (Rob t1953u): half-glare aligns swapped L<->R (static+leaf). GLAREPOP (Rob t1954u): removed bz_hf_ph hides on static half glares (no pop).

## 5.33.268 — Music layer 3 new album strip, step 1 (Rob t2022u–t2024u, Nov 1 2026)
- New in-album left strip per Mock 1 (mock_album_disc_view option D) + Mock 2 (mock_album_list_d_approve): header top, no 450 slot, 60px track rows, white pill focus, no thumbs. `$EXP[bz_l3]` (View D + MM closed). Includes_Bezel.xml only + new media/bezel/l3_pill.png. XML/media → ReloadSkin. Not zipped.
- Left: disc header rows, right song panel at mock size, drop A/D toggle.

## 5.33.269 — L3 right song panel (Rob t2026u, Nov 1 2026)
- Big album art scale (3B 330²), not jumbo; static swap on song change (no anim — Rob no). Title rest bz_m40 no-scroll (fixes "| MU" marquee seam). XML only → ReloadSkin. Not zipped.
- Optional parked: big album anim on song change — Rob said no.

## 5.33.270 — MERGED13: Artists → one song list with album headers (Rob t2053u/t2054u/t2057u, Nov 1 2026 ~17:15 ET)
- Parked/reverted 5.33.268/269 L3 strip + right-panel edits: Includes_Bezel.xml restored from the 5.33.267 backup (the only diffs were 268/269). l3_pill.png + the 269 XML were moved to /workspace/b401/parked_l3_268_269/. No dual L3.
- bz_flip.py: Artists root → artists/ID/ hops to artists/ID/-1/ (all songs), sort Album asc. Back from merged → artists/ID/ → Action(Back) → Artists. Gated !bz_nav !bz_mmwarm.
- Includes_Bezel: new $EXP[bz_m13]; bz_discbar fix-in-place also fires in bz_m13 on track 1 → album header bar; $VAR[BzDiscBarLabel] (ALBUM · YEAR / ALBUM · DISC n / DISC n · title).
- Backups *.bak-5.33.269-*, /workspace/b401/bz_flip.py.bak-5.33.269-*. Smoke /workspace/b401/smoke_270_merged13/. .py → FULL restart. Not zipped.

## 2026-11-01 17:45 ET — 5.33.271 t2061 remove View D cover slot from merged Music list
Rob: "Take out" the black box above the merged song list. Gated the View D cover-column groups (FF141414 mask + BezelInAlbumArt + album title/artist header; Includes_Bezel ~L1542/2198/2199) with `+ !$EXP[bz_m13]`. Normal album View D unchanged. Album header disc bars, big album, strip, fold, sway, MM, ALLHIDE untouched. Rows stay in covercol slots (list height is fixed; ungating the 900 slide left the bottom half empty and rows spilled above the panel — reverted). XML only → ReloadSkin. Smoke: /workspace/b401/smoke_271_nocovercol/. Not zipped/pushed.

## 5.33.272 — Nov 01 2026 17:44 ET — MERGED13 full-height rebuild (Rob t2062)
- bz_covercol excludes bz_m13; new dedicated 75px item/focused layouts for bz_m13 (full height, header bars); bz_allpull_inall gated !bz_m13; bz_nojumbo blocks idle jumbo zoom on Artists root + merged list. Fold lock untouched. ReloadSkin (XML). Not zipped.

- **5.33.273 NOFRAME (Rob t2065u, Nov 1 2026):** big white "panel frame" on Music right art was NOT a panel control — it was the hinge-fold stack group (Includes_Bezel.xml ~L1097: static half-frames bz_frame_half_l/r + shades) and the two glare groups (~L1117, ~L1121) still running the idle jumbo zoom 100→150 around 1440,420 (→990,120 900²) because 272 gated only the art layers with `!$EXP[bz_nojumbo]`. Gate added to those 3 zoom-ins. On Artists L1 + merged songs the fold half-frames/glare now stay locked to the 600² art at 1140,220 (thin edge only). Fold, sway, glare, 6180 touch untouched. ReloadSkin (XML). Smoke /workspace/b401/smoke_273_noframe/. Not zipped.

- 2026-11-01 ~5:50 PM ET — 5.33.272 zipped (/workspace/skin.bezel2-5.33.272.zip, 48995220 B, sha256 633e48f8206d38e345a83d66f7c704fb7f747128c49d8e11a103efed146e437c). Push to HPLaptop failed: machine unreachable.

## 5.33.274 THREELEVEL mock + old view options removed (Rob pt2094u "Mock the 3 level list. Be sure to remove old view types from options") — Nov 1 2026 ~6:55 PM ET
- Native Artists → Albums (artists/ID/) → album Songs; 270 merged hop already removed in bz_flip.py; bz_m13 now = any Artists songs list (L3).
- L2 artist albums full-height: bz_covercol clause 2 + `!$EXP[bz_artistalbums]`.
- Removed: DialogMusicInfo 9978 Album View (A/D), 9979 View Type (grid/album list/cover column); 9980 now focuses 9971. 6880 view pill music onclicks stripped (pill already hidden). bz_flip resets bz_albview_a + bz_grid_music at start.
- Open: L2 `..` above list top + ALL ALBUMS row floating. Smoke /workspace/b401/smoke_274_3level/. .py → FULL restart. Not zipped/pushed. Backup /workspace/b401/bak_5.33.274_previewopts_*.

## 5.33.275 L2ALLFIX + L3 NOTITLE (Rob pt2096u + steer "Keep all albums. Why is so far away?") — Nov 1 2026 ~7:00 PM ET
- ALL ALBUMS 6097 KEPT. Float cause: `bz_allpick` still included `[bz_artistalbums + bz_allrow]` (old cover-column disc-picker slides +390/+45/+N) → now `bz_allpick = bz_mdiscpick` only. Dropped the L2 +20 nudge on 6097. ALL ALBUMS now sits directly under the last album row.
- L2 `..` leak above list: allpull120 pulls list up 120 (.. + hidden *All) but `..` was not blanked → ALLHIDE2 groups get `!ListItem.IsParentFolder | !bz_artistalbums` (8 layouts). Back still goes up.
- L3 (bz_m13): regular 60px list — 75px m13 item/focused layouts disabled (condition `false`, parked in place); album header disc bar no longer drawn for bz_m13 (bz_discbar = TotalDiscs>1 + !bz_m13).
- XML only → ReloadSkin. Smoke /workspace/b401/smoke_275_l3_notitle/. Backup /workspace/b401/bak_5.33.274_pre275_*. Not zipped/pushed.


## 5.33.276 (Nov 1 2026)
- Rob: "take it all out, it never worked" — removed all no-art behavior: DefaultAlbumCover.png dropped from BzWarmMusicArt; idle big-album bz_noart60 fade and poster-window bz_vnoart fade removed; bz_noart60/bz_vnoart expressions deleted. Stand-ins: no live wiring remained in XML/scripts; extras/standins/ left on disk, never displayed. ReloadSkin.

- 2026-11-01 19:16 ET — 5.33.276 shipped/pushed: skin.bezel2-5.33.276.zip (32110811 B, sha256 d335cee0…47cf) → HPLaptop Downloads. All no-art paths removed. ReloadSkin.

## 5.33.277 FSMETA (Rob pt2142u "Build") — Nov 1 2026 ~8:30 PM ET
- 1121 Music Fanart FS: Music-meta block (small artist 150,196 / big album 150,226 / year+genre pills 150,296); on open year pill expands right into pill-shaped NP progress bar (600ms sine), genre fades. 6-cycle pill 6421 moved to FULLSCREEN-pill spot 140,136 (labels + cycle unchanged, per Rob steer). BezelNPInPlace old title/progress overlay hidden while 1121 visible.
- DEFERRED: list-in-strip (View_60_BezelInfoList shared by 5 windows, ~30 fixed 450px widths — own build), Music-section meta on fanart + FULLSCREEN 6886 move to fanart UL (collide with list 60 rows until strip list lands), album leaf flip across screens.
- Backup /workspace/b401/bak_5.33.276_pre277/. XML only → ReloadSkin. Not GUI-smoked (no audio decoder in box Kodi). Not zipped.

## 5.33.278 STRIPLIST + MUSICMETA (Rob pt2147u "Push when done") — Nov 1 2026 ~8:40 PM ET
- Music (artists/albums/songs, `$EXP[bz_mstrip]`): list 60 group + cover group + ALL row 6098 ride into colour strip 570..960 via Conditional zoom 86.67% (center 120,120) + slide 450 — layout only, nav/focus/MM warm/controls unchanged (Rob steer). L1 full list; L3 (covercol) cover above half list. Strip text (info pairs/bio) faded off under bz_mstrip.
- Music meta on BzCIStage fanart block: small line 150,196 (ARTIST / artist / artist · album), big ListItem.Label 150,226, year+genre pills y296 (disabled buttons, np_pill32).
- FULLSCREEN pill 6886 grouplist moved 786,136 → 140,136 (fanart UL), behaviour unchanged.
- FS 277 morph (1121) untouched. Leaf/fold untouched (fold sits on big album 1140,220, not moved).
- NOT done: L2 artist-albums album-above (would need bz_covercol change = list behaviour change, against steer). Touch hit on scaled list not verified. Not GUI-smoked.
- Backup /workspace/b401/bak_5.33.277_pre278. XML only → ReloadSkin.

- 5.33.279 (pt2150u) Wire MM/warm big-album leaf fold after 5 s; conflict cleared: idle_hinge ok() no longer requires HasFocus(60) under MM warm Music (6996/6897). Idle list hold stays 10 s. Fold look untouched; playing-anim parked.

## 5.33.280 (Nov 1 2026)
- Music L2/L3 half list (bz_mhalf → bz_covercol): small album at top of strip, list under it, no big strip title (BezelArtistMeta3B hidden). Strip slide 450→510.
- Meta = FS fanart format: small artist bz_mm18s, big title bz_mm34 uppercase, outlined pills np_pill32_ol.png (also in Custom_1121 year/genre).
- FULLSCREEN pill 6886: Left from list 60 (music strip, pill visible) → 6886; Left on 6886 → list 60 + open MM; Select unchanged (1121 when bz_m1121ok, else visualisation).
- Open: L2 ALL ALBUMS row 6097/6098 not shown in half-list mode.

## 5.33.281 WARMRAIL (Rob pt2174u) — Nov 1 2026 ~9:15 PM ET
- Music warm BG = same big-album rail family (6367/6377/6397/6382), unbroken. Cause: BezelMusicPlayingArt face A/B twin swap on bz_navmenu (fadetime 0 → 3000 MM twin) re-faded the album on MM open. Fix in place: section face un-gated; MM twin false (inside Player.HasAudio group). No new group.
- Dust: ambient BELOW + 1114 fade-under-MM skipped when Music list content is underlay. Glare already ungated.
- L2 ALL ALBUMS (6097 hidden by bz_covercol via bz_mhalf) — NOT fixed (row nav/allpick entangled), noted.
- Backup /workspace/b401/bak_5.33.280_pre281. XML only → ReloadSkin. Not zipped. Not GUI-smoked.

## 5.33.282 ALLHALF (Rob pt2178u) — Nov 1 2026 ~9:20 PM ET
- L2 ALL ALBUMS 6097 now shows in half-list (artist albums). Fix in place: new `bz_allhalf` = bz_mhalf + bz_artistalbums; 6097 visible `!covercol | allpick | allhalf`. Covercol rows are 75px from y450 (.. pulled 75) vs 6097 60/item stacking → +15/item (N 1–14) and −135 when `..` row, under bz_allhalf only. Lands flush under last album. L1 (not covercol) and L3 (allhalf false) untouched. Existing y1020 clip gate (≤6 rows) kept. 6098 (video) untouched.
- Backup /workspace/b401/bak_5.33.281_pre282. XML only → ReloadSkin (done). Not zipped. Not GUI-smoked on L2.
- 5.33.286 t2210/t2211: 1121 FS pill→bar zoom centre fix (0,16), extend 600→1200ms, bar opacity →60%.

- **5.33.288** (Rob t2214, Nov 1 2026): FS fanart 6-cycle pill 6421 — Select/Down on Controls no longer opens 1115; Select cycles Controls→Visualizer like other modes, Down → 6420.

## 5.33.291 — TV studio into pill (Rob t2223/t2224)
- TV L1 vstrip meta: studio text line removed; studio now a Bezel pill in the year/MPAA/genre row (tvshows only). TV clearart 150,200 430×92 above pills. ReloadSkin.
- Mocks /workspace/b401/mock_tv_l2l3/: L2 seasons plain half list (no season art), L3 episodes plain half list (no episode thumb); title/clearart carry L1–L3. Awaiting 👍.

## 5.33.300 docs — LEAF-FLIP own behaviour (Rob pt2265u) — Nov 1 2026 ~11:59 PM ET
- New behaviors/leaf-flip.md = leaf-flip family index (bz_hf_*, 1400 ms×2, slit x1440). Idle = live/locked (idle-big-album-fold.md), while-play next-song PARKED, FS stubs PLANNED. MUST NOT share rock/sway clock or bz_cov_side full flip.
- Cross-links: README index, idle-big-album-fold, sway-animations, music-list. Docs-only, no XML/py, no bump, no restart.

## 5.33.316 — SPLASH tighter mock built (Rob pt2395u) — Nov 2 2026 ~3:30 AM ET
- BezelWarmGate visuals replaced per /workspace/b401/mock_splash_315/splash_v2.png: near-black, one logo 280 @50% (80FFFFFF), BEZEL Montserrat-Bold 68 + dynamic version dimmer, bottom credit "Design by Robert Politano" 20px @50% + small US flag (us_flag.png regenerated 54×28, shown 27×14).
- Removed logoglow multiimage + logo pulse. Warm-gate timing/props/fade untouched. New fonts bz_splash68b/28m/20r. Backup /workspace/b401/bak_5.33.315_pre316. No zip/push.
- Fix: same visible gate on BezelAlbumCast outer grouplist (Includes_Bezel.xml). Docs: behaviors/sway-animations.md. ReloadSkin. Backup bak_5.33.317_pre318. Not zipped.

## 5.33.319 — Rob t2399 "Progress bar opacity 25" (Nov 2 2026)
- Custom_1121_MusicFanartFS.xml FS pill progress bar: ring/inner/fill colordiffuse 99 (~60%) → 40 (25%). No Tuner row existed (hardcoded). behaviors/music-fanart-fs.md updated. ReloadSkin. Backup bak_5.33.318_pre319. Not zipped.

## 5.33.320 — Rob t2402/t2403 "music stops in fullscreen, viz close → big album no art; doesn't heal" (Nov 2 2026)
- Cause: on stop bz_flip clears bz_cov_a/b and BezelBigArt falls to BezelPoster60, which only resolves Window.IsActive(music)+Container(60) art; after FS/viz close with no resolvable list art the 1122 big album had nothing, permanently.
- Fix: bz_flip saves last cover to Home bz_cov_last at stop; BezelBigArt falls back to it when no Music list art. Files: scripts/bz_flip.py, xml/Includes_Bezel.xml, behaviors/music-list.md. FULL restart. Backup bak_5.33.319_pre320. Not zipped.

## 5.33.321 — Rob t2408 "Ignore quick back presses at home" (Nov 2 2026)
- Cause: Home <home> keymap had no Back mapping → Kodi default Back = ShutdownMenu → Power 1118 on quick/CEC double Back during Home bounce.
- Fix: Back keys → noop in resources/keymaps/bezel2_np_tab.xml <home>. Docs keymaps.md + home-splash.md. FULL restart. Backup bak_5.33.320_pre321. Not zipped.

## 5.33.322 — Rob t2409 "Power menu needs two Down after open" (Nov 2 2026)
- Likely cause: onload SetFocus(7800,0,absolute) fired before the 6996->7800 hand-off finished and/or a pending bzpwrf close-alarm SetFocus(6996) landed after reopen, so first Down was spent re-focusing.
- Fix: Custom_1118 onload CancelAlarm(bzpwrf) + delayed AlarmClock re-assert of SetFocus(7800,0,absolute). behaviors/power-menu.md. ReloadSkin. Backup bak_5.33.321_pre322. Not zipped.
- **5.33.323** (Rob t2414 "Tv show watch flag get drawn in big album group"): xml/Includes_Bezel.xml poster-corner watched/resume badge group gated `!$EXP[bz_mmmushide]` (matched the frame next to it). Docs: behaviors/mm-warm.md. ReloadSkin. Backup bak_5.33.322_pre323/.
- 5.33.323 zipped (Rob t2418 "Build push"): /workspace/skin.bezel2-5.33.323.zip, 50.3 MB, sha256 500f3504…71f8e0; FULL restart after install.

- 5.33.344 (Nov 2 2026, t2489): MM FAVOURITES opened last section — ActivateWindow(Favourites) is not a Kodi 21 window name; now favouritesbrowser (bz_mm.py GO fav + Includes_Bezel ~496). FULL restart (.py). Not zipped.
- 5.33.345 t2490 TV pills clipped: VSTRIP meta pill grouplist width 400→780 (Includes_Bezel). ReloadSkin.
- 5.33.368 Rob t2636: Music NP + idle list art Python-mirrored (bz_m_np_art/bz_m_idle_art), dual preloaded big album, opacity on Player.HasAudio — FULL
- 2026-11-02 5.33.373 (Rob t2680): MM enter fade 400 ms sine out on BezelNavMenu chrome group (was 150 ms). Art lanes untouched (mirror-enter). XML → ReloadSkin. No zip. bak_5.33.372_pre373.

## 5.33.375 LEAFWAKE (Rob pt2688u, Nov 2 2026)
"Switch to new artist. Part of anim is running but not the flip. Looks like the glare or shadow moving only?" — Root: LEAFDIM (313) hides leaf groups under bz_lfdim but idle_hinge kept stepping bz_hf_ph, and 7 phase overlays (shadows, landing black) weren't dim-gated. Fix in place: Python dim() gate + XML !bz_lfdim on overlays. LEAFDIM intent kept (no fold in normal MM). FULL restart. Not zipped/smoked.

## 5.33.376 FANARTFADE (Rob t2692/t2693, Nov 2 2026)
"Did the new music list break the fanart fade?" / "fanart pop is carrying over into the section list" — Root: section fanart fadetime lost its `<!-- BETA 2.6 item 10` marker (was `5.0.3 #7` fadetime 0), so Tuner Fanart fade patch never hit. Fix in place: both section fadetimes → 200 + marker. Leaf 375 untouched. ReloadSkin. Not zipped. bak_5.33.375_pre376.

## 5.33.377 FSMATCH (Rob t2694u #1, Nov 2 2026)
"Fs fanart and fs fanart dialog are not same layout on fanart stage. Use the fs fanart dialog for style. Explain" — Root: 5.33.277 FSMETA restyle was built only inside 1121 (and NPInPlace overlay hidden only while 1121 visible), so MusicVisualisation kept the pre-277 layout. Kodi Fanart FS (MusicVisualisation) now uses the Music Fanart FS dialog 1121 fanart-stage layout: shared include BezelFSMeta (artist · album 150,196 / song title 150,226 / year pill→progress 150,296) mounted in both; BezelNPInPlace old title (150,162)/artist/album/progress (150,323)+time (729,305) hidden in viz; cycle pill 6391 moved 530,130 right → 140,136 left (NPInPlace params pillx/pilly/pillal), live shadow copies off in viz, "press down to open" hint 530,166 → 140,172. Keys unchanged. XML only - ReloadSkin. Queue #2/#3 not started.
- 5.33.379 (Nov 2 2026, Rob t2697): Info/Options blank art fixed — 1122 poster/album held while Info open (bz_flip hold + bz_railvis clause). FULL restart. Not zipped. Unsmoked.

- 5.33.385 (Nov 2 2026, Rob t2702 GO): DUALHOLD — separate last-Movies (`bz_v60_mov`) / last-TV (`bz_v60_tv`) poster holds; Music→Movies/TV + MM highlight fade up matching hold. FULL restart. Not zipped. Unsmoked.

## 5.33.386 — Rob t2705 (GO): whole-MM quick-tap ignore
- DONE: 6996 Select/Back/Left/Right gated on `bz_mmtap`; 400 ms latch (bz_flip `mm_tap`). Wake 0.5 s park on 6897 kept. FULL restart. Not zipped.

## 5.33.387 IDLEPARK (Rob t2714 "MM loses focus and doesn't hide on auto hide"): mm_idle hide step fixed in place. It did SetFocus(6897) then checked focus after only 50 ms; on Shield the park often wasn't focused yet, so bz_mmidle never set (no hide) and the late SetFocus then stranded focus on the invisible 6897 park (strip unfocused) with no retry. Now polls up to 1 s for the park; held -> hide (+clears any stray bz_mmtap); never held -> hand focus back to 6996 (_bzstrip). Also: if focus is found on 6897 with no hide armed (late SetFocus), the hide completes instead of stranding. 386 MMTAP latch unchanged. bz_flip.py only. FULL restart. Not zipped.

## 5.33.389 SETTINGS TREE (Rob t2725 "structure so one list can carry seamless? A tree")
- DONE: bz_setkids is now the root of a tree (bz_set_hub / bz_set_kodi / bz_set_tools); bz_flip `SETTINGS_TREE` mirrors it and builds `_SETKIDS`; `scripts/bz_tree_check.py` verifies sync. Same 15 windows, behavior unchanged. Tuner not added (pending Rob). FULL restart (.py). Not zipped.

## 5.33.391 SHARED ART SWAY CLOCK (Rob t2742 "DO IT")
- DONE: poster sway (bz_pswayon/bz_ppulse) now anchored to the album sway grid (t0+7.4+k*24.5 s) via bz_flip `_art_sw_anchor`; free-running epoch when no music; Home `bz_art_t0`. XML anims untouched (look, glares, casts, leaf-flip unchanged). FULL restart (.py). Not zipped.

## 5.33.394 A2PFADE (Rob t2778 "Ok give tuner for a2p")
- DONE: Tuner slider ALBUM / POSTER > Poster ↔ album fade (`bz_at_a2pfade` 1–7 = 200/250/300/**400**/500/600/800 ms) drives 6401, 6402 and handoff pre-warm fades in Custom_1122. Reset album -> 400. ReloadSkin. Not zipped.
- 5.33.396 (Rob t2785u) SETHOLD: no UADVRAND random step while the MM strip is on the SETTINGS row; held art fixed through auto-hide/wake. bz_flip.py under_adv.
- 5.33.397 (Rob t2789-t2793) MMAUDIO: big album on every MM row while audio plays (bz_mmaudio in bz_railvis / bz_artposter).

## 5.33.398 NOAUTOHIDE (Rob t2799u "Rip out the mm autohide") — Nov 2 2026 ~9:40 PM ET
- Removed MM auto-hide entirely: bz_flip.py mm_idle thread (30 s → SetFocus 6897 → bz_mmidle, WAKEGRACE, IDLEPARK) deleted; IDLERESET wake edge in under_adv deleted; mm_warm 6897/bz_mmidle skip deleted; idle_hinge mmw/dim no longer reference 6897/bz_mmidle. Startup clears stale bz_mmidle/bz_mmidle_set.
- Includes_Bezel: 6894 visible/hide-fade gate removed; park button 6897, PRESS ANY BUTTON idle label and auto-hide clearart stage removed; colour backdrop idle fade removed; BezelSecDim mmdim and bz_lfdim no longer special-case bz_mmidle.
- Tuner: MAIN MENU › Auto-hide menu row, BzATVal_mmidle, its L/R handlers and media/bezel/info/mm_autohide.png removed.
- Behaviors mm-list / mm-warm / artwork-group / skin-settings-tuner updated. Backup /workspace/b401/bak_5.33.397_pre398. .py → FULL restart. No zip/push.

## 5.33.399 — ONEART (Rob t2807–t2814) · FULL restart · zipped with 400
- MS 1117 empty poster fixed (poster stack Visible=bz_pready → opacity via $EXP[bz_pshow]; setkids hold last bz_v60_art).
- All art-lane Visible remounts → Conditional opacity (Includes_Bezel 17, Includes_BezelDialogs 5, 1117 2, MyPics 2+1 group); 4 dead visible=false art images removed.
- Smoke (flatpak bwrap): Videos→1117 poster shown (bz_vpl_on=1, art held); Videos poster OK. MM-open/audio paths not smoked.

## 5.33.400 — STRESSFIX (Rob stress 399 → Push) · FULL restart · zipped/pushed
- F1 MS Back→MEDIA SOURCES row (msret latch + bz_msretrow). PASS.
- F3 Recently Played Back→RECENTLY PLAYED row (FolderPath musicdb://recentlyplayed → 6905). PASS.
- F2 Music→Movies stale poster: lanes + v60 dualpick/dualrec hold while bz_mmwarm. Residual: first Movies visit of a session with no Movies hold can blip last TV poster ~0.4s (parked).
- Stress baseline from 399 otherwise kept. Backup bak_5.33.399_pre400/.


## 5.33.401 — UADVFOCUS (Rob t2864 "Don’t mm background scroll on section list60 unless focus on MM row") · FULL restart · not zipped
- `under_adv` UADVRAND now requires `Control.HasFocus(6996)`. If focus leaves the MM strip, random pauses and the last list-60 / warm art stays held.
- Still paused for: MM closed, mmstart, mmwarm, Tuner/settings/submenu, uadv_off, SETTINGS row (396 SETHOLD), modal/busy, <2 items.
- Backup bak_5.33.400_pre401/.


## 5.33.408 NOROCK/SWAYSTART (Nov 3 2026, Rob t2914u)
"DISABLE ALBUM ROCK, I JUST WANT SWAY. START POSTER AND ALBUM SWAY ON STARTUP" — idle album 2D rock (±4° rotate) replaced in place by album rotatey sway on bz_big_go/bz_big_pulse (armed at Home startup); Tuner Idle rock row removed; poster sway anchor armed at poster_clock thread start. Files: addon.xml, xml/Includes_Bezel.xml, xml/Includes_Tuner.xml, scripts/bz_flip.py, behaviors/sway-animations.md, leaf-flip.md, idle-big-album-fold.md. FULL restart. Not zipped.

- 5.33.409 NOAUTOVIZ (Rob pt2915u, Nov 3 2026): Music Select popped Kodi stock fullscreen viz. Cause: Kodi setting musicfiles.selectaction (Switch to visualisation on playback) on. Fix: bz_dustviz.py startup forces it off. FULL restart. Follow-up queued: list highlight bar flash on return from FS.


## 5.33.411 NOIDLEFS (2026-11-03)
Removed the 30 s idle auto-open of Dialogue FS (1120) from bz_flip.py and its Tuner row (FULLSCREEN MUSIC > Open after 30 s idle). Fullscreen music opens ONLY on explicit Select. bz_fsauto_off is now dead. NOAUTOVIZ (409, musicfiles.selectaction forced off) kept.

## 5.33.414 GLAREONE (2026-11-03, Rob t2929u)
Album glare restored to ONE static 600x600 texture (art_mask.png) over the idle big album — GLARESPLIT 300x600 halves (art_mask_hl/hr) removed from static + leaf groups. Sweep (5 s go) + 8.5 s pulse pair, zoom/fade/sway unchanged. Whole glare hidden during hinge fold (bz_hf_a). Cover single when leaf off.

## 5.33.420 MODALGUARD (2026-11-03, Rob t2944u/t2945u)
DialogConfirm focus steal fixed: bz_flip `_modal_blocks_strip()` gates all SetFocus(6996)/_bzstrip reclaim (MM-start, open-MM, warm bounces, mini-player) while HasModalDialog/yesnodialog; bz_warmgate bounce guarded. Keep-skin + everyday Yes/No get focus. FULL restart.

- 5.33.421 IDLEGLARE (Rob t2958u, Nov 3 2026): idle glare pulse fades 8500→12250 ms to sync with idle sway. ReloadSkin.
