# Big album pill — big-album-pill

**Object:** `big-album-pill` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/big-album-pill.md) · [layout](../layout/big-album-pill.md) · [state](../state/big-album-pill.md) · [motion](../motion/big-album-pill.md) · [art](../art/big-album-pill.md) · [input](../input/big-album-pill.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
The **big album pill** is the ALBUM ↔ PREV/NEXT mode control. It looks the same, sits in the same place and works the same on Dialogue FS and on full screen album viz. It is **not** the fan art pill (`6391`, fanart-fs.md).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_b15`
- set/clear sites: 1 · read sites: 15
  - `xml/Includes_Bezel.xml` L997: `<control type="button" id="6401"><width>auto</width><height>32</height><label>$VAR[BezelDFSModeName]</label><onfocus>ClearProperty(bz_pnfoc,home)</onfocus><font`
  - `xml/Includes_Bezel.xml` L2268: `<control type="button" id="6886"><width>auto</width><height>32</height><label>FULLSCREEN</label><font>bz_b15</font><textoffsetx>16</textoffsetx><align>center</a`
  - `xml/Includes_Bezel.xml` L3005: `<control type="grouplist"><!-- 5.33.48 cycle pill live shadow --><include>BzFSShSlide</include><!-- 5.33.49 soft L1 centre --><left>530</left><top>130</top><wid`
  - `xml/Includes_Bezel.xml` L3005: `<control type="grouplist"><!-- 5.33.48 cycle pill live shadow --><include>BzFSShSlide</include><!-- 5.33.49 soft L1 centre --><left>530</left><top>130</top><wid`

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

