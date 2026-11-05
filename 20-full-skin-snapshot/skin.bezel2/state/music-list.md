# Music section list — music-list

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `music-list` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-list.md) · [layout](../layout/music-list.md) · [state](../state/music-list.md) · [motion](../motion/music-list.md) · [art](../art/music-list.md) · [input](../input/music-list.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

**See screen:** [music-list baselines](../port-refs/music-list/) — smoke baseline + port diff target.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_albd`
- set/clear sites: 0 · read sites: 4
  - `xml/Includes_Bezel.xml` L372: `<expression name="bz_albd">!Skin.HasSetting(bz_albview_a) + $EXP[bz_inalbum]</expression><!-- 5.33.246 View D in album -->`
  - `xml/Includes_Bezel.xml` L2198: `<control type="group"><visible>$EXP[bz_covercol]</visible><animation effect="fade" start="100" end="0" time="1000" tween="sine" easing="inout" condition="String`
  - `xml/Includes_Bezel.xml` L2199: `<!-- 3.2.0 item 5: album list: rows that slide up under the 450 cover are hidden by redrawing the cover above the list --><control type="group"><visible>$EXP[bz`

### `bz_albva`
- set/clear sites: 2 · read sites: 3
  - `scripts/bz_flip.py` L472: `last = key; home.setProperty('bz_albva', '1')`
  - `scripts/bz_flip.py` L475: `last = None; home.clearProperty('bz_albva')`
  - `xml/Includes_Bezel.xml` L371: `<expression name="bz_ameta">Control.HasFocus(6095) | Control.HasFocus(6096) | !String.IsEmpty(Window(Home).Property(bz_albva)) | !String.IsEmpty(Window(Home).Pr`
  - `scripts/bz_flip.py` L464: `def albview_a():   # 5.33.237 t1843 view A: hold 3B album panel at album/disc level (bz_albva); D (default) = disc headers in list rows`
  - `scripts/bz_flip.py` L474: `elif last is not None or home.getProperty('bz_albva'):`

### `bz_albvd`
- set/clear sites: 3 · read sites: 5
  - `scripts/bz_flip.py` L490: `if home.getProperty('bz_albvd') != '1': home.setProperty('bz_albvd', '1')`
  - `scripts/bz_flip.py` L490: `if home.getProperty('bz_albvd') != '1': home.setProperty('bz_albvd', '1')`
  - `scripts/bz_flip.py` L492: `home.clearProperty('bz_albvd')`
  - `xml/Includes_Bezel.xml` L371: `<expression name="bz_ameta">Control.HasFocus(6095) | Control.HasFocus(6096) | !String.IsEmpty(Window(Home).Property(bz_albva)) | !String.IsEmpty(Window(Home).Pr`
  - `xml/Includes_Bezel.xml` L371: `<expression name="bz_ameta">Control.HasFocus(6095) | Control.HasFocus(6096) | !String.IsEmpty(Window(Home).Property(bz_albva)) | !String.IsEmpty(Window(Home).Pr`
  - `xml/Includes_Bezel.xml` L375: `<control type="group"><left>570</left><top>120</top><visible>$EXP[bz_ameta] + !$EXP[bz_infoup] + [String.IsEmpty(Window(Home).Property(bz_albvd)) | Control.HasF`

### `bz_albview_a`
- set/clear sites: 0 · read sites: 9
  - `xml/Includes_Bezel.xml` L126: `<variable name="BzAlbViewLbl"><value condition="Skin.HasSetting(bz_albview_a)">A · 3B ALBUM</value><value>D · SONGS + DISCS</value></variable>`
  - `xml/Includes_Bezel.xml` L372: `<expression name="bz_albd">!Skin.HasSetting(bz_albview_a) + $EXP[bz_inalbum]</expression><!-- 5.33.246 View D in album -->`
  - `xml/Includes_Bezel.xml` L373: `<expression name="bz_discbar">!Skin.HasSetting(bz_albview_a) + $EXP[bz_inalbum] + !ListItem.IsParentFolder + Integer.IsGreater(ListItem.TotalDiscs,1) + [String.`

### `bz_allret`
- set/clear sites: 3 · read sites: 1
  - `scripts/bz_cmd.py` L561: `xbmcgui.Window(10000).setProperty('bz_allret', fp)  # 5.33.95: Back from All lands on the ALL row, not the parked Disc 2`
  - `scripts/bz_flip.py` L318: `home.clearProperty('bz_allret'); xbmc.executebuiltin('SetFocus(%d)' % _ab); sw_prev[0] = 0; sw_path[0] = _fp`
  - `scripts/bz_flip.py` L321: `elif _ar and _fp != _ar and '/-1/' not in _fp: home.clearProperty('bz_allret')`
  - `scripts/bz_flip.py` L316: `_ar = home.getProperty('bz_allret')`

### `bz_allrow`
- set/clear sites: 0 · read sites: 4
  - `xml/Includes_Bezel.xml` L101: `<!-- ALLROW (Rob t3729/t3730): stock All hidden (showallitems off), bottom row opens the same All path --><!-- 5.0.3 t3972 --><variable name="BzListHiText"><val`
  - `xml/Includes_Bezel.xml` L104: `<expression name="bz_mdiscpick">Window.IsActive(music) + String.StartsWith(Container.FolderPath,musicdb://albums/) + !String.IsEqual(Container.FolderPath,musicd`
  - `xml/Includes_Bezel.xml` L2196: `</control></control><!-- t4533 end clip --><control type="button" id="6097"><!-- ALLROW --><visible>!$EXP[bz_covercol] | $EXP[bz_allpick]</visible><animation ef`

### `bz_allup`
- set/clear sites: 2 · read sites: 8
  - `scripts/bz_flip.py` L334: `if _prev and _prev > _pos and xbmc.getCondVisibility('Control.IsVisible(6097)'): home.setProperty('bz_allup', str(_n)); xbmc.executebuiltin('SetFocus(6097)')  #`
  - `scripts/bz_flip.py` L338: `if _prev and _prev > _pos and xbmc.getCondVisibility('Control.IsVisible(6098)'): home.setProperty('bz_allup', str(_n)); xbmc.executebuiltin('SetFocus(6098)')  #`
  - `xml/Includes_Bezel.xml` L2196: `</control></control><!-- t4533 end clip --><control type="button" id="6097"><!-- ALLROW --><visible>!$EXP[bz_covercol] | $EXP[bz_allpick]</visible><animation ef`
  - `xml/Includes_Bezel.xml` L2196: `</control></control><!-- t4533 end clip --><control type="button" id="6097"><!-- ALLROW --><visible>!$EXP[bz_covercol] | $EXP[bz_allpick]</visible><animation ef`
  - `xml/Includes_Bezel.xml` L2196: `</control></control><!-- t4533 end clip --><control type="button" id="6097"><!-- ALLROW --><visible>!$EXP[bz_covercol] | $EXP[bz_allpick]</visible><animation ef`

### `bz_am_`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_artist.py` L9: `W.clearProperty('bz_am_' + k)`
  - `scripts/bz_artist.py` L37: `W.clearProperty('bz_am_' + k)`
  - `scripts/bz_artist.py` L6: `# 5.33.224 3B artist meta: Home props bz_am_* for BezelArtistMeta3B`

### `bz_am_counts`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_artist.py` L27: `W.setProperty('bz_am_counts', '%d album%s  \u00b7  %d song%s' % (na, '' if na == 1 else 's', ns, '' if ns == 1 else 's'))`
  - `scripts/bz_artist.py` L60: `W.setProperty('bz_am_counts', '  \u00b7  '.join(bits))`
  - `xml/Includes_Bezel.xml` L380: `<control type="group"><animation effect="slide" start="0,0" end="0,-58" time="0" condition="String.IsEmpty(Window(Home).Property(bz_am_n2))">Conditional</animat`

### `bz_am_g1`
- set/clear sites: 0 · read sites: 0

### `bz_am_n1`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_artist.py` L29: `W.setProperty('bz_am_n1', w[0]); W.setProperty('bz_am_n2', w[1] if len(w) > 1 else '')`
  - `scripts/bz_artist.py` L62: `W.setProperty('bz_am_n1', w[0]); W.setProperty('bz_am_n2', w[1] if len(w) > 1 else '')`
  - `xml/Includes_Bezel.xml` L378: `<control type="label"><left>30</left><top>400</top><width>330</width><height>62</height><font>bz_b46</font><textcolor>FFFFFFFF</textcolor><aligny>center</aligny`

### `bz_am_n2`
- set/clear sites: 2 · read sites: 2
  - `scripts/bz_artist.py` L29: `W.setProperty('bz_am_n1', w[0]); W.setProperty('bz_am_n2', w[1] if len(w) > 1 else '')`
  - `scripts/bz_artist.py` L62: `W.setProperty('bz_am_n1', w[0]); W.setProperty('bz_am_n2', w[1] if len(w) > 1 else '')`
  - `xml/Includes_Bezel.xml` L379: `<control type="label"><left>30</left><top>458</top><width>330</width><height>62</height><font>bz_m44</font><textcolor>FFFFFFFF</textcolor><aligny>center</aligny`
  - `xml/Includes_Bezel.xml` L380: `<control type="group"><animation effect="slide" start="0,0" end="0,-58" time="0" condition="String.IsEmpty(Window(Home).Property(bz_am_n2))">Conditional</animat`

### `bz_am_thumb`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_artist.py` L30: `W.setProperty('bz_am_thumb', thumb)`
  - `scripts/bz_artist.py` L63: `W.setProperty('bz_am_thumb', a.get('thumbnail') or a.get('fanart') or '')`
  - `xml/Includes_Bezel.xml` L377: `<control type="image"><left>30</left><top>40</top><width>330</width><height>330</height><aspectratio scalediffuse="false">scale</aspectratio><fadetime>150</fade`

### `bz_ameta`
- set/clear sites: 0 · read sites: 11
  - `xml/Includes_Bezel.xml` L371: `<expression name="bz_ameta">Control.HasFocus(6095) | Control.HasFocus(6096) | !String.IsEmpty(Window(Home).Property(bz_albva)) | !String.IsEmpty(Window(Home).Pr`
  - `xml/Includes_Bezel.xml` L375: `<control type="group"><left>570</left><top>120</top><visible>$EXP[bz_ameta] + !$EXP[bz_infoup] + [String.IsEmpty(Window(Home).Property(bz_albvd)) | Control.HasF`
  - `xml/Includes_Bezel.xml` L1440: `<visible>!$EXP[bz_infoup] + !$EXP[bz_ameta]</visible><animation effect="fade" start="100" end="0" time="150">Hidden</animation><!-- t4142: music strip content h`

### `bz_artbtn`
- set/clear sites: 0 · read sites: 6
  - `xml/Includes_Bezel.xml` L369: `<expression name="bz_artbtn">Window.IsActive(music) + [Container.Content(songs) | [Container.Content(albums) + !$EXP[bz_artistalbums]]] + !Container(60).ListIte`
  - `xml/Includes_Bezel.xml` L1465: `<include content="BezelArtistBtn"><param name="id" value="6095"/><param name="h" value="46"/><param name="vis" value="$EXP[bz_artbtn] + Container.Content(songs)`
  - `xml/Includes_Bezel.xml` L1466: `<include content="BezelArtistBtn"><param name="id" value="6096"/><param name="h" value="66"/><param name="vis" value="$EXP[bz_artbtn] + Container.Content(albums`

### `bz_artist`
- set/clear sites: 0 · read sites: 8
  - `xml/Includes_Bezel.xml` L374: `<include name="BezelArtistMeta3B"><definition><!-- 5.33.224 Rob t1770 option 3B: large artist art + split name (bold / regular), counts plain, genre pills only `
  - `xml/Includes_Bezel.xml` L408: `<onfocus condition="Container.Content(songs)">RunScript(special://skin/scripts/bz_artist.py,meta,song,$INFO[Container(60).ListItem.DBID],$INFO[Container(60).Lis`
  - `xml/Includes_Bezel.xml` L408: `<onfocus condition="Container.Content(songs)">RunScript(special://skin/scripts/bz_artist.py,meta,song,$INFO[Container(60).ListItem.DBID],$INFO[Container(60).Lis`

### `bz_artmeta_ok`
- set/clear sites: 0 · read sites: 1
  - `xml/Includes_Bezel.xml` L370: `<expression name="bz_artmeta_ok">Window.IsActive(music) + Container.Content(artists) + !Container(60).ListItem.IsParentFolder + !Control.IsVisible(6600) + !Stri`

### `bz_at_fsslide`
- set/clear sites: 24 · read sites: 118
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`
  - `xml/Custom_1112_NowPlaying.xml` L37: `<control type="group"><animation effect="slide" start="0,0" end="-1100,0" time="480" tween="sine" easing="inout" condition="[Window.IsActive(1120) | [Window.IsA`

### `bz_atnavroot`
- set/clear sites: 3 · read sites: 1
  - `scripts/bz_flip.py` L961: `if fp not in ROOTS: home.setProperty('bz_atnavroot', 'true')`
  - `scripts/bz_flip.py` L963: `if home.getProperty('bz_atnavroot'): home.clearProperty('bz_atnavroot')`
  - `scripts/bz_flip.py` L963: `if home.getProperty('bz_atnavroot'): home.clearProperty('bz_atnavroot')`
  - `xml/Includes_Bezel.xml` L2372: `<expression name="bz_atroot">String.IsEqual(Window(Home).Property(bz_rootarm),true) + ![String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Co`

### `bz_atroot`
- set/clear sites: 0 · read sites: 5
  - `xml/Includes_Bezel.xml` L1594: `<onback condition="String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Container.FolderPath,sources://)">ActivateWindow(1117)</onback><onback `
  - `xml/Includes_Bezel.xml` L1594: `<onback condition="String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Container.FolderPath,sources://)">ActivateWindow(1117)</onback><onback `
  - `xml/Includes_Bezel.xml` L2372: `<expression name="bz_atroot">String.IsEqual(Window(Home).Property(bz_rootarm),true) + ![String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Co`

### `bz_audio_latch`
- set/clear sites: 4 · read sites: 47
  - `scripts/bz_flip.py` L946: `if home.getProperty('bz_np') and home.getProperty('bz_audio_latch') != 'true': home.clearProperty('bz_np')`
  - `scripts/bz_flip.py` L1516: `home.setProperty('bz_audio_latch', 'true'); sway['t0'] = time.time()   # sway (keyed on the latch) starts from flat`
  - `scripts/bz_flip.py` L1519: `if gone >= 2.5 or xbmc.getCondVisibility('Player.HasVideo'): home.clearProperty('bz_audio_latch'); gone = 0.0; sway['t0'] = None; had = False`
  - `xml/Custom_1112_NowPlaying.xml` L14: `<!-- BETA 1.1b: the gate below uses Player.HasAudio directly (the debounced bz_audio_latch from bz_flip.py may not be set yet on the first Tab after Kodi start;`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L125: `<expression name="bz_audio">[Player.HasAudio + !Player.HasVideo] | String.IsEqual(Window(Home).Property(bz_audio_latch),true)</expression>`

### `bz_b46`
- set/clear sites: 0 · read sites: 16
  - `xml/Custom_1119_SecCtx.xml` L13: `<control type="grouplist"><left>150</left><top>150</top><width>400</width><height>320</height><itemgap>6</itemgap><usecontrolheight>true</usecontrolheight><cont`
  - `xml/DialogPVRInfo.xml` L11: `<control type="grouplist"><left>150</left><top>150</top><width>400</width><height>320</height><itemgap>6</itemgap><usecontrolheight>true</usecontrolheight><cont`
  - `xml/Includes_Bezel.xml` L378: `<control type="label"><left>30</left><top>400</top><width>330</width><height>62</height><font>bz_b46</font><textcolor>FFFFFFFF</textcolor><aligny>center</aligny`

### `bz_bottomedge`
- set/clear sites: 1 · read sites: 1
  - `xml/Includes_Bezel.xml` L2699: `<onup>SetProperty(bz_topedge,1,home)</onup><ondown condition="Control.IsVisible(6098)">6098</ondown><!-- t4357: numeric nav = no native wrap flash --><ondown>Se`
  - `xml/Includes_Bezel.xml` L1570: `<onright condition="$EXP[bz_artbtn] + Container.Content(songs) + [!Player.HasAudio | !Control.IsVisible(6160)]">SetFocus(6095)</onright><onright condition="$EXP`

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_discbar`
- set/clear sites: 0 · read sites: 37
  - `xml/Includes_Bezel.xml` L373: `<expression name="bz_discbar">!Skin.HasSetting(bz_albview_a) + $EXP[bz_inalbum] + !ListItem.IsParentFolder + Integer.IsGreater(ListItem.TotalDiscs,1) + [String.`
  - `xml/Includes_Bezel.xml` L1620: `<control type="label"><animation effect="slide" start="0,0" end="0,13" time="0" condition="$EXP[bz_discbar]">Conditional</animation><!-- 5.33.246 D: text under `
  - `xml/Includes_Bezel.xml` L1626: `<control type="label"><animation effect="slide" start="0,0" end="0,13" time="0" condition="$EXP[bz_discbar]">Conditional</animation><!-- 5.33.246 D: text under `

### `bz_flip`
- set/clear sites: 1 · read sites: 69
  - `xml/MyVideoNav.xml` L23: `<onload condition="Skin.HasSetting(bz_grid_video)">SetProperty(bz_gpend,1,home)</onload><onload>AlarmClock(bzgpend,ClearProperty(bz_gpend,home),00:02,silent)</o`
  - `xml/MyPlaylist.xml` L9: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L14: `<!-- BETA 1.1b: the gate below uses Player.HasAudio directly (the debounced bz_audio_latch from bz_flip.py may not be set yet on the first Tab after Kodi start;`

### `bz_hf_a`
- set/clear sites: 2 · read sites: 8
  - `scripts/bz_flip.py` L1492: `home.setProperty('bz_hf_a', cv[idx]); home.setProperty('bz_hf_b', cv[nxt])`
  - `scripts/bz_flip.py` L1500: `home.setProperty('bz_hf_a', cv[nxt]); home.clearProperty('bz_hf_ph'); idx = nxt; t0 = time.time()   # seamless: A := B (same pixels)`
  - `xml/Includes_Bezel.xml` L1094: `bz_flip.py idle_hinge(): bz_hf_a = shown cover, bz_hf_b = next, bz_hf_ph 1 = right half of A swings 0 -> -90 (2200 ms sine in, 5.33.245 slow fold), 2 = left hal`
  - `xml/Includes_Bezel.xml` L1096: `<control type="group"><visible>!Player.HasAudio + Window.IsActive(music) + !String.IsEmpty(Window(Home).Property(bz_hf_a))</visible><camera x="1440" y="520"/><!`
  - `xml/Includes_Bezel.xml` L1100: `<control type="image"><left>1140</left><top>220</top><width>300</width><height>600</height><aspectratio align="left">scale</aspectratio><fadetime>0</fadetime><t`

### `bz_inalbum`
- set/clear sites: 0 · read sites: 8
  - `xml/Includes_Bezel.xml` L110: `<expression name="bz_inalbum">Window.IsActive(music) + Container.Content(songs) + [String.StartsWith(Container.FolderPath,musicdb://albums/) | String.StartsWith`
  - `xml/Includes_Bezel.xml` L121: `<expression name="bz_covercol">$EXP[bz_inalbum] | $EXP[bz_artistalbums] | [Window.IsActive(music) + Container.Content(albums) + Skin.HasSetting(bz_albumlist) + `
  - `xml/Includes_Bezel.xml` L372: `<expression name="bz_albd">!Skin.HasSetting(bz_albview_a) + $EXP[bz_inalbum]</expression><!-- 5.33.246 View D in album -->`

### `bz_infoup`
- set/clear sites: 1 · read sites: 109
  - `xml/Includes_Bezel.xml` L2335: `<control type="list" id="63"><onback condition="[String.IsEmpty(Container.FolderPath) | String.IsEqual(Container.FolderPath,sources://pictures/)] + !$EXP[bz_nav`
  - `xml/Includes_Bezel.xml` L44: `<control type="group"><visible>!Window.IsActive(1120) + !Skin.HasSetting(bz_dtap_off) + [Control.IsVisible(60) | Control.IsVisible(63) | [Control.IsVisible(50) `
  - `xml/Includes_Bezel.xml` L361: `<expression name="bz_infoup">Window.IsVisible(movieinformation) | Window.IsVisible(musicinformation) | Window.IsVisible(songinformation) | Window.IsVisible(pict`
  - `xml/Includes_Bezel.xml` L362: `<expression name="bz_lsthide">$EXP[bz_navmenu] | $EXP[bz_infoup]</expression>`

### `bz_m26`
- set/clear sites: 0 · read sites: 4
  - `xml/Includes_Bezel.xml` L380: `<control type="group"><animation effect="slide" start="0,0" end="0,-58" time="0" condition="String.IsEmpty(Window(Home).Property(bz_am_n2))">Conditional</animat`
  - `xml/Includes_Bezel.xml` L394: `<control type="label"><left>30</left><top>530</top><width>330</width><height>36</height><font>bz_m26</font><textcolor>FFFFFFFF</textcolor><aligny>center</aligny`
  - `xml/Font.xml` L269: `<name>bz_m26</name>`

### `bz_m44`
- set/clear sites: 0 · read sites: 4
  - `xml/Includes_Bezel.xml` L379: `<control type="label"><left>30</left><top>458</top><width>330</width><height>62</height><font>bz_m44</font><textcolor>FFFFFFFF</textcolor><aligny>center</aligny`
  - `xml/Includes_Bezel.xml` L392: `<control type="label"><left>30</left><top>458</top><width>330</width><height>62</height><font>bz_m44</font><textcolor>FFFFFFFF</textcolor><aligny>center</aligny`
  - `xml/Font.xml` L284: `<name>bz_m44</name>`

### `bz_mm18s`
- set/clear sites: 0 · read sites: 3
  - `xml/Includes_Bezel.xml` L399: `<include name="BezelAMPill"><definition><control type="button"><width>auto</width><height>32</height><font>bz_mm18s</font><textoffsetx>16</textoffsetx><aligny>c`
  - `xml/Font.xml` L330: `<name>bz_mm18s</name>`
  - `xml/Font.xml` L682: `<name>bz_mm18s</name>`

### `bz_mmwarm`
- set/clear sites: 5 · read sites: 18
  - `scripts/bz_flip.py` L724: `home.setProperty('bz_mmwarm', 'true'); home.setProperty('bz_navroot', path)`
  - `scripts/bz_flip.py` L744: `home.clearProperty('bz_mmwarm'); home.clearProperty('bz_xfade')   # t4333: fade back in`
  - `scripts/bz_flip.py` L747: `home.setProperty('bz_mmwarm', 'true'); home.setProperty('bz_navroot', path)`
  - `xml/Includes_Bezel.xml` L6: `<include name="BezelMMFocusBounceList"><onfocus condition="!String.IsEmpty(Window(home).Property(bz_mmwarm)) + !String.IsEqual(Window(home).Property(bz_mmpick),`
  - `xml/Includes_Bezel.xml` L6: `<include name="BezelMMFocusBounceList"><onfocus condition="!String.IsEmpty(Window(home).Property(bz_mmwarm)) + !String.IsEqual(Window(home).Property(bz_mmpick),`
  - `xml/MyVideoNav.xml` L6: `<onload condition="!Control.HasFocus(6996) + !String.IsEqual(Window(home).Property(bz_mmpick),true) + !String.IsEmpty(Window(home).Property(bz_mmwarm)) + !Strin`

### `bz_msret`
- set/clear sites: 1 · read sites: 22
  - `xml/Custom_1117_MediaSources.xml` L6: `<onload>ClearProperty(bz_msret,home)</onload><onload condition="!String.IsEmpty(Window(Home).Property(bz_msfocus))">AlarmClock(bzmsf,SetFocus($INFO[Window(Home)`
  - `xml/Custom_1132_BzSources.xml` L10: `<control type="list" id="9150"><left>0</left><top>112</top><width>390</width><height>720</height><orientation>vertical</orientation><scrolltime tween="cubic" ea`
  - `xml/Includes_Bezel.xml` L1594: `<onback condition="String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Container.FolderPath,sources://)">ActivateWindow(1117)</onback><onback `
  - `xml/Includes_Bezel.xml` L1594: `<onback condition="String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Container.FolderPath,sources://)">ActivateWindow(1117)</onback><onback `

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

### `bz_navgrace`
- set/clear sites: 5 · read sites: 4
  - `scripts/bz_cmd.py` L648: `home.clearProperty('bz_navgrace'); home.setProperty('bz_mmstart', '1'); home.setProperty('bz_nav', 'true')`
  - `scripts/bz_cmd.py` L671: `home.clearProperty('bz_navgrace'); home.setProperty('bz_mmstart', '1'); home.setProperty('bz_nav', 'true')`
  - `scripts/bz_flip.py` L1007: `if nav_was[0] and not nv: home.setProperty('bz_navgrace', 'true'); navgr[0] = now`
  - `xml/Includes_Bezel.xml` L414: `<expression name="bz_navok">String.IsEmpty(Window(Home).Property(bz_navlock)) + String.IsEmpty(Window(Home).Property(bz_navgrace)) + !String.IsEqual(Window(Home`
  - `scripts/bz_flip.py` L1003: `if not nv and not home.getProperty('bz_navgrace') and not home.getProperty('bz_navlock'):`
  - `scripts/bz_flip.py` L1005: `# BEZEL 3.0: one close routine. Any close sets bz_navgrace (0.5 s lock + 0.3 s grace); every open path checks $EXP[bz_navok],`

### `bz_navlock`
- set/clear sites: 1 · read sites: 6
  - `scripts/bz_flip.py` L815: `elif now - navlk[0] >= 0.25: home.clearProperty('bz_navlock'); navlk[0] = 0.0`
  - `xml/Includes_Bezel.xml` L414: `<expression name="bz_navok">String.IsEmpty(Window(Home).Property(bz_navlock)) + String.IsEmpty(Window(Home).Property(bz_navgrace)) + !String.IsEqual(Window(Home`
  - `scripts/bz_flip.py` L812: `# BETA 1.3: slide menu: Up / Down set bz_navlock (XML); further presses are ignored until the bar glide (280 ms) is done`
  - `scripts/bz_flip.py` L813: `if home.getProperty('bz_navlock'):`

### `bz_navmenu`
- set/clear sites: 9 · read sites: 593
  - `xml/Includes_Bezel.xml` L2335: `<control type="list" id="63"><onback condition="[String.IsEmpty(Container.FolderPath) | String.IsEqual(Container.FolderPath,sources://pictures/)] + !$EXP[bz_nav`
  - `xml/MusicVisualisation.xml` L17: `<onunload condition="!$EXP[bz_navmenu]">AlarmClock(bz_vizret,SetFocus(60),00:00,silent)</onunload><!-- 5.33.112 t786: Play Next / viz exit -> section list 60 --`
  - `xml/FileManager.xml` L14: `<control type="list" id="20"><onback condition="String.IsEmpty(Container(20).FolderPath) + !$EXP[bz_navmenu]">SetProperty(bz_nav,true,home)</onback><!-- 5.33.17`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`

### `bz_navok`
- set/clear sites: 11 · read sites: 11
  - `xml/Includes_Bezel.xml` L579: `<onleft condition="$EXP[bz_navok]">SetProperty(bz_nav,true,home)</onleft><onright>$PARAM[list]</onright>`
  - `xml/Includes_Bezel.xml` L588: `<onleft condition="$EXP[bz_navok]">SetProperty(bz_nav,true,home)</onleft><onleft condition="!$EXP[bz_navok]">noop</onleft><!-- BEZEL 3.0: jump bar Left = guarde`
  - `xml/Includes_Bezel.xml` L588: `<onleft condition="$EXP[bz_navok]">SetProperty(bz_nav,true,home)</onleft><onleft condition="!$EXP[bz_navok]">noop</onleft><!-- BEZEL 3.0: jump bar Left = guarde`
  - `xml/Includes_Bezel.xml` L414: `<expression name="bz_navok">String.IsEmpty(Window(Home).Property(bz_navlock)) + String.IsEmpty(Window(Home).Property(bz_navgrace)) + !String.IsEqual(Window(Home`
  - `xml/Includes_Bezel.xml` L651: `<onright>60</onright><ondown>60</ondown><!-- 3.0.2 slide-menu loop fix: Down on the logo no longer opens the menu (focus only lands here by itself during fast l`
  - `xml/Includes_Bezel.xml` L1594: `<onback condition="String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Container.FolderPath,sources://)">ActivateWindow(1117)</onback><onback `

### `bz_navroot`
- set/clear sites: 7 · read sites: 23
  - `scripts/bz_mm.py` L17: `'music': ['SetProperty(bz_navroot,musicdb://albums/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,tomusic,musicdb://albums/)'],`
  - `scripts/bz_mm.py` L18: `'movies': ['SetProperty(bz_navroot,videodb://movies/titles/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,go,videodb://movies/titles/)'],`
  - `scripts/bz_mm.py` L19: `'tv': ['SetProperty(bz_navroot,videodb://tvshows/titles/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,go,videodb://tvshows/titles/)'],`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`

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

### `bz_np_focus`
- set/clear sites: 1 · read sites: 1
  - `xml/MyMusicNav.xml` L26: `<onload>ClearProperty(bz_np_focus,home)</onload>`
  - `xml/MyMusicNav.xml` L25: `<onload condition="String.IsEqual(Window(Home).Property(bz_np_focus),true)">SetFocus(6390)</onload>`

### `bz_np_was`
- set/clear sites: 4 · read sites: 0
  - `xml/MyMusicNav.xml` L20: `<onunload>SetProperty(bz_np_was,$INFO[Window(Home).Property(bz_np)],home)</onunload><!-- 2.0a3.4: Tab toggle -->`
  - `scripts/bz_cmd.py` L121: `home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez'); home.clearProperty('bz_np_was')`
  - `scripts/bz_cmd.py` L284: `home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez'); home.clearProperty('bz_np_was')`

### `bz_pndlg_ok`
- set/clear sites: 8 · read sites: 104
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L2953: `<onclick condition="Window.IsActive(visualisation) + [!String.IsEqual(Window(Home).Property(bz_pnoff),1)] + !Player.Paused">SetProperty(bz_pnfoc,6403,home)</onc`
  - `xml/Includes_Bezel.xml` L335: `<expression name="bz_pndlg_ok">!Skin.HasSetting(bz_pndlg_off) + Player.HasAudio + !Player.HasVideo + Window.IsActive(music) + !Window.IsActive(visualisation) + `
  - `xml/Includes_Bezel.xml` L1371: `<!-- 5.33.221: touch tap big album = Dialogue FS (same as 6390 remote) --><onclick condition="$EXP[bz_pndlg_ok] + String.IsEqual(Skin.String(bz_at_fsslide),1)">`
  - `xml/Includes_Bezel.xml` L1371: `<!-- 5.33.221: touch tap big album = Dialogue FS (same as 6390 remote) --><onclick condition="$EXP[bz_pndlg_ok] + String.IsEqual(Skin.String(bz_at_fsslide),1)">`

### `bz_randpend`
- set/clear sites: 8 · read sites: 1
  - `scripts/bz_flip.py` L582: `finally: home.clearProperty('bz_randpend')   # 5.33.226 RANDFLASH: always release the list alpha`
  - `scripts/bz_flip.py` L598: `home.setProperty('bz_randpend', '1')   # 5.33.226 RANDFLASH (t1796u): list 60 alpha 0 until the random row lands (no row-1 flash)`
  - `scripts/bz_flip.py` L605: `if not ok[0]: home.clearProperty('bz_randpend')   # 5.33.230: no deferred apply -> release now`
  - `scripts/bz_flip.py` L1465: `and not home.getProperty('bz_randpend') and not home.getProperty('bz_back'))`

### `bz_rootarm`
- set/clear sites: 2 · read sites: 3
  - `scripts/bz_flip.py` L956: `rp[0] = fp; rp[1] = now - (0.6 if _fresh else 0); rp[2] = _wid; home.clearProperty('bz_rootarm')`
  - `scripts/bz_flip.py` L960: `home.setProperty('bz_rootarm', 'true')`
  - `xml/Includes_Bezel.xml` L2372: `<expression name="bz_atroot">String.IsEqual(Window(Home).Property(bz_rootarm),true) + ![String.IsEqual(Window(Home).Property(bz_msret),1) + String.StartsWith(Co`
  - `scripts/bz_flip.py` L950: `# (bz_rootarm = that path) before Back counts, so the Back that lands on the top level never opens it`
  - `scripts/bz_flip.py` L958: `elif now - rp[1] >= 0.6 and (fp in ROOTS or (home.getProperty('bz_navroot') and fp.rstrip('/') == home.getProperty('bz_navroot').rstrip('/'))) and home.getPrope`

### `bz_sd_alb`
- set/clear sites: 0 · read sites: 2
  - `xml/Includes_Bezel.xml` L395: `<control type="label"><left>30</left><top>572</top><width>330</width><height>30</height><font>bz_r18</font><textcolor>B3FFFFFF</textcolor><aligny>center</aligny`
  - `scripts/bz_flip.py` L487: `'bz_sd_alb': ' \u2014 '.join([x for x in (aa, al) if x]), 'bz_sd_thumb': g('Art(thumb)') or g('Icon')}`

### `bz_sd_meta`
- set/clear sites: 0 · read sites: 2
  - `xml/Includes_Bezel.xml` L394: `<control type="label"><left>30</left><top>530</top><width>330</width><height>36</height><font>bz_m26</font><textcolor>FFFFFFFF</textcolor><aligny>center</aligny`
  - `scripts/bz_flip.py` L486: `vals = {'bz_sd_n1': w[0], 'bz_sd_n2': w[1] if len(w) > 1 else '', 'bz_sd_meta': '  \u00b7  '.join(bits),`

### `bz_sd_n1`
- set/clear sites: 0 · read sites: 2
  - `xml/Includes_Bezel.xml` L391: `<control type="label"><left>30</left><top>400</top><width>330</width><height>62</height><font>bz_b46</font><textcolor>FFFFFFFF</textcolor><aligny>center</aligny`
  - `scripts/bz_flip.py` L486: `vals = {'bz_sd_n1': w[0], 'bz_sd_n2': w[1] if len(w) > 1 else '', 'bz_sd_meta': '  \u00b7  '.join(bits),`

### `bz_sd_n2`
- set/clear sites: 0 · read sites: 3
  - `xml/Includes_Bezel.xml` L392: `<control type="label"><left>30</left><top>458</top><width>330</width><height>62</height><font>bz_m44</font><textcolor>FFFFFFFF</textcolor><aligny>center</aligny`
  - `xml/Includes_Bezel.xml` L393: `<control type="group"><animation effect="slide" start="0,0" end="0,-58" time="0" condition="String.IsEmpty(Window(Home).Property(bz_sd_n2))">Conditional</animat`
  - `scripts/bz_flip.py` L486: `vals = {'bz_sd_n1': w[0], 'bz_sd_n2': w[1] if len(w) > 1 else '', 'bz_sd_meta': '  \u00b7  '.join(bits),`

### `bz_sd_thumb`
- set/clear sites: 0 · read sites: 2
  - `xml/Includes_Bezel.xml` L390: `<control type="image"><left>30</left><top>40</top><width>330</width><height>330</height><aspectratio scalediffuse="false">scale</aspectratio><fadetime>150</fade`
  - `scripts/bz_flip.py` L487: `'bz_sd_alb': ' \u2014 '.join([x for x in (aa, al) if x]), 'bz_sd_thumb': g('Art(thumb)') or g('Icon')}`

### `bz_secfade`
- set/clear sites: 3 · read sites: 6
  - `scripts/bz_cmd.py` L408: `home.clearProperty('bz_secfade'); home.setProperty('bz_secload', 'true')`
  - `scripts/bz_cmd.py` L431: `home.setProperty('bz_secfade', 'true'); home.clearProperty('bz_secload')`
  - `scripts/bz_cmd.py` L433: `mon.waitForAbort(0.6); home.clearProperty('bz_secfade')`
  - `xml/MyVideoNav.xml` L28: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`
  - `xml/MyVideoNav.xml` L30: `<animation effect="fade" start="0" end="100" time="400" tween="sine" easing="out" condition="!String.IsEmpty(Window(Home).Property(bz_secfade))" reversible="fal`
  - `xml/MyMusicNav.xml` L31: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`

### `bz_secload`
- set/clear sites: 3 · read sites: 6
  - `scripts/bz_cmd.py` L407: `home.clearProperty('bz_secload'); home.clearProperty('bz_nav'); home.clearProperty('bz_navtune'); home.clearProperty('bz_navbez'); return`
  - `scripts/bz_cmd.py` L408: `home.clearProperty('bz_secfade'); home.setProperty('bz_secload', 'true')`
  - `scripts/bz_cmd.py` L431: `home.setProperty('bz_secfade', 'true'); home.clearProperty('bz_secload')`
  - `xml/MyVideoNav.xml` L28: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`
  - `xml/MyVideoNav.xml` L29: `<animation effect="fade" start="100" end="0" time="0" condition="!String.IsEmpty(Window(Home).Property(bz_secload))">Conditional</animation><animation effect="f`
  - `xml/MyMusicNav.xml` L31: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`

### `bz_topedge`
- set/clear sites: 1 · read sites: 3
  - `xml/Includes_Bezel.xml` L2699: `<onup>SetProperty(bz_topedge,1,home)</onup><ondown condition="Control.IsVisible(6098)">6098</ondown><!-- t4357: numeric nav = no native wrap flash --><ondown>Se`
  - `xml/Includes_Bezel.xml` L1568: `<control type="grouplist"><!-- t4533: TRUE CLIP for list 60. A grouplist scissors its children to its own rect (bz_list_x,bz_top 450x900 = bottom y1020); the co`
  - `xml/Includes_Bezel.xml` L1570: `<onright condition="$EXP[bz_artbtn] + Container.Content(songs) + [!Player.HasAudio | !Control.IsVisible(6160)]">SetFocus(6095)</onright><onright condition="$EXP`
  - `xml/Includes_Bezel.xml` L2693: `<control type="grouplist"><animation effect="slide" end="0,450" time="0" condition="$EXP[bz_actcov]">Conditional</animation><!-- t4464 actors cover column --><o`

### `bz_vback`
- set/clear sites: 11 · read sites: 34
  - `xml/Includes_Bezel.xml` L645: `<onclick condition="!$EXP[bz_np] + !String.IsEmpty(Window(Home).Property(bz_vback))">SetProperty(bz_vback_close,true,home)</onclick>`
  - `xml/Includes_Bezel.xml` L646: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !String.IsEmpty(Window(Home).Property(bz_back))">SetProperty(bz_back_clos`
  - `xml/Includes_Bezel.xml` L1584: `<onleft condition="!String.IsEmpty(Window(Home).Property(bz_vback))">SetProperty(bz_vback_close,true,home)</onleft>`
  - `xml/Includes_Bezel.xml` L565: `Tap: flips to the info back (bz_vback). Mini player: the whole poster scales to 90% about its bottom edge so it sits under the bar. -->`
  - `xml/Includes_Bezel.xml` L647: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !!String.IsEmpty(Window(Home).Property(bz_back)) + Control.IsVisible(60)"`
  - `xml/Includes_Bezel.xml` L648: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !!String.IsEmpty(Window(Home).Property(bz_back)) + !Control.IsVisible(60)`

### `bz_vback_close`
- set/clear sites: 8 · read sites: 2
  - `xml/Includes_Bezel.xml` L645: `<onclick condition="!$EXP[bz_np] + !String.IsEmpty(Window(Home).Property(bz_vback))">SetProperty(bz_vback_close,true,home)</onclick>`
  - `xml/Includes_Bezel.xml` L1584: `<onleft condition="!String.IsEmpty(Window(Home).Property(bz_vback))">SetProperty(bz_vback_close,true,home)</onleft>`
  - `xml/Includes_Bezel.xml` L1593: `<onback condition="!String.IsEmpty(Window(Home).Property(bz_vback))">SetProperty(bz_vback_close,true,home)</onback>`
  - `scripts/bz_flip.py` L291: `# dialog is open), on Back (bz_vback_close), when the focused title changes or the list is focused again, fading to black first.`
  - `scripts/bz_flip.py` L426: `if (home.getProperty('bz_vback_close') or left or (k or '') != home.getProperty('bz_vback_key') or not vid`

