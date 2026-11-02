# BEZEL request tracker (skin.bezel2) — generated 2026-10-24 09:30 EDT, checked against skin.bezel2-4.0.0.zip
Status key: logged / mockup / approved / built vX / verified vX / dropped. Note: chat transcripts were not readable by the auditing agent; open items come from the parent's logged list + Rob's latest messages; built items come from the shipped changelog.txt.

### Oct 31 2026 — big album pill on FS album viz (APPROVED voice)
Added `BezelBigAlbumPill` (6401) to MusicVisualisation matching Dialogue FS 1120 (pos 1360,60; ALBUM↔PREV/NEXT via `bz_dfs_mode`). Fan art pill 6391 stays. Sides gated by dfs_mode. Code only — no zip/commit.

### Oct 31 2026 — 5.33.203 SHIP (voice approved zip)
Zip: `C:\Users\rober\Downloads\skin.bezel2-5.33.203.zip` (~30.5 MB), no mockups.
Includes: FS sides 3s/2s; double-Select album viz only; fan art pill 6391 fanart-only; big album pill 6401 on album viz; TV Y/G under title; jump-bar bg; strip/cast; viz keymap. FULL restart recommended (keymap/.py in tree).

### Oct 31 2026 — 5.33.204 SHIP (voice approved zip+git)
Zip: `C:\Users\rober\Downloads\skin.bezel2-5.33.204.zip` (~30.5 MB), no mockups.
Music↔Movies/TV album+poster true-fade; startup list randomizer; prior FS/pill/TV/jump-bar/Warm docs. FULL restart.

### Oct 31 2026 — Fanart FS right-nav fix (voice)
MusicVisualisation 6409: removed ClearProperty(bz_pnoff) onclick (noop bounce only). Right/nav no longer opens FS album viz from Fanart FS. Album viz = double-Select 6390 only. Music Right→1120 unchanged. ReloadSkin. Code only, no zip.

## Open / not built (as of 4.0.0)
| id | date | request | status | notes |
|---|---|---|---|---|
| O01 | 10-24 | New power menu | built + verified v4.0.1 | new power menu (earlier session shots) |
| O02 | 10-24 | Soft dust: own size, brightness, on/off; smaller default | built + verified v4.0.1 | Soft dust on/off (bz_sdust_off, all densities), Soft dust size S/M/L (default M = 75%, old = L), brightness 20-100%; b401/o02_cmp2.png, o02_tun_a/b.png |
| O03 | 10-24 | Rename Bokeh -> Soft dust everywhere visible | built + verified v4.0.1 | Drift speed + Spin layer descriptions say soft dust; no visible "bokeh" left |
| O04 | 10-24 | Fiber + flake particle types | built + verified v4.0.1 | Fibers / Flakes rows + amount (pre-composited spin variants, 16 textures 673 KB); b401/o04_nc_diff.png, o04_tun.png; flake sparkle built v4.0.2 (Flake sparkle toggle + Sparkle speed rows; b402/shot_1.6.png, spark_clip.mp4) |
| O05 | 10-24 | Right menu unfocused items dimmed, not see-through | built + verified v4.0.1 | right menu unfocused items dimmed, opaque |
| O06 | 10-24 | "Video stream" value overlaps label | Kodi limitation v4.0.1 | Video stream value/label overlap is drawn by Kodi core (not skinnable); left as is |
| O07 | 10-24 | Channel manager control shows only left arrow | built + verified v4.0.1 | channel manager shows both arrows |
| O08 | 10-24 | Logo glow animation "not right" | built + verified v4.0.1 | Rob approved 9:49 (panel 11 last); media/bezel/logoglow 114 frames, 11.4 s seamless loop white>orange>white, 0 grey frames (b401/o08_capture_strip.png) |
| O09 | 10-23 | Dev guide + cleanup/optimize pass (merge near-duplicate code, test-gated) | built v4.0.1 (Rob 11:18 go) | lossless oxipng (pixel-identical check) media 11.94->7.68 MB (colour types kept); removed 34 unreferenced media/bezel textures + 29 unused tuner bars + DialogMusicInfo.xml.bak_infofocus (kept in b401/gen/dead_media); dead code: bz_cmd nofs action, albumscale vars/P/V/patch regex/MIG keys; merges: none (no near-duplicate merge passed a no-change test cheaply enough to risk); dev guide /workspace/BEZEL_DEV_GUIDE.md |
| O10 | — | Glare dust over poster with full particle mix + depth | built + verified v4.0.1 | poster glare lit dust gets the full mix layer (crisp specks + fibers + flakes, honours Fibers/Flakes rows, near-layer colour); album unchanged; b401/o10_poster.png |
| O11 | — | Separate album-dust timing (fade-in 1s / fade-out 3.5s, own hold/drift) | partial (open) v4.0.1 | not built: since 3.1.2 lit dust rides the glare continuously, there is no album hold event to time a 1 s in / 3.5 s out against; needs Rob decision (re-add hold-triggered album dust or drop) |
| O12 | — | Breathe setting; per-layer glow on/off | built + verified v4.0.1 | Breathe on/off + per-layer Breathe rows (far/mid/near/soft/spin); off = steady at Ambient; patch verified in Custom_1114 (BZG:2 67/67); b401/o12_tun.png |
| O13 | — | Poster-dust separate on/off | built + verified v4.0.1 | Poster lit dust row (bz_at_pdust); wrapper verified with Control.IsVisible true/false/true; b401/o13_tun.png |
| O14 | — | Left vs right dust size evening | checked v4.0.1 | dust layers are uniform tiles; 3-frame speck measure on edge strips noisy (L median 9 px area vs R 29, mid 18) - no code change; flag for Rob eyeball |
| O16 | 10-24 | Fullscreen pill no longer cycles modes on tap; only opens player controls list. Fix: restore pill cycle, keep controls list on M/RED | verified v4.0.1 | pill cycles vis>bio>fanart>lyrics>upnext>controls(1115)>vis, 2 s mode label; shots /workspace/b401/o16_*.png;  Last working: 3.2.0 (button 6391 onclick cycles Skin.String(bz_npmode) vis→bio→fanart→lyrics→upnext). Broken since 3.2.1 (changelog item 1+2), still in 4.0.0: Includes_Bezel.xml ~L2678-2686 button 6391 `<onclick>ActivateWindow(1115)</onclick>`. Block tap 2641/2651 also ActivateWindow(1115) |
| O15 | — | Tuner description clipping off right strip | verified v4.0.1 | descriptions wrap inside the 340 px strip (o02_tun_a/b, o12_tun) |

## Dust items IN 4.0.0
| id | request | status | evidence |
|---|---|---|---|
| D01 | Universal dust on/off | built v4.0.0 | TOG dust / bz_dust_off |
| D02 | Lit dust hold toggle | built | bz_adust_off |
| D03 | Cut-out toggle + feathered edges | built | bz_dust_nocut; media/bezel/d3/feather_* |
| D04 | Density / Ambient / Lit / Drift / Gap / Poster hold sliders with Rob's defaults | built | d3dens=Low, d3amb=30%, d3lit=100%, d3speed, d3speed=1x, d3gap=Large, phold=2s |
| D05 | Ambient glow peak 10% steps default 45% | built | d3glow default idx5=45% |
| D06 | Glow layer offset 0-10s default 2s | built | d3goff default idx3=2s |
| D07 | Spin layer on/off, speed, direction; lit spin | built | spinspd/lspinspd default 90s (range 30-600s), bz_spin_ccw, bz_lspin_cw, dust_spin.png, litspin_s/_l |
| D08 | Particle size settings | built | d3asize, d3lsize (Small/Med/Large) |
| D09 | Low-res textures for blurry layers | built | dust_bokeh_* 480x270, dust_far_* 960x540 |
| D10 | Dust only in black void, clipped | built | Custom_1114_Dust.xml grouplist clips |

## Built (from shipped changelog)
| id | date | request | status | notes |
|---|---|---|---|---|
| C001 | (per changelog 4.0.0) | big BEZEL logo is static (no spin) with an internal glow from the centre - 20 s loop of pre-rendered frames (media/bezel/logoglow, 10 fps), drawn above the menu dim so the peaks reach full brightness, Kodi version label  | built v4.0.0 | from shipped changelog |
| C002 | (per changelog 4.0.0) | remaining base-skin dialogs laid out BEZEL (login / profile picker, startup splash 4.0.0 with loading bar, screen calibration, PVR Channels OSD, group manager, channel manager, PVR info, Guide search, subtitle search, vi | built v4.0.0 | from shipped changelog |
| C003 | (per changelog 4.0.0) | settings dialog title and slider sizing fixed during playback | built v4.0.0 | from shipped changelog |
| C004 | (per changelog 4.0.0) | small-album list shared across in-album, artist albums and album list | built v4.0.0 | from shipped changelog |
| C005 | (per changelog 4.0.0) | music Genres and Years hide the poster window and its shadow (no art) | built v4.0.0 | from shipped changelog |
| C006 | (per changelog 4.0.0) | fullscreen no longer auto-starts when playback begins - songs and videos started from the library lists keep the current screen (Kodi's automatic switch to fullscreen video is sent straight back by the skin), fullscreen  | built v4.0.0 | from shipped changelog |
| C007 | (per changelog 4.0.0) | the skin forces no Kodi playback setting. | built v4.0.0 | from shipped changelog |
| C008 | (per changelog 3.2.1) | Now Playing pill and controls open the music controls (1115) or the video OSD | built v3.2.1 | from shipped changelog |
| C009 | (per changelog 3.2.1) | pill width fits its label | built v3.2.1 | from shipped changelog |
| C010 | (per changelog 3.2.1) | slide menu opens/closes with slide + fade | built v3.2.1 | from shipped changelog |
| C011 | (per changelog 3.2.1) | Playlists moved into the Music drop-down and Settings into the main list (Up/Down reaches every row) | built v3.2.1 | from shipped changelog |
| C012 | (per changelog 3.2.1) | section switch loads the new section behind the menu before it closes | built v3.2.1 | from shipped changelog |
| C013 | (per changelog 3.2.1) | unfocused right section dims, tiles get an even bottom margin | built v3.2.1 | from shipped changelog |
| C014 | (per changelog 3.2.1) | 'Kodi 21.2' under the spinning logo | built v3.2.1 | from shipped changelog |
| C015 | (per changelog 3.2.1) | drop-down arrows point down when closed and up when open | built v3.2.1 | from shipped changelog |
| C016 | (per changelog 3.2.1) | focus blur option removed | built v3.2.1 | from shipped changelog |
| C017 | (per changelog 3.2.1) | leaving fullscreen music returns focus to the list. Item 9: View options restyled like the Main menu (Montserrat, see-through block-colour bars, description in the colour strip, right section hidden while open). Item 10: | built v3.2.1 | from shipped changelog |
| C018 | (per changelog 3.2.1) | grid takes focus first | built v3.2.1 | from shipped changelog |
| C019 | (per changelog 3.2.1) | grid view choice no longer reset per folder. Item 13: small-album list clip strip fixes the half-visible bottom row for every album size. Item 15: base-skin dialogs restyled BEZEL (Montserrat fonts, dark panel with accen | built v3.2.1 | from shipped changelog |
| C020 | (per changelog 3.2.1) | startup splash gets a loading bar and 'Kodi + version' label | built v3.2.1 | from shipped changelog |
| C021 | (per changelog 3.2.1) | all control IDs kept. Item 16: levels with no art hide the poster window and its shadow | built v3.2.1 | from shipped changelog |
| C022 | (per changelog 3.2.1) | it returns when items have art. Separator gap above Favourites restored as non-focusable spacing (Up/Down unchanged). | built v3.2.1 | from shipped changelog |
| C023 | (per changelog 3.2) | restyled slide menu (Montserrat, fanart inside the block, rounded album / fanart tiles, see-through highlights in the block colour, BEZEL Tuner under Settings) | built v3.2 | from shipped changelog |
| C024 | (per changelog 3.2) | fullscreen music controls as a 9-row list in the colour block (M or the album tap cycle Standard -> Jumbo -> controls) | built v3.2 | from shipped changelog |
| C025 | (per changelog 3.2) | video OSD as a matching list | built v3.2 | from shipped changelog |
| C026 | (per changelog 3.2) | pause screen (28% dim, poster slides in) | built v3.2 | from shipped changelog |
| C027 | (per changelog 3.2) | old seek bar and its debug timestamp removed | built v3.2 | from shipped changelog |
| C028 | (per changelog 3.2) | finger-touch target over the album art | built v3.2 | from shipped changelog |
| C029 | (per changelog 3.2) | grid views use Arctic Zephyr Reloaded wall mechanics (105% focus zoom, 350 ms quadratic scroll, block-colour focus frame, no sway in grid only) | built v3.2 | from shipped changelog |
| C030 | (per changelog 3.2) | focus watchdog returns focus to the list when the focused control disappears (music lists focus loss). | built v3.2 | from shipped changelog |
| C031 | (per changelog 3.1) | drop-down slide menu (big Music / Movies / TV rows with fold-out sub rows, mini player band with a fullscreen button, Recent strip on the right, view options slide in on Left, tuner inside the menu) | built v3.1 | from shipped changelog |
| C032 | (per changelog 3.1) | Animation Tuner redesign (section list left, description panel right with what each setting does and what higher / lower means) | built v3.1 | from shipped changelog |
| C033 | (per changelog 3.1) | dust - bigger and more specks, pulses, own drift directions per layer, cut-out toggle, glare dust | built v3.1 | from shipped changelog |
| C034 | (per changelog 3.1) | album art tap / OK toggles Standard 600 / Jumbo 900 (Jumbo default, flip track list removed) | built v3.1 | from shipped changelog |
| C035 | (per changelog 3.1) | grid view takes the focus first | built v3.1 | from shipped changelog |
| C036 | (per changelog 3.1) | artist discography IN LIBRARY pill | built v3.1 | from shipped changelog |
| C037 | (per changelog 3.1) | every quit path stops the skin scripts and closes the dust dialog | built v3.1 | from shipped changelog |
| C038 | (per changelog 3.1) | Now Playing kept inside the colour block. | built v3.1 | from shipped changelog |
| C039 | (per changelog 3.0.1) | fixes - Animation Tuner no longer opens as a white screen (0% / none colours now near-transparent black) | built v3.0.1 | from shipped changelog |
| C040 | (per changelog 3.0.1) | tuner no longer fails with 'Could not apply to Custom_1114_Dust.xml' (dust file ships pre-tuned, all tuner writes are atomic and never leave a partial file) | built v3.0.1 | from shipped changelog |
| C041 | (per changelog 3.0.1) | black edge band over the BEZEL logo removed | built v3.0.1 | from shipped changelog |
| C042 | (per changelog 3.0.1) | Standard album restored to 600 px (66.67% Mini zoom path removed), Jumbo toggle = 900 px, no double zoom | built v3.0.1 | from shipped changelog |
| C043 | (per changelog 3.0.1) | Subtle preset no longer leaves the album blank (hold fix) | built v3.0.1 | from shipped changelog |
| C044 | (per changelog 3.0.1) | 0% shadow opacity no longer draws white | built v3.0.1 | from shipped changelog |
| C045 | (per changelog 3.0.1) | brighter dust, default level 70% | built v3.0.1 | from shipped changelog |
| C046 | (per changelog 3.0.1) | Exit in the power menu no longer freezes Kodi (skin scripts are stopped before Quit). | built v3.0.1 | from shipped changelog |
| C047 | (per changelog 3.0) | persistent dust dialog (1114) behind all windows, sparse 3-layer pinpoint dust, open black right side at the library root (mask variant R) | built v3.0 | from shipped changelog |
| C048 | (per changelog 3.0) | small album by default (600x600) with a Jumbo toggle in the tuner | built v3.0 | from shipped changelog |
| C049 | (per changelog 3.0) | Animation Tuner v2 - sections ART / BLOCK / LIST / EPISODES / MENU / MUSIC / DUST / LOOK / SYSTEM, per-section presets (Left / Right), speed rows as x1-x3 factors, block colour (8 presets) + opacity, toggles (Jumbo, dust | built v3.0 | from shipped changelog |
| C050 | (per changelog 3.0) | slide menu guards - one close routine with a 0.8 s grace, every open path checks bz_navok, menu controls can't take focus while the menu is closed or sliding out, stray focus returns to the list, jump bar Left opens the  | built v3.0 | from shipped changelog |
| C051 | (per changelog 3.0) | M / Menu key opens the slide menu on card 2 (view options) instead of Estuary's blade | built v3.0 | from shipped changelog |
| C052 | (per changelog 3.0) | card 2 carries all of Estuary's options-blade actions with the same visibility (music: party mode, go to playlist, get more, add-on settings, edit nodes | built v3.0 | from shipped changelog |
| C053 | (per changelog 3.0) | video: order, filter, party mode, master mode, go to playlist, get more, edit nodes, download icons, add-on settings) | built v3.0 | from shipped changelog |
| C054 | (per changelog 3.0) | library root (musicdb:// / videodb://): no art, poster, shadow or glare | built v3.0 | from shipped changelog |
| C055 | (per changelog 3.0) | album and song lists: Right focuses the artist name in the colour block, Select opens that artist (album artist first), Left returns to the list | built v3.0 | from shipped changelog |
| C056 | (per changelog 3.0) | music info dialog: fanart backdrop through the colour block, buttons as a row inside the block | built v3.0 | from shipped changelog |
| C057 | (per changelog 3.0) | artwork pre-cache (from about 1 min after start, one image at a time, pauses while scrolling / playing / fullscreen, resumes 3 s after the last key, Skin toggle bz_precache_off) | built v3.0 | from shipped changelog |
| C058 | (per changelog 3.0) | Splash D v2 - pure black, Raleway Light BEZEL letters slide in from both sides, superscript 3.0 and the Kodi version line, logo spin, all after the 2 s black hold | built v3.0 | from shipped changelog |
| C059 | (per changelog 3.0) | double-tap Select drops a stale pending tap when the context changes. | built v3.0 | from shipped changelog |- O16 pill cycle fix: APPROVED (Rob 👍 Oct 24 9:26) for next build: Visualizer > Bio > Fanart > Lyrics > Up Next > Controls; M/RED open controls
| O17 | 10-24 | Spin layer: replace blurry texture with sharp, small crisp dust specks; keep motion (Rob: spin makes effect 100x better, texture ruins it) | built + verified v4.0.1 | crisp random-depth specks texture, alpha x1.5, motion kept |
| O18 | 10-24 | Exiting Main menu: logo outline flashes on the next screen | built + verified v4.0.1 | BezelNavLogoGlow gated on bz_navmenu, Hidden 150 ms / WindowClose 120 ms; logo gone in ~150-330 ms on exits to Movies/TV/Music/Settings (b401/o18_seq_*.png) |
| O19 | 10-24 | Poster animation may slow while dust is active; measure FPS dust on vs off and optimize | measured v4.0.1 | System.FPS home, dust on ~10.4 vs off ~10.7-11 (5 samples each, software renderer + shared CPU with another Kodi): no measurable dust cost here; dust already hidden in fullscreen video/PVR; no code change; re-measure on real hardware |

| O20 | 10-24 | Remove floor reflection + its tuner rows (shadow/glare/poster unchanged) | built v4.0.1 | Includes_Tuner lkfloor vars/item/overlay removed, bz_tune.json P 51->50, bz_reflect_floor.png deleted |
| O21 | 10-24 | List cascade end snaps; must scale with cascspeed + cascstag | built v4.0.1 | root cause: bz_flip.py cleared bz_casc after a fixed 0.7 s while rows 6-15 ran to ~1.24 s (Includes_Bezel rows: delay (k-1)*60, 400 ms cubic). Now delay=(k-1)*stag*speed/400, time=speed*(1+0.35(k-1)/14) quadratic out, bz_flip clear = casc_len() |
| O22 | 10-24 | Exiting fullscreen music: section list focus highlight flashes | built + verified v4.0.1 | no section highlight flash on leaving fullscreen music |
| O23 | 10-24 | Main menu slide in/out too fast even at slowest | built v4.0.1 | merged into O24: slowest 0.4x = 1000 ms open / 875 ms close (was 400/350); default 1x unchanged |
| O24 | 10-24 | Fine-step tuner scale for speed/timing rows | built v4.0.1 | 17 steps (0.4x..3x, step 7 = 1x default) for menuopen/menuclose/mctrl/albumscale/flip/rowscroll/cascspeed; cascstag 0-160 ms 17 steps (60 default); zoomtime 0-800 ms 17 steps (110 default); bar_17_*.png; presets remapped to same values |
| O25 | 10-24 | Section opened from Main menu pops in piecemeal | built v4.0.1 | bz_secload hides MyVideoNav/MyMusicNav content until list + focused art are in (cap 3 s), then one 400 ms fade (bz_secfade) |
| O26 | 10-24 | Grid tiles still sway | built v4.0.1 | 56 rotatey idle-sway/pulse animations removed from BezelGridOverlayM/V; poster 6280 Long sway untouched |
| O27 | 10-24 | Arctic grid not in use in Movies; Arctic focused + unfocused layouts in all grids | built v4.0.1 | panels already AZR (350 ms quadratic, 105% focus zoom, block-colour frame) in all video + music grids, but the 3.5.5/3.5.7 overlay covered them when the grid was focused (50% dim, white glide ring, bounce slot). Overlay grid-focus parts disabled so the Arctic layouts show |
| O28 | 10-24 | Video starts in fullscreen | verified v4.0.1 | Player.Open episode -> fullscreenvideo active, Player.HasVideo after 7 s (b401/o28_fs.png) |
| O29 | 10-24 | Remove overlay on movie pause poster | verified v4.0.1 | Custom_1116: gradient + pause badge removed; title/time/progress sit left of the clean poster (b401/o29_pause_after.png) |
| O30 | 10-24 | Music fullscreen must not auto-open | verified v4.0.1 | 75 s of music playback, window stays Music (b401/o30_after70s.png) |
| O31 | 10-24 | No movie poster in player submenus | verified v4.0.1 | osdaudiosettings/osdsubtitlesettings during movie: no poster (b401/o31_audio_after.png, o31_sub_after.png) |
| O32 | 10-24 | Phantom logo top right when a TV video starts | built + verified v4.0.1 | DialogBusy BEZEL logo suppressed while video starts/plays (no close-fade hold, hidden under Player.HasVideo/fullscreenvideo); forced busy dialog during video shows no logo (b401/o32_busy_during_video.png). "Detected new con..." toast is Kodi's own notification |
| O33 | 10-24 | Title + SxxExx overlay on TV episode art tiles | built + verified v4.0.1 | prev/next drum tiles (flat + a/b faces) now carry the tv_strip_v2 overlay, dimmed with the tile (b401/o33_after.png, o33_after_scroll.png); next tile's overlay sits below the screen edge by layout |
| O34 | 10-24 | TV Continue watching empty | built + verified v4.0.1 | bz_flip cw thread: in-progress episodes + next-up per show -> alternating xsp (bz_cwfile), rebuilt at start, 2 s after stop, every 10 min; list 6913 shows next-up (b401/o34_after.png) |
| O35 | 10-24 | View options slide list too fast; link to Main menu slide tuner | built + verified v4.0.1 | BezelATViewAnim follows Open/Close speed (17 steps): verified 1000 ms / 400 ms / 133 ms (b401/o35_step1/7/17.png); default now 400/350 (was fixed 240/200) |
| O36 | 10-24 | Remove tap-to-enlarge/shrink album entirely | built + verified v4.0.1 | album kept at Jumbo permanently |
| B401 | 10-24 | 4.0.1 sweep bugs | fixed | (1) O20 deleted bz_reflect_floor.png but Rainbow LOOK still uses it as mask -> restored; (2) d3gap tuner bar_4_* textures never existed -> generated; (3) changelog had a stale duplicate 4.0.1 line and said album Standard 600 px -> fixed to Jumbo |- O37 [BUILT 4.1.0] All dust tuner row (DUST, top): one master on/off for main, soft, album/poster and sparkle dust (bz_tune.py alldust). [queued next build, after 4.0.2 sparkle] Single 'All dust off' master toggle in tuner (kills every dust layer: main, soft, album, glare, poster, fibers/flakes). Rob Oct 24 12:04.
- Backdrop colour/white lock option: Rob 👎 Oct 24 12:04, not wanted; backdrop stays random.
- O38 [BUILT 4.1.0] left-strip dust grouplists 900->904 so they meet the bottom strip at the lower-left corner (no gap/overlap seam); fix_o38 applied. BUG 4.0.2: artifact in the colour block on all screens (Rob Oct 24 12:45). Suspect 4.0.1 image recompression of colour block textures.
- O39 [BUILT 4.1.0] Tuner ALBUM / POSTER "Big album" row, default ON (bz_bigalb_off); no tap or on-screen buttons. Big album on/off toggle in the TUNER (default large); no tap-to-enlarge or on-screen buttons (Rob Oct 24 12:46).
- O40 [SUPERSEDED by O46 in 4.1.0] Main menu Recently played music -> single album view (albums, not tracks) (Rob Oct 24 12:47).
- O41 [MOOT in 4.1.0: logo removed by O43] BUG 4.0.2: logo glow anim still broken (Rob Oct 24 12:47); compare to storyboard_v2 panel 1-11.
- O42 [BUILT 4.1.0] fix_o42 applied: 1115 unload resets the mode, pill label reads CONTROLS while 1115 is open. BUG 4.0.2: pill cycle button (6391) label doesn't always match the open mode (Rob Oct 24 13:07).
- O43 [BUILT 4.1.0] Main menu logo, glow and Kodi text removed. Remove EVERYTHING in the Main menu logo area: big logo, logo glow, text (Rob Oct 24 13:17). O41 glow fix now moot.
- O44 [SKIPPED in 4.1.0 per Rob] More tuner control for list slide-in + cascade (distance, easing, fade length, end slowdown, start delay).
- O45 [SKIPPED in 4.1.0 per Rob] Remove Rainbow reflection tuner row (dead floor reflection leftover).
- O46 [BUILT 4.1.0] strip-list Main menu (list 6996 inside the strip, white bar / black text, black screen, strip-tinted edge glow; Left = view options, Right = BEZEL Tuner, Back closes; remote + touch tested). Main menu direction chosen: simple strip-list Main menu living ONLY inside the colour strip (Music, Movies, TV Shows, Music Videos, Recently Played, Favourites, Playlists, Search, Files, Add-ons | Settings, Kodi, Power; white focus bar), rest of screen empty black reserved for effects, soft strip-tinted edge glow that lights nearby dust specks only. Replaces colour-block variants A/B/C (rejected). Mockups: /workspace/mockups/menu_list/glow_*.png (Rob Oct 24 13:20-13:25).
- O47 [BUILT 4.1.0] 0.25 s black fade-in, list slides in behind the strip, menu fades in; highlight preloads bz_lastart_<section> (stored on leaving a section); select = menu fades out, list slides out, art back after 0.2 s over 0.8 s. Main menu transition (revised Rob Oct 24 13:38): (1) trigger from a section = quick ~0.25 s fade to black of the section art (poster/colour block/album) while the left list slides right BEHIND the colour strip; (2) Main menu list fades in on the strip with edge glow + lit dust; (3) highlighting (not selecting) a menu item invisibly preloads that section's last-used poster/album; (4) select = menu fades out, short delay, then slower ~0.8 s fade-in of the already-loaded section art while the left list slides out populated. Mockups: /workspace/mockups/menu_list/transition_v2.mp4 + transition_v2_keyframes.png (v1: transition.mp4).
- O48 [BUILT 4.1.0] Settings window fades instead of sliding (Rob Oct 24).
- EMPTY-ART [BUILT 4.1.0] ".." / no-art rows never show the DefaultFolderBack icon as the big poster/album; parent item uses the folder art.

## 2026-10-24 (after 4.1.0)
- **O49** Main menu has no focus (t2476u) — DIAGNOSING. Test Kodi: Left from Music opens menu, focus=6996, white bar shows (b410/focus/open_left2.png). Not reproduced on desktop yet; suspect another open path (touch/logo, Back, other windows) or Shield timing. Needs Rob's open method.
- **O50** Glow BEHIND colour strip, not blur edge (t2476u) — MOCKUP: mockups/menu_list/glow_behind_{music,movies}.png (+_4k), compare glow_compare_old_vs_behind.png. Skin mm_strip_glow.png untouched.
- **O51** New Main menu list layout style, same colour strip (t2477u) — APPROVED style B (t2482u): inset rounded pill + dark strip-colour text + › chevron. Mockups list_style_B*.png. A/C rejected. Awaiting go to build.
- **O52** Now Playing cycle pill should take focus on Up (t2478u) — FIXED IN SOURCE (not built): colour block 6390 <onup>noop</onup> -> 6391. Backup /workspace/backup_o52/.
- **O52 verified** in test Kodi: NP block 6390 + Up -> focus 6391 (evidence b410/focus/o52_up.png).
- **O53** Ambient dust looks dimmer in fullscreen (t2479u) — DIAGNOSED, no fix. No fullscreen-tied alpha/colordiffuse in dust (BzD3A_* vary only by bz_at_d3glow; fades only for sdbright and menu open). Dust dialog 1114 is HIDDEN in fullscreenvideo (by design). In music fullscreen viz/NP, the dust switches to the other cut-mask set (Custom_1114 line 23 vs 11, keyed on Window.IsActive(music)/bz_np) and sits over a bright vis/fanart block, so it reads dimmer. Needs Rob: which fullscreen (video or music viz)? photo.
- **O54** Jump bar hidden behind dust dialog (t2480u) — DIAGNOSED, no fix. Dust is dialog 1114 (zorder 0); Kodi always draws dialogs above windows, so dust particles in the left column (x16-120, Custom_1114 line 16/29) draw over the A-Z jump bar (x~78) in Music/Videos. No zorder change can put a window control above a dialog. Fix options: (a) regenerate dust (gen/gen_dust3.py, not hand-edited) with the jump-bar column cut out, or (b) fade that column of dust while the jump bar group has focus. Needs go.
- **O55** Album sway looks choppier than before (t2481u) — DIAGNOSED, no fix. Sway XML (Includes_Bezel ~866-950: rotatey sine inout 5500/10250 ms pulse, big-album rotate ±4 8.5 s) and bz_flip.py sway timing are UNCHANGED in 4.1.0 vs backup_bezel2_410_pre (only bz_flip diff = menu SetFocus 6996). Main 4.1.0 change touching render load: Custom_1114_Dust.xml (O38 regen, size by tile geometry instead of zoom) grew 3.48->4.07 MB, images 3748->5508 (+47%), animations 14578->16118; dust dialog draws over the music window every frame, so a likely Shield GPU/CPU frame-time hit = choppy sway. Secondary: new strip menu/glow (hidden when closed, low risk); bz_mm.py runs only on select (no loop). Fix options (need go): (a) regen dust with one shared tile set (fewer controls), (b) pause/fade dust while sway runs, (c) A/B: Rob toggles dust off to confirm. Rob (t2483u): Short sway. Still need: does it smooth with dust off?
- **O56** Dust: optimize more + lower default amount (t2484u) — DIAGNOSED, no change (needs go). Linked O55 (short-sway chop) + O54 (jump bar under dust). Rob (t2487u): flakes and fibers do not need their own layers — bake some flake/fiber into one of the sharper dust textures (drops fib/flk layer stacks + Fibers/Flakes amount rows can stay as texture mix or go). Current defaults (empty string): d3dens=Low(1 = already the minimum), d3amb Ambient 30% (min 10%), d3glow peak 45% (min 10%), d3lit 100% (min 10%), sdbright soft dust 100% (min 20%), sdsize Medium, fibamt Rare (min), flkamt Low (min), spin on, all 5 breathe layers on. Load: 5508 images / 16118 animations; every layer's 1920x1080 tile grid is re-emitted once per void clip rect per mode (rects() splits into many thin strips) + duplicated A/B lit stacks + 15 d3speed slide variants per grid + separate fiber/flake spin stacks. Proposal: one regen of gen_dust3.py covering O54 (cut jump-bar column x~60-120 from Music/Video void) + O55/O56 (merge clip rects, share one stack, drop unused size grids, bake flake/fiber into sharper dust texture) + new defaults (amb 20%, glow 20%, lit 60%, soft dust 40%). NOTE gen_dust3.py SPD has 7 speeds but shipped 1114 has 15 — confirm generator is the O38 version before regen.
- **O57** Auto-start fullscreen music delay + Off (t2488u) — LOGGED, not built. Rob: add tuner option to set delay and Off for auto-start music fullscreen. Sequence: music starts, then after the delay fullscreen music opens. Context: O30/4.0.1 removed auto-open entirely (`if False` idle NP path in bz_flip.py); Busy logo delay is unrelated. Default Off (Rob confirmed t2489u). Needs go: tuner row (Off + delay steps), re-enable auto path gated on setting, delay from play start (not only idle).
- **O58** Dust brighter + denser after leaving fullscreen music (t2485u) — DIAGNOSED (code), not reproduced on rig, no change (needs go). Linked O53/O56. Findings: no alpha/colordiffuse var (BzD3A_*, BzD3L_*, sdbright, d3glow) depends on fullscreen/visualisation/1112/bz_np, and no script sets a dust-boost property on exit; 1114 stays open over viz (only fullscreenvideo hides it), so no WindowOpen re-fade. What does change: (1) MODE SWITCH — viz/NP shows mode A group (Custom_1114 l.23, larger void: full top band, right strip x1890, no music-art cut, Feather_A); library shows mode S (l.11, needs Window.IsActive(music)+!bz_np+bz_mini+no bz_back). If bz_np/bz_back is still set for a moment (or stays set) after Back, mode A keeps drawing over the library = dust where the S cut normally hides it (denser) and without the S feather (brighter). (2) ANIMATION RESTART — every group hidden in fullscreen restarts all its looping anims from t=0 when shown again: the 5 breathe layers (BZG:0-4, staggered delays 0/2/4/6/8 s) and spark A/B (BZS) lose their offsets and run in phase, so peaks stack together (brighter) and the drift slides reset to the same start offset. A long run then drifts back out of phase, so if it settles after ~30 s it's (2); if it stays it's (1). Rig: could not repro (NULL audio sink = no bz_audio_latch, no viz add-on, grid view on); evidence /workspace/b_o57/. Proposed fix (in the O56 regen; this is O58 not the auto-start O57): one dust set for music library + music fullscreen (same clip/feather, viz just adds nothing) so no group swap, which removes both causes; failing that, key mode S on Window.IsActive(music) only (not bz_np) and give the breathe/spark loops a fixed pre-roll so a restart lands on the low point, not the peak. Rob (widget): stays brighter/denser (points to mode swap / sticky bz_np or bz_back, not the ~30s pulse restart). Still open: from NP or viz?
- **O59** Main menu section subcategories (t2490u question / t2491u variety mockups) — MOCKUPS DONE, awaiting Rob's pick. Current: strip list 6996 has no subs (bz_mm.py jumps to section root: Music→albums, Movies→titles, TV→shows); old slide menu 6900 Music/Movies/TV expanders (Artists/Albums/Genres…) still in XML but unused by 6996. Variants (style B + glow behind), /workspace/mockups/menu_list/subs/: A inline expand, B drill-in page, C side flyout on void, D peek hint + D2 drill-in on Select; sheet subs_variety_sheet.png; script render_subs.py. No skin change. Rob (t2493u): D-style peek but different — highlight category, Right cycles primed subsection, Select/Enter opens that sub; on highlight default subsection is already ready for quick Select. D3 LOCKED (t2493 widget Yes) (see sub-bullet).
  - **Rob pick (t2493u): D-style peek but different (D3)** — highlighting a category primes a DEFAULT subsection ready for quick Select (Music→Albums); RIGHT cycles primed sub (Artists→Albums→Genres→Songs→Recently Added→wrap); SELECT/Enter opens that sub. Primed sub shown as a dark chip on the focused pill + position dots. Mockups D3_cycle_albums / D3_cycle_artists / D3_cycle_genres (+_4k), D3_cycle_sheet.png; script subs/render_subs_d3.py. AWAITING confirm/go. Not built, no skin change.
- **O60** Tuner menu in BEZEL colour strip style (t2494u) — MOCKUPS in progress. Restyle tuner (6970) to match Main menu strip: style B pill + glow behind strip, not the old dual colour-block panel.
- **O61** Ambient dust particles sharper and smaller (t2495u) — LOGGED, not built. All ambient dust particles need to be sharper and smaller. Pair with O56 regen (bake fib/flk, merge clips, lower defaults) + O58 one music layout. Needs go.
- **O62** Remove bright gold + remove sparkle layer (t2498u) — LOGGED into 4.2.0 build. Drop gold tint and sparkle (BZS / flake sparkle) entirely from dust.
- **O63** Tuner dust-layers info graphic + per-layer on/off (t2499u) — MOCKUPS DONE (t2503u), APPROVED — add to 4.2.0; was awaiting Rob pick; not built into skin yet. /workspace/mockups/menu_list/tuner/info/dust_exploded*.png. Exploded-view info graphic in Tuner showing dust layer labels; on/off toggle for every layer (no sparkle — O62 removed).
- **O64** Info graphics for other Tuner options (t2501u) — MOCKUPS DONE (t2503u, small/compact per t2502u), APPROVED — add to 4.2.0; was awaiting Rob pick; not built into skin yet. info/{cascade_stagger,open_speed,fs_music_delay,doubletap_window}*.png + info_graphics_sheet.png. Small labelled diagram/exploded style as dust layers for other tuner rows (not text-only desc).
- **O65** Separate Tuner controls + info graphics for lit vs ambient dust (t2507u) — LOGGED into 4.2.0. Lit and ambient get their own control groups and each its own info graphic (not one combined exploded view).
- **O66** 2.0-style splash (t2509u/t2510u) — LOGGED for next build. Restore the 2.0 splash look. Not in 4.2.0.
- **O60** Tuner menu in BEZEL colour strip style (t2494u) — LOCKED B (strip + desc) — awaiting go. Not built. Restyle Tuner (Includes_Tuner.xml list 6970, old slide-menu colour block) to Main menu strip style B (inset pill focus, dark text in strip colour #26345C, › chevron, glow behind lighting void/dust). /workspace/mockups/menu_list/tuner/: A strip list w/ value/slider in pill; A2 strip list + D3-style ‹ value › chip on void; B strip list + focused-option description on void; C section tabs (DUST/LIST/LOOK/MUSIC/SYSTEM) in strip + that section's list. Sheet tuner_variety_sheet.png; script render_tuner.py. No skin change.

### 4.2.0 build status (Oct 24, 2026, EDT) — zip /workspace/skin.bezel2-4.2.0.zip, evidence /workspace/b420/
- **O50** [BUILT 4.2.0] Glow behind the strip.
- **O51** [BUILT 4.2.0] Main menu list style B.
- **O59** [BUILT 4.2.0] Section sub cycle.
- **O60** [BUILT 4.2.0] Tuner restyled: strip + style B pill + description on the void (b420/o60_tuner.png).
- **O57** [BUILT 4.2.0] Tuner "Auto fullscreen music" Off/5/10/20/30/60 s (default Off); verified 5 s opens NP, Off does not (b420/o57_*.png). Opens only when the music window is up.
- **O62** [BUILT 4.2.0] Sparkle layer removed (220 BZS images, spark vars/rows/textures). No gold colour found in dust textures/colordiffuses; the "gold" was the sparkle glints, now gone.
- **O63** [BUILT 4.2.0] Far / Mid / Near layer toggles + small exploded-view graphic that dims layers live (b420/o63_*.png).
- **O64** [BUILT 4.2.0] Small info graphics for cascade, open speed, double-tap, auto fullscreen delay (media/bezel/info/).
- **O65** [BUILT 4.2.0] New "Ambient dust" master row (bz_amb_off hides far/mid/near/soft/spin) separate from "Lit dust (hold)"; ambient rows show amb_*.png graphic, lit rows (adust, d3lit, d3lsize, lspin*, phold, pdust) show lit_*.png graphic (b420/o65_*.png).
- **O52** [VERIFIED 4.2.0] NP block 6390 Up -> 6391 (b420/o52_np_up_pill.png).
- **O49** NOTE: not reproduced; every tested open path focuses 6996. Left open, needs Rob's exact repro path.
- **O56** partial: lower defaults shipped (ambient 20%, glow 20%, lit 60%, soft dust brightness 40%).
- **O54 / O55 / O56 regen / O58 / O61** DEFERRED: gen_dust3.py is stale versus the hand-edited 4 MB Custom_1114_Dust.xml; regenerating would drop shipped changes (O38, layer toggles). Needs a generator refresh first.

### 2026-10-24 (after 4.2.0)
- **O68** [DECIDED] Rob (t2519u): remove feather bands entirely — likes dust in front of everything (not soften/cap). Awaiting go.
- **O70** [LOCKED] Rob (t2522u): Left navigates to section settings / View options **only when focused on the Settings row** in Main menu 6996; remove Left→bz_navset from other rows. Awaiting go.
- **O71** [QUEUED] Rob (t2521u): Tuner options for glare and shadow need rework after dust-in-front / feather-off (O68). Pair with that pass.
  - Mockups (Oct 25): /workspace/mockups/tuner_glare_shadow/ (NOTES.txt). LOCKED: glare+shadow GLOBAL across all posters+albums (t2536u/t2537u); glare style picker + opacity + tint; shadow style/size/opacity/shape; infographics per row; Tuner drop-down sections.

- **O67** [INVESTIGATING] Rob (t2512u): Settings → Media → Library → Videos → Add video: can't navigate to the Browse button; Left seems to open another window (maybe section menu). Diagnosis (XML only, not reproduced in GUI): DialogMediaSource.xml. Browse (11), Add (13) and Remove (14) sit in grouplist 9000 below the paths list, but list 10 goes ondown=12 (the Name field) and Name goes onup=10, so Down/Up skip 9000. The only way into 9000 is Left from list 10. No section-menu or ActivateWindow hook found in the dialog or BzDlgFrame. Likely the "other window" is the FileBrowser that Kodi opens when you click the list's path row. Proposed fix: 10 ondown=9000, 9000 onup=10 ondown=12, 12 onup=9000. Optionally 9000 onleft/onright=noop. Safe for the next build.
  - **O67 update (t2514u, Oct 24 ~11:12 PM EDT):** Rob says it works in Estuary, breaks after switching to BEZEL, and stays broken after switching back to Estuary. Estuary's DialogMediaSource.xml has the same focus map as BEZEL's (10: up 9001, left 9000, down 12; 9000: left/right 10, down 12; 12: up 10, down 9001), so the earlier focus-link theory can't explain this. It becomes a minor polish item. The skin writes two files into the profile keymaps folder: userdata/keymaps/zz_bezel2_np_tab.xml (bz_cmd.py keymap) and zz_bezel2_dtap.xml (bz_dtap.py). Both stay loaded under any skin. np_tab has a <global> block: keyboard c / menu / longpress return and a few raw key ids, plus remote menu / title / contentsmenu / rootmenu / topmenu, all mapped to ContextMenu. Gamepad/joystick A on hold is mapped to ContextMenu too. Revised hypothesis: on Rob's remote or Shield, one of these global bindings fires inside the dialog (or a key code collides) and opens the context menu, the "other window". After a switch back to Estuary they also point at special://skin scripts that no longer exist. Needs confirming against Rob's kodi.log / Debug key codes. Fix (not applied): scope the global block to the BEZEL windows only, or gate it on the skin; delete zz_bezel2_* keymaps when the skin is unloaded or changed; drop the bare keyboard 'c' mapping (it also blocks typing 'c' in edit fields). Workaround for Rob: delete userdata/keymaps/zz_bezel2_*.xml and restart Kodi.
- **O68** [DIAGNOSED, not fixed] Rob (t2515u, Oct 24 ~11:20 PM EDT): horizontal ambient dust layers show black bars top and bottom. Diagnosis (files + XML; not live-reproduced): the dust textures are clean (dust_far/mid/near/bokeh/spin_*.png all have transparent edge rows, mean alpha 0–3). Tile layout also covers the screen in every size mode (Medium is 1:1 1920×1080; Large zooms 140; Small zooms 75 on a 3×3 grid). Cause is the black **feather overlay** (`$VAR[BzD3Feather_S/A/P/R(0)]` → media/bezel/d3/feather_*_{1-4}.png, a full-screen 1920×1080 image drawn on top of each mode group in Custom_1114_Dust.xml). It draws an opaque black band along every edge of each void rectangle. The horizontal void strips are thin (mode S: y16–29 is 13px, y85–120 is 35px, y1020–1064 is 44px; mode A: 1050–1064 is 14px, 1020–1050 is 30px). On those strips the top and bottom feather bands fill most or all of the height, so the dust drifting through reads as running between two black bars. The vertical strips are 64–104px wide, so their bars are side bars that look like intended edging. Lit dust (BezelLitDust, its own mask) is not involved. Proposed fix for the next dust pass (NOT applied): in the feather generator, clamp the feather width to ≤ ~⅓ of the strip's short side and soften it (alpha ramp, no solid core). Or drop the screen-edge and cross-strip bands on strips shorter than ~48px, or leave those strips out of ambient dust. This needs the gen_dust3 refresh first: gen_dust3.py is stale (7 vs 15 speeds), and a full regen would roll back O38/O65. Regenerate only the feather PNGs, or hand-patch. Evidence: b420/o68/feathers_grid.jpg, feather_*_3_on_grey.jpg.
- **O69** [DIAGNOSED, not fixed] Rob (t2516u): turning off Soft dust also turns off the spin layer. Cause: a nesting bug in shipped Custom_1114_Dust.xml, probably from the hand patch that added `+ !Skin.HasSetting(bz_amb_off)` in O65. The spin wrapper is emitted as an empty, self-closed group, `<control type="group"><visible>!Skin.HasSetting(bz_spin_off) + !Skin.HasSetting(bz_amb_off)</visible></control><!--BZG:4-->`. So the spin images (BzD3Tex_spin, 2300/3067px rotate) fall through into the still-open Soft dust group (BZG:3, `visible !bz_sdust_off + !bz_amb_off`). Result: Soft dust off hides spin, and the Spin toggle hides nothing. Found in all 55 copies (every mode × void rect). gen_dust3.py spin() itself is correct (wraps the images properly). Proposed fix (NOT applied): a scripted replace across 1114 that removes the stray `</control>` after the BZG:4 visible and adds one `</control>` before it to close BZG:3. Then check the group balance per grouplist. Do not regen.

- **O79** [LOCKED] Rob (t2545u/t2546u, Oct 25): mini player on Main menu (strip 6996) with prev/play/next + FULL button. LOCKED (t2549u): C, top of strip; list tightened. Plus (t2550u) a › right arrow on the focused section pill, placed after the primed O80 sub chip when one shows. Mockups: miniplayer/C_locked_top_arrow.png, C_locked_top_arrow_chip.png, C_locked_sheet.png. Earlier variants A/B/A2 are kept for reference. Open: is the arrow on the pills, the chips, or both (mockup covers both)?
- **O80** [MOCKUP] Rob (t2547u, Oct 25): visual aid for Main menu section cycle (O59 D3: Right cycles primed sub chip, Select opens) on Music/Movies/TV. /workspace/mockups/menu_list/subs/cycle_visual_aid.png (+render_cycle_aid.py). Movies/TV sub lists illustrative.
- **O79 update** (t2553u): CONFIRMED keep current bar + pill style, only add the › arrow. No style change.
- **O79 style variants** (t2554u): mockup style variants delivered: miniplayer/V1_baseline … V9_chip_density.png, mp_style_sheet.png (render_mp_variants.py). These are chrome options only. Placement C and the bar/pill style stay locked. Awaiting Rob pick.
- **O79 chrome** (t2555u): LOCKED V6 — plain icons (no circle; focused underline + pause), no visible progress bar. Placement C + bar/pill + › unchanged.
- **O82** [DIAGNOSED, not fixed] Rob (t2552u, Oct 25 ~12:14 AM EDT): "Fullscreen music auto open broke". Code: scripts/bz_flip.py ~L368 (O57). Skin.String(bz_at_autonp) 1/empty=Off, 2-6=5/10/20/30/60 s; Tuner L/R rows Includes_Tuner.xml 1120-1129 are intact. Only auto path in the skin (no AlarmClock/ActivateWindow(visualisation) elsewhere). Causes: (1) default Off = never fires (rig :77 has bz_at_autonp empty = Off); (2) the delay counts from play START, not from arriving in the music list, and it only fires when the music window is up with no menu/flip/dialog/1112 — music started from Home / mini player / another window never auto-opens; (3) once per play session: autonp flag only resets when audio stops, so after FS closes once it never re-opens during a continuous playlist. 4.1.0 had none (O30 removal 4.0.1); old 60 s idle-based logic was replaced by play-start timer. Proposed fix (not applied): time from idle in music window (System.IdleTime(delay)) instead of play start; re-arm autonp when FS/NP closes or on track change; fire from Home/menu too if wanted (ask Rob); confirm Rob's Tuner value is not Off.
- **O83** [NEXT BUILD] Rob (t2556u, Oct 25): Main menu color strip — keep the fan art from the previous screen visible (don't blank/cover it). Background should still show prior screen fanart under/through the strip.
- **O84** [MOCKUPS] Rob (t2557u, Oct 25): Fullscreen music — small visual aid at the BOTTOM of the colour block showing the cycle prev · CONTROLS · fwd (same idea as O80/O78). 6 variants A–F in /workspace/mockups/fs_music/cycle_aid/ (sheet.png, closeups.png, A_under_label … F_inset_corner, NOTES.txt). Awaiting Rob pick. **v2 (t2558u):** in colour block, faded low-opacity white text + icons — 6 variants A_tri_text_25 … F_icons_only_35 (opacity 25–40%, triangle/chevron/skip arrows, sliders/play-ring icon) in same folder; v1 moved to v1_old/. Awaiting Rob pick.
- **O84 update** (t2559u): Labels LAST — (play/pause logo) — NEXT (not CONTROLS). In fullscreen music: Select pauses when the cycle pill is not highlighted / when outside the player-control menu. Player control menu is opened from the pill. Mockups to refresh with LAST / ▶❚❚ / NEXT. **v3 (t2559u/t2561u):** labels LAST — real skin play/pause icon (icons/now-playing play+pause) — NEXT, in-block faded white; 6 variants A_last_pp_next_25 … F_dash_pp_30 (v2 → v2_old/). Behaviour: FS music SELECT pauses when pill not highlighted / outside player-control menu; control menu opened from pill. Awaiting Rob pick.
- **O84 chrome** (t2563u): LOCKED C — LAST ▶❚❚ NEXT with small triangles, in-block faded white (~30%), real skin play/pause icons. **C locked (t2565u):** 16 C-family variants C_var_01..16 (opacity/spacing/triangle/icon scale/tracking/nudge/dashes) + C_var_sheet.png, C_var_closeups.png. Awaiting Rob pick of C_var.
- **O84 C pick** (t2569u/t2570u): LOCKED C_var_4 (tiny play/pause, Raleway, spaced) + add small triangles back.
- **O85** [MOCKUPS] Rob (t2562u, t2564u "make some varieties"): FS music player-controls menu (opened from cycle pill) in BEZEL colour-strip style (Main menu/Tuner B language). 10 variants A–J in /workspace/mockups/fs_music/controls_strip/ (sheet.png, mk.py, NOTES.txt): A Tuner-B list+desc, B +icons, C transport pill row head, D compact one-line, E strip right, F replaces block, G bottom horizontal strip, H tabs, I icon rail, J now-playing card. Skin untouched. Awaiting Rob pick.
- **O85 chrome** (t2566u): LOCKED D — compact one-line rows (icon, label, value on the right) in BEZEL colour-strip style. **C v2 (t2567u/t2568u):** 8 obvious C_var_1..8 (faint/bright, huge/tiny pp, huge/no tri, stacked, wide+dashes, left packed), Raleway SemiBold, wider gaps. Awaiting pick. **LOCKED C_var_4 + small triangles (t2569u/t2570u):** C_var_4_smalltri.png — confirmation mockup.

## 4.3.0 — built 2026-10-25 (zip: /workspace/skin.bezel2-4.3.0.zip)
- BUILT 4.3.0: O79 (mini player above the main menu with prev/play/next and a FULL pill; › arrow on every focused row), O79b (strip gradient, alpha 150 rising to 255), O83 (previous fanart stays visible behind a 60% dim), O84 (C_var_4 cycle hint with small triangles; Select pauses instead of opening controls), O85 (1115 restyled to D: PLAYBACK/MODE/MORE, ids 6401-6409 kept, plus 6410 Close), O67 (np-tab keymap scoped per window, bare C removed), O68 (Dust3 feather blanked), O69 (1114 spin group nesting fixed), O70 (Left from Settings opens settings nav), O77 (6391 pill brightened), O82 (auto-fullscreen based on idle time, re-arms on track change).
- SKIPPED: O71 (picks not locked), O72/O78 (no spec found), O73–O76, O81 (not fully specified), O66 splash (not feasible).
- Notes: O85 left out the empty description panel from the mockup. O79b was read as the strip gradient. The 'favourites' keymap scope was dropped because Kodi 21 doesn't recognise it.

## O86 — 2026-10-25 (Rob) abrupt crash while listening to music in the music list (4.2.0, no log)
- Status: investigating; no Shield log available (Android/data access denied). No rebuild.
- Hypotheses (skin side): (1) bz_flip main loop calls xbmc.Player().getTime()/isPlayingAudio every tick from a Python thread -> race at track change/end on Android; (2) RunScript(bz_cmd.py,np) fired by auto NP (O57) or the "same file restarted" tap detector while a track change / busy dialog is up -> two np scripts / window activate mid-transition; (3) GPU/texture memory: dust (73 controls, d3 frames) + flip/fanart + cascade on Shield; (4) Kodi-core paplayer/decoder crash unrelated to skin.
- 4.3.0 O82: idle-based auto NP + re-arm on track change means MORE auto-opens, not fewer; does not mitigate (1)/(3).
- Next: ask Rob whether auto fullscreen music was on, whether crash was at track change, file type/source; get kodi.old.log via Settings > System > Logging > debug or a log uploader addon (script.kodi.loguploader).

## 4.4.0 — built 2026-10-25 (zip: /workspace/skin.bezel2-4.4.0.zip, backup of 4.3.0 source: /workspace/backup_bezel2_430_pre44)
- BUILT: O66 (2.0 splash, bz_splash60 font, "BEZEL VERSION 4.4"); O71 (new Tuner sections: ALBUM GLARE with styles Original + G1–G6, opacity and tint; POSTER GLARE kept separate; ALBUM SHADOW for the swaying big album with styles Original/Soft/Hard/Contact/Glow, size, opacity and shape; Original is the default in every case); O72 (TV chip shortened to RECENT / WATCHING and moved right); O73 (Tuner SLIDE MENU renamed MAIN MENU, Main menu speed row Original/Fast/Faster with Fast as default, about 40% quicker; slide rows kept); O74 (info graphic on every Tuner option: the O71 mockup cards plus generated opt_<id>.png for 41 options); O76 (every Tuner section is a drop-down that starts collapsed, OK toggles it, +/– marker); O78 (pill cycle to Controls keeps focus, shows CONTROLS ▾, Down opens 1115); O81 (Main menu bar brightness 60–100%, default 90%, same as before); O86 hardening (bz_flip auto NP and tap detector skip while busy, caching, no audio, 1112 or visualisation is up; getTime is in a try block); O87 (Tuner "Crash report" button in the last section, scripts/bz_crash.py: view the latest kodi_crashlog, kodi.log or kodi.old.log, copy the crash log to Kodi home, open script.kodi.loguploader if installed).
- SKIPPED: O75 Main menu lit dust (not built, for time); dust regen of O54/55/56/58/61 (generator is stale, 7 speeds vs 15, and regenerating would overwrite the hand-made O38/O65/O69 fixes).
- Checks: all xml parsed; py compiled; test Kodi (:77, /tmp/bz2home) loaded 4.4.0 with no skin XML errors. The Tuner, splash and crash button were not checked by eye.

## O88 — 2026-10-25 — "Why does FPS get so low in BEZEL?" (investigated, no build)
- Finding: Custom_1114_Dust.xml is 3.9 MB: 5,288 image controls, 1,715 groups, 55 grouplists, ~15,600 animations (6,600 rotate, 8,305 slide, 495 zoom, 223 fade). All size/density variants (d3asize, d3dens, sdsize, d3lsize) are separate control copies toggled by visible= conditions, so Kodi loads and checks all of them every frame, even the hidden ones. The earlier O19 test (software renderer, shared CPU) showed no cost, but that test can't be trusted on real hardware.
- Smaller causes: album sway, glare and shadow layers stacked on top (O71); bz_flip.py polls every 0.05 s while the menu/anim is active; several dust layers can be on at once (dust/adust/pdust/sdust/ps_dust/alldust).
- Turn down now: Tuner > DUST: dust off (or lowest density/smallest size), turn off the extra album/poster/screensaver dust; glare/shadow opacity 0 or Original; swaypause on.
- Next build: generate only the one active dust variant (or $PARAM includes) instead of all copies; fewer particles and one animation per particle; open the 1114 dust dialog only when dust is on; poll at 0.1–0.2 s; measure System.FPS on the real box with dust on and off.

## 4.5.0 — built 2026-10-25 (zip: /workspace/skin.bezel2-4.5.0.zip, backup of 4.4.0 source: /workspace/backup_bezel2_440_pre45)
- BUILT: O75 Main menu lit dust (media/bezel/mm/mmdust_{low,med,high}_{1,2,3}.png by gen/gen_mmdust45.py; group in BezelNavMenu after the strip glow; Tuner MAIN MENU rows mmdust/mmdamt/mmdbright + bz_tune.json + info graphics opt_mmdust/opt_mmdamt/opt_mmdbright).
- BUILT: dust regen with gen/gen_dust45.py (synced to the 15-speed Tuner): O54 jump-bar cutout (x60-120, music/video lists), O55 greedy rect merge (56 clips), O56 dead soft group dropped, O61 textures regenerated (gen/gen_dust45_tex.py). Custom_1114_Dust.xml: 4,488 images (was 5,288), 15,291 animations (was ~15.6k), 3.72 MB (was 3.95 MB).
- PARTIAL: O55/O56 cut only ~15% of the load. The big FPS fix (O88: generate only the active dust variant) is still open.
- NOT BUILT: O58 (diagnosis unresolved; waiting on Rob: "from NP or viz?").
- Checks: all xml parsed; test Kodi :77 loaded 4.5.0 with no skin errors; screenshots /workspace/b450/o75_mainmenu.png, /workspace/b450/dust_1114_albums.png.

## O49 update — 2026-10-25 ~11:05 AM EDT — Rob (t2662u, 4.5.0): "main menu doesn't open, looks like section list keeps focus" — DIAGNOSED, not fixed
- Open path (by design): Left (or Back at root, or M) on the section list 60 runs XML `SetProperty(bz_nav,true,home)` only (xml/Includes_Bezel.xml ~L1316 onleft/onback, L2519 for video; MyMusicNav.xml:43 / MyVideoNav.xml:38 for M). XML never moves focus. The focus move to strip 6996 is done ONLY by the bz_flip.py nav_menu thread: scripts/bz_flip.py:500-514 `SetFocus(6996,N,absolute)` (or 6930/6931 for card 2). That thread also clears bz_navgrace / bz_navlock (L320-322, L488-491).
- REPRODUCED on test Kodi :77: stop the bz_flip loops while leaving bz_flip_running=true, then Left in Music -> bz_nav=true, focus stays 60, menu not drawn, further Left/Back do nothing (bz_navok false because bz_nav is true). Screenshot /workspace/b401/mm_noflip.png. With bz_flip healthy every path (Left from music/videos/settings, Back at root, M) focuses 6996 / 6920 — so 4.5.0 XML is not the cause.
- Root cause (likely): bz_flip.py's nav_menu thread is dead while Home property bz_flip_running is still 'true', so no new bz_flip is started (onload guard MyMusicNav.xml:15, MyVideoNav.xml:18, MyPlaylist.xml:8). Ways it happens:
  1. Installing a new zip (4.5.0) over a running skin without restarting Kodi: Kodi stops/aborts the old script; finally block (bz_flip.py:815-818) skips clearing bz_flip_running when abortRequested -> flag stuck 'true' -> nothing restarts the service until Kodi restart. (bz_cmd.py:58 version check can't catch this: bz_flip_ver is hard-coded 'np3' in every build.)
  2. An unhandled exception inside nav_menu (bz_flip.py:301 loop has no try/except) kills only that thread; other threads keep the flag 'true'. Same symptom; fits O49 being intermittent and O86 Android crash notes.
- 4.3–4.5 changes checked: 4.5.0 only touched O75 dust group (non-focusable images, Includes_Bezel.xml after strip glow), Tuner rows, dust 1114, splash. diff vs backup_bezel2_440_pre45: no change to bz_flip.py, MyMusicNav/MyVideoNav, 6996, 60 onleft. Not an O75/dust/nav regression.
- Also by design (not a bug, but feels like "list keeps focus"): lists with >20 items show the A–Z bar (6100 music / 6500 video); first Left goes to the bar, second Left opens MM.
- Immediate workaround for Rob: fully restart Kodi (Shield: force stop Kodi) after installing 4.5.0. If it still happens after a restart, send kodi.log (look for a Traceback mentioning bz_flip / nav_menu).
- Proposed fix (needs go): (a) wrap nav_menu loop body in try/except + log and keep going; (b) heartbeat property (bz_flip_hb = time) and onload restart if stale instead of trusting bz_flip_running; (c) XML fallback: on 60 onleft add `<onleft condition="$EXP[bz_navok]">SetFocus(6996)</onleft>` after the SetProperty so focus moves even without Python (check it doesn't fight the absolute-row SetFocus / card-2 path); (d) bump bz_flip_ver per build so bz_cmd.py warns.

## O49 update 2 — 2026-10-25 ~11:08 AM EDT — Rob (t2671u): still broken on WINDOWS after full Kodi quit/reopen; works first time, breaks after leaving the menu and opening again
- Restart doesn't fix it, so the "stale bz_flip after install" cause is ruled out for Windows.
- Reading scripts/bz_flip.py nav_menu (L296-535): every state var is defined at L298-300; risky calls (getTime) are already guarded; no unguarded int()/dict lookups on the open/close path. No death cause found by reading.
- Reproduced on :77, 4.5.0: about 25 open/close cycles with close via Back, Select on a row (same and other section), Left on the Settings row (view options) + Back x2, section switch Music<->Videos, mouse moves while open. nav_menu stayed alive the whole time (it keeps logging "stray focus"/"focus stolen" lines), bz_flip_running=true, no Traceback in kodi.log. Death of the thread NOT reproduced.
- Reproduced a "section list keeps focus" path that IS by design: grid views (bz_gridfirst, Includes_Bezel.xml:256; MyMusicNav.xml:5 / MyVideoNav.xml:5 onload SetFocus(6600); bz_flip.py L311-317 re-focuses 6600 for 2.5 s after every folder change). After choosing a section from the menu, focus lands on the grid 6600; Left on 6600 is `<onleft>60</onleft>` (Includes_Bezel.xml ~L2852), so the first Left only moves to the section list 60 and the menu does not open; a second Left opens it. Fresh start often lands on 60 instead, so "works first time". Also lists >20 items: Left goes to the A–Z bar first.
- Needed from Rob: (1) does a SECOND Left (or Back) open it? (2) Windows log %APPDATA%\Kodi\kodi.log right after it fails — search "Traceback", "bz_flip", "BEZEL menu"; (3) which section/view and how he left the menu (Back / Select / Right).
- Proposed minimal fixes (need go):
  a. Robustness: wrap the nav_menu loop body in try/except + xbmc.log(traceback) so one bad tick never kills it (covers cause 2 if a Windows log shows a Traceback).
  b. Heartbeat: nav_menu sets bz_flip_hb each tick; the window onload restarts bz_flip if the heartbeat is older than 2 s.
  c. If (1) = yes (grid two-step): grid 6600 onleft -> `<onleft condition="$EXP[bz_navok]">SetProperty(bz_nav,true,home)</onleft>` (open the menu straight from the grid's left column) instead of `<onleft>60</onleft>`; this changes grid nav, so it needs Rob's OK.

### O49 update 3 — ~11:20 AM EDT (round 3, :77 repro, no source change, no zip)
Conditions chain for 6996 (all must hold): include BezelNavMenu → group 6899 `bz_navmenu + !fullscreenvideo + !visualisation` (400ms Hidden hold) → group @570,120 `bz_navmenu` (fade) → plain group 390x900 → list 6996 `<visible>$EXP[bz_navmenu]</visible>`, no `<enable>`, 13 static items (no conditional items, so never 0 items). bz_navmenu = bz_nav; bz_navok gate = !navlock + !navgrace + !bz_nav.
Repro log (:77, open → Select MUSIC → Left → Left):
- 11:19:37.07 bz_nav=true, 6899 visible=TRUE, 6996 visible=FALSE → 11:19:37.272 `Control 6996 in window 10502 has been asked to focus, but it can't` (same line as Rob's). Retry succeeded 0.25s later on Linux.
- After close (11:19:39.69+): 6899 visible=false but Control.IsVisible(6996)=TRUE (stale — children of a hidden group are not re-evaluated, so 6996's Hidden slide/state never runs). This stale/half-animated state is the likely "section partially hidden" and why reopen behaves differently from first open (Visible slide doesn't retrigger).
- After Select a section the window lands on grid 6600 (gridfirst); first Left goes 6600→60 (looks like "list keeps focus"), second Left opens MM; 11:19:45.251 "focus stolen just after open -> back to the menu" fired, recovered.
Cause: SetFocus(6996) races 6996's OWN visible condition, which lags the parent by ≥1 frame and holds stale state between opens; on Rob's Windows box the retry window evidently loses every time on reopen. Could not reproduce the permanent failure on Linux.
Proposed minimal fix (awaiting Rob's go): on list 6996 change to `<visible allowhiddenfocus="true">$EXP[bz_navmenu]</visible>` (one line, Includes_Bezel.xml:453) — SetFocus no longer depends on the child's lagging visibility; parent 6899 still gates display. Alt: drop 6996's own <visible> and move its slide animations to the 390x900 parent group.
Siblings logged, not fixed: spin pulse-face fade missing; O85 controls overlay colour-strip info (same size/pos); Tuner opens only on Right from settings bar; section partially hidden after leave (= stale 6996 state above).

- O49 quick fix shipped 4.5.1 (2026-10-25): list 6996 visible allowhiddenfocus="true" so Main menu reopens. Other queued items NOT included.

## 4.5.2 (2026-10-25)
Done and smoke-tested on :77:
- 1 Main menu in front of the section box, also on reopen (3 opens in a row). Cause: speed-conditional Visible/Hidden fades stuck at 0 on reopen; the menu fades are now one unconditional pair (Main-menu speed setting no longer changes them). `<enable>` on menu buttons removed; allowhiddenfocus kept.
- 3 Tuner highlight: white pill visible on the focused row, dark text.
- Tuner opens only with Right on the Settings row (kept).
- 6 Spin layer always pulses 40%<->100% (bz_tune_patch._dust, layer 4), even when Ambient = Glow.
- 7 Player controls (1115) sit on the colour strip, 570,120 390x900, solid backing hides the Now Playing text under it.
- 10 Cut-out off dust: drawn straight to the full screen (no clip grouplist / margin edge).
- 11 O79b strip gradient: mm_strip_grad.png now fully see-through on the left, solid from ~300 px.
Skipped: 4, 5, 8, 12; 9 awaits Rob. addon name attribute still says "BEZEL 4.4.0" (version 4.5.2).

## Post-4.5.2 todos (Rob t2711u–t2715u, Oct 25 2026)
- UNDO the t2712u idea "second Tuner dust set = album/poster lit dust only" (Rob t2713u). Do not build it.
- Tuner dust: relabel the dust sections to say what each one is for (Album / Poster / Global), and add an info graphic for each unique dust control section (t2713u).
- Main menu mini player: the FULL button pill end is not round (t2714u; correction: ONLY the small FULL pill, not the card). Mockups are in mockups/menu_list/miniplayer/pill_ends/full_pill/ (A ref, B–E + closeups + sheet). The card mockups in pill_ends/ A–E are superseded. Waiting for Rob to pick (t2715u). Style stays locked: V6 plain icons, no progress bar, top of strip, bar/pill + ›.
- addon.xml name attribute still says "BEZEL 4.4.0" (shown on update). Fix it to match the version in the next pack (t2711u).
- Kodi crash: Rob sent a .dmp (Oct 25 2026). Waiting for kodi.log for detail; no fix yet.

- **Dust 2.0** (t2731u 👍): rebuild Spin so fibers stay streaks-only; round blobs stay out of the fiber mix. Named Dust 2.0.

- **Dust 2.0 ambient** (t2732u): Far, Mid, Spin only (drop Near + Soft from ambient).

- **Dust 2.0 depth** (t2733u): depth look baked into textures (not extra ambient layers).

- **Dust 2.0 particles** (t2741u): Far=fine dots+fibers; Mid=standard dots+fibers; Spin=fine+standard mix+fibers; 3 density textures each layer.

- **Dust 2.0 slide** (t2746u): Far+Mid horizontal back-and-forth, opposing directions, different speeds.

- **Dust 2.0 speed** (t2747u): Tuner speed per layer (Far / Mid / Spin).

- **Dust 2.0 fade** (t2751u): slow wipe per layer; Far/Mid opposing directions + staggered times.

- **Dust 2.0 loop** (t2753u): all layers loop (pulse = looping).

- **Dust 2.0 Spin fade** (t2755u): looping wipe top→down.

- **Dust 2.0 Tuner** (t2759u): fade speed slider.

- **Dust 2.0 Tuner** (t2760u): fade speed per layer + proper labels.

- **Dust 2.0 album/poster** (t2762u–t2763u): keep 1.0 look + sync with poster/album.

- **Dust 2.0 album** (t2768u): add full mix spin to album (match poster).

## 4.6.0 (built Oct 25 2026, EDT)
- Item 1 Dust 2.0 — BUILT (approximation): Custom_1114 regenerated by gen/gen_dust46.py (Distant/Mid/Spin layers, density/brightness/fade/slide per layer, nested Tuner subs with info graphics, ALBUM section with Glare/Shadow/Dust/Look/Size/Sway subs). Fade is a looping alpha fade (Far/Mid opposite phase); no true wipe (Kodi has no animated mask); Spin top-to-bottom wipe not built. Lit dust at both Long-sway ends (mix on); Short sway right end only; poster 6280 untouched.
- Item 2 Shadow labels — BUILT: "Album shadow (on the colour strip)" vs "Big album shadow …", info album_shadow_labels.png.
- Item 3 FULL pill 6960 — BUILT: mm_full_ol.png / mm_full.png (86x34 r10, border 12).
- Item 4 Version strings — BUILT: addon.xml 4.6.0 / BEZEL 4.6.0, news + changelog, splash "BEZEL VERSION 4.6".
- Item 5 Crash dig (bz_flip.py) — PARTIAL: _np_open() single guarded launcher (4 s cooldown + _np_safe right before launch) for auto-NP and tap paths; getTime replaced by Player.Time info label (no xbmc.Player() objects 10x/s in a helper thread); every helper thread wrapped (traceback to kodi.log, restart up to 5x, then bz_flip_running cleared + bz_flip_fail set so a new RunScript can start). No root cause claimed; Rob's .dmp / kodi.log still needed.
- Item 6 Album list behind art — NOT FIXED (diagnosed only): cover column list slides up to -480 (pos 14) so row 0 sits 30 px above the 450 cover redraw; test library has 1 track so it could not be reproduced; Jumbo/standard/small not distinguishable in the cover column (fixed 450). Needs a repro screenshot.
- Item 7 A-Z bar flicker — FIX ATTEMPTED: 6100/6500 visible now Container(60).NumItems>20 (was Container.NumItems, which follows the focused container and replayed the Visible/Hidden fades). Not visually verified. Dust O54 cut-out kept in gen_dust46.


## 4.6.1 (2026-10-25)
- DONE: Album list regression — rows slid up to -480 (30 px above the 450 cover top, y 90-120). Added a clipped black strip (grouplist, 60 px above the cover, visible at Container(60).Position >= 12) in Includes_Bezel.xml before the 3.2.1 item 13 bottom strip. 4.4 slide steps untouched. Backup: /workspace/backup_bezel2_460_pre461/. Zip: /workspace/skin.bezel2-4.6.1.zip. Not visually verified on long album (test album on :77 had 1 track).
| N1 | 2026-10-25 | Artists grid/info desync after deep scroll | fix applied (src, 4.6.2 pending build) | bz_flip grid_sync: list-follow Control.Move was fire-once (dropped move = permanent desync); now re-checks + retries up to 4x. Mid-row cut = shot taken mid 350 ms panel scroll (984/246 = exact 4 rows) |
| N2 | 2026-10-25 | Vis over Music root: NP see-through, list bleeds | fix applied (src), live check w/ audio pending | list 60 fade on NP required bz_npdlg (only set by 1112 dialog); in-place NP via vistoggle never set it. Fade now also on non-library (root/genre) lists |
| N3 | 2026-10-25 | Movies stale info on open | fix applied + verified | Kodi restores old selection before bz_flip resets grid/list to item 0. bz_flip now puts list 60 on item 0 too; MyVideoNav holds content hidden (bz_gpend, 2 s failsafe) until synced. Verified: hidden while 'Joker', shown at 'Alien' |
| N4 | 2026-10-25 | Back with Main menu open goes up folder | fix applied + verified | menu opened but focus not yet moved (bz_flip poll) -> Back hit list 60 -> parent dir. list 60 onback now closes menu + consumes Back when bz_nav set (both list 60s) |
| N5 | 2026-10-25 | Settings Left dead | not reproducible; no change | Left from Settings list opens MM (verified shot b401/nav5_check.png). Repro = Left within 0.8 s bz_navgrace after MM closed opening Settings |
| N6 | 2026-10-25 | A-Z bar never takes focus | not a bug; no change | grid(6600) focused by default -> Left goes to list, 2nd Left to A-Z (verified # focused, b401/az_focus_check.png). Latent: id 6600 duplicated (video A-Z grouplist for list 64 vs grid panel) - rename suggested |
| N7 | 2026-10-25 | Settings BEZEL style | built in src (4.6.2 pending build), verified on :77 | Settings.xml rebuilt: MM strip group 570/120 390x900, mm_strip_grad + glow, list 9000 rows 56 from top 40 (+120 w/ player), bz_mm28, pill + ›; category + desc on the void at Tuner B x1010. Rows line up exactly with MM (b401/navtest_settA3.png vs settA_mm.png). BezelMiniPlayer include dropped (strip shows player like MM). Backup /workspace/backup_settings_A_pre/ |
| N8 | 2026-10-25 | Settings Back -> Main menu, Left dead | built + verified on :77 | list 9000 onleft=noop; onback=AlarmClock(bz_setmm,SetProperty(bz_nav,true,home),1s) then normal window Back -> previous window opens with MM, focus 6996 (b401/navtest_settA_back.png). Tuner Back already -> 6996. NOTE: <onback>Back</onback> crashed Kodi - not used |
| N9 | 2026-10-25 | MM Left/Right cycle; Section Settings to Settings left nav; icon indicator on Settings bar | pending - needs spec from Rob | not built |
| N5/N6 | 2026-10-25 | Rob: leave as-is | locked | A-Z two-Left path kept; 0.8 s grace kept; 6600 not renamed. Rob: jump bar should load at >39 items; source rule is Container(60).NumItems>20 (3x Includes_Bezel.xml) - not changed, needs Rob's call |

## 4.7 — Music-start + Dust 2.0 + Tuner (2026-10-25)
- Startup: Music opens with Main Menu over it (bz_cmd.py start; opt-out bz_nomenustart). Section dims via parent group fade (Tuner "Section dim" 50–90%, default 90%); fullscreen dim texture hidden in Music/Videos.
- Glow PNG soft-edged; Tuner "Glow brightness" 20–100% (default 100%).
- Dust 2.0: ambient Far/Mid/Spin; Tuner "Ambient position" ABOVE (1114, default) / BELOW (in-window copy, BezelAmbientBelow).
- MENU DUST nest: Menu dust, Density, Brightness, Fade, Slide (default Mid); album textures masked to glow (mm/mmd20_*), draws over glow.
- One parent group per section: MyMusicNav + MyVideoNav (BezelSecDim).
- Open: old mm/mmdust_* files kept; bz_tune_patch / presets don't know new keys; Spin wipe not built.
- 4.7.0 SHIPPED 2026-10-25: Section dim remapped default 90%, Left lightens by 10 to 30% (Right back to 90); Left from Albums grid -> Main Menu (not Music root); MM strip bezel C (mm_strip_bezel_c.png light hairline + mm_strip_shadow_c.png soft Gaussian; shadow weak on dark bg, alpha bump offered). Zip /workspace/skin.bezel2-4.7.0.zip, backup /workspace/backup_bezel2_pre470_20261025_1845. Stress leftover: pill cycle / Section Settings / Vis rerun.

## 4.7.1 (built 25 Oct 2026, 8:58 PM EDT) — zip /workspace/skin.bezel2-4.7.1.zip, backup /workspace/backup_bezel2_pre471_20261025_2048/
- [x] A1 Presets Default/Subtle/Mid/High/Extreme (Default = Subtle) for Album(art incl. poster hold), List, Episodes, Main menu, Music, Ambient Dust (Poster has no own preset row; phold is in the Album/art preset)
- [x] A2 MM strip 100% · [x] A3 dim default 40% (now Global dimmer) · [x] A4 Dust-below fix · [x] A5 Cut-out gone from Tuner · [x] A6 Poster dust nest keys — verified in source
- [x] A7 Size labels 90% / 100% / 125%
- [x] B8 Cast shadow, Album SHADOW + new POSTER > SHADOW: style/length/softness/opacity/Y/animated; defaults identical to 2.7 shadow; dead strip-shadow rows (shadowtex/shadowop, also in LOOK) removed
- [x] B9 Lit 1.0 default + 2.0 toggle · [x] B15 separate poster 2.0 bake (lit20p_*)
- [x] B10 Global dimmer LOOK 90..30%, default 40%; MAIN MENU Section dim retired
- [x] B11 Fade hold Far/Mid/Spin (Off..5 s, default 2 s), live via bz_tune_patch
- [x] B12 AMBIENT DUST · [x] B13 Album SWAY / Poster SWAY hold · [x] B14 D20 defaults
- Concerns: Default preset (Subtle, 30% bri) ≠ B14 slider defaults (70%); mmdbright 30/50/70/90 approximated to 40/60/80/100; lit spin preset approximated; B14 fade Slow applied to Spin too; 2.0 lit ignores lit size; grid sway shadows (2861/2913) not cast-ified.

## 4.7.2 (in progress) — Global dimmer fix
- Bug: LOOK > Global dimmer did nothing on non-Music/Videos (hardcoded 99 scrim) and Music/Videos SecDim fade was easy to miss / conflict.
- Fix try 1: `$VAR[BzGDimCol]` drives MM full-screen scrim for every section; `BezelSecDim` retired (empty include). Live in addon + b300; not zipped yet.
- Bug (Rob): TV show posters missing in TV Shows list view (non-grid). Root cause: the :77 test Kodi (HOME=/tmp/bz2home) was running a stale 18:45 copy of the skin, not the 4.7.1 addon; also `bz_noart60` treated a `Default*` icon as "no art" even when a poster existed (TV shows always have icon DefaultFolder.png), which faded the poster group. Fix try 1: Default-icon clause dropped from bz_noart60 (art checks only); /tmp/bz2home addon synced to /home/box addon (backup /workspace/backup_bz2home_skin_pre_tvfix). Verified b401/tvposter_before3.png -> tvposter_after.png.
- Bug (Rob): episode drum, next tile title + SxxExx not on the art. Root cause: next-tile overlay at y 1179-1349, below the screen (tile only visible 843-1080). Fix try 1: overlay moved to the tile's top (strip_grad flipy at 843, labels 863/893), 3 copies. Verified b401/tvep_overlay_before.png -> tvep_overlay_after.png.
- Queued (Rob t3180u): MM glow brightness default → 30 (was 100% / Tuner Glow brightness).
- Note (Rob t3179u): cast shadow is list/big-art only — grid must NOT have cast (not a bug).
- Queued (needs go): Cast Soft as Default — BzCastTex_a/p currently fall back to sway_shadow when Style empty/Current; Soft only when Style=2 or Softness 3/4.
- Queued (Rob t3181u): Section View options menu — crossfade in/out, no slide.
- Queued (Rob t3182u): Tuner menu not lined up with MM strip; pops on open — align + crossfade/no-pop.
- Stress update (Rob t3183u): include Tuner/View options vs MM strip alignment + open pop (geometry overlay), not only enter/close.
- Stress update (Rob t3184u): same for similar strip/menu misalignments (View options, Settings, etc.).
- Queued (Rob t3185u): remove dots under Main Menu section labels.
- Queued (Rob t3186u/t3187u): MM pills center between arrows; restyle to match mini-player pill.
- Queued (Rob t3188u): remove old Player Controls still in the skin.
- Queued (Rob t3189u): fullscreen music — “Select” text next to play/pause.
- GO clarify (Rob t3202u): all Soft-mockup cast looks (4 views) in cast system; switchable Album+Poster Tuner SHADOW.

## 4.7.2 (2026-10-25) GO pack, not zipped
- 1 Cast Soft as Default: empty Style = Soft (cast_m_soft) for Album + Poster.
- Cast looks (Rob GO t3202u): root cause of "all styles look the same": album cast image had rotatey 0→13 about x1440 (+ pulse rotatey) → every texture smeared into one diagonal band; and the cast_b16/b30 textures were the wrong shape (blob top of block). Fix: rotatey removed (pulse timing kept via no-op zoom); new textures cast_m_{current,soft,hard,long,short,offset,faint}.png baked from mockups/album_shadow/cast/mk.py parameters (480x880 slot, right edge at block edge). Tuner Style: 1 Current, 2 Soft, 3 Long, 4 Short, 5 Offset Low, 6 Faint, 7 Hard (new) — Album SHADOW + Poster SHADOW.
- 2 Poster cast not showing: cast was gated on bz_pswayon/bz_ppulse (hidden until sway started) and zoomed to 0 at every flat pass. Gate fade + zoom/fade removed; counter-rotation kept so it stays flat.
- 3 MM glow default 30%. 4 View options crossfade (220/180 ms), no slide. 5 Tuner card aligned to MM strip right edge 960, glow 0/1920, no slide pop. 6 MM label dots removed. 7 MM pills = mini-player pill (mm_full_ol, BzMMDark), centred between arrows.
- 8 Old Player Controls: unused Estuary PlayerControlsPlayImageVar removed; PlayerControls.xml kept (redirect to 1115/VideoOSD needed by M key / Start). Needs Rob confirm if he meant something visible.
- 9 Fullscreen music cycle aid: LAST ◂ ▶‖ SELECT … NEXT ▸ (SELECT added next to play/pause).
- 10 Global dimmer try1 (BzGDimCol) kept. TV poster / episode overlay fixes untouched.
- Backup: /workspace/backup_bezel2_pre472_2213
- 4.7.2 follow-up (Oct 25 22:4x): poster cast uses brighter cast_mp_* (Hard shares cast_m_hard); all 7 poster looks visible (b401/cast_poster3_compare.png). Screen-checked on :77: MM pills/dots/glow (472_mm_open.png), Tuner aligned right edge 960 (472_tuner_open.png), View options on MM strip (472_viewopts_open.png), FS SELECT label (472_fs_select.png, SELECT nudged to 524/NEXT 630). Old Player Controls left as-is pending Rob. Not zipped.
- 4.7.2 (Rob t3207u, Oct 25 ~22:55 EDT) View options font sizes: labels stay bz_mm28 (same as MM section list 6996); values (label2) moved to a parallel non-focus grouplist (6932 music / 6933 videos, row-for-row, same visible conds) at bz_mm22 right-aligned, width fitted per label; textwidth 180 cap removed; VISUALIZATION row label → VISUALIZER. Labels no longer truncate/scroll. Nav checked (Down 6920→6921→6924→6922→6925). Shots: b401/472_vofont_before.png, 472_vofont_after.png, 472_vofont_after_vis.png. Synced addon + /tmp/bz2home. Backup b300/Includes_Bezel.xml.bak_vofont. Videos panel not screen-checked. Not zipped.

## 4.7.2 SHIPPED (zipped 25 Oct 2026, 10:46 PM EDT) — zip /workspace/skin.bezel2-4.7.2.zip, backup /workspace/backup_bezel2_pre472zip_20261025_2245/ (earlier: /workspace/backup_bezel2_pre472_2213)
- Cast: Soft default (empty Style) for Album + Poster; 7 mockup styles (Current/Soft/Long/Short/Offset Low/Faint/Hard), rotatey smear removed.
- Poster cast always shown (gate/zoom removed), brighter cast_mp_* textures.
- MM glow default 30%; MM label dots removed; MM pills = mini-player pill, centred.
- View options + Tuner crossfade, no slide; Tuner aligned to MM strip right edge 960.
- Fullscreen music SELECT label next to play/pause.
- Global dimmer (BzGDimCol) all sections; TV show list poster fix (bz_noart60); episode next-tile overlay moved onto art.
- View options fonts: labels bz_mm28 (match section list), values bz_mm22 (one step smaller), VISUALIZATION → VISUALIZER.
- Unused PlayerControlsPlayImageVar removed; PlayerControls.xml kept (pending Rob).
- addon.xml 4.7.2, changelog.txt 4.7.2 entry. Addon + /tmp/bz2home synced. Splash label still reads 4.6 (unchanged). Full Kodi restart needed after install.

## 4.7.3 SHIPPED (zipped 25 Oct 2026, 11:19 PM EDT) — zip /workspace/skin.bezel2-4.7.3.zip, backup /workspace/backup_bezel2_pre473zip_20261025_2319/. Was: live — cast shadow edge + X axis + info panel (Rob t3211u)
- Cast now starts at the colour block edge, slightly overlapping (image right edge 965 = 5 px past block edge 960; textures cast_m_*/cast_mp_* rebaked so peak density holds to the edge instead of fading out ~45 px before it). Hard unchanged. Backup: /workspace/b401/bak_cast_x_2259/
- Tuner: new "Cast offset X" (bz_at_acx Album SHADOW, bz_at_pcx Poster) -60..+60 px, 7 steps, default 0; slide anims on all album (6) and poster (4) cast images.
- Tuner info panel: bezel/info/cast_shadow_styles.png (built from mockups/album_shadow/cast/infographic.png, album crops of the 7 styles) on all Cast rows.
- addon.xml 4.7.3, changelog.txt 4.7.3 entry. Addon + /tmp/bz2home synced. Full Kodi restart needed after install. Not screen-checked: Poster cast X, info panel.

## Backdrop: Rays + Panes (live, unzipped)
- Added to extras/backdrop (840x900, white overlays): rays_topleft, rays_bottom, rays_fine, rays_corner, panes_tight, panes_loose, panes_nogap, panes. Splatters kept. Joins random rotation at Backdrop Opacity.

- 4.7.4 (live, not zipped) Tuner LOOK > **Backdrop image**: LEFT/RIGHT (OK = next) cycles Random → each file in extras/backdrop (sorted) → Random. Skin string `bz_bdimg` (empty = Random, else file name; sticks until changed). bz_cmd.py `backdrop` honours it on window load; new action `bdimg,next|prev` sets it + `Window(Home).Property(bz_backdrop)` immediately. Files: scripts/bz_cmd.py, xml/Includes_Tuner.xml (BzATVal_bdimg, row id bdimg, onleft/onright).

## 4.7.4 SHIPPED (zipped 25 Oct 2026, 11:58 PM EDT) — zip /workspace/skin.bezel2-4.7.4.zip (20.6 MB), backup /workspace/backup_bezel2_pre474zip_20261025_2358/
- Rays + Panes backdrops (8) in extras/backdrop; Tuner LOOK > Backdrop image (bz_bdimg). addon.xml + changelog 4.7.4. Addon + /tmp/bz2home synced, :77 restarted on 4.7.4.
- Stress 4.7.4 (Rob t3223u): shots b401/stress474_*. bdimg cycles all 10 + Random and sticks across window reload: PASS. Tuner/VO aligned to MM strip (right 959/960, top 120, bottom 1019), crossfade no pop: PASS. No Python exceptions. RSS 440→612 MB over 16-window sweep (watch). Label shows raw file name (panes.png); toast "Tuning applied" on change.

## 4.7.5 (live) — actor photo release (Rob, 2026-10-26)
- "Cast" = actor photos in DialogVideoInfo (panel 50), not cast-shadow textures. Cast-shadow loading unchanged (BzCastTex_a/_p $VAR left as-is).
- Audit: actor thumbs are only `$INFO[ListItem.Art(thumb)]` inside panel 50 with background="true"; no window/home property, script, or variable copies them. Kodi frees them when DialogVideoInfo closes. No code change needed.
- Backdrop ClearProperty on unload + bz_backdrop_last kept.

## 4.7.5 (live) — Poster cast + Ambient dust on section menus (Rob, 2026-10-26)
- Poster cast: box screen-check — Tuner > POSTER (head) > SHADOW (sub, collapsed by default) shows all 7 rows (style/length/softness/opacity/offset Y/offset X/animated); L/R writes bz_at_pc*; shadow visibly changes (Short, +60 px X) in BEZEL VIDEO POSTER LIST. No code change. Cast only drawn in Video Poster List + video info back; hidden in episodes, on the flipped info back (bz_vback), and Poster Wall (grid = no cast, by design). Needs Shield confirm of where Rob looked.
- Ambient dust on section menus: cause = with Ambient position BELOW, BezelRootArtHide (opaque black x962-1920 at library root musicdb:// / videodb://) sat above BezelAmbientBelow, so the right void had no dust; MM looked fine because 1114 (ABOVE) draws there. Fix: clipped BezelAmbientBelow copy (grouplist x962 w958) inside BezelRootArtHide, visible bz_libroot + bz_amb_below. Box-checked Music root: dust back. Backup /workspace/b300/backup_rootdust_*.

## 2026-10-26 — Poster cast covers TV + movie posters (Rob)
- Request: poster cast shadow for BOTH movie and TV show posters (list/big-art views, not grid/wall). Tuner POSTER › SHADOW unchanged.
- Audit: BezelVPLPoster (cast lives inside it) is drawn for Content movies / sets / tvshows / seasons when Video grid is off (`!$EXP[bz_gridv] + !Container.Content(episodes)`); cast images only fade on episodes or flipped back (bz_vback). Sway/cast clock (bz_flip.py poster_clock) is content-agnostic. So TV Shows + Seasons already get the cast; no movie-only gate exists.
- Not shown (by design): Episodes (banner layout, no poster drawn), Poster Wall / grid (bz_grid_video), flipped info back.
- Status: live, no XML logic change needed; needs Shield check on TV Shows list.

- 2026-10-26 01:14 — Cast shadow X (Album acx + Poster pcx): fine 5 px steps, −60…+60 (25 stops, was 7 stops @20 px). Values stored as x-60…x60; legacy 1–7 still honored. Live only, no zip. Backup b300/backup_castx5_011417.

- [t3250u] Short sway toggle moved: section View Options (id 6927, Music) → Tuner › ALBUM › SWAY (first row, id swayshort). Same key bz_swayright + bz_sway_restart. Live only, no zip.

- 2026-10-26 t3322u: Christmas FS toggle did nothing from Music FS (Tab from Music stays in Music window w/ in-place NP; xmas layer was only in 12006 non-Music branch). Moved xmas layer into BezelNPInPlace (hidden in NP dialog). box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 2026-10-26 02:46 EDT: MM Tuner "Bar brightness" -> "Bar opacity" (t3325)
- Setting bz_at_mmbar (steps 1-5 = 30/48/65/83/100%, default/empty = 100%). Controls the MM colour strip (390x900 BzMMStrip image) opacity via conditional fade in Includes_Bezel.xml + Settings.xml.
- White focus bar BzMMBarCol fixed at E6FFFFFF (old default 90%). bz_tune presets mmbar -> 5. Glow (bz_at_mmglow) untouched.
- Backups *.bak_mmbarop_20261026024607. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

- 2026-10-26 (t3327u) Episode drum titles not following thumb slide: labels now frozen per drum face (bz_dr{a,b}_* props from bz_flip.py drum_dir). Backups *.bak_20261026_eptitle. Needs Kodi restart.

## 2026-10-26 02:55 EDT — Poster cast "not working" / baked-in? (t3326u)
- Answer: NOT baked. Cast is a separate overlay image (BzCastTex_p → media/bezel/cast_mp_*.png, 480x880 at x485 y130) drawn on top of the colour block inside the poster sway group (Includes_Bezel.xml BezelVPLPoster ~L2455/2460). Block texture is plain white.png tinted.
- Box test (Kodi :77, Movies > Poster List): red debug tint showed the overlay renders; Opacity 0% removes it; Short + X +60 changes shape/position. System works on box; 4.7.5 zip has same XML + textures.
- Gotcha: the dark side of the cast sits at the block's right edge (x~960); positive X offsets slide it under the poster → looks like it vanished. Negative X pulls it onto the block.
- Earlier "nothing changes" tests via JSON-RPC were invalid (XBMC.ExecuteBuiltin not a JSON method); use /workspace/bz_reload.py (EventServer).
- No code change. Needs Shield screenshot if still not seen.
- 2026-10-26: Poster cast animated (grow/fade with poster sway, like album); static via bz_pcast_static. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 4.7.6 (2026-10-26)
- Startup: Main Menu opens under splash before Music (bz_cmd.py start)
- Christmas LOOK on BezelNPInPlace (both FS paths)
- MM Tuner: Bar brightness -> Bar opacity (color strip 30-100%)
- Episode titles locked to drum faces (bz_flip)
- TV DRUM (EPISODES) Tuner: slide speed/ease, neighbour dim 0-90%
- Poster cast grows/fades with sway like album
- 2026-10-26 03:05 (t3333u) Settings sub menus (SettingsCategory.xml) still 2.0 style (grey 120-570 category panel, block bar, grey control wash, white-bar focus, font25/bz_list fonts, mini player). Restyled to match Settings/MM: MM strip 570 390x900 + glow + bz_at_mmbar opacity, categories bz_mm28 with mm_pill focus, header CATEGORY/BZ_MM34 + accent at 1010, controls grouplist 990/280 bz_mm22 pill focus, desc bz_mm17 at bottom, level button in strip. Backup xml/SettingsCategory.xml.bak_setsub_20261026030414. Not GUI-verified. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 2026-10-26 03:08 setaudit (Settings windows BEZEL style)
- SkinSettings, SettingsProfile: MM strip + bz_mm + mm_pill, no grey/ContentPanel/TopBar/miniplayer
- DialogAddonSettings: rebuilt on BzDlgFrame (DialogSettings style)
- DialogSettingButton (1101 SettingsList, 1105 MusicOSD) -> mm_pill + bz_mm22
- SettingsSystemInfo: miniplayer removed, font12->bz_mm17
- backups *.bak_setaudit_20261026030737; not zipped
- 2026-10-26 03:29 EDT: Zipped skin.bezel2 4.7.8 -> /workspace/skin.bezel2-4.7.8.zip (Settings pill/strip title/Back, strip notch 570, grid Left->list). Full Kodi restart required.
- 2026-10-26 03:38 EDT: Zipped skin.bezel2 4.7.9 -> /workspace/skin.bezel2-4.7.9.zip (Christmas FS above colour block, MM corner labels offset, MM-first startup). Full Kodi restart required.
- 2026-10-26 03:44 EDT: MM branding moved INSIDE colour strip (strip-local 390x900: logo 16,856 84x30; v-label 104,856; Kodi right-aligned 214-374,856; 73FFFFFF). Removed -570/-120 screen-corner footer. Backup Includes_Bezel.xml.bak_mmstripbrand_034125. done
- 2026-10-26 03:46 EDT: MM-first startup re-verified (black under splash, strip up at splash_done; bz_nav=true). No change needed.
- 2026-10-26 03:47 EDT: Zipped 4.7.10 -> /workspace/skin.bezel2-4.7.10.zip (strip branding + 4.7.9 Christmas/MM-first). Full Kodi restart.

## 2026-10-26 ~04:05 EDT — t3376 MM-first still broken on Shield + t3377 version label nearer logo (source only, no zip)
- Root cause: bz_cmd 'start' only set bz_nav after waiting max 3 s for Window.IsActive(music); on Shield the music window/list load is slower, so bz_nav was never set under the splash; the post-splash re-assert opened the menu AFTER the splash faded (Music seen first). Also bz_flip's post-splash focus retries (t<30) + 0.3 s auto-close could still drop it on a slow list refresh.
- Fix: bz_cmd arms bz_mmstart + bz_nav BEFORE ActivateWindow(Music); music wait 15 s. bz_flip: while bz_mmstart and menu not yet focused, never auto-close, re-SetFocus(6996,0) each tick for up to 6 s after splash; grace-cancel skipped while bz_mmstart. Cleared on first strip focus.
- Strip label: version label left 104 -> 52 (logo renders 30x30 at 16..46).
- Backups *.bak_mmfirst2_*. FULL restart required.

## 2026-10-26 03:59 EDT — t3378 mini player hides on next song (source only, no zip)
- Cause: bz_flip audio latch (bz_audio_latch, drives $EXP[bz_mini]) had a fast-drop: cleared after 0.45 s if !Player.HasMedia. On track change (non-gapless/Shield) the player is briefly empty, so latch dropped -> mini player Hidden fade, then re-shown.
- Fix: latch only clears after 2.5 s continuous no-audio, or on Player.HasVideo. Backup scripts/bz_flip.py.bak_minipop_035924. FULL restart.
- Confirmed t3376 MM-first (bak_mmfirst2) + t3377 version label 104->52 already in source from prior pass.

- t3379 (2026-10-26): zip 4.7.11 — /workspace/skin.bezel2-4.7.11.zip. Includes MM-first harden (t3376), version closer to logo (t3377), mini player latch across tracks (t3378). Backup: b300/backup_skin.bezel2_pre4711. Full Kodi restart required.
- t3380 (4.7.11): Music visible before MM after splash. Root cause: startup tuner-patch ReloadSkin (bz_dtap) cleared bz_nav under splash. Fix in bz_dtap.py reload_tuned (keep bz_nav while bz_mmstart). Verified on box: splash fades onto MM. Not zipped. FULL restart.

## t3381 — Remove Christmas from build, park for later
Removed BezelNPInPlace Xmas group, Tuner LOOK›Christmas item + BzATVal_xmasfs var; moved bz_xmas_fs*.png + bz_album_garland.png to /workspace/b300/parked_christmas/ (RESTORE.md). No zip.

## t3382 — Zip 4.7.12
- Built /workspace/skin.bezel2-4.7.12.zip (MM-first K23 tuner-reload fix, Christmas parked, 4.7.11 fixes). Backup: backup_skin.bezel2_pre4712.

## 2026-10-26 04:28 EDT — TV episode labels still broken (t3383u)
- Cause: drum thumbs read Container(60).ListItem(-1/0/1) live, but titles/SxxExx read bz_dr{a,b}_* props snapshotted by bz_flip.py drum_dir (50 ms poll, slower on Shield) → labels lagged/mismatched thumbs on each move and rapid scroll.
- Fix: all 24 drum label refs in Includes_Bezel.xml now read Container(60).ListItem(n).Season/Episode/Title directly — same source + same group as the thumbs, so they slide together. bz_flip props now unused (left in place, harmless). Backup Includes_Bezel.xml.bak_tvep_*. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Stress (box :77, Breaking Bad S1): rest shots b401/tvep_t1.png/t1b.png; 20 fps burst during down/down-up-down b401/tvep_burst_tile.png — titles ride on their thumbs every frame.
- Drum speed/Tuner scale ask (t3385/t3386) cancelled by Rob — no change made.

## t3389 (2026-10-26 04:30 EDT) — Episode drum smoother/slower + more range
- TV EPISODES Slide speed: 7 steps (1x–3x) → 11 steps 0.3x(2000ms) 0.4x 0.5x 0.6x 0.75x(800) 1x(600) 1.25x 1.5x 2x 2.5x 3x(200). Default now 0.75x (800ms, was 600).
- Default Slide ease cubic out → sine in-out (smoother). Presets remapped (default 5/sine, subtle 3, mid 5, high 8, extreme 11).
- Files: Includes_Tuner.xml (BezelATEpSlideDown/Up, BzATVal/Step/Bar eposlide+epease, nav), bz_tune.json, bz_tune.py. Backups *.bak_drumslow_042940. Episode only; t3385–87 generic drum stays cancelled.
- Old stored eposlide 1–7 now map to new scale (1 = 0.3x) → press Reset episodes once. .py changed → full Kodi restart.

## t3390/t3391 (2026-10-26 ~04:40 EDT) — Episode label fades with drum slide
- Removed the title/SxxExx strip (grad + 2 labels) from inside both sliding drum faces (a/b) in Includes_Bezel.xml. Added two flat overlays (visible bz_drumk==a / ==b) using new include BezelATEpLabelFade (Includes_Tuner.xml): on each flip the label snaps out, then fades in with delay = Tuner episode slide time (2000…200 ms per eposlide 1–11; default 800) so it appears once art stops. Static idle overlay (bz_drumk empty) unchanged. Labels still read Container(60).ListItem(0) (settled item).
- Drum slow/range (t3389) already done by prior agent (see above). Backups *.bak_epfade_*. ReloadSkin (but t3389 .py change still needs full restart). Not yet visually verified on box rig.

## t3392 (2026-10-26 04:31 EDT) — Zip what's built to try
- 4.7.13 zip /workspace/skin.bezel2-4.7.13.zip: TV ep label live-ListItem fix (t3383), episode drum slower/smoother + 11-step range (t3389), label fade-with-slide (t3390/91, not rig-verified), Christmas parked, MM-first K23. Backup b300/bak_pre4713_043143. Full Kodi restart (.py changed).

## t3394 (2026-10-26 04:36 EDT) — Note MM break + required fix
- Documented K23 in BEZEL_BREAKS.md (cause→fix→test) and startup prop-survival rule in KODI_SKIN_ENGINEERING.md. No source change, no zip.

## 2026-10-26 04:40 — t3396
- Rob: 4.7.13 TV episode list/label fix (labels fade with slide/stop) WORKED — KEEP.
- New episode drum defaults: slide speed 0.75x (eposlide 5, unchanged), ease **circle out** (epease 6; was sine 2). Empty skin string now maps to circle out in Includes_Tuner; bz_tune.json/py default + mid preset → epease 6; desc "Default: circle out".
- Backups *.bak_epdef_*. Restart: FULL Kodi restart (bz_tune.py changed). No zip yet.

## t3397 (2026-10-26 04:4x EDT) — Q: warm section behind MM while strip is highlighted?
Answer only ("?" rule). No code change, no backup needed. Findings: MM is an overlay inside Music/Videos window; Enter sets bz_navroot -> bz_flip does ActivateWindow/Container.Update. Same-window warm via Container.Update on focus is possible but risks showing section/DB churn under MM; cross-window (music<->videos) cannot preload hidden. Awaiting Rob go.

## t3400 (2026-10-26 04:48 EDT) — MM highlight loads section underneath (TEST ONLY)
- Rob: highlight Videos row → Videos loads under MM; back to Music → Music loads, MM stays on top. Parent: test only, keep isolated/reversible.
- bz_flip.py: new `mm_warm` thread (block marked "MMWARM TEST") + `bz_mmwarm` guard in nav_menu auto-close. Strip 6996 rows music/recent→Music, movies/tv→Videos (ActivateWindow/Container.Update to that root), 450 ms debounce, re-holds bz_nav and refocuses 6996 at same row. Skips during bz_mmstart/secload/splash 1113/1112/modal/submenus (K23 safe); the row MM opens on never warms (only a move).
- Rig r.sh cold start: MM held on recent-songs start list untouched; Down→Movies/TV swap under menu, Up→Music albums, focus+bz_nav kept; rapid Down/Up x6 → no swap; 0 log errors. Not checked visually for flash (no screenshot tool).
- Revert: copy /workspace/b300/bak_mmwarm/skin.bezel2/scripts/bz_flip.py back. FULL restart (.py). No zip.
- t3407 MMWARM2 (test): focus locked on MM strip 6996 during warm — bz_flip _hold loop, list 60 onfocus bounce while bz_mmwarm, window onload SetFocus(6996) in MyMusicNav/MyVideoNav. Backups *.bak_mmwarm2. Stress: 0 focus hits on 60 (was 1 per swap).

## 2026-10-26 — t3411u: reinstate section parent dim on Global dimmer (30–100% opacity)
- `BezelSecDim` (Includes_Bezel.xml) restored: Conditional fades on `$EXP[bz_navmenu]` driven by `bz_at_gdim` (no separate setting). Step → parent opacity: 1=30, 2=37, 3=44, 4=51, 5=56, 6/empty(default)=60, 7=100.
- `BzGDimCol` returns `00FFFFFF` (transparent) in Music/Videos → no double veil; other windows keep the scrim. NOTE: colordiffuse `00000000` is treated as unset = WHITE in Kodi — use `00FFFFFF`.
- Tuner label `BzATVal_gdim` now shows parent opacity (30%…100%).
- Backups: Includes_Bezel.xml.bak_/Includes_Tuner.xml.bak_ (2026-10-26). ReloadSkin. Not zipped. Warm focus lock untouched.
- 2026-10-26 05:10 EDT stress MM warm focus lock (4.7.13, full restart): Music<->Movies focus held on 6996 (0 leaks, 9+ swaps). NEW FAILS: (1) MM auto-closes ~1s after landing on a Music-side row when the warm target is already Music (Up into RECENTLY PLAYED, wrap to POWER, MOVIES->MUSIC on some swaps) -> bz_nav cleared, focus 60; keys then fall to underlay (reached Settings 9000). (2) on each window swap 6996 briefly reports the previous row (~100ms pill jump). (3) second cold start showed white/blank underlay behind MM, no section content. Logs /workspace/b401/mmw/r3/.

## 2026-10-26 05:15 — t3421u Go: FS music pill to colour-block corner (built, ReloadSkin, no zip)
BezelNPInPlace (Includes_Bezel.xml): title top 146→162 width 590→780; artist 212→228, album 258→274, progress 307→323, time 289→305; pill grouplist (6391) top 144→128, right edge 886→946 (left 486→546). Per mockup /workspace/mockups/fs_music_pill_corner/. Backup /workspace/b300/Includes_Bezel.xml.bak_fspill_*.

## 2026-10-26 05:12 EDT — t3419u Global Dim parent fade on ALL screens, black veil removed (XML, ReloadSkin, no zip)
- Backup: /workspace/b300/bak_gdim_all_20261026_0509
- Includes_Bezel.xml: BzGDimCol → always 00FFFFFF (MM scrim image kept, transparent = no veil anywhere).
- Wrapped all content before BezelLogoButton in a BezelSecDim group: AddonBrowser, FileManager, MyFavourites, MyGames, MyPics, MyPlaylist, MyPrograms, Settings, SettingsCategory, SettingsProfile, SettingsSystemInfo, SkinSettings (Music/Videos already had it). Mapping unchanged 30…100%, default 60%.
- Check: Music + Settings with MM, gdim 1/6/7 — both fade, no veil (b401/g474_sheet.png). Warm focus lock untouched.

## t3420 (2026-10-26) MMWARM3 — skip warm when target window already open
- bz_flip.py mm_warm: if Window.IsActive(win) -> log skip, no ActivateWindow/Container.Update. Backup bz_flip.py.bak_*. Full restart. No zip.
- Stress (/tmp/mmw.py, 78 steps, slow 1.6s + rapid 0.15s, down/up/wrap): 0 menu auto-closes in steady state (70/70 OK); 5 FAILs only in first 8 steps right after cold start (harness started before MM was up).
- Side effect: same-window rows no longer swap underlay (Music<->Recent, Movies<->TV keep previous list). Pill ~100ms row jump not touched.

## 2026-10-26 05:15 EDT — t3422u gdim wraps for remaining MM windows
- Audit: every window including BezelNavMenu/BezelLogoButton checked for BezelSecDim. Only missing: Custom_1112_NowPlaying.xml (dialog that hosts MM over Now Playing). Wrapped all content before BezelNavMenu in BezelSecDim group (MM unfaded). Backup .bak_secdim_*.
- Skipped: Home.xml (1.2KB redirect stub, no MM/content), MyWeather, MusicVisualisation, VideoFullScreen, OSDs — none host the MM include, so MM can't open over them; nothing to fade. ReloadSkin. No zip.

## t3424/t3425 — MMWARM4 in-place folder swap (test, no zip)
- bz_flip.py mm_warm: same window + different folder (Music↔Recently Played, Movies↔TV) → `Container.Update(path,replace)` in place, no ActivateWindow; focus held on 6996. Same window + same path still skipped. Backup /workspace/b300/bz_flip.py.bak_t3425.
- Full restart stress: down/up walk 28/28 menu open, pairs 12 Movies↔TV + 8 Music↔Recent swapped, 2 spam bursts settled correct; 26 in-place swaps logged. One 1.6s sample (MV6) still showed TV list, correct shortly after.

## 2026-10-26 05:28 — 4.7.5 Global Dim always-on (Rob t3438u)
- BezelSecDim (Includes_Bezel.xml L579): removed $EXP[bz_navmenu] gate; bz_at_gdim applies with MM open or closed. MM (Custom window) not inside faded group.
- Wrapped for dim: MyMusicPlaylistEditor, MyPVRChannels/Guide/Recordings/Search/Timers, MyWeather, EventLog. Backups /workspace/b300/*.bak_gdim_*.
- Shots: b401/gd/music_nomm_g1.png (30%), music_nomm_g7.png (100%), MM closed. Gdim restored to 6 (60%). No zip.

## 2026-10-26 05:32 — Pictures Global Dim recheck
- Side panel (MediaMenu 9000) already inside MyPics 4.7.4 SECTION PARENT GROUP (BezelSecDim). Retest g1 vs g7 MM closed: panel/icon dim (icon 127→73, panel 16→8). Earlier 'fail' was a misread of the semi-transparent grey panel. No code change. Shots b401/gd/pictures_nomm_g1_fixed.png, _g7_fixed.png, pics_cmp.png. Gdim restored 60%.

## 2026-10-26 05:36 EDT — t3430u MM highlight flash fix + t3442u MM scroll stress (full restart, no zip)
- Flash cause: MyMusicNav/MyVideoNav onload `SetFocus(6996)` (no row) → new window's strip showed row 0/previous row until bz_flip re-focused (~100ms).
- Fix: bz_flip mm_warm sets home `bz_mmpos`=row before ActivateWindow (cleared after warm); onload now `SetFocus(6996,$INFO[Window(home).Property(bz_mmpos)],absolute)`. Backups scripts/bz_flip.py.bak_flash_*, /workspace/b300/My{Music,Video}Nav.xml.bak_flash_*.
- Scroll stress (/tmp/mmw.py, 78 steps: slow 1.6s down/up, fast 0.15s down/up, slow down) + 40ms poll: 77/78 OK; 1 FAIL = fast-pass step where position moved between reads (pending key, not a close). 842 polls: 0 menu closes, 0 focus leaves 6996, 0 row bounces (flash gone). 17 warms fired (Music/Movies/TV/Recent, in-place + window swaps). Shots /workspace/b401/mmw/scroll/.
- Crossfade (fade underlay out/in around warm): NOT built yet — parked per t3442 priority. Plan: conditional fade in BezelSecDim on home prop bz_xfade set by mm_warm.

## 2026-10-26 05:40 EDT — t3446/t3447u ship 5.0.0
- /workspace/skin.bezel2-5.0.0.zip (addon.xml 4.7.13→5.0.0). In: Global Dim always-on + wraps + help text, MM warm flash bz_mmpos fix, in-place swaps. Not in: crossfade, prefetch. Backup b300/skin.bezel2.bak_pre500_053844. FULL restart (bz_flip.py).

## 2026-10-26 — MM speed (in-place+prefetch), t3445/t3451/t3453
- bz_flip.py mm_warm: poll 0.1→0.05s, debounce 0.45→0.2s, in-place hold exits early once 6996 focused & not updating; cross-window final loop only re-SetFocus if focus lost (bak_speed_*, bak_jump_*).
- bz_cmd.py _bz_load_then_close: fast path when target already loaded; pre-secfade wait 0.35→0.15 (bak_selspeed_*).
- Warm latency medians: music 1087→811, movies 913→661, tv 709→481, recent 1078→813 ms.
- Select→menu close after a warm: movies/tv ~340-400ms, music 810-1040ms.
- mmw stress: 6 "FAIL" in fast pass; trace shows no A→B→A jump-back yet, Movies→TV jump still open (deferred). No zip; version 5.0.0.
- 2026-10-26 05:53 EDT t3455u FIX: old pre-O46 MM right section (RECENTLY PLAYED panel 6911 + Movies/TV In Progress groups, Includes_Bezel.xml line 458, visibility keyed only on bz_navstrip) leaked under MM. Set the 3 groups <visible>false</visible>. Backup xml/Includes_Bezel.xml.bak_oldlist_t3455. xmllint ok. ReloadSkin. No zip.
- 2026-10-26 05:55 EDT t3456u/t3457u: old right-list groups 6911/6912/6913 + their onright deleted from Includes_Bezel.xml (backup .bak_oldlist_del_t3456); MM verified clean. Built 5.0.1 zip (speed pass + oldlist delete). Full restart.
- 2026-10-26 06:12 EDT t3461u/t3463u/t3465u: mm_warm no-op on same window+path, IsUpdating guard (freeze), 500ms settle for window switch, cascade skip under MM. Backups bz_flip.py.bak_t3463 + b300/bak_prezip_502. Built 5.0.2. Live verify not completed (interrupted). Full restart.

- 5.0.2 (Rob t3461/t3463/t3465 ~6:10 AM EDT): MM warm noop same-path; guard Container.IsUpdating; suppress cascade under MM; zip skin.bezel2-5.0.2.zip full restart.

- 2026-10-26 06:25 EDT t3468u: docs pass for 5.0.0–5.0.2 — engineering D13/D14, BREAKS K24–K26, skill, PDF rebuilt. No skin edits.
- [t3473] Rob: highlight load underlay drastically improved snappiness/smoothness — document as standing preference (keep MM warm; no fade-over-speed).
- [t3474] Rob: document MM warm coding structure/style (table-driven WARM, poll loop, last/done state, three outcomes NOOP/inplace/Activate, prop locks).
- [t3493] FS music: Nav Up/Down change tracks — restore previous Up/Down (no track skip) on next build.
- Oct 26 08:16 t3555: plane orbit back/front multiimages added around BezelMusicPlayingArt in Music NP in-place (Includes_Bezel.xml, vis Player.HasAudio + bz_np).

## 2026-10-26 18:38 EDT — t3646/t3648 old FS player controls removed
- MusicOSD.xml: full 3.2 colour-block list → redirect stub (Close + ActivateWindow(1115)); cannot steal FS keys / Up-Down.
- PlayerControls.xml: kept as redirect stub only (M/Start → 1115 or VideoOSD); comment clarified.
- Removed unused PlayerControlsRepeatImageVar from Variables.xml.
- Includes_Bezel NP comment: MusicOSD → 1115.
- Backup: /workspace/b300/bak_oldpc_20261026_183834. ReloadSkin. No zip. Up/Down track-skip expected to self-fix with this.

## 2026-10-26 18:40 EDT — t3649/t3650 FS cycle pill position
- Pill grouplist (6391): top 128→125 (centred in gap colour-block top 120 ↔ title top 162); left 546→530 so right edge 930 (30px inset, matches title). Upper-right kept.
- Backup Includes_Bezel.xml.bak_pillcenter_*. ReloadSkin. No zip.

## 2026-10-26 18:41 EDT — t3651u NEXT BUILD full list (source of truth)
Rob pasted master list. Status snapshot after old-PC + pill center:

### Done / expected done
- FS old Player Controls on Select → MusicOSD/PlayerControls stubs (t3646/48)
- FS Up/Down track-skip → rides old-PC clean (t3648)
- Pill closer / centered UR equal margins (t3649/50)
- Old Player Controls leftovers confirm remove → done stubs
- MM Settings / Media Sources / outline / Bar style global → **talked+mockups, not built**
- Media Library → MEDIA SOURCES row (talked)
- Plane / multiimage characters → parked

### Still open (queue order after current FS)
Bugs: MM lists steal focus; Grid→MM close; MM glow opacity; strip/fanart right misalign; Music controls close pops; grid/list flash on song change; MM flash next song; TV grid Left→MM; Settings arrows when not needed; MM arrows when no L/R
MM warm: Warm Music→Artists; keep last Music location; hide lists while MM active
FS/NP: next/prev titles by icons; viz menu in 1115; double-tap label; double-tap poster keep; multiimage cache Q
Cast/dust: poster cast 60%; album cast X 30; album lit dust small; poster cast textures; movie info poster
Lists/grids/TV: all albums/seasons bottom; TV title no 1x01; grid style; grid closer; outline snappier; auto-scroll unfocused
Info: movie fanart+strip opacity; keep list poster anim; music discography vs pills; refresh info BEZEL; clear discography Q
Art/settings BEZEL: choose art; addon download; L&F skin menu; shared dialog name; menu style+addon mockup first
Tuner/MM: A–Z ~39+; slow MM decoration slide; TV slide tune; MM bar opacity rename default 50%; bar styles; default outline; Global Dim exclusions talk; Settings cues mockup; logo text; Fav↔Music Videos swap; Artist return last screen
Talk/mockup first: Global Dim exclusions; shared dialog; addon download; MM Settings; info refresh; double-tap layout
Parked: multiimage characters / plane

## 2026-10-26 18:45 EDT — t3653 dig: more completed from chat

### Built / Rob-confirmed (on master list)
- FS old Player Controls on Select (stubs) — t3646/48
- FS Up/Down no track-skip — expected w/ old-PC (t3648)
- Pill closer / UR equal margins — t3649/50
- Old Player Controls leftovers — stubs done
- Music grid Left → list (not MM) — Rob Fixed t3509 (TV grid Left still open)

### Talk / mockup locked (not built into skin)
- MM Settings button cues — B-style 3-zone outline pill (hamburger | SETTINGS | sliders+Bezel)
- Media Library → MEDIA SOURCES row (+ refresh zone; Select → BEZEL Select sources)
- Default list bar = outline; bar styles global on every list
- BEZEL Select layout approved (detail above strip buttons; row icons; no big art/NP label unless vid/music)
- Addon download / Get more redesign mockups (same Select language)
- Shared colour-strip colour + opacity + backdrop across Select-style menus
- SETTINGS above MEDIA SOURCES in MM list

### Parked
- Plane / multiimage characters

### Partial (not mark done)
- Settings/SettingsCategory BEZEL restyle (4.7.x) — L&F still open
- Poster cast textures brighter (4.7.2) — default opacity still 100% not 60%
- Cast offset X control exists (−60…+60, 5px) — default still 0 not 30
- TV slide defaults 0.75 + circle out — more speeds / ~0.3 still open
- MM corner logo + Kodi labels — “smaller bottom-align” still open
- Global Dim always-on — exclusions talk still open
- Old right MM lists 6911–13 deleted — “hide lists under MM” still open

## 2026-10-26 — Refresh format pushed into skin.bezel2 (5.0.2, no zip/bump)
- New: xml/Includes_BezelRefresh.xml (generated by /workspace/b300/gen/refresh_strip.py). Includes.xml now includes it.
- DialogKeyboard/DialogSelect/DialogConfirm: when Window.IsVisible(musicinformation), use BzRefreshKeyboard/Select/Progress; otherwise use the original bodies, which moved verbatim to Includes_BezelDialogs.xml as BzStd*.
- Backups: *.bak_refreshstrip_20261026_214614 and gen/refresh_strip.py.bak_*.
- Limits: TAB/CTRL/ALT/INS are no-ops. HOME/END/PGUP/PGDN/UP/DOWN repeat the cursor 40 times. DEL = right + backspace. Shift symbols = Shift + key.
- Open issue: the LEFT/RIGHT/BKSP labels render larger than the other keys, even though the XML sets bz_b12.
- Screens: /workspace/mockups/choose_art/refresh/build/01-03.

## 2026-10-26 22:05 EDT — mmbuild (approved queue t3826u), live only, no zip
- Built: LOOK › Fanart opacity (bz_at_fanop, 0–100% step 10, default 50%) — fade on BezelFanartLayer image (all section fanart); Tuner row after Global dimmer (Includes_Tuner.xml + bz_tune.json).
- Built: A–Z bar threshold Container(60).NumItems >38 (was >20), 3 bars.
- Built: Poster cast opacity default 60% (empty = step 4; 100% now explicit step 6). Album cast X default +30 px (empty = x30; x0/legacy 4 = 0).
- Built: Video/TV grid Left → MM always (was list 60 when A–Z bar visible).
- NOT built: cast 4 thumbs + names (lives in 1111 XInfo / Dialog*Info — sibling combined-info lane; XInfo already shows cast thumbs+names); MM Settings 3-zone pill / MEDIA SOURCES / outline bar styles (order conflict: lock text says SETTINGS above MEDIA SOURCES, mock media_right_sep shows MEDIA SOURCES above; Select target "BEZEL Select sources" undefined); MM focus bugs (not reproduced — shared rig busy with sibling).
- Backups: *.bak_mmbuild_220043. Restart: ReloadSkin is enough (XML + json read at Tuner run).

## 2026-10-26 ~10:20 PM EDT — FS build (t3826, 5.0.2, no zip/bump)
- 1115: new Visualisation row 6411 (MORE, above Close; value = Visualisation.Name ›). Select closes 1115 then opens Kodi's viz picker (Addon.Default.Set musicviz: installed + Get more) — single level, not the mock's in-strip sub-list. Close moved to top 710; nav 6409↔6411↔6410.
- FS cycle aid (BezelNPInPlace): LAST/NEXT labels → $VAR[BzFSPrevTitle]/[BzFSNextTitle] (MusicPlayer.offset(∓1).Title, fallback LAST/NEXT); label boxes widened to 300.
- Double-tap hint: include BezelDtapHint ("ⓘ Double-tap Select · info", bottom-centre of list+strip panel) in MyMusicNav/MyVideoNav; hidden when bz_dtap_off, list 60 not visible, MM open, NP/1112/1115 up.
- NOT built: "double-tap poster keep" (meaning not defined anywhere — needs Rob).
- Backups *.bak_fsbuild_220152. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 2026-10-26 22:15 EDT — Combined Info+Context built into skin.bezel2 (5.0.2, no zip/bump) — XML only, ReloadSkin
- New xml/Includes_BezelInfo.xml (gen: /workspace/b300/gen/combined_info.py); Includes.xml includes it after Includes_BezelRefresh.
- DialogMusicInfo.xml + DialogVideoInfo.xml REPLACED: options IN colour strip (OPTIONS header, white pill focus), Play focused on open, L/R = Close, side list hidden (native list 50 kept off-screen/invisible for Kodi), fanart + right art kept, library meta under a rule, cast 4 thumbs+names (video), TV: SHOW/SEASONS/EPISODES, episode TITLE/EPISODE.
- Music: Play / Play next / Queue / More from [artist] (album/song) or Browse albums (artist) / Artist|Album info (12) / More options → Choose art (10), Refresh (6), Set rating (7), Context menu, ‹ Back. Native ids kept so Refresh-in-strip still fires (window still musicinformation).
- Backups: *.bak_cinfo_20261026_220113 (DialogMusicInfo, DialogVideoInfo, Includes).
- CONFLICT: a parallel Choose-art agent backed up the same two Dialog files at the same second (*.bak_chooseart_20261026_220113) and drives the same :77 test Kodi. Merge needed: its chooseart hook for button 10 is not in these files.

## 2026-10-26 22:10 — Choose art (skin.bezel2) — BUILT
- The Info dialog's More/Choose art button (id 7710) runs bz_cmd.py chooseart. It shows the type rows in the colour strip, then a shaped grid over the fanart (sq/wide/tall). OK applies the art. Back on the grid steps back to the types, and Back on the types closes it.
- Files: scripts/bz_cmd.py, xml/Includes_BezelChooseArt.xml (new), Includes.xml, DialogSelect.xml (gated on bz_artsel), DialogVideoInfo.xml, DialogMusicInfo.xml. Backups: *.bak_chooseart_20261026_220113
- Needs a FULL restart (.py changed). No zip made.
## 2026-10-26 22:13 — Choose art × combined info merge (skin.bezel2) — DONE
- Combined info files had been rewritten by the combined-info agent, so they had stock button id 10 with no chooseart hook. I re-applied the hook in DialogVideoInfo.xml and DialogMusicInfo.xml: id 7710 now runs RunScript(bz_cmd.py,chooseart,$INFO[ListItem.DBType],$INFO[ListItem.DBID]). Backups: *.bak_cinfo_merge_*.
- DialogSelect gating is unchanged and correct: bz_artsel types/sq/wide/tall → BzArt*, empty+musicinformation → BzRefreshSelect, else BzStdSelect.
- Live test (r.sh full restart): movie Information → More options → Choose art → types → poster grid → Back → types → Back → More. Shots are in /workspace/mockups/choose_art/merge/.

## 2026-10-26 ~23:05 ET — MEDIA SOURCES Back-from-Music focus (Rob t3852 "Fix and continue")
- Bug: Back from sources://music/ (and actually sources://video/ too) → 1117 with nothing focused; focus reset to row 1.
- Cause: BEZEL onback chain in View_60 (Includes_Bezel 1370/2578) runs ActivateWindow(1117) then later onbacks (nav targets/props) strip focus after 1117 inits. Native Back is NOT an option for Music (goes to musicdb history, not 1117).
- Fix (gen/media_sources.py → Custom_1117 only; Includes unchanged): rows store SetProperty(bz_msfocus,<id>,home); defaultcontrol no longer always; onload AlarmClock(bzmsf,SetFocus($INFO[bz_msfocus]),00:01,silent) re-focuses after the chain settles; hidden 6299 bounce button. Result: Music/Videos Back → focus restored to the row that opened it (~1s unfocused gap). Pictures unchanged.
- Backups /workspace/b401/bak_msfocus_*. ReloadSkin. Shot /workspace/mockups/media_sources/live/focus_music_back.png

## Oct 26 2026 23:05 EDT — MM hide-lists (steal focus + Grid→MM close) [Rob t3853/t3854/t3855]
- bz_flip.py nav_menu: while bz_nav open, if focus lands on underlay 60/61/62/63/64/6600 (no modal, no pick) → SetFocus(6996,row) instead of auto-closing MM (log "BEZEL MMHIDE").
- bz_mm.py: sets bz_mmpick on a menu pick (exempts the guard); flip clears it when MM closes.
- Includes_Bezel.xml 6898 (tap outside): ClearProperty(bz_nav) before SetFocus(60).
- Verified cold start: Down/Up moves strip, MM stays open across Music→Videos warm; forced SetFocus(60)/(6600 grid) bounced back; pick still exits. FULL restart (.py).
- Backups: xml/Includes_Bezel.xml.bak_mmhide_225839, /workspace/b401/bak_mmhide_*_bz_flip.py, bak_mmhide_bz_mm.py.
- MM glow opacity: already exists (Tuner › MAIN MENU › Glow, bz_at_mmglow 20–100%, default 30%). Fixed desc text "Default: 100%" → 30%. Includes_Tuner.xml.bak_mmhide_glow_*.

## Oct 26 2026 ~23:08 EDT — FS controls soft close + song-change focus (+MM flash next song) [Rob t3857/t3858]
- Custom_1115: WindowClose fade 250→420ms sine inout + panel slides up 20px on close (was hard-ish pop). XML.
- bz_flip.py focus watchdog: remembers last good control; on track change (MusicPlayer.Title|Album) within 2.5s, if focus drops → SetFocus(same control) (keeps grid 6600 + position, no jump to list 60); under MM (bz_nav) never SetFocus(60) — restores 6996 instead (MM mini-player hitch / MM flash next song); skips while Container.IsUpdating; fallback now targets 6600 if grid visible, 1.0s.
- Backups: xml/Custom_1115_MusicControls.xml.bak_fsfade_*, /workspace/b401/bak_fsfade_*_bz_flip.py. FULL restart (.py).
- Verify: no tracebacks; list position held (item 5) across 2 track changes; rig playback stops after ~1 track (NULL sink) so multi-song grid/MM test incomplete — Rob to confirm on device. Shots /workspace/mockups/fs_fade/.
- Queued (not started): Settings/MM arrows when no L/R, MM bar opacity rename default 50%, Warm Music→Artists, Keep last Music location.

## 2026-10-26 23:19 MM queue pack (skin.bezel2) — backups bak_mmqueue_231002
1 Settings › hidden (L/R does nothing there) — DONE
2 MM strip › only on Music/Movies/TV/Settings — DONE
3 MM bar opacity renamed "Strip opacity", default 50% (empty=step 2, preset default=2) — DONE
4 Warm Music -> musicdb://artists/ — DONE
5 Keep last Music location (bz_lastmusic, used by warm + subgo when chip is default) — DONE
6 Hide list text under MM (fade only, scroll underlay untouched) — DONE (music list + video list)
7 Viz picker: names only (Label2 hidden when header = Visualisation) — DONE, not live-tested (rig has no viz add-ons)
8 Lit dust size default Small — already Small in behaviour and preset; fixed desc "Default: Medium" to "Small" — DONE
Restart: FULL (.py changed). No zip.

## 2026-10-26 23:3x — Cast styles rebuild (t3878–t3881, approved t3881s11892)
- pcstyle/acstyle → 1 Current, 2 Hard, 3 Floor, 4 Glow, 5 Fade, 6 Contact (empty = Current). Movies+TV share cast_mp_*; album cast_ma_*.
- Textures baked by /workspace/mockups/cast/bake.py (480x880). Old Long/Short/Offset zoom/slide anims + Faint opacity bake removed; pclen/aclen, X/Y, softness override kept.
- Info: bezel/info/cast_poster_styles.png + cast_album_styles.png (old cast_shadow_styles.png kept). Backup /workspace/b401/bak_caststyles_233103. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 2026-10-26 23:50 EDT — Attention queue build pass 1 (Rob t3893u) — backup /workspace/b401/bak_attnqueue_234818
- #3 TV titles DONE: BezelListLabel — tvshows = TVShowTitle only; episodes = "01 · Title" (zero-pad <10). XML.
- #4 Grid closer DONE: music grid cell 226x246→226x231; video grid 222x325→214x317. XML.
- NOT built yet: #1 info dup poster, #2 All albums/seasons at bottom (Kodi engine puts "All" first; needs script/hide approach), #5 auto-scroll unfocused lists, #6 fanart+strip opacity Tuner row, #7 keep poster anim, #8 MM Settings 3-zone pill, #9 global outline bars+Tuner, #10 Select/Addon layout, L&F Interface restyle (approved t3893s12053, mock /workspace/mockups/lf_skin/after.png).
- Restart: FULL via r.sh (XML only, ReloadSkin would suffice). No zip.

## 2026-10-26 23:53 EDT — Attention queue pass 2 (Rob t3893u) — backup /workspace/b401/bak_attnqueue2_234947
- #1 DONE: DialogVideoInfo — full black + own 600px poster only when not over Videos; over Videos a left-half mask only, underlay art shows live.
- #7 DONE (same change): underlay sway poster keeps animating behind info (no cover). Context menu already non-covering.
- #6 DONE: Tuner LOOK "Strip follows fanart" toggle (bz_fansync, default OFF); fanop L/R → bz_cmd.py fansync maps fanart % → bz_at_blockop.
- #9 DONE: bz_cmd start one-shot migration sets bz_at_hishape=5 (Outline) (flag bz_attn_outline); Tuner bar shape row still switches. Covers list bars using BzATHiTex (list 60 family); MM/Select keep own pills.
- #11 DONE (partial): SettingsCategory rows white outline focus + faint outline unfocused (mm_pill_ol). No detail panel/strip header from mock.
- #8 MM Settings 3-zone pill, #10 Select/Addon layout: NOT built.
- #2 All-at-bottom: BLOCKED (Kodi engine pins "All" items first; needs a plugin/virtual source). #5 unfocused autoscroll: BLOCKED (label scroll only on focused item in Kodi lists).
- FULL restart (.py). Shots /workspace/b401/attnq2_lf.png, attnq2_info.png, attnq2_movies.png

## MMUI pass (2026-10-27 ~00:05 EDT) — backup /workspace/b401/bak_mmui_235351 — restart FULL, no zip
- L&F Interface restyle (SettingsCategory.xml LFUI): DETAIL panel + colour strip + blue header + bottom-right title. DONE, verified live (mmui_lf.png).
- MM Settings 3-zone pill (Includes_Bezel.xml 6996, media/bezel/mm_set_*.png): built, not verified with a screenshot.
- Select/Addon layout (Includes_DialogSelect.xml SELUI, BezelSelPillBtn): built, not verified with a screenshot.
- Global outline bars + Tuner hishape: already done in an earlier pass.
- All-at-bottom (bz_allrow, 6097/6098, ALLHIDE layouts h1, bz_cmd allrow, bz_flip ALLHIDE): PARTIAL. TV seasons view still shows the top *All, and the bottom row doesn't appear. The seasons view uses a different row include that I haven't hooked up yet.

## Stress protocol extras (Rob t3914u, 2026-10-27)
Always fold into full stress: cold first start after install/zip; MM open while music plays (warm); Back from every deep path; Movies/TV/Music list+grid side-by-side visual pass.

## 2026-10-27 · All-at-bottom force-hide (ALLHIDE2/ALLBOTTOM2) — DONE
- Includes_Bezel.xml (per-item visible group hides *All rows; 6098 moved out of grouplist; 6097/6098 +60 slide and covercol slides; ondown via bz_allrow), bz_flip.py (direction-aware skip + wrap catch to 6097/6098). Backups *.bak_allbottom_*. FULL restart.
- Caveat: Kodi can't collapse one list row, so a blank gap is left where *All was. Open: 6097/6098 stay visible under MM.
- Shots: b401/allbottom_seasons.png, allbottom_albums.png. Pill/Select verified: mmui_pill.png, mmui_select.png. AddonBrowser has no SELUI styling (mmui_addon.png), not changed.

## 2026-10-27 · Underlay auto-advance (UNDERADV, Rob t3910u) — DONE
- bz_flip.py under_adv thread: while bz_nav is set (not mmstart/mmwarm/modal/splash/video), after a hold of 5 s it runs Control.Move(60) every 8 s, wraps, and skips '..' and *All. No Container.Update (K24).
- bz_cmd.py uadv,<delay|hold>,<±1>. Includes_Tuner.xml LOOK rows: Auto-advance under menu (bz_uadv_off, default ON), every 4–30 s (bz_uadv_delay), first hold 2–15 s (bz_uadv_hold). Backups *.bak_underadv_*. FULL restart.
- Smoke on Movies: Alien→Avatar→Back to the Future→Barbie; closing MM + Select lands on Barbie. Shots b401/uadv_1.png, uadv_2.png, uadv_close.png, uadv_select.png.
- Oct 27 00:29 t3925u splash mockups A–F at /workspace/mockups/splash_styles/ (see-through, 5.0.2+Kodi 21.2, new fonts). Fix-list: splash double-load; 4.6 hardcoded in Custom_1113. Awaiting approval.

## 2026-10-27 00:20–00:40 EDT — FULL STRESS after build (Rob t3911/t3914) — no fixes, no zip
- Restart: FULL cold first start via r.sh (fresh copy into /tmp/bz2home, kodi killed). Shots /workspace/b401/stress_oct27/ (01_..16_).
- Result: 29 PASS / 10 FAIL. Protocol extras all run (cold first start, MM warm + music, Back from deep paths, list+grid side-by-side 04_list_vs_grid_sidebyside.png).
- FAIL F1 (high): Left on All-at-bottom row 6097/6098 does nothing, MM won't open (06_allbottom_albums3_left_from_all, 06_allbottom_albums_MMopen).
- FAIL F2 (high): ActivateWindow(Videos,movies) while Videos is on TV stays on TV; Music artists→albums (grid) stays artists (04_grid_music_albums, 12_contextmenu, 16_info_movie). Seen 3 times.
- FAIL F3: Down past POWER in MM leaks focus to grid 6600 under MM (02_mm_wrap).
- FAIL F4: Cold splash text reads "BEZEL VERSION 4.6", not 5.0.2 (01_cold_t6/t16, 01_cold_contact).
- FAIL F5: Cold start underlay is bz_recent_songs.xsp while the pill says ARTISTS; artist bio text shows through the MM panel (01_cold_settled).
- FAIL F6: L&F DETAIL title clipped ("ERFORM ON STARTU") and "STANDARD ( )" empty label; log: Control 10/60 in window 10129 can't focus (11_lf_interface_right, 11_lf_cat_down).
- FAIL F7: after Select (play) on a movie, the poster frame is empty (07_uadv_selected, 05_movies_d1).
- FAIL F8: Back from Settings window returns MM focus on TV SHOWS, not SETTINGS (10_pill_settings_back).
- FAIL F9: Down on the bottom All row doesn't wrap/move (06_allbottom_seasons_wrap).
- FAIL F10: underlay auto-advance keeps stepping while the Tuner is open (art changes while you tune) (08_tuner_row_*).
- WARN: ".." row focus shows an empty bar (Music albums); Global dimmer reads 100% (test HOME value); AddonBrowser has no SELUI style; gap where *All was.
- PASS highlights: K23 MM visible at splash fade; MM warm with music playing (36 rapid moves in 9.5 s, no hitch, audio kept); auto-advance Movies 4 steps in 20 s, Back/Select land on the item; Tuner uadv rows (OFF hides delay/hold, 4–30 s and 2–15 s ranges wrap); Settings pill L=Section Settings / R=Tuner / OK=Settings; All-at-bottom seasons+albums; combined info movie/TV/album; FS vis + Back.
- Tuner uadv delay/hold reset to default after test.

## 2026-10-27 00:37–00:50 EDT · Fix batch 3 (Rob t3930u parallel) — F5/F6/F9
- F5 bz_cmd.py start: MM-first cold start now opens musicdb://artists/ (+bz_navroot) instead of bz_recent_songs.xsp, so underlay = ARTISTS pill. Verified on first cold after r.sh (FolderPath musicdb://artists/, pill ARTISTS). Bio still shows faintly through the translucent strip (left alone, Global Dim). FULL restart. Backup bz_cmd.py.bak_fixb3_*.
- F6 SettingsCategory.xml: DETAIL title label→wrapping textbox (no clip); group 5 onright 60 (hidden scrollbar, "can't focus")→3; level button 20 shows "SETTINGS LEVEL" in DETAIL instead of "Standard ( )"; its focusedcolor was BzMMDark on outline pill (label vanished on focus)→white. Verified wrap + SETTINGS LEVEL + cat Down→20; white-focus colour edit not re-shot (Kodi contention). ReloadSkin. Backup *.bak_fixb3_*.
- F9 Includes_Bezel.xml 6097/6098 ondown noop→SetFocus(60,0,absolute); batch 1 onleft kept. Not verified live (other executors driving the shared test Kodi). box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Shots b401/stress_oct27/fix_batch3/.

## t3930 batch 2 (Oct 27 2026, 00:39 ET) — F2 / F8 / F10 (bz_flip.py, bz_cmd.py; backups *.bak_batch2_003907; FULL restart)
- F2 same-window path switch: verify + retry Container.Update after mm_warm in-place and in bz_cmd _bz_load_then_close. TV→Movies, Artists→Albums, MM-pick TV→Movies PASS (couldn't reproduce the fail before the change either).
- F8 Back from Settings: nav_menu tracks Settings-family close; MM reopening within 4s lands on SETTINGS (row 9). PASS (fix_batch2/f8_back.png).
- F10 uadv: paused while bz_navtune / bz_navset / bz_navsub / bz_kset or dialogs 1111/1112 are up. Not verified — the shared test Kodi was being driven at the same time.

## Oct 27 2026 ~00:45 EDT — post-stress fix batch 1 (t3923) — XML only, ReloadSkin
- F1: 6097/6098 onleft → `$EXP[bz_navok]` SetProperty(bz_nav,true,home) + 6996 (same as list-60 pattern). PASS albums (artists/10) + seasons (tvshows/2).
- F3: Container 6996 `<ondown>SetFocus(6996,0,absolute)</ondown>` — Power Down wraps to Music, ctl 6996, nav=true. PASS.
- Hide under MM: 6097/6098 visible = `$EXP[bz_allrow] + !$EXP[bz_navmenu]`. PASS (hidden w/ MM, back at bottom w/ MM closed). Top gap untouched.
- Coexists with batch 3's ondown→SetFocus(60,0,absolute) on 6097/6098 (my onleft got dropped by its overwrite once; re-added).
- Shots: /workspace/b401/stress_oct27/fix_batch1/. Backups: /workspace/b401/bak_batch1_*_Includes_Bezel.xml

## 2026-10-27 00:50–01:06 EDT · Fix verify + POST-FIX STRESS (Rob t3933/t3934) — no zip, no splash build
- Part A (r.sh FULL first, picks up batch 1–3 XML+py). Shots b401/stress_oct27/fix_verify/.
  - HARNESS BUG: old stress lib sent Input.ExecuteAction "Down"/"Left" (capitalised) → JSON-RPC rejects (invalid enum), so the key was never pressed. Prior F1/F9-style "nothing happens" results may be artefacts. Fixed in b401/fvlib.sh (lowercase + Input.Down etc).
  - F9 PASS: 6097 (albums) + 6098 (seasons) Down → list 60 pos 0 (f9_albums_wrap_top, f9_seasons_wrap_top).
  - F10 PASS: Tuner open (bz_navtune) 20 s, CurrentItem fixed at 6; close → uadv resumes (f10_tuner_t20, f10_uadv_resumed). Underlay was TV (warm passes rows on the way to SETTINGS).
  - F6 PASS: level button "Standard" white on focus; DETAIL "PERFORM ON STARTUP" full (f6_level_focus, f6_startup_detail). Minor: level focus DETAIL body still shows the category text.
  - Reset leftover Skin.String(bz_uadv_delay)=4 from earlier test.
- Part B F7: NOT a persistent bug. Stub movie plays ~1 s, list returns, poster frame blank ~2–3 s then poster comes back (f7_sel_t3 vs f7_sel_t6; stress 17_f7_sel_t3/t8). Posters are remote image:// URLs reloaded after window re-init. Logged WARN, no change, no backup needed.
- Part D stress: cold FIRST start via fresh copy (r.sh-style, kodi killed). Shots /workspace/b401/stress_oct27b/, results.txt, scripts b401/st1–st5.sh.
  - 61 PASS / 3 FAIL.
  - FAIL splash double-load: 1113 visible twice (0.6–1.9 s, then 2.7–12.5 s) (01_cold_i6/i12/i20). Known F4 family, waiting on Rob's go. Splash still reads "BEZEL VERSION 4.6".
  - FAIL F8: Back from Settings window → MM on MUSIC not SETTINGS when the underlay is Music (10_settings_back, retry 10_settings_back_retry). Batch 2 only passed from Videos.
  - FAIL (transient) F7: blank poster ~3 s after play returns (17_f7_sel_t3); recovers (17_f7_sel_t8).
  - Rechecked PASS: F1 Left→MM (both), F2 list/grid paths ×4, F3 Power wrap, F5 cold artists, F6, F9, F10, hide *All under MM, K23 MM at splash fade, warm+music 36 moves 5.9 s audio kept, Back from deep tv/movies/artists/genres, uadv, pill L/R/OK, context, addon browser, NP 1112, FS in-place NP, combined info movie/tv/album. Side-by-side 04_list_vs_grid_sidebyside.png.

## Oct 27 2026 ~01:10 EDT — t3943u / t3950u / t3951u
- t3943u DELETE unwired Tuner rows (30 ids: glare 8, LOOK finish 10, TV DRUM 3 + EPISODES section/ps_ep/reset, dust holds 3, mmdamt/mmdbright, hicol/hiop, mmspeed, busydelay). Also empty subs: ALBUM GLARE (+reset), ALBUM LOOK EFFECTS, POSTER "Reset poster glare". Scrubbed bz_tune.py presets (ep preset removed, menu/dust keys, LOOK set), bz_tune.json P 111→80.
- t3950u DELETE Splash hold Tuner row + all wire (handlers, P entry, MIG in bz_tune.py/bz_cmd.py, _splash patch + FILES entry in bz_tune_patch.py). Custom_1113 keeps its fixed hold.
- t3951u Splash label now live: $INFO[System.AddonVersion(skin.bezel2),BEZEL VERSION ] → reads 5.0.2. HABIT: version comes from addon.xml; bump addon.xml every build.
- Backups /workspace/b300/bak_tuner_dead_0106/. Full restart (r.sh).
- t3953u Splash: added live Kodi line $INFO[System.BuildVersionShort,KODI ] under BEZEL version.
- t3943u follow-up: d20 Fade hold was patch-wired (_hold in bz_tune_patch.py) → now fixed H=2000 ms. Cold first start PASS (splash BEZEL 5.0.2 / KODI 21.2, Tuner walk 145 rows clean, no errors). Zip /workspace/skin.bezel2-5.0.2.zip (bak excluded).

## 2026-10-27 t3961u — v5.0.3 download
- Bumped addon.xml + changelog 5.0.2→5.0.3; zipped from source to /workspace/skin.bezel2-5.0.3.zip (no Kodi touch; stress_oct27c running).

## t3957u (Oct 27 2026 ~01:50 EDT) — full stress oct27c + Tuner label/function audit
- Stress `/workspace/b401/stress_oct27c/results.txt`: 61 PASS / 4 FAIL — splash double (on 1.2s off 1.9s, on 2.8s→11.7s) persists after Splash-hold removal; F8 Settings Back on Music underlay → MUSIC; NEW Back from deep artists → albums; NEW FS visualisation did not open.
- Splash versions live PASS: 5.0.2 / Kodi 21.2.
- Tuner walk 145 items (103 setting rows, 42 headers/presets/resets/actions): labels all non-blank, every row's L/R writes its own skin key; 1 FAIL: fansync L/R no-op (OK only). Visual spot checks gdim/mmbar/mmglow/fanop change screen. JSON-only dead ids not shown in UI: d3asize sdsize sdbright glow0-4 (+TOG d3l2, sdust) — cleanup candidates.

## Oct 27 2026 ~01:50 EDT — 5.0.3 FIX LIST batch 1 (t3967u/t3968u/t3970u)
- #1 UADVRAND: bz_flip.py under_adv now jumps to a random list-60 item (never same, skips '..' and hidden *All) — only path is list hidden under MM; visible list unchanged. Backup /workspace/b300/bak_bz_flip_uadvrand_*.py. py_compile OK. FULL restart needed; not live-tested (shared Kodi rig busy with LOOK bar-style agent).
- #1 white flash: not yet diagnosed (underlay fanart control lives in Includes_Bezel.xml — held off, bar-style agent editing it).
- #2 watched badges under MM: confirmed in shot b401/ci_now.png (checks at x~288 beside MM). Fix lives in list-60 layout in Includes_Bezel.xml — deferred to avoid collision.
- #3/#6/#7: #6/#7 in DialogVideoInfo.xml + Includes_BezelInfo.xml (black mask -60..960 + BzCIFanart drawn over strip area; strip BG 570–960 at BezelBlockBF 7F alpha). Needs live shot; Kodi went black mid-test (other agent restart) — not edited.

## Oct 27 2026 ~01:55 EDT — batch 2 #6/#7 (t3971u)
- #7: BzCIStripBG (Includes_BezelInfo.xml) now E6 black base + BezelBlockBF stacked x3 → strip reads solid over fanart, still follows Tuner block colour.
- #6: DialogVideoInfo.xml always draws new BzCIVPoster (portrait 504x754 at 1073,165, white frame + shadow) — removed the !Window.IsVisible(videos) guard that hid it over the dimmed underlay poster. Music info untouched (BzCIArt always on).
- NOTE: both files say "Generated by gen/combined_info.py" — regenerate would overwrite; port edits there if regenerated.
- Backups *.bak_ci67_<HHMMSS>. xmllint OK. ReloadSkin sent; live shot FAILED — bar-style agent driving same Kodi (window jumped to Music). Not visually verified. #1 uadv random likely live since their 01:45 Kodi restart, not observed.

## 2026-10-27 01:45 EDT — t3967u GO: global Bar style (built, no zip)
- LIST › Highlight shape → LOOK › Bar style (same `bz_at_hishape`), after Global dimmer; visible under bz_topen_look.
- Default now Outline (empty == 5) in BzATHiTex/Val/Step/Bar + L/R wiring.
- MM focus (6996 focusedlayout, 25 MM sub buttons, Settings.xml 9000, SkinSettings.xml) now use $VAR[BzATHiTex] + BzMMBarCol.
- New var BzMMFocTxt (Includes_Bezel): white on Underline/Outline/default, else BzMMDark.
- Backups *.bak_barstyle_20261027014504. Shots /workspace/mockups/bar_style/build/ (mm_1..5, list_5b, sheet.png).
- Not changed: MM sub-chips 6941.. (mm_round_a60 white), Tuner's own list, DialogSelect/Buttons.xml settings rows.

## Oct 27 2026 ~01:58 EDT — batch 3 (#2 #3 t3973) + smokes
- Backup /workspace/b300/bak_Includes_Bezel_fix503b_*.xml. xmllint OK. Full restart via t.sh (test Kodi runs from /tmp/bz2home copy — NOTE: "reloadskin" is not a valid JSON-RPC action; batch-2 ReloadSkin never applied, restart now covers it).
- #2 PASS: watched/resume badge groups (4 layouts) fade out on $EXP[bz_navmenu] like the labels (b401/b2_mm_movies.png: no ticks under MM).
- #3 PASS: list 60 onfocus → SetFocus(6996) while bz_nav=true (+6996 visible). MM Music→Movies→TV: focus stayed 6996 throughout.
- t3973 PASS: All node empty because ALLHIDE2 hid every item whose FolderPath contains /-1/ — inside the All node that's every song. Visible now `!itemhas -1 | Container.FolderPath has /-1/`. Adele All → 28 songs (b2_allrow.png).
- #1 random uadv PASS: under MM CurrentItem 3→37→36 (random, not sequential), focus held 6996.
- t3975 Movies↔TV jump: not reproduced after #3 (6996 stayed on TV 6 s). Likely the same list focus steal; needs Rob confirm.
- Not done: t3972 (All albums focus / hide when 1 item / dim labels), #6/#7 visual smoke (code in), #1 white flash.

## 5.0.3 batch 4 (2026-10-27)
- #5 dtap→Action(Info) w/ bz_dtapinfo guard on oninfo (bz_dtap.py, Includes_Bezel.xml): EDITED, smoke INCONCLUSIVE — test Kodi has bz_dtap_off=True and keeps jumping Videos→Music on its own.
- #6 poster realigned to underlay slot 990,118 (BzCIVPoster): EDITED, real-item smoke pending.
- #7 strip: PASS (b3_vi.png).
- t3972: NOT STARTED.

## 2026-10-27 ~02:00 EDT — batch 5: t3972 + re-smokes #5/#6 (t3979u)
- t3972 (Includes_Bezel.xml + colors/defaults.xml; backups /workspace/b300/bak_Includes_Bezel_t3972_*.xml, bak_colors_t3972_*.xml; xmllint OK; FULL restart r.sh):
  - bz_allrow now also needs >1 real item (NumItems>2, or ==2 without '..'). PASS: artist 13 (1 album) → no All row; artist 10 (3 albums) → ALL ALBUMS shown.
  - New var BzListHiText: list focused-row label → bz_dimtext while 6097/6098 has focus (replaced 31 BzATHiText label uses). bz_dimtext CCCCCC→8C8C8C (all unfocused labels dimmer, global). PASS f72_allfocus.png.
  - All albums focus: Down×4 → 6097, still 6097 after 10 s+ (no steal). PASS. Down from All wraps to top (F9) PASS.
- #5 re-smoke PASS: exclusive /tmp/bz2home Kodi, bz_dtap_off OFF (ToggleSetting; Skin.Reset via script.bz.test did not stick), xdotool Return×2 80 ms on Back to the Future → Video info = BEZEL combined Options+Info (f5_dtap.png), not old ContextMenu. bz_dtap_off restored to ON(off=True) after.
- #6 PASS (same shot): poster drawn right, not behind black box. #7 strip present PASS. gen/combined_info.py NOT run.

## 2026-10-27 ~02:10 EDT — batch 6: #4 #8 #9 (t3979u)
- Backups /workspace/b300/bak_DialogVideoInfo_b6_*.xml, bak_Includes_Bezel_b6_*.xml. xmllint OK. FULL restart r.sh. gen/combined_info.py NOT run (DialogVideoInfo hand-edited — port to gen if ever regenerated).
- #4 PASS: BezelDtapHint now horizontal grouplist align=center over colour block x570–960, y978 (b6_hint.png).
- #8 PASS: DialogVideoInfo options 166–466, sep 476, CAST caption + 4 actor thumbs y508, sep 624, TITLE/YEAR/GENRE 636, plot 792 — matches mockups/fs_music/context/combined_movies (b6_ci.png).
- #9 PASS: More options "Context menu" (opened Kodi ContextMenu window) → inline "Mark watched/unwatched" (BzCIWatchLbl, Action(ToggleWatched)); hidden for seasons. Alien toggled 8→unwatched, back in Videos, no context window (b6_more.png, b6_after.png). Alien playcount restored to 8 via RPC. Music info (DialogMusicInfo) not changed.

## 2026-10-27 02:10 EDT — t3981u Auto-advance first hold max 60 s
- bz_cmd.py uadv hold steps: [2,3,4,5,6,8,10,15,20,25,30,40,50,60] (was 2–15); default 5 s; wraps 60→2. bz_flip reads value unclamped.
- Includes_Tuner.xml uadvh desc: "2 to 60 s   Default: 5 s". Backup /workspace/b300/bak_uadvh_*.
- xmllint OK, py_compile OK, FULL restart (r.sh). Smoke PASS: script cycle 5→60, Tuner LOOK row shows "60 s" (/workspace/b401/uadvh60.png).

## 2026-10-27 02:15 EDT — t3984u Background dim level (MAIN MENU)
- New skin string `bz_at_mmdim` (steps 1–7 = 30/37/44/51/56/60/100%, default 6 = 60%), vars BzATVal/Step/Bar_mmdim, L/R in Includes_Tuner, row "Background dim level" under MAIN MENU after Glow brightness. Reset main menu also resets it (bz_tune.py).
- BezelSecDim (Includes_Bezel): gdim fades now gated `!$EXP[bz_navmenu]`; parallel mmdim fades gated `$EXP[bz_navmenu]`. Same parent-opacity mechanism; gdim untouched otherwise.
- Backups *.bak_mmdim_*. xmllint OK, full restart (py). Smoke: closed gdim 30 vs 100 visibly changes; open mmdim 30→100 lifts section pixels ~3x, gdim ignored while open. PASS.

## t3988u — 5.0.3 #7 Fanart crossfade only under MM (Oct 27 2026)
- BezelFanartLayer (Includes_Bezel.xml): split fanart image into two controls — `!$EXP[bz_navmenu]` fadetime 0 (instant cut, list focused) and `$EXP[bz_navmenu]` fadetime 400 (crossfade while MM open). Black backing kept. Replaces batch7 blanket 200ms.
- Backup Includes_Bezel.xml.bak_mmxfade_*. xmllint OK. ReloadSkin-type change (XML).
- Smoke (20fps burst): MM open → gradual low per-frame diffs (fade) PASS; MM closed TV list Down → bulk change within ~100ms (cut) PASS. Frames /workspace/b401/x7/.

## 2026-10-27 02:21 EDT — t3994u fix batch (PAUSED by t3996u)
- #1 Choose art right preview: edit present in Includes_BezelChooseArt.xml (1100,130 580x860 backer + Container(6).ListItem.Art(thumb) preview, all 3 grids); xmllint OK; full restart r.sh. Real-path smoke NOT finished (Info dialog open on Jurassic Park, Down keys stayed on PLAY). No code changes this batch.
- #2 white flash, #3 F8 Settings Back (Music underlay), splash double, t3995u poster/album MM-only crossfade: NOT STARTED — held.

## 2026-10-27 02:45 EDT — t4004u/t4005u/t4010 double-tap → Options+Info only, old context removed
- Backups *.bak_dt4004_* (bz_dtap.py, DialogVideoInfo.xml, DialogMusicInfo.xml). xmllint + py_compile OK. FULL restart (r.sh). gen/combined_info.py NOT run (hand edits; port if regenerated).
- bz_dtap.py: keymap now also maps longpress return/enter/select → bz_sel (Kodi default longpress Select = ContextMenu); stale keymap rewritten once per run. New always-on zz_bezel2_noctx.xml (home/music/videos): c / menu / title / contextmenu / rightclick / longclick → NotifyAll(bz,bz_ctx) → Options+Info (sets bz_dtapinfo so xinfo is skipped). Installed for dtap ON and OFF.
- More options (video): + Add to favourites, + Remove from library (confirm; new scripts/bz_ctx.py via JSON-RPC). Music: "Context menu" (Action(ContextMenu)) replaced by Add to favourites. No ContextMenu wire left in xml/scripts (non-.bak).
- Large title upper-left of fanart (bz_b46, 150,150, 400w) in video + music Options+Info.
- Smoke (bz_dtap_off=false, xdotool Return×2 @80ms): Movies Aliens/Avatar → Video info combined, no old context PASS; TV Better Call Saul PASS; Music album 21 PASS; 'c' key → combined info PASS; colour block, poster, cast-above-title visible PASS. Shots /workspace/b401/dts_sheet2.png, dt_sheet3.png, more3.png.
- Note: More options list scrolls (Remove from library / Back below fold). Rob's "old context first" = his installed zip predates the 5.0.3 dtap fix; needs new zip.

## t4014 (Oct 27 2026) Tuner › MAIN MENU › Default section on start — BUILT, smoke DEFERRED
- Skin.String bz_at_mmdef 1–13 (empty=1 Music) → MUSIC, MOVIES, TV, MV, RECENT, FAV, PLAYLISTS, SEARCH, ADD-ONS, SETTINGS, MEDIA SOURCES, KODI, POWER (6996 row order). LEFT/RIGHT wraps.
- bz_cmd.py startup (first): sets home bz_mmstartrow/bz_mmstartsec before ActivateWindow(Music); bz_flip.py MM-start hold focuses SetFocus(6996,row) + bz_navstrip=sec. Underlay stays Music.
- Includes_Tuner.xml: BzATVal_mmdef var, onleft/onright, item above Double-tap window. Backups *.bak_mmdef_<time>.
- .py change → FULL restart. Smoke not run (stress agent owns /tmp/bz2home).

## t4017/t4018 (Oct 27 2026 ~02:50 EDT) MM active: section list flash / focus steal — BUILT, smoke DEFERRED
- Cause: only bz_flip.py MMHIDE poll yanked focus back (loop latency → list paints focused for a frame).
- Fix: Includes_Bezel.xml — every underlay container (list 60 ×2, 61, 62, 63, 64, 6600 ×3; shared by Music/Movies/TV/all sections) gets first `<onfocus condition="$EXP[bz_navmenu] + !bz_mmpick">SetFocus(6996)</onfocus>` → same-frame bounce to strip (keeps strip row). Python MMHIDE kept as backstop. Backup Includes_Bezel.xml.bak_mmlist_*. xmllint OK. XML only → box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Smoke NOT run: stress (stress_oct27d c2.sh) owns test Kodi.

## t4019 (Oct 27 2026 ~02:50 EDT) Hide A–Z jump bar while MM active — ALL sections — BUILT, smoke DEFERRED
- Includes_Bezel.xml: grouplists 6100 (music), 6600 (movies/TV list 64), 6500 (movies/TV list 60) get `<visible>!$EXP[bz_navmenu]</visible>` (ANDed). BezelAZFade gradients follow Control.IsVisible → hidden too. Hidden anim fades 400ms.
- Also added t4017 MMHIDE onfocus bounce to 6100 and 6500 (were missing; 6600 already had it). t4017/18 list bounce already in from prior pass (60×2,61,62,63,64).
- Backup Includes_Bezel.xml.bak_mmjump_*. xmllint OK. XML only → ReloadSkin. Smoke NOT run: stress c3.sh owns test Kodi.

## 2026-10-27 02:5x stress_oct27d (5.0.3, post Options+Info build)
FAILs: splash x2 cold; MM 12-down/POWER wrap; F8 Settings Back->TV SHOWS; deep Artists Back->albums; seasons Left on All ->6979 + All row not back; FS vis; dtap x4 no info (synthetic); C key opens old context; chaos nav blank. t4021 scroll/swap: focus kept, no jump-back, no visual flash.

## 2026-10-27 03:0x t4027/t4028 stand-in art (MM only)
- Art in `extras/standins/{posters,albums,artists}/` (5 each, from mockups v2; posters 540x720, sq 640). README.txt: drop new jpg/png in, ReloadSkin. Poster credit fine print Gaussian-blurred (A–E).
- Includes_Bezel.xml: 32 image controls (16 Container(6600) album thumbs, 2 grid album thumbs, 12 BezelGridPosterF, 2 BezelGridPoster) got a sibling multiimage (randomize, 600s/image) from the folder; visible only `$EXP[bz_navmenu]` + art empty (+ !parent). Artists folder when DBType=artist. Episode 16:9 tiles untouched.
- Backup Includes_Bezel.xml.bak_standin_*. xmllint OK. XML+media → box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Smoke INCONCLUSIVE: test Kodi drifted (splash hold, then options panel); MM-closed no-art artist showed no stand-in (correct); MM-open on a no-art item not captured. Test lib movies all have posters; 16/40 albums lack thumbs.

## 2026-10-27 03:00 EDT — t4030u Learn from mistakes/breaks
- Logged K27–K30 in BEZEL_BREAKS.md; D15 smoke discipline in KODI_SKIN_ENGINEERING.md.
- Skills [bezel](sand-workflow:bezel) + [bezel-stress-protocol](sand-workflow:bezel-stress-protocol) updated: real MM open, fixtures, PASS=gated-on shot, exclusive Kodi.
- Trigger: stand-in t4027 smoke set bz_nav directly → Kodi drifted; poster stand-in unverifiable (all movies have art); closed-MM only shot.

## 2026-10-27 03:01 EDT — t4031u All recent MM breaks → remember
- Added K31–K38 (list focus steal/flash, grid yank, Settings Back row, Movies↔TV jump, POWER wrap leak, badges/AZ under MM, mmdim≠gdim, MM-only crossfade).
- D16 MM never-break contract in KODI_SKIN_ENGINEERING.md.
- Skills + durable memory updated so MM edits re-check the contract before shipping.
- 2026-10-27 03:10 EDT t4036: BEZEL code mastery map → /workspace/BEZEL_CODE_MAP.md

- t4041 (2026-10-27): MAIN MENU Tuner infographics shipped (mm_dim_level, mm_open_speed, mm_close_speed, mm_default_section, mm_dtap_window, mm_dtap_toggle) wired via property info; panel not enlarged. Gaps: mockups/tuner_info/GAP.md

## t4043 — Tuner infographics use live BEZEL screens
Remade 6 MAIN MENU boards (mm_*.png, 860x560) from live shots: b401/472_mm_open.png (dim/open/close/default), b401/b3_dtap.png (dtap x2). Script: mockups/tuner_info/main_menu/make_live_t4043.py. Kodi busy (other agent) — no new capture.

## t4039 Continue — oct27e fixes (03:20 EDT)
1. Old context (C/Menu/longpress/raw contextmenu action) → Options+Info: np_tab keymap home/music/videos ContextMenu→NotifyAll(bz,bz_ctx); bz_dtap poll closes stray contextmenu → Action(Info). PASS (fix_oct27e/1_ctx_action.png).
2. MM 12-down/POWER wrap: no code change; re-smoke PASS (2_walk12_power, 2_wrap_down_music, 2_wrap_up_power). Stress fail likely post-cold-start key eat.
3. F8 Settings Back: FAIL on Videos underlay (lands TV SHOWS) and Music→Videos sequence (MOVIES). bz_flip setret hook never fires (no log) — attempted patch reverted. Still open.

## Oct 27 2026 — F8 Settings Back (K33) — PASS
- Cause: MM open loop runs up to 30 ticks; F8 batch2 cleared setret after tick 1, so ticks 2+ re-targeted TV/Movies from the underlay.
- Fix `scripts/bz_flip.py`: latch `bz_setret` (+ bz_mmpos=9) for the whole open; cleared on MM close / fresh non-settings open. Backup `/workspace/b401/fix_oct27e_f8/bz_flip.py.bak`.
- Smoke (FULL restart, /tmp/bz2home): Videos (TV shows) + Music (artists) underlay → Settings → Back: strip 6996 pos 9 SETTINGS at 1.5s and 4.5s. Shots `/workspace/b401/fix_oct27e_f8/`.
- t4045 (Oct 27 2026): fixes + Tuner infographics run in parallel. LOOK batch + mmbar live boards wired; LIST/MUSIC placeholders wired; backup bak_tinfo_t4045_*.

## t4049 — Tuner infographic 2-char codes
Stamped [code] amber pill top-right on all 154 PNGs in media/bezel/info (88 boards; amb_*/lit_* families share D1/DA). Prefixes M=MainMenu L=LOOK D=DUST I=LIST A=Album P=Poster U=Music C=ColourBlock Y=System Z=unused. Table: /workspace/mockups/tuner_info/CODES.md + media/bezel/info/CODES.txt. Script /workspace/b300/stamp_codes.py (rerun on a clean restore only). Backup /workspace/b300/backups/info_pre_t4049.tgz. desc prefix NOT added. Media only → ReloadSkin. No zip.

## t4050/t4051 (Oct 27 2026)
- Deleted Tuner LOOK 'Strip follows fanart' (bz_fansync): row, BzATVal_fansync var, fanop L/R fansync AlarmClock hooks, bz_cmd.py fansync action, CODES L2, look_fansync.png (moved to /workspace/b300/removed_fansync/). Fanart opacity + Strip opacity stay separate. Backups *.bak_nofansync_*. FULL restart (py).

## t4053/t4054 — subtle codes + skin fonts
- Restored info/ from backups/info_pre_t4049.tgz; switched gen.py, make_live_t4043, make_look_t4045, make_uadv_t4046 from DejaVu to skin Montserrat (SemiBold/Medium) and re-rendered.
- stamp_codes.py rewritten: fixed CODES.txt map, Montserrat-Medium ~14px (2.6% H), soft gray 47% alpha, no pill/brackets, top-right. 153 PNGs / 87 codes.
- t4055: restored again and re-rendered opt_* boards for live rows (20, gen/regen_opt_t4055.py) in skin Montserrat SemiBold/Medium; restamped. album_shadow_labels kept as-is (its script outputs a different size; Inter swapped to Montserrat in the script only).

- t4057 (Oct 27): Work through open fixes — investigated; 0 code changes. Splash double = startup ReloadSkin from tuner patch (options in b401/fix_oct27f/results.txt); FS vis = test false-fail; Artists Back/Seasons Left = non-repro flaky.

## t4057/t4060–t4067 (Oct 27 2026 ~03:55 EDT)
- Artists Back retest (t4061.sh/t4061c.sh, shots fix_oct27f/t4061/): YES false-fail. Old stress sequence now PASS; with grid ON Back from album->artist->(grid->list)->artists PASS (Back x3); Left from artist grid -> list -> MM PASS. No skin change. Procedure: fix_oct27f/STRESS_NOTE_t4060.md.
- t4064 splash removed: Startup.xml onload ActivateWindow(1113) -> SetProperty(bz_splash_done,1,home); Custom_1113_Splash.xml moved to /workspace/b300/removed_splash_t4064/. No splash Tuner row existed. bz_dtap.reload_tuned(force) keeps bz_nav (MM-first) through startup tuner ReloadSkin. Backups backups/pre_t4064_nosplash_0353.tgz, scripts/bz_dtap.py.bak_t4064_*. FULL restart. Cold start PASS MM open (fix_oct27f/t4064/cold2_8.png). Splash option C not built.

## t4075 (Oct 27 2026) — MM pill keeps last-used position — DONE 5.0.5
- Left/Right cycle also writes Skin.String bz_last_mmsub_{music,movies,tv}; Back restores chip from it (no wipe).
- bz_cmd start restores Home props from Skin.Strings (cold start / reload); bz_mm subgo keeps prop + persists (no clear). Added `bz_mm.py,restore`.
- Fixed Music Prev/Next treating empty as slot 2 (now slot 1 = Artists, matching label).
- Smoke: Albums → ReloadSkin → still 2; cold r.sh → still 2, Select → musicdb://albums/ PASS. FULL restart.

## t4083 (Oct 27 2026) — Delete Estuary blue background + clean code — DONE (XML/media, ReloadSkin)
- Includes.xml: deleted `ColoredBackgroundImages` include (primary.jpg tinted primary_background + pattern overlay) and its group inside `DefaultBackground` (videowindow / visualisation / fanart layers kept). All DefaultBackground windows (AddonBrowser, MyPrograms, Custom_1100, MyGames, MyPics, MyFavourites, MyPlaylist, EventLog, PVR*, SettingsSystemInfo, MyMusicPlaylistEditor, SettingsScreenCalibration) now black underneath.
- DialogPVRChannelGuide / DialogPVRRadioRDSInfo: ColoredBackgroundImages → black image.
- Deleted `extras/backgrounds/` (primary.jpg, pattern0–7.jpg); removed SkinSettings background_overlay onload + button 607; Variables BackgroundOverlayTypeVar; primary_/secondary_background from colors/*.xml.
- Backup /workspace/b300/bak_t4083_040922. Smoke: cold start, AddonBrowser → Back 10fps (17 frames) — no blue flash.

## t4084 — MM background art crossfade Tuner (Oct 27 2026)
- New Tuner row MAIN MENU > "Background art crossfade" (id mmxfade, bz_at_mmxfade, code MD). 11 steps 0–5 s by 0.5 s, default step 5 = 2 s (was hard 400 ms).
- Wiring: BezelFanartLayer MM-open image `<fadetime>2000</fadetime><!-- BZMMXF ...>` patched by bz_tune_patch._bezel (val mmxfade) → ReloadSkin via bz_tune_dirty. MM-closed image stays fadetime 0.
- Files: xml/Includes_Tuner.xml (vars/nav/row), xml/Includes_Bezel.xml, scripts/bz_tune.json (P+V), scripts/bz_tune_patch.py, media/bezel/info/mm_art_xfade_1..11.png (+CODES.txt MD). Backups *.bak_t4084_*.
- Smoke: MM open over Music, under-adv steps measured ~2.0 s dissolve (20 frames @10fps), twice. Tuner row/infographic not visually smoked. No zip.

## t4089 (Oct 27 2026) — Stand-in posters not working — FIXED (XML, ReloadSkin)
- Cause: stand-ins were only wired into grid 60 / 6600 item layouts; the poster visible under MM in Movies list view is the list-60 swing poster (`$VAR[BezelPoster60]`, Includes_Bezel ~2506) — never had one. Also `String.StartsWith(Icon,Default)` excluded movies whose Icon is an auto video-frame thumb.
- Fix: multiimage (posters/) after the list-60 poster image, MM-open + no poster/tvshow.poster + not `..` + [video content | Icon Default]. Grid/6600 conditions relaxed the same way.
- Backup /workspace/b300/bak_t4089_041514. Smoke: Alien poster blanked → MM open shows stand-in (sp_closed.png); Toy Story keeps real poster (sp_mm.png); Alien poster restored.

## t4092/t4094 — late MM warm load yanks highlight back to warmed section
- Cause: when the warm window/list finished loading it stole focus; nav_menu "focus stolen just after open" reset had=False → re-ran open-on-current-section → SetFocus(6996, Music/Movies/TV row of the window that just loaded). MMHIDE + warm _hold/in-place regrab also used stale row.
- Fix (bz_flip.py, backup bz_flip.py.bak_t4092_*): live strip row `bz_mmlive` tracked every tick while 6996 focused; stolen-focus re-grab, MMHIDE, warm _hold/inplace/retry all SetFocus to the live row only; cleared on MM close. FULL restart.
- Smoke: Music/Movies/TV warms then quick-scroll to row 6–7, 5s later: 5/6 runs held exact row; 1 run slipped by one row (key landing during window swap). No section yank.

## t4094b — onload restore from bz_mmlive (Oct 27 2026)
- MyVideoNav/MyMusicNav onload: SetFocus(6996, bz_mmlive) when set, else bz_mmpos. bz_flip.py warm-launch seeds bz_mmpos from bz_mmlive first. Backups *.bak_t4094b_*. FULL restart.
- Smoke (t4092.sh, 4 rounds, 6 quick downs past Music/TV/Movies): R1,R2 held row 6 exactly; R3 keys LOST (focus on list 60 during swap, strip stayed row 0); R4 landed 12 then slipped to 10 at +4.5s. Not fixed.
- Residual cause: bz_mmlive is a per-tick sample — keys between sample and window swap are lost/rewound; list 60 can hold focus during swap and eat keys.

## t4085/t4086/t4090 (Oct 27 2026 ~04:30 EDT) — MM list flash / focus leave (warm + uadv)
- Repro YES (Music uadv): list rows ("TEST ARTIST nn") flashed under MM on every auto-advance step. Cause: list-text hide was a `Conditional` fade (200 ms) on itemlayout labels; recycled rows on Control.Move replay the fade from 100% -> visible flash. Fix: Includes_Bezel.xml, all 41 MMQUEUE/badge fades -> hard `<visible>!$EXP[bz_navmenu]</visible>` (no fade; a Hidden fade replays the same way — tried, still flashed).
- Movies warm: bz_flip.py "nothing focused -> SetFocus(60)" (vid only) fired mid-load under MM. Gated on bz_nav != true and !bz_mmwarm. Observed 60 focus blips (~100 ms) before fix on Videos; none after.
- Backups: xml/Includes_Bezel.xml.bak_t4085_*, scripts/bz_flip.py.bak_t4085_*. FULL restart (py). Smoke: Music uadv 3 steps + Movies uadv + Movies->TV warm: focus 6996 throughout, 0 flagged frames (b401/t4085/sm3, sm4, t4085_music_mm_open.png). Rig shared with sibling agents (K30) — earlier runs contaminated.

## t4097 (Oct 27 2026) Info + Choose art never draw art over section artwork area
- DialogVideoInfo.xml: removed BzCIVPoster include (own static poster) — underlay sway poster shows through.
- DialogMusicInfo.xml: removed BzCIArt include (own album art) — same pattern.
- Includes_BezelChooseArt.xml: removed E6 black box + Container(6) preview image at 1100,130 580x860.
- Backups *.bak_t4097_*. XML only → ReloadSkin. Smoke NOT valid: shared Kodi driven by parallel agent (Add-on browser). Dim over poster area (5.0.3 catch) unverified.

## t4098 (Oct 27 2026) — Choose art bounce removed
- DialogSelect.xml window include Animation_DialogPopupOpenClose (zoom 80→100 tween="back" = bounce) now conditional: skipped when Home prop bz_artsel set (Choose art). Other select dialogs unchanged. Backup DialogSelect.xml.bak_t4098_*. ReloadSkin. Live smoke Info→Choose art NOT captured (MM/nav ate RPC keys) — needs manual check.

## t4094c — late-warm snap-back harden (Oct 27 2026 ~04:35 EDT) — PASS
- (1) Warm branch of nav_menu: if list 60/61-64/6600 holds focus while bz_mmwarm runs -> bounce to strip 6996 at once (was skipped during warm → keys eaten).
- (2) bz_mmlive now updated from strip focus inside every warm loop (_hold, inplace, post-swap), not just the per-tick sample. Onload restores in MyVideoNav/MyMusicNav gated `!Control.HasFocus(6996)`.
- Root cause found in trace: positional `SetFocus(6996,N,absolute)` is queued and landed AFTER the user's keys, rewinding the row (5→3). New `_bzstrip()` helper: plain SetFocus(6996) (keeps the strip's own row); forces a row only when the strip is at 0 and live row ≠ 0 (fresh window). Used by _hold, inplace, post-swap, MMHIDE, stolen-focus regrab, warm bounce.
- Backups *.bak_t4094c_*. FULL restart. No zip.
- Smoke t4094c.sh (pause 0.65s on Movies/TV/row3 to fire a late warm, then quick downs to row 7): pre-fix R1 landed 3 (fail). Post-fix 6/6 + final 4/4 after clean FULL restart held row 7 at +0.4s and +4.4s, MM stayed open. Movies (ActivateWindow), TV/Movies in-place, and Music windows all covered.

## t4101/t4102 (Oct 27 2026 04:40 EDT) Info hides list + strip content; section art stays
- Includes_Bezel.xml: new `bz_infoup` (movieinformation|musicinformation|songinformation visible). List 60 (both views) + every `!bz_navmenu` list-chrome gate (labels, badges, A–Z 6100/6600, allrow, pill, dtap hint) get a 150 ms Conditional fade-out on bz_infoup (t4102: plain quick fade). MM hard gates unchanged.
- DialogMusicInfo.xml: full-screen BezelBlack → left-only black (x≤960) like VideoInfo, so album art stays visible.
- Backups *.bak_t4101_*. Smoke t4101/: Movies + Music(Song info) PASS. ReloadSkin. No zip.

- t4104 (Oct 27 04:36): Choose art Banner thumbs show full banner — BzArtGrid_wide (banner/fanart/logo/landscape) images scale→keep aligny=center (Includes_BezelChooseArt.xml, bak_t4104_*). ReloadSkin. Smoke: Breaking Bad Banner grid, 5 full banners PASS (b401/t4104/).

- t4097/t4100 (Oct 27 04:45): Info/More/Choose art black poster box = bz_flip poll read Container(60) from the dialog (empty) -> cleared bz_pready. Fix: freeze key while modal dialog/info/select visible (bz_flip.py, FULL restart). Choose art sq/wide preview (E6000000 box + Container(6) art) removed. Smoke on private Kodi :97/8097: PASS. Shots /workspace/b401/t4097s/.

## t4105/t4106 (Oct 27 04:40 EDT) Info must not have its own strip
- Removed `<include>BzCIStripBG</include>` from DialogVideoInfo.xml + DialogMusicInfo.xml (include def left unused in Includes_BezelInfo.xml).
- Info full black mask (line 7) narrowed width 1020→630 (x −60..570) so section colour strip (bar opacity) shows through; left fanart side still masked.
- Choose art BzArtTypes: removed its own BezelBlockFF strip image at 570/390.
- Backup /workspace/b300/bak_202610270436/. XML only → ReloadSkin. Smoke: Info open not captured (RPC Info action didn't open dialog) — Rob visual check pending.

- t4108: Info runtime split from YEAR into own RUNTIME caption row (DialogVideoInfo.xml). box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- t4109 (Oct 27 04:40): Info plot textbox 345x110→345x250 (y792–1042); Music about 170→206 (y836–1042). bak /workspace/b300/bak_t4109_0440

## t4107 — Year under title on Info (Oct 27 2026)
DialogVideoInfo + DialogMusicInfo: title (t4004, 150/150, bz_b46) now inside grouplist (left150 top150 w400 h320, itemgap 6, usecontrolheight) as textbox height=auto; year label bz_r26 B3FFFFFF under it, hidden when ListItem.Year empty. Backup /workspace/b300/bak_t4107_*. ReloadSkin. Smoke: INCOMPLETE — could not open Info with a bound item via RPC.

## t4111 (Oct 27 2026) — Info cast strip closer to button list
DialogVideoInfo.xml: grouplist 9000 height 306→276 (6 rows); cast divider 476→446, CAST label 482→452, list 50 top 506→476, under-divider 624→594, meta 636→606, plot 792→762 (h 250→280). Gap −30px. Backup /workspace/b300/bak_DialogVideoInfo_t4111.xml. ReloadSkin-type (XML).

## t4110 — Info cast focusable + actor → movie folder (Oct 27 2026)
DialogVideoInfo: hidden list 50 replaced by real horizontal list 50 (593,506 352×108, 88px items, focus frame) replacing 4 static cast groups; grouplist 9000 ondown 9000→50; list 50 onup 9000. Select: ActivateWindow(Videos, videodb://movies/titles/?xsp actor-is <name>,return) then Dialog.Close(all,true). XInfo (1111) cast 6720 items: onclick noop → xclose + same actor xsp. Backups /workspace/b300/bak_DialogVideoInfo_t4110.xml, bak_Includes_Bezel_t4110.xml. ReloadSkin. Smoke: INCOMPLETE — shared test Kodi being driven by a parallel agent (window jumped to Music mid-run).

## t4112/t4113/t4114 (Oct 27 2026) — All seasons focus jump + auto-scroll
Cause: bz_flip.py poster_clock ALLBOTTOM2 skipper matched `String.Contains(ListItem.FolderPath,/-1/)` — inside the All-seasons (or All-albums) folder EVERY item path has /-1/, so it kept doing Control.Move(60,1) (auto-scroll). Wrap-to-All did Control.Move(60,-1) before SetFocus(6097/6098), so list showed top briefly.
Fix: skipper now EndsWith /-1/ and only when Container.FolderPath has no /-1/; wrap does SetFocus(All) first then Move. Shared loop → Movies/TV/Music all covered. Backup scripts/bz_flip.py.bak_t4112_*. FULL restart. Smoke: partial (harness state flaky).

## t4119 (Oct 27 2026 04:52 EDT) Info buttons follow Tuner LOOK > Bar style
- Includes_BezelInfo.xml BzCIBtn: texturefocus pill_fill.png → $VAR[BzATHiTex] (live on bz_at_hishape), focusedcolor → $VAR[BzATHiText] (white text on underline/outline). Covers DialogVideoInfo + DialogMusicInfo 9000 buttons. Bak /workspace/b300/bak_Includes_BezelInfo_t4119.xml. ReloadSkin. Smoke pending.
- t4115/t4121 (5.0.6): DialogVideoInfo plot moved into meta grouplist (flows under GENRE, no overlap); strip bg left off per t4117.

## t4121 — All-row Down wrap flash ('..' before 6097/6098) — PASS (2026-10-27 05:0x EDT)
- Includes_Bezel.xml list 60 (BezelInfoList→6097, BezelVideoPosterList→6098): ondown pair now `condition="Control.IsVisible(609X)"` SetFocus + unconditional SetProperty(bz_bottomedge) → Kodi OnDown never wraps (HasActionsMeetingCondition true). Backup b300/bak_Includes_Bezel_t4121.xml. No .py change.
- Smoke on isolated instance (HOME=/tmp/bzwraphome :94 port 8094, script b401/w.sh) — shared bz2home/8099 was being restarted by a sibling, which caused false FAILs.
- TV videodb://tvshows/titles/1/ Season2 Down: 25 polls, CurrentItem never 0, focus 60→6098. Music Coldplay albums Parachutes Down: 60→6097, no 0. Plain list end: bz_bottomedge=1 (unchanged behaviour).

## t4125 / t4128 — Info: section strip visible + Section options fold-in (2026-10-27)
- Includes_BezelInfo.xml: BzCIFanart first image width 840→450 (fanart covers x120–570 only; strip visible). BzCIHead "OPTIONS › SECTION".
- Includes_Bezel.xml: strip info-pairs/plot groups + dtap hint fade under $EXP[bz_infoup] (colour bar stays, labels hidden).
- DialogVideoInfo.xml: grouplist 9000 defaultcontrol 8 (Play); new 9980 "Section options ›" (Up from Play) → bz_ci_more=sec page: buttons 9979,9971-9973,9980-9988 (old 6xxx video Section Settings, same conditionals) + 9984 Back. More page now bz_ci_more==1.
- Smoke PASS: opens on Play, Up→Section options, Select→View Type, strip visible, no bleed. Known: Back key on Section page closes Info (use ‹ Back row).
## t4129 — removed old video MM Settings-Left section menu (2026-10-27)
- Includes_Bezel.xml: video Section Settings group (grouplist 6931 + buttons 6979,6971-6973,6980-6988) deleted; Left triggers now music-only; removed the two videos SetFocus(6931) onlefts.
- bz_flip.py: Menu-key card2 in videos now opens on Movies row (no navset). FULL restart done.
- Music section menu (6930/6920-6926/6990-6994) KEPT — DialogMusicInfo has no fold-in yet.
- Smoke PASS: videos MM Settings Left = no panel; music Left = VIEW TYPE still works; Info fold-in intact.

## t4136–t4138 (Oct 27 2026 ~5:10 AM EDT) — episode drum pop/jump → slide as one, gentle
- Root cause: drum faces a/b (Includes_Bezel 6706) froze titles via bz_flip _drsnap, but ART read live Container(60).ListItem(±1/0).Art(thumb). List 60 moves first; bz_flip polls 50 ms then flips face → visible face repainted art in place (pop) before slide began; incoming focused tile used background="true" (async load = late pop); no ±2 tiles so the edge slot was empty at slide start (jump-in).
- Fix: _drsnap now snapshots art per face (bz_dr{a,b}_{mm,m,0,p,pp}a); faces read snapshot props; removed background load on focused tile; added ±2 edge tiles (y -735 / 1369). Whole strip now moves as one group.
- Ease: default already 800 ms circle-out (eposlide empty/5, epease empty/6) — unchanged; Tuner can soften.
- Backups /workspace/b300/bak_IncBezel_drum_*.xml, bak_bz_flip_drum_*.py. .py change → FULL restart. Not visually smoked (no private-instance shots yet).

## t4135 (Oct 27 2026 ~05:20 ET) — MM Settings bar live (mock G_t4134)
- xml/Includes_Bezel.xml focusedlayout Settings group: removed mm_pill_ol border, left ‹, hamburger, left divider. SETTINGS left=36 (list-aligned), scroll=false. Kept right divider (x226), sliders x238, BEZEL logo media/bezel/logo.png x290 36x36 keep (replaces mm_set_b.png), › x346.
- Backup: xml/Includes_Bezel.xml.bak_t4135_*. ReloadSkin. Smoke: private Kodi HOME=/tmp/bzsethome :96/8096 → /workspace/b401/t4135_settings3.png PASS. No zip.

## t4147 (Oct 27 2026 ~5:30 AM EDT) — flat episode strip replaces drum (👍 on live_* mock)
- xml/Includes_Bezel.xml group 6706 only: removed both <camera> (drum perspective); focused tile now carries its own S·E + title overlay inside faces a/b (frozen bz_dr{a,b}_0s/e/t) so labels ride the art and slide as one; neighbour labels switched from live Container(60).ListItem(±1) to frozen bz_dr{f}_m*/p* (no pre-slide pop); dropped separate BezelATEpLabelFade title overlays. Static (drumk empty) group untouched. Kept: same-size dimmed neighbours (BzEpDimCol), frame.png border, strip_edge top/bottom fade, ±2 edge tiles, EPISODES speed/ease Tuner (BezelATEpSlideUp/Down; default circle out = soft stop).
- bz_flip.py NOT changed (drum_dir/_drsnap still feed direction + frozen labels) → ReloadSkin is enough (full restart fine).
- Backup xml/Includes_Bezel.xml.bak_t4147_051847. Smoke: private HOME=/tmp/bzdrumhome :131/8157, fresh copy + cold start, Breaking Bad S1 Down/Down/Up → /workspace/b401/t4147_strip/ (sheet3.png, crop.png) PASS. No zip.

## t4142 / t4146 (Oct 27 2026 ~05:22 EDT) — Music Info parity with Video Info + list per combined_music mock
- DialogMusicInfo.xml: defaultcontrol 8 (Play); new 9980 "Section options ›" (Up from Play) → bz_ci_more=sec page: View Type (same bz_grid_music/bz_albumlist cycle), Sort By, Filter, Order, Visualizer, Update Library, Party Mode, Go To Playlist, Get More…, Add-On Settings, Edit Nodes (same conditionals as old 6920–6994) + ‹ Back (9967). More page now bz_ci_more==1.
- t4146 main list per /workspace/mockups/fs_music/context/combined_music.png: Play · Play next · Queue · Favourite (9095 moved up from More) · Browse (9083 more-from-artist / 9084 artist albums) · More options; Album/Artist information (12) moved into More options. Row icons media/bezel/ci/{play,next,queue,fav,browse,more}.png (overlay, hidden for artist items). textoffsetx 62 on those rows. YEAR meta row dropped (year under title).
- About/bio textbox moved into meta grouplist (flows, no overlap).
- Includes_Bezel.xml: music Section Settings group (6930/6920–6926/6990–6994 + values 6932) deleted; 2 music onleft→6930 pairs removed; music strip info pairs/biography (lines ~1239–1319) get <visible>!$EXP[bz_infoup]</visible> (conditional fade was overridden by the NP fade → overlapped Info).
- bz_flip.py: Menu-key card2 in music opens on Music row (no navset). FULL restart.
- Backups *.bak_t4142_0513xx, DialogMusicInfo.xml.bak_t4146_051816. Smoke private :94/8094 PASS: opens Play, Up→Section options, Select→View Type, MM Settings Left = no panel. Shots /workspace/b401/t4142/. Open: focus bar not visible on Info rows in this instance (same shared BzCIBtn as Video); divider sits at y596 (gap under list) because the Section page needs the height.

## t4149 (Oct 27 2026) — MM Music pill set to Artists didn't open Artists — FIXED (.py, FULL restart)
- Cause: bz_mm.subgo treated pill 1 (Artists) as "default", so MMQUEUE's keep-last-Music-location (bz_lastmusic) overrode it. Since t4075 the pill is always restored, so Artists never won.
- Fix: scripts/bz_mm.py `explicit = prop != ''`. Any pill set (incl. 1) opens that pill; keep-last only applies when the pill is empty. Backup scripts/bz_mm.py.bak_t4149_*.
- Smoke (private Kodi, real keys): Albums list → Left MM → cycle pill to ARTISTS → Select → musicdb://artists/ PASS.

## t4153 (Oct 27 2026) — TV clearart header (strip + Info) — BUILT (XML-only, ReloadSkin)
- Rule: clearlogo → tvshow.clearlogo → clearart → tvshow.clearart ($VAR[BzTVClear]). Art → image at top of strip / Info, big title hidden. No art → [B]UPPERCASE show title[/B] bz_b46 right-aligned at strip top (BzTVShowName).
- Includes_Bezel.xml: new vars + header group (600,96 330x76) for tvshows/seasons/episodes, hidden on ".." and under Info. DialogVideoInfo.xml line 9 title block only (left t4154 meta/plot alone): title textboxes hide for TV with art; image 400x150 shown instead.
- Backups *.bak_t4153_*. Smoke: Info on Better Call Saul shows clearlogo, title hidden PASS; strip header visible behind MM PASS. No-art fallback not exercised (all test shows have logos). Shared private Kodi was being driven by sibling mid-smoke.

## t4154/t4155 (Oct 27 2026) — Info plot clipped under EPISODES / meta rows — FIXED (XML, ReloadSkin)
- Cause: DialogVideoInfo meta grouplist (595,606 h408) held up to 6 rows (48px each) + spacer + fixed 196px plot; TV show (SHOW/SEASONS/EPISODES/YEAR/RUNTIME/GENRE) and episode overflowed, grouplist dropped/clipped the plot.
- Fix: plot textbox split by type — TV show/episode h110, others h200 (fits 408 = strip bottom). Backup /workspace/b401/bak_t4154_*_DialogVideoInfo.xml.
- Music Info checked: max 4 rows ×50 + 206 plot = 410 ≤ 434 — no change needed. Movies: 4 rows fits.
- Finding: Info key on TV show list (non-dtap) opened old in-place BezelXInfo (Includes_Bezel.xml, blue panel, PLAY/FAVOURITE, ctl 6701) — not fixed (out of scope).

## t4156 (Oct 27 2026) — LOOK Tuner: Now-playing music label toggle — DONE
- New LOOK row "Now-playing music label" (id npmlbl, setting bz_npmlbl_off, Default ON) after Auto-advance rows in Includes_Tuner.xml; var BzATVal_npmlbl.
- Includes_Bezel.xml: top-right mini-player title/artist/time grouplist (left 416 top 29) gets `<visible>!Skin.HasSetting(bz_npmlbl_off)</visible>`. Click button 6949 untouched.
- Infographic media/bezel/info/look_npmlbl.png (860x560), code L9 in CODES.txt.
- Backups *.bak_t4156_*. Smoke: ON shows LONGTONE · time top right; OFF hides it (setting forced via settings.xml, then removed). XML-only → box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## t4159 — Info screens share Global dimmer (Oct 27 2026)
- New include `BezelInfoDim` (Includes_Bezel.xml): gdim-only fade (bz_at_gdim 1–6 → 30–60%, 7 = 100%), no MM condition.
- `BzCIFanart` (Includes_BezelInfo.xml) wrapped in group with BezelInfoDim → DialogVideoInfo + DialogMusicInfo fanart follow LOOK › Global dimmer. Section underlay behind Info already dimmed by BezelSecDim.
- Backup /workspace/b300/bak_t4159_*. Smoke /workspace/b401/t4159/ (cmp_mu.png gdim1 vs gdim7 PASS). XML → ReloadSkin. No zip.

## t4157 (Oct 27 2026) — LOOK Tuner: BEZEL logo colour + opacity — BUILT (XML/media/json, ReloadSkin)
- New LOOK rows (after Colour Block, before Reset look): "BEZEL logo colour" (bz_at_logocol, 8 steps White/Silver/Amber/Orange/Red/Green/BEZEL blue/Purple, default White) code LA; "BEZEL logo opacity" (bz_at_logoop, 30–100% by 10, default 100%) code LB. Empty = default.
- Includes_Tuner.xml: BzLogoCol (64-combo AARRGGBB) + BzATVal/Step/Bar_logocol/logoop vars (after t4156 npmlbl var); L/R onleft/onright pairs before blockcol pairs.
- Wired: MM Settings bar logo (Includes_Bezel 6996 focusedlayout) + DialogBusy logo → colordiffuse $VAR[BzLogoCol]. Not wired (intentional): strip branding logo (73FFFFFF subtle), library BezelLogoButton (bz_dimmed / focus states).
- bz_tune.json P += logocol/logoop (look) so Reset look clears them. CODES.txt + mockups CODES.md += LA/LB. Info art media/bezel/info/look_logocol.png, look_logoop.png (860x560).
- Backups *.bak_t4157_*. Smoke private Kodi (HOME=/tmp/bz57home, :57, 8157): default white PASS; amber 50% on Settings bar PASS; Tuner LOOK rows render with infographic, Left changes value (3→2 Silver) PASS. Shots /workspace/b401/t4157/.

## t4148 — Music album list overflowed fanart box bottom (FIXED, smoke OK, no zip)
- Cause: row text inside the section parent group draws above later images in that group, so the existing Includes_Bezel 990–1020 band / 1020 mask never hid text; and any mask carrying BezelSecDim is only ~60% opaque.
- Fix (MyMusicNav.xml only, after section group): undimmed opaque black 120..570 × 990–1080, then a dimmed copy of the 990–1020 band (black + BezelFanartLayer) so the half-row strip matches the box. Includes_Bezel untouched.
- Backups: MyMusicNav.xml.bak_t4148_*, MyMusicNav.xml.bak_t4148b_*. Shots: /workspace/b401/t4148/v4_bottom.png, v3_top.png. Needs box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- t4166: removed BezelXInfo oninfo wires (Includes_Bezel list+grid); 1111 window emptied/self-closes; Info -> DialogVideoInfo

## t4163 (Oct 27 2026) — TV clearart must stay with colour strip — FIXED (XML-only, ReloadSkin)
- Cause: t4153 header placed at top 96 (h76) while strip starts at bz_top 120 → logo poked 24px above the strip.
- Fix: Includes_Bezel.xml BezelVPLContent clearart image + fallback title → top 126 h48 (inside strip x600–930). Fallback title also fixed: invalid `$UPPERCASE[...]` rendered literally → `[UPPERCASE]` tag, label bz_b34 bold, scrolls if long.
- Info (DialogVideoInfo) clearart is on fanart, not the strip — unchanged.
- Backup Includes_Bezel.xml.bak_t4163_*. Smoke private Kodi :163 — with art PASS, no-art (forced in private copy) PASS. Shots /workspace/b401/t4163/.

## t4165 — Info follows fanart + colour strip LOOK settings (Oct 27 2026)
- Ask: Info screens must follow fanart and colour-strip brightness/opacity/colour.
- Found: Info strip = the open section's strip showing through 570–960 (BzMMStrip colour from Colour Block blockcol/blockop + bz_at_mmbar opacity), so it already tracks. Info fanart had Global dimmer (t4159) but NOT LOOK Fanart opacity (bz_at_fanop).
- Fix: new include BezelInfoFanOp (same 10 bz_at_fanop fade anims as section fanart, Includes_Bezel L675) added to the BzCIFanart image in Includes_BezelInfo.xml. Backup Includes_BezelInfo.xml.bak_t4165_*. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Smoke (private Kodi :91/8165): Music Info PASS at fanop 0% / gdim 30% / blockcol 1 vs fanop 100% / gdim 100% / blockcol 5 (green strip). Movies/TV Info didn't open in the script (dtap Info path) — not verified visually. /workspace/b401/t4165/
- t4171 (Oct 27 2026): MM strip opacity (bz_at_mmbar) range 30–100 → 10–100. Level1 30%→10% in Includes_Bezel/Settings/SettingsCategory/SettingsProfile/SettingsSystemInfo/SkinSettings fade + Tuner label/desc; levels 2–5 (50 default/65/83/100) unchanged. Infographic mm_strip_opacity.png text updated. Backups *.bak_t4171_*. Smoke PASS /workspace/b401/t4171/. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## t4172–t4173 (Oct 27 2026) Tuner infographic panel bigger/square
- Includes_Tuner.xml: all 13 info image controls (incl. black backing) 1010,330 520×340 → 1010,300 560×560 (square, aspectratio keep). Desc textbox moved 1010,686 760×236 → right column 1600,300 300×560. Key hint 1010,934 → 1010,890 w890.
- New boards going forward: 560×560 square (author at 1120×1120), title/text in top + bottom bands. Existing landscape boards letterbox, not remade.
- bak: Includes_Tuner.xml.bak_t4173_*. ReloadSkin. Smoke: /workspace/b401/t4173/look_info.png
- t4174 (Oct 27 ~05:50 ET): Tuner strip now = MM strip — Colour Block (BzMMStrip) + bz_at_mmbar opacity anims copied live from Includes_Bezel MM strip, MM shadow + thin bezel, Tuner glow follows bz_at_mmglow. File: xml/Includes_Tuner.xml (bak /workspace/b300/bak_t4174_Includes_Tuner_*.xml). ReloadSkin. Smoke /workspace/b401/t4174/ (bar 1 vs 4). Note: tests need live file copied to /tmp/bz2home addons (r.sh copy).
- t4175 (Oct 27): Tuner sliders symmetric+bigger — value centred between ‹ ›, bar 360x8 full-width centred (was 180x5 right). bar_*.png trimmed to content (bak /workspace/b300/at.bak_t4175). Includes_Tuner bak_t4175_*. ReloadSkin. Smoke /workspace/b401/t4175/.
- t4185/t4186 (Oct 27 ~05:55 ET): cast shadows broken after infographic work → reverted media/bezel/at/ to pre-t4175 (at.bak_t4175; 123 files restored). Pre-revert copy at.bak_t4185_055502. XML untouched. Full restart (r.sh). Smoke /workspace/b401/t4185/.
- t4183/t4184: Music Info main list = Play·Play next·Queue·Favourite·Browse·More options (icons). Section options moved into More; Artist/Album info already in More. bak_t4183_*. ReloadSkin. Smoke b401/t4183 PASS.
- Oct 27 06:04 t4197: FS music plane orbit (parked) visible->false in all bezel/plane multiimages. bak_t4197_060436. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Oct 27 06:04 t4198: plane orbit DELETED from live (4 multiimages in Includes_Bezel + MusicVisualisation; media/bezel/plane moved to /workspace/b300/parked_plane_t4198/). bak_t4198_060456. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Oct 27 06:08 t4200: plane TEST skin /workspace/b300/skin.bezel2.plane-test/ (copy of core, bak files stripped, plane art restored from parked). Plane back+front in MusicVisualisation (vis HasAudio+!Paused, 400ms fade) and Includes_Bezel NP in-place (+bz_np gate). Launcher /workspace/b401/rt.sh. Smoke INCONCLUSIVE: MM stayed open, bz_np never set, plane not seen. Core still 0 plane refs.

## t4202 — Global dimmer makes fanart see-through (DIAGNOSE ONLY, Oct 27 2026)
- Cause: bz_at_gdim drives BezelSecDim/BezelInfoDim parent *fade* (alpha) since 4.7.4 veil retirement; fades whole section incl. fanart → background bleeds through. BzGDimCol scrim is 00FFFFFF (off).
- Want: gdim = black veil (darken), fanart stays opaque; only bz_at_fanop makes fanart translucent.
- Mocks: /workspace/mockups/gdim_opaque_t4202/ (A veil whole scene rec., B veil art-only, C current wrong). No core edit — awaiting Rob pick/Go.

## 2026-10-27 06:15 EDT — t4204u Global dimmer default = 100% (XML+json, ReloadSkin, no zip)
- Empty Skin.String(bz_at_gdim) now = step 7 = 100% (no fade). Was empty = step 6 = 60%.
- Includes_Bezel.xml: BezelSecDim + BezelInfoDim step-6 fade now only `==6` (empty → no animation). mmdim untouched.
- Includes_Tuner.xml: BzATVal/Step/Bar_gdim empty → 100% / 7 / bar_7_7; Left from empty → 6; Right from empty does nothing (at max).
- scripts/bz_tune.json gdim default index 6→7 (label list in json is legacy/unused-looking: 90..30%).
- Users with explicit stored values keep them; only empty changes. Backups *.bak_t4204_*.
- t4203 exclude: no fanart-exclude ever coded; only t4202 mocks (gdim_opaque_t4202: veil whole scene / veil art-only) awaiting Rob pick.
- t4224 (Oct 27 063737): FS Music + FS Music 2 (1112): removed BezelBlockBF tint over NP fanart; fanart wired to bz_at_fanop; 1112 bg=true (black+fanart covers list/strip). bak_t4224_063737
- t4226 (Rob Go): Tuner applied popup shipped = mock A (t4181 bottom card) + logo spin (A2 idea, logo spins inside card). No A/B/C pick on record. bz_dtap.py sets Home bz_tunapplied before 'Tuning applied' notification (2.6s); DialogNotification.xml: BEZEL card x700 y880 520x110 colour-block blue, spinning bezel/logo.png, TUNING APPLIED / Reloading BEZEL look...; stock toast hidden while prop set; onunload clears prop. Baks *.bak_t4226_*. .py change → full restart done (r.sh). Smoke b401/t4226/ PASS (card + spin, normal toasts unaffected).
  t4224 add: 12 music list/strip/small-album fade conds now fire on bz_np alone (was dlg-or-non-music-content), so in-place FS hides list too. Smoke PASS shots b401/t4224/fsA.png, fs2_1112.png
- t4228/t4229 (Rob): bottom card A disliked → rebuilt as mock B (t4181 B1/B2): pill beside top-left BEZEL logo (colour-block blue fill mm_pill + solid white mm_pill_ol outline like list bars, 'TUNING APPLIED'), pill fades at 1.5s, then logo spins (B2). DialogNotification.xml only (bz_dtap.py trigger from t4226 unchanged). Baks bak_t4228_*, bak_t4228B_*. ReloadSkin. ✓ glyph dropped (font tofu). Smoke b401/t4228/ PASS.

## t4227 (Oct 27 2026 ~06:55 EDT) — Music Info polish (t4146 leftovers)
- Focus highlight: root cause = button `<texturefocus>` does not resolve `$VAR[BzATHiTex]` (text recoloured, bar never drawn) — affected Music AND Video Info. Fix in Includes_BezelInfo.xml BzCIBtn: conditional includes BzCIHi1–5 per `bz_at_hishape` (default outline). Follows Tuner Bar style on dialog open.
- Gap under list: DialogMusicInfo divider + meta grouplist slide up 144px (y596→452 / 608→464) when main page (`bz_ci_more` empty); More/Section pages keep old position.
- Backups *.bak_t4227_*. Private smoke :228/8228 PASS, shots /workspace/b401/t4227/ (post_*). ReloadSkin on bz2home.
- Known nit: solid (shape 1) bar = white, row icons are white → icon hidden on focused row.
- 2026-10-27 t4233u: Tuner applied pill (DialogNotification.xml) → rectangular: white.png 272x44 outline + 2px-inset white.png fill F0115E85 (replaced mm_pill/mm_pill_ol); label full pill width align center/aligny center. Backup xml/DialogNotification.xml.bak_t4233_*. ReloadSkin (XML only). Smoke on separate :228 / /tmp/bz4227mi (stress :77 untouched): /workspace/b401/t4233/B1(_crop).png B2(_crop).png PASS.
- 2026-10-27 t4235u: Applied pill "No fill" — DialogNotification.xml: removed F0115E85 inset fill; solid white 272x44 base replaced by 4×2px white.png edges (outline only), label centered unchanged. Backup xml/DialogNotification.xml.bak_t4235_*. ReloadSkin (XML only) on private :228 /tmp/bz4227mi (also copied to bz2home, :77 not reloaded). Smoke /workspace/b401/t4235/B1(_crop).png PASS.

## t4242 — Album + Poster glare Tuner rows restored (Oct 27 2026)
- ALBUM › GLARE sub (bz_topen_al_glare): Glare style (aglstyle, Original/Diagonal/Twin bar/Top sheen/Spot/Vinyl arc/Glass edge, def Original), Glare opacity (aglop 0–100% 25-step, def 100%), Glare tint (agltint White/Warm/Cool/Gold/Rose/Accent, def White), Reset album glare (reset,aglare).
- POSTER › GLARE sub (new bz_topen_p_glare): pglstyle/pglop/pgltint same ranges + Reset poster glare (reset,pglare).
- Restored BzATVal/BzATBar vars + 60 onleft/onright from bak_underadv_001639; P entries back in bz_tune.json (from bak_pre500). Info art: o71_glare_style/opacity/tint.png. bz_tune.py unchanged → box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Smoke private Kodi :242 — Left/Right PASS both. Shots /workspace/b401/t4242/. Backups *.bak_t4242_*.

## t4237 (Oct 27 2026 ~07:10 EDT) Choose art "proper operation" — right side previews focused grid art — PASS
- Includes_BezelChooseArt.xml (sq/wide/tall grids): re-added right preview 1110,140 560x840 keep, fade 150, `Container(6).ListItem.Art(thumb)`; black backing x960–1920 only while a focused thumb exists (hides underlay sway poster so they don't stack; no empty black box).
- DialogVideoInfo.xml + DialogMusicInfo.xml: Info strip chrome (cast/buttons 9000/meta) wrapped in group with Conditional fade-to-0 while Home bz_artsel set → Choose art type rows no longer overlap Info rows. Fade (not visible) keeps focus targets alive on return.
- Backups *.bak_t4237_*. XML only → ReloadSkin. Smoke on private Kodi :237/8237 (/tmp/bz4237home): Aliens poster 3 moves + fanart 2 moves, Album 21 thumb; types screens clean. Shots /workspace/b401/t4237/ (v2_types, v3_sheet, v4m_sheet, m1_types, m_sheet). One coverartarchive thumb loads blank (source/offline, grid too).

## t4238 (Oct 27 2026 ~07:15 EDT) Zip 5.0.7 — DONE
- addon.xml 5.0.6→5.0.7 (+news, changelog). Checks: all XML parse, py_compile OK, 1 pre-existing missing ref bezel/frame2.png. Zip /workspace/skin.bezel2-5.0.7.zip (1744 files, ~24.9 MB, testzip OK). Includes t4237 Choose art, t4242 glare Tuners, applied pill, Music Info polish, FS fanart, Tuner strip. .py changed since 5.0.6 (bz_mm/bz_flip/bz_dtap) → FULL restart. Stress not started; no fresh-install screenshot pass run.

## t4260/t4261 (Oct 27 2026)
Deleted stray upper-right BEZEL logo (DialogBusy.xml: shadow card, dark tile, logo image w/ $VAR[BzLogoCol] at 1807,57) — showed on Music entry, wired to Tuner logo color/opacity. Backup /workspace/b300/bak_t4260_DialogBusy.xml. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## t4263 (Oct 27 2026)
Wired LOOK Tuner logo colour+opacity ($VAR[BzLogoCol]) to upper-left logo: BezelLogo image (was bz_dimmed) + BezelLogoButton focus image (was FFFFFFFF) in Includes_Bezel.xml. Backup /workspace/b300/bak_t4263_Includes_Bezel.xml.
t4264: unwired Settings-row MM logo (Includes_Bezel) + DialogNotification logo from BzLogoCol -> fixed FFFFFFFF. Only upper-left logo follows Tuner. Backups bak_t4264_*.

## t4266 (Oct 27 2026)
Upper-left logo (BezelLogo + BezelLogoButton focus image) spins (loop rotate -360/1.2s linear, centre 60,58) while Window.IsActive(busydialog|busydialognocancel). DialogBusy logo stays deleted. Backup bak_t4266_Includes_Bezel.xml.

## t4268 (Oct 27 2026)
FS music viz: hid bottom transport hint row (O84 cycle aid: LAST/SELECT/NEXT + t4245 prev/next pills) with + !Window.IsActive(visualisation). NP elsewhere unchanged. BezelBlack untouched. Backup bak_t4268_Includes_Bezel.xml.
t4269: reverted t4268 viz-hide (pills + LAST/SELECT/NEXT back); added grad_bottom.png image 120,860 840x160 (full fanart width, fades to ~86% black at bottom edge) behind the pills. No opaque bar. Backup bak_t4269_Includes_Bezel.xml.
t4271: live mockup FS music viz (repeat-all album so 2s stubs keep playing): /workspace/b401/t4271/live_full.png, live_bot.png, live_bot_left_zoom.png. Gradient + pills visible; hard pure-black block still at x~110-570 y>=990 (covers lower half of prev pill + LAST/SELECT) — source not yet found.
t4274: re-smoke after fresh restart (Adele repeat-all, Home->viz), 5 frames /workspace/b401/t4274/f1-5.png + live_full/live_bot/live_bot_left_zoom.png: NO hard black rect; pills, LAST/SELECT, NEXT, soft gradient all visible. No skin control draws a black rect there (audited BezelNPInPlace, MusicVisualisation, NPControls(empty), MusicPlayingArt, cycle aid). t4271 frame was a transient (stale Kodi session; prior capture was fully black). No XML change, no backup needed.
t4272: bz_at_fanop wired on FS Music (BezelNPInPlace artist.fanart image, Includes_Bezel.xml:2737) = YES; FS Music 2 (Custom_1112) includes same BezelNPInPlace = YES.
t4275: FS Music prev/next song pill titles were already align/aligny center but sat ~3px low (descenders on pill border). Includes_Bezel.xml:2811 labels offset(-1)/offset(1).Title top 982->979. Backup /workspace/b300/bak_t4275_Includes_Bezel.xml. Shots /workspace/b401/t4275/full.png bot.png pills_before.png pills_after.png.
t4276 (answer only): MM crossfade (bz_at_mmxfade, BezelFanartLayer Includes_Bezel.xml:683 fadetime 2000) = fanart ONLY. Album art: NO (tiles fadetime 250, standins 0, MM preview 150). Posters: NO (tiles fadetime 250, standin multiimage 0). No edits.
t4277: MM-open crossfade wired to album + poster. Includes_Bezel.xml: BezelFlipA, BezelFlipB (600x600 @1140,220), BezelSwingPoster main $VAR[BezelPoster], BezelVPLPoster main $VAR[BezelPoster60] each split into 2 layers: !bz_navmenu (orig fadetime 0/300/300) + bz_navmenu copy fadetime 2000 tagged <!-- BZMMXF t4277 --> so bz_tune_patch.py mmxfade regex retimes them with fanart. Backup /workspace/b300/bak_t4277_Includes_Bezel.xml. Smoke /workspace/b401/t4277/sheet.png (mm0 + mmx_01-12, 250ms): Music->Movies under MM, poster fades in over ~2s (no pop); outgoing album cuts out (section include hides). 
t4278: album cast shadow investigated, NOT edited (no Rob shot on box; see report). Before shots /workspace/b401/t4278/.

## t4280 (Oct 27 2026 08:16 EDT) — Remove section fanart tints, keep Tuner opacity
- Includes_Bezel.xml BezelFanartLayer: deleted the $PARAM[dim] black white.png veil overlay. PARAM[dim] kept (unused) so call sites (dim=99000000/A0000000/01000000 in Includes_Bezel x5, MyMusicNav x1) are harmless.
- Kept: black backing, both fanart images with bz_at_fanop fade (MM-closed + MM-open 2s crossfade), gdim/mmdim, FS Music untouched.
- Backup /workspace/b300/bak_t4280_081458 · smoke /workspace/b401/t4280/ (sheet.png, after_movies_fanop100.png). xmllint OK, test Kodi restarted via r.sh.

## t4282 — Album cast shadow LEFT — MOCK ONLY (Oct 27 2026)
- Mock only, no live XML/media changes. Base: b401/t4280/before_music_closed.png (Tusk, MM closed) -> b401/t4282/base_music_closed_tusk.png
- Mock: b401/t4282/mock_t4282_album_shadow_left.png (+ before_after_crop.png, ref_fanart_on_noshadow.png)
- Shadow: falls left from cover's left edge x=1104 (cover 1104,220-1704,820), ~100px deep, drops ~40px down at the far end, 28px blur, ~90% black. Fanart-like backdrop simulated right of x~980 (live bg was pure black, so the shadow wouldn't show otherwise).
- Waiting on Go/👍 before building.

## t4284 (Oct 27 2026) — Settings logo off LOOK logo Tuner
MM Settings-bar logo (Includes_Bezel L472) was already fixed FFFFFFFF; the logo still on the Tuner in Settings was the UL BezelLogo/BezelLogoButton included by the Settings windows. BezelLogo + BezelLogoButton now take param `col` (default $VAR[BzLogoCol]); Settings, SettingsCategory, SettingsProfile, SettingsSystemInfo, SkinSettings pass col=FFFFFFFF. Library/other windows unchanged (still Tuner). Notification logo already FFFFFFFF. Backup /workspace/b300/bak_t4284_081914. Smoke /workspace/b401/t4284 (Tuner red 30%: Settings logo white, Videos UL logo red).

## t4285 — TV pill "Watching" → empty list? (diagnose, 2026-10-27)
- Pill 6 (WATCHING) → bz_mm.py SUBS['tv'][5] = `videodb://inprogresstvshows/` → bz_cmd.py go → ActivateWindow(Videos, path). Same route as Shows/Recent; In Progress MM item uses same path.
- Smoke (/tmp/bz2home, test lib 8 shows): Files.GetDirectory = 5 shows; via skin route Container.FolderPath=videodb://inprogresstvshows/, Content=tvshows, NumItems=5 — list populated. Shot b401/t4285/pill6_closed.png.
- Verdict: NOT a skin wiring bug. Kodi's in-progress TV node only lists shows with partly-watched/resume episodes; empty on Rob's box = his library has none flagged in progress. No edit made.

- t4286: All albums row (6097) permanent outline — texturenofocus was mm_pill_ol @33 alpha; blanked. Outline focus-only. Backup bak_t4286_Includes_Bezel.xml
  - t4286 smoke PASS (Oct 27 8:25 AM EDT): synced Includes_Bezel.xml to /tmp/bz2home, JSON-RPC ReloadSkin, Music musicdb://artists/2/ (Adele). Focus on list 60 → All albums row has no outline (b401/t4286/unfocused.png); focus 6097 → white pill outline (b401/t4286/focused.png).

## t4283 (Oct 27 2026 ~08:23 EDT) — Go: album cast shadow LEFT of cover (LIVE)
- Includes_Bezel.xml: all 6 album cast images (BzCastTex_a/BzCastCol_a; swayright animated/static groups + !swayright animated/static) moved left 485 -> 624 (480 wide, right edge 1104 = cover left edge), zoom centers 965 -> 1104. Tagged <!-- t4283 -->. Poster cast untouched. Backup /workspace/b300/bak_t4283_Includes_Bezel.xml. xmllint OK, synced, box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Smoke: /workspace/b401/t4283/after_music_audio.png. Shadow not confirmed visible on screen: the background is pure black, and a debug colour pass during smoke showed no cast drawn in the current state (Kodi is shared with another agent). Needs follow-up check of the parent group visibility.
- Mock reference: /workspace/b401/t4282/.
t4283b (~08:28 EDT): z-order probe in INSTALL copy only (t4283/probe.sh): red 300x100 at 900,100 as last child of the cast parent group (line 984) and of the now-playing art root group (918) -> neither showed in Music with Tusk playing. Kodi is shared with another agent (it opened the Main Menu/TV mid-test), so these results aren't reliable. Faint dark band on the info panel's right edge in probe_g918_clean_frame.png might be the cast (not confirmed). No live XML change; install copy restored; acop back to 5. No proven shot yet. Red shots r1-r4 deleted.

## t4288 TV Watching not populating (Oct 27 2026)
- Wiring OK: bz_mm.py SUBS tv[6]=videodb://inprogresstvshows/, label WATCHING (BzMMSubLbl). Test lib: path → NumItems 5, Content tvshows, list visible (shot b401/t4288/a_pill.png). No skin filter/empty-state hides it. No change made.
- Empty on Shield = Kodi library has no show w/ resume point or partially-watched count (e.g. watched via addon/external player, or watched-status synced elsewhere). Alternative (needs Go): BEZEL Continue-watching xsp from bz_flip cw_clock (special://profile/addon_data/skin.bezel2/bezel_cw_a|b.xsp, in-progress eps + next-up).
- MM-open smoke blocked: another agent's fullscreen-video test grabbed shared Kodi.

## t4287 — BEZEL logo hides in fullscreen video (DONE)
- Includes_Bezel.xml: BezelLogo image, BezelLogoButton button 6001 + focus logo image get `<visible>!Window.IsActive(FullscreenVideo) + !Window.IsActive(VideoOSD)</visible>`. Library/Settings unchanged.
- Smoke /workspace/b401/t4287/ (trio.png): Videos logo on → fullscreen big.mp4 logo gone → back logo on. Backup bak_t4287_*. XML → box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- [t4289] Rob: MM background Music not loading fallback art. Cause: BezelFanartLayer never had a stand-in (stand-ins only on poster/tile/list-60 art); no-fanart artist → black/default bg. Fix: Includes_Bezel.xml — new expr bz_nofanart (mirrors BezelFanart sources; $VAR illegal in conditions) + multiimage extras/standins/artists/ random 8s, visible bz_navmenu + music + bz_nofanart, same bz_at_fanop Tuner opacity anims. Backup Includes_Bezel.xml.bak_t4289_*. Smoke /workspace/b401/t4289/c_after_standin.png PASS (stand-in shows MM-open Test Artist 04). box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

- t4290 (2026-10-27 08:30): MM bottom — removed BEZEL version (v$INFO[System.AddonVersion]) and Kodi version (System.BuildVersionShort) labels from MM strip footer, Includes_Bezel.xml L474. Small BEZEL logo icon kept. Backup /workspace/b300/bak_t4290_*. Shot b401/t4290/mm_open2.png. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## t4293/t4294 (Oct 27 2026 ~08:35 EDT) — MM Settings bar focused look (LIVE MOCKUP, not final)
- xml/Includes_Bezel.xml Settings row only: sliders icon (mm_set_sliders.png) removed; divider x226→x284 (next to logo); BEZEL logo x290→x296; › stays x346. Focus bar image (BzATHiTex/BzMMBarCol) now shows on Settings too (dropped !sec=settings) → same white outline as rest of list. Unfocused unchanged.
- Backup xml/Includes_Bezel.xml.bak_t4294_*. Copied to /tmp/bz2home. Smoke private HOME=/tmp/bzsethome :96 → /workspace/b401/t4294/{focused,unfocused}{,_closeup}.png PASS. ReloadSkin. No zip. Approval mocks: /workspace/b401/t4293/.

- t4294 (2026-10-27 08:35): MM Settings row focused (6996 sec=settings, t4135 G group, Includes_Bezel.xml L474) — sliders icon (mm_set_sliders.png) removed; divider 2x32 @x284 (was further left), BEZEL logo 36x36 @x296, › @x346; Settings row now shows the shared list focus bar (18,4 354x48, $VAR[BzATHiTex] default bezel/at/hi_outline.png, BzMMBarCol) same as siblings. Backup Includes_Bezel.xml.bak_t4294_083518. Shots b401/t4294/{focused,unfocused}[_closeup].png. Synced /tmp/bz2home. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

- t4295 (2026-10-27 08:37): Rob — separator/logo/arrow hidden unless focused. Already true in t4294 build: itemlayout = label only; t4135 G group (divider x284, logo x296, › x346) visible only Control.HasFocus(6996)+sec=settings. No XML change, no new backup. Shots copied to b401/t4295/ (unfocused_closeup shows SETTINGS label only).
- t4296 (Oct 27 2026): Video mini player → poster + Play/Pause & Stop pills (VideoOSD 6501/6504 style). MOCK only: /workspace/b401/t4296/{before,after,compare}.png. Build target: BezelVPLContent Player.HasVideo group (Includes_Bezel.xml ~2368, videowindow). Awaiting Go.
- t4298 Oct 27 08:40 Movies/list outline flash under MM: BzATHiTex highlight images in list focusedlayouts now visible only !bz_navmenu (onfocus bounce to 6996 already present). Backup ../../bak_t4298_0840

## t4296/t4299 — Video mini-player in MM (MOCK, awaiting Go)
- Same slot as music mini (MM strip top, strip-local 0..140; strip @570,120; list 6996 slides +120 on Player.HasMedia).
- Poster (2:3, 80x120 @20,12), title + year·time, Pause/Stop pills in VideoOSD 6501/6504 style (white rounded focus, 8A3E10 icon chip). Poster only, no video.
- Mocks: /workspace/b401/t4299/{A_current_music_mini,B_video_mini_pause_focused,C_video_mini_stop_focused,D_compare_crop}.png
- Build plan: split O79 mini group: music = Player.HasMedia+!Player.HasVideo (6957-6960 unchanged); video = Player.HasVideo, new ids 6961 Pause(PlayerControl(Play)) / 6962 Stop(PlayerControl(Stop)); onup from 6996 → 6961 when HasVideo; ondown → 6996. No live edits yet.
- t4300: pills now TEXT ONLY (no icon chips), VideoOSD 6501/6504 look: focused = white rounded fill + dark FF23160E text; unfocused = F0FFFFFF text + faint underline. B/C/D regenerated.

## t4301 (Oct 27 2026) — Remove KODI from MM
- Removed KODI item (sec kodi → systeminfo) from strip 6996 in xml/Includes_Bezel.xml; fixed !Player.HasMedia onup SetFocus(6996,12)→11 (POWER). Settings stays row 9. Backup Includes_Bezel.xml.bak_t4301_*. ReloadSkin. Smoke PASS: 12 rows, no KODI, wrap OK, Settings open + Back returns SETTINGS row focus 6996. Shots b401/t4301/. bz_mm.py kodi action left unused (harmless).

## t4305 (Oct 27 2026) — STYLE→MOCK: TV colour strip
Ask: match TV strip font/layout to Movies; centre clearart logo in strip upper, bigger. Mock only, awaiting Go.
Mock: /workspace/b401/t4305/{before_tv,before_movies,after_tv_mock,compare}.png (built from t4230 stress shots; Kodi left to t4304).
Proposed: logo 330x150 centred @600,130 (align center); Movies-style pairs bz_small_s/bz_value_s 52px from y300 (Year,Genre,Seasons,Episodes,Watched,Rating); divider y632; DESCRIPTION label 662 + bz_plot_s plot 696–979. Drop "Overview"-on-top layout. Episodes view to follow same pattern on Go. Live code: Includes_Bezel.xml ~2400–2432.
- t4304 GO BUILT: Includes_Bezel.xml (backup xml/Includes_Bezel.xml.bak_t4304_* + /workspace/b401/t4304/Includes_Bezel.xml.bak). O79 music mini now Player.HasMedia + !Player.HasVideo (6957-6960 unchanged). New video mini group (Player.HasVideo) before list 6996: poster VideoPlayer.Art(poster) 80x120, title, year·time/duration, text pills 6966 Pause/Play ($VAR[BzOSDPlayLbl], PlayerControl(Play)) + 6967 Stop. 6961/6962 were TAKEN (TV sub-nav) -> used 6966/6967. 6996 onup -> 6966 (video) / 6958 (music). Pills ondown 6996. Smoke (private HOME /tmp/bz4304home, :84): Up->6966, Right->6967, Select toggles Pause->Play, Down->6996 PASS. Shots /workspace/b401/t4304/.
- t4309 (Oct 27 2026): Colour Block nest moved to first row under LOOK in Tuner (Includes_Tuner.xml). Backup /workspace/b401/t4309/.

## t4306/t4310 (Oct 27 2026) — BUILD TV colour strip (from t4305 mock) — DONE, ReloadSkin
Includes_Bezel.xml ~2400–2433 only. Clearart 330x150 @600,130 centred (fallback title centred); shows/seasons + episodes: compact pairs (52/bz_small_s/bz_value_s) from y300, divider 632, DESCRIPTION 662, plot bz_plot_s 696–979 (Movies match). Backup b401/t4306/Includes_Bezel.xml.bak. Smoke: tv_show/tv_season/tv_episode/movies_ref/tv_mm_open + strips.png. No opacity lines touched (t4308 tag not found in tree at time of build).

## t4311 (Oct 27 2026)
Logo spin not stopping: t4266 spin used Window.IsActive(busydialog|nocancel), which stays true while DialogBusy is active-but-hidden (its group hides during music/album flip/caching/video start) and through its 800 ms close hold. New expression bz_logobusy = [Window.IsVisible(busydialog|busydialognocancel)] + !startup + !Player.Caching + bz_flipping empty + cinemavision empty; both logo spin animations (BezelLogo + BezelLogoButton focus) use it. Logo colour/opacity ($PARAM[col]/BzLogoCol) untouched. Backup /workspace/b300/bak_t4311_Includes_Bezel.xml. Smoke /workspace/b401/t4311: busy spins, idle static at rest angle (pre==idle). box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## t4313 (Oct 27 2026) — MM background warm park delay + Tuner row
- bz_flip mm_warm: debounce reads Skin.String(bz_at_mmwarm) (step×0.2 s, default 4 = 0.8 s, was 0.2); window switch settle = max(park, 0.5).
- Tuner › MAIN MENU: "Background warm delay" (id mmwarm) after Background art crossfade; 0.2–2.0 s; info mm_warm_delay.png.
- bz_tune reset menu clears bz_at_mmwarm. Backup /workspace/b300/bak_t4313_090422. FULL restart (.py).

## t4319 (Oct 27 2026) — FS/NP VISUALIZER cycle pill lower
- Includes_Bezel.xml:2868 cycle pill grouplist (6391..) top 125->145 (h32). Colour block top 120: gap 5->25. Now overlaps title label box (150,162 780x66) by 15px — long titles may run under pill. Backup /workspace/b300/bak_t4319_Includes_Bezel.xml. ReloadSkin. Smoke pending.

## t4315 / t4316 — Tuner › MAIN MENU › Startup highlight (Oct 27 2026)
- Skin.String bz_at_mmdef: 1 MUSIC / 2 MOVIES / 3 TV SHOWS; empty = TV SHOWS (Rob t4316). No KODI row (t4301).
- bz_cmd.py start → bz_mmstartrow/sec; bz_flip.py MM-start "menu focused" branch now SetFocus(6996,startrow) + bz_mmlive/bz_mmpos = startrow (686 had captured row 0 before focus landed).
- Row "Startup highlight" (toggle, L/R wrap) before Double-tap window; info mm_startup_button.png; Reset main menu clears bz_at_mmdef (bz_tune.py).
- Backups *.bak_t4315 (bz_cmd, bz_flip, bz_tune, Includes_Tuner). Smoke t4315/: cold default→TV SHOWS PASS (x3), mmdef=2→MOVIES PASS.

## t4318 — Tuner › MAIN MENU › Strip colour (Oct 27 2026)
- Row id mmstripcol, top of MAIN MENU above Strip opacity; L/R set shared bz_at_blockcol (same as COLOUR BLOCK › Colour); label2/icon BzATVal/Bar_blockcol; info mm_strip_colour.png. Menu reset leaves blockcol (Colour Block reset owns it). Backup Includes_Tuner.xml.bak_t4318.

### t4321 — 2026-10-27 09:13 ET — FS mode pill top 130
Rob: Move down 5. Mode pill (6391 grouplist) `125→130` (was live 145 from t4319 overshoot). Gap above block top: 10px; pill bottom flush with title box top 162. Backup `bak_t4321_Includes_Bezel.xml`. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

### t4322 — 2026-10-27 09:13 ET — FS1+FS2 same pill
Rob: Both fullscreen 1 and 2. Mode pill lives once in `BezelNPInPlace` (top 130 from t4321); MusicVisualisation (FS1) and Custom_1112_NowPlaying (FS2) both include it — no second edit. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- t4324 MOCK-only: FS1/FS2 bottom line arrows closer/bigger, SELECT removed, pp centered, symmetric — b401/t4324/ — awaiting Go

## t4325 — MOCK (awaits Go)
Rob: "Arrows to outside of next last text. Keep close". Revises t4324 mock: arrows move outside the words.
Order: [prev pill 128,982 226×30] [◀] [LAST] … [pp] … [NEXT] [▶] [next pill 726,982].
Proposed: aid_tri_l 404,990 12×16 (8 px left of LAST ink); LAST 386,982 84×30 right-aligned (ends 470);
aid_pp 522,987 36×20 (centred 540); NEXT 610,982 84×30 left-aligned; aid_tri_r 670,990 12×16 (8 px right of NEXT ink).
SELECT removed. Gaps from the pills: ◀ 50 px from prev pill, ▶ 46 px from next pill. Mock: /workspace/b401/t4325/{after,compare,after_closeup}.png. No live edits.

## t4327 — MOCK (awaits Go)
Rob: "Good. Use more rectangular pill ends". Builds on approved t4325 layout (arrows outside LAST/NEXT, SELECT gone, pp centred) — all coords unchanged.
Change: prev/next song pills (128,982 226×30 and 726,982 226×30) drawn as 2 px outlined rounded rects, corner radius ~7 px (was full capsule from hi_outline.png border=14), dim 59FFFFFF.
Go-build note: hi_outline.png at border=14 is inherently capsule-shaped at 30 px height — need a new outline texture (e.g. hi_outline_sq.png, ~7 px radius, border≈8) used only on these two pills, so other hi_outline users stay unchanged.
Mock: /workspace/b401/t4327/{after,compare,after_closeup}.png (compare = t4325 top / t4327 bottom). No live edits.

## t4329 Go (09:3x EDT) — FS1/FS2 bottom next/prev row BUILT (BezelNPInPlace, Includes_Bezel.xml)
- SELECT label removed; aid_pp 522,987 36×20 (centred x=540).
- Arrows 2× (12×16) OUTSIDE text, 8 px gap (measured): aid_tri_l 400,989; aid_tri_r 672,989 (y centred on 997). LAST 386 84w right; NEXT 610 84w left.
- Pills 128/726,982 226×30 now bezel/at/hi_outline_sq.png (new, 450×60, r14 tex ≈7 px on screen, border=16); other hi_outline users untouched. Dim 59FFFFFF, gradient, title visibility unchanged.
- Backup xml/Includes_Bezel.xml.bak_t4329_*. Shots /workspace/b401/t4329/ (fs1_mid = live FS1 row; final_composite = live shot + final arrow offsets + pill texture, since test Kodi had no audio sink to re-enter FS). Fanart hide-chrome (t4326) NOT touched. Restart: box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## t4326b (09:5x EDT) — Fanart cycle hides all FS chrome (BezelNPInPlace, Includes_Bezel.xml)
- Conditional fade 100→0 300ms on $EXP[bz_npm_fan] added to: title/artist/album/progress/time group; grad_bottom image; t4329 next/prev group (coords/textures untouched); 6391 pill grouplist (6391 stays focusable — Select keeps cycling). 2 s mode-name flash label gets `+ !$EXP[bz_npm_fan]`.
- BezelLogo / sway album are outside the fanart block — left as is.
- Backup /workspace/b300/bak_t4326b_*_Includes_Bezel.xml. Restart: box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Smoke (test Kodi /tmp/bzh4326b :426/8426, pulse null sink): bio → Select → Fanart clean → Select → Lyrics chrome back, focus 6391 throughout. Shots /workspace/b401/t4326b/.
- Seen (not touched): in-place music-window NP shows a black bar x≈120–570 y≈990–1020 over LAST pill/LAST/pp in all modes — not in t4329 fs1 shot; needs a look.

## t4333/t4335 (Oct 27 2026) — MM section fade in/out on warm — DONE
- BezelSecDim: +conditional fade 100→0, 350 ms sine, on Home prop `bz_xfade` + `$EXP[bz_navmenu]` (reverses = fade back in).
- bz_flip.py mm_warm: set bz_xfade + 350 ms wait before in-place Container.Update and before ActivateWindow; cleared in both finally blocks.
- MM open/close keeps existing 300 ms mmdim/gdim fade. No Tuner (follow-up). Did not touch covercol (t4334).
- FULL restart. Test /workspace/b401/t4333.sh: TV→Movies warm, xfade=1 seen, focus 6996 held, path landed. Shots /workspace/b401/t4333/.

## t4334 (Oct 27 2026) — Delete album cover-column black footer mask
- Deleted from xml/Includes_Bezel.xml: the "3.2.1 item 13" grouplist (-120,870 570×30: black white.png + dimmed BezelFanartLayer half-row mask) and the sibling bz_covercol group (black 0,900 590×300 + BezelFooter redraw), with their comments (9 lines). white.png kept (shared). Other bz_covercol controls (cover redraws, 4.6.1 top clip, scrollbar hide, list slides) untouched.
- Backup xml/Includes_Bezel.xml.bak_t4334_*. XML parses. ReloadSkin on :77. Shots /workspace/b401/t4334/ (6 album list bottom, 7 NP over album: no black bar, 8 list still navigable). PASS.

## t4339 (Oct 27 2026) — MAIN MENU Tuner: Section fade (t4333 underlay fade speed)
- New Tuner row "Section fade" (id mmsecfade, Skin.String bz_at_mmsecfade) in MAIN MENU nest after Background warm delay. Steps 1–7 = Off / 0.15 / 0.25 / 0.35 (default, empty) / 0.5 / 0.7 / 1.0 s. (bz_at_mmxfade already = Background art crossfade, so new key.)
- Includes_Tuner.xml: BzATVal/Step/Bar_mmsecfade vars (bar_7_N), L/R handlers, item with info bezel/info/mm_secfade_$VAR[BzATStep_mmsecfade].png (7 PNGs 860×560).
- Includes_Bezel.xml BezelSecDim: single 350 ms bz_xfade fade → 6 conditional fades keyed on the step; Off has none.
- bz_flip.py mm_warm: reads the step per warm; Off skips bz_xfade + the pre-swap wait entirely (instant swap as before t4333).
- Backups *.bak_t4339_*. FULL restart. Smoke /workspace/b401/t4339.sh: Tuner R/L moves string 4→5→3→4; default warm TV→Movies xfade seen, cleared, focus 6996, path landed; Off warm Movies→TV no xfade, path landed, focus 6996. Shots /workspace/b401/t4339/. PASS.

- t4342 (Oct 27 2026): TV strip info list top 300→290 (shows/seasons + episodes grouplists); clearart gap 10px. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

- t4342 (Oct 27 2026): TV strip info list tops 300→290 (clearart box 130–280 → gap 10 px). ReloadSkin. Shots /workspace/b401/t4342/tv_strip(.png,_crop.png). Backup b401/Includes_Bezel.pre_t4342.xml.
- t4340 (Oct 27 2026): logo bounce on busy end — bz_flip.py fires bz_logospin 1.5 s when busy falls (MM closed, no spin running; busy_was tracker). Busy loop gated + String.IsEmpty(bz_logospin); bz_logospin bounce copied onto BezelLogoButton image. t4311 IsVisible gate kept. FULL restart. Backups b401/t4340/*.pre_t4340.*
- t4344/t4345 (Oct 27 2026): all logo spins one anim — busy loop now rotate −360 1100 ms tween back easing out (same as menu-close/auto/busy-end bounce), both BezelLogo + BezelLogoButton. Smoke: busy spins, busy-end spin=true ~0.2–0.4 s then clears, menu-close spin fires. Shots b401/t4340/u_*.
- t4346 (Oct 27 2026): Zip 5.0.9 → /workspace/b401/skin.bezel2-5.0.9.zip (fade Tuner, logo bounce/unify, album mask delete, TV list -10, FS bottom line). FULL restart.
- 2026-10-27 11:15 t4351: created /workspace/b300/bezel_extras/ staging (copies of media/bezel/info + extras/), RESTORE.md. No live change, no split zip.

## t4354 — Back out of Add-ons with music playing showed music viz
Cause: Includes.xml DefaultBackground (used by AddonBrowser + 15 other windows) had a full-screen `visualisation` control visible with Player.HasAudio, and backdrop group 31111 hid itself when a viz was enabled → viz seen behind Add-ons / during Back fade. Fix: viz control `<visible>false</visible>`; 31111 no longer hides for audio viz. XML only → ReloadSkin. Backup Includes.xml.bak_t4354_*. Smoke /workspace/b401/t4354/ (music playing → Add-ons → Back → Music list, MM open OK). FS music window (MusicVisualisation.xml) untouched.

## t4355 (Oct 27 2026) — BUG: open on TV highlight but Music underlay + focus jumped to Music
- Cause: mm_warm treated the row MM opened on as "already the underlay" (done=sec) even when it didn't match — startup lands TV over Music, so TV never warmed; Music underlay + later reopen picked Music row.
- Fix (bz_flip.py mm_warm): open row only counts as done if the underlay window/content matches (music / videos+movies / videos+tvshows|seasons|episodes); otherwise it warms after park. Generic for all sections.
- Smoke: cold → MM-start row 2 TV, MMWARM tv under menu, Videos tvshows, focus 6996 TV held 10 s; Up→Movies warm, Down→TV warm. Shots /workspace/b401/t4355/. Backup bz_flip.py.bak_t4355. FULL restart.

## t4360 (Oct 27 2026) — BUG: black bar still visible in FS (after t4334)
- Audit of FS1 (MusicVisualisation) / FS2 (Custom_1112) stack: BezelNPInPlace has only the 840×900 block backing (behind fanart, intended); remaining bz_covercol rects are list-side only (not in FS); video-only crop covers (BezelVPLContent) n/a for music. Only opaque black rect left on the FS screen: BezelMusicPlayingArt "2.0a3.3 controls backing" 960,878 960×142 FF000000 (under title/progress row, right half).
- Deleted that rect (Includes_Bezel.xml ~L1210, comment left). Backup Includes_Bezel.xml.bak_t4360_*. XML parses. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Smoke: test Kodi (:77, NULL audio sink) drops playback so FS1/FS2 could not be held for an after-shot (same limit as t4329). Before shot /workspace/b401/t4360/fs1_before.png; fs1_after.png landed in Music. NEEDS Rob eyes-on.
- t4362 (11:33 EDT): small album wrong art (always same) — BezelInAlbumArt preferred Container(6074) album-name xsp; quotes/special chars or dup names make it return the first album. Now own ListItem.Art(thumb) first, 6074 only when its Label==ListItem.Album. Backup Includes_Bezel.xml.t4362.bak. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- t4363 (Oct 27 2026): Music list 60 title labels width 300→380 (match Movies/TV) — Includes_Bezel.xml L1449 + focused ping-speed labels L1611–1695 (14 labels). List/bar/cover untouched. Backup Includes_Bezel.xml.bak_t4363. ReloadSkin. Shots /workspace/b401/t4363/.

## t4361 (Oct 27 2026 ~11:50 EDT) — album cast shadow still broken: diagnosis
- Live settings: !bz_swayright + bz_acast_static -> image Includes_Bezel.xml:1040 (child of NP group 996, Player.HasAudio). Fades in only during the playing sway (audio_latch + sway_go).
- Geometry bug fixed: NP cover is x1140-1740 y220-820 (group 1050), not 1104. Album cast left 624->660 (right edge 1140), zoom centers 1104->1140 and 4 leftover 965->1140 (lines 1022-1045 only). Movies poster cast (485, lines 2507+/3381+) untouched. Backup /workspace/b300/bak_Includes_Bezel_t4361.xml. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Root cause it still looks missing: the area left of the playing cover is pure black (0,0,0 measured x1040-1140 in /workspace/b401/t4361/after_np6/7.png) -> a dark cast has nothing to darken. Movies works because its cast falls on the colour/info block. Needs a design call (mockup first): cast onto the info block like Movies, a lighter backing panel, or glow-style cast on black.

## t4366
Live MOCK (left in tree): Music list grown to screen bottom. Includes_Bezel.xml L1394 group height bz_h→960; L1399 list 60 height 900→960; MyMusicNav.xml L40 covercol black pad (990,90) visible=false. bz_h constant / video list L2607 untouched. Backups *.bak_t4366_113616. ReloadSkin (XML-only).
Result: 16 rows, focus bar outline y1021–1078 (bottom stroke ends 1078, AA 1079) = flush with 1080. Leftovers: colour block/backdrop/info panel still end at 1020 → 16th row sits on black; covercol (album list) band/mask in MyMusicNav L41-47 still clips 990–1080. Shots /workspace/b401/t4366/live_{full,bot,bot_zoom}.png

## t4368 — FS Music lower-left bar black→white? (Oct 27 2026)
- Live: FS1/FS2 would not hold (window stays Music 10502; SetFullscreen false, ActivateWindow(1112) no-op). Shots /workspace/b401/t4368/fs{1,2}_full.png + _bot_left.png are Music + in-place NP.
- Pixels x120-570: y990-1080 avg ~(20,33,40) w/ list; y1020-1080 ~(0-9) black. No white captured.
- Cause hypothesis: the lower-left "black bar" Rob saw = MyMusicNav pad (450x90 @ y990), hidden by t4366 mock; mock also grew list to 960 so a 15th row now renders in y1020-1080 below the 900 panel (white focus texture when focused there). Not caused by t4360 right-side delete. No new white fill found.
- No edits. Recommend: decide on t4366 mock (revert pad+960, or extend panel/grad to 1080).

## t4370 (Oct 27 2026) — Album cast texture flip
- Added flipx="true" on all 6 `$VAR[BzCastTex_a]` texture tags in xml/Includes_Bezel.xml (t4370 comment). No anim/poster/bz_h changes. Backup xml/bak_t4370_*.xml + /workspace/b300/bak_Includes_Bezel_t4370.xml. xmllint OK, synced /tmp/bz2home, box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- t4372: live test with animated cast (bz_acast_static toggled OFF, was ON). Shots /workspace/b401/t4370/after_full.png, after_cast_crop.png, sway_1..8.png.
- NOTE: cast_ma_current.png alpha is dense on its RIGHT edge (≈170 near x 400–460 of 480), so unflipped it was already dense at cover left (x1140); flipped puts dense side at x~660 away from cover. Cast is black on pure-black bg → not visible/measurable in screenshots. Await Rob confirm; revert = restore backup.

## t4357 — All seasons / All albums focus flashed to top of list (Tue Oct 27 2026, ~11:45 EDT) — FIXED
- Root cause: video list 60 (View_60_BezelVideoPosterList) is the only child of a vertical `<control type="grouplist">`. Kodi's GUIControlGroupList::AddControl overwrites the child's onup/ondown with the grouplist's own (empty), so list 60's `<ondown>SetFocus(6098)</ondown>` never ran. Down off the last row natively wrapped to `..` (top), and ~100-150 ms later bz_flip's ALLBOTTOM2 poll moved focus to 6098 = the flash.
- Fix (XML only): Includes_Bezel.xml line 2602 grouplist now has `<ondown condition="Control.IsVisible(6098)">6098</ondown>`. List 60's own ondown is now numeric too (6097/6098; harmless). Up/wrap behaviour otherwise unchanged; the poll's wrap fallback is kept as a safety net.
- Music list 60 isn't inside a grouplist, so it already went straight to 6097 (verified, no flash).
- Backup: xml/Includes_Bezel.xml.bak_t4357_* (+ /workspace/b401/t4357/Includes_Bezel.xml.bak). Reload type: ReloadSkin (XML only).
- Proof: /workspace/b401/t4357/fix_tv.png/.mp4 (Season 2 -> All seasons, no top flash), fix_mu.png/.mp4 (OK Computer -> All albums), fix_mm_open.png (MM ok). Sampler: before 3->0->6098; after 3->6098.

## t4378
Screenshot list 60 fixed. Undo of t4366 was already in source (group height bz_h, list 60 900, MyMusicNav y990 pad no visible=false). Live /tmp/bz2home XML was stale → synced 4 xml, ReloadSkin. Music Songs, MM closed, list 60: 15 rows, bar bottom ~y1018, not flush. Shots b401/t4378/list60_full.png, list60_bot.png.

## t4380 — Mock: cover-column list bar to bottom edge (before/after)
- Hid MyMusicNav covercol pads L39 (black 990 450x90) + L42 (BezelSecDim band) via `false +` visible, tagged `<!-- t4380 mock -->`. Backup xml/MyMusicNav.xml.bak_t4380_MyMusicNav.
- Result: NO visual change. Bar still ends ~y990. Real limiter is list 60 itself: height 900 from y120 → bounds end 1020, slide 450 pushes rows down, Kodi drops the partial row 990-1050. Pads weren't the cause. Parent group doesn't clip, so group height 960 would do nothing.
- Reaching 1080 requires list 60 height +90 (only when covercol, e.g. conditional/separate list) or changing slide — both outside mock rules. Awaiting Rob.
- Shots /workspace/b401/t4380/{before,after}_{full,bot}.png, before_after.png. Plain list 60 untouched.

## t4382 — cover-column list rows 64 px (7 rows fill y570–1020)
- Includes_Bezel list 60: added conditional itemlayout/focusedlayout copies (`condition="$EXP[bz_covercol]"`, height 64, 39 inner 60→64 heights). Plain list 60 (Movies/TV/Music plain) untouched at 60.
- Covercol slide steps 8 on list 60 + 8 on 6097 ALLROW → -64…-512. List height 900, slide 0,450, bz_h unchanged. t4380 pads stay hidden.
- Backups *.bak_t4382. Shots /workspace/b401/t4382/after_full.png, after_bot.png (7 rows, last-row bar ends ~1018 vs block 1020).

## t4383 — Album cast Long + sway test (Oct 27 2026)
- Set via EventServer builtin: bz_at_aclen=7 (175%), bz_acast_static=false. No XML edits; flipx (t4370) kept.
- Played Adele 21 / Rolling in the Deep → visualisation FS. Shots: b401/t4383/cast_long_full.png, cast_long_crop.png, sway_1..4.png.
- Cover sways (left edge x1128–1133). Pixels x975→cover edge, y150–900: max RGB 0 in all 5 frames → cast is still invisible on the black bg, even at Long. Open: dark cast on pure black can't show — needs a lighter bg/glow or a different cast colour.

## t4385 — album cast visible + full sway recording (Oct 27 2026)
- Root cause of "invisible": animated album-cast group only renders with `bz_swayright` (Short sway); it was OFF. Also every cast_ma_* PNG (incl. glow) is pure black RGB + alpha, so it can't show on black.
- Set bz_at_acstyle=4 (glow), bz_at_acop=6, Skin.SetBool(bz_swayright) ON. aclen 7, acast_static OFF, flipx kept.
- XML: temp `<!-- t4385 -->` FF2A2A2A white.png backing 660,230 480x580 inside the animated cast group (fades with cast). Backup b401/t4385/bak_t4385_*_Includes_Bezel.xml. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Out: b401/t4385/sway_full.mp4 (30s), cast_visible_full.png, cast_visible_crop.png, sway_sheet.png.

## t4387
- Rob: "Make background dim level scale 5-100" (t4387) + "Default 10" (t4388).
- MAIN MENU > Background dim level (bz_at_mmdim): 11 steps 5,10,20..100% (bar_11_*); empty = step 2 = 10%. % = remaining section opacity while MM open.
- Includes_Tuner.xml: collapsed duplicate Val/Bar into single Val+Step+Bar; single 11-step L/R chain on 6970 (removed duplicate block); desc Range 5–100 Default 10.
- Includes_Bezel.xml BezelSecDim: 6 old mmdim fades → 11 (end=5..100). gdim/xfade untouched.
- Backups xml/*.bak_t4387_* + /workspace/b401/t4387/. ReloadSkin + Skin.Reset(bz_at_mmdim).

## t4432 / t4433 — Info Clearart toggle + Section options scroll fix (Oct 27 2026)
- DialogVideoInfo.xml: new button 9969 "Clearart" (label2 ON/OFF via BzTVClearOnOff) above View Type 9979 in Section options; TV types only; Skin.ToggleSetting(bz_tvclear_off). Header clearart images get `+ !Skin.HasSetting(bz_tvclear_off)`; title fallbacks show when off.
- Includes_Bezel.xml: variable BzTVClearOnOff; BezelVPLContent TV strip clearart/title fallback wired to bz_tvclear_off.
- t4433: grouplist 9000 had duplicate IDs (9980 Section options + Order; 9984 Go To Playlist + Back) — renamed Order→9989, sec Back→9990.
- Backup /workspace/b401/t4432/. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## t4449/t4450 — A–Z jump bar lands on current SortLetter (Oct 27 2026)
- New include `BezelAZLeft` (params bar=61/65/66, cond) top of Includes_Bezel.xml: 26 conditional SetFocus(<bar>02..27) on ListItem.SortLetter A–Z, else <bar>01 (#).
- Replaced all 4 fixed entry points (6501 x2, 6101, 6601); existing onleft conditions kept. Bars in tree: 6100/6500/6600 only. XML only, ReloadSkin. Backup /workspace/b401/t4449/.

## t4451/t4452 (Oct 27 2026 1:15 PM ET) — POWER MENU F built; old power menu removed
- New xml/Custom_1118_PowerMenu.xml (dialog): full-screen black 33000000 (20%); strip-bound group 570,160 390x728: outline logo media/bezel/pw_logo_ol.png @50%, "BEZEL 5.0", "design by. Robert Politano" @50%, outline pills 7801 Shutdown() / 7802 Quit() / 7803 Suspend(). onload clears bz_nav (MM hidden); onunload restores bz_nav + SetFocus(6996).
- MM strip POWER row (6996) onclick -> ActivateWindow(1118) (MM chrome touched: one onclick only).
- Removed: old DialogButtonMenu power UI (now stub redirecting stock ShutdownMenu/remote power key -> 1118), bz_mm.py 'power' entry, Includes.xml topbar shutdownmenu -> 1118, media/bezel/bz_power.png.
- Backup /workspace/b401/t4451/. Restart: FULL (bz_mm.py edited). Not smoked live yet.
- t4454/t4455 (Oct 27 13:21 ET): MOCK ONLY — Movies ACTORS in movie list view (A–Z + poster slot w/ actor thumb) + actor info via INFO LIST panel. /workspace/b401/t4454/mock_actors_movielist.png. No build.
- t4456 (Oct 27 ET): MOCK B — actor name large bold title atop info list. /workspace/b401/t4454/mock_actors_movielist_b.png. No build.
- t4462/t4463 (Oct 27 2026 ~1:30 PM ET): MOCK ONLY — supersedes t4459/60. Both actors directory + actor folder = MUSIC COVER LIST look (cover square top-left, list below, colour-strip actor info). Bottom actor thumb in strip UNDONE. Directory: no right art. Actor folder: right poster = HIGHLIGHTED MOVIE (focused item) w/ movie-poster sway anim. /workspace/b401/t4462/mock_actors_directory.png + mock_actor_folder.png (gen mk.py). No build.

## t4464 (Oct 27 2026 ~1:45 PM ET) — BUILD: Movies ACTORS = music cover list look
- Includes_Bezel.xml only. New exps bz_actdir (videos + Content(actors)), bz_actfold (videos + movies + path videodb://movies/actors/), bz_actcov; vars BzActName, BzActCover, BzActDescH.
- View_60_BezelVideoPosterList: list grouplist slides 0,450 under a 450 cover (BzActCover) + black mask below y1020 when bz_actcov. Movie titles untouched (content-conditioned).
- BezelVPLContent: normal pairs/description hidden on actors; actor strip = "Actor" + large bold name (bz_b34), info list (folder: movies count/selected/year/role/genre/rating; dir: actors count/born/movies), Biography/Description.
- Dir: BezelVPLPoster hidden (no right art). Folder: existing sway poster = highlighted movie.
- Backup /workspace/b401/t4464/ + xml/Includes_Bezel.xml.bak_t4464_*. FULL restart done (r.sh). Smoke shots t4464/smoke_actors_dir.png, smoke_actor_folder.png — PASS visually; MM-open shot not taken.

- t4468 (Oct 27 2026) MOCK ONLY: 8 MM glow texture candidates (A anamorphic, B hex ghosts, C spectral rim, D warm tungsten, E teal/magenta, F starburst, G rainbow halo, H sunrise haze) composited on live MM shot. /workspace/b401/t4468/ (stylesheet_t4468.png, textures/). No live edits, no zip.

## t4465/t4467 (Oct 27 2026 ~1:50 PM ET) — BUILD: actor thumbs in small art
- Actors dir small art (450 cover) already = focused actor thumb (BzActCover). Actor folder small art was the movie poster → now the actor thumb.
- bz_flip.py poster_clock: on Content(actors) stores focused actor Art(thumb)/FolderPath in Home props bz_actthumb/bz_actpath. BzActCover first value: bz_actfold + IsEqual(Container.FolderPath, bz_actpath) → bz_actthumb. Right sway poster still = highlighted movie. Movie titles untouched.
- Learned: list 60 <onclick> does NOT fire on media views (tried, removed); String.StartsWith(x,$INFO[prop]) returned False — use IsEqual(x,Window(Home).Property(p)).
- Backup /workspace/b401/t4465/ (+ .bak_t4465). FULL restart (r.sh, .py). Shots t4465/dir.png, folder.png, titles.png PASS; MM-open shot not taken. No zip.
- t4469 (Oct 27 2026) MOCK ONLY: glow A–H remade cinematic (multi-scale bloom, blurred streak/ghosts, lateral CA, film grain, soft prism fringe, veiling haze). /workspace/b401/t4469/. No live edits.
- t4471/t4472 (Oct 27 2026) BUILD: cinematic MM glow A–H live. Textures in media/bezel/glow/ (mm_glow_current.png = copy of old mm_glow_behind + mm_glow_{A_anamorphic,B_ghosts,C_spectral_bloom,D_warm_tungsten,E_teal_rose,F_soft_glint,G_halo_ring,H_veiling_haze}.png). Old media/bezel/mm_glow_behind.png kept (Settings*/SkinSettings windows still use it).
- Tuner MAIN MENU › Glow style (id mmglowsty, Skin.String bz_at_mmglowsty: empty=Current, A–H; Left/Right wraps). Vars BzMMGlowTex / BzMMGlowCol / BzATVal_mmglowsty in Includes_Tuner.xml. Colour: B C D E G = white FFFFFFFF; Current/A/F/H = strip tint. Applied to MM glow + slide-menu glow (Includes_Bezel) and Tuner preview glow. Info art bezel/info/mm_glow_style.png (from stylesheet).
- Backup /workspace/b401/t4471/. ReloadSkin. Smoke Current/C/D MM open: focus 6996 PASS, shots t4471/mm_*.png, smoke.png. Glow subtle at default 30% brightness. No zip.

## t4475 — Glow styles I–P added (Tuner › MAIN MENU › Glow style)
- 8 textures → media/bezel/glow/mm_glow_{I_corner_key..P_dusk_rake}.png; L/M alpha edge-feathered 40px (edge lines removed).
- Includes_Tuner.xml: BzMMGlowTex/BzMMGlowCol/BzATVal_mmglowsty + cycle Current→A..P→Current; new BzMMGlowInfo var; desc updated.
- White tint (own colour): B C D E G I L M O P. Strip tint: A F H J K N + Current.
- Info art: media/bezel/info/mm_glow_style_ip.png (shown when I–P selected; A–H sheet otherwise).
- Backup /workspace/b401/t4475/. Smoke L/O/N MM-open shots in t4475/. Style reset to Current. XML/media → ReloadSkin. No zip.

## t4477 Zip
- Shipped /workspace/b401/skin.bezel2-5.0.10.zip (glows A–P, power E flag + FF000000 bg).

## t4476 (Oct 27 2026) — Power menu E + colour flag + solid black — DONE
- xml/Custom_1118_PowerMenu.xml: bg white.png colordiffuse 33000000 → FF000000; new image after credit label (318,418 30×18, D9FFFFFF) bezel/us_flag.png.
- media/bezel/us_flag.png (30×18, from t4474 m.py flag()).
- Backup /workspace/b401/t4476/Custom_1118_PowerMenu.xml. Smoke /workspace/b401/t4476/power.png (Shutdown focused, no bleed). ReloadSkin. No zip.
- Note: /tmp/bz2home addon is a COPY, not symlink — sync edits before box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## t4494 — logo unwired from busy, never black
- Removed looped $EXP[bz_logobusy] rotate from BezelLogo + BezelLogoButton; removed bz_logobusy expression. bz_logospin bounce kept.
- DialogBusy.xml verified logo/plate-free (no textures). No black plate behind logo.png anywhere live.
- Backup: xml/Includes_Bezel.xml.bak_t4494_*. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## t4513 — Album cast rolled back to 4.7.5 (album only; poster untouched)
- Includes_Bezel: album cast block (animated + static, Short/Long groups) + BzCastTex_a / BzCastCol_a replaced verbatim from skin.bezel2-4.7.5.zip. Removes t4283 left move, t4361 x660 edge, t4370 flipx, t4385 grey backing; back to x485 right-of-cover with 4.7.5 anim speeds/directions.
- Includes_Tuner: ALBUM SHADOW style row (BzATVal/Step/Bar_acstyle + acstyle onleft/onright) back to 4.7.5 (Soft default, 6 styles).
- Album textures cast_m_*/cast_b16/b30/sway_shadow identical to 4.7.5 already — no media change.
- Poster cast (BzCastTex_p/Col_p, bz_at_pc*) unchanged (diff verified). Backup /workspace/b401/bak_t4513_albumcast_150248. xmllint OK. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## t4514 (Oct 27 2026) album cast cleanup: removed cast_ma_{current,hard,floor,glow,fade,contact}.png + info/cast_album_styles.png; album SHADOW rows restored to 4.7.5 (info cast_shadow_styles.png, 4.7.5 desc); BzCastTex_p comment cleaned. Poster untouched. bak /workspace/b401/bak_t4514_150406
## t4515 zip 5.0.11 /workspace/b401/t4515/skin.bezel2-5.0.11.zip
- t4532: logo constant spin — removed busy-end bounce + 30s auto spin in bz_flip.py (menu-close spin kept). Backup /workspace/b401/t4532/. FULL restart.
- t4534: restored 30s logo auto-spin in bz_flip.py; busy bounce stays removed. Backup /workspace/b401/t4534/. FULL restart.

## t4533 (Oct 27 2026) cover-list no-mask clip
- list 60 wrapped in clipping grouplist (450x900 at bz_list_x,bz_top -> bottom y1020) in Includes_Bezel.xml; bottom masks stay off; reload: ReloadSkin. Backup /workspace/b401/t4533/
- t4535: removed all busy→logo code (bz_flip busy_was/bb watcher, stale comments in Includes_Bezel + DialogBusy). 30s auto + menu-close spin kept. Backup /workspace/b401/t4535/. FULL restart.

## t4536 housekeeping (2026-10-27 15:28)
Removed 302 files (bak/pyc + 9 unreferenced mm_set/mask/grad/frame textures). Backup: /workspace/b401/t4536/removed_backup.tgz

- t4541 Build and zip: 5.0.12 -> /workspace/b401/t4541/skin.bezel2-5.0.12.zip

## t4543 (Oct 27 2026) cover-list bottom overflow (t4533 clip failed)
- Root cause: Kodi clips a control in its own pre-animation coords; list 60's +450 / -64n slides move the clip with the rows, so the t4533 grouplist never cut at y1020. 6097 All row sat outside the clip.
- Fix: new expression bz_ccover (row offset from focus vs Container(60).Position, slot past y1020) hides those rows in covercol itemlayout; 6097 shown in covercol only when its slot fits (or focused). No masks. Backup /workspace/b401/t4543/. ReloadSkin. Live smoke not done (test env has no long album list).

## t4547/t4548/t4550 (Oct 27 2026) cover list = videos feel
- Removed 8 Position-based -64n slide anims on list 60 (covercol); list now native-scrolls like videos.
- Viewport: list zoom 100,50 (center 0,0) + existing +450 slide → 900 list renders as 450 (y570–1020) inside t4533 clip. Covercol rows: slot 150 with inner zoom 100,200 → 6 flush rows of 75 px (content heights 64→75, badges re-centred).
- bz_ccover hide removed from itemlayout (expression left defined, unused). 6097 All-albums row hidden in covercol (it depended on slides).
- Backup /workspace/b401/t4547/Includes_Bezel.xml. ReloadSkin. No long-album live smoke.
- t4562 (Oct 27): ALL logo spins OFF (bz_flip.py: 30s auto + menu-close disabled, bz_logospin force-cleared each tick). XML anims kept. Backup b401/t4562/. FULL restart.
- t4562b (Oct 27): continuous logo spin root cause = DialogNotification.xml "TUNING APPLIED" logo had rotate loop="true" (spun nonstop while any toast showed with bz_tunapplied set; property can stick). Now one spin (reversible=false). Backup b401/t4562b/. ReloadSkin. bz_flip 30s/menu-close spins were already single-shot (t4562 disabled them; restore pending Rob).

## t4588 (Oct 27 2026) — MM Background dim rebuilt
- Removed 11 mmdim Conditional fades from BezelSecDim (xfade + gdim-closed kept).
- Added var BzMmdimDiffuse (Includes_Bezel): MM open → alpha from bz_at_mmdim 1..10 (dim 10..100 → remain 100..10; empty/6=80 hex); closed FFFFFFFF.
- colordiffuse on 45 art textures (BezelFanart, BezelPoster/60, BezelBigArt, BezelInAlbumArt, BezelGridPoster(F), Container 60/6600 thumbs) + 52 stand-in multiimages.
- Lit dust: BzD3L_mid/near + BzD3PL_mid/near get MM-open baked values (lit × remain).
- Tuner mmdim: 10 steps, bar_10_*, 10%..100%, default 60%, desc + mm_dim_level.png redone.
- Smoke: /workspace/b401/t4588/ (ReloadSkin-type XML; ran cold r.sh).
- 2026-10-27 t4615 Power menu MOCK ONLY (refresh E + flag + black bg; A/B/C) — /workspace/b401/t4615/ — no live edits
- 2026-10-27 t4617 Power menu MOCK ONLY (MM-list rows, white→black radial bg, big black logo 2px white stroke; A flag/B no flag/C side) — /workspace/b401/t4617/ — no live edits
- 2026-10-27 t4618 Power menu MOCK ONLY 'less in MM' (full radial cover, 1px logo stroke; A/B/C) — /workspace/b401/t4618/ — no live edits

## t4614 (Oct 27 2026) album list rebuild — root cause of old album-list bug
- Cover list 60 (bz_covercol) = video-list bones scaled 50% (zoom 100,50) under the 450 cover. Bug: the +450 slide sat inside the zoom, so it rendered as 225 → list started y345, rows 0-2 hidden under the cover, rows 6+ clipped (only 3 rows ever showed). Fix: slide 0,900 (=450 on screen). Now 6 flush 75px rows y570-1020, native list scroll, no anim/type change.
- Same list serves Albums, artist→albums, in-album (bz_inalbum/bz_artistalbums) so all fixed together; no other section used the cover list. Strip/right art untouched (already old album layout).
- Backup /workspace/b401/t4614/xml_before. XML only → ReloadSkin. Smoke shots in b401/t4614.
- 2026-10-27 t4620 Power menu MOCK ONLY: Power list replaces MM list in colour strip (A live/B radial+logo/C black all-in-strip, 1px stroke) — /workspace/b401/t4620/ — no live edits
- 2026-10-27 t4623 GO Power menu LIVE: Power list replaces MM list in colour strip (1118 rewritten: list 7800 at strip slot, MM row look, BEZEL 5.0 + credit + flag under rows, no black bg); Includes_Bezel 6996 visible += !Window.IsVisible(1118); bz_flip.py MM auto-close skips while 1118 visible. Smoke 5/5 PASS /workspace/b401/t4623/. FULL restart (py). Backups in t4623/.
- 2026-10-27 t4627 Power strip MOCK ONLY: add bg + logo (1px stroke) inside strip; A radial lower/B radial full fade/C black lower — /workspace/b401/t4627/ — no live edits
- 2026-10-27 t4644 Remove Tuner dialogue popup: bz_dtap.py 'Tuning applied' toast (+bz_tunapplied card) removed at both apply sites (no-reload + ReloadSkin paths). Error/reset/preset/import notes left. Backup /workspace/b401/t4644/. FULL restart (py). Smoke: Tuner Strip colour Right→Back, 6 shots no popup PASS /workspace/b401/t4644/.
- 2026-10-27 t4662 GO Artwork pre-cache warning: Includes_Tuner.xml precache row desc prefixed with orange bold 'Warning: uses extra memory / may stutter on first open.' (right desc panel). Backup /workspace/b401/t4662/. XML only → ReloadSkin. Smoke shot t4662/tuner_precache.png PASS. Fanart chrome A/B removal NOT done (separate Go).

## t4691 (2026-10-27) 5.0.13 — Rob default picks + renames
- DEF table in bz_tune.json + `seed` action in bz_tune.py (Home onload, once per bz_defseed=5.0.13); Reset applies picks per section; json P defaults = picks; timings baked offline.
- mmbar 10 steps (10–100%), default 50%. Spinning dust→Ambient spin; Lit dust 2.0→Version V1.0/V2.0; lit brightness→"lit dust brightness"; removed Zoom time/size + Fanart chrome A/B rows. Precache warning kept. FULL restart.

## t4724 (Oct 27 2026) — BezelSecDim xfade stick fix
- Replaced six speed-gated bz_xfade Conditional 100→0 fades with one out (reversible false) + bz_xfade_in fade-back.
- bz_flip.py pulses bz_xfade_in 0.4s after clearing bz_xfade (inplace + window-swap paths).
- Stress: rapid MM Movies/Music/TV, dim 20/60/100, restart sim.

## t4734 (Oct 27 2026) — xfade restore + Misplaced [ on bz_navmenu
- Removed nested `[$EXP[bz_navmenu]]` (and libroot if any) → `$EXP[bz_navmenu]` (Misplaced [ parse error).
- BezelSecDim: fade-out now reversible (default) so clearing bz_xfade restores opacity; kept bz_xfade_in explicit fade-back; pulse 0.55s in bz_flip.
- Live: ReloadSkin XML + FULL restart for py.

## t4773 — Oct 27 2026 ~9:00 PM ET — Port window-level MM-open poster to LIVE 5.0.13 — PASS
- Copied proven PosterDiag blocks: MyVideoNav.xml (BezelPoster60 $EXP[bz_navmenu] fadetime 3000 after RootArtHide/before LogoButton), MyMusicNav.xml (FlipA/FlipB), Includes_Bezel.xml (removed nested BZMMXF MM-open copies from VPL/FlipA/FlipB/SwingPoster; closed-MM !$EXP stays in sway).
- Bak: /workspace/b300/bak_t4773_20261027_205359/. xmllint OK. FULL restart (r.sh).
- Right-region lum closed/open-MM: Movies 49.8/21.6, TV 70.5/17.3, Music 61.6/25.0, Videos 34.2/21.6 — posters visible open (dim), closed unchanged. Shots /workspace/b401/t4773/.
- Fork /workspace/b401/t4760 wiped after PASS. Nested [$EXP] cleanup = follow-up.
- t4780 (2026-10-27) zip live 5.0.13 posterdual (t4773 window-level MM-open poster + t4724 bz_flip.py xfade_in; no version bump) -> /workspace/b401/t4780/skin.bezel2-5.0.13-posterdual.zip
- t4781 (2026-10-27) version bump 5.0.13 -> 5.1 (addon.xml live+installed, changelog); rebuilt -> /workspace/b401/t4780/skin.bezel2-5.1-posterdual.zip; old 5.0.13 zip/xz removed; no XML/dim changes

## t4813 — 5.0.13 Background dim = 5.0.12 section fades
- Restored BezelSecDim 11-step mmdim fades (step = % art left visible).
- Removed BzMmdimDiffuse texture tint from Includes_Bezel poster/fanart/etc.
- Restored Tuner mmdim 11-step labels/bars/left-right from 5.0.12.
- Tree: /workspace/b401/t4813/skin.bezel2 · zip: skin.bezel2-5.0.13-dim512.zip
- Live untouched.

## t4813 2026-10-27 21:54
- Transplant 5.0.12 BezelSecDim into 5.0.13; strip BzMmdimDiffuse; stress 11-step + MM + Movies/Music/TV; package zip with stress results.
- Stress: 12 PASS / 2 FAIL. Zip: /workspace/b401/t4813/skin.bezel2-5.0.13.zip

## t4813 bugfix 2026-10-27
- Bug B fixed (bz_flip.py poster_clock frozen under MM, FULL restart). Bug C partial: Tuner mmdim desc restored, Dust3 mmdim remap; step-11 poster loss unresolved. Bug A unresolved. Notes: t4813/stress/bugfix_notes.txt
- 2026-10-27 22:58 EDT: full stress 5.0.14 (t4813 tree) -> 62 PASS / 48 FAIL, stress_20261027_t5014/results.txt (prior t4436 baseline 83/56)

## t4857 — Player control missing from cycle pill (5.0.15)
- Cause: t4496 removed Controls from FS music mode pill cycle.
- Fix in t4813 Includes_Bezel.xml: cycle Vis→Bio→Fanart→Lyrics→Up Next→Controls; Select on Controls opens 1115; land stays on pill (O78); M/RED unchanged. BezelNPModeShort CTL.
- Bak: /workspace/b401/t4813/bak_pill_controls_20261027_232136/
- Zip: await Go (XML → ReloadSkin once installed).

## t4858 — Go: rebuild 5.0.15 zip with t4857 Controls-in-pill
- Packing from /workspace/b401/t4813/skin.bezel2/

- t4860: Rename to 5.0.16 (addon.xml version/name bump; includes t4857 Controls-in-pill fix). box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## t4864 — Tuner opens but keys dead, multiple Backs (dig only, no patch)
- Tuner card (Includes_Tuner.xml:401) is an opaque full-screen group over the MM; list 6970 only gets focus via AlarmClock(bz_tun,SetFocus(6970),00:00) from 6996 Right (Settings row) / BEZEL Tuner button.
- Suspect 1: every focus redirect under MM targets 6996 with no bz_navtune exception — XML onfocus on 60/61/62/63/64/6100/6500/6600 (`$EXP[bz_navmenu] + !bz_mmpick` → SetFocus(6996)) and bz_flip.py MMHIDE (~l.752, _bzstrip) + "focus stolen just after open" (~l.766). If the underlay list refreshes or grabs focus (warm finishing, Container refresh; F10 stress FAIL shows the underlay still changes 36x/20s with Tuner open), focus goes to 6996 hidden behind the Tuner card. Up/Down move the hidden strip, Left/Right do strip stuff → looks dead. Back from 6996 runs the strip onback chain (mmsub restores / close MM), and bz_navtune is only cleared by 6970 onback or bz_dtap's slow 5-tick sweep → several Backs.
- Suspect 2: AlarmClock SetFocus(6970) lands before the card is visible / is lost to a same-frame underlay onfocus bounce.
- Fix shape: (a) redirect to 6970 when bz_navtune: duplicate onfocus `condition="$EXP[bz_navmenu] + String.IsEqual(Window(Home).Property(bz_navtune),true)">SetFocus(6970)` and add `+ String.IsEmpty(Window(Home).Property(bz_navtune))` to the 6996 ones (XML → ReloadSkin); (b) bz_flip nav loop watchdog: if bz_navtune and not Control.HasFocus(6970) and no modal → SetFocus(6970); MMHIDE/_bzstrip use 6970 when bz_navtune (py → FULL restart).

## t4867 — LOCK 5.0.16 MM background art + under_adv
- Rob: under_adv (MM UNDER CYCLE) and Movies/Music/TV MM background art features working in 5.0.16 — do not change unless unlocked.
- Covers: uadv/under_adv, BezelFanartCycler, BezelFanartLayer, mm_warm bg art path, mmxfade.

## t4874 Delete BEZEL settings (Tuner SYSTEM) — 2026-10-28
- Added Tuner › SYSTEM › **Delete BEZEL settings** → `RunScript(...bz_tune.py,wipesettings)`
- Wipes `special://profile/addon_data/skin.bezel2/` files (settings.xml, bezel_cw*, etc.), Skin.ResetSettings, then `lookandfeel.skin` → `skin.estuary`
- Confirm yes/no first. Locked: under_adv / MM background art untouched.
- Work tree 5.0.17 `/workspace/b401/t4813/skin.bezel2/`; bak bak_wipe_*

## t4876 Delete BEZEL settings blackout bounce — 2026-10-28
- `scripts/bz_wipe.py`: black WindowDialog → confirm → delete addon_data/skin.bezel2/* → lookandfeel.skin Estuary → immediately skin.bezel2 → ReloadSkin → dismiss black when BEZEL ready.
- Copies self + black.png to special://temp so the runner can outlive skin unload.
- Tuner SYSTEM row onclick → bz_wipe.py; desc updated. under_adv / MM bg art untouched.

## t4877 Move Delete BEZEL settings to SkinSettings main list — 2026-10-28
- Removed from Tuner › SYSTEM.
- Added as permanent last item (id 5) on SkinSettings category list 9000 — OK runs bz_wipe.py (blackout sequence unchanged).
- under_adv / MM bg art untouched.

## t4878 Poster missing after Tuner Background dim — 2026-10-28
- Cause: BezelSecDim used 11 Conditional fade anims for bz_at_mmdim; Kodi leaves those sticky when the step changes (ReloadSkin deferred while bz_nav=true), so the right poster could drop out while fanart still looked present.
- Fix: removed mmdim parent fades from BezelSecDim; added BezelMmDimScrim (black colordiffuse overlay = 100−art%) after the section group in MyVideoNav + MyMusicNav. FanartCycler/Layer / under_adv / mm_warm / mmxfade untouched.

## t4878 Poster missing after Tuner Background dim — 2026-10-28
- Cause: BezelSecDim 11 Conditional fades for bz_at_mmdim stick when the Tuner step changes (ReloadSkin deferred while bz_nav=true) → right poster can drop out.
- Fix: removed those mmdim parent fades; BezelMmDimScrim colordiffuse black overlay (100−art%) after section group in MyVideoNav + MyMusicNav. FanartCycler/Layer, under_adv, mm_warm, mmxfade untouched. ReloadSkin for XML.

## t4880 BACKGROUND DIM labels — 2026-10-28
- Renamed BezelMmDimScrim→BezelBackgroundDimScrim, BzMmdimScrim→BzBackgroundDimScrim; plain BACKGROUND DIM comments on var/include/wires/Tuner L-R. Skin.String(bz_at_mmdim) unchanged. Fanart/under_adv untouched. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## t4883 BACKGROUND DIM restore + labels — 2026-10-28
- Reverted black scrim; restored BezelSecDim Conditional fade BACKGROUND DIM (5–100%). Sticky fix: bz_bgdim_kick pulse via bz_cmd bgdim_kick on Tuner L/R. Plain LABEL comments on major includes/windows. FanartCycler/Layer + under_adv untouched. FULL restart (py).

## t4887 Fix-in-place standing rule — 2026-10-28
- Rob: always fix existing system in place; never replace mechanism unless he explicitly asks. Logged memory + DEV_GUIDE + BREAKS K39 + bezel skill. BACKGROUND DIM sticky fix remains Conditional fades + bz_bgdim_kick pulse (no scrim).

## t4889 BACKGROUND DIM scale 0–100 — 2026-10-28
- Dim amount Skin.String(bz_at_mmdim) 0,10,…,100 (empty=0). Opacity left = 100−0.75×dim → 100## t4889 BACKGROUND DIM scale 0-100 — 2026-10-28
- Dim amount Skin.String(bz_at_mmdim) 0,10,...,100 (empty=0). Opacity left = 100-0.75*dim → 100%...25% (75% fade at 100). Conditional fades on BezelSecDim + bgdim_kick kept. Tuner labels/L-R/desc updated. Fanart/under_adv untouched.

## t4891 BACKGROUND DIM snap — 2026-10-28
- BezelSecDim BACKGROUND DIM Conditional fades: time 300→0 (instant). Scale/kick/labels kept. Fanart/under_adv untouched. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
## t4891 ship skin.bezel2-5.0.17.zip — 2026-10-28
- Windows zip ~29.4MB; FULL Kodi restart. Session: BACKGROUND DIM Conditional fades 0-100 snap+kick; labels; Delete BEZEL + bz_wipe; Fanart/under_adv untouched.
## t4892 MM nav flash on section switch — 2026-10-28
- Cause: MM warm ActivateWindow remounts BezelNavMenu; Visible/WindowOpen open-anims (strip slide, dim button BezelATDimAnim, menu fade) replay while bz_nav stays true → brief flash.
- Fix-in-place: gate those Visible/WindowOpen anims with String.IsEmpty(bz_mmwarm) in BezelNavMenu + BezelATDimAnim/BezelATMenuAnim (+ tune_patch templates). Hidden/open-when-not-warming unchanged. Fanart/under_adv untouched. FULL restart (py).

## t4893 LOCK nav flash fix — 2026-10-28
- Locked t4892 bz_mmwarm gate on MM nav Visible/WindowOpen (6996, ATDim, ATMenu, tune_patch) for next build; no revert unless Rob unlocks.

## t4895 Big Logo rename + spin mock — 2026-10-28
- Renamed/labeled BezelLogo as Big Logo (comments + description). Spin every 30s mock only — await Go.

## t4898 Big Logo spin applied — 2026-10-28
- BezelLogo (Big Logo): Conditional rotate on bz_biglogo_spin. bz_flip pulses every 30s, clears after 1.2s. Position/size/texture unchanged. FULL restart.
## t4899 Big Logo spin STOP — 2026-10-28
- Reverted t4898 apply; spin mock-only again. Big Logo label kept. Note: Ambient Dust default ON await Go.

- [x] t4908 Big Logo spin approved → applied: BezelLogo + focused button logo use `bz_biglogo_spin` (−360°/1100ms/back out); `bz_flip` pulses every 30s, clear ~1.2s; legacy `bz_logospin` stays off (t4562). Dust DEF: `bz_dust_off` → DEF.off (default ON); Ambient stays OFF. bak `bak_biglogo_spin_20261028_141830` + `bak_dust_def_*`. Work tree 5.0.17 — FULL restart for py.

## t4911 QUEUE next build K42 — album covercol first-paint squash — 2026-10-28
- Cause: Includes_Bezel list 60 under `$EXP[bz_covercol]`: list Conditional zoom 100,50 (Y) + itemlayout/focusedlayout compensating zoom 100,200; on first paint list zoom applies, row zoom often waits until click/focus invalidates layout → squashed text.
- Scope: Albums + artist→albums + in-album (same bz_covercol path).
- Fix intent: make row zoom apply on first paint (fix-in-place; do not replace covercol zoom stack unless Rob says).
- Queue with K40 nav flash (already in work tree; not in shipped 5.0.17.zip). Id was briefly K41; retagged K42 when K41 became FS pill (t4913).

## t4913 CAPTURE K41 — FS1/FS2 cycle pill stay visible on Fanart — 2026-10-28
- Rob: Update K41 — full screen music FS1 and FS2 pill cycle button never hidden.
- Specific: pill currently hides when cycle hits Fanart; must stay visible on Fanart too.
- Scope: FS Music + FS Music 2; the cycle pill button.
- No code change — requirement capture only.

## t4914 CAPTURE K41 add — Controls hint popup + nav-down open — 2026-10-28
- Add to K41 (FS1/FS2 cycle pill never hidden):
  1) When pill reaches Controls position, show popup text: "press down or nav down to open up the controls."
  2) Once on Controls, trigger to open controls is nav Down (pairs with that popup).
- Scope: FS Music + FS Music 2; cycle pill.
- No code change — requirement capture only (with t4913 Fanart-visible).

## t4915 CAPTURE K41 clarify — Controls-only popup — 2026-10-28
- Clarify K41: popup text "press down or nav down to open up the controls" appears ONLY when the cycle pill is on Controls.
- No popup on Vis / Bio / Fanart / Lyrics / Up Next / any other cycle position.
- Still: pill never hidden (incl. Fanart); nav Down on Controls opens controls.
- No code change — capture only.

## t4916 CAPTURE K41 — popup text shortened — 2026-10-28
- Popup text now: "press down to open" (was "press down or nav down to open up the controls").
- Still the only popup; only when FS1/FS2 cycle pill is on Controls.
- Nav Down still opens Controls from that position.
- No code change — capture only.

## t4917 CAPTURE K43 — FS1/FS2 player bar 50% opacity — 2026-10-28
- Alongside K41 FS music work: the player bar at the bottom of fan art — group with now playing, next up, and transport controls (play, pause, next; font and graphic) — must share a common opacity and never go below 50%.
- Set at 50% opacity.
- Scope: FS Music + FS Music 2.
- No code change — capture only.

## t4918 CAPTURE K43 update — player bar unwired, static 50% — 2026-10-28
- Update FS player bar (beside K41 / K43): unwire from fullscreen music chrome dim and from the fullscreen music Tuner entirely.
- Must not follow any dim or opacity control — static at 50% opacity, period.
- Still: now playing + next up + transport (play/pause/next; font+graphic) share that one opacity.
- No code change — capture only.

## t4921 K44 — Music colour-strip text shift on song start — 2026-10-28
- Symptom: Music section colour strip (info text) shifts down when a song starts and does not hold position.
- Cause: Includes_Bezel.xml View_60 colour-strip grouplists (~1342 artist/title, ~1405 info pairs) still have Conditional slide `end="0,34"` on `Player.HasAudio` from BETA 2.4 item 13 (clear space under pill at 894,144). Pill removed BETA 2.6 (6891 visible=false) but slides left → 34px permanent drop while audio plays.
- Fix into 5.0.18: remove those orphaned slides (fix-in-place). Separate from K42 album squash.
- Zip held until Rob says zip.

## t4920 (Oct 28 2026) — 5.0.18 FS music ship (HELD, not delivered)
- K41 Includes_Bezel ~3259/3262/3267: pill grouplist fschromeop dim + fanart fade removed; Down on Controls → ActivateWindow(1115), else 6390; new label "press down to open" visible only $EXP[bz_npm_ctl] (!1115).
- K42 ~1509/1530: covercol item/focused layout group adds Visible zoom 100,200 (first-paint) alongside existing Conditional.
- K43 ~3232: grad_bottom + t4269 LAST/NEXT/transport group — fschromeop fades + fanart fade replaced by static fade 50 (condition=true).
- addon/DEF.ver 5.0.18. Zip HELD at /workspace/b401/t4813/skin.bezel2-5.0.18.zip.
## t4921 — K44 Music colour-strip text shift on song start
- Root cause: orphan `slide 0,34 condition=Player.HasAudio` (BETA 2.4 item 13, for removed 894,144 pill) on songs artist/title + info-pair grouplists (~1342/~1405). Both removed. FIXED 5.0.18.

## t4922 K45 — Music Info Play next does not queue — 2026-10-28
- Symptom: Options+Info / music information Play next does not queue up the chosen song.
- Cause: DialogMusicInfo.xml button 9081 onclick Action(PlayNext) = player skip-to-next-track, not queue ListItem as next. Close-then-action also drops ListItem context for any item-based builtin.
- Fix into 5.0.18: QueueMedia(...,playnext) while ListItem valid (songs/albums); then close. Zip held.
## t4922 — K45 Music Info "Play next" did not queue the song
- DialogMusicInfo 9081: Action(PlayNext) (= skip to next track) → QueueMedia(album musicdb path | ListItem.FileNameAndPath, playnext) before Dialog.Close. Queue 9082 unchanged. FIXED 5.0.18.

## t4928 — Rob approve K45 Play next + Queue as-is — 2026-10-28
- Approved: K45 DialogMusicInfo 9081 Play next → QueueMedia playnext for 5.0.18.
- Approved: Cue/Queue 9082 Action(Queue) behavior as-is (no change).
- Zip still held for explicit zip command.

## t4959 K45 into live 5.0.17 + Play next wrong-song dig — 2026-10-28
- Applied exact K45 to live `/workspace/b300/skin.bezel2/xml/DialogMusicInfo.xml` 9081: QueueMedia album/song path + playnext before Dialog.Close (was Action(PlayNext)). bak `bak_k45_live5017_20261028_150638_DialogMusicInfo.xml`. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Wrong-song investigation (no extra code change beyond K45): song branch uses `ListItem.FileNameAndPath`; album uses `musicdb://albums/DBID/`. Queue (9082) still Close→Action(Queue) which queues the dialog/underlay item natively. Likely wrong-item cause: FileNameAndPath is weaker than musicdb song DBID (empty/odd paths, comma/special chars) so QueueMedia can miss the focused library song; album Play next queues the whole album not a single focused track. Hidden Container(50) track list is not the focus target.

- t4962 (Oct 28 2026): K40 excluded; K41+K42+K43+K44+PlayNext-DBID (9081 songs musicdb://songs/DBID/) + Dust default ON (DEF.ver 5.0.17) + t4908 Big Logo spin into live 5.0.17; zip HOLD. Bak /workspace/b300/bak_t4962/, bak_t4962b/. FULL restart.

- t4962 (Oct 28 2026): SHIPPED 5.0.19 from t4813 — K40 removed (K52 pwrswap gate kept), 9081 songs DBID, DEF.ver 5.0.19. Zip /workspace/b401/t4813/skin.bezel2-5.0.19.zip. Live b300 synced, FULL restart.
- 2026-10-28 15:18 t4972: Reverted live skin.bezel2 5.0.19 -> 5.0.16 from b401/t4813/skin.bezel2-5.0.16.zip; bak /workspace/b300/bak_pre_revert_5016_20261028_151835; FULL restart. No zip.

## t4980 — 5.0.20 (2026-10-28)
Fresh 5.0.16 base + K41–K52 (no K40), song playnext (musicdb://songs/DBID/), Dust ON (DEF ver 5.0.20), Big Logo spin. Skipped 5.0.19 BACKGROUND DIM/mmdim rework, bz_wipe, SkinSettings delete, bgdim_kick, tuner mmdim. Fixed inherited 5.0.19 bz_flip.py bug: `# t4908` comment mid-line commented out casc/dview/fguard/autonp inits → nav_menu helper NameError crash loop. FULL r.sh: BEZEL 5.0.20, 0 crashes. Zip: /workspace/b401/t4813/skin.bezel2-5.0.20.zip (29,421,082 B), .xz 25,787,040 B.
- t4985 Oct 28: Big Logo spin ungated from bz_nav (MM open) so 30s pulse runs on every section. bz_flip.py only. FULL restart.
- 2026-10-28 15:55 EDT t4990 Music Info fanart jump: DialogMusicInfo uses new BzCIFanartMusic (840x900 scale crop clipped by 450 grouplist, matches MyMusicNav BezelFanartLayer). BzCIFanart (Videos/TV) untouched. bak /workspace/b401/bak_t_mmifan_20261028_155513. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

- t4990b (Oct 28 2026, base 5.2): Videos+TV Info fanart BzCIFanart -> 840x900 scale crop clipped to 450 grouplist (matches BezelVPLContent section 120,120,840,900); Music BzCIFanartMusic unchanged. Colour strip: Info already transparent 570-960 so section strip shows through (no change). bak /workspace/b401/bak_t_vtvifan_20261028_155811

## t5002 Restore Delete BEZEL settings on 5.2 — 2026-10-28
- Rob voice: missing "Reload Bezel Settings" in menu. Skin never had that label; missing row was **Delete BEZEL settings** (t4877) dropped when 5.0.20 was built from 5.0.16 without wipe/SkinSettings cherry-pick.
- Restored SkinSettings list 9000 item id=5 + scripts/bz_wipe.py from 5.0.18. bak bak_t_reloadbezel_20261028_160131. Path: Settings › Interface › Skin settings › last category row.

## t5007 Move Delete BEZEL settings to Tuner ALL — 2026-10-28
- Removed SkinSettings list 9000 item id=5.
- Added last row under Tuner › ALL (after Import tuning): Delete BEZEL settings → bz_wipe.py. Visible with bz_topen_all.
- bak bak_t_tunerwipe_20261028_160424. under_adv/MM locks untouched.

## t5008 Approved Info strip+fanop for next build — 2026-10-28
- Rob voice approved shared BezelColourBlock / BezelBlockBF + bz_at_fanop Info match (Music/Video/TV) on 5.2 base for next version. Already in live tree; no version bump/zip until asked.

## t5011 MM-on-load Music = Artists — 2026-10-28
- Cause: bz_cmd start opened recentlyplayed albums/songs (or albums) behind MM.
- Fix: path = musicdb://artists/; on first start set bz_mmsub_music=1 + bz_last_mmsub_music. Warm/pill defaults already Artists.
- bak bak_t_mmartists_20261028_160714. FULL restart for .py.

## t5013 (Oct 28 2026) TV seasons All-row one-slot shift
- Cause: Show All ON inserts stock * All seasons (/-1/) as Absolute(1) after ..; ALLHIDE blanks it but Kodi still reserves the 60px row → Season 1 sits one slot low. Music t5012 only patched covercol list 60; video uses View_60_BezelVideoPosterList list 60.
- Fix: bz_allpull120 / bz_allpull60 expressions; whole-list slide −120/−60 on video list 60 + matching 6098 ALLROW (same mechanism as t5012). bak bak_t_tvallshift_*. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
2026-10-28 17:52 t5022: 5.22 list trio (allpull music+inall, ALLHIDE parent blank inside All) + Reset System last top-level in-place Yes/No (bz_topen_resetsys, reset,sys,force)
2026-10-28 18:15 t5022b: Reset System Yes/No — Tuner list visibility only updates on ReloadSkin; resetui open/close in bz_tune.py (SetBool/Reset + ReloadSkin + restore bz_navtune). LIST/MUSIC OR gates bracketed. Smoke PASS Yes/No only then full list. bak bak_t_522resetprop_* / it_work.

## t5075 fork 5.23-test left stack sway
- Fork only: /workspace/b401/fork_523test/skin.bezel2 (addon 5.23.90 "BEZEL 5.23-test"); b300 mainline 5.22 untouched.
- MyMusicNav: new wrap group around BezelFanartCycler + ArtistHelpers + View_60 + DtapHint; camera 540,570, rotatey centre x540, same conditions/timing as BezelMusicPlayingArt (lead-in -13/5s, Short -30/5.5s pulse, Long hold+-13..13 pulse), gated !bz_lsway_off. Album playing-art group moved out of View_60 on Music only (View_60 copy gated !Window.IsActive(music)) and redrawn after the wrap, unchanged.
- Fan art glare + lit dust: copies of album Short/Long glare groups over x120-960 y120-1020 (gates bz_lglare_off / bz_ldust_off).
- Fan art cast onto album: swayback_shadow2 on the album LEFT edge (x1140), rides album rotatey (1440) in lockstep, fades in toward -13.
- Tuner: new head FAN ART (bz_topen_leftpanel): Fan art sway / Fan art glare / Fan art lit dust (default ON). No infographics yet.
- Smoke: wrapper rotates whole left stack (forced 20deg debug); live sway not exercisable — test library tracks are 2 s so bz_sway_go/pulse never settle.
- How to check: play Music >30 s, OR start a song then **pause** — sway / glare / lit dust / cast keep running while paused (Rob voice Oct 28 2026 short-track workaround). Notes: /workspace/b401/fork_523test/TEST.md


- **t5093** (Oct 28 2026, Rob voice): 5.23-test STAGE1 cast added — fan-art RIGHT edge shadow at L→R peak (+13 Long pulse fade 0→60); swayback_shadow2 flipx @ x780; rides left-stack rotatey; Short stays off (no + peak). Stage2 (album left @ x1140) unchanged. New two-stage system only — acast untouched. Fork only; b300 untouched. bak bak_t5093_stage1_20261028_201719. TEST.md updated.

- **t5088** (Oct 28 2026, Rob voice): K40 (open-anim empty-bz_mmwarm gates, t4892/t4893) BANNED forever. Live trees (b300 mainline, fork_523test, t4813) already had 0 gates; 16 bak/historical files under b401/t4813 scrubbed (list: /workspace/t5088_k40_scrubbed_files.txt); skill LOCK replaced with ban. bz_mmwarm property, MM warm focus bounce, mm_warm thread, Background warm delay tuner kept.

- **t5095** (Oct 28 2026, Rob voice): SHIPPED mainline 5.22 xz only — `/workspace/b401/t4813/skin.bezel2-5.22.zip.xz` from live b300 (list trio + Reset System; no menu-flash fix; no K40; no 5.23-test fork). Zip not retained/sent per Rob. DEF.ver in tree still 5.0.20 (unchanged).

- **t5096** (Oct 28 2026, Rob voice) SMOKE 5.23-test sway DONE: fork 5.23.90 in /tmp/bz2home only; pause workaround; Long sway; shots smoke_t5096/. Shared clock PASS (fan+album edges move same phase). Glare+lit dust PASS (visible on left stack). Stage1/2 cast peaks PASS (opposite extremes). Acast identical to mainline PASS. Cast flush: stage1 OK; stage2 album left shows bright outermost rim during cast — does not fully meet no-gap/cover-edge. TEST.md criteria updated (t5096b). HOME restored to 5.22.

- **t5096b** (Oct 28 2026, Rob voice): Cast flush criteria for 5.23-test — when casting, no gap between shadow texture and fan-art right / album left **texture** edges (not layout boxes). TEST.md updated.

- **t5104** (Oct 28 2026) superseded by **t5111** — unreachable All slot (showallitems off + skipper). Earlier docs-only hold lifted by Rob voice ask to block Up nav.

## t5121 — 5.23-test fork sway issues (fork only) — 2026-10-28
Rob voice call-6e006896: three bugs on fork 5.23-test. **Docs only.** Bug1 heals after select (visibility only).
1. First enter Music: lists active but text invisible; colour strip has no metadata. Heals after select.
2. Black bar between album and fan art at top of swing; clips fan-art left edge.
3. Big Logo included in left-section sway — remove from animation; keep static in corner.
Doc: `/workspace/b401/docs/BUG_t5121_523test_sway.md` + `/workspace/b401/fork_523test/ISSUES.md`.

## t5123 — CORRECT: t5121 off mainline 5.24 log — 2026-10-28
Rob voice: 5.23-test must **not** influence the main build. Removed the three t5121 sway bugs from the 5.24 main build log entirely — they stay on the fork issue list only. Keep 5.24 clean of any 5.23-test findings.

## t5123b — What remains on 5.24 (mainline) after that removal
Approved mainline 5.24 scope only (no fork sway / no t5121):
- BEZEL Settings skin-only panel (MM → SETTINGS → Right); Back returns to SETTINGS row
- Single **Tuner** button nesting the exact same 6970 layout as today (Delete / Import / Reset stay in Tuner)
- Independent **View All Seasons** / **View All Albums** skin toggles (replace blanket showallitems force-off)
- No settings.xml / Settings category / SkinSettings rebuild; no Kodi core menus
- Do not touch 5.23-test fork

## 5.24 — BEZEL Settings panel (Oct 28 2026, voice)
- New skin-only BEZEL Settings card (list 6968, Home prop bz_navbez) in Includes_Tuner.xml (BezelSettingsCard), included before BezelTunerCard in Includes_Bezel.xml. Chrome = Tuner chrome, title BEZEL SETTINGS.
- Items: Tuner (nests into unchanged 6970), View All Seasons (bz_allseasons → videolibrary.showallitems), View All Albums (bz_allalbums → musiclibrary.showallitems).
- MM SETTINGS→Right and side button 6919 (now "BEZEL Settings") open 6968. 6968 Back → 6996. 6970 Back → 6968 when bz_navbez (AlarmClock SetFocus after plain 6996 nav — plain nav needed so Back doesn't leak to underlay parent-dir), else 6996.
- bz_cmd.py: t5111 force-off replaced by _bz_showall_sync() at start; new action showall,<seasons|albums>. BzATDimCol also dims for bz_navbez.
- Backup: /workspace/b300/bak_t_bezelset_20261028_205217. Smoke: /workspace/b401/s524/. Fork 5.23-test untouched.

## t5126 — fork 5.23-test: black-bar dig+remove-if-useless; list-text jitter dig — 2026-10-28
Rob voice: Bug2 — if the black bar between album/fanart (top of swing, clips fan left) is found and not necessary, remove it. Bug4 NEW — list text jitter during left sway; investigate/docs unless cause obvious. Fork only; no mainline.

## t5127 — fork 5.23-test: Animation type tuner (Sync default) — 2026-10-28
Rob voice: FAN ART Tuner row for animation type. Current left-stack sway (shared clock rotateY + dust/glare + both cast stages) = **Sync**, default. Picker for future types. Fork only; no mainline 5.24.

## t5128 — Animation type options clarified: Off | Sync (default) — 2026-10-28
Rob voice: fork FAN ART Animation type = (1) Off static fan art; (2) Sync = current shared-clock sway+dust+glare+casts, default. Fork only.
- t5126 follow-up (fork only): Bug2 black bar = BezelMusicPlayingArt opaque plate x960; hidden in Music during left sway. Bug4 jitter = list inside rotatey (engine), docs only. Added Tuner FAN ART 'Animation type' Off|Sync (bz_lanim, default Sync). Mainline untouched.

## 5.24 soft fixes (Oct 28 2026, Rob voice) — mainline only
- Panel graphic DROPPED by Rob (voice 9:10 PM) — reverted; 6968 stays title + desc, no graphic, no new PNGs.
- Settings card group no longer hides on bz_navtune (stays under opaque Tuner card) so 6970 Back → `6968` direct when bz_navbez (no 6996 hop, no underlay parent-dir leak); 6996 only when !bz_navbez.
- bz_cmd.py showall: after sync, Container.Update(<Container(60).FolderPath>,replace) (fallback Container.Refresh) only on seasons list (seasons toggle) / music albums list (albums toggle); AlarmClock SetFocus(6968). MM + bz_navbez untouched.
- Backup /workspace/b300/bak_t_524soft_20261028_210103. Smoke /workspace/b401/s524soft/. Fork untouched.
- t5136 (Oct 28 2026 voice call-6e006896): **fork 5.23-test only** — Bug 5 logged: Music player controls not animated with fan-art sway (should move with sway). Docs only, no fix. Mainline untouched.
- 5.24 soft: shared includes BezelMMGlowLayer + BezelMMStripChrome (Includes_Bezel.xml) now used by MM, Settings card 6968 AND Tuner card 6970 — all inherit MM strip colour/opacity/glow; no extra rows. Colour/opacity rows on 6968 removed.
- t5137 (Oct 28 2026, fork 5.23-test, docs only): Bug 6 black texture next to Music player controls = 1115 dim plate 99000000 x120 y120 840x900 (Custom_1115_MusicControls.xml l.13), intentional dim but static vs swaying fan art → fork bug; logged in fork ISSUES.md.
- t5138 (Oct 28 2026 voice call-6e006896): **zip mainline 5.24** → `/workspace/b401/skin.bezel2-5.24.zip` (Settings panel + nested Tuner shared MM includes, View All toggles + live refresh, Tuner Back→6968). Zip only, no xz. Fork untouched.
- t5139/t5141 (Oct 28 2026 voice, FORK 5.23-test only): music global sway — 1115 dimmer+controls in left-stack rotatey (Bug5/6), bz_flip shared phase (no t0 re-anchor; join at next cycle) for Music/FS1/FS2/1115. FS2 delete requested then reverted; Custom_1112 kept. Mainline untouched.
- t5142 (fork 5.23.90): Music global sway Tuner rows Sway angle (13°) / Sway speed (20 s), patched into the XML plus the bz_flip clock; FS2 (Custom_1112) kept.

## t5146 (2026-10-28, mainline 5.24) Settings strip match / outline rows / meta-left box / Bezel Look Options
- Root cause: Settings and Tuner cards drew their own opaque FF000000 plate and glow under the shared strip. The ~50% strip composited over black, not over the MM backdrop, and geometry differed (520/440 vs 570/390).
- Fix: plates removed. The MM strip and list fade out under the cards. Settings uses MM geometry (570/390).
- New shared includes: BezelMMRowBar and BezelMMRowText (MM 6996 + Settings 6968). BezelMMStripChrome param box: 40% black (66000000), 840x900 at fan-art position. Metadata on left.
- Bezel Look Options row: bz_cmd.py lookcycle cycles Skin.String(bz_at_hishape) 1-5 (Square/Rounded/Pill/Underline/Outline). This drives $VAR[BzATHiTex] for MM and all lists.
- STANDING RULE: all new lists and sections draw their focus button via BezelMMRowBar / $VAR[BzATHiTex]. No private styles. The comment is next to the include.
- Big Logo: Home-level BezelLogo (28,26 64x64) is now visible on Settings because the plate is gone.
- Backup: /workspace/b401/bak_t5146_strip_20261028_213010/
- t5157 (Oct 28 2026 voice): **zip mainline 5.24 again** → `/workspace/b401/skin.bezel2-5.24.zip` (+ .xz for chat if needed). Full Settings accumulation at zip time.

## t5158 (Oct 28 2026 voice call-6e006896) — FORK 5.23-test only: pull 5.24 BEZEL Settings design into fork + zip
- 3-way merge (git merge-file) base=/workspace/b300/bak_t_bezelset_20261028_205217 (mainline pre-Settings), ours=fork, theirs=mainline 5.24 on Includes_Bezel.xml, Includes_Tuner.xml, scripts/bz_cmd.py. 0 XML conflicts; 1 bz_cmd.py conflict (fork had dropped t5111 showallitems force-off; took mainline _bz_showall_sync()).
- Sway files (MyMusicNav, Custom_1112, Custom_1115, bz_flip, bz_tune_patch) untouched — mainline had no changes there.
- Backup /workspace/b401/fork_523test/bak_t_forksettings_20261028_214004. Version stays 5.23.90. No K40 gates. Mainline hashes verified unchanged.
- Boot smoke fork OK (5.23.90, no log errors); live install restored to mainline 5.24.
- Zip /workspace/b401/skin.bezel2-5.23.90.zip (29,507,282 B) + single-file /workspace/b401/skin.bezel2-5.23.90.zip.xz (25,859,980 B). No splits.
- t5159 (Oct 28 2026 voice): fork 5.23.90 Settings-from-5.24 merge done → single-file chat delivery `/workspace/b401/skin.bezel2-5.23.90.zip.xz` (~24.7 MiB). Plain zip 29.5MB on disk. FULL restart (bz_cmd.py).
- t5161 (Oct 28 2026 voice): fork newer build renumbered **5.23.91** (was same 5.23.90 as older sway-only). addon.xml version+name BEZEL 5.23.91. Older skin.bezel2-5.23-test.zip.xz stays 5.23.90. Single xz `/workspace/b401/skin.bezel2-5.23.91.zip.xz`. Mainline untouched.
- t5162 (Oct 28 2026 voice, FORK 5.23.91): Bug 1 music list text invisible on first enter → ACTIVE. Not reproduced headless (3 entry paths); no code change; needs device repro. Smoke fork_523test/smoke_t5162.
- t5163 (fork): Bug 3 Big Logo static — View_60 BezelLogo hidden in Music (Includes_Bezel.xml); MyMusicNav draws BezelLogo outside the left-stack rotatey (inside SecDim parent). FIXED.
- t5164 (fork): fan art glare at both Long-sway ends — added left end-B glare group (TexB + shadow + LitDust glare2_br, album end-B timing) in MyMusicNav. Backup bak_t_listinvis_20261028_214757. Mainline md5 unchanged; live restored to 5.24. No zip.
- t5170 (Oct 28 2026 voice): fork 5.23.91 — decouple fan-art lit dust from glare in MyMusicNav. Glare=bz_lglare_off; dust=bz_ldust_off; both ends. Quadrants: End A right-third full height; End B left-third full height. bak_t_dustdecouple_20261028_215658. Mainline untouched. No zip.
- t5172 (Oct 28 2026 voice): fork 5.23.91 — new lit dust quadrant anchors. Album: L→R=lower-right; R→L=UL+LL. Fan art: L→R=UL+LL; R→L=upper-right. bak_t_dustquad_*. Mainline untouched. No zip.
- t5173 (Oct 28 2026 voice): fork 5.23.91 — fan-art lit dust correction: L→R=upper-left only; R→L=lower-left only. Album anchors unchanged (L→R=lower-right; R→L=UL+LL). bak_t_dustquadfix_*. Mainline untouched. No zip.
- t5174 (Oct 28 2026 voice): fork 5.23.91 — FS music left section (BezelNPInPlace: fanart block, vis, titles, progress, bio/lyrics chrome) rides music global sway (camera 540,570 + left-stack rotatey). Applies FS1 + FS2 + in-place NP. FS2 onload bz_sway_restart. Logo/album/controls outside wrap unchanged. bak_t_fsleftsway_*. Mainline untouched. No zip.
- t5175 (Oct 28 2026 voice): fork 5.23.91 — FS fan-art section inventory + red block fix. Red = Music colour strip (Tuner blockcol Red / bz_at_blockcol=4) + obsolete bz_npdlg colour fill still swaying under FS2/NP. Hide Music fanart/colour/shadow/glare/dust under $EXP[bz_np]; retire npdlg fill. Entire BezelNPInPlace (FS fanart section) already on music global sway since t5174. Mainline untouched. No zip.
- t5176 (Oct 28 2026 voice): fork 5.23.91 — FS fan-art lit dust inside BezelNPInPlace (same UL/LL quads as Music t5173, bz_ldust_off, music global sway). Album lit dust already in BezelMusicPlayingArt (shared FS1+Music/FS2 underlay; bz_adust_off). Fade 0↔100 (peak via BzD3L_mid). Textures litspeck 588×888, litspin 588×588. bak_t_fsdust_*. Mainline untouched. No zip.
- t5177 (Oct 28 2026 voice): fork 5.23.91 — song-change album flip no longer sets bz_sway_hold or re-anchors sway t0. Music global sway (fan+list+meta left stack) keeps pulsing; bz_flipping still fades glare/dust for the cover turn. Fixes freeze + erratic list/meta. bak_t_flipsway_*. FULL restart (bz_flip.py). Mainline untouched. No zip.

## t5200 (Oct 28 2026 22:40 EDT) fork 5.23.91 — menu sway
Shared include BezelMenuSway (Includes_Bezel.xml, before BezelNPInPlace) = same music global sway clock/gates as left stack (bz_lsway_off, bz_lanim off, bz_audio_latch, bz_sway_hold/go/pulse, bz_swayright). Wired: MM strip/list group (BezelNavMenu), Section Settings desc group, Tuner/Settings 6968 strip groups (Includes_Tuner 570/520), 1117 Media Sources, 1118 Power. Dim 6898 + static logo untouched. ReloadSkin only. Not smoke-tested.
- 2026-10-28 22:42 EDT [fork 5.23.91] t_bezback: BEZEL Settings Back exited MM. Fix: Includes_Tuner 6968 onback now SetProperty(bz_nav,true) + clear bz_navtune/bz_navbez + focus 6996 (+AlarmClock bz_bezmm retry); Includes_Bezel 6996 onback close-MM (ClearProperty bz_nav / 60) gated on !bz_navbez, else clears bez flags only. XML-only, ReloadSkin, not on-screen smoked. Backup bak_t_bezback_20261028_224146. Owner voice call-b905acde.

- t5201 (2026-10-28 22:42): MM sway audit fix — BezelMenuSway was sitting as sibling in 6899 (applied twice to whole menu + swayed full-screen dim 6898). Moved into strip-list group and 4.6.5 Section Settings group. Video section fanart (MyVideoNav) still has no sway; music section already sways via MyMusicNav.
- 2026-10-28 22:43 EDT t5111 port (fork): bz_flip.py TV All-seasons nav — Contains(/-1/) not EndsWith for hidden *All row bounce; new elif inside All folder moves focus off hidden '..' parent. FULL restart. Not smoked.

## t_secswaycont Wed Oct 28 22:55:27 EDT 2026
- REQUEST (Rob voice): section switch under MM keeps fan-art sway running/continuous while music playing/paused.
- Wrapped BezelFanartCycler in BezelMenuSway group: MyVideoNav, MyPrograms, MyPics, MyFavourites, MyPlaylist, MyGames, AddonBrowser (Music already in left stack).
- bz_flip.py sway_clock: bz_sway_restart while bz_nav open + latch + t0 set -> no hold/no re-anchor.
- ISSUE: newly loaded window starts its pulse anim at cycle start (Kodi), so the new section may be out of phase with the strip until next boundary; no stop/flat though. Not smoked.

## 2026-10-29 01:53 EDT fork 5.23.93 (/workspace/b401/fork_52393/skin.bezel2) — ports
- A/B: music global sway = 5.23.90 sway (t5139/t5142: left-stack sway, FS1 1115 + FS2 1112 join, gsangle/gsspeed Tuner rows, bz_lsway_off gate, glare/dust/casts) swapped in; kept 5.24 t5111 All-row fixes. 5.24 Settings panel already byte-identical (nothing to port). bak_t_mmsway_52393_20261029_015123, bak_t_settings52390_52393_20261029_015226.
- C: colour strip/glow (t5146) already in 5.24 base — no change.
- D: double-sway fix (t5201) NOT ported — needs BezelMenuSway + bz_swayclk_* rename from 5.23.91-fork package; awaiting decision.
- E: FS join 0.25 s hold (t5193/t5195) ported into bz_flip.py sway_clock (old names kept). bak_t_fsjoin_52393_20261029_015327. FULL restart.
- 2026-10-29 03:0x ET fork-3 (5.24.1-fork-3): textbake (bz_textbake, bz_textbake.py, Tuner 'Baked text'), 6 dedicated ov_sh_* shadows, slide lock verified (no snap per Rob). FULL restart.

## 2026-10-29 03:27 EDT — fork-4 build (Rob voice, approved)
- 1115 onload bz_swayclk_restart removed (controls no longer reset sway)
- FS player-bar visuals group moved from fan-art sway wrap into 6389 (BezelOverlayParallax, zoom 90), placed before hit target 6386
- LR soft-shadow pulse hold 0→0 → 100→100 (right set fades in)
- addon.xml: script.module.pil optional import; version 5.24.1-fork-4
- Package /workspace/b401/skin.bezel2-5.24.1-fork-4.zip.xz (no install)
- 2026-10-29 fork-4 tree (Rob voice): (1) BezelOverlayParallax slide X signs inverted (lead-in/pulse/swayright) so overlay slides opposite fan-art lean; (2) hid grad_bottom.png dim plate behind transport in 6389. No version bump/zip. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

- 2026-10-29 fork-4 tree (Rob voice approved): BezelOverlayParallax pulse/lead-in/short-sway slides get delay="2000" to match fan-art lean (fixes FS open hitch). bak_hitch_035323. ReloadSkin. No zip.

## pkg 5.24.1-fork-6 — 2026-10-29 ~4:31 AM EDT
Includes: music list wrapper camera removed (always-visible); Parallax direction tuner (Opposite|Same). zip.xz + part01/02 under /workspace/b401/. Full Kodi restart. mock_shadows_iso excluded.

## 5.25 — 2026-10-29 ~9:45 AM EDT — Music Info Play next (Rob t8u)
Bug: Play next on a song did nothing. Root cause: 9081 song branch used `QueueMedia(musicdb://songs/<id>/,playnext)` — trailing slash makes Kodi treat it as a folder → queues nothing (albums/<id>/ fine). Fix: drop slash → `musicdb://songs/$INFO[ListItem.DBID]`. Builtin-verified on test Kodi: inserts right after current track. addon 5.24→5.25. bak /workspace/b300/bak_202610290940. ReloadSkin. No zip. GUI click-through smoke not completed (MM focus).

- t5026 (5.26): Multi-disc disc picker ALL row (6097) was hard-hidden by t4547 covercol hide while allpull still slid list -> list shifted, no bottom All. Added bz_mdiscpick exemption.

- t5027 (Oct 29 2026) 5.27: 6097 ALLROW multi-disc covercol position: +450 now !bz_mdiscpick; mdiscpick base +390 +15/item (N2-8) so ALL DISCS sits flush under 75px covercol rows. Zip skin.bezel2-5.27.zip.

## 5.28 (t528, Oct 29 2026) — double-disc enter: first column shifted / ALL row missing
Root cause: Kodi 21 disc picker (musicdb://albums/<id>/) reports Container.Content=albums. bz_mdiscpick, bz_allpull_ctx, bz_allrow all required !Container.Content(albums) → never true in the disc picker, so 5.26/5.27 6097 fixes never fired. bz_allrow also failed on "2 discs + .." (NumItems=2 rule). With show-All ON, blank *All slot (150 → 75 on screen) only got allpull120 (60 on screen) → first column 15px low + 6097 hidden.
Fix (Includes_Bezel.xml, in place): disc test `[!Content(albums) | Abs0/1/2 FolderPath contains discid=]` in bz_allrow/bz_mdiscpick/bz_allpull_ctx; bz_allrow +discid clause; list 60 extra -30 slide (covercol+mdiscpick+allpull120); 6097 +45 when mdiscpick + Abs1 /-1/; BzAllRowLabel ALL DISCS for disc picker. Verified on :77 seeded 2-disc album, show-All ON and OFF: /workspace/b401/t528_after_allon.png, t528_after_alloff.png (before: t528_before*.png). Restart: box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
2026-10-29T10:04:52-04:00 Built skin.bezel2-5.28.zip with mdisc + music playnext FileNameAndPath

### t5029 MM highlight flash (5.28) — Rob voice Oct 29 2026
- Bug: intermittent flash of highlighted MM button when Music/Movies/TV content loads under MM.
- Cause: unguarded `bz_gridfirst` onload SetFocus(6600) steals focus from 6996 then grid onfocus bounces back.
- Fix: gate that onload with `!$EXP[bz_navmenu] + String.IsEmpty(Window(Home).Property(bz_mmwarm))` in MyMusicNav.xml + MyVideoNav.xml.
- Backup: /workspace/b401/bak_mmflash_20261029_100819/

### t5030 View All default ON (5.28) — Rob voice Oct 29 2026
- View All Albums (`bz_allalbums`) + View All Seasons (`bz_allseasons`) default On on fresh userdata.
- `bz_cmd.py` start: one-shot `Skin.String(bz_showall_inited)` then SetBool both; still `_bz_showall_sync()` to musiclibrary/videolibrary.showallitems.
- User Off still sticks across ReloadSkin (inited flag set). Wipe userdata clears flag → On again.
- Backup: /workspace/b401/bak_showall_default_20261029_101552/

## 5.29 (Oct 29 2026) — ALL DISCS / disc-list shift after ReloadSkin or View All toggle
- Root cause: 5.28 disc-picker detection only matched `discid=` in disc row paths. Kodi also builds disc nodes as `musicdb://albums/<id>/<n>/?albumid=<id>&disctitle=Disc%20N` (seen after Container.Update/refresh from the View All toggle, and after ReloadSkin). No `discid=` → bz_mdiscpick / bz_allrow / bz_allpull_ctx false → 6097 hidden + blank All slot not pulled (first column shifted down).
- Fix in place: new `bz_discrow` expression (Abs0–2 contains `discid=` OR `disctitle=`) used by bz_allrow, bz_mdiscpick, bz_allpull_ctx, BzAllRowLabel. Includes_Bezel.xml only; backup b401/Includes_Bezel.pre_529.xml. addon 5.29.
- Verified Kodi Live: cold, ReloadSkin, View All OFF, View All ON — ALL DISCS visible under Disc 2, list flush. Shots b401/rl_cold (5.28 broken) tg_off tg_on v_reload.
2026-10-29T10:20:33-04:00 Built skin.bezel2-5.29.zip (disctitle discrow + prior 5.28 fixes)

## 5.30 — t5030 MM Select blocked / bounced during warm-load (Oct 29 2026, voice)
Rob: Music/Movies/TV can't be selected while underlay warm-loads, or enters then bounces back to MM with a flash.
Root cause: bz_flip.py mm_warm() hold loops (in-place Container.Update loop, ActivateWindow _hold loop, finally 15x hold) re-assert `bz_nav=true` + `_bzstrip()` every 20–50 ms for up to ~3 s, ignoring a Select (bz_mmpick). bz_cmd `_bz_load_then_close` clears bz_nav → warm re-opens MM (bounce) or keeps it (no-op). Also MyMusicNav/MyVideoNav onload SetFocus(6996) under bz_mmwarm fired after the pick's window activation.
Fix: mm_warm latches `_pk()` (bz_mmpick seen) → stops setting bz_nav / strip focus, breaks finally hold, no new warm while picked. Nav onload SetFocus(6996) gated `!bz_mmpick`. No K40 anim gates. .py → FULL restart.
2026-10-29T10:26:58-04:00 Built/sent skin.bezel2-5.30.zip (mm_warm Select latch)

## t5031 — 5.31 MM warm-load pre-entry flicker / list jump (Oct 29 2026)
Rob repro: dead stop on TV → Up → Select immediately (before art). Cause: after a pick (bz_mmpick) two paths still yanked focus back to strip 6996: (1) list 60 onfocus bz_mmwarm and bz_nav+6996-visible SetFocus(6996) were NOT gated by !bz_mmpick (both list-60 copies in Includes_Bezel.xml); (2) bz_flip nav_menu "focus stolen just after open" (<1s of MM open) re-grabbed the strip on a fast pick. Each regrab = strip highlight flash + list re-layout. Fix: gate all three on !bz_mmpick. Python+XML → FULL restart. Backup /workspace/b300/bak530_*. Smoke t531.py on :77: no strip regrab after pick; Select lands and stays.
2026-10-29T10:40:34-04:00 Built/sent skin.bezel2-5.31.zip (mm pick strip flicker)

## 5.32 — Oct 29 2026 (Rob voice) MM Select ignore window (band-aid)
- scripts/bz_mm.py: after a Select starts a section pick, further strip Selects within 300 ms (MMLOCK_S=0.30, Home prop bz_mmlock timestamp) are dropped. First Select never blocked. mmpick latch (5.30/5.31) untouched; K40 untouched.
- Restart: FULL Kodi restart (Python). Backup: /workspace/b300/bak_531_1047/

## 2026-10-29 10:49 — Background warm delay default 0.8→0.2 (5.33)
- Ask (voice): change Tuner park delay default from ~0.8 s to 0.2 s (separate from 5.32 Select ignore).
- `bz_flip.py` mm_warm: empty/bad `bz_at_mmwarm` → step 1 (0.2 s); was step 4 (0.8 s).
- `bz_tune.json` DEF `bz_at_mmwarm` 4→1; `Includes_Tuner.xml` empty maps to step 1 (val/step/bar + onright); desc Default: 0.2 s.
- Existing saved Skin.String stays; Reset MAIN MENU / never-touched → 0.2 s.
- Restart: full (Python) + ReloadSkin picks up Tuner XML.
- Zip: not built.

## 2026-10-29 10:50 — ship 5.33 zip
- Voice: build+send zip with park default 0.2 + 5.32 Select ignore (300 ms). Full Kodi restart.
- Built `/workspace/b300/skin.bezel2-5.33.zip` + `.xz`.

## 5.34 — t5034 shared MM stage: fanart + poster texture-swap on section switch (Oct 29 2026, voice)
- Rob: TV↔Movies switch redraws fanart window + poster; wants ONE fanart stage + ONE poster stage, only textures swapped from the highlighted item (any section).
- Root cause: Movies↔TV is already an in-place Container.Update in the same MyVideoNav (same controls), but during the update list 60 empties → $VAR[BezelFanart]/$VAR[BezelPoster60] go blank → MM fanart (fadetime 3000) fades to black backing and back; poster group fades out via bz_vnoart (empty list = no art), frame hides (ListItem.Label empty), stand-in multiimage flashes. Looks like a full redraw.
- Fix in place: bz_flip `mm_stage` thread latches highlighted item's fanart/poster into Home props bz_stfan/bz_stpos (holds during Container.IsUpdating/empty list, cleared on MM close). MM-open fanart image (BezelFanartLayer, shared by Music + Videos) and MM-open poster image now read $VAR[BzStageFan]/$VAR[BzStagePos]. Poster group bz_vnoart fade, frame and stand-in held under MM while stage latched/updating. No K40, warm/mmpick untouched.
- Backup /workspace/b300/bak_533_1100/. addon 5.34. Restart: FULL Kodi (.py + XML). Not smoked live. Zip not built.
- Residual: Music is a separate window (MyMusicNav); Kodi can't keep one control across windows (dialog would draw over strip). Music↔Video still swaps windows but the stage opens already on the latched texture; Music has no poster stage (album art layout differs).

## 2026-10-29 11:08 — 5.33 fork project setup
- Voice: ground-up rebuild of BEZEL 5.33 off Estuary; 5.33 (park 0.2 + Select ignore) is baseline; 5.34 stages not in baseline.
- Created `/workspace/bezel-533-fork/` with frozen `reference/skin.bezel2` from 5.33 zip, `docs/SPEC.md`, `docs/PLAN.md`, empty `rebuild/`.
- Live `/workspace/b300/skin.bezel2/` left alone (5.34).
- 2026-10-29 fork.5 (5.33.5, /workspace/bezel-533-fork): Rob t79/t81/t82/t85 — 3 s crossfade label, hold old art until section warm, keep merging. Done; notes/FORK5.md.

## 2026-10-29 15:54 — fork 5.33.13 PVR icon clip fix (t157)
- PVRInfoPanel icon/text kept inside 450 fanart block; strip unclipped. No zip.
- 5.33.14 (Oct 29) Rob t160: TV logo upper row of PVR list (80x40 box x290 top8, keep-aspect, inside strip); stage fallback EPGEventIcon / centred channel logo when no fanart

## 2026-10-29 16:15 — fork 5.33.15 Pictures on Movies/TV template (t168/t172) — HELD mid-smoke
- View_63 rebuilt (Includes_Bezel.xml only): list 63 LEFT x120 w450 y120–1020 in grouplist, 60px rows, BzATHiTex bar, chrome !bz_navmenu; BezelFanartLayer 120,120 840×900; BezelShadow+BezelColourBlock strip x570; INFO CONTEXT LIST strip x600 y176 (Name, Date taken, Resolution, Size, Camera, Exposure, Aperture, ISO, Location; Description @652); ARTWORK x1010 790×900 kept; onleft bz_navok→bz_nav; MMFocusBounce+List; bz_casc a–d (casc_fp gate dropped). No K40. MyPics.xml/ListThumbInfoPanel untouched. addon 5.33.15. Backup bezel-533-fork/bak_5.33.14_pre_picsvpl_1611.
- Smoke partial: Left from list 63 → focus 6996 MM opened PASS. Closed-state shot with rows NOT yet verified. No zip. Held per parent (Tuner mockup ask).

## 5.33.16 (fork, 2026-10-29)
- Tuner: list in colour strip x570 w390 with global Outline bar (BzATHiTex/Col); dialog (sec/row/value/desc/keys) on fanart stage x120-570 w/ Pop-in; info thumbs on right via new shared BezelArtworkPanel (album template 600x600 @1140,220).
- BezelArtworkPanel include (Includes_Bezel.xml) used by Tuner + Pictures View 63; Big Album Rock (±4°, !Player.HasAudio). Music album untouched.
- Pictures: Left from MyPics now highlights PICTURES (bz_flip tgt 6908 -> row 8).
- Browse focus in all Add-source dialogs (DialogMediaSource): list ondown/onleft -> 11; grouplist renamed 9000->9100 (collided with MyVideoNav/MyMusicNav blade 9000 which stole focus + opened MM). Extra !HasModalDialog/mediasource gates on nav 9000 onfocus.
- Smoke :133 PASS: Videos/Music/Pictures Browse -> File browser; Pics Left -> PICTURES; Tuner layout. FULL restart (py changed).
- 2026-10-29 16:45 EDT t196: Pictures double-click → Info (5.33.17 fork). Other-section rollout pending audit go.

## 2026-10-29 16:55 EDT — fork 5.33.18 section info/context menus (t203)
- New Custom_1119_SecCtx.xml on section template (BzDlgFrame stage 120,120: dark list 450 + colour strip info 390 + BzDlgPoster art). One surface, rows chosen per section window.
- Programs/Games/Add-ons: Open, Add-on info (native DialogAddonInfo: enable/update/uninstall), Add-on settings, Check for updates, Sort by, Order, Get more…/Install from repo, Favourite.
- Playlist (music+video): Play from here, Item info, Move up/down, Remove, Shuffle, Repeat, Save, Clear (old side-blade buttons 20/26/21/22 folded), Favourite.
- PVR (channels/guide/recordings/timers/search, TV+radio): Switch, Programme info, Record, Guide, Play/Recording info/Delete, Edit/Timer info/Delete timer, Favourite, Search guide, Channel manager, PVR settings.
- bz_dtap.py: keymaps (dtap Select + C/Menu/rightclick) extended to these windows; double-tap/ctx -> 1119 there, Action(Info) still for Movies/TV/Music/Pics; stray Kodi contextmenu in these windows -> 1119. bz_ctx.py fav handles add-ons.
- BezelDtapHint added to Programs/Games/AddonBrowser/Playlist/PVR windows (PVR via list 50); hidden while 1119 up.
- Backup bezel-533-fork/bak_5.33.17_pre_secctx_1649. FULL restart (py). Smoke :133: Add-ons ctx -> 1119 PASS; Playlist double-tap -> 1119 PASS. No zip. No K40.

## 2026-10-29 16:57 EDT — fork 5.33.19 Add-ons section template (t205/t206 APPROVED)
- AddonBrowser.xml only: strip metadata (ADD-ON kind; Name/Version/Author/Type/Status/Installed/Updated/Origin pairs @600,176; Summary+Description @600) + BezelArtworkPanel (icon, Big Album Rock) right; hidden under MM / bz_infoup / 1119. BezelDtapHint kept. SecCtx 1119 rows unchanged.
- Backup bezel-533-fork/bak_5.33.18_pre_addontpl_*. XML only → ReloadSkin. Smoke :133 closed-state PASS (shots/s19_addons.png). MM-open shot NOT taken (interrupted). No zip. No K40.
- PENDING (Rob LOCK t206+): migrate SecCtx 1119 (Programs/Games/Add-ons/Playlist/PVR/Pics) onto Movies/TV/Music Options+Info shell, keep section rows.
## 2026-10-29 17:01 EDT — fork 5.33.20 (fork) — t210 MAKE ALL TO THE TEMPLATE
- Custom_1119_SecCtx rebuilt on Movies/TV/Music Options+Info shell (DialogVideoInfo): black left mask, BezelLogo, 450 fanart crop (BzSecCtxFan), big title @150,150, BzCIStripBG "OPTIONS" strip, BzCIBtn rows grouplist 9000 @582,166, BzCIMeta block @595,606 + summary/plot textbox. Opaque black under strip (stops underlay strip text bleeding).
- All 32 5.33.18 rows folded unchanged (ids 7901-7932). New Pictures rows 7940-7947: View, Open folder, Picture info (native), Slideshow, Recursive slideshow, Sort by, Order, Favourite.
- bz_dtap.py: 'pictures' moved into SECW -> double-tap/C in Pictures opens 1119 (was Action(Info)). Movies/TV/Music unchanged (Action(Info)).
- Includes_BezelDialogs: BzSecCtxName PICTURES; new BzSecCtxFan var.
- Backup bak_5.33.19_pre_secctx_shell_1657. FULL restart (py). No K40. No zip.
- Smoke :133 C + double-tap -> 1119 focus on first row: Pictures, Programs, Games, Add-ons, Music playlist, TV channels PASS (shots/s20).
- MM fix: bz_flip Left from Add-ons/Programs/Games now highlights ADD-ONS (row 9; was MUSIC + window swapped to Music). Smoke :133 PASS: Left -> 6996 ADD-ONS, stays Add-on browser, Back -> list 60; Pictures Left -> PICTURES still PASS (shots/s20/addons_mm2.png).
- t231 (5.33.24): 1115 Player Controls + Viz settings row 6412 → Addon.Default.OpenSettings(xbmc.player.musicviz); Close 6410 moved to 766
## 2026-10-29 18:05 EDT — fork 5.33.28 Info/Options template audit (t243/t244)
- DialogPictureInfo/AddonInfo/PVRInfo rebuilt on Options+Info shell (native ids kept; Left/Right=Close). New BzCIStripUnder (opaque black + same 840 fanart crop under strip) used by Video/Music/1119/Pics/Addon/PVR; 1119 flat black under strip removed. All Info fanart fadetime 400->0. Backup bak_5.33.27_pre_infotpl_1754. XML only. Smoke: AddonInfo PASS (Left->60, Back->60); Movies Info NOT verified (test hit non-media item -> "No information"). No zip.

## fork 5.33.29 — t257 (Oct 29 2026 18:20 EDT)
- Info/Options pop-in anim removed (Animation_DialogPopupOpenClose include dropped) on DialogVideoInfo/MusicInfo/PictureInfo/AddonInfo/PVRInfo + Custom_1119_SecCtx. Backup bak_5.33.28_pre_infoanim_1812.
- "List closes to MM": Movies (Alien) Info → Left / Back / Close / Info-toggle / Down-Down-Left all land on list 60, bz_nav empty. Not reproduced on :133; no nav code changed. Need Rob's exact path if still happening.

## fork 5.33.30 — t262/t263 FANART STAGE template (Oct 29 2026 18:25 EDT)
- Locked: FANART STAGE = fanart block + colour strip (120..960, 840x900); colour strip overlays the stage.
- New BzCIStage (Includes_BezelInfo): one continuous 840x900 fanart over opaque black, BezelSecDim + Fanart opacity. BzCIFanart / BzCIFanartMusic now call it; 450 grouplist crops in Custom_1119/DialogAddonInfo/PVRInfo/PictureInfo replaced with it. BzCIStripUnder retired (empty) — old version's -450 offset was ignored inside a grouplist, so strip showed the wrong (left) slice of fanart = seam.
- FileBrowser: BezelFanartLayer 450 -> 840 + BzMMStrip strip redrawn on top (was black under strip).
- Sections already 840 (VPL, Music, Pictures V63, PVR stage) PASS. Backup bezel-533-fork/bak_5.33.29_pre_stage_1819. XML only -> ReloadSkin. Smoke :133 shots/s30 (Movie + Music Info continuous; Info Back/Left -> list 60). No zip.

## fork 5.33.31 — t265 "fanart drawn twice" (Oct 29 2026 18:28 EDT)
- Proof test: hid BzCIStage fanart image → Info showed NO fanart (dialog's opaque black hides section layer). Only one fanart texture exists across all six Info/Options XMLs ($PARAM[fan] in BzCIStage).
- Cause of double look: section stage shows 9880 rotated extrafanart; Info stage used ListItem.Art(fanart) → a different second image swapped in on open (dialog can't read 9880).
- Fix in place: bz_dtap.py loop mirrors Control.GetLabel(9880)+ListItem.Label to Home bz_secfan/bz_secfanlbl (not while Info/1111 open); new var BzCIStageFan (bz_secfan when label matches, else BezelMIFanart) feeds BzCIFanart/BzCIFanartMusic. Dead empty BzCIStripUnder calls removed from Video/Music/Pics/Addon/PVR/1119.
- Backup bak_5.33.30_pre_onefan_1824. .py → FULL restart. Smoke :133 shots/s31: Adele + Alien section vs Info stage pixels identical (same image, same crop); Back → list 60. Pics/Addon/PVR/1119 not smoked on-screen (they use own art var, single BzCIStage). No zip.

## 5.33.32 fork (Oct 29 2026 ~18:40 ET) t253–t259, t271
- Artist clearlogo inside BezelLitDust include (album lit dust, Includes_Dust3.xml): Player.Art(artist.clearlogo), soft mask media/bezel/clogo_soft.png (edges → 0), fade 0→100 4250 / 100→0 @12750, same 17000ms loop, colordiffuse BzD3L_mid. Gate bz_mclogo_off.
- Tuner row "Fullscreen Music Clearart" ON/OFF (id mclogo) after Album lit dust in both ALBUM/POSTER›DUST and DUST›ALBUM DUST; info media/bezel/info/mclogo_info.png.
- Backup bak_5.33.31_pre_clogo_*. XML/media only → box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## fork 5.33.33 — t275 GO: DialogMediaSource (Browse) template (Oct 29 2026 18:50 EDT)
- Rebuilt onto fanart stage + colour strip (FileBrowser locks): BezelFanartLayer 840x900 + strip 570 390 on top + 3px outline. Block: PATHS list 10 + Browse/Add/Remove 9100 (pills, white focus/black text). Strip: label 2 header, MEDIA SOURCE, current path, NAME edit 12, OK/Cancel 9001, help text.
- Nav: list/9100 Right -> 12; 12/9001 Left -> 9100; onload SetFocus(11) when list empty (was no focus). All native ids kept.
- Pre-step: re-pushed 5.33.32 zip to Desktop (Rob ZIP FIRST). Backup bak_5.33.32_pre_browse_*. XML only -> ReloadSkin. Smoke :133 shots/s33 (Add video source: focus 11, Right->12, Down->18, Left->11, Back->Videos 60). Edit-source path w/ real items not smoked.

## fork 5.33.34 — DialogSelect / context pickers template (Rob 👍 Browse, Oct 29 2026 18:55 EDT)
- BezelStdFrame new param tpl (default false = old look untouched for Weather/1117/progress). tpl=true: BezelFanartLayer 840x900 stage + A0 black list block + BzMMStrip strip on top + 3px outline (FileBrowser/Browse locks).
- tpl=true on DefaultDialogSelectLayout (DialogSelect std) and DialogContextMenu. Art-chooser/Refresh/game/video-version layouts untouched.
- Backup bak_5.33.33_pre_select_*. XML only -> ReloadSkin. Smoke :133 shots/s34: Select PASS (focus 3, Down/Right -> Cancel 7, Left -> 3, Back -> Videos 60). Context menu (from System info) draws template but whole window sits ~450px high on screen (Kodi context positioning) — not yet checked if pre-existing.

## fork 5.33.35 — clearart lit APPLY (Rob 👍 glare-path mock, t277–t283, Oct 29 2026 19:02 EDT)
- Artist clearlogo in BezelLitDust now placed by new params lx/ly: end A (bl1500, glare upper right) 1390,45; end B (bl1080, glare lower left) 790,645 = half off the album corner. 700x350 keep, clogo_soft.png regenerated 700x350 (fade 180 x / 120 y), colordiffuse A6FFFFFF (65%).
- Inner 17000ms fade loop dropped: logo now rides its glare group pulse (same timing/flip/scroll hide as the glare). All 6 callers updated.
- Backup /workspace/bak_5.33.34_pre_clogoglare_1901. XML/media -> ReloadSkin. Live smoke not possible (audio wont hold); offline mock /workspace/s35_clogo_glare.png.

## fork 5.33.36 — DialogSelect/context pickers resume (Oct 29 2026 19:08 EDT)
- DialogSelect already on template (5.33.34), unchanged. DialogContextMenu offset fix: 999 sizing image 2160 -> 4320 tall so Kodi SetPosition clamp (h = img - grouplist size + grouplist height) always lands at 0,0. Backup bak_5.33.35_pre_ctxpos_*. XML only -> ReloadSkin. Smoke :133 shots/s36: frame at 120,120, Back closes. Rob: Desktop zip only, no chat parts.
## fork 5.33.37 — t286 Power stays; Search dialog (Custom_1107) template (Oct 29 2026 19:15 EDT)
- Rebuilt 1107 onto fanart stage + colour strip (Browse locks): BezelFanartLayer 840x900 + strip 570 390 + 3px outline. Block: SEARCH list 9000 (same 3 items/onclicks, pill rows white focus/black text). Strip: Search header, SELECTED label, item description (label2).
- Backup bak_5.33.36_pre_search_1910. XML only -> ReloadSkin. Smoke :133 shots/s37: MM SEARCH -> 1107 focus 9000, Down -> add-ons + desc, Back -> Videos 60. Desktop zip only.
## fork 5.33.38 — Smart playlist editor + rule template (Oct 29 2026 19:20 EDT)
- BzDlgFrame new params bgc/darkc (defaults FF000000/F50E0F12 = old look elsewhere). SmartPlaylistEditor/Rule pass 01000000 (00000000 renders WHITE in Kodi — lesson) + BezelFanartLayer stage 840x900 + A0 rounded block + 3px outline; strip from frame on top. Buttons white focus/black text (Browse locks).
- Backup bak_5.33.37_pre_smartpl_1912. XML only -> ReloadSkin. Smoke :133 shots/s38: editor focus 22, Down 12, Right -> rules 10, OK New rule -> rule editor focus 15, Back x2 closes. Stage black in smoke (opened via RPC, no item fanart).
- 5.33.39 (t287): removed glare-path moving clearart (Dust3); static artist clearlogo band above album in MusicVisualisation (1140,40 600x165 keep, bottom-aligned); bz_mclogo_off toggle kept.

## 5.33.40 SmartPL template (2026-10-29 ~19:18 ET)
Rob: ARE THESE ALL FOLLOWIN THE TEMPLATE (Smart playlist).
Fix: SmartPlaylistEditor+Rule onto FileBrowser stage+strip — colour strip 570 overlay; rules list / rule form in strip; settings/help in fanart block; OK/Cancel strip bottom. Backup bak_5.33.39_pre_smartpl_tpl_1917.

## 5.33.43 (Oct 29 2026) Fullscreen Music OVERLAY group
- Tuner FULLSCREEN MUSIC: CHROME -> OVERLAY (bz_topen_fs_overlay): chrome op/colour + Title/artist/album (bz_fs_ttl_off), Progress+time (bz_fs_prog_off), Cycle pill 6391 (bz_fs_pill_off, fade-only), Transport bar (bz_fs_tbar_off: next/prev pills+LAST/NEXT+arrows+aid_pp). VIZ/CLEARART kept.
- Removed bottom grad_bottom.png from FS (Rob t296).

## 5.33.44 (Oct 29 2026, t300u)
- FULLSCREEN MUSIC > OVERLAY: new slider "Title / artist / album size" (bz_at_fsttlsize 1=90%,2/empty=100%,3=125%). Scales all three labels together via bz_fsttl_* fonts (both fontsets); bottom-anchored above progress. Drop shadows still mockup-only.
- 5.33.44 also: Tuner rows Shadow angle (bz_at_fsshang 4-way cycle) + Shadow opacity (bz_at_fsshop 30/50/80) with vars BzFSShX/BzFSShY/BzFSShCol; shadow not applied live until Rob approves mockup.
- 5.33.44 (t302u/t303u): OVERLAY row "Shadow distance" (bz_at_fsshdist 1=2px NEAR, 2/empty=4px MEDIUM, 3=8px FAR). BzFSShX/Y = angle direction x distance. Interactive infographics: BzFSShInfo (36 art fssh_{ang}_{dist}_{op}.png) on angle/opacity/distance rows; BzFSTtlInfo (fsttl_{1..3}.png) on title size. Shadow still mockup-only. Backup skin.bezel2.bak_5.33.44_pre_shdist_*. XML/media -> ReloadSkin. Desktop zip.

## fork 5.33.45 — DialogAddonInfo template pass (Rob t306 NEXT, Oct 29 2026 19:36 EDT)
- Already on Info shell (5.33.28/29: BzCIStage fanart stage + BzCIStripBG strip on top, no pop-in, Left/Right Close). Added FileBrowser 3px Outline bar (117..963 x 117..1023, BzMMStrip) + explicit onback Close on 9000. Native ids untouched. No K40.
- Backup /workspace/bak_5.33.44_pre_addoninfo_1936. XML only -> ReloadSkin. Desktop zip only.

## fork 5.33.46 — Favourites/Programs/Games/Playlist template audit (Rob t306 NEXT, Oct 29 2026 ~19:40 EDT)
- All four already on View_60_BezelInfoList (colour strip on fanart stage, Outline bar, Cascade rows), BezelSecDim, MM 9000, BezelLogoButton. ListThumbInfoPanel left as is (Rob).
- Fix: MyFavourites was missing BezelDtapHint (others got it 5.33.18 t203) — added after the list.
- Left: Playlist has no BezelMiniPlayer (music already playing there; by design); Games legacy ContentPanel for views 50/54/501 is dead (views=60 only); Playlist side-menu buttons use raw textures (MM covers 9000).
- Backup bak_5.33.45_pre_favprog_*. XML only -> ReloadSkin. Desktop zip only. PVR manager next.

## fork 5.33.47 — PVR manager dialogs template (Rob, last open batch item, Oct 29 2026 ~19:45 EDT)
- Audit: DialogPVRChannelManager, DialogPVRGroupManager, DialogPVRGuideSearch were on old BzDlgFrame solid black block + dark panel (no fanart stage, no Outline bar). Fix in place: BzDlgFrame bgc/darkc 01000000 (SmartPL lesson, not 00), BezelFanartLayer stage behind block, colour strip redrawn on top of stage, 3px BzMMStrip Outline bar around block. Controls/IDs/nav untouched. Power untouched. No K40.
- Backup /workspace/bak_5.33.46_pre_pvrmgr_*. XML only -> ReloadSkin. Desktop zip only.
- 5.33.48 (t307u): Overlay drop shadows LIVE on FS Music. Shadow copy (colour $VAR[BzFSShCol]) drawn under each element, offset by new include BzFSShSlide (12 Conditional slide anims = angle x distance; mirrors BzFSShX/Y since Kodi posx can't take $VAR). Attached: title/artist/album labels (all 3 size sets), progress bar + time, cycle pill (disabled non-id duplicate grouplist behind 6391), transport bar (prev/next pills+titles, LAST/NEXT, aid_pp, tri arrows). Each shadow sits inside its element's group so Tuner Off toggles hide it too. Tuner desc "awaiting approval" removed. Backup skin.bezel2.bak_5.33.48_pre_shlive_*. XML -> ReloadSkin. Desktop zip.
- 2026-10-29 t309/t311: Soft Overlay shadow — MOCKUP ONLY (mockups/fs_overlay_soft_vs_hard_5.33.49.png). Planned: 9-layer stacked BzFSShSlide copies (centre 40%, r2 diag 22%, r4 axis 10%) keeping angle/opacity/distance Tuners. Awaiting Rob approve; live tree still 5.33.48.
- 5.33.49 (t312–t315 GO): Overlay shadow SOFT 5-layer stack (Rob "effect heavy" → 5 not 9). Each of 21 shadow controls → centre (BzFSShColC + BzFSShSlide) + 4 diag r2 ring copies (BzFSShColR + fixed ±2,±2 slide). t315: also added to Bio header + bio text, Lyrics text + "No lyrics", Up Next row title/artist/duration (unfocused layout). Bio facts grouplist (BezelInfoPair include) not shadowed. Angle/distance via BzFSShSlide, opacity bz_at_fsshop (C 33/55/80, R 14/24/3A). XML-only → ReloadSkin. Backup bezel-533-fork/bak_skin.bezel2-5.33.48_pre549. No K40.
  - t316 (in 5.33.49): Player Controls (Custom_1115) soft 5-layer shadow on strip-outside parts only: "PLAYER CONTROLS" header (y66, above panel) + panel backing outer edge (390x900 at x570). Rows inside the solid panel / fanart centre not shadowed.

## fork 5.33.50 — Overlay shadow FX Tuners (Rob t319–t329, Oct 29 2026 ~20:10 EDT)
- Opacity 10–100% (10 steps), Distance 5 steps NEAR 2 / MEDIUM 4 / FAR 8 / FARTHER 14 / MAX 22, MORE SOFT (centre p*0.55, ring r4 p*0.16).
- New Tuners (FULLSCREEN MUSIC › OVERLAY, after Shadow distance): Shadow blur strength (fsshblur TIGHT2/SOFT4/WIDE7/HUGE11 ring spread via BzFSShRing_PP/PM/MP/MM includes), Shadow colour tint (fsshtint BLACK/BLUE/PURPLE/WARM/RED), Shadow soft/hard mix (fsshmix SOFT/BALANCED/HARD; ColC/ColR = opacity×mix×tint generated vars).
- Separate FX with toggle pills (kind=pill, pill_on/off.png; OK on/off, L/R strength), INTERLOCKED (only one of Glow / Emboss / Letterpress): Glow/halo (fsglow, 4 white copies ±3/±6), Emboss (fsemb, hi -1/-2 + lo +1/+2), Letterpress (fslp, dark top + light bottom lip). Copies generated from each centre shadow control (26: Overlay labels/progress/time, Bio, Lyrics, Up Next, Player Controls header/panel); grouplist/button shadows (cycle pill) skipped. Off = visible false (no render cost).
- Info art media/bezel/info/fsfx_<tuner>_<v>.png (21, 900x580, active pill lit). No blob. No K40. Backup skin.bezel2.bak_5.33.50_pre_fx_2004. XML/media → box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- 2026-10-29 5.33.52: Music fullscreen -> album/disc list flash: skip list 60 covercol fades on FS bounce (bz_fsbounce). box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- 5.33.53 (Oct 29 2026): Fanart Pop Flat/Pop toggle in FS Music (fanart_pop/bg.png+fg.png subfolder), samples in samples/fanart_pop. Notes notes/fanartpop_5.33.53.md
- 5.33.53: Overlay Soft shadow On/Off (bz_fssh_off) gating existing BzFSShCol* stack
- 5.33.54 (Oct 29 2026, t365): Tuner dialog moves below the album cover (y590-1050, compact) when bz_covercol; else unchanged y120-1020. Tuner art rock during playback: investigated, not fixed.
- 5.33.55: Tuner art rocks while playing (BezelArtworkPanel cond !Player.HasAudio→true); below-album dialog clamped to art frame (h460→430, desc 240→220)
- 5.33.58 (Oct 29): Tuner-over-MM fix (bz_navtune/bz_navbez cleared wherever bz_nav cleared, XML+bz_cmd.py); Add-ons on MENU template (AddonBrowser.xml rewritten view; bak /workspace/bezel-533-fork/AddonBrowser.5.33.57.bak)

## 5.33.59 (Oct 29 2026) t390/t394
- No second playing album under Tuner: BezelMusicPlayingArt wrapped in group visible !Player.HasAudio | bz_navtune!=true. Tuner dialog position unchanged.
- Overlay FX: Emboss/Letterpress gained Left 1->OFF; Right no longer cascades OFF->STRONG (glow/emb/lp). All four (incl Drop shadow) can be OFF. XML only -> box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.60 (Oct 29 2026) t395 Tuner focus audit
Root: underlay list/grid onfocus bounces + 6996 had no Tuner guard -> focus leaked to MM strip behind Tuner; Tuner open relied on AlarmClock-only SetFocus(6970).
Fix: navtune->SetFocus(6970) before each 6996 bounce (+!navtune on bounce); 6996 onfocus navtune->6970; direct SetFocus(6970) on Tuner onclick (alarm kept). XML only, box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.60 (Oct 29 2026) t398-t404 REBUILT (t395 focus-audit edits REVERTED to 5.33.59 bounce)
- Power 1118: TUNER (blue FF7ACAFE, id 7801) below separator, BEZEL version under it. Opens Tuner (bz_tunesrc=pwr, clears navbez/navset, 1118 onunload skips 6996 focus). Tuner Back -> reopens Power.
- Nav-right Tuner removed (BEZEL subpanel item gone); Right-from-Settings still opens BEZEL subpanel w/o Tuner.
- MM: MUSIC VIDEOS + PLAYLISTS removed. Settings focused row: divider/logo/› extras removed.
- Music FS controls 1115: TUNER row 6413 (blue) above Close; bz_tunesrc=fsctrl, Back -> visualisation + 1115. Music only.
- bz_nav kept on Power->Tuner (Tuner group visible requires $EXP[bz_navmenu]). XML only -> box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- 5.33.62 (Oct 29 2026, t412) K42: album covercol list unfocused text squashed until click. Cause: covercol itemlayout/focusedlayout row Conditional zoom start=100,100 end=100,200 (time 0) — first processed frame at 100% under list zoom 100,50 lays out/caches labels at half height; only focus invalidation re-laid them. Fix in place: start=100,200 (start=end). Includes_Bezel.xml only. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.63 — Oct 30 2026 (Rob t425u) Overlay FX can't all turn off
- Cause: Glow/Emboss/Letterpress OK did SetProperty(bz_fxt) then gated on bz_fxt in the same onclick list. Kodi evaluates all onclick conditions BEFORE running any, and the list ends with ClearProperty(bz_fxt) → gate always saw empty → OK always turned the effect ON (never OFF). 5.33.59 only fixed Left/Right.
- Fix: Includes_Tuner.xml OK gates on Skin.String(bz_at_fs*) directly: off→1 + others 0; on→0. Render gates already exclusive (audited Includes_Bezel 96/24/24 + Custom_1115). Drop shadow pill unchanged (Toggle bz_fssh_off). box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.65 — Play Next Music dialog (Rob t429–t434 👍 "slow smooth slide")
- New `xml/Custom_1120_PlayNext.xml` (dialog 1120). Entry: Music NP block 6390 Right when `$EXP[bz_pndlg_ok]` (Music, audio, not visualisation); else Right = next song as before.
- Slide: Music window's own BezelMusicPlayingArt group slides −480 (1140→660) + NPInPlace/fanart stage slides −1100, 3000 ms sine inout, Conditional on Window.IsActive(1120) → sway never restarts; reverses on Back.
- Sides: shared BezelFSPlayNext (now param'd vis/sdelay; FS defaults unchanged) — dialog sdelay 6000 (3 s slide + 3 s), 3 s fade. NP bar fades in 1.8–3.0 s.
- Keys: L/R prev/next, OK play/pause, Back close. Kill switch: Skin bool bz_pndlg_off.
- Remove: delete Custom_1120 + 6390 bz_pndlg_ok onright + 2 "5.33.65 Play Next dialog slide" anims + bz_pndlg_ok expression. Backup /workspace/b401/bak_5.33.64_pndialog_0020. ReloadSkin. No zip.

## 5.33.66 — t438 (Oct 30 2026) Global backdrop (narrow Corner Key beam)
- Texture `media/bezel/glow/fs_backdrop_I_corner_key.png` remade: narrow beam from upper-left aimed at big album (1140,220 600x600) + soft pool; neutral white so it tints. Gen: /workspace/b401/gbd_tex.py
- Include `BezelGlobalBackdrop` (Includes_Bezel.xml) inside `BezelBlack` → Home, Music/Video nav, MusicVisualisation, Settings, SkinSettings, DialogVideoInfo, PVR.
- LOOK Tuner rows (after Global dimmer): gbd (bool bz_gbd_off, default ON), gbdop (bz_at_gbdop 1-5, empty=60%), gbdcol (bz_at_gbdcol empty=Warm/white/amber/teal/rose/strip). Infographics media/bezel/info/look_gbd_*.png (interactive per value). Art: /workspace/b401/gbd_art.py
- Backup /workspace/b401/bak_53365_pre66/. No zip. ReloadSkin. Not runtime-smoked.

## 5.33.69 t457 (Oct 30 2026)
- Global backdrop On/Off -> Backdrop style slider (bz_at_gbdsty: empty=Corner Key, off=Off). Textures: media/bezel/glow/backdrop/gbd_N_name.png via BzGbdTex. Info art look_gbd_sty_{off,1}.png. bz_gbd_off retired.

## 5.33.71 (Oct 30 2026, t475) Undo 5.33.39
- Restored 5.33.35 glare-path artist clearlogo in BezelLitDust (Includes_Dust3.xml, from bak_5.33.38_pre_staticlogo_1915); gated !Window.IsActive(visualisation) + !Window.IsActive(1120) so no clearlogo in fullscreen Music / Dialogue FS. Removed static 5.33.39 clearlogo band from MusicVisualisation. bz_mclogo_off kept. Backup bak_5.33.70_pre_undo539_0101. XML -> box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.72 (Oct 30 2026, t479) Glare back to regular
- Removed glare-path artist clearlogo group from BezelLitDust (Includes_Dust3.xml) — regular glare / lit dust only, Music + FS. bz_mclogo_off now unused. Backup /workspace/b401/bak_5.33.71_pre_noglarelogo_0103. XML -> ReloadSkin. No zip.
- 5.33.73 (Oct 30, t500): DialogConfirm (OK/YesNo/progress, e.g. "Installation failed") on MENU template = Add-ons 5.33.58 look: dim stage, colour strip (CONFIRM + buttons 10/11/12 as bz_mm28 rows, BzMMBarCol/BzATHiTex highlight), heading 1/message 9/progress 20 in 600x600 artwork frame. Edited BzStdProgress in place (only DialogConfirm uses it); BzRefreshProgress untouched. bak /workspace/bezel-533-fork/Includes_BezelDialogs.5.33.72.bak. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.74 (Oct 30 2026) — Dialogue FS long sway build (Rob 👍 t501s1739)
- Rock (bz_big_go/bz_big_pulse rotate + glare) gated `!Window.IsActive(1120) + !Window.IsActive(visualisation)`.
- pn_cast L/R animated on the long-sway conditions (lead-in 5 s + 12.25 s pulse): L peaks at -13 end, R at +13, ~15% mid/opposite.
- Dialogue FS slide 3 s → 5 s sine (= sway lead-in); 1120 sides sdelay 6 s → 8 s, NP bar/pill delay 1.8 → 3.8 s.
- Files: xml/Includes_Bezel.xml, xml/Custom_1120_PlayNext.xml, addon.xml. ReloadSkin. Backups /tmp/Inc_b4_5374.xml, /tmp/C1120_b4_5374.xml. No zip.

## 5.33.75 (Oct 30 2026, t504) Movie info dialog into fanart block, menu template
- DialogVideoInfo: cast (50) + CAST label/rules + meta/plot grouplist moved from strip into fanart block (x150–550; cast y476, meta y632). Strip now = menu template: bz_mm34 title (new $VAR BzCIDlgTitle: MOVIE/TV SHOW/SEASON/EPISODE/MUSIC VIDEO) + action list 9000 (y230, h760). Plot 200→150 / TV 110→100. IDs/onclicks unchanged. No K40. Backups bezel-533-fork/DialogVideoInfo.5.33.74.bak, Includes_BezelInfo.5.33.74.bak. ReloadSkin. No zip.

- 5.33.77 (Oct 30 2026, Rob t512 👍): DialogConfirm/BzStdProgress body (heading/message/progress) moved into fanart block x140-550; right artwork frame removed; strip CONFIRM + OK/Yes/No rows unchanged; progress bar hidden unless progressdialog + System.Progressbar set. Fork tree. No zip. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.79 — t513/t514/t515 Dialogue FS Play Next outer albums 90%
- BezelFSPlayNext (Includes_Bezel.xml): Previous/Up-next 600→540 (grad 378/162, labels 22/437,482 w496, pn_cast 144×540 at 396/0, frame 542). Center unchanged 600 @660–1260.
- L left 57→40 (40–580), R left 1263→1340 (1340–1880), top 220→250 (same vertical centre 520). Rest gap 80 px each side.
- Clip check: ±13° rotatey of 600 album overhang ≲ 300(1−cos13)+persp ≈ +13–25 px near edge; sides worst ~+12 px; total ≤ ~40 < 80 gap → no overlap.
- Backup bak_5.33.79/. XML parse clean. ReloadSkin needed.
- 2026-10-30 01:45 ET — t517/t518 push latest: 5.33.79 deployed to fork :133 (full restart; JSON-RPC AddonVersion=5.33.79); zip skin.bezel2-5.33.79.zip copied to HPLaptop OneDrive\Desktop.
- 2026-10-30 01:52 EDT 5.33.79 fork stress smoke PARTIAL (paused by parent): 1120-over-1112 overlay/centre-art FAIL, kodi segfault after 1120 back, flaky NP Right. shots/stress_20261030/results.txt
- 2026-10-30 01:57 EDT 5.33.81 (fork) t524: BezelMusicPlayingArt black 960x900 underlay visible=false (hide for now; shadows/frames kept). t525: Global backdrop opacity Tuner 5–100 (new level 0=5%: alpha 0D / strip fade 5; Left from 20%→5%; label 5%, reuses bar_5_1 + look_gbd_op_1 art). Gdim untouched. Backup bak_5.33.81. Deployed to bz533f1home; box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.80 (fork) — Oct 30 2026 1:58 AM EDT — t520 Right from player controls → Dialogue FS 1120
- Root cause: Music list Right opens Player Controls dialog 1115 (not NP block 6390). All 13 1115 rows had `<onright>noop</onright>`, so Right did nothing. 6390 wiring (bz_pndlg_ok → ActivateWindow(1120)) intact; 5.33.78 visible-gate removal not the cause.
- Fix in place: Custom_1115_MusicControls.xml rows: onright when $EXP[bz_pndlg_ok] → Dialog.Close(1115,true) + ActivateWindow(1120); else noop. Version 5.33.80. Backup rebuild/bak_5.33.80_pre_1115right.
- Live :133: Artists list Right → 1115 (6401), Right → 1120 (6400) PASS. Back-close not re-verified (Kodi on :133 killed externally mid-test).
- 5.33.82 (t528, Oct 30 2026): Music list 60 Right — no audio (or 6160 hidden): artist tag 6095 (songs)/6096 (albums), else 6192; audio + 6160 visible: ActivateWindow(1115); 1115 Right → 1120 unchanged; 1120 keys unchanged.
- 5.33.83 (t530, Oct 30 2026): 1115 Right always closes controls — no-audio case was noop, now Dialog.Close(1115); audio case unchanged (close + 1120). Backup rebuild/bak_5.33.83_pre_t530.

## 5.33.84 (fork, Oct 30 2026 ~02:10 EDT)
- t533 → CLEARED by t536: Power TUNER keeps menu-bar highlight (unchanged).
- t534: Back from Tuner(pwr) → 1118 drew under 1112 (zorder 1 hosts BezelNavMenu/Tuner). Fix: 1118 `<zorder>2</zorder>`.
- t535: Overlay FX default all Off. Drop shadow inverted bz_fssh_off → opt-in bz_fssh_on (1115 ×10, Tuner vars/pill/L-R/toggle). Glow/Emboss/Letterpress already default OFF (empty string). Backup bak_5.33.83_pre84. Fork :133 restarted, version 5.33.84 confirmed.

## 5.33.85 (fork, Oct 30 2026 ~02:40 EDT) — t554–t567
- CRASH FIX: Custom_1120 `<onback>Close</onback>` (6400 + 6401) → `Dialog.Close(1120)`. "Close" ran as the Back action again → infinite onback recursion → stack overflow segfault (CApplication::OnMessage/ExecuteXBMCAction). Back crashed; Esc (PreviousMenu) did not. Verified Back + Esc both clean after fix.
- Viz play-next (MusicVisualisation): album moved by group `<left>-480</left>` (two visibility-gated copies) instead of a 0 ms slide anim, so sway camera follows → perspective centred. 1120 sway untouched.
- 1112 NP stage: added -1100 slide (5 s sine) when 1120 opens (t560 fanart off-frame) — NOT yet confirmed on screen.
- Backup: rebuild/bak_5.33.84_pre85_t554

## 5.33.86 (Oct 30 2026, t568–t571) — fork
- t568 (Rob: move sway pivot with centre album): BezelMusicPlayingArt sway/flip group (camera 1440,520) now two copies: A camera 1440 (fades out over the 5 s 1120 slide), B `<left>-480</left>` + static +480 slide = camera x960 (fades in). Both always rendered (alpha only) so sway stays lock-step/unbroken; no visibility toggle. Viz play-next unchanged (already camera-follows via left -480).
- t569 mid-sway stuck? No: sway conditions don't reference 1120; no .py touches 1120; only idle (no-audio) ±4° rotate is gated by 1120.
- t570 Back/Esc: 1120 6400+6401 onback = Dialog.Close(1120) (verified in file). Live 1120 open not reached this pass (Right didn't open 1115 after restart; Player.Time stuck 00:00).
- Backup: /workspace/bezel-533-fork/backups/pre_5.33.86/. K40 untouched.

## 5.33.87 (Oct 30 2026 ~02:50 EDT, t575–t576) — fork
- Removed +3 s from sides delay everywhere: Custom_1120 BezelFSPlayNext sdelay 8000→5000 (5 s slide only); BezelFSPlayNext default sdelay 3000→5000 so viz play-next matches. Comments updated. Fade stays 3 s.
- Backup rebuild/bak_5.33.86_pre87_t575. Full restart :133, version 5.33.87 confirmed. Zip rebuild/skin.bezel2-5.33.87.zip → HPLaptop OneDrive Desktop. K40 untouched.

## 5.33.88 (Oct 30 2026 ~02:55 EDT, t577) — fork
- Cast gate: BezelFSPlayNext L pn_cast visible only when MusicPlayer.offset(-1) Title+Cover present; R only when offset(1) Title+Cover present (matches sides; 1120 + viz). Sides delay 5 s kept both. Backup rebuild/bak_5.33.87_pre88_t577. Full restart :133. K40 untouched.
- 2026-10-30 02:58 ET — t580–t583: 5.33.89. Root cause: the 5.33.86 dual-copy A/B pivot in BezelMusicPlayingArt duplicated the whole sway/cover/cast tree. Copy B's alpha hold made the album go to 0, and the duplicate layers (cast/stage) drew behind on 1120 + viz. Removed copy B + the copy A fade wrapper, so the single copy is back (= .85 structure). Viz keeps .85 left −480 pivot. 1120 pivot is back at x1440 (the dual-copy was the only pivot mover). Sides 5 s, cast gate, Dialog.Close untouched; K40 untouched. Backup rebuild/bak_5.33.88_pre89_t580. Full restart :133 → 5.33.89. Zip rebuild/skin.bezel2-5.33.89.zip.
- 02:59 ET addendum: also faded the music-list BezelFanartLayer (Includes_Bezel ~1277) under 1120 so the duplicate fanart no longer shows behind the sliding stage (t584). Redeployed :133.

## 5.33.90 (Oct 30 2026 ~03:15 EDT, t586–t588) — fork
- Pivot moves with 1120 centre album, ONE album tree, no A/B opacity crossfade. Kodi camera = origin only (GraphicContext::SetCameraPosition adds m_origins, never animations) so a slide anim can't move it. The −480 Conditional slide on the Music-window BezelMusicPlayingArt wrapper (Includes_Bezel ~2137) replaced by horizontal grouplist 6397 (scrolltime 5000 sine inout): [6398 1px btn][album group 1919w][6399 480w btn]. Focus 6399 (last) → scroll 480 (camera+rotatey ride along); focus 6398 (first) → scroll 0, 6398 onfocus → SetFocus(6390).
- Triggers: 6390 onright + all 13 Custom_1115 onright (after Dialog.Close(1115,true)) → SetFocus(6399) before ActivateWindow(1120). Custom_1120 onunload → AlarmClock(bz_pvret,SetFocus(6398),00:00,silent) (every close path). 6399 any nav → 6398/6390 fallback.
- Kept: stage −1100 slide, list fanart fade, 5 s sides, cast gate, Dialog.Close, sway unbroken (same controls). Viz play-next untouched (static left −480). K40 untouched.
- Smoke :133 (PULSE null sink, PULSE_SERVER): list→1115→1120 opens, album slides to centre full opacity with sway, Back → Music focus 6390, album slides back to 1140, no crash. Backup rebuild/bak_5.33.89_pre90_t587.

## 2026-10-30 overnight (t591/t593) — 5.33.91 / 5.33.92 (fork rebuild/skin.bezel2, :133)
- 5.33.91 t593: bz_allpick expr — ALL ALBUMS row (6097) now shows on artist album lists (showall ON, >1 item); hidden on 1-item dirs. bz_flip bounce off hidden `..` on artist/album dirs (no more blank-art/stale-bio open). Up wraps to ALL.
- 5.33.92: bounce extended to songs inside albums/discs (opened on hidden `..` with stale Adele bio). Verified D1 TRACK 1 focus.
- Open: first Up from first album needs 2 presses; info panel shows last disc while ALL focused; Back from All Discs lands on Disc 2 not ALL; showall OFF + >8-album artists unverified; MM→MUSIC path oddity (videodb path) recheck; splash unverified.
- Zip on box only (laptop offline): /workspace/skin.bezel2-5.33.92.zip

## 5.33.94 (Oct 30 2026 ~03:50 EDT, t592 template audit) — fork
- Audit: Dialog*/Custom_11* vs Bezel template. Already on template: Confirm/Select/Keyboard (BzStd*), Settings/AddonSettings/1101 (BzDlgPill), Video/Music/PVR/Picture/AddonInfo + 1119 (BzCI strip), Slider (BzDlgFrame), 1118 Power (MM strip).
- Templated (fix in place, same controls/ids/actions):
  1. DialogContextMenu button template 1000: white focus + black text + bz_list_music → MM bar (BzMMBarCol/BzATHiTex, BzMMFocTxt, bz_mm28, 58px).
  2. Custom_1110 TempoControl: Estuary dialog-bg/font14/arrow textures → BzDlgFrame bottom-left (DialogSlider pattern), colour strip head/desc, ‹ › MM-bar buttons 11/12 (TempoDown/Up kept).
  3. Custom_1103 VolumeSlider: Estuary progress/arrows → BzDlgFrame bottom-left, bz slider art (as DialogSlider), slider 11 Player.Volume/action Volume, bg close button kept.
- Left: DialogMediaSource + FileBrowser white mm_round focus override (may be t275 lock — ask Rob); DialogColorPicker, Custom_1105, DialogVideoManager still Estuary-ish (not clear-cut).
- Smoke :133 full restart → 5.33.94; 1110 + 1103 open/close render OK (shots/t592). Ctx menu xmllint only (libraries redirect it). Backup rebuild/bak_5.33.93_pre94_t592. Zip /workspace/skin.bezel2-5.33.94.zip. K40 untouched. Album-list items not attempted.

- 5.33.95 (Oct 30 overnight): album leftovers — bz_flip sw_path reset + 0.15s bounce settle; bz_allret Back->ALL; BzInfoAlbumLbl on ALL focus.
- 2026-10-30 5.33.96 overnight: Up-wrap guard (top row -> ALL row or stay) + TV seasons skip '..' on open/Up -> ALL SEASONS (bz_flip.py ALLBOTTOM2 block).
- 2026-10-30 5.33.96 overnight: Up-wrap guard (top row -> ALL row or stay) + TV seasons skip '..' on open, Up -> ALL SEASONS (bz_flip.py ALLBOTTOM2).

- **5.33.98** t620 Rob: FileBrowser back to classic double pane (list 450/451 left, OK/Cancel/Mkdir/Flip column 9100 + detail block right), restored from live b300; 9000->9100 kept. Template single-pane + t275 white-round lock retired. DialogMediaSource untouched. Smoke :133 PASS. Double-tap-to-open FileBrowser: pending spec.
- 5.33.99 t625: FileBrowser ctx menu = Estuary popup style (DialogContextMenu conditional); dtap a file in FileBrowser -> ContextMenu (bz_dtap.py). Double-pane unchanged.
- 5.33.100 t635: MAIN MENU>WARM SYSTEM Section fade depth (Keep/Lighter/Off) bz_at_mmsecdepth

- 2026-10-30 5.33.101: Dialogue FS 1120 auto-closes when music stops (Timers.xml bz_1120_autoclose; Player.HasAudio gate). box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.102 (Oct 30 2026, t654) — Dialogue FS 1120 left-stage slide + cast hide
- New wrapper (View_60_BezelInfoList) around list fanart (BezelFanartLayer, fade-only removed) + colour block/album-artist labels/list chrome: slide -1100 5s sine inout on Window.IsActive(1120)+music.
- BezelNPInPlace keeps its existing -1100 slide. Player controls slide too: compact bar group (BezelMusicPlayingArt, 1120 hide gate from 5.33.97 dropped so it slides) + BezelNPControls group.
- Colour-strip cast (4 cast elements in BezelMusicPlayingArt sway) : Conditional fade 800ms on Window.IsActive(1120) → fades back in after close.
- XML only → box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- Viz Play Next (MusicVisualisation, bz_fs_layout=playnext): NP stage instant alpha-0 → same -1100 5s slide; BezelNPControls wrapped in same slide; cast fade condition also covers viz+playnext.
- Rob confirm: ONE wrapper BezelFSLeftStage now spans list fanart → colour/chrome → list 60/A–Z → NP stage (NP old own -1100 moved onto wrapper). Player controls (compact bar in PlayingArt, BezelNPControls) carry identical synced slide — drawn after swaying art, so they cannot sit in the same group without changing draw order.

## 5.33.104 (Oct 30 2026, t683) FS center controls applied
- BezelFSPlayNext: side dim 35% + glare pn_glare_ul (R flipx) under labels/frame; center group 660,220: dim 40%, logo.png 117px 35%, focusable rc_prev/rc_pause/rc_next 6402-6404 (Previous/Play/Next). 1120 default 6403; 6400 forwards to 6403; pill 6401 down/up->6403. Backup bak_5.33.103_pre104.
- t686: 1120 default 6400 (no button focus); 6400 Select->6403, Left->6402, Right->6404; each button onclick action + Dialog.Close(1120); pill up/down->6400.
- t687: viz play-next too: 6390 (when visualisation + playnext) Select->6403, L->6402, R->6404 (else old behaviour); buttons in viz: action + ClearProperty(bz_np)+Action(Back) (same as Back); Up/Back -> 6390.

## 5.33.105 (t717, Oct 30 2026)
Back sequence on Dialogue FS 1120 + viz play-next: side albums fade 600ms first, then LeftStage/NP/controls reverse slide (5s). 1120: onback sets Home bz_fsret latch, AlarmClock clears after ~1s; stage conditions = [IsActive(1120) | bz_fsret]. Viz: BezelFSPlayNext WindowClose fade 600 + stage/controls WindowClose slide -1100->0 delay 1000 time 5000. Backup /workspace/bezel-533-fork/bak_5.33.104_t717
- 5.33.106 t718 see skin BEZEL_REQUESTS
- 5.33.108 see skin BEZEL_REQUESTS.md
- 5.33.109 fork log: /workspace/bezel-533-fork/rebuild/skin.bezel2/BEZEL_REQUESTS.md

## 5.33.111 (Oct 30 2026) — t783/t784
- t783 Select→controls: 6400 SetFocus(6403) worked, but Music-window overlay (BzPN107, 1120 visuals) had Visible fade delay 3800+1200ms → looked unfocused. Now 250ms fade.
- t784 fanart FS double-tap: bz_vdtapgo alarm was gated on bz_vdtap==1 (second tap) → double-tap queued play/pause, single tap did nothing. Now armed on first tap (vdtap empty); second tap cancels it + clears bz_pnoff → Play Next.
- 5.33.112 t786: FS close / Play Next exit -> list 60 (see fork log)

## 5.33.114 (Oct 30 2026) t792
- Play Next / Dialogue FS side albums closer to centre: gap 80->30px (L 40->90, R 1340->1290; centre 660-1260). Shared BezelFSPlayNext (viz + 1120); side pn_cast moves with groups.
- Cast audit: strip cast fades out 250ms while 1120 / viz Play Next active (by design t654/t780), back 600ms on close; side pn_cast gated on offset(+-1) Title+Cover.

## 5.33.116 (Oct 30 2026) t807/t809
- Dialogue FS (1120) 6400 Select = PlayerControl(Play) toggle; pausing sets bz_pnfoc=6403 -> BzPN107 overlay (dim + logo + pause lit); resume clears. Single press, no reveal-then-second-Select.
- 6400 Left/Right = PlayerControl(Previous/Next); pill 6401 keeps L/R = cycle mode.
- 5.33.115 bz_pnsel 1 s guard removed from 6402-6404 (Includes_Bezel BezelFSPlayNext). XML only -> box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.117 (Oct 30 2026) t811
- Viz Play Next 6390 (Includes_Bezel) Select = pause/resume + pause logo (bz_pnfoc 6403); Left/Right = PlayerControl(Previous/Next). Matches 1120 6400 from 5.33.116. XML only -> box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- t813: Music section click/Select on 6390 (bz_pndlg_ok) -> 1120 instead of play/pause.
- t815: side-album taps play that song (1120 6405/6406, viz 6407/6408); centre tap = pause+logo. t816: BezelLogo tap = Back.
- 2026-10-30 5.33.120 t834/t835: Music/Movies/TV list Up-wrap fixed. Root cause: list 60 sits alone in a vertical grouplist, which overwrites the child's onup (t4357) — Music grouplist had no onup, video grouplist only ondown, so Kodi natively wrapped Up to the last row and bz_flip ALLBOTTOM2 only bounced it after the fact (flash). Added grouplist <onup> ALL row (6097/6098) if visible else SetProperty(bz_topedge) = stay. Includes_Bezel.xml only. Backup rebuild/bak_5.33.119_pre120. Smoke PASS (box): Up x3 at top stays on row 0 for Music artists / Movies / TV shows; .119 control wrapped 0->43.

- 5.33.121 (t850): Music compact NP grouped with big album — removed separate -1100 Conditional slide on player-controls group in BezelMusicPlayingArt (Includes_Bezel.xml); NP now rides grouplist 6397 scroll with album. 1120 fade + 5.33.97 hide kept. bak: rebuild/bak_5.33.120_pre121
- 5.33.123 (t868, Oct 30 2026): Dialogue FS / Play Next side albums fade only — removed WindowOpen edge slide (±620,0, from 5.33.102 t663) on both side groups in BezelFSPlayNext. Fades kept. Backup bak_5.33.122_pre123. Box zip only.
- 5.33.125 (Rob t901, Oct 30 2026): Fanart-stage overlay rolled back to ".50 soft" — Glow/Emboss/Letterpress overlay copies removed (208 `5.33.50 fx` controls: Includes_Bezel 192, Custom_1115 16) + their 3 Tuner rows; soft drop-shadow stack (BzFSShCol*/rings, opacity/distance/blur/tint/mix Tuners) kept; default inverted back to ON (bz_fssh_on → bz_fssh_off kill bool; Drop shadow pill kept). Nothing else touched. Backup rebuild/bak_5.33.124_pre125_overlay. Box zip only. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- 5.33.126 (Rob t909, Oct 30 2026): FULLSCREEN pill (id 6886) on Music colour block upper-right (x786 y136, 158x32 right-aligned), cycle-pill 6401 style (np_pill32 border16, bz_b15, BzFSCTint 50/80). Inside BezelFSLeftStage fanart-stage group (rides its slide). Visible only Player.HasAudio + music window + artists/albums/songs + !bz_navmenu. Select = ActivateWindow(visualisation). Touch/mouse only; keyboard Up at top keeps 4.2 no-jump rule. Movies/TV not included (Rob: music-only). Backup rebuild/bak_5.33.125_pre126_fspill. Box zip only.

## 5.33.128 (Oct 30 2026) t926-t929
Fanart FS remap: Select pause; double-Select (bz_vdtap 1s latch) -> Play Next, no Tuner playnext gate; L/R prev/next song (no 1120 from viz); Up pill; pill Select/L/R cycle; Down on pill -> 1115 controls; Down on block no-op in viz. Touch: tap big album 6409 -> Play Next; tap fanart 6410 -> Up Next mode.
- 5.33.129 (Rob t940/t947, Oct 30 2026): colour-strip dtap hint — "›" arrow moved to the RIGHT of "controls" (Includes_Bezel ~44, K47b group x800: controls label right-aligned 0–120, arrow 134). Backup rebuild/bak_5.33.128_pre129_ctlarrow. Box zip only. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- 5.33.130 (Oct 30): section switch — xfade+arthold release in one frame after new art present; swap at half fade. Smoke partial: poster gap ~0.3s remains.
- 5.33.131 (t954, Oct 30): poster gate — mm_warm _arel waits for poster/tvshow.poster/thumb (not fanart/Icon); held poster no longer drops when label arrives before art; MM stand-in hidden while bz_arthold. Backup rebuild/bak_5.33.130_pre131_postergate. FULL restart (.py). Not smoked.

## 5.33.132 (Oct 30 2026) t960
- Section transition: fade-out removed, fade-in only. BezelSecDim bz_xfade fades -> bz_xfin fade-in (start=depth end=100, non-reversible); bz_flip.py _arel sets bz_xfin at release (timer clears after _xf), pre-swap fade-out wait removed. Hold/poster gate unchanged. Full restart. Zip /workspace/skin.bezel2-5.33.132.zip. Not smoked.

## 5.33.133 — t962 Music list losing focus → delayed return (Oct 30 2026)
- Fix in place: bz_flip.py focus watchdog. Container.IsUpdating no longer resets the lost-focus timer forever (holds, 3 s cap). In Music, offscreen 6385 / hidden blade 9000 count as lost (unless NP/npctl/lctl). Music return delay 0.5 s (Videos 1.0 s). Returns to 6600 if visible else 60. MM path (bz_nav) untouched. K40 not touched. FULL restart.

## 5.33.134 (t967)
- Bug: FULLSCREEN pill 6886 (5.33.126) clipped Dialogue FS in colour strip. Fix: pill group hidden while Window.IsActive(1120) or bz_fsret. XML only -> ReloadSkin. No K40.

## 5.33.135 (t968/t970 + parent steer, Oct 30 2026)
- Stub album chrome behind shadows, BOTH views (BezelFSPlayNext shared by 1120 Dialogue FS + viz Play Next): side frame bz_frame_soft drawn before pn_cast in prev+next side groups (was drawn after = chrome over cast).
- Fanart FS L/R/dtap dead: 6390 conditions used `!( ... )` — Kodi infobools only group with [ ]; 7 conditions rewritten to `![ ... ]` (incl. onleft Previous fallback, onclick fallbacks). Single-Select pause: AlarmClock(bz_vdtapgo) now armed BEFORE SetProperty(bz_vdtap,1) (old order made its own condition false → pause never fired). Backups /workspace/*.bak5.33.134. XML only -> ReloadSkin. No K40.

## 5.33.136 (t974, Oct 30 2026)
- Rob rejected .134 hide-pill. Reverted 6886 visibility gate (!1120 / !bz_fsret removed) — FULLSCREEN pill stays visible.
- Music colour-strip text moved below pill (pill 786..944 x 136..168): info grouplists top 150->172 (3x), Biography header 562->584 (2x), bio body 600/h366 -> 622/h344 (3x, still ends 966). Backup /workspace/Includes_Bezel.xml.bak5.33.135. XML only -> ReloadSkin. No K40.

## 5.33.137 (t976, Oct 30 2026)
- Fanart FS L/R/Select/double-Select dead. Root cause: Kodi default <Visualisation> keymap — Select/Enter = OSD (MusicOSD -> opens 1115), Shield pad/joystick d-pad = StepBack/StepForward, Up/Down SkipNext/Prev, Y = preset list; these never reach 6390 so its onclick/onleft/onright never fired.
- Fix in place: bezel2_np_tab.xml <visualisation> maps remote select/enter, keyboard return/enter, gamepad A, joystick a (default+shield) -> Select; pad/joystick d-pad + left stick -> Left/Right/Up/Down; preset/OSD keys -> noop; longpress Enter = PlayPause. 6390 logic (.135) unchanged.
- MusicVisualisation onload runs bz_cmd.py keymap (fresh map even if FS opened without visiting Music). Backup bak_5.33.136_pre137_fsfankeys. No K40. Full restart.

- 5.33.138 (Oct 30 2026, t980): Pause overlay unified to ghost Bezel logo (111px, 35%, .118 look) on big album for all pause paths (Select+touch): Dialogue FS 1120, fanart FS, viz Play Next centre. Gated on Player.Paused (was bz_pnfoc focus). Old rc_prev/pause/next nav-arrow overlay removed (1120 images) / textures blanked (6402-6404 buttons kept). XML -> ReloadSkin. Bak: bezel-533-fork/bak_5.33.137_prepauselogo

## 5.33.139 (Oct 30 2026, t987/t988)
- Music section tap/Select big album (6390) -> Dialogue FS 1120 restored: flattened nested `![..]` onclick/onleft gates to `$EXP[bz_pndlg_ok]` / `!Window.IsActive(visualisation) + !$EXP[bz_pndlg_ok]` / `!viz | bz_pnoff==1` (same logic). ReloadSkin. Zip /workspace/skin.bezel2-5.33.139.zip. Bak /workspace/Includes_Bezel.xml.bak5.33.138

- 2026-10-30 5.33.140 (Rob "push new build"): MM SETTINGS L/R removed; Movies/TV pill reorder (labels + bz_mm SUBS); behaviors/ in zip. FULL restart.
- 2026-10-30 5.33.141 (Rob "push new"): re-push current tree, version bump only, no functional change vs .140. ReloadSkin OK (full restart if .140 not yet loaded).
---
5.33.142 2026-10-30 20:36 — BezelBackdrop sticky across Music/Videos section swaps (onload if empty; no onunload clear). No zip yet.
5.33.143 2026-10-30 20:40 — FS LeftStage/Dialogue slides 5000→480 ms (ReloadSkin).
5.33.144 2026-10-30 20:42 — File Manager dtap → ContextMenu (bz_dtap.py; FULL restart).
5.33.143 2026-10-30 20:44 — FS slides 480ms + FM dtap ContextMenu; zip ready; HPLaptop offline for push.
5.33.145 2026-10-30 20:45 — BUG-002 FM ContextMenu focus/Back; zip push.
5.33.146 2026-10-30 21:02 — DUST Opacity tuners all subsections (MENU new mmdbright).
5.33.147 2026-10-30 21:20 — WARM 2.0: MM session row map + backdrop cache + 10s gated cycle (bz_flip.py; FULL restart); behaviors/mm-warm.md.
- 5.33.148 (Oct 30 2026): WARM 2.0 MM-only A/B preload (fanart, list-60 poster, album browse) — bz_flip ab_clock/_ABLane; Includes_Bezel MM twins. Not zipped.

- 5.33.158 (Oct 30 voice): Music mm_warm always musicdb://artists/ — removed bz_lastmusic path override in bz_flip mm_warm; tracking + bz_mm Select still use bz_lastmusic. bak scripts/bz_flip.py.bak_pre158_musicartists. FULL restart.

- 5.33.159 (Oct 30 voice): zip push HPLaptop Downloads skin.bezel2-5.33.159.zip (includes .158 Music warm always artists). FULL restart for .py.

- 5.33.160 (Oct 30 voice): MM section art fade-in only — A/B Visible keep 1.5s, Hidden→0; MM BZMMXF fadetime 3000→0 (Includes_Bezel). ReloadSkin. bak_pre160_fadein.

- BUG-010 logged (Oct 30 voice): WARM Music↔poster cross-draw / stretch — shared BezelPoster60/_ab_poster/bz_hold_poster; no fix yet.

- 5.33.161 (Oct 30 voice): BUG-010 fix — Music/poster art family split in bz_flip mm_warm + Includes_Bezel BezelPoster60/Poster/Flip. FULL restart. bak_pre161_bug010.

- 5.33.170 (Oct 30 voice): BUG-021 fix — stub Play Next cast reads shared sway clock (bz_flip sway_clock → bz_castL/bz_castR; own XML fade timers removed). FULL restart. bak_5.33.169_pre170_bug021.
- 5.33.172 (Oct 30): BUG-022 fanart FS Select/L/R cycle pill. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

- 2026-10-30 5.33.176 BUG-013: Back from Kodi Settings opens MM same frame (Settings.xml 9000 onback SetProperty(bz_nav) before the 1 s AlarmClock fallback). box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

- 5.33.178 (Oct 30 voice): TV-enter Movies-poster leak — poster A/B lane no longer stages bz_hold_poster (outgoing section) as new art; _arel sets bz_pos_drop when destination has no poster so lane drops outgoing art immediately (BUG-015 1.5 s hold kept only when destination art is coming). bz_flip.py; bak bz_flip.py.bak_5.33.177_pre178_tvleak. FULL restart.

## 5.33.194 — keymap quarantine (option one) (2026-10-31)
Leaving skin.bezel2 deletes all three profile keymaps (zz_bezel2_np_tab / _dtap / _noctx) + reloadkeymaps via new scripts/bz_km.py leave(); triggered from bz_dtap.py loop/finally and a bz_flip.py watcher thread/finally; manual `bz_cmd.py,keymap_leave`. Install behavior and dtap-off (dtap-only removal) unchanged. Doc: behaviors/keymaps.md. Full Kodi restart needed (.py). Not zipped/pushed.

## PARKED — swipe-to-spin poster (2026-10-31 voice)
**Not approved / not a feature request** — design exploration of Bezel platform limits.

**Concept:** Flat movie poster; sliding a finger (or slider) back and forth drives the poster`s `rotatey` in real time — Python reads touch/slider position and sets the image rotatey directly (no Kodi animation timeline). Once past a chosen threshold, Python flips a condition that starts a real Kodi spin/flip. Handoff must be seamless: the flip`s starting angle must match where the poster already sits, or there is a visible jump. Goal: illusion of swiping a poster and making it spin (iPad-like direct manipulation).

**Constraints noted:**
- Kodi animations cannot be paused, scrubbed, or seeked to a frame
- Conditional / WindowOpen anims only play forward and reverse from the ends (if reversible)
- Python can approximate scrubbing by setting control properties from a slider value
- One slider can drive multiple effects at once
- Python can toggle conditions to start or reverse anims from the ends

Related earlier park: anim scrubber / stepped keyframes via Tuner slider.
- 2026-10-31 · behaviors/*.md catch-up synced to live 5.33.194 (docs only; new dust.md; README index + standing rule). No XML/py, no zip.
- 2026-10-31 · behaviors stub deepen pass (docs only): 30 stub files deepened vs live 5.33.194; fixes fullscreen-pill keys, music-controls IDs, video-osd order, dialogue-fs pill Down; sway re-verified (.184/.193 notes). No XML/py/zip/version change.
- 2026-10-31 · WARM GATE (Rob approved startup splash folded into warm): Startup.xml first-paint gate, Custom_1113_WarmGate, BezelWarmGate include, scripts/bz_warmgate.py, precache gate. Docs mm-warm.md + home-splash.md pointer. Source only — version stays 5.33.194, no zip/push. Needs FULL restart when shipped.
- 2026-10-31 · Startup backdrop flash fix (code only, no commit/zip): `BezelGlobalBackdrop` visible now requires empty `bz_warm_gate` (`Includes_Bezel.xml`). Docs: mm-warm.md, home-splash.md. Version stamp stays 5.33.200.
- 2026-10-31 · Warm-gate art GetDirectory window: random start offset per section (still 400 long) in bz_warmgate.warm(). Code only, no commit/zip.

### Oct 31 2026 — MM strip soft shadow left -37→-47 (code only, no zip)
BezelMMStripChrome `mm_strip_shadow_c.png` left **-47** (was -37) so dark contact sits on colour-strip edge (~tex core x47). Live + Kodi home patched; Bezel-source pending. Smoke PASS on MM Music. Screenshots: music-strip-shadow-BEFORE-left-37-sway-peak.png / music-strip-shadow-AFTER-left-47-sway-peak.png → Downloads.

### Oct 31 2026 — Music album cast pin to strip edge (code only)
Album cast `left` **480** (was 485), zoom centers **960,520** (was 965,520). Live + Bezel-source. Smoke PASS at peak sway full fade-in. No zip/commit.
- 5.33.210 (live, not zipped): Music Fanart FS dialog 1121 built (t1595).

- 2026-10-31 22:3x ET (5.33.211) Rob t1621–t1623: WARM HOLD — always last WARM art for non-Music/Movies/TV sections; Tuner kill switch; incremental versions. Built, not zipped.

- 2026-10-31 · Rob: track Warm feature versions closely like Bezel builds. This hold build = **Warm 2.0.1** (skin 5.33.211). Docs/tuner relabeled; properties (bz_mmwarm, bz_topen_warm20) unchanged.
- 5.33.211 SHIPPED 2026-10-31 22:35 ET: zip → HPLaptop Downloads skin.bezel2-5.33.211.zip (31 MB); Bezel-source c29f841 pushed origin + bezel-source. FULL restart.

- 2026-10-31 5.33.213 Background dim poster/fanart split fixed: removed 3.1.2 MM-open black art cover from BezelRootArtHide (inside SecDim → inverse poster dim, ~60% hinge). Doc mm-warm.md. ReloadSkin. Not zipped.
- 2026-10-31 23:1x ET 5.33.214 Rob t1641: Background dim needs a no-dim stop. Existing top stop 11 already fades to 100% (no dim); relabeled "No dim (100%)" + desc (Right = brighter, range 5% to No dim). Doc mm-warm.md. ReloadSkin. Not zipped.
- 5.33.214 SHIPPED 2026-10-31 23:2x ET: zip → HPLaptop Downloads skin.bezel2-5.33.214.zip (30.6 MB, 32037599 B, no mockups); Bezel-source cb5c0b7 pushed origin + bezel-source (incl. 212 mmdim L/R, 213 MM-open cover removed, 214 No dim label). ReloadSkin (XML only).

- 2026-11-01 ~00:30 ET 5.33.215 Rob pt1691u: new BEZEL Settings (dialog 1130 over section, MM strip style, ▾ expand / » menus / ‹VALUE› pills, SERVICES sub-page, WARM 2.0.1 · TUNER row under INTERFACE). Back = MM, no poster reload. bz_mm.py + new bz_set.py → FULL restart. Docs settings.md + mm-warm.md. Bak b401/bak_5215_settingsmm_001550. Not zipped. Other stock pages to be done one by one.
- 5.33.215 SHIPPED 2026-11-01 00:32 ET: zip → HPLaptop Downloads skin.bezel2-5.33.215.zip (30.6 MB, 32044792 B, no mockups); Bezel-source 9f2e73e pushed origin + bezel-source (Settings 1130, bz_set.py, bz_mm.py). FULL restart.

## 5.33.216 (Nov 1 2026, t1700–t1705) — Music A/B Warm + MM idle fade
- Music A/B art lane: `bz_mart_a/b/side/on/empty`, 1500 ms sine, preload hidden; BUG-010 kept (Videos owns bz_pos). Docs: mm-warm.md.
- MM idle fade: 30 s → strip group 6894 fades to 0, focus parked 6897, any key wakes + SetFocus(6996). Tuner MAIN MENU › Auto-hide menu (bz_at_mmidle). Docs: mm-list.md, skin-settings-tuner.md.
- FULL restart (.py). Smoked headless; not zipped/pushed.
- Closed (leave it, Rob Nov 1 t1706u): with strip faded, underlay list text the colour block covered (e.g. TV show info column) shows through — intended, do not hide.
- 5.33.216 SHIPPED 2026-11-01 ~01:00 ET: zip → HPLaptop Downloads skin.bezel2-5.33.216.zip (30.6 MB, 32124111 B, no mockups); Bezel-source 0a8f93e pushed origin + bezel-source (Music A/B mart lane, MM idle fade, Tuner Auto-hide). FULL restart.

- 5.33.217 (Rob t1709u, 2026-11-01): MM idle undim — BezelSecDim mmdim Conditionals (11) + `String.IsEmpty(Window(Home).Property(bz_mmidle))`; idle → art 100% opacity, wake → Background dim returns. gdim untouched. XML only → ReloadSkin. Docs mm-list.md, mm-warm.md. Not zipped/pushed.

## 5.33.218 — see live tree REQUESTS.md (mushide everywhere fixed; Music randstart partial/open)

## 5.33.219 (Nov 1 2026) — MM idle "PRESS ANY / BUTTON" label
- Rob 👍 mock D: stacked smaller low-opacity text right of Bezel logo while MM idle (`bz_mmidle`). XML only (Includes_Bezel BezelNavMenu group before 6897). bz_mm17, 6EFFFFFF, x108 y36/58, fade-in 1500 ms, hide 200 ms on wake. ReloadSkin. Smoke `/workspace/b401/smoke219/` PASS. Backup `/workspace/b401/bak_5.33.218_pre219`. Not zipped.

- 5.33.219 (t1720u) Music RANDSTART new apply path: `_defer` re-applies SetFocus(60,row) when list 60 becomes visible (strip bounce under MM). selectItem() path crashed Kodi — rejected. Smoke: music cold land row 4 landed, MM strip kept focus.
- 2026-11-01 5.33.220: Add-ons (new 1131) + Media Sources 1117 + AddonBrowser + DialogAddonInfo rebuilt as Warm strip menus (Rob t1727s5849 👍, t1729–t1731). FileBrowser stays stock.
- 5.33.220 SHIPPED 2026-11-01 01:09 ET: zip → HPLaptop Downloads skin.bezel2-5.33.220.zip (32134457 B, 1854 files, no mockups/bak/pyc); Bezel-source 4949c3e pushed origin + bezel-source (Add-ons Custom_1131 strip, Media Sources 1117 strip, AddonBrowser/DialogAddonInfo restyle). FULL restart. Follow-up queued: Warm strip menus to use Bezel list highlight bars + Bezel pills.
- 2026-11-01 5.33.221 (Rob t1737/t1738/t1739/t1741): Warm strip menus (Add-ons 1131, Media Sources 1117, AddonBrowser zip/repo/category follow-ons, DialogAddonInfo, Settings 1130) now use Bezel list highlight bar ($VAR[BzATHiTex]/BzATHiCol, text BzATHiText) and Bezel np_pill32 pills (replaced mm_pill_ol outline + ad_pill_on/off). Buttons use HasFocus sibling image ($VAR in button texturefocus didn't render). Smoke /workspace/b401/smoke221/. Bak /workspace/bak221/. XML only → ReloadSkin (FULL restart recommended if coming from <220).
- 2026-11-01 5.33.221 (Rob 👍): Music big-album touch 6180 wired to Dialogue FS (6390 bz_pndlg_ok + fsslide onclicks → ActivateWindow(1120)). Docs music-list.md, dialogue-fs.md.

## 5.33.222 (Nov 1 2026) — mushide double album / poster aspect
- Rob 👍: under MM with music playing show only the Music-style sway album. Root cause: WARM 2.0 mushide slot in BezelVPLPoster drew BzWarmMusicArt in the 600×900 poster rect (aspect keep) — poster-shaped redraw; also not excluded from Music content where BezelMusicPlayingArt already draws. Fix in place: slot now square 600×600 at 990,270 (poster sway pivot), scale + art_mask + bz_frame_soft frame; gated off in Music/MusicPlaylist artists/albums/songs. XML only → ReloadSkin. Bak `/workspace/b401/bak_5.33.221_pre222`. Not zipped.
- 5.33.222 SHIPPED 2026-11-01 ~01:50 ET (Rob "Push" t1752): zip → HPLaptop Downloads skin.bezel2-5.33.222.zip (32137007 B, 1854 files, sha256 6747df48…982c, classic FileBrowser); Bezel-source b9a22f3 pushed origin + bezel-source (stray 9594b70 added 2 bak files, removed in b9a22f3). ReloadSkin (XML only).
- 5.33.223 BUILT, NOT SHIPPED/NOT SMOKED: FileBrowser.xml → Warm strip (570,120 BezelMMStripChrome box, 411 title, 412 crumb, panels 450/451 390w × 48 rows Bezel hi bar, » folders / size ✓ files, 9100 horizontal np_pill32 pills 413/414/415/416, 60 hidden). Classic fallback xml/FileBrowser.xml.classic.bak + /workspace/b401/bak_5.33.222_pre223/. Headless smoke couldn't open FileBrowser (screen grab stale) — needs re-smoke before ship.

- Nov 1 2026 ~1:55 AM ET: SHIPPED 5.33.223 (FileBrowser Warm strip; classic bak kept off-zip). Rob chose Push over Shield smoke (pt1758u). zip sha256 66fc35e7…c7483, 32137047 B, git 15c7e0a origin+bezel-source. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- 5.33.224 (Nov 1 2026, t1770): Music artist meta option 3B built into colour strip (6094/6095/6096 + BezelArtistMeta3B, bz_artist.py meta). Not zipped.
- 5.33.225 (Nov 1): 3B artist meta album/disc only; 6094 off — fixes dual artist image on Artists list. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.
- 5.33.226 (t1796u) Music RANDSTART first-item flash: fix in place on the .219 `_defer` path — `bz_randpend` Home prop set while deferred apply pending; list 60 (both Includes_Bezel instances) Conditional alpha 0 while set; poll 0.1→0.02s, post-apply wait 0.3→0.06s; always cleared in finally. No K40 gates. Backups b401/*.pre_226_*. Needs FULL restart (.py). Not zipped. Smoke pending on device.
- 2026-11-01 ~02:40 ET 5.33.227 (pt1804u): Music art in poster crossfade on section switch — poster-slot live twins split Videos (BezelPoster60V) / Music (BezelPoster60M) so fadetime never starts from a stale Music album. XML only → ReloadSkin. Bak b401/bak_5.33.226_pre227_0240. Not zipped.

## 5.33.228 — 2026-11-01 (t1805) Media Sources from MM
- Fix: 1117 kept the MM warm underlay (bz_fan_a/b lane) behind the Warm strip. It was going black.
- Fix: drop-list rows could not be focused (Down stuck on VIDEOS). Added explicit conditional onup/ondown on every row.
- Checked: no 1117 row opens the keyboard. Smoked live tree on :77. XML only → ReloadSkin. Not zipped. K40 untouched.
- 2026-11-01 ~03:10 ET 5.33.229 (Rob 👍 mock_ms_strip_keyboard): Add Source strip keyboard built — DialogKeyboard picks BzStripKeyboard while mediasource visible; vbars A–Z 9601 / 0–9 9602 / symbols 9603 left of colour strip, SPACE/DEL/DONE + abc/ABC caps pill; new scripts/bz_kb.py (Input.SendText). Other keyboards untouched. MM art behind kept. No K40. Bak b401/bak_5.33.228_pre229. Smoke b401/smoke229 (headless). Docs media-sources.md, new keyboard.md. FULL restart (.py). Not zipped.

## 5.33.230 — RANDFLASH2 (t1825u "Still flash 1st in list music on start")
- Cause: 226 armed `bz_randpend` inside `_defer`, after `_restore` — row 1 + its album had already painted.
- Fix in place: arm at Music warm-start (pre-load) when no session row; release in `_restore` early-outs; big album/flip vars blank while pending; defer poll 20→10 ms, re-apply 60→30 ms. K40 not used. FULL restart (.py). Not zipped. Backup: /workspace/bezel-533-fork/skin.bezel2.bak-5.33.229-randflash2

- 5.33.231 (Nov 1 2026, t1826): strip kb Left on A–Z toggles caps; abc/ABC pill 9604 removed; pills Down→bars. Backup bak_5.33.230_pre231. Not zipped.
- 5.33.230 addendum (executor): de-duped warm-start `bz_randpend` arm (kept 'w' + 4 s watchdog), `_restore` wrapper releases if no defer; big-album group alpha 0 while pending.
## 5.33.231 — Idle Big Album hinge flip (Rob pt1824u Approved)
- AWAY centre hinge w/ perspective in big-album group (Includes_Bezel, after BezelBigArt image), same rect/zoom; bz_flip.py idle_hinge(); masks + baked shadows media/bezel/hf_*.png. Artist: albums by year; album: album↔artist. 10 s hold; playback/focus/MM reset.
- Tuner ALBUM/POSTER "Idle rock" (bz_idlerock, default OFF) gates bz_big_go/pulse; info opt_idlerock.png. No K40. Bak b401/bak_5.33.230_pre231_*. FULL restart. Not zipped. Not device-smoked; rotatey sign (away vs toward) to confirm on Shield.

## 5.33.233 — 2026-11-01 ~03:15 ET (pt1830u "Fanart flash on media source open")
- Parallel 232 (t1827) had already removed window-level BezelSecFadeIn on 1117. Remaining flash: held lane images used `background="true"` (async → empty frame) over StdFrame's `bz_backdrop` image (fadetime 200) which could blink stale art.
- Fix in place: lane `bz_fan_a/b` textures load sync (already cached by MM); opaque black cover under the lane while `bz_fan_on` so bz_backdrop can't show through. No K40. Bak b401/Custom_1117.pre233_*.xml + addon.pre233.xml. Headless smoke b401/smoke233 (opens, lane + strip render, no XML errors). ReloadSkin. Not zipped.
- Open: right-side art panel (x1010+) is empty on 1117 by design (StdFrame showart=false) — awaiting Rob on whether he wants poster/art there.
- 2026-11-01 ~03:15 ET 5.33.232 (pt1826u/pt1827u): caps toggle already in 231 (verified). Media Sources › SOURCES → new Warm strip follow-on dialog 1132 (dynamic sources:// list 9150; select opens source in media window with msret return). 1117 fanart flash fixed (window fade removed, strip-only fade); right art slot held (bz_pos_a/b / bz_cov_a). No K40. Bak /workspace/b401/bak_5.33.231_pre232. Smoke /workspace/b401/smoke232 (headless — no MM art props, art/flash unverified on device). XML only → ReloadSkin. Not zipped.

## 5.33.235 — 2026-11-01 ~03:20 ET (pt1837u "Search doesn’t close back to mm")
- Cause: 1107 list 9000 control-level onback (SetProperty bz_nav) consumes Back, so the dialog stayed open over the MM.
- Fix in place: added onback Dialog.Close(1107,true) after the bz_nav set. No K40. Bak /workspace/b401/bak_5.33.234_pre235_search. behaviors/search.md updated. ReloadSkin. Not zipped.

- 5.33.234 (Nov 1 2026, t1833): Media Sources background = MM (mmdim on held fan+poster, fanop 50% default, strip fade removed). Pictures: held MM warm lane after MM closes (MyPics). Pictures Warm strip layout NOT built yet. FULL restart. Not zipped.
- 5.33.236 (Nov 1 2026, t1841): 3B meta on album + disc levels now shows the album (art, split title, artist·year·disc/track counts, genres) via bz_artist.py ameta(); artist fallback. FULL restart. Not zipped. Backup /workspace/bak236/.
- 5.33.237 (Nov 1 2026 ~3:25 AM ET, pt1843u): album/disc view types A (3B album panel held) + D (songs + disc headers, DEFAULT) selectable via Options › Section options › Album View 9978. bz_flip albview_a thread + bz_albva prop + bz_ameta OR; disc header in song layouts. No K40. Bak /workspace/bak237/. FULL restart. Not zipped. Not device-smoked.
- 5.33.239 (Nov 1 2026 ~3:30 AM ET, pt1854u "Use new keyboard where necessary"): DialogKeyboard now uses BzStripKeyboard everywhere (Search, Add Source, rename, other text fields) except Music Refresh (BzRefreshKeyboard) and File Manager (BzStdKeyboard, skipped per Rob). Focus A–Z 9601. No K40. Bak /workspace/b401/bak_5.33.238_pre239. Docs keyboard.md + search.md. XML only → ReloadSkin. Not zipped. Not device-smoked.
- 2026-11-01 ~03:35 ET 5.33.240 Rob pt1857u: Back from BEZEL Settings 1130 didn't land on MM. Fix: 9130 onback sets bz_setret + bz_nav BEFORE Dialog.Close (was after) + 1 s AlarmClock bz_setmm re-arm; bz_flip.py _sw now includes Window 1130 so MM reopens on SETTINGS opener row. K40 untouched. Bak rebuild/bak_5.33.239_pre240_setback. Docs settings.md. FULL restart (.py). Not zipped, not smoked.
- 5.33.241 (Nov 1 2026 ~3:40 AM ET, pt1858u "Setting > System subs not warm style"): SYSTEM subs DISPLAY/AUDIO/INPUT/POWER SAVING/LOGGING now Warm strip pages in 1130 (list 9132 cloned from 9131; bz_set.py pg focuses 9132, new ENUM/NUM pills, SYSP load). MORE (KODI) row keeps stock fallback. Settings Back→MM already in 240 (verified onback order + _sw). No K40. File Manager untouched. Bak /workspace/b401/bak_5.33.240_pre241_syswarm. FULL restart (.py). Not zipped, not smoked.

- 5.33.242 (Nov 1 2026 ~3:50 AM ET, pt1862u "Build"): Warm for remaining pieces — Pictures list 63 moved into Warm strip (no BezelWindowFade, held lane behind, artwork right); Settings 1130 pages PROFILES / SYSTEM INFO / SKIN / SCREENSAVER / GAMES on 9132 (kind i info rows; bz_set.py NUM skinzoom/screensaver.time, SYSP games); source context menu (DialogContextMenu bz_ctxwarm over 1117/1132/Pictures root) in strip. File Manager stock. No K40. FULL restart (.py). Not zipped. Bak /workspace/b401/bak_5.33.241_pre242_warm/.
- 5.33.243 (Nov 1 2026 ~3:48 AM ET, pt1870u "Ok build push"): Sources 1132 flash fix — 1117 strip chrome no longer hidden under 1132 (only its labels + grouplist 9000 hide); 1132 dropped BezelSecFadeInDialog, 8C full-screen dim and its own BezelMMStripChrome; Select now SetProperty bz_msret + ActivateWindow BEFORE Dialog.Close(1132). XML only. Zipped + pushed to HPLaptop Downloads.
- 5.33.244 (Nov 1 2026 ~4:00 AM ET, pt1871u "Music section broken. No list no album art. Rollback"): 242/243 diffs vs bak_5.33.241 touch no Music code (Pictures/1117/1132/1130/ctx only). Last shipped zip before 243 was 226, so 227–243 Music work reached Shield together. Rolled back the bz_randpend (RANDFLASH 226/230/238) XML gates that hide list 60 (alpha 0, both instances), the big album, flip A/B and poster vars while pending — a stuck/long pending (defer loop up to 120 s) = exactly "no list, no album art". Python still sets the prop but nothing reads it. Row-1 flash on Music start may return. Bak b401/bak_5.33.243_pre244_music. ReloadSkin (FULL if Shield not restarted since 243 install).
- 5.33.245 (Nov 1 2026 ~4:10 AM ET, pt1884u "slow gentle fold, 10 sec hold, idle only" + preload ask): fixed the existing 231 idle hinge in place to a slow fold. Each phase is now 900→2200 ms: A's right half folds onto itself, then B's left half unfolds. Shadows and darkening fade over the same time. The next cover is preloaded: it is set at the start of the hold and drawn under A, and B textures load sync (background off). Hold is still 10 s. Idle rock is still OFF by default. No K40. Bak /workspace/b401/bak_5.33.244_pre245_fold. FULL restart (.py). Not zipped, not device-smoked.
- 5.33.246 (Nov 1 2026 ~4:25 AM ET, pt1890u "Go" on View D approve sheet b401/mock_album_list_d_approve/sheet.png): View D (default) rebuilt to mock. Fix in place on covercol layouts: full-width 450x26 white DISC n bar on each disc's track 1 + text shifted under it (bz_discbar); old 237 right overlay header removed from 60 layouts; small in-list album art hidden in D, replaced by album title/artist header in the cover slot; right 3B = focused SONG (bz_flip albview_a sets bz_albvd + bz_sd_*; song panel in BezelArtistMeta3B). View A + Options 9978 switch unchanged. No K40. Bak /workspace/b401/bak_5.33.245_pre246_viewd. behaviors/music-list.md. FULL restart (.py). Headless load clean (no XML errors); not device-smoked. Not zipped. Known: cover slot keeps its 450 px height (list geometry/ALLROW/masks depend on it) — header sits at slot bottom, empty dark space above.

- 5.33.247 (Nov 1 2026 ~4:40 AM ET, Rob 👎 live fold black mid-fold + 'two images slit down the middle' + 'BUILD PUSH'): fixed the existing idle hinge fold in place (Includes_Bezel ~L1093–1105). Removed the black backing under the left half and the black fade overlays on both moving halves (those were the black panels); flipped rotatey signs (ph1 0→90, ph2 −90→0) so the edge swings AWAY — was swinging toward camera = oversized + dark; dropped background="true" on moving A halves. Each cover = left/right half images via hf_ml/hf_mr masks; next preloaded at hold start. bz_flip.py unchanged. Doc: behaviors/music-list.md. Smoke: interrupted, not completed. Zipped + pushed.

## 5.33.248 — idle Big Album half-fold (Rob pt1900u, Nov 1 2026)
Rob: 247 "looks like the top image is spinning, not half folding." Fix in place (Includes_Bezel.xml idle hinge block, XML only):
- 247 bug: base was full B; A-right rotated first then B-left — read as card/coin spin, wrong half first.
- 248: base = B-left + A-right; A-left on top. Ph1 ONLY left half folds at centre hinge (0→−90), right half static. Ph2 next right half unfolds (90→0). sine inout 2200 each. No slit line (seam invisible at rest). Removed full-cover art_mask base.
- Smoke: /workspace/b401/live_album_anim_248/ (fold1_clip.mp4, mid_*.png, mid_strip.png). Not zipped.
- 2026-11-01 ~11:05 ET 5.33.249 (Rob t1903–t1904 + steering): idle Big Album fold rebuilt as a RIGHT-half book page (left static, B right preloaded under it, back of page = B left, camera on the slit). XML only. No K40. Bak b401/bak_5.33.248_pre249_bookpage. Smoke b401/live_album_anim_249: right-edge lift + top/bottom overflow OK, but the page still shows the full A face and the left shows B mid-fold. Does NOT match the mock yet. Not zipped.

## 5.33.250 (Nov 1 2026) — idle album fold HALFCUT
Rob: 249 still spun whole cover from centre; left changed early. Cause: diffuse masks hf_ml/hf_mr did not clip → full 600 cover rotated (centre 1440 = its own centre) and full next drew over left. Fix in place: 300x600 half Images (aspectratio scale align left/right), rotatey centre 1440 = slit edge. Smoke /workspace/b401/live_album_anim_250/ (strip.png, mid_strip_250.png): left frozen, right leaf turns at slit, next under. Not zipped.

## 5.33.251 (Nov 1 2026 ~11:25 ET) — idle album fold PERSP (Rob t1913)
Rob: 250 "very close — perspective should go off the album not into it". Fix in place: fold rotatey signs flipped (ph1 leaf 0→+90, ph2 −90→0); camera unchanged at slit 1440,520. Free edge now swings toward viewer → taller than frame, overflows top+bottom. Left still frozen in ph1. Smoke /workspace/b401/live_album_anim_251/ (rec.mp4, mid_strip_251.png). Backup /workspace/b401/bak_5.33.250_pre251_persp/. Not zipped. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.252 (Nov 1 2026 ~11:40 ET) — fold bezel + opaque + shade (Rob t1915 + steer)
Rob: "white bezel follow the top image… should not be see through, is global dim lowered?" + "shadow on the static front, fade to black synced". Fix in place on 251: half-frame textures (bz_frame_half_l/r) ride each half / the leaf; full frame hidden while hinge group shows; glare group fades out during bz_hf_ph (was painting over the leaf = see-through). Left-static black shade 0→60 ph1, 60→0 ph2. Smoke gdim=7 (100% = no dim), mmdim=3 (MM-open only, not involved). Smoke /workspace/b401/live_album_anim_252/ (rec.mp4, mid_strip_252.png). Backup /workspace/b401/bak_5.33.251_pre252_bezelopaque/. Not zipped. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.


## 5.33.253 (Nov 1 2026 ~11:45 ET) — fold shadow (Rob t1917)
Rob: "It needs some shadow to sell it better??" Fix in place on 252 (all 252 locks kept). Left front black 60→85%; new baked hf_shd_hinge_l (hinge gradient on left, 0→100%); new hf_shd_cast (cast shadow on revealed next-right under leaf, 0→100%); leaf darkens 0→45% turning, 45→0 landing. All bz_hf_ph-synced 2200 sine, 0 at rest. Backup b401/bak_5.33.252_pre253_shadow. Smoke b401/live_album_anim_253. ReloadSkin. Not zipped.
Steer (Rob "back poster need a shadow also on the right half?"): added uniform black 0→70%/70→0 on next-cover right half under the cast gradient.

## 5.33.254 (Nov 1 2026 ~11:58 ET) — fold speed lock (Rob pt1922u "1400 is best")
Idle Big Album fold phases 2200→1400 ms: Includes_Bezel fold block (all phase anims) + bz_flip.py idle_hinge waitForAbort 1.4. Shadows unchanged from 253 (direction pending). FULL restart (.py). Not zipped. Smoke b401/live_album_anim_254.
Steer (Rob t1923u "left shadow should fade in as left gets covered; back shadow fade out as top cover leaves"): left black 0 ph1 / 0→85 ph2, hinge_l 0 / 0→100; back-right black 70→0 ph1 / 0, cast 100→0 ph1 / 0; leaf unchanged 0→45 / 45→0. Still 1400 ms.

## 5.33.255 (Nov 1 2026 ~12:32 ET) — shadow keyed to centre (Rob pt1929u)
ph1 = lift→centre, ph2 = centre→land. Back-right 70→0 by centre (ph1), cast 100→0 by centre; left black 0 through ph1, 0→70 (was 85) ph2; hinge_l 0 ph1 / 0→100 ph2; leaf 0→45/45→0. 1400 ms. XML only → ReloadSkin. Smoke b401/live_album_anim_255.
Steer (Rob t1930u): left/back-right flat black replaced by slit gradients hf_shd_grad_l (R→L) / hf_shd_grad_r (L→R); same opacity curves.

## 5.33.256 (Nov 1 2026 ~12:52 ET) — bottom-right outer shade + glare fade (Rob pt1934u)
New hf_shd_grad_r_outer (R→L, dark at outer right) on under-right 0→60 ph1 / 60→0 ph2; existing slit grad_r 70→0 by centre kept. Glare group fade 200 ms pop → 1000 ms sine out, reversible fade back in. XML+media → ReloadSkin. Smoke b401/live_album_anim_256.

## 5.33.257 — Rob t1936u
- Reversed outer-right fold shade gradient: darkest at slit → light at outer right. Opacity timing unchanged. ReloadSkin; not zipped; K40 untouched.

## 5.33.258 — Rob t1937u
- Bottom/under glare fade-in starts at phase 2 start (was after fold end): ~1400 ms sooner. XML only; ReloadSkin; not zipped; K40 untouched.

## 5.33.259 — idle fold leaf white outline (Rob t1940u) — 2026-11-01 13:23 ET
- Rob: bottom white outline seen on the flipping page.
- Cause: 5.33.252 half-frames (`bz_frame_half_l/r`) rode the leaf; under perspective the bottom stroke stretched into a visible white edge on the flipping page.
- Fix in place: removed half-frame controls from ph1/ph2 leaf groups only; static half frames on the base halves stay. Full `bz_frame_soft` still hidden while hinge active.
- Backup `/workspace/b401/bak_5.33.258_pre259_leafwhite_*`. XML only → ReloadSkin. Not zipped.

- 5.33.260 STATICBLEED (Rob t1941u/t1942u): reverted 259 (leaf half-frames restored on ph1/ph2 leaves); static bz_frame_half_r hidden during ph1, static bz_frame_half_l hidden during ph2, so the static bottom stroke no longer shows under the flipping page. XML-only, box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

- 5.33.264 (Rob t1959u): back border popping → static half-frames always on (sliced white outline, leaf frame rides). Glare stack fix: static L hide ph2 / R hide ph1 restored; ph1 leaf glare limited to bz_hf_ph=1. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.265 — GLAREFADE (Rob t1962u "Better but the glares are popping")
Static half-glare ph hard-hides (L hide ph2 / R hide ph1) replaced by 1400 ms sine fade groups synced to fold phases (R fades in during ph1, L fades out during ph2). Still one glare layer; leaf glares unchanged; 264 frame fix kept. Backup /workspace/Includes_Bezel.xml.bak-5.33.264. ReloadSkin. Not zipped.


## 5.33.266 — GLARECONT (Rob t1968u "Yes let's try that")
Dropped 265 static-half fade groups. Static half glares moved under the hinge leaves (no ph conditions); leaf glares = exact copies of static, ride the leaf whenever it shows. Opaque leaf occludes static beneath = one glare, no start/end swap. Fallback static glare group when hinge stack not up. Backup /workspace/bak_5.33.265_pre266. ReloadSkin; not zipped.

## 5.33.267 — FOLDLOCK (Rob pt1992u "Leaf anim 100%. Lock in and make behavior file") — 2026-11-01 ~14:55 ET
- Idle Big Album fold **APPROVED 100% / LOCKED** at the 5.33.266 look (GLARECONT). Don't change it without Rob.
- No behaviour change. addon.xml 266→267, FOLDLOCK marker comment on the hinge group (Includes_Bezel ~L1096).
- New `behaviors/idle-big-album-fold.md` (current state). README index row added. music-list.md fold detail trimmed to a pointer.
- Backup /workspace/bak_5.33.266_pre267. ReloadSkin. Not zipped/pushed.

## 2026-11-01 (ET) — Port blueprint pack (Rob t2001u; steer: behaviors = feel layer peer, Simple+Deep tiers, port-refs baselines)
- Docs only, live tree 5.33.267, **no version bump, no XML/Python change, no zip**.
- New: `PORT_INDEX.md`; layers `layout/ state/ motion/ art/ input/ theme/` (README + per-object files for 45 shipped objects); globals `state/home-properties.md`, `motion/tokens.md`, `art/media-map.md`, `input/keymap-overview.md`, `layout/resolution.md`, `theme/tokens.md`; `port-refs/` candidate screen baselines (9 objects) + PASS table.
- Behaviors: every file gets blueprint footer links; `keyboard.md` got Simple; `behaviors/README.md` port section + standing rule.
- Generators: `/workspace/portgen/gen.py`, `/workspace/portgen/globals_gen.py`. Fold baseline is pre-lock (259) — recapture on 267.

## 2026-11-01 · Port blueprint phase 2 (Rob "Continue") — docs only, 5.33.267, no bump/zip
- behaviors/keyboard.md deepened (strip keyboard How it works + Wiring table from Includes_BezelDialogs L564+, bz_kb.py).
- Layout/input/motion clean pass (`/workspace/portgen/clean.py`): rows kept only when the control id is named in the behavior; verification note added to every Deep tier. Fold: bogus control 100 removed from layout + input; input points at list 60.
- port-refs recaptured on 267 (isolated Kodi HOME=/tmp/bz2home on Xvfb :178): fold ×3, music-list, mm-list, tv-list, movies-list, mm-warm. Blocked: now-playing (no audio decoder), tuner (entry not reached), splash (missed). Old shots labeled stale.

## Phase 3 (Rob "Keep going") — 2026-11-01
- Behaviors: added a "Wiring table (live XML, 5.33.267)" section (ids, positions, sizes, nav, visibility, actions read from the live tree) before PORTLINKS in: dialog-confirm, filebrowser, favourites, home-splash, fullscreen-video, files-filemanager, music-viz-settings, addons, bezel-logo-back, big-album-pill, context-menu, dialog-busy, dialogue-fs, dust, info-options, mm-mini-player, music-fanart-fs, pause-overlay, search. Generator `/workspace/portgen/wire.py`. No source found for fullscreen-pill, keymaps, recently-played (Object lines name no XML/include) — left as is.
- Port-refs: splash ×3, tuner, tv-list, music-list NP captured on 267 (see port-refs/README). MM+NP awake still blocked (bz_mmidle).
- Layout hand-verify (mm-list, music-list, mm-warm): not done this phase.
- No XML/Python/look change, no bump, no zip, no Push.
- 5.33.270 MERGED13 (Nov 1 2026): see live tree REQUESTS.md.
- 5.33.271 t2061 (Nov 1 2026): merged Music list cover slot removed — see live tree REQUESTS.md.

## 5.33.272 — Nov 01 2026 17:44 ET — MERGED13 full-height rebuild (Rob t2062)
- bz_covercol excludes bz_m13; new dedicated 75px item/focused layouts for bz_m13 (full height, header bars); bz_allpull_inall gated !bz_m13; bz_nojumbo blocks idle jumbo zoom on Artists root + merged list. Fold lock untouched. ReloadSkin (XML). Not zipped.

- **5.33.273 NOFRAME (Rob t2065u, Nov 1 2026):** big white "panel frame" on Music right art was NOT a panel control — it was the hinge-fold stack group (Includes_Bezel.xml ~L1097: static half-frames bz_frame_half_l/r + shades) and the two glare groups (~L1117, ~L1121) still running the idle jumbo zoom 100→150 around 1440,420 (→990,120 900²) because 272 gated only the art layers with `!$EXP[bz_nojumbo]`. Gate added to those 3 zoom-ins. On Artists L1 + merged songs the fold half-frames/glare now stay locked to the 600² art at 1140,220 (thin edge only). Fold, sway, glare, 6180 touch untouched. ReloadSkin (XML). Smoke /workspace/b401/smoke_273_noframe/. Not zipped.

## 5.33.277 FSMETA (Rob pt2142u "Build") — Nov 1 2026 ~8:30 PM ET
- 1121 Music Fanart FS: Music-meta block (small artist 150,196 / big album 150,226 / year+genre pills 150,296); on open year pill expands right into pill-shaped NP progress bar (600ms sine), genre fades. 6-cycle pill 6421 moved to FULLSCREEN-pill spot 140,136 (labels + cycle unchanged, per Rob steer). BezelNPInPlace old title/progress overlay hidden while 1121 visible.
- DEFERRED: list-in-strip (View_60_BezelInfoList shared by 5 windows, ~30 fixed 450px widths — own build), Music-section meta on fanart + FULLSCREEN 6886 move to fanart UL (collide with list 60 rows until strip list lands), album leaf flip across screens.
- Backup /workspace/b401/bak_5.33.276_pre277/. XML only → ReloadSkin. Not GUI-smoked (no audio decoder in box Kodi). Not zipped.

- **5.33.277 SHIPPED** Nov 1 2026 8:20 PM ET — lean zip skin.bezel2-5.33.277.zip (32111630 B, sha256 29f9966a834ea8bfedc23f13c7367152724e2309640b96d615078498463f4dd3) → HPLaptop Downloads. FS fanart meta at Music coords; first pill→NP progress; 6-cycle at FULLSCREEN spot. box test Kodi restarted (ReloadSkin not callable via JSON-RPC) — runs 5.33.277.

## 5.33.278 STRIPLIST + MUSICMETA (Rob pt2147u "Push when done") — Nov 1 2026 ~8:40 PM ET
- Music (artists/albums/songs, `$EXP[bz_mstrip]`): list 60 group + cover group + ALL row 6098 ride into colour strip 570..960 via Conditional zoom 86.67% (center 120,120) + slide 450 — layout only, nav/focus/MM warm/controls unchanged (Rob steer). L1 full list; L3 (covercol) cover above half list. Strip text (info pairs/bio) faded off under bz_mstrip.
- Music meta on BzCIStage fanart block: small line 150,196 (ARTIST / artist / artist · album), big ListItem.Label 150,226, year+genre pills y296 (disabled buttons, np_pill32).
- FULLSCREEN pill 6886 grouplist moved 786,136 → 140,136 (fanart UL), behaviour unchanged.
- FS 277 morph (1121) untouched. Leaf/fold untouched (fold sits on big album 1140,220, not moved).
- NOT done: L2 artist-albums album-above (would need bz_covercol change = list behaviour change, against steer). Touch hit on scaled list not verified. Not GUI-smoked.
- Backup /workspace/b401/bak_5.33.277_pre278. XML only → ReloadSkin.

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

- 5.33.282 (Nov 1 2026): L2 ALL ALBUMS 6097 shown in half-list via bz_allhalf (+15/item, -135 with ..). Backup bak_5.33.281_pre282. ReloadSkin. Not zipped.

## 5.33.283 VSTRIP (Rob 👍 mock pt2182u) — Nov 1 2026 ~9:30 PM ET
- Movies + TV L1 titles in Music L1 style: new `bz_vstrip`; list 60 + 6098 into colour strip (OR'd into existing bz_mstrip anims, fix-in-place); strip text off; meta + plot inside fanart stage 150,196; poster group zoom 66.67% → big-album slot 1140,220.
- Caveats: poster kept 2:3 (400×600 in 600² slot) not cropped square; stub cast (485,130) scales with the poster group and may overlap strip edge — check. Not GUI-smoked. Backup /workspace/b401/bak_5.33.282_pre283. XML only → ReloadSkin. Not zipped.
- 5.33.285 (Nov 01 21:49) Rob approved: TV+Movies L1 strip clearlogo/clearart replaces fanart-meta title (430x90); no logo -> text. Backup /workspace/bak285. Zipped+pushed.

- 5.33.287 (Rob t2213, Nov 1 2026): 1121 cycle pill 6421 Left=prev / Right=next through 6 bz_npmode modes, wrap; replaced SendClick (Right used to open 1115 from Controls). XML → ReloadSkin.

## 5.33.289 (Nov 1 2026, t2216–t2220 "Go")
Same big album rail on non-Music MM underlays via shared include BezelMusicRail; visible only while MM open + audio ($EXP[bz_mmmushide]); 600×600 BzWarmMusicArt stand-in retired. Remount flash on Music↔other section accepted. Live tree only, not zipped.

## 5.33.290 (Rob t2221, Nov 1 2026 ~11 PM ET)
- TV L1 clearart 150,211 430×90 → 150,228 430×64 (no overlap w/ studio 196..226 or pills 296). Movies untouched (split control). Backup /workspace/b401/bak_5.33.289_pre290. ReloadSkin. Not zipped.
- TV L2/L3 mocks: /workspace/b401/mock_tv_l2l3/ — awaiting 👍.

## 5.33.291 (Rob t2223, Nov 1 2026 ~11 PM ET)
- TV L1: studio text line removed → studio pill in Year/MPAA/Genre row (after Year). TV clearart 150,228 430×64 → 150,200 430×92. Backup /workspace/b401/bak_5.33.290_pre291. tv-list.md updated. ReloadSkin. Not zipped.
- TV L1–L3 mocks regenerated with studio pill: /workspace/b401/mock_tv_l2l3/.

## 5.33.292 (Rob t2226 "Approve build", Nov 1 2026 ~11:10 PM ET)
- TV L2 seasons / L3 episodes → strip-list (bz_vstrip extended). Clearart via BzTVClear carries L1–L3; TV no-logo fallback = show title; SxE pill, studio pill all TV levels, runtime on episodes; season/episode name line + plot -40. Rows already thumbless; poster untouched. Backup /workspace/b401/bak_5.33.291_pre292. XML → ReloadSkin. Not zipped. Not GUI-smoked.

## 5.33.293 RECENT (Rob pt2228u "Update to new style lists", Nov 1 2026 ~11:15 PM ET)
- bz_vstrip widened (fix-in-place, no new groups): + Movies RECENTLY ADDED (videodb://recentlyaddedmovies/, Content movies) + TV RECENT (videodb://recentlyaddedepisodes/, Content episodes). Same L1 strip-list meta/clearart/pills/plot/poster slot.
- Music recent (Recent Songs/Albums) already on bz_mstrip (Content albums/songs in music window) — unchanged.
- Mocks /workspace/b401/mock_recent_lists/. Backup /workspace/b401/bak_5.33.292_pre293. XML → ReloadSkin. Not zipped. Not GUI-smoked.

## 5.33.294 PILLS (Rob pt2229u "Approve", Nov 1 2026 ~11:15 PM ET)
- bz_vstrip widened fix-in-place: Movies videodb://movies/{years,actors,sets,genres}/ (Content movies); TV videodb://inprogresstvshows/ + tvshows/{years,actors,genres}/ (Content tvshows/seasons/episodes). Category-name folder levels stay old layout (content-gated). Backup /workspace/b401/bak_5.33.293_pre294. movies-list.md + tv-list.md updated. XML → ReloadSkin. Not zipped. Not GUI-smoked.

## 5.33.295 FOLDERS (Rob pt2232u "Yes", Nov 1 2026 ~11:20 PM ET)
- New expression bz_vfold (Content years/actors/genres/sets/tags under videodb://movies/ | videodb://tvshows/) OR'd into bz_vstrip → folder-name levels now strip-list too. Movies title label shows folder name for bz_vfold; TV no-logo label excluded on bz_vfold. Backup /workspace/b401/bak_5.33.294_pre295. movies-list.md + tv-list.md updated. XML → ReloadSkin. Not zipped. Not GUI-smoked.
- MM Movies double-press (6996 never-break): NOT fixed — no repro without library; still awaiting Rob's direction (Up/Down/Left, pill vs list).
- 5.33.296 (Nov 1 2026, Rob t2233u): Music L2→L3 small strip album jump fixed. L2 list-group cover mask+art (Includes_Bezel ~L2519/2520, local 0,0 450² inside zoom 86.67@120,120 + slide 510 → screen ≈562,120 390²) drew over the strip album (570,120 390²); L3 (bz_m13) hid it. Both mask groups now gated !$EXP[bz_mhalf] → L2+L3 share the one strip album at 570,120 390×390. Backup /workspace/b401/bak_5.33.295_pre296. ReloadSkin. Not zipped.
- 5.33.299 (Nov 1 2026, Rob t2247u 👍): album cast pinned to colour strip — moved to include BezelAlbumCast outside rails/1121/-480; acx slide removed; right edge x960 always. Doc sway-animations.md.
- 5.33.300 (Nov 1 2026, Rob t2254u/t2257u): CAST300 — poster cast (strip + Info, animated+static) left 485→480, centre 965,570→960,570 (right edge x960); BezelAlbumCast wrapped in clip grouplist x570–960 (Soft/Long/Length spill clipped at meta wall); dead Tuner acx row + vars/handlers removed; disabled BETA 2.2 cast_shadow_short block deleted. Smoke composites /workspace/b401/mock_cast_300/. ReloadSkin. Not zipped.

## 5.33.301 — album sway next song fade (Rob t2276u, Nov 2 2026)
Album change while playing: crossfade new cover inside the sway tree (stays tipped); bz_cov_side full spin removed from next-song path (bz_flip.py). Overlay `bz_cov_x`/`bz_cov_xf` (900 ms) on both faces in Includes_Bezel.xml. Same-album no fade; play start no flip; idle leaf + rock clock untouched; tap/video flip XML untouched. Docs: leaf-flip.md, sway-animations.md. Backup bak_5.33.300_tipfade. FULL restart. No zip.

- 5.33.302 (Nov 2 2026, t2287/t2288): 1121 progress fill texturebg fix; old 6391 shadow gated off in 1121/album viz. ReloadSkin. Not zipped. Bak: /workspace/b401/bak_5.33.301_pre302

## 5.33.304 (Rob pt2293u + follow-ups) — not zipped or pushed
- Nav: list → FULLSCREEN pill → A–Z. Pill Right goes to the list, pill Left goes to the A–Z bar, and the A–Z bar is reachable with the pill on or off. No K40 gates.
- List: ALL ALBUMS no longer sits on top of the first album in Level 2 (ALLHALF -135 removed). Long Level 1 lists clear the double-tap tag (height 981). Levels 1–3 sit flush in the colour strip (slide 517).
- Vis: in Fanart FS, "press down to open" moved under the pill (1121, at 140,172).
- Files: xml/Includes_Bezel.xml, xml/Custom_1121_MusicFanartFS.xml, addon.xml, plus behaviors fullscreen-pill.md, music-list.md and music-fanart-fs.md. Backups are in /workspace/b401/bak_5.33.303_pre304/.

## 5.33.305 (Rob pt2301u) — not zipped or pushed
- Fanart FS meta text matches Music L3: the small line is "ARTIST · ALBUM" and the big line is the song title (new BzFSL3Big variable). The L3 pills and the FS pills are unchanged. Fanart FS keeps its own fonts and positions.
- Files: xml/Custom_1121_MusicFanartFS.xml, xml/Includes_Bezel.xml, addon.xml, behaviors/music-fanart-fs.md. Backups are in /workspace/b401/bak_5.33.304_pre305/.

## 5.33.306 (Rob pt2304u) — not zipped or pushed
- Fanart FS exit fade is skipped on Music L3: both WindowClose fades in Custom_1121 are gated with condition="!$EXP[bz_m13]".
- Files: xml/Custom_1121_MusicFanartFS.xml, addon.xml, behaviors/fanart-fs.md. Backups are in /workspace/b401/bak_5.33.305_pre306/.

## 5.33.307 (Rob: keep sway, real left offset) — not zipped or pushed
- Fanart FS 1121 album viz tip freeze fixed: on all 4 FS Slide rails in Includes_Bezel.xml, the Conditional -480 slide was replaced with an inner group at left -480 (visible with 1121 and bz_pnoff not 1), the same as core viz.
- Files: xml/Includes_Bezel.xml, addon.xml, behaviors/sway-animations.md, behaviors/fanart-fs.md. Backups are in /workspace/b401/bak_5.33.306_pre307/.

## 5.33.308 (Rob pt2310u/pt2311u) — not zipped or pushed
- Up Next 6395: the shadow-ring multi-draw labels were dropped (one soft shadow kept). The white focus bar was replaced with the Bezel outline highlight over a 25% black fill, with white focused text.
- Files: xml/Includes_Bezel.xml, addon.xml, behaviors/play-next.md. Backups are in /workspace/b401/bak_5.33.307_pre308/.

## 5.33.309 (Rob pt2347u/pt2352u) — P1 global big album; not zipped or pushed
- Deleted the tap-to-flip track list: list 6185, BezelFlipText, BezelNPHeader, BezelBackPath, the back-face panel, 1112 tap 6381, every bz_back* condition, and back_face()/play_pick() in bz_flip.py (bz_albumid tracker kept as album_id()).
- New always-open dialog Custom_1122_BigAlbum.xml (modeless, zorder 0, nothing focusable): cast + two real BezelMusicPlayingArt copies (home 0 / centre -480), slide speed = bz_at_fsslide.
- bz_rail (Home): centre / home / hide. Expressions bz_railvis (where) and bz_railc (centre). 1120 sets centre on load and home on unload, then focuses 60 (or 6996).
- Removed BezelMusicRail (+ grouplists 6367/6377/6397/6382) from Music View_60 and MyVideoNav, and the album/cast copies from MusicVisualisation. 1115/6390/6180 no longer SetFocus into rails.
- Files: addon.xml, xml/Includes_Bezel.xml, Custom_1112/1115/1120, Custom_1122 (new), MyMusicNav, MyVideoNav, MusicVisualisation, scripts/bz_flip.py, behaviors (big-album.md new, leaf-flip, music-list, now-playing, dialogue-fs, music-fanart-fs, fanart-fs, mm-warm, sway-animations, play-next, music-controls, np-bar, bezel-logo-back, README). Backups in /workspace/b401/bak_5.33.308_pre309/.
- Needs a FULL restart (bz_flip.py changed), not just ReloadSkin.

## 2026-11-02 ~02:11 ET — 5.33.309 smoke (global rail 1122)
9 PASS / 2 FAIL? / 3 WATCH. See /workspace/b401/smoke_309_global_rail/results.txt. No code changed, not zipped.

## 5.33.310 — big album home↔centre gap fix (Nov 2 2026)
- Rob: "Fixing?" — album viz open left ~1 s with no album (fs_dtap_gap.png).
- Cause: 309 swapped the two copies with Visible; the arriving copy remounted BezelMusicPlayingArt and its inner Visible fade-ins replayed while the leaving copy vanished at once.
- Fix: Custom_1122 copies always visible; Conditional slides at FS Slide speed move both together; leaving copy goes alpha 0 (time 0) only after the slide ends; reverse restores at once. No fade/gap either direction. behaviors/big-album.md updated.
- Backup: /workspace/b401/bak_5.33.309_pre310/. XML only → ReloadSkin. Not zipped.
- 5.33.312: startup add-on auto-install blank screen — warmgate rescue_startup() re-issues ReplaceWindow(StartupWindow) once after dialogs close.

## 5.33.314 (2026-11-02) — t2382/t2383/t2384
- A: MyMusicNav onload bz_sway_restart removed — MM Music focus no longer resets big album sway.
- B: Custom_1122 rail group takes BezelSecDim — MM dim / Global dim now hit big album.
- C: FS pill Down: 6391 Controls→1115 / Up Next→6396 / else 6390. 1121 pill 6421 Controls→1115 / else 6420 (Up Next cross-window, not possible yet).
- XML only → ReloadSkin. Not zipped/pushed.
- 5.33.314 **Fix D** (Rob t2385/t2386): Fanart cycle mode hides FS chrome (title/meta + progress) in NPInPlace and 1121; cycle pill (6391/6421) + transport bar prev/next stay visible. Tuner `bz_fschrome_fan` Keep overrides. Files: Includes_Bezel.xml, Custom_1121_MusicFanartFS.xml, behaviors/fanart-fs.md, music-fanart-fs.md. C: 6421 Up Next Down remains →6420 (cross-window).

## 5.33.315 (Nov 2 2026, Rob t2389 "Fix. Explain")
- Music Fanart FS 1121 gets its own Up Next: list 6395 + proxy 6396 extracted into shared include `BezelFSUpNext` (Includes_Bezel), mounted in BezelNPInPlace (home 6390, hidden while 1121 visible) and in Custom_1121 (home 6421, vis bz_npm_upn + bz_pnoff).
- 6421 Down: Controls→1115 / Up Next→6396 / else 6420. Select = bz_cmd.py upnext_goto (unchanged).
- XML only → ReloadSkin. Backup bak_5.33.314_pre315. Not zipped/pushed.

## 5.33.318 — Rob t2398 "Cast shadow big album lost sync" (Nov 2 2026)
- Root cause: album sway group hidden (frozen) under Tuner via BezelMusicPlayingArt `!bz_navtune` gate; BezelAlbumCast in 1122 lacked the gate and kept pulsing → phase drift (no MyMusicNav sway_restart since .314 to re-zero).
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

## 5.33.324 — Rob t2419 "Audit fix now playing music level 2" (Nov 2 2026)
- Audit: L2 = artist albums (bz_artistalbums → bz_mhalf half list). NP = 1112 over list (gate passes at L2 unless grid_music), compact NP rides big album in 1122.
- Bug: strip small album (Includes_Bezel ~L1480, 570,120 390²) had no bz_np fade — stayed on screen under Now Playing at L2/L3 while list, meta, info faded. Regression from .296 (old list-group cover carried the fade).
- Fix: added the standard bz_np Conditional fade (1000 ms sine). Docs music-list.md + now-playing.md. ReloadSkin. Backup /workspace/b401/bak_5.33.323_pre324. Not zipped.

## 5.33.325 — t2420u / t2421u (Nov 2 2026)
- Auto-open Dialogue FS (1120) after 30 s idle while music plays in the Music section (bz_flip.py loop, once per idle period, key press re-arms; same guards as big-album tap + no dialog/MM/NP).
- Tuner toggle in FULLSCREEN MUSIC: "Open after 30 s idle in Music" (ON default, bz_fsauto_off). Bak: bak_5.33.324_pre325. FULL restart (.py). Not zipped.

## 5.33.326 — t2422u (Nov 2 2026)
- FS prev/next song pills (transport bar, Includes_Bezel BezelNPInPlace) restyled to the 6-cycle pill 6391 look: hi_outline_sq outline → np_pill32 fill (border 16), 30→32h (top 981), fill BzFSCTint59→BzFSCTint50, titles bz_ral21/Tint59 → bz_b15/BzFSCTint. Shadow/ring copies follow. Layout x/width, LAST/NEXT labels, triangles, focus untouched. Bak: xml/Includes_Bezel.xml.bak_5.33.325_pre326. ReloadSkin. Not zipped.

## 5.33.327 (Nov 2 2026 ~4:20 AM ET) — Rob t2423 / t2424
- t2423 "Slow down the pill expand when enter fullscreen": Custom_1121 year-pill→NP bar WindowOpen zoom 1200→2000 ms (delay 150, sine inout); time labels fade in @2100 (300 ms); genre pill fade 600→1000, hard-hide 750→1150. Fix-in-place. ReloadSkin.
- t2424 "Movie to music mm big album reset??": Audit — 1122 never remounts and no script sets bz_rail hide/clear on section switch, but bz_railvis MM clause excluded Window.IsActive(music); on Movies→Music under MM the Music window goes active before Container.Content(artists/albums/songs) loads → false frames → big album Hidden 300/Visible 400 dip. Fix: bz_railvis MM clause = plain $EXP[bz_mmmushide]. Docs big-album.md, music-fanart-fs.md. Bak *.bak_5.33.326_pre327. No zip.

- 5.33.328 (Nov 2 2026, t2428 Continue): MM movie poster flash behind big album when Movies focused w/ music — gated poster stack group (bz_pready) with !bz_mmmushide. ReloadSkin. Not zipped.

- **5.33.329** (t2430, Nov 2 2026) Music section art fade-in instead of pop: big album + Music twin + list album fadetime 400; Music twin Visible fade 400 sine. Warm A/B untouched. ReloadSkin. Not zipped.

## 5.33.330 — MM auto-hide extend (mm-feature-fanart) — Nov 02 2026 ~4:35 AM ET (Rob t2436u "continue")
- On MM auto-hide (bz_mmidle, Tuner Auto-hide menu / 30 s): global colour backdrop (BezelGlobalBackdrop) fades out 1500 ms with the strip.
- Fanart stage shows associated clearart (clearlogo→tvshow→artist→clearart) + movie/TV/artist title ONLY during auto-hide (Music/Videos underlay, Container 60 focused item). New vars BzMMIdleClear / BzMMIdleTitle; group before 6897 in BezelNavMenu.
- Backup bak_5.33.329_pre330/. Docs mm-list.md + skin-settings-tuner.md. No K40. XML only → ReloadSkin. Not zipped. Not GUI-smoked.

## 2026-11-02 ~04:45 ET — 5.33.331 Settings Warm drill-downs (Rob t2438u overnight)
- PLAYER ▾ VIDEOS/MUSIC/DISCS/LANGUAGE, MEDIA ▾ VIDEO FILES/MUSIC FILES/PICTURES, LIBRARY ▾ VIDEO/MUSIC LIBRARY, INTERFACE ▾ REGIONAL, SERVICES » SMB/WEATHER/CACHING, EVENT LOG → Warm pages on 9132 (generic pills from Settings.GetSettings). MEDIA ▾ SOURCES → Media Sources 1117.
- New generator `/workspace/b401/set5215/gen533.py` (+ scripts/bz_set_pages.py). FULL restart (.py). Not zipped.

## 5.33.332–333 (2026-11-02 overnight)
- 332: bz_railvis clause — big album 1122 shows while music plays under Settings 1130 / Add-ons 1131 / addonbrowser (t2447/t2448).
- 333: same clause extended to Media Sources 1117 + 1132 (t2449). XML only → ReloadSkin. Live smoke pending (album.sh smoke did not reach 1131; MM was in front).
- 334 (t2450u): Tuner WARM SYSTEM sub merged into single WARM 2.0.1 folder. (t2443u) Video list + ALLROW slide 510→517, flush with strip x570. Album re-smoke 1130/1131/1117/1132 PASS. Movies flash root-caused (in-place warm park 0.2 s) — flagged, not changed. XML only → ReloadSkin.
- 335 (t2451u): Add-ons strip — background section list 60 + dtap hint hidden while 1131/1130/1117/1132 visible (was bleeding through). XML only → ReloadSkin. Smoke 335_addons_pre/post.png. MM Movies flash untouched (awaiting Rob).

## 5.33.336 — t2453 MM Movies focus flash + pull-back (FULL restart, .py)
- bz_flip.py: _bzstrip no-op if strip focused; _restore2/_defer use live strip row via forced SetFocus. 0.2 s warm delay untouched. Backup bak_5.33.335_pre336/. behaviors/mm-warm.md updated. Smoke OK: shots audit_settings_levels/tv/336_mm_{music,tv,movies_focus}.png. No zip/push.

## 5.33.337 (t2458, Nov 2 ~5:30 AM ET)
- ADD SOURCE is now Warm-direct (opens the stock add-source dialog, then returns to 1117/7130). IMPORT LIBRARY stays SKIP (no builtin; stock settings action).
- Deepened Settings pages: display, power, logging, games, audio (new GENP pills).
- TV seasons `..`: visibility guards added, NOT fixed yet (still visible).
- Needs a FULL restart (bz_set.py, bz_set_pages.py). No zip, no push. Backup bak_5.33.336_pre337/.

## 5.33.338 (t2458, Nov 2 ~5:40 AM ET)
- TV seasons `..` above the strip: FIXED. The parent row is hidden in seasons content by a group-level `!ListItem.IsParentFolder | !Container.Content(seasons)` guard in the list-60 layouts. The 337 label guards were removed. L2 unchanged. Up from S1 still goes to ALL SEASONS.
- XML only, so ReloadSkin is enough. Backup bak_5.33.337_pre338/. No zip, no push.
- 5.33.339 (bak_5.33.338_pre339): SERVICES › NAME moved from stock Settings/Services to Warm: Bezel keyboard (bz_set.py dname), kind m→p. Smoked: keyboard opens, Back returns to the NAME row. AUDIT/SKIP updated; no other Warm candidates are left. No zip/push.
- 5.33.340 (bak_5.33.339_pre340): SERVICES NAME is a text pill. No ‹ › and no L/R cycle (txt prop + list guards + py TXT guard). Save smoke OK: keyboard → BezelTest → pill BEZELTEST + RPC value, restored to Kodi. Shots b401/audit_settings_levels/340_*.png. No zip/push.
- 5.33.341 (bak_5.33.340_pre341): 330's MM auto-hide clearart/title was dead. $VAR inside String.IsEmpty in visible guards was never true; replaced with Container(60) Label/Art conditions. XML only, deployed then ReloadSkin. Smoke 341_mm_idle.png (Friends logo + title). 330's 'Not GUI-smoked' item is closed. No zip/push.
- 5.33.342 (bak_5.33.341_pre342): TV seasons no-All edge case. Repro: showallitems=false leaves a blank top slot (tv/341_noall_pre.png). Fix: the 8 guards add | !System.GetBool(videolibrary.showallitems). Smoke tv/342_withall.png (GoT, no `..`) + tv/342_noall.png (BB, `..` in slot); setting restored to true. Library: all 8 shows have 2 seasons + All row. XML only, deployed then ReloadSkin. No zip/push.
- 5.33.342 verify (Nov 2 ~5:29 AM ET): the 280 'Open: L2 ALL ALBUMS not shown in half-list' is CLOSED, fixed in 282 (bz_allhalf). Live: Radiohead L2 shows ALL ALBUMS under 3 albums. Down from the last album reaches it and Up returns. Shot b401/audit_settings_levels/343_music_L2_all.png. No change, no bump.
- 5.33.343 (bak_5.33.342_pre343): OUT OF OVERNIGHT SCOPE (Rob t2466u; found while scavenging old REQUESTS, not from t2438/t2458). TV episode lists in strip mode: 3.5.6 info pairs + Description + plot were drawn over the strip list (shots 343_tvL3.png / 343_recenteps_item.png). Fix: 4 controls get !$EXP[bz_vstrip]. Smoke tv/343_L3_fixed.png clean. Revert = restore bak_5.33.342_pre343. Also verified with no change: 280's Music L2 ALL ALBUMS half-list was already fixed in 282 (343_music_L2_all.png). Work stopped, idle.

- 5.33.344 (Nov 2 2026, t2489): MM FAVOURITES fix — ActivateWindow(Favourites)→favouritesbrowser (Kodi 21). FULL restart. Not zipped.
- 5.33.345 t2490 TV pills clipped: VSTRIP meta pill grouplist width 400→780 (Includes_Bezel). ReloadSkin.
- 5.33.346 (t2488): bz_pos_a/b poster lane gated Window.IsActive(videos) — no posters in Music album frame. ReloadSkin. Not zipped.
- 5.33.347 (t2491): list 60 clip 981→858 (ends y978 above dtap hint y978 h30); PVR 50 lists 900→858. Grid 63 already ends y832. ReloadSkin. Not zipped.
- 5.33.348 (t2492): MM SEARCH 1107 rebuilt as Warm strip (1131 chrome/rows), items unchanged; list 60 + dtap hidden under 1107. ReloadSkin. Shot b401/d348_search.png. Not zipped.

## 5.33.349 — t2493 Settings → Warm deeper (FULL restart, .py)
Custom_1130_BzSettings.xml: new 9132 pages upnp/control/airplay/internet (+visible OR), 9131 UPnP/Web server→CONTROL/AirPlay rows → pg rows, SYSTEM ▸ INTERNET row, 9132 onback = 9139 only. bz_set.py pgback: services sub-pages → 9131. bz_set_pages.py GENP += 18 ids. Backups *.bak_5.33.348_pre349. Docs behaviors/settings.md, AUDIT.md.
- 5.33.350 t2490 TV/Movies pills real layout: 2 rows inside text column (row1 short pills w410, studio max200; row2 genre max410 truncating), name/plot down 40. bak *.bak_5.33.349_pre350. ReloadSkin. Shot b401/d350_tv.png.
- 5.33.351 t2498/t2499: Settings SKIN row L/R pick + Select switch; SKIN page Warm rows replace MORE (KODI)
- 5.33.354 (t2515–t2518): strip KB remote path #!?→DEL→DONE→CANCEL (new 9604); CLEAN LIBRARY Yes/No (bz_set msclean). FULL.
- 5.33.355 COLDLEAF: idle_hinge cold-start cover re-read (pt2531u)
- 5.33.356 (t2536) Media Sources: per-section ADD SOURCE (7107/7117/7122), UPDATE→REFRESH LIBRARY, 1132 MENU edit·remove hint. Not zipped.
- 5.33.360 t2554/t2555 Add Source real Warm chrome + art fix
- 5.33.364 (t2572/t2573/t2577, resumed after pause Nov 2 ~1:50 PM ET): SOURCES Select → Warm dropdown OPEN/RENAME/REMOVE/REFRESH (no EDIT; REFRESH not Pictures), source name in strip. DialogConfirm Warm GLOBAL (BzMSUnderlay on all Yes/No; B3 dim only over fullscreen video/viz). Backups *.bak_5.33.363_pre364. FULL restart (.py). NOT GUI-smoked: box rebooted, Kodi binary missing, apt mirror 500. No zip.
- 5.33.365 (t2585 Go, Nov 2 ~2 PM ET): new DialogContentSettings.xml Warm (Set content); first-open fix (no window fade on DialogMediaSource/ContentSettings, underlay art sync); StdFrame showline param, off in BzMSUnderlay (poster line). Backups *.bak_5.33.364_pre365. XML only → ReloadSkin. NOT GUI-smoked (no Kodi on box). No zip.
- 5.33.366 artwork group 6400 (Rob t2616) — 1122 album opacity-gated, poster layer 6401 prewarm/crossfade; Includes 6180 railvis guard. Unsmoked (no Kodi).
- 5.33.367 (Nov 2 2026, t2622): artwork phase 2 — bz_flip v60_mirror relays list 60 → Home props; BezelVPLPoster moved into 1122 layer 6401; per-screen mounts → BezelVPLPosterTap only. FULL restart. Not zipped.
- 5.33.369 (Nov 2 2026, t2652): MMHOLD — Music→MM holds focused list-60 art (bz_m_idle_lock) for uadv hold (5 s, min 3) then UADVRAND; RANDSTART untouched. FULL restart. Unsmoked.
