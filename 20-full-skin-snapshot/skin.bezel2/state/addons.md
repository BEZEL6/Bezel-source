# Add-ons browser — addons

**Object:** `addons` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/addons.md) · [layout](../layout/addons.md) · [state](../state/addons.md) · [motion](../motion/addons.md) · [art](../art/addons.md) · [input](../input/addons.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Pick ADD-ONS in the Main Menu and Kodi's add-on browser opens in BEZEL chrome with a random backdrop. Press Back at the top level and the Main Menu opens again.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

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

### `bz_bdimg`
- set/clear sites: 2 · read sites: 6
  - `scripts/bz_cmd.py` L99: `xbmc.executebuiltin('Skin.SetString(bz_bdimg,%s)' % nxt); home.setProperty('bz_backdrop', d + nxt)`
  - `scripts/bz_cmd.py` L102: `xbmc.executebuiltin('Skin.Reset(bz_bdimg)'); home.setProperty('bz_bdimg_lbl', 'Random')`
  - `xml/Includes_Tuner.xml` L186: `<variable name="BzATVal_bdimg"><value condition="String.IsEmpty(Skin.String(bz_bdimg))">Random</value><value>$INFO[Skin.String(bz_bdimg)]</value></variable><!--`
  - `xml/Includes_Tuner.xml` L186: `<variable name="BzATVal_bdimg"><value condition="String.IsEmpty(Skin.String(bz_bdimg))">Random</value><value>$INFO[Skin.String(bz_bdimg)]</value></variable><!--`
  - `scripts/bz_cmd.py` L80: `# 4.7.4: Tuner LOOK > Backdrop image (skin string bz_bdimg: empty = Random, else a file name that sticks until changed)`

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_lastart_`
- set/clear sites: 1 · read sites: 1
  - `scripts/bz_mm.py` L15: `if a and 'DefaultFolderBack' not in a: xbmc.executebuiltin('Skin.SetString(bz_lastart_%s,%s)' % (s, a)); return`
  - `scripts/bz_mm.py` L1: `# BEZEL 4.1 O46/O47: strip-list Main menu actions. Stores the leaving section's art (bz_lastart_<sec>) then runs the item.`

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

### `bz_mmpick`
- set/clear sites: 3 · read sites: 16
  - `scripts/bz_mm.py` L65: `xbmcgui.Window(10000).setProperty('bz_mmpick', 'true')   # MMHIDE: a pick may focus the list under MM`
  - `scripts/bz_flip.py` L1081: `if home.getProperty('bz_mmpick'): home.clearProperty('bz_mmpick')`
  - `scripts/bz_flip.py` L1081: `if home.getProperty('bz_mmpick'): home.clearProperty('bz_mmpick')`
  - `xml/Includes_Bezel.xml` L4: `<include name="BezelMMFocusBounce"><onfocus condition="$EXP[bz_navmenu] + !String.IsEqual(Window(home).Property(bz_mmpick),true)">SetFocus(6996)</onfocus></incl`
  - `xml/Includes_Bezel.xml` L6: `<include name="BezelMMFocusBounceList"><onfocus condition="!String.IsEmpty(Window(home).Property(bz_mmwarm)) + !String.IsEqual(Window(home).Property(bz_mmpick),`
  - `xml/Includes_Bezel.xml` L6: `<include name="BezelMMFocusBounceList"><onfocus condition="!String.IsEmpty(Window(home).Property(bz_mmwarm)) + !String.IsEqual(Window(home).Property(bz_mmpick),`

### `bz_mmwarm`
- set/clear sites: 5 · read sites: 18
  - `scripts/bz_flip.py` L724: `home.setProperty('bz_mmwarm', 'true'); home.setProperty('bz_navroot', path)`
  - `scripts/bz_flip.py` L744: `home.clearProperty('bz_mmwarm'); home.clearProperty('bz_xfade')   # t4333: fade back in`
  - `scripts/bz_flip.py` L747: `home.setProperty('bz_mmwarm', 'true'); home.setProperty('bz_navroot', path)`
  - `xml/Includes_Bezel.xml` L6: `<include name="BezelMMFocusBounceList"><onfocus condition="!String.IsEmpty(Window(home).Property(bz_mmwarm)) + !String.IsEqual(Window(home).Property(bz_mmpick),`
  - `xml/Includes_Bezel.xml` L6: `<include name="BezelMMFocusBounceList"><onfocus condition="!String.IsEmpty(Window(home).Property(bz_mmwarm)) + !String.IsEqual(Window(home).Property(bz_mmpick),`
  - `xml/MyVideoNav.xml` L6: `<onload condition="!Control.HasFocus(6996) + !String.IsEqual(Window(home).Property(bz_mmpick),true) + !String.IsEmpty(Window(home).Property(bz_mmwarm)) + !Strin`

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

### `bz_set`
- set/clear sites: 0 · read sites: 120
  - `xml/Custom_1132_BzSources.xml` L2: `<!-- 5.33.232 Rob t1827: Media Sources > SOURCES follow-on Warm strip (dynamic sources:// list, opens the source in its media window; context menu = edit/remove`
  - `xml/Custom_1117_MediaSources.xml` L2: `<!-- 5.33.220 Rob t1727 mock C/D: MEDIA SOURCES in the Warm strip (Settings 1130 language). ▾ expand bz_msx · » stock sources/library actions · ‹VALUE› pills vi`
  - `xml/Custom_1117_MediaSources.xml` L5: `<onload>RunScript(special://skin/scripts/bz_set.py,msload)</onload>`

