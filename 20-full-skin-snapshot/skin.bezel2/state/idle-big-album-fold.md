# Idle Big Album fold (book-page leaf) — idle-big-album-fold

**Object:** `idle-big-album-fold` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/idle-big-album-fold.md) · [layout](../layout/idle-big-album-fold.md) · [state](../state/idle-big-album-fold.md) · [motion](../motion/idle-big-album-fold.md) · [art](../art/idle-big-album-fold.md) · [input](../input/idle-big-album-fold.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
When Music is idle (nothing playing) and list 60 is focused, the big album turns like a book page every 10 s. The cover is cut down the middle. The right half lifts off the slit and swings toward you, and the next cover shows underneath. Then the next cover's left half lands over the old left half. The page is solid, the shadows sell the lift and landing, the white border stays sliced and rides with the page, and the glare never pops.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

**See screen:** [idle-big-album-fold baselines](../port-refs/idle-big-album-fold/) — smoke baseline + port diff target.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_at_gdim`
- set/clear sites: 25 · read sites: 30
  - `xml/Includes_Tuner.xml` L2043: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),gdim) + String.IsEqual(Skin.String(bz_at_gdim),1)">Skin.SetString(bz_at_gdim,2)</onrigh`
  - `xml/Includes_Tuner.xml` L2043: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),gdim) + String.IsEqual(Skin.String(bz_at_gdim),1)">Skin.SetString(bz_at_gdim,2)</onrigh`
  - `xml/Includes_Tuner.xml` L2044: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),gdim) + String.IsEqual(Skin.String(bz_at_gdim),2)">Skin.SetString(bz_at_gdim,1)</onleft>`
  - `xml/Includes_Bezel.xml` L630: `<variable name="BzGDimCol"><value>00FFFFFF</value></variable><!-- 4.7.2: Global dimmer LOOK → MM scrim alpha --><include name="BezelSecDim"><!-- 5.33.147: warm `
  - `xml/Includes_Bezel.xml` L630: `<variable name="BzGDimCol"><value>00FFFFFF</value></variable><!-- 4.7.2: Global dimmer LOOK → MM scrim alpha --><include name="BezelSecDim"><!-- 5.33.147: warm `
  - `xml/Includes_Bezel.xml` L630: `<variable name="BzGDimCol"><value>00FFFFFF</value></variable><!-- 4.7.2: Global dimmer LOOK → MM scrim alpha --><include name="BezelSecDim"><!-- 5.33.147: warm `

### `bz_back`
- set/clear sites: 4 · read sites: 27
  - `xml/Includes_Bezel.xml` L646: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !String.IsEmpty(Window(Home).Property(bz_back))">SetProperty(bz_back_clos`
  - `xml/MyMusicNav.xml` L13: `<onload>ClearProperty(bz_back,home)</onload>`
  - `scripts/bz_flip.py` L279: `home.clearProperty('bz_back'); on = False`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L455: `<visible>Player.HasAudio + !String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_back_fade))</visible>`
  - `xml/Includes_Bezel.xml` L647: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !!String.IsEmpty(Window(Home).Property(bz_back)) + Control.IsVisible(60)"`

### `bz_flip`
- set/clear sites: 1 · read sites: 69
  - `xml/MyVideoNav.xml` L23: `<onload condition="Skin.HasSetting(bz_grid_video)">SetProperty(bz_gpend,1,home)</onload><onload>AlarmClock(bzgpend,ClearProperty(bz_gpend,home),00:02,silent)</o`
  - `xml/MyPlaylist.xml` L9: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L14: `<!-- BETA 1.1b: the gate below uses Player.HasAudio directly (the debounced bz_audio_latch from bz_flip.py may not be set yet on the first Tab after Kodi start;`

### `bz_frame_half_l`
- set/clear sites: 0 · read sites: 2
  - `xml/Includes_Bezel.xml` L1101: `<control type="image"><left>1440</left><top>220</top><width>300</width><height>600</height><aspectratio align="right">scale</aspectratio><fadetime>0</fadetime><`
  - `xml/Includes_Bezel.xml` L1107: `<control type="image"><left>1140</left><top>220</top><width>300</width><height>600</height><aspectratio align="left">scale</aspectratio><fadetime>0</fadetime><t`

### `bz_frame_soft`
- set/clear sites: 0 · read sites: 6
  - `xml/Includes_Bezel.xml` L1021: `<control type="image"><left>-1</left><top>-1</top><width>542</width><height>542</height><texture border="8">bezel/bz_frame_soft.png</texture></control><!-- 5.33`
  - `xml/Includes_Bezel.xml` L1033: `<control type="image"><left>-1</left><top>-1</top><width>542</width><height>542</height><texture border="8">bezel/bz_frame_soft.png</texture></control><!-- 5.33`
  - `xml/Includes_Bezel.xml` L1112: `<left>1139</left><top>219</top><width>602</width><height>602</height><!-- BETA 2.6: +2 px transparent pad (bz_frame_soft) so the rotated frame edge antialiases;`

