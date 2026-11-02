# Dialogue FS — dialogue-fs

**Object:** `dialogue-fs` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/dialogue-fs.md) · [layout](../layout/dialogue-fs.md) · [state](../state/dialogue-fs.md) · [motion](../motion/dialogue-fs.md) · [art](../art/dialogue-fs.md) · [input](../input/dialogue-fs.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Tap the big album in Music, or press Right from Music controls, and the album slides out to a full-screen album view. Back slides it home again.

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

### `bz_audio_latch`
- set/clear sites: 4 · read sites: 47
  - `scripts/bz_flip.py` L946: `if home.getProperty('bz_np') and home.getProperty('bz_audio_latch') != 'true': home.clearProperty('bz_np')`
  - `scripts/bz_flip.py` L1516: `home.setProperty('bz_audio_latch', 'true'); sway['t0'] = time.time()   # sway (keyed on the latch) starts from flat`
  - `scripts/bz_flip.py` L1519: `if gone >= 2.5 or xbmc.getCondVisibility('Player.HasVideo'): home.clearProperty('bz_audio_latch'); gone = 0.0; sway['t0'] = None; had = False`
  - `xml/Custom_1112_NowPlaying.xml` L14: `<!-- BETA 1.1b: the gate below uses Player.HasAudio directly (the debounced bz_audio_latch from bz_flip.py may not be set yet on the first Tab after Kodi start;`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L125: `<expression name="bz_audio">[Player.HasAudio + !Player.HasVideo] | String.IsEqual(Window(Home).Property(bz_audio_latch),true)</expression>`

### `bz_dfs_mode`
- set/clear sites: 18 · read sites: 13
  - `xml/Includes_Bezel.xml` L999: `<onclick condition="String.IsEqual(Skin.String(bz_dfs_mode),album)">Skin.Reset(bz_dfs_mode)</onclick><onclick condition="!String.IsEqual(Skin.String(bz_dfs_mode`
  - `xml/Includes_Bezel.xml` L999: `<onclick condition="String.IsEqual(Skin.String(bz_dfs_mode),album)">Skin.Reset(bz_dfs_mode)</onclick><onclick condition="!String.IsEqual(Skin.String(bz_dfs_mode`
  - `xml/Includes_Bezel.xml` L999: `<onclick condition="String.IsEqual(Skin.String(bz_dfs_mode),album)">Skin.Reset(bz_dfs_mode)</onclick><onclick condition="!String.IsEqual(Skin.String(bz_dfs_mode`
  - `xml/Includes_Bezel.xml` L985: `<variable name="BezelDFSModeName"><value condition="String.IsEqual(Skin.String(bz_dfs_mode),album)">ALBUM</value><value>PREV/NEXT</value></variable>`
  - `xml/Includes_Bezel.xml` L988: `<!-- Oct 31 2026: big album pill — shared by Dialogue FS 1120 and FS album viz (MusicVisualisation). ALBUM ↔ PREV/NEXT via bz_dfs_mode. -->`
  - `xml/MusicVisualisation.xml` L29: `<control type="group"><animation effect="fade" start="100" end="0" time="600" tween="sine" easing="inout">WindowClose</animation><include content="BezelFSPlayNe`

### `bz_fsret`
- set/clear sites: 6 · read sites: 14
  - `xml/Includes_Bezel.xml` L1002: `<onback condition="String.IsEqual($PARAM[back_close],1)">SetProperty(bz_fsret,true,home)</onback><onback condition="String.IsEqual($PARAM[back_close],1)">AlarmC`
  - `xml/Includes_Bezel.xml` L1002: `<onback condition="String.IsEqual($PARAM[back_close],1)">SetProperty(bz_fsret,true,home)</onback><onback condition="String.IsEqual($PARAM[back_close],1)">AlarmC`
  - `xml/Custom_1120_PlayNext.xml` L21: `<onback>SetProperty(bz_fsret,true,home)</onback><onback>AlarmClock(bz_fsretclr,ClearProperty(bz_fsret,home),00:01,silent)</onback><onback>Dialog.Close(1120)</on`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`

### `bz_fsretclr`
- set/clear sites: 3 · read sites: 0
  - `xml/Includes_Bezel.xml` L1002: `<onback condition="String.IsEqual($PARAM[back_close],1)">SetProperty(bz_fsret,true,home)</onback><onback condition="String.IsEqual($PARAM[back_close],1)">AlarmC`
  - `xml/Custom_1120_PlayNext.xml` L21: `<onback>SetProperty(bz_fsret,true,home)</onback><onback>AlarmClock(bz_fsretclr,ClearProperty(bz_fsret,home),00:01,silent)</onback><onback>Dialog.Close(1120)</on`
  - `xml/Timers.xml` L30: `<onstop condition="Window.IsActive(1120) + !Player.HasAudio">SetProperty(bz_fsret,true,home)</onstop><onstop condition="Window.IsActive(1120) + !Player.HasAudio`

### `bz_noop`
- set/clear sites: 6 · read sites: 2
  - `xml/Includes_Bezel.xml` L2658: `<onclick>SetProperty(bz_noop,1,home)</onclick><!-- BETA 2 item 23: a tap no longer flips the poster (long-press / context = extended info as before) -->`
  - `xml/Includes_Bezel.xml` L2974: `<onleft>6390</onleft><onright>SetProperty(bz_noop,1,home)</onright><onback>6390</onback>`
  - `xml/Includes_Bezel.xml` L2978: `<onback>6390</onback><onup>6390</onup><onleft>6390</onleft><onright>SetProperty(bz_noop,1,home)</onright><ondown>SetProperty(bz_noop,1,home)</ondown>`
  - `xml/Includes_Bezel.xml` L2956: `<onup condition="[!String.IsEqual(Window(Home).Property(bz_pnoff),1)]">6401</onup><onup condition="String.IsEqual(Window(Home).Property(bz_pnoff),1)">6391</onup`
  - `xml/Includes_Bezel.xml` L2956: `<onup condition="[!String.IsEqual(Window(Home).Property(bz_pnoff),1)]">6401</onup><onup condition="String.IsEqual(Window(Home).Property(bz_pnoff),1)">6391</onup`

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

### `bz_pnsel`
- set/clear sites: 2 · read sites: 1
  - `xml/Custom_1120_PlayNext.xml` L10: `<onload condition="String.IsEmpty(Skin.String(bz_dfs_mode))">Skin.SetString(bz_dfs_mode,album)</onload><!-- 5.33.109: pill defaults to album --><onunload>ClearP`
  - `xml/Custom_1120_PlayNext.xml` L19: `<onfocus>ClearProperty(bz_pnfoc,home)</onfocus><onclick condition="!Player.Paused">SetProperty(bz_pnfoc,6403,home)</onclick><onclick condition="Player.Paused">C`
  - `xml/Includes_Bezel.xml` L1038: `<!-- 5.33.107 t721: mirrored sway removed; 1120 overlay visuals live in BezelMusicPlayingArt sway group (BzPN107) --><control type="group"><left>660</left><top>`

### `bz_pvret`
- set/clear sites: 4 · read sites: 0
  - `xml/Custom_1120_PlayNext.xml` L10: `<onload condition="String.IsEmpty(Skin.String(bz_dfs_mode))">Skin.SetString(bz_dfs_mode,album)</onload><!-- 5.33.109: pill defaults to album --><onunload>ClearP`
  - `xml/Custom_1120_PlayNext.xml` L10: `<onload condition="String.IsEmpty(Skin.String(bz_dfs_mode))">Skin.SetString(bz_dfs_mode,album)</onload><!-- 5.33.109: pill defaults to album --><onunload>ClearP`
  - `xml/Custom_1120_PlayNext.xml` L10: `<onload condition="String.IsEmpty(Skin.String(bz_dfs_mode))">Skin.SetString(bz_dfs_mode,album)</onload><!-- 5.33.109: pill defaults to album --><onunload>ClearP`

