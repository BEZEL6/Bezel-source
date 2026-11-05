# Favourites — favourites

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `favourites` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/favourites.md) · [layout](../layout/favourites.md) · [state](../state/favourites.md) · [motion](../motion/favourites.md) · [art](../art/favourites.md) · [input](../input/favourites.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
FAVOURITES in the Main Menu opens Kodi Favourites as a BEZEL list with a random backdrop. Back opens the Main Menu.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_atnavroot`
- set/clear sites: 3 · read sites: 1
  - `scripts/bz_flip.py` L961: `if fp not in ROOTS: home.setProperty('bz_atnavroot', 'true')`
  - `scripts/bz_flip.py` L963: `if home.getProperty('bz_atnavroot'): home.clearProperty('bz_atnavroot')`
  - `scripts/bz_flip.py` L963: `if home.getProperty('bz_atnavroot'): home.clearProperty('bz_atnavroot')`
  - `xml/Includes_Bezel.xml` L2372: `<expression name="bz_atroot">String.IsEqual(Window(Home).Property(bz_rootarm),true) + ![String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Co`

### `bz_backdrop`
- set/clear sites: 21 · read sites: 21
  - `xml/MyPlaylist.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/MyPlaylist.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/Settings.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L3048: `<texture colordiffuse="$VAR[BezelBackdropAlpha]">$INFO[Window(Home).Property(bz_backdrop)]</texture>`
  - `xml/Includes_Bezel.xml` L3049: `<visible>String.IsEmpty(Window(Home).Property(bz_npdlg)) + [Skin.HasSetting(bezel_norotate) | String.IsEmpty(Control.GetLabel(9880))] + String.IsEmpty(ListItem.`

### `bz_backdrop_last`
- set/clear sites: 14 · read sites: 1
  - `xml/MyPlaylist.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/MyPlaylist.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/Settings.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `scripts/bz_cmd.py` L83: `cur = home.getProperty('bz_backdrop') or home.getProperty('bz_backdrop_last')  # 4.7.5: cleared on window close`

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_ctx`
- set/clear sites: 0 · read sites: 14
  - `xml/Custom_1119_SecCtx.xml` L45: `<control type="button" id="7904"><label>Favourite</label><onclick>RunScript(special://skin/scripts/bz_ctx.py,fav)</onclick><visible>[Window.IsActive(programs) |`
  - `xml/Custom_1119_SecCtx.xml` L56: `<control type="button" id="7947"><label>Favourite</label><onclick>RunScript(special://skin/scripts/bz_ctx.py,fav)</onclick><visible>Window.IsActive(pictures)</v`
  - `xml/DialogMusicInfo.xml` L14: `<control type="grouplist" id="9000"><left>582</left><top>166</top><width>360</width><height>420</height><itemgap>2</itemgap><orientation>vertical</orientation><`

### `bz_fav`
- set/clear sites: 0 · read sites: 0

### `bz_favpath`
- set/clear sites: 1 · read sites: 2
  - `scripts/bz_fav.py` L14: `xbmcgui.Window(10000).setProperty('bz_favpath', path if now else '')`
  - `xml/Includes_Bezel.xml` L89: `<variable name="BezelNPFavIcon"><value condition="String.IsEqual(Window(Home).Property(bz_favpath),Player.Filenameandpath)">bezel/np_fav.png</value><value>bezel`
  - `xml/Includes_Bezel.xml` L2813: `<variable name="BezelOSDIconCol_6198"><value condition="!Control.HasFocus(6198) + [String.IsEqual(Window(Home).Property(bz_favpath),Player.Filenameandpath)]">bz`

### `bz_flip`
- set/clear sites: 1 · read sites: 69
  - `xml/MyVideoNav.xml` L23: `<onload condition="Skin.HasSetting(bz_grid_video)">SetProperty(bz_gpend,1,home)</onload><onload>AlarmClock(bzgpend,ClearProperty(bz_gpend,home),00:02,silent)</o`
  - `xml/MyPlaylist.xml` L9: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L14: `<!-- BETA 1.1b: the gate below uses Player.HasAudio directly (the debounced bz_audio_latch from bz_flip.py may not be set yet on the first Tab after Kodi start;`

### `bz_minibig`
- set/clear sites: 7 · read sites: 3
  - `xml/MyPrograms.xml` L9: `<onunload>ClearProperty(bz_minibig,home)</onunload>`
  - `xml/MyVideoNav.xml` L13: `<onunload>ClearProperty(bz_minibig,home)</onunload>`
  - `xml/MyVideoNav.xml` L19: `<onload>ClearProperty(bz_minibig,home)</onload>`
  - `xml/Includes_Bezel.xml` L2548: `<animation effect="fade" start="100" end="0" time="1500" tween="sine" easing="inout" condition="String.IsEqual(Window(Home).Property(bz_minibig),true)">Conditio`
  - `xml/Includes_Bezel.xml` L2657: `<visible>Window.IsActive(videos) + String.IsEmpty(Window(Home).Property(bz_vback)) + String.IsEmpty(Window(Home).Property(bz_vbackanim)) + String.IsEmpty(Window`
  - `scripts/bz_flip.py` L892: `if home.getProperty('bz_minibig'):`

### `bz_mm`
- set/clear sites: 0 · read sites: 12
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_nav`
- set/clear sites: 75 · read sites: 103
  - `xml/Custom_1107_SearchDialog.xml` L23: `<control type="list" id="9000"><onback>SetProperty(bz_nav,true,home)</onback><onback>Dialog.Close(1107,true)</onback><!-- 5.33.235 Rob t1837: control onback con`
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Custom_1112_NowPlaying.xml` L15: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L16: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L17: `<onload condition="[String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visualis`

### `bz_navroot`
- set/clear sites: 7 · read sites: 23
  - `scripts/bz_mm.py` L17: `'music': ['SetProperty(bz_navroot,musicdb://albums/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,tomusic,musicdb://albums/)'],`
  - `scripts/bz_mm.py` L18: `'movies': ['SetProperty(bz_navroot,videodb://movies/titles/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,go,videodb://movies/titles/)'],`
  - `scripts/bz_mm.py` L19: `'tv': ['SetProperty(bz_navroot,videodb://tvshows/titles/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,go,videodb://tvshows/titles/)'],`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`

### `bz_rootarm`
- set/clear sites: 2 · read sites: 3
  - `scripts/bz_flip.py` L956: `rp[0] = fp; rp[1] = now - (0.6 if _fresh else 0); rp[2] = _wid; home.clearProperty('bz_rootarm')`
  - `scripts/bz_flip.py` L960: `home.setProperty('bz_rootarm', 'true')`
  - `xml/Includes_Bezel.xml` L2372: `<expression name="bz_atroot">String.IsEqual(Window(Home).Property(bz_rootarm),true) + ![String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Co`
  - `scripts/bz_flip.py` L950: `# (bz_rootarm = that path) before Back counts, so the Back that lands on the top level never opens it`
  - `scripts/bz_flip.py` L958: `elif now - rp[1] >= 0.6 and (fp in ROOTS or (home.getProperty('bz_navroot') and fp.rstrip('/') == home.getProperty('bz_navroot').rstrip('/'))) and home.getPrope`

