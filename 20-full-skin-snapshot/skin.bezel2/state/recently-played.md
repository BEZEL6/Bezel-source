# Recently played — recently-played

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `recently-played` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/recently-played.md) · [layout](../layout/recently-played.md) · [state](../state/recently-played.md) · [motion](../motion/recently-played.md) · [art](../art/recently-played.md) · [input](../input/recently-played.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

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

### `bz_load_then_close`
- set/clear sites: 0 · read sites: 5
  - `xml/MyVideoNav.xml` L28: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`
  - `xml/MyMusicNav.xml` L31: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`
  - `scripts/bz_cmd.py` L400: `def _bz_load_then_close(win, path):`

### `bz_mm`
- set/clear sites: 0 · read sites: 12
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

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

### `bz_rootarm`
- set/clear sites: 2 · read sites: 3
  - `scripts/bz_flip.py` L956: `rp[0] = fp; rp[1] = now - (0.6 if _fresh else 0); rp[2] = _wid; home.clearProperty('bz_rootarm')`
  - `scripts/bz_flip.py` L960: `home.setProperty('bz_rootarm', 'true')`
  - `xml/Includes_Bezel.xml` L2372: `<expression name="bz_atroot">String.IsEqual(Window(Home).Property(bz_rootarm),true) + ![String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Co`
  - `scripts/bz_flip.py` L950: `# (bz_rootarm = that path) before Back counts, so the Back that lands on the top level never opens it`
  - `scripts/bz_flip.py` L958: `elif now - rp[1] >= 0.6 and (fp in ROOTS or (home.getProperty('bz_navroot') and fp.rstrip('/') == home.getProperty('bz_navroot').rstrip('/'))) and home.getPrope`

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

