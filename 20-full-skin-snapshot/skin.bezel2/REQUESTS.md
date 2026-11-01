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