### `bz_hf_a`
- set/clear sites: 2 · read sites: 8
  - `scripts/bz_flip.py` L1492: `home.setProperty('bz_hf_a', cv[idx]); home.setProperty('bz_hf_b', cv[nxt])`
  - `scripts/bz_flip.py` L1500: `home.setProperty('bz_hf_a', cv[nxt]); home.clearProperty('bz_hf_ph'); idx = nxt; t0 = time.time()   # seamless: A := B (same pixels)`
  - `xml/Includes_Bezel.xml` L1094: `bz_flip.py idle_hinge(): bz_hf_a = shown cover, bz_hf_b = next, bz_hf_ph 1 = right half of A swings 0 -> -90 (2200 ms sine in, 5.33.245 slow fold), 2 = left hal`
  - `xml/Includes_Bezel.xml` L1096: `<control type="group"><visible>!Player.HasAudio + Window.IsActive(music) + !String.IsEmpty(Window(Home).Property(bz_hf_a))</visible><camera x="1440" y="520"/><!`
  - `xml/Includes_Bezel.xml` L1100: `<control type="image"><left>1140</left><top>220</top><width>300</width><height>600</height><aspectratio align="left">scale</aspectratio><fadetime>0</fadetime><t`

### `bz_hf_b`
- set/clear sites: 1 · read sites: 5
  - `scripts/bz_flip.py` L1492: `home.setProperty('bz_hf_a', cv[idx]); home.setProperty('bz_hf_b', cv[nxt])`
  - `xml/Includes_Bezel.xml` L1094: `bz_flip.py idle_hinge(): bz_hf_a = shown cover, bz_hf_b = next, bz_hf_ph 1 = right half of A swings 0 -> -90 (2200 ms sine in, 5.33.245 slow fold), 2 = left hal`
  - `xml/Includes_Bezel.xml` L1101: `<control type="image"><left>1440</left><top>220</top><width>300</width><height>600</height><aspectratio align="right">scale</aspectratio><fadetime>0</fadetime><`
  - `xml/Includes_Bezel.xml` L1107: `<control type="image"><left>1140</left><top>220</top><width>300</width><height>600</height><aspectratio align="left">scale</aspectratio><fadetime>0</fadetime><t`

### `bz_hf_ph`
- set/clear sites: 2 · read sites: 25
  - `scripts/bz_flip.py` L1497: `home.setProperty('bz_hf_ph', ph)`
  - `scripts/bz_flip.py` L1500: `home.setProperty('bz_hf_a', cv[nxt]); home.clearProperty('bz_hf_ph'); idx = nxt; t0 = time.time()   # seamless: A := B (same pixels)`
  - `xml/Includes_Bezel.xml` L1094: `bz_flip.py idle_hinge(): bz_hf_a = shown cover, bz_hf_b = next, bz_hf_ph 1 = right half of A swings 0 -> -90 (2200 ms sine in, 5.33.245 slow fold), 2 = left hal`
  - `xml/Includes_Bezel.xml` L1101: `<control type="image"><left>1440</left><top>220</top><width>300</width><height>600</height><aspectratio align="right">scale</aspectratio><fadetime>0</fadetime><`
  - `xml/Includes_Bezel.xml` L1101: `<control type="image"><left>1440</left><top>220</top><width>300</width><height>600</height><aspectratio align="right">scale</aspectratio><fadetime>0</fadetime><`

### `bz_nav`
- set/clear sites: 75 · read sites: 103
  - `xml/Custom_1107_SearchDialog.xml` L23: `<control type="list" id="9000"><onback>SetProperty(bz_nav,true,home)</onback><onback>Dialog.Close(1107,true)</onback><!-- 5.33.235 Rob t1837: control onback con`
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Custom_1112_NowPlaying.xml` L15: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L16: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L17: `<onload condition="[String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visualis`

### `bz_randpend`
- set/clear sites: 8 · read sites: 1
  - `scripts/bz_flip.py` L582: `finally: home.clearProperty('bz_randpend')   # 5.33.226 RANDFLASH: always release the list alpha`
  - `scripts/bz_flip.py` L598: `home.setProperty('bz_randpend', '1')   # 5.33.226 RANDFLASH (t1796u): list 60 alpha 0 until the random row lands (no row-1 flash)`
  - `scripts/bz_flip.py` L605: `if not ok[0]: home.clearProperty('bz_randpend')   # 5.33.230: no deferred apply -> release now`
  - `scripts/bz_flip.py` L1465: `and not home.getProperty('bz_randpend') and not home.getProperty('bz_back'))`

