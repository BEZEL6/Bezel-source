# Skin settings / BEZEL Tuner — skin-settings-tuner

**Object:** `skin-settings-tuner` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/skin-settings-tuner.md) · [layout](../layout/skin-settings-tuner.md) · [state](../state/skin-settings-tuner.md) · [motion](../motion/skin-settings-tuner.md) · [art](../art/skin-settings-tuner.md) · [input](../input/skin-settings-tuner.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

**See screen:** [skin-settings-tuner baselines](../port-refs/skin-settings-tuner/) — smoke baseline + port diff target.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_at_`
- set/clear sites: 3 · read sites: 9
  - `scripts/bz_cmd.py` L606: `xbmc.executebuiltin('Skin.SetString(bz_at_%s,%d)' % (_i, _m[int(_v) - 1])); _ch = True`
  - `scripts/bz_tune.py` L17: `def setv(i, v): xbmcgui.Window(10000).setProperty('bz_tune_dirty', '1'); xbmc.executebuiltin('Skin.SetString(bz_at_%s,%s)' % (i, v)) if v else xbmc.executebuilt`
  - `scripts/bz_tune.py` L17: `def setv(i, v): xbmcgui.Window(10000).setProperty('bz_tune_dirty', '1'); xbmc.executebuiltin('Skin.SetString(bz_at_%s,%s)' % (i, v)) if v else xbmc.executebuilt`
  - `xml/Includes_Tuner.xml` L3: `Each setting = Skin.String(bz_at_<id>) step index; empty = default (the 2.7 look). Kodi animation times are fixed, so every step is its own conditional copy. --`
  - `scripts/bz_tune_patch.py` L11: `s = get('Skin.String(bz_at_%s)' % i)`
  - `scripts/bz_tune_patch.py` L56: `x = g('Skin.String(bz_at_%s)' % i); return vals[int(x) - 1] if x.isdigit() and 1 <= int(x) <= len(vals) else vals[d - 1]`

### `bz_at_dtapwin`
- set/clear sites: 58 · read sites: 50
  - `xml/Includes_Tuner.xml` L1062: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtapwin) + String.IsEqual(Skin.String(bz_at_dtapwin),2)">Skin.SetString(bz_at_dtapwin,1)`
  - `xml/Includes_Tuner.xml` L1062: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtapwin) + String.IsEqual(Skin.String(bz_at_dtapwin),2)">Skin.SetString(bz_at_dtapwin,1)`
  - `xml/Includes_Tuner.xml` L1063: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtapwin) + String.IsEqual(Skin.String(bz_at_dtapwin),3)">Skin.SetString(bz_at_dtapwin,2)`
  - `xml/Includes_Tuner.xml` L334: `<variable name="BzATVal_dtapwin"><value condition="String.IsEqual(Skin.String(bz_at_dtapwin),1)">150 ms</value><value condition="String.IsEqual(Skin.String(bz_a`
  - `xml/Includes_Tuner.xml` L334: `<variable name="BzATVal_dtapwin"><value condition="String.IsEqual(Skin.String(bz_at_dtapwin),1)">150 ms</value><value condition="String.IsEqual(Skin.String(bz_a`
  - `xml/Includes_Tuner.xml` L334: `<variable name="BzATVal_dtapwin"><value condition="String.IsEqual(Skin.String(bz_at_dtapwin),1)">150 ms</value><value condition="String.IsEqual(Skin.String(bz_a`

