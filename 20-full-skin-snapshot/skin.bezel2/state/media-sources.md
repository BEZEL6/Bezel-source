# Media sources — media-sources

**Object:** `media-sources` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/media-sources.md) · [layout](../layout/media-sources.md) · [state](../state/media-sources.md) · [motion](../motion/media-sources.md) · [art](../art/media-sources.md) · [input](../input/media-sources.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
MEDIA SOURCES in the Main Menu opens a BEZEL page with Videos, Music and Pictures sources and their library tools. Pick one to open Kodi's sources for it. Back from there returns to this page on the same row. Back here opens the Main Menu.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_at_fanop`
- set/clear sites: 42 · read sites: 159
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L2023: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),fanop) + String.IsEqual(Skin.String(bz_at_fanop),2)">Skin.SetString(bz_at_fanop,1)</onle`
  - `xml/Includes_Bezel.xml` L737: `<!-- 5.0.2 mmbuild: LOOK Fanart opacity 0-100 step 10, default 50% --><animation effect="fade" start="100" end="0" time="0" condition="String.IsEqual(Skin.Strin`
  - `xml/Includes_Bezel.xml` L737: `<!-- 5.0.2 mmbuild: LOOK Fanart opacity 0-100 step 10, default 50% --><animation effect="fade" start="100" end="0" time="0" condition="String.IsEqual(Skin.Strin`
  - `xml/Includes_Bezel.xml` L737: `<!-- 5.0.2 mmbuild: LOOK Fanart opacity 0-100 step 10, default 50% --><animation effect="fade" start="100" end="0" time="0" condition="String.IsEqual(Skin.Strin`

