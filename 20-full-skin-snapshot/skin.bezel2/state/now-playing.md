# Now playing (dialog 1112) — now-playing

**Object:** `now-playing` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/now-playing.md) · [layout](../layout/now-playing.md) · [state](../state/now-playing.md) · [motion](../motion/now-playing.md) · [art](../art/now-playing.md) · [input](../input/now-playing.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

**See screen:** [now-playing baselines](../port-refs/now-playing/) — smoke baseline + port diff target.

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

### `bz_back`
- set/clear sites: 4 · read sites: 27
  - `xml/Includes_Bezel.xml` L646: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !String.IsEmpty(Window(Home).Property(bz_back))">SetProperty(bz_back_clos`
  - `xml/MyMusicNav.xml` L13: `<onload>ClearProperty(bz_back,home)</onload>`
  - `scripts/bz_flip.py` L279: `home.clearProperty('bz_back'); on = False`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L455: `<visible>Player.HasAudio + !String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_back_fade))</visible>`
  - `xml/Includes_Bezel.xml` L647: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !!String.IsEmpty(Window(Home).Property(bz_back)) + Control.IsVisible(60)"`

### `bz_backanim`
- set/clear sites: 3 · read sites: 19
  - `xml/MyMusicNav.xml` L14: `<onload>ClearProperty(bz_backanim,home)</onload>`
  - `scripts/bz_flip.py` L284: `home.clearProperty('bz_backanim'); home.clearProperty('bz_back_fade'); closed_at = None`
  - `scripts/bz_flip.py` L1600: `for k in ('bz_back', 'bz_backanim', 'bz_back_pick', 'bz_albumid', 'bz_pswayon', 'bz_ppulse', 'bz_ppulse2', 'bz_pready', 'bz_vreq', 'bz_sway_pulse2', 'bz_castL',`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L1131: `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="!String.IsEmpty(Window(Home).Property(bz_back)) | !String.IsEmpty`
  - `xml/Includes_Bezel.xml` L1141: `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="!String.IsEmpty(Window(Home).Property(bz_back)) | !String.IsEmpty`

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_flipping`
- set/clear sites: 5 · read sites: 14
  - `scripts/bz_flip.py` L195: `home.setProperty('bz_flipping', 'true'); home.setProperty('bz_sway_hold', 'true')`
  - `scripts/bz_flip.py` L199: `if not sway.get('busy'): home.clearProperty('bz_flipping')`
  - `scripts/bz_flip.py` L1564: `home.setProperty('bz_flipping', 'true')    # v0.1.23: glares fade out (150 ms) before the sway is held`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L1131: `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="!String.IsEmpty(Window(Home).Property(bz_back)) | !String.IsEmpty`
  - `xml/Includes_Bezel.xml` L1141: `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="!String.IsEmpty(Window(Home).Property(bz_back)) | !String.IsEmpty`

### `bz_fsnp`
- set/clear sites: 5 · read sites: 2
  - `xml/MusicVisualisation.xml` L11: `<onload>SetProperty(bz_fsnp,true,home)</onload>`
  - `xml/MusicVisualisation.xml` L16: `<onunload condition="String.IsEqual(Window(Home).Property(bz_fsnp),true)">ClearProperty(bz_np,home)</onunload>`
  - `xml/MusicVisualisation.xml` L17: `<onunload condition="!$EXP[bz_navmenu]">AlarmClock(bz_vizret,SetFocus(60),00:00,silent)</onunload><!-- 5.33.112 t786: Play Next / viz exit -> section list 60 --`
  - `xml/Includes_Bezel.xml` L2801: `<expression name="bz_np">String.IsEqual(Window(Home).Property(bz_np),true) + [Window.IsActive(music) | String.IsEqual(Window(Home).Property(bz_fsnp),true)] + St`
  - `xml/MusicVisualisation.xml` L21: `<visible>String.IsEqual(Window(Home).Property(bz_fsnp),true)</visible>`

### `bz_fsret`
- set/clear sites: 6 · read sites: 14
  - `xml/Includes_Bezel.xml` L1002: `<onback condition="String.IsEqual($PARAM[back_close],1)">SetProperty(bz_fsret,true,home)</onback><onback condition="String.IsEqual($PARAM[back_close],1)">AlarmC`
  - `xml/Includes_Bezel.xml` L1002: `<onback condition="String.IsEqual($PARAM[back_close],1)">SetProperty(bz_fsret,true,home)</onback><onback condition="String.IsEqual($PARAM[back_close],1)">AlarmC`
  - `xml/Custom_1120_PlayNext.xml` L21: `<onback>SetProperty(bz_fsret,true,home)</onback><onback>AlarmClock(bz_fsretclr,ClearProperty(bz_fsret,home),00:01,silent)</onback><onback>Dialog.Close(1120)</on`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`

### `bz_nav`
- set/clear sites: 75 · read sites: 103
  - `xml/Custom_1107_SearchDialog.xml` L23: `<control type="list" id="9000"><onback>SetProperty(bz_nav,true,home)</onback><onback>Dialog.Close(1107,true)</onback><!-- 5.33.235 Rob t1837: control onback con`
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Custom_1112_NowPlaying.xml` L15: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L16: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L17: `<onload condition="[String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visualis`

### `bz_navbez`
- set/clear sites: 18 · read sites: 36
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_navtune`
- set/clear sites: 21 · read sites: 45
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_np`
- set/clear sites: 33 · read sites: 98
  - `xml/Custom_1112_NowPlaying.xml` L19: `<onunload condition="!Window.IsActive(visualisation)">ClearProperty(bz_np,home)</onunload>`
  - `xml/Custom_1112_NowPlaying.xml` L42: `<onclick>ClearProperty(bz_np,home)</onclick><onclick>Dialog.Close(1112)</onclick></control>`
  - `xml/Custom_1112_NowPlaying.xml` L44: `<control type="button" id="6299"><left>-400</left><top>0</top><width>10</width><height>10</height><label></label><texturefocus></texturefocus><texturenofocus></`
  - `xml/Custom_1112_NowPlaying.xml` L3: `list view (view 60, not the grid): bz_cmd.py np (logo menu entry, 60 s idle open) sets bz_npdlg + bz_np and opens it. Every other route keeps the in-place panel`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L13: `and run Kodi's fullscreen music window (the old route). Opened by bz_cmd.py (menu card, idle) bz_np is already set. -->`

### `bz_np_focus`
- set/clear sites: 1 · read sites: 1
  - `xml/MyMusicNav.xml` L26: `<onload>ClearProperty(bz_np_focus,home)</onload>`
  - `xml/MyMusicNav.xml` L25: `<onload condition="String.IsEqual(Window(Home).Property(bz_np_focus),true)">SetFocus(6390)</onload>`

### `bz_np_was`
- set/clear sites: 4 · read sites: 0
  - `xml/MyMusicNav.xml` L20: `<onunload>SetProperty(bz_np_was,$INFO[Window(Home).Property(bz_np)],home)</onunload><!-- 2.0a3.4: Tab toggle -->`
  - `scripts/bz_cmd.py` L121: `home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez'); home.clearProperty('bz_np_was')`
  - `scripts/bz_cmd.py` L284: `home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez'); home.clearProperty('bz_np_was')`

### `bz_npctl`
- set/clear sites: 2 · read sites: 10
  - `xml/MusicVisualisation.xml` L46: `<!-- 5.33.205: 6409 touch — onclick=play/pause; ondoubleclick=album viz (ClearProperty bz_pnoff). Keys bounce to 6390 (onfocus). --><control type="button" id="6`
  - `scripts/bz_flip.py` L929: `home.clearProperty('bz_npctl')`
  - `xml/Custom_1112_NowPlaying.xml` L38: `<include content="BezelNPControls"><param name="vis" value="$EXP[bz_np] + String.IsEqual(Window(Home).Property(bz_npctl),true)"/><param name="dx" value="0"/><pa`
  - `xml/Includes_Bezel.xml` L2285: `<include content="BezelNPControls"><param name="vis" value="[$EXP[bz_np] + String.IsEqual(Window(Home).Property(bz_npctl),true)] | [!$EXP[bz_np] + !String.IsEmp`
  - `xml/Includes_Bezel.xml` L2962: `<visible>!String.IsEqual(Window(Home).Property(bz_npctl),true)</visible><!-- 3.5.1: tap the bottom of the panel (left half only) shows the player controls -->`

### `bz_npdlg`
- set/clear sites: 3 · read sites: 14
  - `xml/Custom_1112_NowPlaying.xml` L20: `<onunload>ClearProperty(bz_npdlg,home)</onunload>`
  - `scripts/bz_cmd.py` L123: `home.setProperty('bz_npdlg', 'true'); home.setProperty('bz_np', 'true')`
  - `scripts/bz_cmd.py` L288: `home.setProperty('bz_npdlg', 'true'); home.setProperty('bz_np', 'true')`
  - `xml/Custom_1112_NowPlaying.xml` L3: `list view (view 60, not the grid): bz_cmd.py np (logo menu entry, 60 s idle open) sets bz_npdlg + bz_np and opens it. Every other route keeps the in-place panel`
  - `xml/Custom_1112_NowPlaying.xml` L17: `<onload condition="[String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visualis`
  - `xml/Includes_Bezel.xml` L55: `<expression name="bz_fpop_a">Skin.HasSetting(bz_fs_fanartpop) + Window.IsActive(visualisation) + String.IsEmpty(Window(Home).Property(bz_npdlg)) + String.IsEqua`

### `bz_pnoff`
- set/clear sites: 25 · read sites: 70
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`

