# Fanart FS (visualisation) — fanart-fs

**Object:** `fanart-fs` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/fanart-fs.md) · [layout](../layout/fanart-fs.md) · [state](../state/fanart-fs.md) · [motion](../motion/fanart-fs.md) · [art](../art/fanart-fs.md) · [input](../input/fanart-fs.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Full-screen music has two looks. **Fanart FS** is the plain fanart view with the fan art pill. **Album viz** is a big centred album with optional side albums and the big album pill. A double-Select switches from fanart to album viz. Back from album viz drops to fanart.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_dfs_mode`
- set/clear sites: 18 · read sites: 13
  - `xml/Includes_Bezel.xml` L999: `<onclick condition="String.IsEqual(Skin.String(bz_dfs_mode),album)">Skin.Reset(bz_dfs_mode)</onclick><onclick condition="!String.IsEqual(Skin.String(bz_dfs_mode`
  - `xml/Includes_Bezel.xml` L999: `<onclick condition="String.IsEqual(Skin.String(bz_dfs_mode),album)">Skin.Reset(bz_dfs_mode)</onclick><onclick condition="!String.IsEqual(Skin.String(bz_dfs_mode`
  - `xml/Includes_Bezel.xml` L999: `<onclick condition="String.IsEqual(Skin.String(bz_dfs_mode),album)">Skin.Reset(bz_dfs_mode)</onclick><onclick condition="!String.IsEqual(Skin.String(bz_dfs_mode`
  - `xml/Includes_Bezel.xml` L985: `<variable name="BezelDFSModeName"><value condition="String.IsEqual(Skin.String(bz_dfs_mode),album)">ALBUM</value><value>PREV/NEXT</value></variable>`
  - `xml/Includes_Bezel.xml` L988: `<!-- Oct 31 2026: big album pill — shared by Dialogue FS 1120 and FS album viz (MusicVisualisation). ALBUM ↔ PREV/NEXT via bz_dfs_mode. -->`
  - `xml/MusicVisualisation.xml` L29: `<control type="group"><animation effect="fade" start="100" end="0" time="600" tween="sine" easing="inout">WindowClose</animation><include content="BezelFSPlayNe`

### `bz_flip`
- set/clear sites: 1 · read sites: 69
  - `xml/MyVideoNav.xml` L23: `<onload condition="Skin.HasSetting(bz_grid_video)">SetProperty(bz_gpend,1,home)</onload><onload>AlarmClock(bzgpend,ClearProperty(bz_gpend,home),00:02,silent)</o`
  - `xml/MyPlaylist.xml` L9: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L14: `<!-- BETA 1.1b: the gate below uses Player.HasAudio directly (the debounced bz_audio_latch from bz_flip.py may not be set yet on the first Tab after Kodi start;`

### `bz_flip_running`
- set/clear sites: 5 · read sites: 25
  - `scripts/bz_cmd.py` L21: `for k in ('bz_flip_running', 'bz_dtap_running', 'bz_precache_running'): home.clearProperty(k)`
  - `scripts/bz_flip.py` L81: `home.setProperty('bz_flip_running', 'true')`
  - `scripts/bz_flip.py` L455: `home.setProperty('bz_flip_fail', f.__name__); home.clearProperty('bz_flip_running'); return`
  - `xml/MyPlaylist.xml` L9: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`
  - `xml/MusicVisualisation.xml` L14: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`
  - `xml/Custom_1121_MusicFanartFS.xml` L18: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`

### `bz_fsbounce`
- set/clear sites: 0 · read sites: 2
  - `xml/Includes_Bezel.xml` L1579: `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="$EXP[bz_covercol] + String.IsEmpty(Window(Home).Property(bz_fsbou`
  - `xml/Includes_Bezel.xml` L1580: `<animation effect="fade" start="0" end="100" time="300" tween="sine" easing="inout" condition="$EXP[bz_covercol] + String.IsEmpty(Window(Home).Property(bz_fsbou`

### `bz_fsfoc`
- set/clear sites: 0 · read sites: 1
  - `xml/MusicVisualisation.xml` L13: `<onload>AlarmClock(bz_fsfoc,SetFocus(6390),00:00,silent)</onload><!-- Fanart FS: re-focus 6390 after bz_np visible (defaultcontrol can miss hidden 6390 at init)`

### `bz_fsnp`
- set/clear sites: 5 · read sites: 2
  - `xml/MusicVisualisation.xml` L11: `<onload>SetProperty(bz_fsnp,true,home)</onload>`
  - `xml/MusicVisualisation.xml` L16: `<onunload condition="String.IsEqual(Window(Home).Property(bz_fsnp),true)">ClearProperty(bz_np,home)</onunload>`
  - `xml/MusicVisualisation.xml` L17: `<onunload condition="!$EXP[bz_navmenu]">AlarmClock(bz_vizret,SetFocus(60),00:00,silent)</onunload><!-- 5.33.112 t786: Play Next / viz exit -> section list 60 --`
  - `xml/Includes_Bezel.xml` L2801: `<expression name="bz_np">String.IsEqual(Window(Home).Property(bz_np),true) + [Window.IsActive(music) | String.IsEqual(Window(Home).Property(bz_fsnp),true)] + St`
  - `xml/MusicVisualisation.xml` L21: `<visible>String.IsEqual(Window(Home).Property(bz_fsnp),true)</visible>`

### `bz_gridret`
- set/clear sites: 2 · read sites: 4
  - `xml/MusicVisualisation.xml` L18: `<onunload>SetProperty(bz_gridret,1,home)</onunload><onunload>AlarmClock(bzgridret,ClearProperty(bz_gridret,home),00:01,silent)</onunload><!-- 4.0.1 O22: the sec`
  - `xml/MusicVisualisation.xml` L18: `<onunload>SetProperty(bz_gridret,1,home)</onunload><onunload>AlarmClock(bzgridret,ClearProperty(bz_gridret,home),00:01,silent)</onunload><!-- 4.0.1 O22: the sec`
  - `xml/Includes_Bezel.xml` L1567: `<animation effect="fade" start="100" end="0" time="0" condition="$EXP[bz_gridfirst] + !String.IsEmpty(Window(Home).Property(bz_gridret))">Conditional</animation`
  - `xml/Includes_Bezel.xml` L1567: `<animation effect="fade" start="100" end="0" time="0" condition="$EXP[bz_gridfirst] + !String.IsEmpty(Window(Home).Property(bz_gridret))">Conditional</animation`
  - `xml/Includes_Bezel.xml` L2697: `<animation effect="fade" start="100" end="0" time="0" condition="$EXP[bz_gridfirst] + !String.IsEmpty(Window(Home).Property(bz_gridret))">Conditional</animation`

### `bz_m1121ok`
- set/clear sites: 2 · read sites: 7
  - `xml/Includes_Tuner.xml` L499: `<onback condition="String.IsEqual(Window(Home).Property(bz_tunesrc),pwr)">ClearProperty(bz_navtune,home)</onback><onback condition="String.IsEqual(Window(Home).`
  - `xml/Includes_Tuner.xml` L499: `<onback condition="String.IsEqual(Window(Home).Property(bz_tunesrc),pwr)">ClearProperty(bz_navtune,home)</onback><onback condition="String.IsEqual(Window(Home).`
  - `xml/Includes_Bezel.xml` L334: `<expression name="bz_m1121ok">!Skin.HasSetting(bz_m1121_off) + Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !Window.IsActive(visualisation)</ex`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_navmenu`
- set/clear sites: 9 · read sites: 593
  - `xml/Includes_Bezel.xml` L2335: `<control type="list" id="63"><onback condition="[String.IsEmpty(Container.FolderPath) | String.IsEqual(Container.FolderPath,sources://pictures/)] + !$EXP[bz_nav`
  - `xml/MusicVisualisation.xml` L17: `<onunload condition="!$EXP[bz_navmenu]">AlarmClock(bz_vizret,SetFocus(60),00:00,silent)</onunload><!-- 5.33.112 t786: Play Next / viz exit -> section list 60 --`
  - `xml/FileManager.xml` L14: `<control type="list" id="20"><onback condition="String.IsEmpty(Container(20).FolderPath) + !$EXP[bz_navmenu]">SetProperty(bz_nav,true,home)</onback><!-- 5.33.17`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`

### `bz_noop`
- set/clear sites: 6 · read sites: 2
  - `xml/Includes_Bezel.xml` L2658: `<onclick>SetProperty(bz_noop,1,home)</onclick><!-- BETA 2 item 23: a tap no longer flips the poster (long-press / context = extended info as before) -->`
  - `xml/Includes_Bezel.xml` L2974: `<onleft>6390</onleft><onright>SetProperty(bz_noop,1,home)</onright><onback>6390</onback>`
  - `xml/Includes_Bezel.xml` L2978: `<onback>6390</onback><onup>6390</onup><onleft>6390</onleft><onright>SetProperty(bz_noop,1,home)</onright><ondown>SetProperty(bz_noop,1,home)</ondown>`
  - `xml/Includes_Bezel.xml` L2956: `<onup condition="[!String.IsEqual(Window(Home).Property(bz_pnoff),1)]">6401</onup><onup condition="String.IsEqual(Window(Home).Property(bz_pnoff),1)">6391</onup`
  - `xml/Includes_Bezel.xml` L2956: `<onup condition="[!String.IsEqual(Window(Home).Property(bz_pnoff),1)]">6401</onup><onup condition="String.IsEqual(Window(Home).Property(bz_pnoff),1)">6391</onup`

### `bz_np`
- set/clear sites: 33 · read sites: 98
  - `xml/Custom_1112_NowPlaying.xml` L19: `<onunload condition="!Window.IsActive(visualisation)">ClearProperty(bz_np,home)</onunload>`
  - `xml/Custom_1112_NowPlaying.xml` L42: `<onclick>ClearProperty(bz_np,home)</onclick><onclick>Dialog.Close(1112)</onclick></control>`
  - `xml/Custom_1112_NowPlaying.xml` L44: `<control type="button" id="6299"><left>-400</left><top>0</top><width>10</width><height>10</height><label></label><texturefocus></texturefocus><texturenofocus></`
  - `xml/Custom_1112_NowPlaying.xml` L3: `list view (view 60, not the grid): bz_cmd.py np (logo menu entry, 60 s idle open) sets bz_npdlg + bz_np and opens it. Every other route keeps the in-place panel`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L13: `and run Kodi's fullscreen music window (the old route). Opened by bz_cmd.py (menu card, idle) bz_np is already set. -->`

### `bz_npctl`
- set/clear sites: 2 · read sites: 10
  - `xml/MusicVisualisation.xml` L46: `<!-- 5.33.205: 6409 touch — onclick=play/pause; ondoubleclick=album viz (ClearProperty bz_pnoff). Keys bounce to 6390 (onfocus). --><control type="button" id="6`
  - `scripts/bz_flip.py` L929: `home.clearProperty('bz_npctl')`
  - `xml/Custom_1112_NowPlaying.xml` L38: `<include content="BezelNPControls"><param name="vis" value="$EXP[bz_np] + String.IsEqual(Window(Home).Property(bz_npctl),true)"/><param name="dx" value="0"/><pa`
  - `xml/Includes_Bezel.xml` L2285: `<include content="BezelNPControls"><param name="vis" value="[$EXP[bz_np] + String.IsEqual(Window(Home).Property(bz_npctl),true)] | [!$EXP[bz_np] + !String.IsEmp`
  - `xml/Includes_Bezel.xml` L2962: `<visible>!String.IsEqual(Window(Home).Property(bz_npctl),true)</visible><!-- 3.5.1: tap the bottom of the panel (left half only) shows the player controls -->`

### `bz_npm_ctl`
- set/clear sites: 1 · read sites: 11
  - `xml/Custom_1121_MusicFanartFS.xml` L35: `<onclick condition="$EXP[bz_npm_ctl]">ActivateWindow(1115)</onclick><onclick condition="$EXP[bz_npm_vis]">Skin.SetString(bz_npmode,bio)</onclick><onclick condit`
  - `xml/Includes_Bezel.xml` L351: `<expression name="bz_npm_ctl">String.IsEqual(Skin.String(bz_npmode),controls)</expression><!-- 4.0.1 O16 -->`
  - `xml/Includes_Bezel.xml` L2826: `<variable name="BezelNPModeName"><value condition="Window.IsActive(1115)">CONTROLS</value><value condition="$EXP[bz_npm_ctl]">CONTROLS  ▾</value><value conditio`
  - `xml/Includes_Bezel.xml` L2826: `<variable name="BezelNPModeName"><value condition="Window.IsActive(1115)">CONTROLS</value><value condition="$EXP[bz_npm_ctl]">CONTROLS  ▾</value><value conditio`

### `bz_npmlabel`
- set/clear sites: 2 · read sites: 4
  - `xml/Custom_1121_MusicFanartFS.xml` L35: `<onclick condition="$EXP[bz_npm_ctl]">ActivateWindow(1115)</onclick><onclick condition="$EXP[bz_npm_vis]">Skin.SetString(bz_npmode,bio)</onclick><onclick condit`
  - `xml/Custom_1121_MusicFanartFS.xml` L35: `<onclick condition="$EXP[bz_npm_ctl]">ActivateWindow(1115)</onclick><onclick condition="$EXP[bz_npm_vis]">Skin.SetString(bz_npmode,bio)</onclick><onclick condit`
  - `xml/Includes_Bezel.xml` L2948: `the mode name shows for about 2 s after a tap (bz_npmlabel, bz_cmd.py npmode), then fades. Keys: Up from the block; touch: tap -->`
  - `xml/Includes_Bezel.xml` L3014: `<!-- t4857: Controls back in fan art pill cycle — Visualizer > Bio > Fanart > Lyrics > Up Next > Controls. O78: landing sets mode only (stay on pill). Select wh`
  - `xml/Includes_Bezel.xml` L3014: `<!-- t4857: Controls back in fan art pill cycle — Visualizer > Bio > Fanart > Lyrics > Up Next > Controls. O78: landing sets mode only (stay on pill). Select wh`

### `bz_npmode`
- set/clear sites: 12 · read sites: 16
  - `xml/Includes_Bezel.xml` L3027: `<onclick condition="!$EXP[bz_npm_bio]">SetProperty(bz_npinfo_prev,$INFO[Skin.String(bz_npmode)],home)</onclick>`
  - `xml/Includes_Bezel.xml` L3028: `<onclick condition="!$EXP[bz_npm_bio]">Skin.SetString(bz_npmode,bio)</onclick>`
  - `xml/Includes_Bezel.xml` L3029: `<onclick condition="$EXP[bz_npm_bio] + !String.IsEmpty(Window(Home).Property(bz_npinfo_prev))">Skin.SetString(bz_npmode,$INFO[Window(Home).Property(bz_npinfo_pr`
  - `xml/Includes_Bezel.xml` L347: `<expression name="bz_npm_vis">String.IsEqual(Skin.String(bz_npmode),vis) | String.IsEmpty(Skin.String(bz_npmode))</expression>`
  - `xml/Includes_Bezel.xml` L347: `<expression name="bz_npm_vis">String.IsEqual(Skin.String(bz_npmode),vis) | String.IsEmpty(Skin.String(bz_npmode))</expression>`
  - `xml/Includes_Bezel.xml` L348: `<expression name="bz_npm_bio">String.IsEqual(Skin.String(bz_npmode),bio)</expression>`

### `bz_pnfoc`
- set/clear sites: 13 · read sites: 6
  - `xml/Includes_Bezel.xml` L997: `<control type="button" id="6401"><width>auto</width><height>32</height><label>$VAR[BezelDFSModeName]</label><onfocus>ClearProperty(bz_pnfoc,home)</onfocus><font`
  - `xml/Includes_Bezel.xml` L2951: `<control type="button" id="6390"><onfocus>ClearProperty(bz_pnfoc,home)</onfocus><!-- 5.33.109: controls hidden until Select -->`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L986: `<variable name="BzPN107Nof"><value condition="Window.IsActive(1120) | String.IsEmpty(Window(Home).Property(bz_pnfoc))">00FFFFFF</value><value>4DFFFFFF</value></`
  - `xml/Includes_Bezel.xml` L987: `<variable name="BzPN107Foc"><value condition="Window.IsActive(1120) | String.IsEmpty(Window(Home).Property(bz_pnfoc))">00FFFFFF</value><value>B3FFFFFF</value></`
  - `xml/Includes_Bezel.xml` L1038: `<!-- 5.33.107 t721: mirrored sway removed; 1120 overlay visuals live in BezelMusicPlayingArt sway group (BzPN107) --><control type="group"><left>660</left><top>`

### `bz_pnoff`
- set/clear sites: 25 · read sites: 70
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`

### `bz_sway_restart`
- set/clear sites: 4 · read sites: 5
  - `xml/MyPlaylist.xml` L10: `<onload>SetProperty(bz_sway_restart,true,home)</onload>`
  - `xml/MusicVisualisation.xml` L15: `<onload>SetProperty(bz_sway_restart,true,home)</onload>`
  - `xml/MyMusicNav.xml` L18: `<onload>SetProperty(bz_sway_restart,true,home)</onload>`
  - `xml/Custom_1121_MusicFanartFS.xml` L19: `<!-- no bz_sway_restart: sway must stay unbroken (Music never remounts) -->`
  - `xml/Includes_Tuner.xml` L2075: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),swayshort)">Skin.Reset(bz_swayright)</onleft><onleft condition="String.IsEqual(Container`
  - `xml/Includes_Tuner.xml` L2075: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),swayshort)">Skin.Reset(bz_swayright)</onleft><onleft condition="String.IsEqual(Container`

### `bz_vdtap`
- set/clear sites: 10 · read sites: 8
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Custom_1121_MusicFanartFS.xml` L44: `<onclick condition="String.IsEqual(Window(Home).Property(bz_pnoff),1) + String.IsEqual(Window(Home).Property(bz_vdtap),1)">CancelAlarm(bz_vdtapgo,true)</onclick`
  - `xml/Custom_1121_MusicFanartFS.xml` L44: `<onclick condition="String.IsEqual(Window(Home).Property(bz_pnoff),1) + String.IsEqual(Window(Home).Property(bz_vdtap),1)">CancelAlarm(bz_vdtapgo,true)</onclick`
  - `xml/Custom_1121_MusicFanartFS.xml` L44: `<onclick condition="String.IsEqual(Window(Home).Property(bz_pnoff),1) + String.IsEqual(Window(Home).Property(bz_vdtap),1)">CancelAlarm(bz_vdtapgo,true)</onclick`

### `bz_vdtapgo`
- set/clear sites: 2 · read sites: 2
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Custom_1121_MusicFanartFS.xml` L44: `<onclick condition="String.IsEqual(Window(Home).Property(bz_pnoff),1) + String.IsEqual(Window(Home).Property(bz_vdtap),1)">CancelAlarm(bz_vdtapgo,true)</onclick`
  - `xml/Custom_1121_MusicFanartFS.xml` L45: `<onclick condition="String.IsEqual(Window(Home).Property(bz_pnoff),1) + String.IsEmpty(Window(Home).Property(bz_vdtap))">AlarmClock(bz_vdtapgo,PlayerControl(Pla`

### `bz_vizret`
- set/clear sites: 1 · read sites: 0
  - `xml/MusicVisualisation.xml` L17: `<onunload condition="!$EXP[bz_navmenu]">AlarmClock(bz_vizret,SetFocus(60),00:00,silent)</onunload><!-- 5.33.112 t786: Play Next / viz exit -> section list 60 --`

