# Music Fanart FS (dialog 1121) — music-fanart-fs

**Object:** `music-fanart-fs` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-fanart-fs.md) · [layout](../layout/music-fanart-fs.md) · [state](../state/music-fanart-fs.md) · [motion](../motion/music-fanart-fs.md) · [art](../art/music-fanart-fs.md) · [input](../input/music-fanart-fs.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
In Music, FULLSCREEN goes to a dialog copy of Fanart FS instead of Kodi's visualisation window. The Music window stays underneath, so the fanart stage and the swaying album never restart. Same look, same keys. Every other section still opens real Kodi visualisation.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_at_fsslide`
- set/clear sites: 24 · read sites: 118
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`

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

### `bz_fsnp`
- set/clear sites: 5 · read sites: 2
  - `xml/MusicVisualisation.xml` L11: `<onload>SetProperty(bz_fsnp,true,home)</onload>`
  - `xml/MusicVisualisation.xml` L16: `<onunload condition="String.IsEqual(Window(Home).Property(bz_fsnp),true)">ClearProperty(bz_np,home)</onunload>`
  - `xml/MusicVisualisation.xml` L17: `<onunload condition="!$EXP[bz_navmenu]">AlarmClock(bz_vizret,SetFocus(60),00:00,silent)</onunload><!-- 5.33.112 t786: Play Next / viz exit -> section list 60 --`
  - `xml/Includes_Bezel.xml` L2801: `<expression name="bz_np">String.IsEqual(Window(Home).Property(bz_np),true) + [Window.IsActive(music) | String.IsEqual(Window(Home).Property(bz_fsnp),true)] + St`
  - `xml/MusicVisualisation.xml` L21: `<visible>String.IsEqual(Window(Home).Property(bz_fsnp),true)</visible>`

### `bz_m1121_off`
- set/clear sites: 1 · read sites: 3
  - `xml/Custom_1121_MusicFanartFS.xml` L6: `Kill switch: Skin.SetBool(bz_m1121_off) -> every trigger falls back to ActivateWindow(visualisation).`
  - `xml/Includes_Bezel.xml` L334: `<expression name="bz_m1121ok">!Skin.HasSetting(bz_m1121_off) + Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !Window.IsActive(visualisation)</ex`
  - `xml/Custom_1121_MusicFanartFS.xml` L11: `<onload condition="Skin.HasSetting(bz_m1121_off) | !Player.HasAudio | Player.HasVideo">Dialog.Close(1121,true)</onload>`
  - `xml/Custom_1121_MusicFanartFS.xml` L12: `<onload condition="Skin.HasSetting(bz_m1121_off) + Player.HasAudio + !Player.HasVideo">ActivateWindow(visualisation)</onload>`

### `bz_m1121ok`
- set/clear sites: 2 · read sites: 7
  - `xml/Includes_Tuner.xml` L499: `<onback condition="String.IsEqual(Window(Home).Property(bz_tunesrc),pwr)">ClearProperty(bz_navtune,home)</onback><onback condition="String.IsEqual(Window(Home).`
  - `xml/Includes_Tuner.xml` L499: `<onback condition="String.IsEqual(Window(Home).Property(bz_tunesrc),pwr)">ClearProperty(bz_navtune,home)</onback><onback condition="String.IsEqual(Window(Home).`
  - `xml/Includes_Bezel.xml` L334: `<expression name="bz_m1121ok">!Skin.HasSetting(bz_m1121_off) + Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !Window.IsActive(visualisation)</ex`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_m1121ret`
- set/clear sites: 0 · read sites: 1
  - `xml/Custom_1121_MusicFanartFS.xml` L21: `<onunload condition="!$EXP[bz_navmenu]">AlarmClock(bz_m1121ret,SetFocus(60),00:00,silent)</onunload><!-- Back -> Music section list 60 -->`

### `bz_m1121stop`
- set/clear sites: 0 · read sites: 1
  - `xml/Timers.xml` L33: `<name>bz_m1121stop</name>`

### `bz_navmenu`
- set/clear sites: 9 · read sites: 593
  - `xml/Includes_Bezel.xml` L2335: `<control type="list" id="63"><onback condition="[String.IsEmpty(Container.FolderPath) | String.IsEqual(Container.FolderPath,sources://pictures/)] + !$EXP[bz_nav`
  - `xml/MusicVisualisation.xml` L17: `<onunload condition="!$EXP[bz_navmenu]">AlarmClock(bz_vizret,SetFocus(60),00:00,silent)</onunload><!-- 5.33.112 t786: Play Next / viz exit -> section list 60 --`
  - `xml/FileManager.xml` L14: `<control type="list" id="20"><onback condition="String.IsEmpty(Container(20).FolderPath) + !$EXP[bz_navmenu]">SetProperty(bz_nav,true,home)</onback><!-- 5.33.17`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`

### `bz_np`
- set/clear sites: 33 · read sites: 98
  - `xml/Custom_1112_NowPlaying.xml` L19: `<onunload condition="!Window.IsActive(visualisation)">ClearProperty(bz_np,home)</onunload>`
  - `xml/Custom_1112_NowPlaying.xml` L42: `<onclick>ClearProperty(bz_np,home)</onclick><onclick>Dialog.Close(1112)</onclick></control>`
  - `xml/Custom_1112_NowPlaying.xml` L44: `<control type="button" id="6299"><left>-400</left><top>0</top><width>10</width><height>10</height><label></label><texturefocus></texturefocus><texturenofocus></`
  - `xml/Custom_1112_NowPlaying.xml` L3: `list view (view 60, not the grid): bz_cmd.py np (logo menu entry, 60 s idle open) sets bz_npdlg + bz_np and opens it. Every other route keeps the in-place panel`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L13: `and run Kodi's fullscreen music window (the old route). Opened by bz_cmd.py (menu card, idle) bz_np is already set. -->`

### `bz_npmode`
- set/clear sites: 12 · read sites: 16
  - `xml/Includes_Bezel.xml` L3027: `<onclick condition="!$EXP[bz_npm_bio]">SetProperty(bz_npinfo_prev,$INFO[Skin.String(bz_npmode)],home)</onclick>`
  - `xml/Includes_Bezel.xml` L3028: `<onclick condition="!$EXP[bz_npm_bio]">Skin.SetString(bz_npmode,bio)</onclick>`
  - `xml/Includes_Bezel.xml` L3029: `<onclick condition="$EXP[bz_npm_bio] + !String.IsEmpty(Window(Home).Property(bz_npinfo_prev))">Skin.SetString(bz_npmode,$INFO[Window(Home).Property(bz_npinfo_pr`
  - `xml/Includes_Bezel.xml` L347: `<expression name="bz_npm_vis">String.IsEqual(Skin.String(bz_npmode),vis) | String.IsEmpty(Skin.String(bz_npmode))</expression>`
  - `xml/Includes_Bezel.xml` L347: `<expression name="bz_npm_vis">String.IsEqual(Skin.String(bz_npmode),vis) | String.IsEmpty(Skin.String(bz_npmode))</expression>`
  - `xml/Includes_Bezel.xml` L348: `<expression name="bz_npm_bio">String.IsEqual(Skin.String(bz_npmode),bio)</expression>`

### `bz_pndlg_ok`
- set/clear sites: 8 · read sites: 104
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L335: `<expression name="bz_pndlg_ok">!Skin.HasSetting(bz_pndlg_off) + Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !Window.IsActive(visualisation) + `
  - `xml/Includes_Bezel.xml` L1371: `<!-- 5.33.221: touch tap big album = Dialogue FS (same as 6390 remote) --><onclick condition="$EXP[bz_pndlg_ok] + String.IsEqual(Skin.String(bz_at_fsslide),1)">`
  - `xml/Includes_Bezel.xml` L1371: `<!-- 5.33.221: touch tap big album = Dialogue FS (same as 6390 remote) --><onclick condition="$EXP[bz_pndlg_ok] + String.IsEqual(Skin.String(bz_at_fsslide),1)">`

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

### `bz_tunesrc`
- set/clear sites: 16 · read sites: 3
  - `xml/Custom_1118_PowerMenu.xml` L8: `<onload>ClearProperty(bz_tunesrc,home)</onload><onload>SetProperty(bz_pwrswap,1,home)</onload><!-- t4943 K52: skip 6996 slides on POWER swap -->`
  - `xml/Custom_1118_PowerMenu.xml` L26: `<item><label>TUNER</label><onclick>SetProperty(bz_tunesrc,pwr,home)</onclick><onclick>SetProperty(bz_navtune,true,home)</onclick><onclick>ClearProperty(bz_navbe`
  - `xml/Custom_1130_BzSettings.xml` L51: `<item><label>WARM 2.0.1 · TUNER</label><property name="kind">m</property><property name="lvl">sub</property><onclick>SetProperty(bz_tunesrc,set,home)</onclick><`
  - `xml/Custom_1118_PowerMenu.xml` L10: `<onunload condition="!String.IsEqual(Window(Home).Property(bz_tunesrc),pwr)">AlarmClock(bzpwrf,SetFocus(6996),00:00,silent,false)</onunload>`
  - `xml/Custom_1130_BzSettings.xml` L102: `<control type="group"><visible>String.IsEqual(ListItem.Property(kind),p)</visible><animation effect="fade" start="100" end="70" time="0" condition="String.IsEqu`
  - `xml/Custom_1115_MusicControls.xml` L40: `<control type="group"><top>766</top><control type="image"><left>12</left><top>4</top><width>366</width><height>48</height><texture border="23" colordiffuse="E6F`

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

