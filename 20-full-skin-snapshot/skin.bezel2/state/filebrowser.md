# File browser — filebrowser

**Object:** `filebrowser` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/filebrowser.md) · [layout](../layout/filebrowser.md) · [state](../state/filebrowser.md) · [motion](../motion/filebrowser.md) · [art](../art/filebrowser.md) · [input](../input/filebrowser.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Kodi's picker for a file or folder. You browse in the panel, and the OK/Cancel-style buttons sit on the left.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_dtap`
- set/clear sites: 0 · read sites: 7
  - `xml/Includes_Tuner.xml` L498: `<!-- Kodi resets only the first Visible/Hidden animation of a control, so a changed step must not stay applied: any change marks bz_tune_dirty and bz_dtap.py re`
  - `xml/Includes_Tuner.xml` L2410: `<item><label>5.33.11  Settings strip</label><property name="kind">btn</property><property name="id"></property><property name="info">bezel/info/ver_5_33_10.png<`
  - `scripts/bz_cmd.py` L42: `xbmc.executebuiltin('RunScript(special://skin/scripts/bz_dtap.py)')   # BETA 2.8: double-tap Select service (guards itself)`

