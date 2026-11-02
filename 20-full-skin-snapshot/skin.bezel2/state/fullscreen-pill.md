# Fullscreen pill (Music list) — fullscreen-pill

**Object:** `fullscreen-pill` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/fullscreen-pill.md) · [layout](../layout/fullscreen-pill.md) · [state](../state/fullscreen-pill.md) · [motion](../motion/fullscreen-pill.md) · [art](../art/fullscreen-pill.md) · [input](../input/fullscreen-pill.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
A small FULLSCREEN pill shows on the Music list while music plays. Select opens full-screen music (Fanart FS).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_b15`
- set/clear sites: 1 · read sites: 15
  - `xml/Includes_Bezel.xml` L997: `<control type="button" id="6401"><width>auto</width><height>32</height><label>$VAR[BezelDFSModeName]</label><onfocus>ClearProperty(bz_pnfoc,home)</onfocus><font`
  - `xml/Includes_Bezel.xml` L2268: `<control type="button" id="6886"><width>auto</width><height>32</height><label>FULLSCREEN</label><font>bz_b15</font><textoffsetx>16</textoffsetx><align>center</a`
  - `xml/Includes_Bezel.xml` L3005: `<control type="grouplist"><!-- 5.33.48 cycle pill live shadow --><include>BzFSShSlide</include><!-- 5.33.49 soft L1 centre --><left>530</left><top>130</top><wid`
  - `xml/Includes_Bezel.xml` L3005: `<control type="grouplist"><!-- 5.33.48 cycle pill live shadow --><include>BzFSShSlide</include><!-- 5.33.49 soft L1 centre --><left>530</left><top>130</top><wid`

### `bz_fsret`
- set/clear sites: 6 · read sites: 14
  - `xml/Includes_Bezel.xml` L1002: `<onback condition="String.IsEqual($PARAM[back_close],1)">SetProperty(bz_fsret,true,home)</onback><onback condition="String.IsEqual($PARAM[back_close],1)">AlarmC`
  - `xml/Includes_Bezel.xml` L1002: `<onback condition="String.IsEqual($PARAM[back_close],1)">SetProperty(bz_fsret,true,home)</onback><onback condition="String.IsEqual($PARAM[back_close],1)">AlarmC`
  - `xml/Custom_1120_PlayNext.xml` L21: `<onback>SetProperty(bz_fsret,true,home)</onback><onback>AlarmClock(bz_fsretclr,ClearProperty(bz_fsret,home),00:01,silent)</onback><onback>Dialog.Close(1120)</on`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`

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

### `bz_pnoff`
- set/clear sites: 25 · read sites: 70
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`

