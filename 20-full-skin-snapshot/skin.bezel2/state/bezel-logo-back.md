# BEZEL logo / Back button — bezel-logo-back

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `bezel-logo-back` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/bezel-logo-back.md) · [layout](../layout/bezel-logo-back.md) · [state](../state/bezel-logo-back.md) · [motion](../motion/bezel-logo-back.md) · [art](../art/bezel-logo-back.md) · [input](../input/bezel-logo-back.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
The BEZEL logo sits top-left and takes the skin tint. About every 30 seconds it does one spin.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_back`
- set/clear sites: 4 · read sites: 27
  - `xml/Includes_Bezel.xml` L646: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !String.IsEmpty(Window(Home).Property(bz_back))">SetProperty(bz_back_clos`
  - `xml/MyMusicNav.xml` L13: `<onload>ClearProperty(bz_back,home)</onload>`
  - `scripts/bz_flip.py` L279: `home.clearProperty('bz_back'); on = False`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L455: `<visible>Player.HasAudio + !String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_back_fade))</visible>`
  - `xml/Includes_Bezel.xml` L647: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !!String.IsEmpty(Window(Home).Property(bz_back)) + Control.IsVisible(60)"`

### `bz_back_close`
- set/clear sites: 6 · read sites: 2
  - `xml/Includes_Bezel.xml` L471: `<onup>6185</onup><ondown>6185</ondown><onleft>SetProperty(bz_back_close,true,home)</onleft><onright>6185</onright>`
  - `xml/Includes_Bezel.xml` L472: `<onback>SetProperty(bz_back_close,true,home)</onback><onback condition="Control.IsVisible(60)">60</onback>`
  - `xml/Includes_Bezel.xml` L646: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !String.IsEmpty(Window(Home).Property(bz_back))">SetProperty(bz_back_clos`
  - `scripts/bz_flip.py` L270: `# 2.0a1: closes after 15 s without input (was 6), on Back (bz_back_close) or when the music stops;`
  - `scripts/bz_flip.py` L272: `if on and not home.getProperty('bz_back_fade') and (home.getProperty('bz_back_close') or xbmc.getCondVisibility('System.IdleTime(15)') or not xbmc.getCondVisibi`

### `bz_biglogo_spin`
- set/clear sites: 2 · read sites: 5
  - `scripts/bz_flip.py` L989: `home.clearProperty('bz_biglogo_spin'); biglogo_spin[1] = 0`
  - `scripts/bz_flip.py` L992: `home.setProperty('bz_biglogo_spin', 'true'); biglogo_spin[1] = now; biglogo_spin[0] = now + 30`
  - `xml/Includes_Bezel.xml` L612: `<!-- t4908: Big Logo spin — Conditional rotate −360°, center 60,58, 1100 ms, tween back ease-out when Home bz_biglogo_spin=true; bz_flip pulses every 30s (~1.2s`
  - `xml/Includes_Bezel.xml` L617: `<animation type="Conditional" condition="String.IsEqual(Window(Home).Property(bz_biglogo_spin),true)" reversible="false">`
  - `xml/Includes_Bezel.xml` L658: `<animation type="Conditional" condition="String.IsEqual(Window(Home).Property(bz_biglogo_spin),true)" reversible="false"><effect type="rotate" start="0" end="-3`

### `bz_flip`
- set/clear sites: 1 · read sites: 69
  - `xml/MyVideoNav.xml` L23: `<onload condition="Skin.HasSetting(bz_grid_video)">SetProperty(bz_gpend,1,home)</onload><onload>AlarmClock(bzgpend,ClearProperty(bz_gpend,home),00:02,silent)</o`
  - `xml/MyPlaylist.xml` L9: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L14: `<!-- BETA 1.1b: the gate below uses Player.HasAudio directly (the debounced bz_audio_latch from bz_flip.py may not be set yet on the first Tab after Kodi start;`

### `bz_infoup`
- set/clear sites: 1 · read sites: 109
  - `xml/Includes_Bezel.xml` L2335: `<control type="list" id="63"><onback condition="[String.IsEmpty(Container.FolderPath) | String.IsEqual(Container.FolderPath,sources://pictures/)] + !$EXP[bz_nav`
  - `xml/Includes_Bezel.xml` L44: `<control type="group"><visible>!Window.IsActive(1120) + !Skin.HasSetting(bz_dtap_off) + [Control.IsVisible(60) | Control.IsVisible(63) | [Control.IsVisible(50) `
  - `xml/Includes_Bezel.xml` L361: `<expression name="bz_infoup">Window.IsVisible(movieinformation) | Window.IsVisible(musicinformation) | Window.IsVisible(songinformation) | Window.IsVisible(pict`
  - `xml/Includes_Bezel.xml` L362: `<expression name="bz_lsthide">$EXP[bz_navmenu] | $EXP[bz_infoup]</expression>`

### `bz_nav`
- set/clear sites: 75 · read sites: 103
  - `xml/Custom_1107_SearchDialog.xml` L23: `<control type="list" id="9000"><onback>SetProperty(bz_nav,true,home)</onback><onback>Dialog.Close(1107,true)</onback><!-- 5.33.235 Rob t1837: control onback con`
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Custom_1112_NowPlaying.xml` L15: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L16: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L17: `<onload condition="[String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visualis`

### `bz_navmenu`
- set/clear sites: 9 · read sites: 593
  - `xml/Includes_Bezel.xml` L2335: `<control type="list" id="63"><onback condition="[String.IsEmpty(Container.FolderPath) | String.IsEqual(Container.FolderPath,sources://pictures/)] + !$EXP[bz_nav`
  - `xml/MusicVisualisation.xml` L17: `<onunload condition="!$EXP[bz_navmenu]">AlarmClock(bz_vizret,SetFocus(60),00:00,silent)</onunload><!-- 5.33.112 t786: Play Next / viz exit -> section list 60 --`
  - `xml/FileManager.xml` L14: `<control type="list" id="20"><onback condition="String.IsEmpty(Container(20).FolderPath) + !$EXP[bz_navmenu]">SetProperty(bz_nav,true,home)</onback><!-- 5.33.17`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`

### `bz_navok`
- set/clear sites: 11 · read sites: 11
  - `xml/Includes_Bezel.xml` L579: `<onleft condition="$EXP[bz_navok]">SetProperty(bz_nav,true,home)</onleft><onright>$PARAM[list]</onright>`
  - `xml/Includes_Bezel.xml` L588: `<onleft condition="$EXP[bz_navok]">SetProperty(bz_nav,true,home)</onleft><onleft condition="!$EXP[bz_navok]">noop</onleft><!-- BEZEL 3.0: jump bar Left = guarde`
  - `xml/Includes_Bezel.xml` L588: `<onleft condition="$EXP[bz_navok]">SetProperty(bz_nav,true,home)</onleft><onleft condition="!$EXP[bz_navok]">noop</onleft><!-- BEZEL 3.0: jump bar Left = guarde`
  - `xml/Includes_Bezel.xml` L414: `<expression name="bz_navok">String.IsEmpty(Window(Home).Property(bz_navlock)) + String.IsEmpty(Window(Home).Property(bz_navgrace)) + !String.IsEqual(Window(Home`
  - `xml/Includes_Bezel.xml` L651: `<onright>60</onright><ondown>60</ondown><!-- 3.0.2 slide-menu loop fix: Down on the logo no longer opens the menu (focus only lands here by itself during fast l`
  - `xml/Includes_Bezel.xml` L1594: `<onback condition="String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Container.FolderPath,sources://)">ActivateWindow(1117)</onback><onback `

### `bz_np`
- set/clear sites: 33 · read sites: 98
  - `xml/Custom_1112_NowPlaying.xml` L19: `<onunload condition="!Window.IsActive(visualisation)">ClearProperty(bz_np,home)</onunload>`
  - `xml/Custom_1112_NowPlaying.xml` L42: `<onclick>ClearProperty(bz_np,home)</onclick><onclick>Dialog.Close(1112)</onclick></control>`
  - `xml/Custom_1112_NowPlaying.xml` L44: `<control type="button" id="6299"><left>-400</left><top>0</top><width>10</width><height>10</height><label></label><texturefocus></texturefocus><texturenofocus></`
  - `xml/Custom_1112_NowPlaying.xml` L3: `list view (view 60, not the grid): bz_cmd.py np (logo menu entry, 60 s idle open) sets bz_npdlg + bz_np and opens it. Every other route keeps the in-place panel`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L13: `and run Kodi's fullscreen music window (the old route). Opened by bz_cmd.py (menu card, idle) bz_np is already set. -->`

### `bz_pc_img`
- set/clear sites: 3 · read sites: 2
  - `scripts/bz_precache.py` L33: `home.setProperty('bz_pc_img', u)`
  - `scripts/bz_precache.py` L37: `home.clearProperty('bz_pc_img')`
  - `scripts/bz_precache.py` L41: `if not mon.abortRequested(): home.clearProperty('bz_pc_img'); home.clearProperty('bz_precache_running')   # BEZEL 3.0 exit fix`
  - `xml/Includes_Bezel.xml` L638: `<control type="image"><left>0</left><top>1079</top><width>1</width><height>1</height><texture background="true" colordiffuse="01FFFFFF">$INFO[Window(Home).Prope`
  - `xml/Includes_Bezel.xml` L638: `<control type="image"><left>0</left><top>1079</top><width>1</width><height>1</height><texture background="true" colordiffuse="01FFFFFF">$INFO[Window(Home).Prope`

### `bz_vback`
- set/clear sites: 11 · read sites: 34
  - `xml/Includes_Bezel.xml` L645: `<onclick condition="!$EXP[bz_np] + !String.IsEmpty(Window(Home).Property(bz_vback))">SetProperty(bz_vback_close,true,home)</onclick>`
  - `xml/Includes_Bezel.xml` L646: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !String.IsEmpty(Window(Home).Property(bz_back))">SetProperty(bz_back_clos`
  - `xml/Includes_Bezel.xml` L1584: `<onleft condition="!String.IsEmpty(Window(Home).Property(bz_vback))">SetProperty(bz_vback_close,true,home)</onleft>`
  - `xml/Includes_Bezel.xml` L565: `Tap: flips to the info back (bz_vback). Mini player: the whole poster scales to 90% about its bottom edge so it sits under the bar. -->`
  - `xml/Includes_Bezel.xml` L647: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !!String.IsEmpty(Window(Home).Property(bz_back)) + Control.IsVisible(60)"`
  - `xml/Includes_Bezel.xml` L648: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !!String.IsEmpty(Window(Home).Property(bz_back)) + !Control.IsVisible(60)`

### `bz_vback_close`
- set/clear sites: 8 · read sites: 2
  - `xml/Includes_Bezel.xml` L645: `<onclick condition="!$EXP[bz_np] + !String.IsEmpty(Window(Home).Property(bz_vback))">SetProperty(bz_vback_close,true,home)</onclick>`
  - `xml/Includes_Bezel.xml` L1584: `<onleft condition="!String.IsEmpty(Window(Home).Property(bz_vback))">SetProperty(bz_vback_close,true,home)</onleft>`
  - `xml/Includes_Bezel.xml` L1593: `<onback condition="!String.IsEmpty(Window(Home).Property(bz_vback))">SetProperty(bz_vback_close,true,home)</onback>`
  - `scripts/bz_flip.py` L291: `# dialog is open), on Back (bz_vback_close), when the focused title changes or the list is focused again, fading to black first.`
  - `scripts/bz_flip.py` L426: `if (home.getProperty('bz_vback_close') or left or (k or '') != home.getProperty('bz_vback_key') or not vid`