### `bz_at_fsslide`
- set/clear sites: 24 · read sites: 118
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`

### `bz_at_mmdbright`
- set/clear sites: 38 · read sites: 36
  - `xml/Includes_Tuner.xml` L501: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdbright) + String.IsEmpty(Skin.String(bz_at_mmdbright))">Skin.SetString(bz_at_mmdbrig`
  - `xml/Includes_Tuner.xml` L501: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdbright) + String.IsEmpty(Skin.String(bz_at_mmdbright))">Skin.SetString(bz_at_mmdbrig`
  - `xml/Includes_Tuner.xml` L502: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdbright) + String.IsEqual(Skin.String(bz_at_mmdbright),1)">Skin.SetString(bz_at_mmdbr`
  - `xml/Includes_Tuner.xml` L63: `<variable name="BzMMDustA"><value condition="String.IsEqual(Skin.String(bz_at_mmdbright),1)">1AFFFFFF</value><value condition="String.IsEqual(Skin.String(bz_at_`
  - `xml/Includes_Tuner.xml` L63: `<variable name="BzMMDustA"><value condition="String.IsEqual(Skin.String(bz_at_mmdbright),1)">1AFFFFFF</value><value condition="String.IsEqual(Skin.String(bz_at_`
  - `xml/Includes_Tuner.xml` L63: `<variable name="BzMMDustA"><value condition="String.IsEqual(Skin.String(bz_at_mmdbright),1)">1AFFFFFF</value><value condition="String.IsEqual(Skin.String(bz_at_`

### `bz_at_mmidle`
- set/clear sites: 2 · read sites: 2
  - `xml/Includes_Tuner.xml` L1962: `<!-- 5.33.216 MM auto-hide --><onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmidle)">Skin.SetString(bz_at_mmidle,Off)</onleft><onright`
  - `xml/Includes_Tuner.xml` L1962: `<!-- 5.33.216 MM auto-hide --><onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmidle)">Skin.SetString(bz_at_mmidle,Off)</onleft><onright`
  - `xml/Includes_Tuner.xml` L117: `<variable name="BzATVal_mmidle"><value condition="String.IsEqual(Skin.String(bz_at_mmidle),Off)">Off</value><value>On (30 s)</value></variable><!-- 5.33.216 -->`
  - `scripts/bz_flip.py` L1450: `elif (home.getProperty('bz_nav') == 'true' and xbmc.getInfoLabel('Skin.String(bz_at_mmidle)') != 'Off'`

### `bz_at_warmsplash`
- set/clear sites: 3 · read sites: 4
  - `xml/Includes_Tuner.xml` L1961: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),warmsplash)">Skin.SetString(bz_at_warmsplash,Off)</onleft><onright condition="String.IsE`
  - `xml/Includes_Tuner.xml` L1961: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),warmsplash)">Skin.SetString(bz_at_warmsplash,Off)</onleft><onright condition="String.IsE`
  - `xml/Startup.xml` L5: `<onload condition="!String.IsEqual(Skin.String(bz_at_warmsplash),Off)">SetProperty(bz_warm_gate,1,home)</onload>`
  - `xml/Includes_Bezel.xml` L3672: `<visible>!String.IsEmpty(Window(Home).Property(bz_warm_gate)) + !String.IsEqual(Skin.String(bz_at_warmsplash),Off)</visible>`
  - `xml/Includes_Tuner.xml` L116: `<variable name="BzATVal_warmsplash"><value condition="String.IsEqual(Skin.String(bz_at_warmsplash),Off)">Off (warm still runs)</value><value>On</value></variabl`
  - `xml/Startup.xml` L4: `<!-- Tuner WARM 2.0 > Startup splash (bz_at_warmsplash, default On): Off hides splash VISUALS only; warm-cache always runs. -->`

### `bz_defseed`
- set/clear sites: 1 · read sites: 2
  - `scripts/bz_tune.py` L78: `apply_defs('everything'); xbmc.executebuiltin('Skin.SetString(bz_defseed,%s)' % DEF.get('ver')); xbmc.sleep(300)`
  - `xml/Home.xml` L8: `<onload condition="!String.IsEqual(Skin.String(bz_defseed),5.0.20)">RunScript(special://skin/scripts/bz_tune.py,seed)</onload><!-- t4691: Rob default picks seed`
  - `scripts/bz_tune.py` L77: `if DEF and xbmc.getInfoLabel('Skin.String(bz_defseed)') != DEF.get('ver'):`

