# Busy dialog — dialog-busy

**Object:** `dialog-busy` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/dialog-busy.md) · [layout](../layout/dialog-busy.md) · [state](../state/dialog-busy.md) · [motion](../motion/dialog-busy.md) · [art](../art/dialog-busy.md) · [input](../input/dialog-busy.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
It is Kodi's "working…" indicator, restyled. It waits a moment before showing, so quick loads never flash it. It stays out of the way during music, video, caching and flips.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_at_busydelay`
- set/clear sites: 0 · read sites: 6
  - `xml/Includes_Tuner.xml` L11: `<include name="BezelATBusyOpen"><animation effect="fade" start="0" end="100" time="200" delay="150" condition="String.IsEqual(Skin.String(bz_at_busydelay),1)">W`
  - `xml/Includes_Tuner.xml` L11: `<include name="BezelATBusyOpen"><animation effect="fade" start="0" end="100" time="200" delay="150" condition="String.IsEqual(Skin.String(bz_at_busydelay),1)">W`
  - `xml/Includes_Tuner.xml` L11: `<include name="BezelATBusyOpen"><animation effect="fade" start="0" end="100" time="200" delay="150" condition="String.IsEqual(Skin.String(bz_at_busydelay),1)">W`

### `bz_flipping`
- set/clear sites: 5 · read sites: 14
  - `scripts/bz_flip.py` L195: `home.setProperty('bz_flipping', 'true'); home.setProperty('bz_sway_hold', 'true')`
  - `scripts/bz_flip.py` L199: `if not sway.get('busy'): home.clearProperty('bz_flipping')`
  - `scripts/bz_flip.py` L1564: `home.setProperty('bz_flipping', 'true')    # v0.1.23: glares fade out (150 ms) before the sway is held`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L1131: `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="!String.IsEmpty(Window(Home).Property(bz_back)) | !String.IsEmpty`
  - `xml/Includes_Bezel.xml` L1141: `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="!String.IsEmpty(Window(Home).Property(bz_back)) | !String.IsEmpty`

### `bz_tabq`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_flip.py` L933: `if time.time() - tabq[0] > 20: home.clearProperty('bz_tabq'); tabq[0] = 0`
  - `scripts/bz_flip.py` L935: `home.clearProperty('bz_tabq'); tabq[0] = 0`
  - `scripts/bz_flip.py` L931: `if home.getProperty('bz_tabq'):`

