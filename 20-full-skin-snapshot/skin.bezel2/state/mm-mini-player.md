# MM mini-player — mm-mini-player

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `mm-mini-player` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/mm-mini-player.md) · [layout](../layout/mm-mini-player.md) · [state](../state/mm-mini-player.md) · [motion](../motion/mm-mini-player.md) · [art](../art/mm-mini-player.md) · [input](../input/mm-mini-player.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
While something plays, a small player sits on top of the Main Menu. Press Up from MUSIC to reach it. Down goes back to the strip.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_m1121_off`
- set/clear sites: 1 · read sites: 3
  - `xml/Custom_1121_MusicFanartFS.xml` L6: `Kill switch: Skin.SetBool(bz_m1121_off) -> every trigger falls back to ActivateWindow(visualisation).`
  - `xml/Includes_Bezel.xml` L334: `<expression name="bz_m1121ok">!Skin.HasSetting(bz_m1121_off) + Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !Window.IsActive(visualisation)</ex`
  - `xml/Custom_1121_MusicFanartFS.xml` L11: `<onload condition="Skin.HasSetting(bz_m1121_off) | !Player.HasAudio | Player.HasVideo">Dialog.Close(1121,true)</onload>`
  - `xml/Custom_1121_MusicFanartFS.xml` L12: `<onload condition="Skin.HasSetting(bz_m1121_off) + Player.HasAudio + !Player.HasVideo">ActivateWindow(visualisation)</onload>`

### `bz_mm17`
- set/clear sites: 0 · read sites: 163
  - `xml/Custom_1107_SearchDialog.xml` L22: `<control type="label"><left>44</left><top>40</top><width>380</width><height>30</height><font>bz_mm17</font><textcolor>A0FFFFFF</textcolor><label>SEARCH</label><`
  - `xml/Custom_1107_SearchDialog.xml` L61: `<control type="label"><left>44</left><top>836</top><width>380</width><height>30</height><font>bz_mm17</font><textcolor>8CFFFFFF</textcolor><label>OK select   BA`
  - `xml/Custom_1107_SearchDialog.xml` L64: `<control type="label"><left>494</left><top>72</top><width>330</width><height>26</height><font>bz_mm17</font><textcolor>A0FFFFFF</textcolor><label>SELECTED</labe`

### `bz_mm22b`
- set/clear sites: 0 · read sites: 10
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_mmmushide`
- set/clear sites: 0 · read sites: 16
  - `xml/Includes_Bezel.xml` L123: `<expression name="bz_mmmushide">Player.HasAudio + !Player.HasVideo + $EXP[bz_navmenu] + !String.IsEqual(Skin.String(bz_at_warmmusicposters),Off)</expression><!-`
  - `xml/Includes_Bezel.xml` L2559: `<control type="image"><left>990</left><top>120</top><width>600</width><height>900</height><texture>bezel/poster_blur.png</texture><!-- 3.5.1: only while the lis`
  - `xml/Includes_Bezel.xml` L2560: `<control type="image"><left>990</left><top>120</top><width>600</width><height>900</height><texture border="6">bezel/frame.png</texture><visible>!String.IsEmpty(`

### `bz_nav`
- set/clear sites: 75 · read sites: 103
  - `xml/Custom_1107_SearchDialog.xml` L23: `<control type="list" id="9000"><onback>SetProperty(bz_nav,true,home)</onback><onback>Dialog.Close(1107,true)</onback><!-- 5.33.235 Rob t1837: control onback con`
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Custom_1112_NowPlaying.xml` L15: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L16: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L17: `<onload condition="[String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visualis`

### `bz_navbez`
- set/clear sites: 18 · read sites: 36
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_navtune`
- set/clear sites: 21 · read sites: 45
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_np`
- set/clear sites: 33 · read sites: 98
  - `xml/Custom_1112_NowPlaying.xml` L19: `<onunload condition="!Window.IsActive(visualisation)">ClearProperty(bz_np,home)</onunload>`
  - `xml/Custom_1112_NowPlaying.xml` L42: `<onclick>ClearProperty(bz_np,home)</onclick><onclick>Dialog.Close(1112)</onclick></control>`
  - `xml/Custom_1112_NowPlaying.xml` L44: `<control type="button" id="6299"><left>-400</left><top>0</top><width>10</width><height>10</height><label></label><texturefocus></texturefocus><texturenofocus></`
  - `xml/Custom_1112_NowPlaying.xml` L3: `list view (view 60, not the grid): bz_cmd.py np (logo menu entry, 60 s idle open) sets bz_npdlg + bz_np and opens it. Every other route keeps the in-place panel`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L13: `and run Kodi's fullscreen music window (the old route). Opened by bz_cmd.py (menu card, idle) bz_np is already set. -->`

