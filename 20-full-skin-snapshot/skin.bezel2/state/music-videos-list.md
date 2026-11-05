# Music videos list — music-videos-list

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `music-videos-list` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-videos-list.md) · [layout](../layout/music-videos-list.md) · [state](../state/music-videos-list.md) · [motion](../motion/music-videos-list.md) · [art](../art/music-videos-list.md) · [input](../input/music-videos-list.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_allret`
- set/clear sites: 3 · read sites: 1
  - `scripts/bz_cmd.py` L561: `xbmcgui.Window(10000).setProperty('bz_allret', fp)  # 5.33.95: Back from All lands on the ALL row, not the parked Disc 2`
  - `scripts/bz_flip.py` L318: `home.clearProperty('bz_allret'); xbmc.executebuiltin('SetFocus(%d)' % _ab); sw_prev[0] = 0; sw_path[0] = _fp`
  - `scripts/bz_flip.py` L321: `elif _ar and _fp != _ar and '/-1/' not in _fp: home.clearProperty('bz_allret')`
  - `scripts/bz_flip.py` L316: `_ar = home.getProperty('bz_allret')`

### `bz_allrow`
- set/clear sites: 0 · read sites: 4
  - `xml/Includes_Bezel.xml` L101: `<!-- ALLROW (Rob t3729/t3730): stock All hidden (showallitems off), bottom row opens the same All path --><!-- 5.0.3 t3972 --><variable name="BzListHiText"><val`
  - `xml/Includes_Bezel.xml` L104: `<expression name="bz_mdiscpick">Window.IsActive(music) + String.StartsWith(Container.FolderPath,musicdb://albums/) + !String.IsEqual(Container.FolderPath,musicd`
  - `xml/Includes_Bezel.xml` L2196: `</control></control><!-- t4533 end clip --><control type="button" id="6097"><!-- ALLROW --><visible>!$EXP[bz_covercol] | $EXP[bz_allpick]</visible><animation ef`

### `bz_allup`
- set/clear sites: 2 · read sites: 8
  - `scripts/bz_flip.py` L334: `if _prev and _prev > _pos and xbmc.getCondVisibility('Control.IsVisible(6097)'): home.setProperty('bz_allup', str(_n)); xbmc.executebuiltin('SetFocus(6097)')  #`
  - `scripts/bz_flip.py` L338: `if _prev and _prev > _pos and xbmc.getCondVisibility('Control.IsVisible(6098)'): home.setProperty('bz_allup', str(_n)); xbmc.executebuiltin('SetFocus(6098)')  #`
  - `xml/Includes_Bezel.xml` L2196: `</control></control><!-- t4533 end clip --><control type="button" id="6097"><!-- ALLROW --><visible>!$EXP[bz_covercol] | $EXP[bz_allpick]</visible><animation ef`
  - `xml/Includes_Bezel.xml` L2196: `</control></control><!-- t4533 end clip --><control type="button" id="6097"><!-- ALLROW --><visible>!$EXP[bz_covercol] | $EXP[bz_allpick]</visible><animation ef`
  - `xml/Includes_Bezel.xml` L2196: `</control></control><!-- t4533 end clip --><control type="button" id="6097"><!-- ALLROW --><visible>!$EXP[bz_covercol] | $EXP[bz_allpick]</visible><animation ef`

### `bz_atnavroot`
- set/clear sites: 3 · read sites: 1
  - `scripts/bz_flip.py` L961: `if fp not in ROOTS: home.setProperty('bz_atnavroot', 'true')`
  - `scripts/bz_flip.py` L963: `if home.getProperty('bz_atnavroot'): home.clearProperty('bz_atnavroot')`
  - `scripts/bz_flip.py` L963: `if home.getProperty('bz_atnavroot'): home.clearProperty('bz_atnavroot')`
  - `xml/Includes_Bezel.xml` L2372: `<expression name="bz_atroot">String.IsEqual(Window(Home).Property(bz_rootarm),true) + ![String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Co`

### `bz_atroot`
- set/clear sites: 0 · read sites: 5
  - `xml/Includes_Bezel.xml` L1594: `<onback condition="String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Container.FolderPath,sources://)">ActivateWindow(1117)</onback><onback `
  - `xml/Includes_Bezel.xml` L1594: `<onback condition="String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Container.FolderPath,sources://)">ActivateWindow(1117)</onback><onback `
  - `xml/Includes_Bezel.xml` L2372: `<expression name="bz_atroot">String.IsEqual(Window(Home).Property(bz_rootarm),true) + ![String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Co`

### `bz_bottomedge`
- set/clear sites: 1 · read sites: 1
  - `xml/Includes_Bezel.xml` L2699: `<onup>SetProperty(bz_topedge,1,home)</onup><ondown condition="Control.IsVisible(6098)">6098</ondown><!-- t4357: numeric nav = no native wrap flash --><ondown>Se`
  - `xml/Includes_Bezel.xml` L1570: `<onright condition="$EXP[bz_artbtn] + Container.Content(songs) + [!Player.HasAudio | !Control.IsVisible(6160)]">SetFocus(6095)</onright><onright condition="$EXP`

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_flip`
- set/clear sites: 1 · read sites: 69
  - `xml/MyVideoNav.xml` L23: `<onload condition="Skin.HasSetting(bz_grid_video)">SetProperty(bz_gpend,1,home)</onload><onload>AlarmClock(bzgpend,ClearProperty(bz_gpend,home),00:02,silent)</o`
  - `xml/MyPlaylist.xml` L9: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L14: `<!-- BETA 1.1b: the gate below uses Player.HasAudio directly (the debounced bz_audio_latch from bz_flip.py may not be set yet on the first Tab after Kodi start;`

### `bz_mm`
- set/clear sites: 0 · read sites: 12
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_msret`
- set/clear sites: 1 · read sites: 22
  - `xml/Custom_1117_MediaSources.xml` L6: `<onload>ClearProperty(bz_msret,home)</onload><onload condition="!String.IsEmpty(Window(Home).Property(bz_msfocus))">AlarmClock(bzmsf,SetFocus($INFO[Window(Home)`
  - `xml/Custom_1132_BzSources.xml` L10: `<control type="list" id="9150"><left>0</left><top>112</top><width>390</width><height>720</height><orientation>vertical</orientation><scrolltime tween="cubic" ea`
  - `xml/Includes_Bezel.xml` L1594: `<onback condition="String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Container.FolderPath,sources://)">ActivateWindow(1117)</onback><onback `
  - `xml/Includes_Bezel.xml` L1594: `<onback condition="String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Container.FolderPath,sources://)">ActivateWindow(1117)</onback><onback `

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

### `bz_navgrace`
- set/clear sites: 5 · read sites: 4
  - `scripts/bz_cmd.py` L648: `home.clearProperty('bz_navgrace'); home.setProperty('bz_mmstart', '1'); home.setProperty('bz_nav', 'true')`
  - `scripts/bz_cmd.py` L671: `home.clearProperty('bz_navgrace'); home.setProperty('bz_mmstart', '1'); home.setProperty('bz_nav', 'true')`
  - `scripts/bz_flip.py` L1007: `if nav_was[0] and not nv: home.setProperty('bz_navgrace', 'true'); navgr[0] = now`
  - `xml/Includes_Bezel.xml` L414: `<expression name="bz_navok">String.IsEmpty(Window(Home).Property(bz_navlock)) + String.IsEmpty(Window(Home).Property(bz_navgrace)) + !String.IsEqual(Window(Home`
  - `scripts/bz_flip.py` L1003: `if not nv and not home.getProperty('bz_navgrace') and not home.getProperty('bz_navlock'):`
  - `scripts/bz_flip.py` L1005: `# BEZEL 3.0: one close routine. Any close sets bz_navgrace (0.5 s lock + 0.3 s grace); every open path checks $EXP[bz_navok],`

### `bz_navlock`
- set/clear sites: 1 · read sites: 6
  - `scripts/bz_flip.py` L815: `elif now - navlk[0] >= 0.25: home.clearProperty('bz_navlock'); navlk[0] = 0.0`
  - `xml/Includes_Bezel.xml` L414: `<expression name="bz_navok">String.IsEmpty(Window(Home).Property(bz_navlock)) + String.IsEmpty(Window(Home).Property(bz_navgrace)) + !String.IsEqual(Window(Home`
  - `scripts/bz_flip.py` L812: `# BETA 1.3: slide menu: Up / Down set bz_navlock (XML); further presses are ignored until the bar glide (280 ms) is done`
  - `scripts/bz_flip.py` L813: `if home.getProperty('bz_navlock'):`

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

### `bz_navroot`
- set/clear sites: 7 · read sites: 23
  - `scripts/bz_mm.py` L17: `'music': ['SetProperty(bz_navroot,musicdb://albums/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,tomusic,musicdb://albums/)'],`
  - `scripts/bz_mm.py` L18: `'movies': ['SetProperty(bz_navroot,videodb://movies/titles/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,go,videodb://movies/titles/)'],`
  - `scripts/bz_mm.py` L19: `'tv': ['SetProperty(bz_navroot,videodb://tvshows/titles/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,go,videodb://tvshows/titles/)'],`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`

### `bz_navtune`
- set/clear sites: 21 · read sites: 45
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_rootarm`
- set/clear sites: 2 · read sites: 3
  - `scripts/bz_flip.py` L956: `rp[0] = fp; rp[1] = now - (0.6 if _fresh else 0); rp[2] = _wid; home.clearProperty('bz_rootarm')`
  - `scripts/bz_flip.py` L960: `home.setProperty('bz_rootarm', 'true')`
  - `xml/Includes_Bezel.xml` L2372: `<expression name="bz_atroot">String.IsEqual(Window(Home).Property(bz_rootarm),true) + ![String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Co`
  - `scripts/bz_flip.py` L950: `# (bz_rootarm = that path) before Back counts, so the Back that lands on the top level never opens it`
  - `scripts/bz_flip.py` L958: `elif now - rp[1] >= 0.6 and (fp in ROOTS or (home.getProperty('bz_navroot') and fp.rstrip('/') == home.getProperty('bz_navroot').rstrip('/'))) and home.getPrope`

### `bz_topedge`
- set/clear sites: 1 · read sites: 3
  - `xml/Includes_Bezel.xml` L2699: `<onup>SetProperty(bz_topedge,1,home)</onup><ondown condition="Control.IsVisible(6098)">6098</ondown><!-- t4357: numeric nav = no native wrap flash --><ondown>Se`
  - `xml/Includes_Bezel.xml` L1568: `<control type="grouplist"><!-- t4533: TRUE CLIP for list 60. A grouplist scissors its children to its own rect (bz_list_x,bz_top 450x900 = bottom y1020); the co`
  - `xml/Includes_Bezel.xml` L1570: `<onright condition="$EXP[bz_artbtn] + Container.Content(songs) + [!Player.HasAudio | !Control.IsVisible(6160)]">SetFocus(6095)</onright><onright condition="$EXP`
  - `xml/Includes_Bezel.xml` L2693: `<control type="grouplist"><animation effect="slide" end="0,450" time="0" condition="$EXP[bz_actcov]">Conditional</animation><!-- t4464 actors cover column --><o`

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

