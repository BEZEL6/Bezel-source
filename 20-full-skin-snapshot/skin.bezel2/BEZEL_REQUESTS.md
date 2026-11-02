- 5.33.41: Fullscreen Music Clearart Tuner row moved out of DUST to ALBUM / POSTER, right under Preset (ALBUM open only). Desc updated for static logo. (2026-10-29 19:24)
- 5.33.42: FULLSCREEN MUSIC Tuner split into groups CHROME (opacity, colour, reset) / VIZ (viz opacity) / CLEARART (mclogo toggle). Clearart moved out of ALBUM. (2026-10-29 19:25)

## 5.33.60 (Oct 29 2026) t398-t404 REBUILT (t395 focus-audit edits REVERTED to 5.33.59 bounce)
- Power 1118: TUNER (blue FF7ACAFE, id 7801) below separator, BEZEL version under it. Opens Tuner (bz_tunesrc=pwr, clears navbez/navset, 1118 onunload skips 6996 focus). Tuner Back -> reopens Power.
- Nav-right Tuner removed (BEZEL subpanel item gone); Right-from-Settings still opens BEZEL subpanel w/o Tuner.
- MM: MUSIC VIDEOS + PLAYLISTS removed. Settings focused row: divider/logo/› extras removed.
- Music FS controls 1115: TUNER row 6413 (blue) above Close; bz_tunesrc=fsctrl, Back -> visualisation + 1115. Music only.
- bz_nav kept on Power->Tuner (Tuner group visible requires $EXP[bz_navmenu]). XML only -> ReloadSkin.

## 5.33.64 — Play Next fullscreen Music (Rob t416–t426)
- Skin.String bz_fs_layout = playnext → Play Next; empty = Big Album (default).
- Tuner FULLSCREEN MUSIC › "Play Next" row (OK toggles BIG ALBUM / PLAY NEXT).
- New include BezelFSPlayNext (prev 57 / now 660 / next 1263 @ y220, 600px, 3px gaps, bz_frame_soft bezel, pn_cast.png cast from centre, fadetime 800 crossfade, title/artist overlay via MusicPlayer.offset(±1)).
- Centre = existing BezelMusicPlayingArt slid −480 (same sway/effects); NP panel faded to 0 but 6390 keeps OK play/pause + Left/Right prev/next; clearlogo hidden in Play Next.
- Compact NP bar extracted to shared include BezelNPCompactBar (Music list + Play Next, dx −380).
- Backup /workspace/b401/skin.bezel2-5.33.63-prePlayNext. No zip. ReloadSkin.
- t428: side albums fade in 3 s after 3 s delay (Visible + WindowOpen); centre + NP bar immediate.

## 5.33.67 (t445)
- 1120 Play Next: focus 6400 Left=PlayerControl(Previous), Right=PlayerControl(Next); Back/Esc onback Close. Verified present; Music list Right (1120 closed) unchanged.

## 5.33.68 — t447 Play Next → Dialogue FS (labels only)
- Tuner FULLSCREEN MUSIC item label "Play Next" → "Dialogue FS"; value PLAY NEXT → DIALOGUE FS; desc updated.
- Comments "Play Next dialog" → "Dialogue FS dialog". Internal ids kept: window 1120, Custom_1120_PlayNext.xml, bz_fs_layout=playnext, BezelFSPlayNext, bz_pndlg_*.

## 5.33.70 (Rob t458–t462) — Dialogue FS big album pill
- Custom_1120: upper-right **big album pill** 6401 (clone chrome of fan art pill 6391: np_pill32 border16 h32 bz_b15 BzFSCTint/50/80). Label ALBUM / PREV/NEXT.
- Skin.String bz_dfs_mode: `album` = side albums fade out (800 ms); empty = PREV/NEXT (sides shown). Center album (Music window art) untouched, no anim restart.
- 6400 Up → pill; pill Select/Left/Right cycle; Down/Up → 6400; Back closes. 6400 L/R prev/next + Back unchanged.
- BezelFSPlayNext gained param `sides` (default true; Kodi FS unaffected).

- 5.33.76 (t507): undo 5.33.75 Movie Info fanart-block move (restored DialogVideoInfo + Includes_BezelInfo from 5.33.74 bak). Confirm-in-fanart-block MOCK only.

## 5.33.106 (Oct 30 2026, t718) slide smoke fixes: side Visible anim no longer re-delays 5s on track change (WindowOpen keeps 5s slide); Music player controls/timer fade under 1120; ‹ › direction arrows on side album labels (both 1120+viz). Open: double cover behind center (not reproduced in code). Not smoked.
- 5.33.106 t721: centre overlay/buttons (6402-6404, dim, logo) wrapped in sway group mirroring centre album rotatey (centre 960, camera 960,520).

