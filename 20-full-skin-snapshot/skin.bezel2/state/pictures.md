# Pictures — pictures

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `pictures` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/pictures.md) · [layout](../layout/pictures.md) · [state](../state/pictures.md) · [motion](../motion/pictures.md) · [art](../art/pictures.md) · [input](../input/pictures.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_ctx`
- set/clear sites: 0 · read sites: 14
  - `xml/Custom_1119_SecCtx.xml` L45: `<control type="button" id="7904"><label>Favourite</label><onclick>RunScript(special://skin/scripts/bz_ctx.py,fav)</onclick><visible>[Window.IsActive(programs) |`
  - `xml/Custom_1119_SecCtx.xml` L56: `<control type="button" id="7947"><label>Favourite</label><onclick>RunScript(special://skin/scripts/bz_ctx.py,fav)</onclick><visible>Window.IsActive(pictures)</v`
  - `xml/DialogMusicInfo.xml` L14: `<control type="grouplist" id="9000"><left>582</left><top>166</top><width>360</width><height>420</height><itemgap>2</itemgap><orientation>vertical</orientation><`

### `bz_dtap`
- set/clear sites: 0 · read sites: 7
  - `xml/Includes_Tuner.xml` L498: `<!-- Kodi resets only the first Visible/Hidden animation of a control, so a changed step must not stay applied: any change marks bz_tune_dirty and bz_dtap.py re`
  - `xml/Includes_Tuner.xml` L2410: `<item><label>5.33.11  Settings strip</label><property name="kind">btn</property><property name="id"></property><property name="info">bezel/info/ver_5_33_10.png<`
  - `scripts/bz_cmd.py` L42: `xbmc.executebuiltin('RunScript(special://skin/scripts/bz_dtap.py)')   # BETA 2.8: double-tap Select service (guards itself)`

### `bz_fan_a`
- set/clear sites: 0 · read sites: 6
  - `xml/Includes_Bezel.xml` L759: `<texture background="true">$INFO[Window(Home).Property(bz_fan_a)]</texture>`
  - `xml/Includes_Bezel.xml` L2318: `<include name="View_63_BezelPictureList"><!-- 5.33.242 Rob t1862u: Pictures on the Warm strip (MM/Media Sources language). List 63 lives IN the colour strip at `
  - `xml/Custom_1117_MediaSources.xml` L13: `<!-- 5.33.233 Rob t1830: fanart flash on open — lane loads sync (MM already cached it, no empty frame) + black cover hides StdFrame bz_backdrop (fadetime 200) s`

### `bz_fan_on`
- set/clear sites: 0 · read sites: 11
  - `xml/Includes_Bezel.xml` L715: `<expression name="bz_warmhold">$EXP[bz_navmenu] + !String.IsEqual(Skin.String(bz_at_warmhold),Off) + !String.IsEmpty(Window(Home).Property(bz_fan_on))</expressi`
  - `xml/Includes_Bezel.xml` L748: `<visible>$EXP[bz_navmenu] + String.IsEmpty(Window(Home).Property(bz_fan_on))</visible>`
  - `xml/Includes_Bezel.xml` L755: `<visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_fan_on)) + !String.IsEqual(Window(Home).Property(bz_fan_side),b)</visible><animation effect`

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

