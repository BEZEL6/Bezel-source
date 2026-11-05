# Confirm dialog — dialog-confirm

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `dialog-confirm` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/dialog-confirm.md) · [layout](../layout/dialog-confirm.md) · [state](../state/dialog-confirm.md) · [motion](../motion/dialog-confirm.md) · [art](../art/dialog-confirm.md) · [input](../input/dialog-confirm.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Kodi's yes/no question in the Main Menu style: a CONFIRM strip with rows and the message on the left. **No** is the first row and gets focus, so a stray Select never confirms by accident. BEZEL uses it for things like "Remove from library".

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_ctx`
- set/clear sites: 0 · read sites: 14
  - `xml/Custom_1119_SecCtx.xml` L45: `<control type="button" id="7904"><label>Favourite</label><onclick>RunScript(special://skin/scripts/bz_ctx.py,fav)</onclick><visible>[Window.IsActive(programs) |`
  - `xml/Custom_1119_SecCtx.xml` L56: `<control type="button" id="7947"><label>Favourite</label><onclick>RunScript(special://skin/scripts/bz_ctx.py,fav)</onclick><visible>Window.IsActive(pictures)</v`
  - `xml/DialogMusicInfo.xml` L14: `<control type="grouplist" id="9000"><left>582</left><top>166</top><width>360</width><height>420</height><itemgap>2</itemgap><orientation>vertical</orientation><`

### `bz_mm28`
- set/clear sites: 0 · read sites: 88
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_mm34`
- set/clear sites: 0 · read sites: 65
  - `xml/Custom_1107_SearchDialog.xml` L63: `<control type="label"><left>480</left><top>20</top><width>350</width><height>50</height><font>bz_mm34</font><textcolor>FFFFFFFF</textcolor><aligny>center</align`
  - `xml/Custom_1132_BzSources.xml` L8: `<control type="label"><left>34</left><top>34</top><width>340</width><height>44</height><aligny>center</aligny><font>bz_mm34</font><textcolor>FFFFFFFF</textcolor`
  - `xml/DialogSlider.xml` L15: `<control type="label" id="10"><left>30</left><top>18</top><width>300</width><height>44</height><font>bz_mm34</font><textcolor>FFFFFFFF</textcolor><label /></con`

