# Kodi Settings — settings

**Object:** `settings` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/settings.md) · [layout](../layout/settings.md) · [state](../state/settings.md) · [motion](../motion/settings.md) · [art](../art/settings.md) · [input](../input/settings.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

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

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_dtap`
- set/clear sites: 0 · read sites: 7
  - `xml/Includes_Tuner.xml` L498: `<!-- Kodi resets only the first Visible/Hidden animation of a control, so a changed step must not stay applied: any change marks bz_tune_dirty and bz_dtap.py re`
  - `xml/Includes_Tuner.xml` L2410: `<item><label>5.33.11  Settings strip</label><property name="kind">btn</property><property name="id"></property><property name="info">bezel/info/ver_5_33_10.png<`
  - `scripts/bz_cmd.py` L42: `xbmc.executebuiltin('RunScript(special://skin/scripts/bz_dtap.py)')   # BETA 2.8: double-tap Select service (guards itself)`

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

### `bz_mmpos`
- set/clear sites: 6 · read sites: 4
  - `scripts/bz_flip.py` L746: `home.setProperty('bz_mmpos', home.getProperty('bz_mmlive') or pos or '0')   # t4094b live row first; FLASH t3430: new window's onload restores this row (was row`
  - `scripts/bz_flip.py` L754: `if xbmc.getCondVisibility('Control.HasFocus(6996)'): _pp[0] = xbmc.getInfoLabel('Container(6996).Position') or _pp[0]; home.setProperty('bz_mmpos', _pp[0]); hom`
  - `scripts/bz_flip.py` L755: `else: _pp[0] = home.getProperty('bz_mmlive') or _pp[0]; home.setProperty('bz_mmpos', _pp[0] or '0'); (_pk() or _bzstrip(home, _pp[0]))   # t4092 live row`
  - `xml/MyVideoNav.xml` L6: `<onload condition="!Control.HasFocus(6996) + !String.IsEqual(Window(home).Property(bz_mmpick),true) + !String.IsEmpty(Window(home).Property(bz_mmwarm)) + !Strin`
  - `xml/MyMusicNav.xml` L6: `<onload condition="!Control.HasFocus(6996) + !String.IsEqual(Window(home).Property(bz_mmpick),true) + !String.IsEmpty(Window(home).Property(bz_mmwarm)) + !Strin`
  - `scripts/bz_dbg.py` L3: `P = ('bz_nav', 'bz_mmwarm', 'bz_xfade', 'bz_mmpick', 'bz_mmlock', 'bz_mmpos', 'bz_mmlive', 'bz_navroot', 'bz_mmstart')`

### `bz_nav`
- set/clear sites: 75 · read sites: 103
  - `xml/Custom_1107_SearchDialog.xml` L23: `<control type="list" id="9000"><onback>SetProperty(bz_nav,true,home)</onback><onback>Dialog.Close(1107,true)</onback><!-- 5.33.235 Rob t1837: control onback con`
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Custom_1112_NowPlaying.xml` L15: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L16: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L17: `<onload condition="[String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visualis`

### `bz_set`
- set/clear sites: 0 · read sites: 120
  - `xml/Custom_1132_BzSources.xml` L2: `<!-- 5.33.232 Rob t1827: Media Sources > SOURCES follow-on Warm strip (dynamic sources:// list, opens the source in its media window; context menu = edit/remove`
  - `xml/Custom_1117_MediaSources.xml` L2: `<!-- 5.33.220 Rob t1727 mock C/D: MEDIA SOURCES in the Warm strip (Settings 1130 language). ▾ expand bz_msx · » stock sources/library actions · ‹VALUE› pills vi`
  - `xml/Custom_1117_MediaSources.xml` L5: `<onload>RunScript(special://skin/scripts/bz_set.py,msload)</onload>`

### `bz_set_`
- set/clear sites: 1 · read sites: 0
  - `scripts/bz_set.py` L34: `home.setProperty('bz_set_' + s.replace('.', '_'), t)`

### `bz_setback`
- set/clear sites: 0 · read sites: 3
  - `scripts/bz_dtap.py` L30: `''.join('\t<%s>\n\t\t<keyboard><backspace>NotifyAll(bz,bz_setback)</backspace></keyboard>\n\t\t<remote><back>NotifyAll(bz,bz_setback)</back></remote>\n\t</%s>\n`
  - `scripts/bz_dtap.py` L30: `''.join('\t<%s>\n\t\t<keyboard><backspace>NotifyAll(bz,bz_setback)</backspace></keyboard>\n\t\t<remote><back>NotifyAll(bz,bz_setback)</back></remote>\n\t</%s>\n`
  - `scripts/bz_dtap.py` L93: `if method.endswith('bz_setback'):   # 5.33.11: Settings Back - sub-list (grouplist 5) -> parent category list 3, else normal Back`

### `bz_setmm`
- set/clear sites: 1 · read sites: 1
  - `xml/Settings.xml` L46: `<!-- 4.6.3 Rob: Back returns to Main menu like the Tuner (menu opens over Settings, focus on the strip; a navigation target consumes Back) --><onback>SetPropert`
  - `xml/Custom_1130_BzSettings.xml` L16: `<control type="list" id="9130"><left>0</left><top>112</top><width>390</width><height>708</height><visible>String.IsEmpty(Window(Home).Property(bz_setpg))</visib`

### `bz_setpg`
- set/clear sites: 3 · read sites: 59
  - `xml/Custom_1130_BzSettings.xml` L7: `<onload>ClearProperty(bz_setpg,home)</onload>`
  - `scripts/bz_set.py` L53: `home.setProperty('bz_setpg', a[1]); load()`
  - `scripts/bz_set.py` L59: `home.setProperty('bz_setpg', '')`
  - `xml/Custom_1130_BzSettings.xml` L13: `<control type="label"><left>34</left><top>34</top><width>340</width><height>44</height><aligny>center</aligny><font>bz_mm34</font><textcolor>FFFFFFFF</textcolor`
  - `xml/Custom_1130_BzSettings.xml` L14: `<control type="label"><left>34</left><top>34</top><width>340</width><height>44</height><aligny>center</aligny><font>bz_mm34</font><textcolor>FFFFFFFF</textcolor`
  - `xml/Custom_1130_BzSettings.xml` L14: `<control type="label"><left>34</left><top>34</top><width>340</width><height>44</height><aligny>center</aligny><font>bz_mm34</font><textcolor>FFFFFFFF</textcolor`

### `bz_setret`
- set/clear sites: 4 · read sites: 1
  - `scripts/bz_flip.py` L1012: `home.clearProperty('bz_navset'); home.clearProperty('bz_navsub'); home.clearProperty('bz_navnp'); home.clearProperty('bz_navset2'); home.clearProperty('bz_kset'`
  - `scripts/bz_flip.py` L1013: `if nv and not nav_was[0]: home.clearProperty('bz_setret') if not (setret[1] and now - setret[1] < 4.0) else None; had = False; t = 0; stuck[1] = 0; navop[0] = n`
  - `scripts/bz_flip.py` L1045: `elif home.getProperty('bz_setret') or (setret[1] and now - setret[1] < 4.0): tgt = 6909; setret[1] = 0; home.setProperty('bz_setret', '1'); home.setProperty('bz`
  - `xml/Custom_1130_BzSettings.xml` L16: `<control type="list" id="9130"><left>0</left><top>112</top><width>390</width><height>708</height><visible>String.IsEmpty(Window(Home).Property(bz_setpg))</visib`

### `bz_setx`
- set/clear sites: 3 · read sites: 38
  - `xml/Custom_1130_BzSettings.xml` L51: `<item><label>WARM 2.0.1 · TUNER</label><property name="kind">m</property><property name="lvl">sub</property><onclick>SetProperty(bz_tunesrc,set,home)</onclick><`
  - `scripts/bz_set.py` L51: `home.setProperty('bz_setx', '' if home.getProperty('bz_setx') == a[1] else a[1])`
  - `scripts/bz_set.py` L51: `home.setProperty('bz_setx', '' if home.getProperty('bz_setx') == a[1] else a[1])`
  - `xml/Custom_1130_BzSettings.xml` L3: `▾ expand in place (bz_setx) · » new menu · ‹VALUE› cycle pills (bz_set.py reads/writes Kodi settings via JSON-RPC). Generated by /workspace/b401/set5215/gen.py `
  - `xml/Custom_1130_BzSettings.xml` L15: `<control type="label"><left>36</left><top>78</top><width>340</width><height>24</height><aligny>center</aligny><font>bz_b12</font><textcolor>AAFFFFFF</textcolor>`
  - `xml/Custom_1130_BzSettings.xml` L16: `<control type="list" id="9130"><left>0</left><top>112</top><width>390</width><height>708</height><visible>String.IsEmpty(Window(Home).Property(bz_setpg))</visib`

### `bz_tunesrc`
- set/clear sites: 16 · read sites: 3
  - `xml/Custom_1118_PowerMenu.xml` L8: `<onload>ClearProperty(bz_tunesrc,home)</onload><onload>SetProperty(bz_pwrswap,1,home)</onload><!-- t4943 K52: skip 6996 slides on POWER swap -->`
  - `xml/Custom_1118_PowerMenu.xml` L26: `<item><label>TUNER</label><onclick>SetProperty(bz_tunesrc,pwr,home)</onclick><onclick>SetProperty(bz_navtune,true,home)</onclick><onclick>ClearProperty(bz_navbe`
  - `xml/Custom_1130_BzSettings.xml` L51: `<item><label>WARM 2.0.1 · TUNER</label><property name="kind">m</property><property name="lvl">sub</property><onclick>SetProperty(bz_tunesrc,set,home)</onclick><`
  - `xml/Custom_1118_PowerMenu.xml` L10: `<onunload condition="!String.IsEqual(Window(Home).Property(bz_tunesrc),pwr)">AlarmClock(bzpwrf,SetFocus(6996),00:00,silent,false)</onunload>`
  - `xml/Custom_1130_BzSettings.xml` L102: `<control type="group"><visible>String.IsEqual(ListItem.Property(kind),p)</visible><animation effect="fade" start="100" end="70" time="0" condition="String.IsEqu`
  - `xml/Custom_1115_MusicControls.xml` L40: `<control type="group"><top>766</top><control type="image"><left>12</left><top>4</top><width>366</width><height>48</height><texture border="23" colordiffuse="E6F`