### `bz_at_mmdim`
- set/clear sites: 42 · read sites: 542
  - `xml/Includes_Tuner.xml` L2055: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdim) + String.IsEqual(Skin.String(bz_at_mmdim),1)">Skin.SetString(bz_at_mmdim,2)</onr`
  - `xml/Includes_Tuner.xml` L2055: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdim) + String.IsEqual(Skin.String(bz_at_mmdim),1)">Skin.SetString(bz_at_mmdim,2)</onr`
  - `xml/Includes_Tuner.xml` L2056: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdim) + [String.IsEmpty(Skin.String(bz_at_mmdim)) | String.IsEqual(Skin.String(bz_at_m`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`

### `bz_backdrop`
- set/clear sites: 21 · read sites: 21
  - `xml/MyPlaylist.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/MyPlaylist.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/Settings.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L3048: `<texture colordiffuse="$VAR[BezelBackdropAlpha]">$INFO[Window(Home).Property(bz_backdrop)]</texture>`
  - `xml/Includes_Bezel.xml` L3049: `<visible>String.IsEmpty(Window(Home).Property(bz_npdlg)) + [Skin.HasSetting(bezel_norotate) | String.IsEmpty(Control.GetLabel(9880))] + String.IsEmpty(ListItem.`

### `bz_cov_a`
- set/clear sites: 1 · read sites: 14
  - `scripts/bz_flip.py` L1583: `for k in ('bz_cov_a', 'bz_cov_b', 'bz_cov_next'): home.clearProperty(k)`
  - `xml/Includes_Bezel.xml` L128: `<!-- v0.1.24: cover layers bind only to the held bz_cov_a/b properties from bz_flip.py (no Player.HasAudio gate, so a track gap never pops in the live art) -->`
  - `xml/Includes_Bezel.xml` L131: `<variable name="BezelFlipA"><value condition="!Player.HasVideo + !String.IsEmpty(Window(Home).Property(bz_cov_a))">$INFO[Window(Home).Property(bz_cov_a)]</value`
  - `xml/Includes_Bezel.xml` L131: `<variable name="BezelFlipA"><value condition="!Player.HasVideo + !String.IsEmpty(Window(Home).Property(bz_cov_a))">$INFO[Window(Home).Property(bz_cov_a)]</value`

### `bz_ctxwarm`
- set/clear sites: 0 · read sites: 4
  - `xml/Includes_Bezel.xml` L365: `<expression name="bz_ctxwarm">[Window.IsVisible(1132) | Window.IsVisible(1117) | [Window.IsVisible(pictures) + [String.IsEmpty(Container.FolderPath) | String.Is`
  - `xml/DialogContextMenu.xml` L13: `<control type="group"><visible>!Window.IsVisible(filebrowser) + !Window.IsVisible(filemanager) + !$EXP[bz_ctxwarm]</visible><include content="BezelStdFrame">`
  - `xml/DialogContextMenu.xml` L26: `<control type="group"><visible>$EXP[bz_ctxwarm]</visible><left>570</left><top>120</top>`

### `bz_fan_a`
- set/clear sites: 0 · read sites: 6
  - `xml/Includes_Bezel.xml` L759: `<texture background="true">$INFO[Window(Home).Property(bz_fan_a)]</texture>`
  - `xml/Includes_Bezel.xml` L2318: `<include name="View_63_BezelPictureList"><!-- 5.33.242 Rob t1862u: Pictures on the Warm strip (MM/Media Sources language). List 63 lives IN the colour strip at `
  - `xml/Custom_1117_MediaSources.xml` L13: `<!-- 5.33.233 Rob t1830: fanart flash on open — lane loads sync (MM already cached it, no empty frame) + black cover hides StdFrame bz_backdrop (fadetime 200) s`

### `bz_fan_b`
- set/clear sites: 0 · read sites: 3
  - `xml/Includes_Bezel.xml` L766: `<texture background="true">$INFO[Window(Home).Property(bz_fan_b)]</texture>`
  - `xml/Custom_1117_MediaSources.xml` L13: `<!-- 5.33.233 Rob t1830: fanart flash on open — lane loads sync (MM already cached it, no empty frame) + black cover hides StdFrame bz_backdrop (fadetime 200) s`
  - `xml/MyPics.xml` L10: `<include>BezelWarmHold</include><!-- 5.33.211 WARM HOLD --><!-- 5.33.234 Rob t1833: Pictures keeps the MM warm lane after MM closes (same bz_fan_a/b + fanop as `

### `bz_fan_on`
- set/clear sites: 0 · read sites: 11
  - `xml/Includes_Bezel.xml` L715: `<expression name="bz_warmhold">$EXP[bz_navmenu] + !String.IsEqual(Skin.String(bz_at_warmhold),Off) + !String.IsEmpty(Window(Home).Property(bz_fan_on))</expressi`
  - `xml/Includes_Bezel.xml` L748: `<visible>$EXP[bz_navmenu] + String.IsEmpty(Window(Home).Property(bz_fan_on))</visible>`
  - `xml/Includes_Bezel.xml` L755: `<visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_fan_on)) + !String.IsEqual(Window(Home).Property(bz_fan_side),b)</visible><animation effect`

### `bz_fan_side`
- set/clear sites: 0 · read sites: 6
  - `xml/Includes_Bezel.xml` L755: `<visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_fan_on)) + !String.IsEqual(Window(Home).Property(bz_fan_side),b)</visible><animation effect`
  - `xml/Includes_Bezel.xml` L762: `<visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_fan_on)) + String.IsEqual(Window(Home).Property(bz_fan_side),b)</visible><animation effect=`
  - `xml/Custom_1117_MediaSources.xml` L13: `<!-- 5.33.233 Rob t1830: fanart flash on open — lane loads sync (MM already cached it, no empty frame) + black cover hides StdFrame bz_backdrop (fadetime 200) s`

### `bz_kb`
- set/clear sites: 0 · read sites: 53
  - `xml/Includes_BezelDialogs.xml` L586: `<item><label>$VAR[BzKbCase0]</label><onclick>RunScript(special://skin/scripts/bz_kb.py,a,0)</onclick></item>`
  - `xml/Includes_BezelDialogs.xml` L587: `<item><label>$VAR[BzKbCase1]</label><onclick>RunScript(special://skin/scripts/bz_kb.py,a,1)</onclick></item>`
  - `xml/Includes_BezelDialogs.xml` L588: `<item><label>$VAR[BzKbCase2]</label><onclick>RunScript(special://skin/scripts/bz_kb.py,a,2)</onclick></item>`

### `bz_kbcaps`
- set/clear sites: 5 · read sites: 28
  - `xml/Includes_BezelDialogs.xml` L576: `<onup>9601</onup><ondown>9601</ondown><onleft condition="String.IsEmpty(Window(Home).Property(bz_kbcaps))">SetProperty(bz_kbcaps,1,home)</onleft><onleft conditi`
  - `xml/Includes_BezelDialogs.xml` L576: `<onup>9601</onup><ondown>9601</ondown><onleft condition="String.IsEmpty(Window(Home).Property(bz_kbcaps))">SetProperty(bz_kbcaps,1,home)</onleft><onleft conditi`
  - `xml/Includes_BezelDialogs.xml` L576: `<onup>9601</onup><ondown>9601</ondown><onleft condition="String.IsEmpty(Window(Home).Property(bz_kbcaps))">SetProperty(bz_kbcaps,1,home)</onleft><onleft conditi`
  - `xml/Includes_BezelDialogs.xml` L536: `<variable name="BzKbCapsLbl"><value condition="!String.IsEmpty(Window(Home).Property(bz_kbcaps))">ABC</value><value>abc</value></variable>`
  - `xml/Includes_BezelDialogs.xml` L537: `<variable name="BzKbCase0"><value condition="!String.IsEmpty(Window(Home).Property(bz_kbcaps))">A</value><value>a</value></variable>`
  - `xml/Includes_BezelDialogs.xml` L538: `<variable name="BzKbCase1"><value condition="!String.IsEmpty(Window(Home).Property(bz_kbcaps))">B</value><value>b</value></variable>`

### `bz_msfocus`
- set/clear sites: 3 · read sites: 10
  - `xml/Custom_1117_MediaSources.xml` L6: `<onload>ClearProperty(bz_msret,home)</onload><onload condition="!String.IsEmpty(Window(Home).Property(bz_msfocus))">AlarmClock(bzmsf,SetFocus($INFO[Window(Home)`
  - `xml/Custom_1117_MediaSources.xml` L6: `<onload>ClearProperty(bz_msret,home)</onload><onload condition="!String.IsEmpty(Window(Home).Property(bz_msfocus))">AlarmClock(bzmsf,SetFocus($INFO[Window(Home)`
  - `xml/Custom_1117_MediaSources.xml` L6: `<onload>ClearProperty(bz_msret,home)</onload><onload condition="!String.IsEmpty(Window(Home).Property(bz_msfocus))">AlarmClock(bzmsf,SetFocus($INFO[Window(Home)`
  - `xml/Custom_1117_MediaSources.xml` L2: `<!-- 5.33.220 Rob t1727 mock C/D: MEDIA SOURCES in the Warm strip (Settings 1130 language). ▾ expand bz_msx · » stock sources/library actions · ‹VALUE› pills vi`
  - `xml/Custom_1117_MediaSources.xml` L10: `<control type="button" id="6299"><left>-10</left><top>-10</top><width>1</width><height>1</height><texturefocus/><texturenofocus/><onfocus condition="!String.IsE`
  - `xml/Custom_1117_MediaSources.xml` L10: `<control type="button" id="6299"><left>-10</left><top>-10</top><width>1</width><height>1</height><texturefocus/><texturenofocus/><onfocus condition="!String.IsE`

### `bz_msret`
- set/clear sites: 1 · read sites: 22
  - `xml/Custom_1117_MediaSources.xml` L6: `<onload>ClearProperty(bz_msret,home)</onload><onload condition="!String.IsEmpty(Window(Home).Property(bz_msfocus))">AlarmClock(bzmsf,SetFocus($INFO[Window(Home)`
  - `xml/Custom_1132_BzSources.xml` L10: `<control type="list" id="9150"><left>0</left><top>112</top><width>390</width><height>720</height><orientation>vertical</orientation><scrolltime tween="cubic" ea`
  - `xml/Includes_Bezel.xml` L1594: `<onback condition="String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Container.FolderPath,sources://)">ActivateWindow(1117)</onback><onback `
  - `xml/Includes_Bezel.xml` L1594: `<onback condition="String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Container.FolderPath,sources://)">ActivateWindow(1117)</onback><onback `

### `bz_msx`
- set/clear sites: 2 · read sites: 35
  - `scripts/bz_set.py` L100: `if not home.getProperty('bz_msx'): home.setProperty('bz_msx', 'v')`
  - `scripts/bz_set.py` L100: `if not home.getProperty('bz_msx'): home.setProperty('bz_msx', 'v')`
  - `xml/Custom_1117_MediaSources.xml` L2: `<!-- 5.33.220 Rob t1727 mock C/D: MEDIA SOURCES in the Warm strip (Settings 1130 language). ▾ expand bz_msx · » stock sources/library actions · ‹VALUE› pills vi`
  - `xml/Custom_1117_MediaSources.xml` L20: `<control type="group"><width>390</width><height>48</height><control type="image"><left>0</left><top>0</top><width>390</width><height>48</height><texture colordi`
  - `xml/Custom_1117_MediaSources.xml` L20: `<control type="group"><width>390</width><height>48</height><control type="image"><left>0</left><top>0</top><width>390</width><height>48</height><texture colordi`

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

### `bz_navmenu`
- set/clear sites: 9 · read sites: 593
  - `xml/Includes_Bezel.xml` L2335: `<control type="list" id="63"><onback condition="[String.IsEmpty(Container.FolderPath) | String.IsEqual(Container.FolderPath,sources://pictures/)] + !$EXP[bz_nav`
  - `xml/MusicVisualisation.xml` L17: `<onunload condition="!$EXP[bz_navmenu]">AlarmClock(bz_vizret,SetFocus(60),00:00,silent)</onunload><!-- 5.33.112 t786: Play Next / viz exit -> section list 60 --`
  - `xml/FileManager.xml` L14: `<control type="list" id="20"><onback condition="String.IsEmpty(Container(20).FolderPath) + !$EXP[bz_navmenu]">SetProperty(bz_nav,true,home)</onback><!-- 5.33.17`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`

### `bz_navtune`
- set/clear sites: 21 · read sites: 45
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_pos_a`
- set/clear sites: 1 · read sites: 6
  - `scripts/bz_flip.py` L688: `for k in ('bz_pos_a', 'bz_pos_b', 'bz_pos_side', 'bz_pos_empty'): home.clearProperty(k)`
  - `xml/Includes_Bezel.xml` L1212: `<texture background="true">$INFO[Window(Home).Property(bz_pos_a)]</texture>`
  - `xml/Includes_Bezel.xml` L1283: `<texture background="true">$INFO[Window(Home).Property(bz_pos_a)]</texture>`
  - `xml/Includes_Bezel.xml` L2616: `<texture background="true">$INFO[Window(Home).Property(bz_pos_a)]</texture>`

### `bz_pos_on`
- set/clear sites: 1 · read sites: 18
  - `scripts/bz_flip.py` L683: `if enter_music: home.clearProperty('bz_pos_on'); home.clearProperty('bz_hold_poster')   # video poster A/B fades out over the new Music album`
  - `xml/Includes_Bezel.xml` L1202: `<control type="image"><visible>$EXP[bz_navmenu] + ![!String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAudio + String.IsEmpty(Window(Home).Property(`
  - `xml/Includes_Bezel.xml` L1209: `</control><!-- 5.33.148 MM A/B pos side a --><control type="image"><visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAu`
  - `xml/Includes_Bezel.xml` L1216: `</control><!-- 5.33.148 MM A/B pos side b --><control type="image"><visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAu`

### `bz_pos_side`
- set/clear sites: 1 · read sites: 9
  - `scripts/bz_flip.py` L688: `for k in ('bz_pos_a', 'bz_pos_b', 'bz_pos_side', 'bz_pos_empty'): home.clearProperty(k)`
  - `xml/Includes_Bezel.xml` L1209: `</control><!-- 5.33.148 MM A/B pos side a --><control type="image"><visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAu`
  - `xml/Includes_Bezel.xml` L1216: `</control><!-- 5.33.148 MM A/B pos side b --><control type="image"><visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAu`
  - `xml/Includes_Bezel.xml` L1280: `</control><!-- 5.33.148 MM A/B pos side a --><control type="image"><visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAu`

### `bz_srclab`
- set/clear sites: 0 · read sites: 4
  - `xml/Custom_1132_BzSources.xml` L9: `<control type="label"><left>36</left><top>78</top><width>340</width><height>24</height><aligny>center</aligny><font>bz_b12</font><textcolor>AAFFFFFF</textcolor>`
  - `xml/Custom_1117_MediaSources.xml` L21: `<control type="group"><width>390</width><height>48</height><visible>String.IsEqual(Window(Home).Property(bz_msx),v)</visible><control type="image"><left>0</left`
  - `xml/Custom_1117_MediaSources.xml` L28: `<control type="group"><width>390</width><height>48</height><visible>String.IsEqual(Window(Home).Property(bz_msx),m)</visible><control type="image"><left>0</left`

### `bz_srcpath`
- set/clear sites: 0 · read sites: 4
  - `xml/Custom_1132_BzSources.xml` L10: `<control type="list" id="9150"><left>0</left><top>112</top><width>390</width><height>720</height><orientation>vertical</orientation><scrolltime tween="cubic" ea`
  - `xml/Custom_1117_MediaSources.xml` L21: `<control type="group"><width>390</width><height>48</height><visible>String.IsEqual(Window(Home).Property(bz_msx),v)</visible><control type="image"><left>0</left`
  - `xml/Custom_1117_MediaSources.xml` L28: `<control type="group"><width>390</width><height>48</height><visible>String.IsEqual(Window(Home).Property(bz_msx),m)</visible><control type="image"><left>0</left`

### `bz_srcwin`
- set/clear sites: 0 · read sites: 4
  - `xml/Custom_1132_BzSources.xml` L10: `<control type="list" id="9150"><left>0</left><top>112</top><width>390</width><height>720</height><orientation>vertical</orientation><scrolltime tween="cubic" ea`
  - `xml/Custom_1117_MediaSources.xml` L21: `<control type="group"><width>390</width><height>48</height><visible>String.IsEqual(Window(Home).Property(bz_msx),v)</visible><control type="image"><left>0</left`
  - `xml/Custom_1117_MediaSources.xml` L28: `<control type="group"><width>390</width><height>48</height><visible>String.IsEqual(Window(Home).Property(bz_msx),m)</visible><control type="image"><left>0</left`

