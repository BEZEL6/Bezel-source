# Options + Info — info-options

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `info-options` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/info-options.md) · [layout](../layout/info-options.md) · [state](../state/info-options.md) · [motion](../motion/info-options.md) · [art](../art/info-options.md) · [input](../input/info-options.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
One BEZEL menu replaces both Info and the context menu for Movies, TV and Music. Info, Menu/C or a double-tap Select opens it. It has three pages: Main, More and Section.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_albview_a`
- set/clear sites: 0 · read sites: 9
  - `xml/Includes_Bezel.xml` L126: `<variable name="BzAlbViewLbl"><value condition="Skin.HasSetting(bz_albview_a)">A · 3B ALBUM</value><value>D · SONGS + DISCS</value></variable>`
  - `xml/Includes_Bezel.xml` L372: `<expression name="bz_albd">!Skin.HasSetting(bz_albview_a) + $EXP[bz_inalbum]</expression><!-- 5.33.246 View D in album -->`
  - `xml/Includes_Bezel.xml` L373: `<expression name="bz_discbar">!Skin.HasSetting(bz_albview_a) + $EXP[bz_inalbum] + !ListItem.IsParentFolder + Integer.IsGreater(ListItem.TotalDiscs,1) + [String.`

### `bz_ci_more`
- set/clear sites: 2 · read sites: 100
  - `xml/DialogMusicInfo.xml` L6: `<onload>ClearProperty(bz_ci_more)</onload>`
  - `xml/DialogVideoInfo.xml` L6: `<onload>ClearProperty(bz_ci_more)</onload><!-- t4125: land on Play (row 1); Section options is row 0, Up from Play -->`
  - `xml/Includes_BezelInfo.xml` L20: `<variable name="BzCIHead"><value condition="String.IsEqual(Window.Property(bz_ci_more),sec)">OPTIONS › SECTION</value><value condition="!String.IsEmpty(Window.P`
  - `xml/Includes_BezelInfo.xml` L20: `<variable name="BzCIHead"><value condition="String.IsEqual(Window.Property(bz_ci_more),sec)">OPTIONS › SECTION</value><value condition="!String.IsEmpty(Window.P`
  - `xml/DialogMusicInfo.xml` L14: `<control type="grouplist" id="9000"><left>582</left><top>166</top><width>360</width><height>420</height><itemgap>2</itemgap><orientation>vertical</orientation><`

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

### `bz_tvclear_off`
- set/clear sites: 0 · read sites: 12
  - `xml/Includes_Bezel.xml` L282: `<variable name="BzTVClearOnOff"><value condition="Skin.HasSetting(bz_tvclear_off)">OFF</value><value>ON</value></variable>`
  - `xml/Includes_Bezel.xml` L2408: `<!-- 5.33.180 BUG-025: TV fanart-block upper-left bold show title when no clear art (or bz_tvclear_off); same gates as t4153 strip fallback --><control type="la`
  - `xml/Includes_Bezel.xml` L2408: `<!-- 5.33.180 BUG-025: TV fanart-block upper-left bold show title when no clear art (or bz_tvclear_off); same gates as t4153 strip fallback --><control type="la`

### `bz_xinfo`
- set/clear sites: 5 · read sites: 4
  - `xml/Custom_1111_XInfo.xml` L6: `<onunload>ClearProperty(bz_xinfo,home)</onunload>`
  - `scripts/bz_cmd.py` L131: `home.clearProperty('bz_xinfo'); xbmc.executebuiltin('Dialog.Close(1111)'); xbmc.executebuiltin('SetFocus(60)')`
  - `scripts/bz_cmd.py` L180: `home.setProperty('bz_xinfo', 'true'); xbmc.executebuiltin('ActivateWindow(1111)')`
  - `xml/Includes_Bezel.xml` L3473: `<!-- 3.5.6: in-place extended info (ext_info_inplace). Over the list + colour block region (x 120-959, y 118-999) while bz_xinfo is set`
  - `scripts/bz_cmd.py` L128: `# (bz_xinfo, 550 ms sine), focus starts on PLAY; Back closes; no input for 15 s closes it with the same fade.`
  - `scripts/bz_cmd.py` L134: `if home.getProperty('bz_xinfo') == 'true': close(); sys.exit(0)`

