# Keyboard (DialogKeyboard 10103) — keyboard

**Object:** `keyboard` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/keyboard.md) · [layout](../layout/keyboard.md) · [state](../state/keyboard.md) · [motion](../motion/keyboard.md) · [art](../art/keyboard.md) · [input](../input/keyboard.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
- Over Music info (Refresh flow) → `BzRefreshKeyboard` (strip-format 10×10 grid). - File Manager (`filemanager`) → `BzStdKeyboard` (wide MM block, popup anim) — File Manager left stock by Rob. - Everywhere else (Search, Add/Edit Source, rename, playlist name, add-on text settings, etc.) → `BzStripKe

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_kb`
- set/clear sites: 0 · read sites: 53
  - `xml/Includes_BezelDialogs.xml` L586: `<item><label>$VAR[BzKbCase0]</label><onclick>RunScript(special://skin/scripts/bz_kb.py,a,0)</onclick></item>`
  - `xml/Includes_BezelDialogs.xml` L587: `<item><label>$VAR[BzKbCase1]</label><onclick>RunScript(special://skin/scripts/bz_kb.py,a,1)</onclick></item>`
  - `xml/Includes_BezelDialogs.xml` L588: `<item><label>$VAR[BzKbCase2]</label><onclick>RunScript(special://skin/scripts/bz_kb.py,a,2)</onclick></item>`

### `bz_kbcaps`
- set/clear sites: 5 · read sites: 28
  - `xml/Includes_BezelDialogs.xml` L576: `<onup>9601</onup><ondown>9601</ondown><onleft condition="String.IsEmpty(Window(Home).Property(bz_kbcaps))">SetProperty(bz_kbcaps,1,home)</onleft><onleft conditi`
  - `xml/Includes_BezelDialogs.xml` L576: `<onup>9601</onup><ondown>9601</ondown><onleft condition="String.IsEmpty(Window(Home).Property(bz_kbcaps))">SetProperty(bz_kbcaps,1,home)</onleft><onleft conditi`
  - `xml/Includes_BezelDialogs.xml` L576: `<onup>9601</onup><ondown>9601</ondown><onleft condition="String.IsEmpty(Window(Home).Property(bz_kbcaps))">SetProperty(bz_kbcaps,1,home)</onleft><onleft conditi`
  - `xml/Includes_BezelDialogs.xml` L536: `<variable name="BzKbCapsLbl"><value condition="!String.IsEmpty(Window(Home).Property(bz_kbcaps))">ABC</value><value>abc</value></variable>`
  - `xml/Includes_BezelDialogs.xml` L537: `<variable name="BzKbCase0"><value condition="!String.IsEmpty(Window(Home).Property(bz_kbcaps))">A</value><value>a</value></variable>`
  - `xml/Includes_BezelDialogs.xml` L538: `<variable name="BzKbCase1"><value condition="!String.IsEmpty(Window(Home).Property(bz_kbcaps))">B</value><value>b</value></variable>`

