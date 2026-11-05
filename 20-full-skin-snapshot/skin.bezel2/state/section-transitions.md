# Section transitions (STANDARD) — section-transitions

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `section-transitions` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/section-transitions.md) · [layout](../layout/section-transitions.md) · [state](../state/section-transitions.md) · [motion](../motion/section-transitions.md) · [art](../art/section-transitions.md) · [input](../input/section-transitions.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_ab_live`
- set/clear sites: 4 · read sites: 10
  - `scripts/bz_flip.py` L1411: `home.clearProperty('bz_ab_live')`
  - `scripts/bz_flip.py` L1415: `elif not home.getProperty('bz_ab_live') and time.time() - open_t >= 0.3: home.setProperty('bz_ab_live', '1')   # 5.33.207: side-flip fades armed only after MM i`
  - `scripts/bz_flip.py` L1415: `elif not home.getProperty('bz_ab_live') and time.time() - open_t >= 0.3: home.setProperty('bz_ab_live', '1')   # 5.33.207: side-flip fades armed only after MM i`
  - `xml/Includes_Bezel.xml` L755: `<visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_fan_on)) + !String.IsEqual(Window(Home).Property(bz_fan_side),b)</visible><animation effect`
  - `xml/Includes_Bezel.xml` L762: `<visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_fan_on)) + String.IsEqual(Window(Home).Property(bz_fan_side),b)</visible><animation effect=`
  - `xml/Includes_Bezel.xml` L1209: `</control><!-- 5.33.148 MM A/B pos side a --><control type="image"><visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAu`

### `bz_at_gdim`
- set/clear sites: 25 · read sites: 30
  - `xml/Includes_Tuner.xml` L2043: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),gdim) + String.IsEqual(Skin.String(bz_at_gdim),1)">Skin.SetString(bz_at_gdim,2)</onrigh`
  - `xml/Includes_Tuner.xml` L2043: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),gdim) + String.IsEqual(Skin.String(bz_at_gdim),1)">Skin.SetString(bz_at_gdim,2)</onrigh`
  - `xml/Includes_Tuner.xml` L2044: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),gdim) + String.IsEqual(Skin.String(bz_at_gdim),2)">Skin.SetString(bz_at_gdim,1)</onleft>`
  - `xml/Includes_Bezel.xml` L630: `<variable name="BzGDimCol"><value>00FFFFFF</value></variable><!-- 4.7.2: Global dimmer LOOK → MM scrim alpha --><include name="BezelSecDim"><!-- 5.33.147: warm `
  - `xml/Includes_Bezel.xml` L630: `<variable name="BzGDimCol"><value>00FFFFFF</value></variable><!-- 4.7.2: Global dimmer LOOK → MM scrim alpha --><include name="BezelSecDim"><!-- 5.33.147: warm `
  - `xml/Includes_Bezel.xml` L630: `<variable name="BzGDimCol"><value>00FFFFFF</value></variable><!-- 4.7.2: Global dimmer LOOK → MM scrim alpha --><include name="BezelSecDim"><!-- 5.33.147: warm `

### `bz_at_mmdim`
- set/clear sites: 42 · read sites: 542
  - `xml/Includes_Tuner.xml` L2055: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdim) + String.IsEqual(Skin.String(bz_at_mmdim),1)">Skin.SetString(bz_at_mmdim,2)</onr`
  - `xml/Includes_Tuner.xml` L2055: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdim) + String.IsEqual(Skin.String(bz_at_mmdim),1)">Skin.SetString(bz_at_mmdim,2)</onr`
  - `xml/Includes_Tuner.xml` L2056: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdim) + [String.IsEmpty(Skin.String(bz_at_mmdim)) | String.IsEqual(Skin.String(bz_at_m`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`

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

### `bz_gpend`
- set/clear sites: 5 · read sites: 1
  - `xml/MyVideoNav.xml` L23: `<onload condition="Skin.HasSetting(bz_grid_video)">SetProperty(bz_gpend,1,home)</onload><onload>AlarmClock(bzgpend,ClearProperty(bz_gpend,home),00:02,silent)</o`
  - `xml/MyVideoNav.xml` L23: `<onload condition="Skin.HasSetting(bz_grid_video)">SetProperty(bz_gpend,1,home)</onload><onload>AlarmClock(bzgpend,ClearProperty(bz_gpend,home),00:02,silent)</o`
  - `scripts/bz_flip.py` L1161: `home.clearProperty('bz_gpend')   # 4.6.2 nav3: list + grid agree now: show the section`
  - `xml/MyVideoNav.xml` L29: `<animation effect="fade" start="100" end="0" time="0" condition="!String.IsEmpty(Window(Home).Property(bz_secload))">Conditional</animation><animation effect="f`

### `bz_load_then_close`
- set/clear sites: 0 · read sites: 5
  - `xml/MyVideoNav.xml` L28: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`
  - `xml/MyMusicNav.xml` L31: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`
  - `scripts/bz_cmd.py` L400: `def _bz_load_then_close(win, path):`

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

### `bz_secfade`
- set/clear sites: 3 · read sites: 6
  - `scripts/bz_cmd.py` L408: `home.clearProperty('bz_secfade'); home.setProperty('bz_secload', 'true')`
  - `scripts/bz_cmd.py` L431: `home.setProperty('bz_secfade', 'true'); home.clearProperty('bz_secload')`
  - `scripts/bz_cmd.py` L433: `mon.waitForAbort(0.6); home.clearProperty('bz_secfade')`
  - `xml/MyVideoNav.xml` L28: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`
  - `xml/MyVideoNav.xml` L30: `<animation effect="fade" start="0" end="100" time="400" tween="sine" easing="out" condition="!String.IsEmpty(Window(Home).Property(bz_secfade))" reversible="fal`
  - `xml/MyMusicNav.xml` L31: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`

### `bz_secload`
- set/clear sites: 3 · read sites: 6
  - `scripts/bz_cmd.py` L407: `home.clearProperty('bz_secload'); home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez'); return`
  - `scripts/bz_cmd.py` L408: `home.clearProperty('bz_secfade'); home.setProperty('bz_secload', 'true')`
  - `scripts/bz_cmd.py` L431: `home.setProperty('bz_secfade', 'true'); home.clearProperty('bz_secload')`
  - `xml/MyVideoNav.xml` L28: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`
  - `xml/MyVideoNav.xml` L29: `<animation effect="fade" start="100" end="0" time="0" condition="!String.IsEmpty(Window(Home).Property(bz_secload))">Conditional</animation><animation effect="f`
  - `xml/MyMusicNav.xml` L31: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`