### `bz_dtap`
- set/clear sites: 0 · read sites: 7
  - `xml/Includes_Tuner.xml` L498: `<!-- Kodi resets only the first Visible/Hidden animation of a control, so a changed step must not stay applied: any change marks bz_tune_dirty and bz_dtap.py re`
  - `xml/Includes_Tuner.xml` L2410: `<item><label>5.33.11  Settings strip</label><property name="kind">btn</property><property name="id"></property><property name="info">bezel/info/ver_5_33_10.png<`
  - `scripts/bz_cmd.py` L42: `xbmc.executebuiltin('RunScript(special://skin/scripts/bz_dtap.py)')   # BETA 2.8: double-tap Select service (guards itself)`

### `bz_dtap_off`
- set/clear sites: 4 · read sites: 10
  - `xml/Includes_Tuner.xml` L1606: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtap)">Skin.SetBool(bz_dtap_off)</onleft><onright condition="String.IsEqual(Container(69`
  - `xml/Includes_Tuner.xml` L1606: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtap)">Skin.SetBool(bz_dtap_off)</onleft><onright condition="String.IsEqual(Container(69`
  - `scripts/bz_tune.py` L110: `if 'dtap' in st: xbmc.executebuiltin('Skin.SetBool(bz_dtap_off)' if st['dtap'].get('value') == 'OFF' else 'Skin.Reset(bz_dtap_off)')`
  - `xml/Includes_Bezel.xml` L44: `<control type="group"><visible>!Window.IsActive(1120) + !Skin.HasSetting(bz_dtap_off) + [Control.IsVisible(60) | Control.IsVisible(63) | [Control.IsVisible(50) `
  - `xml/Includes_Tuner.xml` L474: `<variable name="BzATVal_dtap"><value condition="Skin.HasSetting(bz_dtap_off)">OFF</value><value>ON</value></variable>`
  - `xml/Includes_Tuner.xml` L2434: `<variable name="BzATPillOff"><value condition="Skin.HasSetting(bz_dtap_off)">FF3D6FA0</value><value>40FFFFFF</value></variable>`

### `bz_m1121ok`
- set/clear sites: 2 · read sites: 7
  - `xml/Includes_Tuner.xml` L499: `<onback condition="String.IsEqual(Window(Home).Property(bz_tunesrc),pwr)">ClearProperty(bz_navtune,home)</onback><onback condition="String.IsEqual(Window(Home).`
  - `xml/Includes_Tuner.xml` L499: `<onback condition="String.IsEqual(Window(Home).Property(bz_tunesrc),pwr)">ClearProperty(bz_navtune,home)</onback><onback condition="String.IsEqual(Window(Home).`
  - `xml/Includes_Bezel.xml` L334: `<expression name="bz_m1121ok">!Skin.HasSetting(bz_m1121_off) + Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !Window.IsActive(visualisation)</ex`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_mmmushide`
- set/clear sites: 0 · read sites: 16
  - `xml/Includes_Bezel.xml` L123: `<expression name="bz_mmmushide">Player.HasAudio + !Player.HasVideo + $EXP[bz_navmenu] + !String.IsEqual(Skin.String(bz_at_warmmusicposters),Off)</expression><!-`
  - `xml/Includes_Bezel.xml` L2559: `<control type="image"><left>990</left><top>120</top><width>600</width><height>900</height><texture>bezel/poster_blur.png</texture><!-- 3.5.1: only while the lis`
  - `xml/Includes_Bezel.xml` L2560: `<control type="image"><left>990</left><top>120</top><width>600</width><height>900</height><texture border="6">bezel/frame.png</texture><visible>!String.IsEmpty(`

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

### `bz_tune`
- set/clear sites: 0 · read sites: 96
  - `xml/Home.xml` L8: `<onload condition="!String.IsEqual(Skin.String(bz_defseed),5.0.20)">RunScript(special://skin/scripts/bz_tune.py,seed)</onload><!-- t4691: Rob default picks seed`
  - `xml/Includes_Tuner.xml` L1414: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),alldust)">RunScript(special://skin/scripts/bz_tune.py,alldust,off)</onleft><onright cond`
  - `xml/Includes_Tuner.xml` L1414: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),alldust)">RunScript(special://skin/scripts/bz_tune.py,alldust,off)</onleft><onright cond`

