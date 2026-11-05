# Section menu (context) — context-menu

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `context-menu` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/context-menu.md) · [layout](../layout/context-menu.md) · [state](../state/context-menu.md) · [motion](../motion/context-menu.md) · [art](../art/context-menu.md) · [input](../input/context-menu.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
BEZEL replaces Kodi's context menu. Press Menu/C or double-tap Select and you get the BEZEL menu that fits the screen: Options+Info in Movies/TV/Music, this section menu (1119) in the other sections, and Kodi's own menu in the file pickers.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_ctx`
- set/clear sites: 0 · read sites: 14
  - `xml/Custom_1119_SecCtx.xml` L45: `<control type="button" id="7904"><label>Favourite</label><onclick>RunScript(special://skin/scripts/bz_ctx.py,fav)</onclick><visible>[Window.IsActive(programs) |`
  - `xml/Custom_1119_SecCtx.xml` L56: `<control type="button" id="7947"><label>Favourite</label><onclick>RunScript(special://skin/scripts/bz_ctx.py,fav)</onclick><visible>Window.IsActive(pictures)</v`
  - `xml/DialogMusicInfo.xml` L14: `<control type="grouplist" id="9000"><left>582</left><top>166</top><width>360</width><height>420</height><itemgap>2</itemgap><orientation>vertical</orientation><`

### `bz_ctxwarm`
- set/clear sites: 0 · read sites: 4
  - `xml/Includes_Bezel.xml` L365: `<expression name="bz_ctxwarm">[Window.IsVisible(1132) | Window.IsVisible(1117) | [Window.IsVisible(pictures) + [String.IsEmpty(Container.FolderPath) | String.Is`
  - `xml/DialogContextMenu.xml` L13: `<control type="group"><visible>!Window.IsVisible(filebrowser) + !Window.IsVisible(filemanager) + !$EXP[bz_ctxwarm]</visible><include content="BezelStdFrame">`
  - `xml/DialogContextMenu.xml` L26: `<control type="group"><visible>$EXP[bz_ctxwarm]</visible><left>570</left><top>120</top>`

### `bz_dtap`
- set/clear sites: 0 · read sites: 7
  - `xml/Includes_Tuner.xml` L498: `<!-- Kodi resets only the first Visible/Hidden animation of a control, so a changed step must not stay applied: any change marks bz_tune_dirty and bz_dtap.py re`
  - `xml/Includes_Tuner.xml` L2410: `<item><label>5.33.11  Settings strip</label><property name="kind">btn</property><property name="id"></property><property name="info">bezel/info/ver_5_33_10.png<`
  - `scripts/bz_cmd.py` L42: `xbmc.executebuiltin('RunScript(special://skin/scripts/bz_dtap.py)')   # BETA 2.8: double-tap Select service (guards itself)`

### `bz_dtapinfo`
- set/clear sites: 6 · read sites: 0
  - `scripts/bz_dtap.py` L100: `home.setProperty('bz_dtapinfo', '1'); info(); threading.Timer(0.8, lambda: home.clearProperty('bz_dtapinfo')).start(); return`
  - `scripts/bz_dtap.py` L100: `home.setProperty('bz_dtapinfo', '1'); info(); threading.Timer(0.8, lambda: home.clearProperty('bz_dtapinfo')).start(); return`
  - `scripts/bz_dtap.py` L105: `st['pend'] = False; home.setProperty('bz_dtapinfo', '1'); info(); threading.Timer(0.8, lambda: home.clearProperty('bz_dtapinfo')).start()   # 5.0.3 #5: double t`

