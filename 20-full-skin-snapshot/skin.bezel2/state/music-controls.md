# Music controls (dialog 1115) — music-controls

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `music-controls` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-controls.md) · [layout](../layout/music-controls.md) · [state](../state/music-controls.md) · [motion](../motion/music-controls.md) · [art](../art/music-controls.md) · [input](../input/music-controls.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
The music controls panel is the "remote control" menu for music: play/pause, skip, shuffle, repeat, Up next, choose a visualisation, tweak its settings, or jump to the Tuner. It opens automatically when Kodi would show its music OSD, and from the fan art pill or the music list. Left always closes it.

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

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_fssh_off`
- set/clear sites: 2 · read sites: 16
  - `xml/Includes_Tuner.xml` L1319: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),fs_ttl)">Skin.SetBool(bz_fs_ttl_off)</onleft><onright condition="String.IsEqual(Containe`
  - `xml/Includes_Tuner.xml` L1319: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),fs_ttl)">Skin.SetBool(bz_fs_ttl_off)</onleft><onright condition="String.IsEqual(Containe`
  - `xml/Custom_1115_MusicControls.xml` L12: `<control type="label"><!-- 5.33.49 t316 soft shadow --><visible>!Skin.HasSetting(bz_fssh_off)</visible><!-- 5.33.57 Drop shadow pill hard off --><include>BzFSSh`
  - `xml/Custom_1115_MusicControls.xml` L13: `<control type="label"><!-- 5.33.49 t316 soft shadow --><visible>!Skin.HasSetting(bz_fssh_off)</visible><!-- 5.33.57 Drop shadow pill hard off --><include>BzFSSh`
  - `xml/Custom_1115_MusicControls.xml` L14: `<control type="label"><!-- 5.33.49 t316 soft shadow --><visible>!Skin.HasSetting(bz_fssh_off)</visible><!-- 5.33.57 Drop shadow pill hard off --><include>BzFSSh`

### `bz_nav`
- set/clear sites: 75 · read sites: 103
  - `xml/Custom_1107_SearchDialog.xml` L23: `<control type="list" id="9000"><onback>SetProperty(bz_nav,true,home)</onback><onback>Dialog.Close(1107,true)</onback><!-- 5.33.235 Rob t1837: control onback con`
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Custom_1112_NowPlaying.xml` L15: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L16: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L17: `<onload condition="[String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visualis`

### `bz_navtune`
- set/clear sites: 21 · read sites: 45
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_npm_ctl`
- set/clear sites: 1 · read sites: 11
  - `xml/Custom_1121_MusicFanartFS.xml` L35: `<onclick condition="$EXP[bz_npm_ctl]">ActivateWindow(1115)</onclick><onclick condition="$EXP[bz_npm_vis]">Skin.SetString(bz_npmode,bio)</onclick><onclick condit`
  - `xml/Includes_Bezel.xml` L351: `<expression name="bz_npm_ctl">String.IsEqual(Skin.String(bz_npmode),controls)</expression><!-- 4.0.1 O16 -->`
  - `xml/Includes_Bezel.xml` L2826: `<variable name="BezelNPModeName"><value condition="Window.IsActive(1115)">CONTROLS</value><value condition="$EXP[bz_npm_ctl]">CONTROLS  ▾</value><value conditio`
  - `xml/Includes_Bezel.xml` L2826: `<variable name="BezelNPModeName"><value condition="Window.IsActive(1115)">CONTROLS</value><value condition="$EXP[bz_npm_ctl]">CONTROLS  ▾</value><value conditio`

### `bz_npmode`
- set/clear sites: 12 · read sites: 16
  - `xml/Includes_Bezel.xml` L3027: `<onclick condition="!$EXP[bz_npm_bio]">SetProperty(bz_npinfo_prev,$INFO[Skin.String(bz_npmode)],home)</onclick>`
  - `xml/Includes_Bezel.xml` L3028: `<onclick condition="!$EXP[bz_npm_bio]">Skin.SetString(bz_npmode,bio)</onclick>`
  - `xml/Includes_Bezel.xml` L3029: `<onclick condition="$EXP[bz_npm_bio] + !String.IsEmpty(Window(Home).Property(bz_npinfo_prev))">Skin.SetString(bz_npmode,$INFO[Window(Home).Property(bz_npinfo_pr`
  - `xml/Includes_Bezel.xml` L347: `<expression name="bz_npm_vis">String.IsEqual(Skin.String(bz_npmode),vis) | String.IsEmpty(Skin.String(bz_npmode))</expression>`
  - `xml/Includes_Bezel.xml` L347: `<expression name="bz_npm_vis">String.IsEqual(Skin.String(bz_npmode),vis) | String.IsEmpty(Skin.String(bz_npmode))</expression>`
  - `xml/Includes_Bezel.xml` L348: `<expression name="bz_npm_bio">String.IsEqual(Skin.String(bz_npmode),bio)</expression>`

### `bz_pndlg_off`
- set/clear sites: 1 · read sites: 1
  - `xml/Custom_1120_PlayNext.xml` L7: `REMOVE: delete this file + the 6390 onright condition bz_pndlg_ok + the two "5.33.65 Dialogue FS dialog slide" animations. Tuner off: Skin.SetBool(bz_pndlg_off)`
  - `xml/Includes_Bezel.xml` L335: `<expression name="bz_pndlg_ok">!Skin.HasSetting(bz_pndlg_off) + Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !Window.IsActive(visualisation) + `

### `bz_pndlg_ok`
- set/clear sites: 8 · read sites: 104
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L335: `<expression name="bz_pndlg_ok">!Skin.HasSetting(bz_pndlg_off) + Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !Window.IsActive(visualisation) + `
  - `xml/Includes_Bezel.xml` L1371: `<!-- 5.33.221: touch tap big album = Dialogue FS (same as 6390 remote) --><onclick condition="$EXP[bz_pndlg_ok] + String.IsEqual(Skin.String(bz_at_fsslide),1)">`
  - `xml/Includes_Bezel.xml` L1371: `<!-- 5.33.221: touch tap big album = Dialogue FS (same as 6390 remote) --><onclick condition="$EXP[bz_pndlg_ok] + String.IsEqual(Skin.String(bz_at_fsslide),1)">`

### `bz_tunesrc`
- set/clear sites: 16 · read sites: 3
  - `xml/Custom_1118_PowerMenu.xml` L8: `<onload>ClearProperty(bz_tunesrc,home)</onload><onload>SetProperty(bz_pwrswap,1,home)</onload><!-- t4943 K52: skip 6996 slides on POWER swap -->`
  - `xml/Custom_1118_PowerMenu.xml` L26: `<item><label>TUNER</label><onclick>SetProperty(bz_tunesrc,pwr,home)</onclick><onclick>SetProperty(bz_navtune,true,home)</onclick><onclick>ClearProperty(bz_navbe`
  - `xml/Custom_1130_BzSettings.xml` L51: `<item><label>WARM 2.0.1 · TUNER</label><property name="kind">m</property><property name="lvl">sub</property><onclick>SetProperty(bz_tunesrc,set,home)</onclick><`
  - `xml/Custom_1118_PowerMenu.xml` L10: `<onunload condition="!String.IsEqual(Window(Home).Property(bz_tunesrc),pwr)">AlarmClock(bzpwrf,SetFocus(6996),00:00,silent,false)</onunload>`
  - `xml/Custom_1130_BzSettings.xml` L102: `<control type="group"><visible>String.IsEqual(ListItem.Property(kind),p)</visible><animation effect="fade" start="100" end="70" time="0" condition="String.IsEqu`
  - `xml/Custom_1115_MusicControls.xml` L40: `<control type="group"><top>766</top><control type="image"><left>12</left><top>4</top><width>366</width><height>48</height><texture border="23" colordiffuse="E6F`

### `bz_tunf`
- set/clear sites: 0 · read sites: 1
  - `xml/Custom_1115_MusicControls.xml` L40: `<control type="group"><top>766</top><control type="image"><left>12</left><top>4</top><width>366</width><height>48</height><texture border="23" colordiffuse="E6F`

### `bz_vback`
- set/clear sites: 11 · read sites: 34
  - `xml/Includes_Bezel.xml` L645: `<onclick condition="!$EXP[bz_np] + !String.IsEmpty(Window(Home).Property(bz_vback))">SetProperty(bz_vback_close,true,home)</onclick>`
  - `xml/Includes_Bezel.xml` L646: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !String.IsEmpty(Window(Home).Property(bz_back))">SetProperty(bz_back_clos`
  - `xml/Includes_Bezel.xml` L1584: `<onleft condition="!String.IsEmpty(Window(Home).Property(bz_vback))">SetProperty(bz_vback_close,true,home)</onleft>`
  - `xml/Includes_Bezel.xml` L565: `Tap: flips to the info back (bz_vback). Mini player: the whole poster scales to 90% about its bottom edge so it sits under the bar. -->`
  - `xml/Includes_Bezel.xml` L647: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !!String.IsEmpty(Window(Home).Property(bz_back)) + Control.IsVisible(60)"`
  - `xml/Includes_Bezel.xml` L648: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !!String.IsEmpty(Window(Home).Property(bz_back)) + !Control.IsVisible(60)`

### `bz_vizset`
- set/clear sites: 1 · read sites: 39
  - `xml/Custom_1115_MusicControls.xml` L3: `<onunload>ClearProperty(bz_vizset)</onunload><onunload condition="String.IsEqual(Skin.String(bz_npmode),controls)">Skin.SetString(bz_npmode,vis)</onunload><!-- `
  - `xml/Custom_1115_MusicControls.xml` L38: `<!-- t231: Viz settings row = Kodi visualisation add-on settings --><control type="group"><top>710</top><control type="image"><left>12</left><top>4</top><width>`
  - `xml/Custom_1115_MusicControls.xml` L38: `<!-- t231: Viz settings row = Kodi visualisation add-on settings --><control type="group"><top>710</top><control type="image"><left>12</left><top>4</top><width>`
  - `xml/Custom_1115_MusicControls.xml` L43: `<!-- 5.33.27 t236 Rob: Viz settings page lives inside Player Controls (replace-parent on the colour strip, no anim). Values via scripts/bz_vizset.py -->`

### `bz_vs`
- set/clear sites: 4 · read sites: 0
  - `scripts/bz_vizset.py` L36: `w.setProperty('bz_vs%d_lab' % i, r['lab']); w.setProperty('bz_vs%d_val' % i, txt)`
  - `scripts/bz_vizset.py` L36: `w.setProperty('bz_vs%d_lab' % i, r['lab']); w.setProperty('bz_vs%d_val' % i, txt)`
  - `scripts/bz_vizset.py` L38: `w.clearProperty('bz_vs%d_lab' % i); w.clearProperty('bz_vs%d_val' % i)`

### `bz_vs_n`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_vizset.py` L29: `w.setProperty('bz_vs_n', str(len(rs)))`
  - `scripts/bz_vizset.py` L42: `w.setProperty('bz_vs_n', '0'); w.setProperty('bz_vs_name', 'None'); return`
  - `xml/Custom_1115_MusicControls.xml` L47: `<control type="label"><left>28</left><top>66</top><width>330</width><height>56</height><aligny>center</aligny><font>bz_mm20</font><textcolor>B4FFFFFF</textcolor`

### `bz_vs_name`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_vizset.py` L42: `w.setProperty('bz_vs_n', '0'); w.setProperty('bz_vs_name', 'None'); return`
  - `scripts/bz_vizset.py` L44: `w.setProperty('bz_vs_name', a.getAddonInfo('name'))`
  - `xml/Custom_1115_MusicControls.xml` L46: `<control type="label"><left>28</left><top>38</top><width>330</width><height>26</height><aligny>center</aligny><font>bz_mm14</font><textcolor>B4FFFFFF</textcolor`