### `bz_tune_dirty`
- set/clear sites: 5 · read sites: 39
  - `scripts/bz_cmd.py` L104: `home.setProperty('bz_tune_dirty', '1')`
  - `scripts/bz_dtap.py` L129: `st['dirty_t'] = None; home.clearProperty('bz_tune_dirty'); reload_tuned()`
  - `scripts/bz_tune.py` L17: `def setv(i, v): xbmcgui.Window(10000).setProperty('bz_tune_dirty', '1'); xbmc.executebuiltin('Skin.SetString(bz_at_%s,%s)' % (i, v)) if v else xbmc.executebuilt`
  - `xml/Includes_Tuner.xml` L498: `<!-- Kodi resets only the first Visible/Hidden animation of a control, so a changed step must not stay applied: any change marks bz_tune_dirty and bz_dtap.py re`
  - `xml/Includes_Tuner.xml` L498: `<!-- Kodi resets only the first Visible/Hidden animation of a control, so a changed step must not stay applied: any change marks bz_tune_dirty and bz_dtap.py re`
  - `xml/Includes_Tuner.xml` L498: `<!-- Kodi resets only the first Visible/Hidden animation of a control, so a changed step must not stay applied: any change marks bz_tune_dirty and bz_dtap.py re`

### `bz_tune_patch`
- set/clear sites: 0 · read sites: 18
  - `xml/Includes_Bezel.xml` L529: `<!-- BEZEL 3.1 slide menu (gen/gen_menu31.py): drops from the block top; one open / one close anim (BezelATMenuAnim, written by bz_tune_patch._tuner); everythin`
  - `xml/Includes_Bezel.xml` L1619: `<control type="group"><!-- 4.3 item 18 + 4.0.1 O21: rows 1-15 drop 40 px; time = speed x (1 + 0.35 row/14), quadratic out; delay = row x stagger, both scaled by`
  - `xml/Includes_Bezel.xml` L1640: `<control type="group"><!-- 4.3 item 18 + 4.0.1 O21: rows 1-15 drop 40 px; time = speed x (1 + 0.35 row/14), quadratic out; delay = row x stagger, both scaled by`

### `bz_tunesrc`
- set/clear sites: 16 · read sites: 3
  - `xml/Custom_1118_PowerMenu.xml` L8: `<onload>ClearProperty(bz_tunesrc,home)</onload><onload>SetProperty(bz_pwrswap,1,home)</onload><!-- t4943 K52: skip 6996 slides on POWER swap -->`
  - `xml/Custom_1118_PowerMenu.xml` L26: `<item><label>TUNER</label><onclick>SetProperty(bz_tunesrc,pwr,home)</onclick><onclick>SetProperty(bz_navtune,true,home)</onclick><onclick>ClearProperty(bz_navbe`
  - `xml/Custom_1130_BzSettings.xml` L51: `<item><label>WARM 2.0.1 · TUNER</label><property name="kind">m</property><property name="lvl">sub</property><onclick>SetProperty(bz_tunesrc,set,home)</onclick><`
  - `xml/Custom_1118_PowerMenu.xml` L10: `<onunload condition="!String.IsEqual(Window(Home).Property(bz_tunesrc),pwr)">AlarmClock(bzpwrf,SetFocus(6996),00:00,silent,false)</onunload>`
  - `xml/Custom_1130_BzSettings.xml` L102: `<control type="group"><visible>String.IsEqual(ListItem.Property(kind),p)</visible><animation effect="fade" start="100" end="70" time="0" condition="String.IsEqu`
  - `xml/Custom_1115_MusicControls.xml` L40: `<control type="group"><top>766</top><control type="image"><left>12</left><top>4</top><width>366</width><height>48</height><texture border="23" colordiffuse="E6F`

