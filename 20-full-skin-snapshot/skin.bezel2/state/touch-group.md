# Touch / tap inputs — touch-group

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `touch-group` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/touch-group.md) · [layout](../layout/touch-group.md) · [state](../state/touch-group.md) · [motion](../motion/touch-group.md) · [art](../art/touch-group.md) · [input](../input/touch-group.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_at_dtapwin`
- set/clear sites: 58 · read sites: 50
  - `xml/Includes_Tuner.xml` L1062: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtapwin) + String.IsEqual(Skin.String(bz_at_dtapwin),2)">Skin.SetString(bz_at_dtapwin,1)`
  - `xml/Includes_Tuner.xml` L1062: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtapwin) + String.IsEqual(Skin.String(bz_at_dtapwin),2)">Skin.SetString(bz_at_dtapwin,1)`
  - `xml/Includes_Tuner.xml` L1063: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtapwin) + String.IsEqual(Skin.String(bz_at_dtapwin),3)">Skin.SetString(bz_at_dtapwin,2)`
  - `xml/Includes_Tuner.xml` L334: `<variable name="BzATVal_dtapwin"><value condition="String.IsEqual(Skin.String(bz_at_dtapwin),1)">150 ms</value><value condition="String.IsEqual(Skin.String(bz_a`
  - `xml/Includes_Tuner.xml` L334: `<variable name="BzATVal_dtapwin"><value condition="String.IsEqual(Skin.String(bz_at_dtapwin),1)">150 ms</value><value condition="String.IsEqual(Skin.String(bz_a`
  - `xml/Includes_Tuner.xml` L334: `<variable name="BzATVal_dtapwin"><value condition="String.IsEqual(Skin.String(bz_at_dtapwin),1)">150 ms</value><value condition="String.IsEqual(Skin.String(bz_a`

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