## 5.33.107 (Oct 30 2026, t721 Rob pick) 1120 centre dim/logo/prev-pause-next visuals moved into BezelMusicPlayingArt centre sway group (left 1140 pre-slide, visible Window.IsActive(1120)); mirrored .106 sway removed. 6402-6404 stay focusable in 1120 (transparent via BzPN107Nof/Foc), onfocus sets bz_pnfoc → Music copy highlights. Viz keeps its own overlay (!1120). Not smoked.

## 5.33.108 (2026-10-30, t726/t732/t733)
- 1120: Music "double-tap info › controls" hint gated `!Window.IsActive(1120)` (bled under FS).
- 1120: prev/pause/next highlight now keyed on home prop bz_pnfoc only (Control.HasFocus is cross-window = never true from Music window); cleared on 6400/6401 focus + 1120 unload.
- Viz play-next: Back (backspace/browser_back/remote back -> SetFocus(6297)) sets home bz_pnoff=1 -> play-next chrome off, stay in viz FS (stage slides home via Conditional reverse). Esc = Back action = sides fade, stage slide home, exit FS. All playnext conditions now `+ !bz_pnoff`; cleared on viz unload. Keymap change needs bz_cmd keymap reinstall.
- Overlay FX all Off: defaults empty; code audit + 1120 shots show normal chrome, no FX bleed.
- Smoke :133: 1120 sides/single cover/single timer/sway overlay/fade-then-slide Back PASS (.107 shots slide_107). Viz Back/Esc NOT live-verified (test Kodi won't hold visualisation window).

## 5.33.109 (Oct 30 2026, Rob path review t750–t761)
- 1120 Dialogue FS: sides sdelay 3000 + new sfade param 2000 (fade/slide 2 s, ends with 5 s centre slide). Album pill unchanged (no sides).
- Controls overlay (1120 BzPN107 + viz 6402-6404) hidden until Select focuses a button (bz_pnfoc); 6390 focus clears it.
- Timers bz_1120_autoclose: audio stop = Step 5 Back path (bz_fsret latch + close).
- bz_dfs_mode empty -> album on 1120 open and viz open.
- Viz: open lands in fanart FS (bz_pnoff=1); double-tap Select on 6390 (bz_vdtap, 1 s) clears bz_pnoff -> Play Next; single tap = play/pause after 1 s. Back from Play Next -> fanart FS (sides Hidden fade 600, stage Conditional reverse). Esc = Back action = exit FS (unchanged).
- t761 list top: bz_flip.py no longer SetFocus(60,last) before ALL row (visible jump to last); stores bz_allup, ALL 6097/6098 onup restores it.
- Backup: /workspace/bezel-533-fork/rebuild/bak_5.33.108_pre109

- 5.33.110 (Rob t780): strip cast shadow quick fade-out 250ms on Dialogue FS (1120)/Play Next trigger (was 800ms reversible); fade back in 600ms on close. Includes_Bezel.xml x4.
- t781/t782 audit (Oct 30): cast coords 485,230 480x580, zoom/slide centre 965,520 identical bak_5.33.80 → .108 → .109 → .110. No position drift in XML; no edit.

## 5.33.112 (Oct 30 2026) — t786
- Cause: 1120 onunload -> SetFocus(6398) (grouplist scroll-home button) whose onfocus forwarded to NP block 6390, so focus stuck on NP/controls. Now 6398 -> list 60 (6996 if MM open). Viz Play Next exit: onunload AlarmClock SetFocus(60) (gated !bz_navmenu). t783/t784 already in .111. t785 Overlay FX deferred. Backup ../bak_5.33.111_pre112_t786. XML only -> ReloadSkin.
- 5.33.127 (Rob t909/t913 parked .125 bugs): (1) strip cast fade-out on 1120/viz never ran — 4 fade animations were self-closed with condition but no type; now type Conditional (fade 250 out / 600 back). (2) Play Next side pn_cast gated on offset(±1) Cover too — no stub cast without real cover. (3) NP centre: verified centred on album (1140–1740, t885); no change. (4) Up-next (right) side labels align right. Backup rebuild/bak_5.33.126_pre127. XML → ReloadSkin.

## 5.33.261 — GLAREFOLD (Rob t1946u / t1947u)
- Static full-album 600x600 glare (above hinge) now `<visible>String.IsEmpty(Window(Home).Property(bz_hf_ph))</visible>` + 400 ms sine Visible fade-in; removed ph1 Conditional fade (which faded back in mid-ph2).
- Added 300x600 half glare (BzATGlareTex / BzATGlare8C) inside ph1 leaf group (right half of A) and ph2 landing leaf group (left half of B, flipx) so glare rotates with the page.

- 5.33.303 (t2294u): Tuner MAPS section + Music screen map pages 1–5 (mapmusic1–5), big right panel 1000,210 880x810. XML only, ReloadSkin. Not zipped.
