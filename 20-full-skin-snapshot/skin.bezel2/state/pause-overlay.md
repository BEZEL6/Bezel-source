# Pause screen (dialog 1116) — pause-overlay

**Object:** `pause-overlay` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/pause-overlay.md) · [layout](../layout/pause-overlay.md) · [state](../state/pause-overlay.md) · [motion](../motion/pause-overlay.md) · [art](../art/pause-overlay.md) · [input](../input/pause-overlay.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_mm18b`
- set/clear sites: 0 · read sites: 6
  - `xml/Custom_1116_PauseScreen.xml` L22: `<control type="label"><left>-540</left><top>728</top><width>500</width><height>28</height><align>right</align><shadowcolor>C0000000</shadowcolor><font>bz_mm18b<`
  - `xml/DialogAddonSettings.xml` L44: `<control type="label" id="14"><height>46</height><font>bz_mm18b</font><textcolor>A0FFFFFF</textcolor><aligny>bottom</aligny><textoffsetx>24</textoffsetx></contr`
  - `xml/Font.xml` L335: `<name>bz_mm18b</name>`

### `bz_mm20`
- set/clear sites: 0 · read sites: 49
  - `xml/Custom_1107_SearchDialog.xml` L65: `<control type="textbox"><left>494</left><top>110</top><width>330</width><height>90</height><font>bz_mm20</font><textcolor>E6FFFFFF</textcolor><label>$INFO[Conta`
  - `xml/Custom_1107_SearchDialog.xml` L67: `<control type="textbox"><left>494</left><top>240</top><width>330</width><height>600</height><font>bz_mm20</font><textcolor>C8FFFFFF</textcolor><label>$INFO[Cont`
  - `xml/LoginScreen.xml` L19: `<control type="textbox"><left>472</left><top>350</top><width>346</width><height>120</height><align>center</align><font>bz_mm20</font><textcolor>E6FFFFFF</textco`

### `bz_mm48b`
- set/clear sites: 0 · read sites: 12
  - `xml/Custom_1116_PauseScreen.xml` L20: `<control type="label"><left>-540</left><top>628</top><width>500</width><height>52</height><align>right</align><shadowcolor>C0000000</shadowcolor><font>bz_mm48b<`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/VideoOSD.xml` L12: `<control type="label"><left>150</left><top>150</top><width>780</width><height>60</height><font>bz_mm48b</font><textcolor>white</textcolor><label>$VAR[BzVOSDTitl`

