# MM warm (WARM 2.0.1) — LOCKED — mm-warm

**Object:** `mm-warm` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/mm-warm.md) · [layout](../layout/mm-warm.md) · [state](../state/mm-warm.md) · [motion](../motion/mm-warm.md) · [art](../art/mm-warm.md) · [input](../input/mm-warm.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
These are the fixed numbers and switches for the whole warm system.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

**See screen:** [mm-warm baselines](../port-refs/mm-warm/) — smoke baseline + port diff target.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_ab_live`
- set/clear sites: 4 · read sites: 10
  - `scripts/bz_flip.py` L1411: `home.clearProperty('bz_ab_live')`
  - `scripts/bz_flip.py` L1415: `elif not home.getProperty('bz_ab_live') and time.time() - open_t >= 0.3: home.setProperty('bz_ab_live', '1')   # 5.33.207: side-flip fades armed only after MM i`
  - `scripts/bz_flip.py` L1415: `elif not home.getProperty('bz_ab_live') and time.time() - open_t >= 0.3: home.setProperty('bz_ab_live', '1')   # 5.33.207: side-flip fades armed only after MM i`
  - `xml/Includes_Bezel.xml` L755: `<visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_fan_on)) + !String.IsEqual(Window(Home).Property(bz_fan_side),b)</visible><animation effect`
  - `xml/Includes_Bezel.xml` L762: `<visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_fan_on)) + String.IsEqual(Window(Home).Property(bz_fan_side),b)</visible><animation effect=`
  - `xml/Includes_Bezel.xml` L1209: `</control><!-- 5.33.148 MM A/B pos side a --><control type="image"><visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAu`

### `bz_art_x`
- set/clear sites: 0 · read sites: 10
  - `xml/Includes_Bezel.xml` L2360: `<constant name="bz_art_x">1140</constant>`
  - `xml/Includes_Bezel.xml` L2595: `<left>bz_art_x</left><top>bz_top</top><width>600</width><height>bz_h</height>`
  - `xml/Includes_Bezel.xml` L2598: `<left>bz_art_x</left><top>bz_top</top><width>600</width><height>bz_h</height>`

### `bz_arthold`
- set/clear sites: 4 · read sites: 7
  - `scripts/bz_flip.py` L700: `home.clearProperty('bz_hold_poster'); home.setProperty('bz_arthold', '1'); return`
  - `scripts/bz_flip.py` L706: `home.setProperty('bz_arthold', '1')   # fanart hold only`
  - `scripts/bz_flip.py` L712: `home.setProperty('bz_arthold', '1')`
  - `xml/Includes_Bezel.xml` L149: `<value condition="!String.IsEmpty(Window(Home).Property(bz_arthold)) + String.IsEmpty(ListItem.Label) + !String.IsEmpty(Window(Home).Property(bz_hold_fanart))">`
  - `xml/Includes_Bezel.xml` L160: `<value condition="Window.IsActive(videos) + !String.IsEmpty(Window(Home).Property(bz_arthold)) + !String.IsEmpty(Window(Home).Property(bz_hold_poster))"><!-- 5.`
  - `xml/Includes_Bezel.xml` L181: `<value condition="Window.IsActive(videos) + !String.IsEmpty(Window(Home).Property(bz_arthold)) + !String.IsEmpty(Window(Home).Property(bz_hold_poster))">$INFO[W`

### `bz_at_abfade`
- set/clear sites: 26 · read sites: 16
  - `xml/Includes_Tuner.xml` L1964: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),abfade) + String.IsEqual(Skin.String(bz_at_abfade),1)">Skin.SetString(bz_at_abfade,2)</`
  - `xml/Includes_Tuner.xml` L1964: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),abfade) + String.IsEqual(Skin.String(bz_at_abfade),1)">Skin.SetString(bz_at_abfade,2)</`
  - `xml/Includes_Tuner.xml` L1965: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),abfade) + String.IsEqual(Skin.String(bz_at_abfade),2)">Skin.SetString(bz_at_abfade,1)</o`
  - `xml/Includes_Tuner.xml` L120: `<variable name="BzATVal_abfade"><value condition="String.IsEqual(Skin.String(bz_at_abfade),1)">2500 ms</value><value condition="String.IsEqual(Skin.String(bz_at`
  - `xml/Includes_Tuner.xml` L120: `<variable name="BzATVal_abfade"><value condition="String.IsEqual(Skin.String(bz_at_abfade),1)">2500 ms</value><value condition="String.IsEqual(Skin.String(bz_at`
  - `xml/Includes_Tuner.xml` L120: `<variable name="BzATVal_abfade"><value condition="String.IsEqual(Skin.String(bz_at_abfade),1)">2500 ms</value><value condition="String.IsEqual(Skin.String(bz_at`

### `bz_at_gbdsty`
- set/clear sites: 0 · read sites: 13
  - `xml/Includes_Bezel.xml` L596: `<!-- 5.33.66 t438 global backdrop (remove: delete this + the include line in BezelBlack) --><variable name="BzGbdCol"><!-- 5.33.81 t525 level 0 = 5% --><value c`
  - `xml/Includes_Tuner.xml` L256: `<!-- 5.33.66 t438 global backdrop --><variable name="BzATVal_gbd"><value condition="String.IsEqual(Skin.String(bz_at_gbdsty),off)">OFF</value><value>CORNER KEY<`
  - `xml/Includes_Tuner.xml` L256: `<!-- 5.33.66 t438 global backdrop --><variable name="BzATVal_gbd"><value condition="String.IsEqual(Skin.String(bz_at_gbdsty),off)">OFF</value><value>CORNER KEY<`

### `bz_at_mmdef`
- set/clear sites: 14 · read sites: 8
  - `xml/Includes_Tuner.xml` L1603: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdef) + String.IsEqual(Skin.String(bz_at_mmdef),1)">Skin.SetString(bz_at_mmdef,3)</onle`
  - `xml/Includes_Tuner.xml` L1603: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdef) + String.IsEqual(Skin.String(bz_at_mmdef),1)">Skin.SetString(bz_at_mmdef,3)</onle`
  - `xml/Includes_Tuner.xml` L1603: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdef) + String.IsEqual(Skin.String(bz_at_mmdef),1)">Skin.SetString(bz_at_mmdef,3)</onle`
  - `xml/Includes_Tuner.xml` L472: `<variable name="BzATVal_mmdef"><value condition="String.IsEqual(Skin.String(bz_at_mmdef),1)">MUSIC</value><value condition="String.IsEqual(Skin.String(bz_at_mmd`
  - `xml/Includes_Tuner.xml` L472: `<variable name="BzATVal_mmdef"><value condition="String.IsEqual(Skin.String(bz_at_mmdef),1)">MUSIC</value><value condition="String.IsEqual(Skin.String(bz_at_mmd`
  - `scripts/bz_cmd.py` L635: `# t5012: pill defaults on cold start — Artists / Titles / Shows (index 1). Tuner Startup highlight (bz_at_mmdef) untouched.`

### `bz_at_mmdim`
- set/clear sites: 42 · read sites: 542
  - `xml/Includes_Tuner.xml` L2055: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdim) + String.IsEqual(Skin.String(bz_at_mmdim),1)">Skin.SetString(bz_at_mmdim,2)</onr`
  - `xml/Includes_Tuner.xml` L2055: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdim) + String.IsEqual(Skin.String(bz_at_mmdim),1)">Skin.SetString(bz_at_mmdim,2)</onr`
  - `xml/Includes_Tuner.xml` L2056: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdim) + [String.IsEmpty(Skin.String(bz_at_mmdim)) | String.IsEqual(Skin.String(bz_at_m`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`

### `bz_at_mmsecfade`
- set/clear sites: 26 · read sites: 25
  - `xml/Includes_Tuner.xml` L1973: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmsecfade) + String.IsEqual(Skin.String(bz_at_mmsecfade),1)">Skin.SetString(bz_at_mmsec`
  - `xml/Includes_Tuner.xml` L1973: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmsecfade) + String.IsEqual(Skin.String(bz_at_mmsecfade),1)">Skin.SetString(bz_at_mmsec`
  - `xml/Includes_Tuner.xml` L1974: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmsecfade) + String.IsEqual(Skin.String(bz_at_mmsecfade),2)">Skin.SetString(bz_at_mmsecf`
  - `xml/Includes_Tuner.xml` L188: `<variable name="BzATVal_mmsecfade"><value condition="String.IsEqual(Skin.String(bz_at_mmsecfade),1)">Off</value><value condition="String.IsEqual(Skin.String(bz_`
  - `xml/Includes_Tuner.xml` L188: `<variable name="BzATVal_mmsecfade"><value condition="String.IsEqual(Skin.String(bz_at_mmsecfade),1)">Off</value><value condition="String.IsEqual(Skin.String(bz_`
  - `xml/Includes_Tuner.xml` L188: `<variable name="BzATVal_mmsecfade"><value condition="String.IsEqual(Skin.String(bz_at_mmsecfade),1)">Off</value><value condition="String.IsEqual(Skin.String(bz_`

### `bz_at_mmwarm`
- set/clear sites: 37 · read sites: 36
  - `xml/Includes_Tuner.xml` L1985: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmwarm) + [String.IsEmpty(Skin.String(bz_at_mmwarm)) | String.IsEqual(Skin.String(bz_at`
  - `xml/Includes_Tuner.xml` L1985: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmwarm) + [String.IsEmpty(Skin.String(bz_at_mmwarm)) | String.IsEqual(Skin.String(bz_at`
  - `xml/Includes_Tuner.xml` L1985: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmwarm) + [String.IsEmpty(Skin.String(bz_at_mmwarm)) | String.IsEqual(Skin.String(bz_at`
  - `xml/Includes_Tuner.xml` L191: `<variable name="BzATVal_mmwarm"><value condition="[String.IsEmpty(Skin.String(bz_at_mmwarm)) | String.IsEqual(Skin.String(bz_at_mmwarm),1)]">0.2 s</value><value`
  - `xml/Includes_Tuner.xml` L191: `<variable name="BzATVal_mmwarm"><value condition="[String.IsEmpty(Skin.String(bz_at_mmwarm)) | String.IsEqual(Skin.String(bz_at_mmwarm),1)]">0.2 s</value><value`
  - `xml/Includes_Tuner.xml` L191: `<variable name="BzATVal_mmwarm"><value condition="[String.IsEmpty(Skin.String(bz_at_mmwarm)) | String.IsEqual(Skin.String(bz_at_mmwarm),1)]">0.2 s</value><value`

### `bz_at_warmhold`
- set/clear sites: 2 · read sites: 4
  - `xml/Includes_Tuner.xml` L1962: `<!-- 5.33.216 MM auto-hide --><onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmidle)">Skin.SetString(bz_at_mmidle,Off)</onleft><onright`
  - `xml/Includes_Tuner.xml` L1962: `<!-- 5.33.216 MM auto-hide --><onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmidle)">Skin.SetString(bz_at_mmidle,Off)</onleft><onright`
  - `xml/Includes_Bezel.xml` L714: `<!-- 5.33.211 WARM HOLD: non-Music/Movies/TV sections (Favourites/Pictures/Add-ons/Settings) draw the last WARM fan lane under the open MM. Kill: Skin.String(bz`
  - `xml/Includes_Bezel.xml` L715: `<expression name="bz_warmhold">$EXP[bz_navmenu] + !String.IsEqual(Skin.String(bz_at_warmhold),Off) + !String.IsEmpty(Window(Home).Property(bz_fan_on))</expressi`
  - `xml/Includes_Tuner.xml` L118: `<variable name="BzATVal_warmhold"><value condition="String.IsEqual(Skin.String(bz_at_warmhold),Off)">Off (section art / plain)</value><value>On (last WARM art)<`

### `bz_at_warmmusicposters`
- set/clear sites: 2 · read sites: 2
  - `xml/Includes_Tuner.xml` L1963: `<!-- 5.33.191 WARM 2.0 --><onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),warmmusicposters)">Skin.SetString(bz_at_warmmusicposters,Off)<`
  - `xml/Includes_Tuner.xml` L1963: `<!-- 5.33.191 WARM 2.0 --><onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),warmmusicposters)">Skin.SetString(bz_at_warmmusicposters,Off)<`
  - `xml/Includes_Bezel.xml` L123: `<expression name="bz_mmmushide">Player.HasAudio + !Player.HasVideo + $EXP[bz_navmenu] + !String.IsEqual(Skin.String(bz_at_warmmusicposters),Off)</expression><!-`
  - `xml/Includes_Tuner.xml` L119: `<variable name="BzATVal_warmmusicposters"><value condition="String.IsEqual(Skin.String(bz_at_warmmusicposters),Off)">Off (posters show)</value><value>On (album `

### `bz_at_warmsplash`
- set/clear sites: 3 · read sites: 4
  - `xml/Includes_Tuner.xml` L1961: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),warmsplash)">Skin.SetString(bz_at_warmsplash,Off)</onleft><onright condition="String.IsE`
  - `xml/Includes_Tuner.xml` L1961: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),warmsplash)">Skin.SetString(bz_at_warmsplash,Off)</onleft><onright condition="String.IsE`
  - `xml/Startup.xml` L5: `<onload condition="!String.IsEqual(Skin.String(bz_at_warmsplash),Off)">SetProperty(bz_warm_gate,1,home)</onload>`
  - `xml/Includes_Bezel.xml` L3672: `<visible>!String.IsEmpty(Window(Home).Property(bz_warm_gate)) + !String.IsEqual(Skin.String(bz_at_warmsplash),Off)</visible>`
  - `xml/Includes_Tuner.xml` L116: `<variable name="BzATVal_warmsplash"><value condition="String.IsEqual(Skin.String(bz_at_warmsplash),Off)">Off (warm still runs)</value><value>On</value></variabl`
  - `xml/Startup.xml` L4: `<!-- Tuner WARM 2.0 > Startup splash (bz_at_warmsplash, default On): Off hides splash VISUALS only; warm-cache always runs. -->`

### `bz_backdrop`
- set/clear sites: 21 · read sites: 21
  - `xml/MyPlaylist.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/MyPlaylist.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/Settings.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L3048: `<texture colordiffuse="$VAR[BezelBackdropAlpha]">$INFO[Window(Home).Property(bz_backdrop)]</texture>`
  - `xml/Includes_Bezel.xml` L3049: `<visible>String.IsEmpty(Window(Home).Property(bz_npdlg)) + [Skin.HasSetting(bezel_norotate) | String.IsEmpty(Control.GetLabel(9880))] + String.IsEmpty(ListItem.`

### `bz_bdimg`
- set/clear sites: 2 · read sites: 6
  - `scripts/bz_cmd.py` L99: `xbmc.executebuiltin('Skin.SetString(bz_bdimg,%s)' % nxt); home.setProperty('bz_backdrop', d + nxt)`
  - `scripts/bz_cmd.py` L102: `xbmc.executebuiltin('Skin.Reset(bz_bdimg)'); home.setProperty('bz_bdimg_lbl', 'Random')`
  - `xml/Includes_Tuner.xml` L186: `<variable name="BzATVal_bdimg"><value condition="String.IsEmpty(Skin.String(bz_bdimg))">Random</value><value>$INFO[Skin.String(bz_bdimg)]</value></variable><!--`
  - `xml/Includes_Tuner.xml` L186: `<variable name="BzATVal_bdimg"><value condition="String.IsEmpty(Skin.String(bz_bdimg))">Random</value><value>$INFO[Skin.String(bz_bdimg)]</value></variable><!--`
  - `scripts/bz_cmd.py` L80: `# 4.7.4: Tuner LOOK > Backdrop image (skin string bz_bdimg: empty = Random, else a file name that sticks until changed)`

### `bz_clr_a`
- set/clear sites: 0 · read sites: 1
  - `xml/Includes_Bezel.xml` L2461: `<control type="image"><left>600</left><top>130</top><width>330</width><height>150</height><aspectratio align="center" aligny="center">keep</aspectratio><fadetim`

### `bz_clr_empty`
- set/clear sites: 0 · read sites: 3
  - `xml/Includes_Bezel.xml` L2461: `<control type="image"><left>600</left><top>130</top><width>330</width><height>150</height><aspectratio align="center" aligny="center">keep</aspectratio><fadetim`
  - `xml/Includes_Bezel.xml` L2462: `<control type="image"><left>600</left><top>130</top><width>330</width><height>150</height><aspectratio align="center" aligny="center">keep</aspectratio><fadetim`
  - `xml/Includes_Bezel.xml` L2464: `<control type="label"><left>600</left><top>130</top><width>330</width><height>150</height><font>bz_b34</font><align>center</align><aligny>center</aligny><scroll`

### `bz_clr_on`
- set/clear sites: 0 · read sites: 5
  - `xml/Includes_Bezel.xml` L2460: `<control type="image"><left>600</left><top>130</top><width>330</width><height>150</height><aspectratio align="center" aligny="center">keep</aspectratio><fadetim`
  - `xml/Includes_Bezel.xml` L2461: `<control type="image"><left>600</left><top>130</top><width>330</width><height>150</height><aspectratio align="center" aligny="center">keep</aspectratio><fadetim`
  - `xml/Includes_Bezel.xml` L2462: `<control type="image"><left>600</left><top>130</top><width>330</width><height>150</height><aspectratio align="center" aligny="center">keep</aspectratio><fadetim`

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_cov_`
- set/clear sites: 3 · read sites: 0
  - `scripts/bz_flip.py` L1540: `home.setProperty('bz_cov_' + side, art); shown = key; shown_art[0] = art`
  - `scripts/bz_flip.py` L1545: `home.setProperty('bz_cov_' + other, art)   # hidden layer`
  - `scripts/bz_flip.py` L1555: `home.setProperty('bz_cov_next', art); home.setProperty('bz_cov_' + other, art)`

### `bz_cov_a`
- set/clear sites: 1 · read sites: 14
  - `scripts/bz_flip.py` L1583: `for k in ('bz_cov_a', 'bz_cov_b', 'bz_cov_next'): home.clearProperty(k)`
  - `xml/Includes_Bezel.xml` L128: `<!-- v0.1.24: cover layers bind only to the held bz_cov_a/b properties from bz_flip.py (no Player.HasAudio gate, so a track gap never pops in the live art) -->`
  - `xml/Includes_Bezel.xml` L131: `<variable name="BezelFlipA"><value condition="!Player.HasVideo + !String.IsEmpty(Window(Home).Property(bz_cov_a))">$INFO[Window(Home).Property(bz_cov_a)]</value`
  - `xml/Includes_Bezel.xml` L131: `<variable name="BezelFlipA"><value condition="!Player.HasVideo + !String.IsEmpty(Window(Home).Property(bz_cov_a))">$INFO[Window(Home).Property(bz_cov_a)]</value`

### `bz_cov_b`
- set/clear sites: 1 · read sites: 9
  - `scripts/bz_flip.py` L1583: `for k in ('bz_cov_a', 'bz_cov_b', 'bz_cov_next'): home.clearProperty(k)`
  - `xml/Includes_Bezel.xml` L132: `<variable name="BezelFlipB"><value condition="!Player.HasVideo + !String.IsEmpty(Window(Home).Property(bz_cov_b))">$INFO[Window(Home).Property(bz_cov_b)]</value`
  - `xml/Includes_Bezel.xml` L132: `<variable name="BezelFlipB"><value condition="!Player.HasVideo + !String.IsEmpty(Window(Home).Property(bz_cov_b))">$INFO[Window(Home).Property(bz_cov_b)]</value`
  - `xml/Includes_Bezel.xml` L134: `<variable name="BezelNPFlipB"><value condition="!Player.HasVideo + !String.IsEmpty(Window(Home).Property(bz_cov_b))">$INFO[Window(Home).Property(bz_cov_b)]</val`

### `bz_debug_mm`
- set/clear sites: 0 · read sites: 7
  - `xml/Includes_Tuner.xml` L473: `<variable name="BzATVal_mmdebug"><value condition="Skin.HasSetting(bz_debug_mm)">ON</value><value>OFF</value></variable><!-- fork.3 -->`
  - `xml/Includes_Tuner.xml` L1605: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdebug)">Skin.Reset(bz_debug_mm)</onleft><onright condition="String.IsEqual(Container(6`
  - `xml/Includes_Tuner.xml` L1605: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdebug)">Skin.Reset(bz_debug_mm)</onleft><onright condition="String.IsEqual(Container(6`

### `bz_fan_a`
- set/clear sites: 0 · read sites: 6
  - `xml/Includes_Bezel.xml` L759: `<texture background="true">$INFO[Window(Home).Property(bz_fan_a)]</texture>`
  - `xml/Includes_Bezel.xml` L2318: `<include name="View_63_BezelPictureList"><!-- 5.33.242 Rob t1862u: Pictures on the Warm strip (MM/Media Sources language). List 63 lives IN the colour strip at `
  - `xml/Custom_1117_MediaSources.xml` L13: `<!-- 5.33.233 Rob t1830: fanart flash on open — lane loads sync (MM already cached it, no empty frame) + black cover hides StdFrame bz_backdrop (fadetime 200) s`

### `bz_fan_on`
- set/clear sites: 0 · read sites: 11
  - `xml/Includes_Bezel.xml` L715: `<expression name="bz_warmhold">$EXP[bz_navmenu] + !String.IsEqual(Skin.String(bz_at_warmhold),Off) + !String.IsEmpty(Window(Home).Property(bz_fan_on))</expressi`
  - `xml/Includes_Bezel.xml` L748: `<visible>$EXP[bz_navmenu] + String.IsEmpty(Window(Home).Property(bz_fan_on))</visible>`
  - `xml/Includes_Bezel.xml` L755: `<visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_fan_on)) + !String.IsEqual(Window(Home).Property(bz_fan_side),b)</visible><animation effect`

### `bz_fan_side`
- set/clear sites: 0 · read sites: 6
  - `xml/Includes_Bezel.xml` L755: `<visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_fan_on)) + !String.IsEqual(Window(Home).Property(bz_fan_side),b)</visible><animation effect`
  - `xml/Includes_Bezel.xml` L762: `<visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_fan_on)) + String.IsEqual(Window(Home).Property(bz_fan_side),b)</visible><animation effect=`
  - `xml/Custom_1117_MediaSources.xml` L13: `<!-- 5.33.233 Rob t1830: fanart flash on open — lane loads sync (MM already cached it, no empty frame) + black cover hides StdFrame bz_backdrop (fadetime 200) s`

### `bz_flip`
- set/clear sites: 1 · read sites: 69
  - `xml/MyVideoNav.xml` L23: `<onload condition="Skin.HasSetting(bz_grid_video)">SetProperty(bz_gpend,1,home)</onload><onload>AlarmClock(bzgpend,ClearProperty(bz_gpend,home),00:02,silent)</o`
  - `xml/MyPlaylist.xml` L9: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L14: `<!-- BETA 1.1b: the gate below uses Player.HasAudio directly (the debounced bz_audio_latch from bz_flip.py may not be set yet on the first Tab after Kodi start;`

### `bz_flip_running`
- set/clear sites: 5 · read sites: 25
  - `scripts/bz_cmd.py` L21: `for k in ('bz_flip_running', 'bz_dtap_running', 'bz_precache_running'): home.clearProperty(k)`
  - `scripts/bz_flip.py` L81: `home.setProperty('bz_flip_running', 'true')`
  - `scripts/bz_flip.py` L455: `home.setProperty('bz_flip_fail', f.__name__); home.clearProperty('bz_flip_running'); return`
  - `xml/MyPlaylist.xml` L9: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`
  - `xml/MusicVisualisation.xml` L14: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`
  - `xml/Custom_1121_MusicFanartFS.xml` L18: `<onload condition="!String.IsEqual(Window(Home).Property(bz_flip_running),true)">RunScript(special://skin/scripts/bz_flip.py)</onload>`

### `bz_fpop`
- set/clear sites: 2 · read sites: 5
  - `scripts/bz_flip.py` L512: `if v: home.setProperty('bz_fpop', v)`
  - `scripts/bz_flip.py` L513: `else: home.clearProperty('bz_fpop')`
  - `xml/Includes_Bezel.xml` L55: `<expression name="bz_fpop_a">Skin.HasSetting(bz_fs_fanartpop) + Window.IsActive(visualisation) + String.IsEmpty(Window(Home).Property(bz_npdlg)) + String.IsEqua`
  - `xml/Includes_Bezel.xml` L56: `<expression name="bz_fpop_b">Skin.HasSetting(bz_fs_fanartpop) + Window.IsActive(visualisation) + String.IsEmpty(Window(Home).Property(bz_npdlg)) + String.IsEqua`
  - `xml/Includes_Bezel.xml` L57: `<expression name="bz_fpop">[$EXP[bz_fpop_a] | $EXP[bz_fpop_b]]</expression>`

### `bz_frame_soft`
- set/clear sites: 0 · read sites: 6
  - `xml/Includes_Bezel.xml` L1021: `<control type="image"><left>-1</left><top>-1</top><width>542</width><height>542</height><texture border="8">bezel/bz_frame_soft.png</texture></control><!-- 5.33`
  - `xml/Includes_Bezel.xml` L1033: `<control type="image"><left>-1</left><top>-1</top><width>542</width><height>542</height><texture border="8">bezel/bz_frame_soft.png</texture></control><!-- 5.33`
  - `xml/Includes_Bezel.xml` L1112: `<left>1139</left><top>219</top><width>602</width><height>602</height><!-- BETA 2.6: +2 px transparent pad (bz_frame_soft) so the rotated frame edge antialiases;`

### `bz_h`
- set/clear sites: 0 · read sites: 14
  - `xml/Includes_Bezel.xml` L1565: `<left>bz_list_x</left><top>bz_top</top><width>450</width><height>bz_h</height><!-- 4.2 section standard: group at bz_list_x (was 420 / 550; BETA 1.3: list at 0 `
  - `xml/Includes_Bezel.xml` L2356: `<constant name="bz_h">900</constant>`
  - `xml/Includes_Bezel.xml` L2410: `<control type="image"><left>912</left><top>bz_top</top><width>48</width><height>bz_h</height><texture flipx="true">bezel/shadow_right.png</texture>`

### `bz_hold_fanart`
- set/clear sites: 1 · read sites: 2
  - `scripts/bz_flip.py` L693: `home.setProperty('bz_hold_fanart', _gp('Control.GetLabel(9880)', 'Container(60).ListItem.Art(fanart)', 'Window(Home).Property(script.grab.fanart.TV.FanArt)'))`
  - `xml/Includes_Bezel.xml` L149: `<value condition="!String.IsEmpty(Window(Home).Property(bz_arthold)) + String.IsEmpty(ListItem.Label) + !String.IsEmpty(Window(Home).Property(bz_hold_fanart))">`
  - `xml/Includes_Bezel.xml` L149: `<value condition="!String.IsEmpty(Window(Home).Property(bz_arthold)) + String.IsEmpty(ListItem.Label) + !String.IsEmpty(Window(Home).Property(bz_hold_fanart))">`

### `bz_hold_poster`
- set/clear sites: 4 · read sites: 9
  - `scripts/bz_flip.py` L683: `if enter_music: home.clearProperty('bz_pos_on'); home.clearProperty('bz_hold_poster')   # video poster A/B fades out over the new Music album`
  - `scripts/bz_flip.py` L700: `home.clearProperty('bz_hold_poster'); home.setProperty('bz_arthold', '1'); return`
  - `scripts/bz_flip.py` L710: `if hp: home.setProperty('bz_hold_poster', hp)`
  - `xml/Includes_Bezel.xml` L160: `<value condition="Window.IsActive(videos) + !String.IsEmpty(Window(Home).Property(bz_arthold)) + !String.IsEmpty(Window(Home).Property(bz_hold_poster))"><!-- 5.`
  - `xml/Includes_Bezel.xml` L160: `<value condition="Window.IsActive(videos) + !String.IsEmpty(Window(Home).Property(bz_arthold)) + !String.IsEmpty(Window(Home).Property(bz_hold_poster))"><!-- 5.`
  - `xml/Includes_Bezel.xml` L181: `<value condition="Window.IsActive(videos) + !String.IsEmpty(Window(Home).Property(bz_arthold)) + !String.IsEmpty(Window(Home).Property(bz_hold_poster))">$INFO[W`

### `bz_lastmusic`
- set/clear sites: 2 · read sites: 5
  - `scripts/bz_flip.py` L636: `home.setProperty('bz_lastmusic', _lp)`
  - `scripts/bz_flip.py` L669: `if sec == 'music': home.setProperty('bz_music_underlay', '1')   # mark artists load as underlay so tracking won't poison bz_lastmusic`
  - `scripts/bz_mm.py` L47: `if not explicit and home.getProperty('bz_lastmusic'): p = home.getProperty('bz_lastmusic')   # MMQUEUE keep last Music location`
  - `scripts/bz_mm.py` L47: `if not explicit and home.getProperty('bz_lastmusic'): p = home.getProperty('bz_lastmusic')   # MMQUEUE keep last Music location`
  - `scripts/bz_flip.py` L551: `WARM = {'music': ('Music', 'musicdb://artists/'),   # 5.33.164: MM Music underlay always Artists (art only); Select uses bz_lastmusic via bz_mm 'recent': ('Musi`

### `bz_libroot`
- set/clear sites: 0 · read sites: 3
  - `xml/Includes_Bezel.xml` L411: `<expression name="bz_libroot">[String.IsEqual(Container.FolderPath,musicdb://) | String.IsEqual(Container.FolderPath,videodb://) | String.IsEqual(Container.Fold`
  - `xml/Includes_Bezel.xml` L413: `<include name="BezelRootArtHide"><control type="image"><left>962</left><top>0</top><width>958</width><height>1080</height><texture colordiffuse="FF000000">bezel`
  - `xml/Includes_Bezel.xml` L413: `<include name="BezelRootArtHide"><control type="image"><left>962</left><top>0</top><width>958</width><height>1080</height><texture colordiffuse="FF000000">bezel`

### `bz_load_then_close`
- set/clear sites: 0 · read sites: 5
  - `xml/MyVideoNav.xml` L28: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`
  - `xml/MyMusicNav.xml` L31: `<control type="group"><!-- 4.7: SECTION PARENT GROUP --><include>BezelSecDim</include><!-- 4.0.1 O25: section content held hidden while it loads behind the Main`
  - `scripts/bz_cmd.py` L400: `def _bz_load_then_close(win, path):`

### `bz_mart`
- set/clear sites: 0 · read sites: 2
  - `xml/Includes_Bezel.xml` L2605: `</control><control type="image"><visible>$EXP[bz_navmenu] + String.IsEmpty(Window(Home).Property(bz_pos_on)) + !$EXP[bz_mmmushide] + ![Window.IsActive(music) + `
  - `xml/Includes_Bezel.xml` L2609: `</control><control type="image"><visible>$EXP[bz_navmenu] + String.IsEmpty(Window(Home).Property(bz_pos_on)) + !$EXP[bz_mmmushide] + ![Window.IsActive(music) + `

### `bz_mart_a`
- set/clear sites: 0 · read sites: 1
  - `xml/Includes_Bezel.xml` L2622: `<!-- 5.33.216 Music A/B art lane side a (BUG-010: own props, never bz_pos) --><control type="image"><visible>$EXP[bz_navmenu] + !$EXP[bz_mmmushide] + Window.IsA`

### `bz_mart_b`
- set/clear sites: 0 · read sites: 1
  - `xml/Includes_Bezel.xml` L2622: `<!-- 5.33.216 Music A/B art lane side a (BUG-010: own props, never bz_pos) --><control type="image"><visible>$EXP[bz_navmenu] + !$EXP[bz_mmmushide] + Window.IsA`

### `bz_mart_empty`
- set/clear sites: 0 · read sites: 4
  - `xml/Includes_Bezel.xml` L2605: `</control><control type="image"><visible>$EXP[bz_navmenu] + String.IsEmpty(Window(Home).Property(bz_pos_on)) + !$EXP[bz_mmmushide] + ![Window.IsActive(music) + `
  - `xml/Includes_Bezel.xml` L2609: `</control><control type="image"><visible>$EXP[bz_navmenu] + String.IsEmpty(Window(Home).Property(bz_pos_on)) + !$EXP[bz_mmmushide] + ![Window.IsActive(music) + `
  - `xml/Includes_Bezel.xml` L2622: `<!-- 5.33.216 Music A/B art lane side a (BUG-010: own props, never bz_pos) --><control type="image"><visible>$EXP[bz_navmenu] + !$EXP[bz_mmmushide] + Window.IsA`

### `bz_mart_on`
- set/clear sites: 0 · read sites: 4
  - `xml/Includes_Bezel.xml` L2605: `</control><control type="image"><visible>$EXP[bz_navmenu] + String.IsEmpty(Window(Home).Property(bz_pos_on)) + !$EXP[bz_mmmushide] + ![Window.IsActive(music) + `
  - `xml/Includes_Bezel.xml` L2609: `</control><control type="image"><visible>$EXP[bz_navmenu] + String.IsEmpty(Window(Home).Property(bz_pos_on)) + !$EXP[bz_mmmushide] + ![Window.IsActive(music) + `
  - `xml/Includes_Bezel.xml` L2622: `<!-- 5.33.216 Music A/B art lane side a (BUG-010: own props, never bz_pos) --><control type="image"><visible>$EXP[bz_navmenu] + !$EXP[bz_mmmushide] + Window.IsA`

### `bz_mart_side`
- set/clear sites: 0 · read sites: 2
  - `xml/Includes_Bezel.xml` L2622: `<!-- 5.33.216 Music A/B art lane side a (BUG-010: own props, never bz_pos) --><control type="image"><visible>$EXP[bz_navmenu] + !$EXP[bz_mmmushide] + Window.IsA`
  - `xml/Includes_Bezel.xml` L2622: `<!-- 5.33.216 Music A/B art lane side a (BUG-010: own props, never bz_pos) --><control type="image"><visible>$EXP[bz_navmenu] + !$EXP[bz_mmmushide] + Window.IsA`

### `bz_mm`
- set/clear sites: 0 · read sites: 12
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_mm28`
- set/clear sites: 0 · read sites: 88
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_mmidle`
- set/clear sites: 3 · read sites: 21
  - `scripts/bz_flip.py` L1440: `home.clearProperty('bz_mmidle')`
  - `scripts/bz_flip.py` L1442: `home.clearProperty('bz_mmidle')   # touch / mouse / key not routed to 6897`
  - `scripts/bz_flip.py` L1454: `home.setProperty('bz_mmidle', '1'); home.setProperty('bz_mmidle_set', '1')`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L551: `</control><control type="group"><!-- 5.33.219 MM idle label: stacked PRESS ANY / BUTTON right of Bezel logo, only while bz_mmidle --><visible>$EXP[bz_navmenu] +`
  - `xml/Includes_Bezel.xml` L551: `</control><control type="group"><!-- 5.33.219 MM idle label: stacked PRESS ANY / BUTTON right of Bezel logo, only while bz_mmidle --><visible>$EXP[bz_navmenu] +`

### `bz_mmlive`
- set/clear sites: 8 · read sites: 14
  - `scripts/bz_flip.py` L730: `if xbmc.getCondVisibility('Control.HasFocus(6996)'): pos = xbmc.getInfoLabel('Container(6996).Position') or pos; home.setProperty('bz_mmlive', pos)   # t4094c l`
  - `scripts/bz_flip.py` L746: `home.setProperty('bz_mmpos', home.getProperty('bz_mmlive') or pos or '0')   # t4094b live row first; FLASH t3430: new window's onload restores this row (was row`
  - `scripts/bz_flip.py` L754: `if xbmc.getCondVisibility('Control.HasFocus(6996)'): _pp[0] = xbmc.getInfoLabel('Container(6996).Position') or _pp[0]; home.setProperty('bz_mmpos', _pp[0]); hom`
  - `xml/MyVideoNav.xml` L6: `<onload condition="!Control.HasFocus(6996) + !String.IsEqual(Window(home).Property(bz_mmpick),true) + !String.IsEmpty(Window(home).Property(bz_mmwarm)) + !Strin`
  - `xml/MyVideoNav.xml` L6: `<onload condition="!Control.HasFocus(6996) + !String.IsEqual(Window(home).Property(bz_mmpick),true) + !String.IsEmpty(Window(home).Property(bz_mmwarm)) + !Strin`
  - `xml/MyVideoNav.xml` L6: `<onload condition="!Control.HasFocus(6996) + !String.IsEqual(Window(home).Property(bz_mmpick),true) + !String.IsEmpty(Window(home).Property(bz_mmwarm)) + !Strin`

### `bz_mmmushide`
- set/clear sites: 0 · read sites: 16
  - `xml/Includes_Bezel.xml` L123: `<expression name="bz_mmmushide">Player.HasAudio + !Player.HasVideo + $EXP[bz_navmenu] + !String.IsEqual(Skin.String(bz_at_warmmusicposters),Off)</expression><!-`
  - `xml/Includes_Bezel.xml` L2559: `<control type="image"><left>990</left><top>120</top><width>600</width><height>900</height><texture>bezel/poster_blur.png</texture><!-- 3.5.1: only while the lis`
  - `xml/Includes_Bezel.xml` L2560: `<control type="image"><left>990</left><top>120</top><width>600</width><height>900</height><texture border="6">bezel/frame.png</texture><visible>!String.IsEmpty(`

### `bz_mmpick`
- set/clear sites: 3 · read sites: 16
  - `scripts/bz_mm.py` L65: `xbmcgui.Window(10000).setProperty('bz_mmpick', 'true')   # MMHIDE: a pick may focus the list under MM`
  - `scripts/bz_flip.py` L1081: `if home.getProperty('bz_mmpick'): home.clearProperty('bz_mmpick')`
  - `scripts/bz_flip.py` L1081: `if home.getProperty('bz_mmpick'): home.clearProperty('bz_mmpick')`
  - `xml/Includes_Bezel.xml` L4: `<include name="BezelMMFocusBounce"><onfocus condition="$EXP[bz_navmenu] + !String.IsEqual(Window(home).Property(bz_mmpick),true)">SetFocus(6996)</onfocus></incl`
  - `xml/Includes_Bezel.xml` L6: `<include name="BezelMMFocusBounceList"><onfocus condition="!String.IsEmpty(Window(home).Property(bz_mmwarm)) + !String.IsEqual(Window(home).Property(bz_mmpick),`
  - `xml/Includes_Bezel.xml` L6: `<include name="BezelMMFocusBounceList"><onfocus condition="!String.IsEmpty(Window(home).Property(bz_mmwarm)) + !String.IsEqual(Window(home).Property(bz_mmpick),`

### `bz_mmpos`
- set/clear sites: 6 · read sites: 4
  - `scripts/bz_flip.py` L746: `home.setProperty('bz_mmpos', home.getProperty('bz_mmlive') or pos or '0')   # t4094b live row first; FLASH t3430: new window's onload restores this row (was row`
  - `scripts/bz_flip.py` L754: `if xbmc.getCondVisibility('Control.HasFocus(6996)'): _pp[0] = xbmc.getInfoLabel('Container(6996).Position') or _pp[0]; home.setProperty('bz_mmpos', _pp[0]); hom`
  - `scripts/bz_flip.py` L755: `else: _pp[0] = home.getProperty('bz_mmlive') or _pp[0]; home.setProperty('bz_mmpos', _pp[0] or '0'); (_pk() or _bzstrip(home, _pp[0]))   # t4092 live row`
  - `xml/MyVideoNav.xml` L6: `<onload condition="!Control.HasFocus(6996) + !String.IsEqual(Window(home).Property(bz_mmpick),true) + !String.IsEmpty(Window(home).Property(bz_mmwarm)) + !Strin`
  - `xml/MyMusicNav.xml` L6: `<onload condition="!Control.HasFocus(6996) + !String.IsEqual(Window(home).Property(bz_mmpick),true) + !String.IsEmpty(Window(home).Property(bz_mmwarm)) + !Strin`
  - `scripts/bz_dbg.py` L3: `P = ('bz_nav', 'bz_mmwarm', 'bz_xfade', 'bz_mmpick', 'bz_mmlock', 'bz_mmpos', 'bz_mmlive', 'bz_navroot', 'bz_mmstart')`

### `bz_mmstart`
- set/clear sites: 5 · read sites: 8
  - `scripts/bz_cmd.py` L648: `home.clearProperty('bz_navgrace'); home.setProperty('bz_mmstart', '1'); home.setProperty('bz_nav', 'true')`
  - `scripts/bz_cmd.py` L671: `home.clearProperty('bz_navgrace'); home.setProperty('bz_mmstart', '1'); home.setProperty('bz_nav', 'true')`
  - `scripts/bz_flip.py` L1022: `if xbmc.getCondVisibility('Control.HasFocus(6996)') and not home.getProperty('bz_mmstart'): home.setProperty('bz_mmlive', xbmc.getInfoLabel('Container(6996).Pos`
  - `scripts/bz_dbg.py` L3: `P = ('bz_nav', 'bz_mmwarm', 'bz_xfade', 'bz_mmpick', 'bz_mmlock', 'bz_mmpos', 'bz_mmlive', 'bz_navroot', 'bz_mmstart')`
  - `scripts/bz_flip.py` L523: `on = (home.getProperty('bz_nav') == 'true' and not home.getProperty('bz_mmstart') and not home.getProperty('bz_mmwarm')`
  - `scripts/bz_flip.py` L641: `if home.getProperty('bz_mmstart') or home.getProperty('bz_secload') or home.getProperty('bz_navsub') or home.getProperty('bz_navset') or home.getProperty('bz_na`

### `bz_mmwarm`
- set/clear sites: 5 · read sites: 18
  - `scripts/bz_flip.py` L724: `home.setProperty('bz_mmwarm', 'true'); home.setProperty('bz_navroot', path)`
  - `scripts/bz_flip.py` L744: `home.clearProperty('bz_mmwarm'); home.clearProperty('bz_xfade')   # t4333: fade back in`
  - `scripts/bz_flip.py` L747: `home.setProperty('bz_mmwarm', 'true'); home.setProperty('bz_navroot', path)`
  - `xml/Includes_Bezel.xml` L6: `<include name="BezelMMFocusBounceList"><onfocus condition="!String.IsEmpty(Window(home).Property(bz_mmwarm)) + !String.IsEqual(Window(home).Property(bz_mmpick),`
  - `xml/Includes_Bezel.xml` L6: `<include name="BezelMMFocusBounceList"><onfocus condition="!String.IsEmpty(Window(home).Property(bz_mmwarm)) + !String.IsEqual(Window(home).Property(bz_mmpick),`
  - `xml/MyVideoNav.xml` L6: `<onload condition="!Control.HasFocus(6996) + !String.IsEqual(Window(home).Property(bz_mmpick),true) + !String.IsEmpty(Window(home).Property(bz_mmwarm)) + !Strin`

### `bz_movfanart_hold`
- set/clear sites: 1 · read sites: 2
  - `scripts/bz_flip.py` L374: `home.setProperty('bz_movfanart_hold', _mf)`
  - `scripts/bz_flip.py` L373: `if _mf and home.getProperty('bz_movfanart_hold') != _mf:`
  - `scripts/bz_flip.py` L1363: `v = home.getProperty('bz_movfanart_hold')`

### `bz_movposter_hold`
- set/clear sites: 1 · read sites: 3
  - `scripts/bz_flip.py` L371: `home.setProperty('bz_movposter_hold', _mp)`
  - `scripts/bz_flip.py` L370: `if _mp and not os.path.basename(_mp.rstrip('/')).startswith('Default') and home.getProperty('bz_movposter_hold') != _mp:`
  - `scripts/bz_flip.py` L1361: `# 5.33.189: movies-only fanart bridge (same idea as bz_movposter_hold) — unused on TV/Music`
  - `scripts/bz_flip.py` L1375: `v = home.getProperty('bz_movposter_hold')`

### `bz_mushref`
- set/clear sites: 6 · read sites: 5
  - `xml/Includes_Tuner.xml` L1963: `<!-- 5.33.191 WARM 2.0 --><onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),warmmusicposters)">Skin.SetString(bz_at_warmmusicposters,Off)<`
  - `xml/Includes_Tuner.xml` L1963: `<!-- 5.33.191 WARM 2.0 --><onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),warmmusicposters)">Skin.SetString(bz_at_warmmusicposters,Off)<`
  - `xml/Includes_Tuner.xml` L1963: `<!-- 5.33.191 WARM 2.0 --><onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),warmmusicposters)">Skin.SetString(bz_at_warmmusicposters,Off)<`
  - `xml/Includes_Bezel.xml` L2605: `</control><control type="image"><visible>$EXP[bz_navmenu] + String.IsEmpty(Window(Home).Property(bz_pos_on)) + !$EXP[bz_mmmushide] + ![Window.IsActive(music) + `
  - `xml/Includes_Bezel.xml` L2609: `</control><control type="image"><visible>$EXP[bz_navmenu] + String.IsEmpty(Window(Home).Property(bz_pos_on)) + !$EXP[bz_mmmushide] + ![Window.IsActive(music) + `
  - `xml/Includes_Bezel.xml` L2613: `</control><!-- 5.33.148 MM A/B pos side a --><control type="image"><visible>$EXP[bz_navmenu] + !$EXP[bz_mmmushide] + !String.IsEmpty(Window(Home).Property(bz_po`

### `bz_music_underlay`
- set/clear sites: 4 · read sites: 1
  - `scripts/bz_mm.py` L46: `home.clearProperty('bz_music_underlay')   # 5.33.164: real Music entry — underlay artists no longer owns the window`
  - `scripts/bz_flip.py` L635: `if home.getProperty('bz_music_underlay'): home.clearProperty('bz_music_underlay')   # real browse after underlay`
  - `scripts/bz_flip.py` L635: `if home.getProperty('bz_music_underlay'): home.clearProperty('bz_music_underlay')   # real browse after underlay`
  - `scripts/bz_flip.py` L632: `if home.getProperty('bz_music_underlay') and _artists:`

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

### `bz_navmenu`
- set/clear sites: 9 · read sites: 593
  - `xml/Includes_Bezel.xml` L2335: `<control type="list" id="63"><onback condition="[String.IsEmpty(Container.FolderPath) | String.IsEqual(Container.FolderPath,sources://pictures/)] + !$EXP[bz_nav`
  - `xml/MusicVisualisation.xml` L17: `<onunload condition="!$EXP[bz_navmenu]">AlarmClock(bz_vizret,SetFocus(60),00:00,silent)</onunload><!-- 5.33.112 t786: Play Next / viz exit -> section list 60 --`
  - `xml/FileManager.xml` L14: `<control type="list" id="20"><onback condition="String.IsEmpty(Container(20).FolderPath) + !$EXP[bz_navmenu]">SetProperty(bz_nav,true,home)</onback><!-- 5.33.17`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`
  - `xml/Includes_Dust3.xml` L11: `<variable name="BzD3L_mid"><!-- t4588 MM dim x lit --><value condition="$EXP[bz_navmenu] + String.IsEqual(Skin.String(bz_at_d3lit),1) + String.IsEqual(Skin.Stri`

### `bz_navroot`
- set/clear sites: 7 · read sites: 23
  - `scripts/bz_mm.py` L17: `'music': ['SetProperty(bz_navroot,musicdb://albums/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,tomusic,musicdb://albums/)'],`
  - `scripts/bz_mm.py` L18: `'movies': ['SetProperty(bz_navroot,videodb://movies/titles/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,go,videodb://movies/titles/)'],`
  - `scripts/bz_mm.py` L19: `'tv': ['SetProperty(bz_navroot,videodb://tvshows/titles/,home)', 'RunScript(special://skin/scripts/bz_cmd.py,go,videodb://tvshows/titles/)'],`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`

### `bz_navset`
- set/clear sites: 2 · read sites: 7
  - `xml/Custom_1118_PowerMenu.xml` L26: `<item><label>TUNER</label><onclick>SetProperty(bz_tunesrc,pwr,home)</onclick><onclick>SetProperty(bz_navtune,true,home)</onclick><onclick>ClearProperty(bz_navbe`
  - `scripts/bz_flip.py` L1012: `home.clearProperty('bz_navset'); home.clearProperty('bz_navsub'); home.clearProperty('bz_navnp'); home.clearProperty('bz_navset2'); home.clearProperty('bz_kset'`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`

### `bz_navsub`
- set/clear sites: 2 · read sites: 79
  - `scripts/bz_flip.py` L822: `if grp and cid and cid.isdigit() and int(cid) not in grp: home.clearProperty('bz_navsub')`
  - `scripts/bz_flip.py` L1012: `home.clearProperty('bz_navset'); home.clearProperty('bz_navsub'); home.clearProperty('bz_navnp'); home.clearProperty('bz_navset2'); home.clearProperty('bz_kset'`
  - `xml/Includes_Bezel.xml` L524: `<variable name="BzMMChev_music"><value condition="String.IsEqual(Window(Home).Property(bz_navsub),music)">[COLOR FFFFFFFF]▲[/COLOR]</value><value>[COLOR 8CFFFFF`
  - `xml/Includes_Bezel.xml` L525: `<variable name="BzMMChev_movies"><value condition="String.IsEqual(Window(Home).Property(bz_navsub),movies)">[COLOR FFFFFFFF]▲[/COLOR]</value><value>[COLOR 8CFFF`
  - `xml/Includes_Bezel.xml` L526: `<variable name="BzMMChev_tv"><value condition="String.IsEqual(Window(Home).Property(bz_navsub),tv)">[COLOR FFFFFFFF]▲[/COLOR]</value><value>[COLOR 8CFFFFFF]▼[/C`

### `bz_navtune`
- set/clear sites: 21 · read sites: 45
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_pos`
- set/clear sites: 0 · read sites: 4
  - `xml/Includes_Bezel.xml` L2622: `<!-- 5.33.216 Music A/B art lane side a (BUG-010: own props, never bz_pos) --><control type="image"><visible>$EXP[bz_navmenu] + !$EXP[bz_mmmushide] + Window.IsA`
  - `xml/Includes_Bezel.xml` L2622: `<!-- 5.33.216 Music A/B art lane side a (BUG-010: own props, never bz_pos) --><control type="image"><visible>$EXP[bz_navmenu] + !$EXP[bz_mmmushide] + Window.IsA`
  - `scripts/bz_flip.py` L1365: `def _ab_poster():   # BUG-010: poster A/B lane is Videos-only — never Music thumb/Icon into bz_pos`

### `bz_pos_`
- set/clear sites: 0 · read sites: 0

### `bz_pos_a`
- set/clear sites: 1 · read sites: 6
  - `scripts/bz_flip.py` L688: `for k in ('bz_pos_a', 'bz_pos_b', 'bz_pos_side', 'bz_pos_empty'): home.clearProperty(k)`
  - `xml/Includes_Bezel.xml` L1212: `<texture background="true">$INFO[Window(Home).Property(bz_pos_a)]</texture>`
  - `xml/Includes_Bezel.xml` L1283: `<texture background="true">$INFO[Window(Home).Property(bz_pos_a)]</texture>`
  - `xml/Includes_Bezel.xml` L2616: `<texture background="true">$INFO[Window(Home).Property(bz_pos_a)]</texture>`

### `bz_pos_empty`
- set/clear sites: 1 · read sites: 9
  - `scripts/bz_flip.py` L688: `for k in ('bz_pos_a', 'bz_pos_b', 'bz_pos_side', 'bz_pos_empty'): home.clearProperty(k)`
  - `xml/Includes_Bezel.xml` L1202: `<control type="image"><visible>$EXP[bz_navmenu] + ![!String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAudio + String.IsEmpty(Window(Home).Property(`
  - `xml/Includes_Bezel.xml` L1209: `</control><!-- 5.33.148 MM A/B pos side a --><control type="image"><visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAu`
  - `xml/Includes_Bezel.xml` L1216: `</control><!-- 5.33.148 MM A/B pos side b --><control type="image"><visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAu`

### `bz_pos_on`
- set/clear sites: 1 · read sites: 18
  - `scripts/bz_flip.py` L683: `if enter_music: home.clearProperty('bz_pos_on'); home.clearProperty('bz_hold_poster')   # video poster A/B fades out over the new Music album`
  - `xml/Includes_Bezel.xml` L1202: `<control type="image"><visible>$EXP[bz_navmenu] + ![!String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAudio + String.IsEmpty(Window(Home).Property(`
  - `xml/Includes_Bezel.xml` L1209: `</control><!-- 5.33.148 MM A/B pos side a --><control type="image"><visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAu`
  - `xml/Includes_Bezel.xml` L1216: `</control><!-- 5.33.148 MM A/B pos side b --><control type="image"><visible>$EXP[bz_navmenu] + !String.IsEmpty(Window(Home).Property(bz_pos_on)) + !Player.HasAu`

### `bz_precache`
- set/clear sites: 0 · read sites: 2
  - `xml/Includes_Bezel.xml` L637: `<!-- BEZEL 3.0: artwork pre-cache target (bz_precache.py): 1 px, alpha 1/255, so Kodi loads + caches the texture -->`
  - `xml/Home.xml` L10: `<onload condition="!String.IsEqual(Window(Home).Property(bz_precache_running),true)">RunScript(special://skin/scripts/bz_precache.py)</onload><!-- BEZEL 3.0: ar`

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

### `bz_splash_done`
- set/clear sites: 2 · read sites: 12
  - `xml/Startup.xml` L6: `<onload>ClearProperty(bz_splash_done,home)</onload>`
  - `scripts/bz_warmgate.py` L89: `home.setProperty('bz_splash_done', '1')`
  - `xml/Includes_Bezel.xml` L633: `<include name="BezelAmbientBelow"><control type="group"><visible>Skin.HasSetting(bz_amb_below) + !Skin.HasSetting(bz_dust_off) + String.IsEqual(Window(Home).Pro`
  - `xml/Custom_1114_Dust.xml` L7: `<visible>String.IsEqual(Window(Home).Property(bz_splash_done),1) + !Skin.HasSetting(bz_dust_off) + !Window.IsActive(fullscreenvideo) + !Window.IsActive(slidesho`
  - `scripts/bz_cmd.py` L660: `# not after bz_splash_done, so the splash fades straight onto the Main menu instead of Music first, menu ~later.`

### `bz_top`
- set/clear sites: 0 · read sites: 18
  - `xml/Includes_Bezel.xml` L1565: `<left>bz_list_x</left><top>bz_top</top><width>450</width><height>bz_h</height><!-- 4.2 section standard: group at bz_list_x (was 420 / 550; BETA 1.3: list at 0 `
  - `xml/Includes_Bezel.xml` L1568: `<control type="grouplist"><!-- t4533: TRUE CLIP for list 60. A grouplist scissors its children to its own rect (bz_list_x,bz_top 450x900 = bottom y1020); the co`
  - `xml/Includes_Bezel.xml` L2355: `<constant name="bz_top">120</constant>`

### `bz_tvclear_off`
- set/clear sites: 0 · read sites: 12
  - `xml/Includes_Bezel.xml` L282: `<variable name="BzTVClearOnOff"><value condition="Skin.HasSetting(bz_tvclear_off)">OFF</value><value>ON</value></variable>`
  - `xml/Includes_Bezel.xml` L2408: `<!-- 5.33.180 BUG-025: TV fanart-block upper-left bold show title when no clear art (or bz_tvclear_off); same gates as t4153 strip fallback --><control type="la`
  - `xml/Includes_Bezel.xml` L2408: `<!-- 5.33.180 BUG-025: TV fanart-block upper-left bold show title when no clear art (or bz_tvclear_off); same gates as t4153 strip fallback --><control type="la`

### `bz_warm_gate`
- set/clear sites: 4 · read sites: 6
  - `xml/Startup.xml` L5: `<onload condition="!String.IsEqual(Skin.String(bz_at_warmsplash),Off)">SetProperty(bz_warm_gate,1,home)</onload>`
  - `scripts/bz_warmgate.py` L76: `home.clearProperty('bz_warm_gate')`
  - `scripts/bz_warmgate.py` L99: `home.clearProperty('bz_warm_gate')`
  - `xml/Includes_Bezel.xml` L596: `<!-- 5.33.66 t438 global backdrop (remove: delete this + the include line in BezelBlack) --><variable name="BzGbdCol"><!-- 5.33.81 t525 level 0 = 5% --><value c`
  - `xml/Includes_Bezel.xml` L3672: `<visible>!String.IsEmpty(Window(Home).Property(bz_warm_gate)) + !String.IsEqual(Skin.String(bz_at_warmsplash),Off)</visible>`
  - `scripts/bz_precache.py` L14: `'Container.Scrolling | !System.IdleTime(3) | Window.IsActive(1113) | !String.IsEmpty(Window(Home).Property(bz_warm_gate))')`

### `bz_warm_ready_`
- set/clear sites: 2 · read sites: 2
  - `scripts/bz_warmgate.py` L46: `home.setProperty('bz_warm_ready_' + sec, '1')`
  - `scripts/bz_warmgate.py` L104: `home.clearProperty('bz_warm_ready_' + s)`
  - `scripts/bz_warmgate.py` L145: `if all(home.getProperty('bz_warm_ready_' + s) for s in PATHS):`
  - `scripts/bz_warmgate.py` L155: `if all(home.getProperty('bz_warm_ready_' + s) for s in PATHS):`

### `bz_warm_ready_music`
- set/clear sites: 0 · read sites: 0

### `bz_warmgate`
- set/clear sites: 0 · read sites: 2
  - `xml/Startup.xml` L7: `<onload>RunScript(special://skin/scripts/bz_warmgate.py)</onload>`
  - `xml/Custom_1113_WarmGate.xml` L2: `<!-- 1113 WARM GATE (legacy dialog). 5.33.199+: bz_warmgate.py does NOT ActivateWindow(1113) — type=dialog is modal and blocked Music (10502). Splash is BezelWa`

### `bz_warmgate_running`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_warmgate.py` L90: `home.clearProperty('bz_warmgate_running')`
  - `scripts/bz_warmgate.py` L95: `home.setProperty('bz_warmgate_running', '1')`
  - `scripts/bz_warmgate.py` L93: `if home.getProperty('bz_warmgate_running'):`

### `bz_warmhold`
- set/clear sites: 0 · read sites: 2
  - `xml/Includes_Bezel.xml` L715: `<expression name="bz_warmhold">$EXP[bz_navmenu] + !String.IsEqual(Skin.String(bz_at_warmhold),Off) + !String.IsEmpty(Window(Home).Property(bz_fan_on))</expressi`
  - `xml/Includes_Bezel.xml` L718: `<visible>$EXP[bz_warmhold]</visible>`

### `bz_warmrow`
- set/clear sites: 2 · read sites: 2
  - `scripts/bz_flip.py` L616: `home.setProperty('bz_warmrow', p2.rstrip('/'))   # 5.33.218: tell the grid sync this folder's list row is a WARM row (do not reset to item 0)`
  - `scripts/bz_flip.py` L1140: `home.clearProperty('bz_warmrow'); j0 = mp.get(xbmc.getInfoLabel('Container(60).ListItem.DBID') or xbmc.getInfoLabel('Container(60).ListItem.Label'))`
  - `scripts/bz_flip.py` L1138: `if j0 is None and home.getProperty('bz_warmrow') and home.getProperty('bz_warmrow') == (sig[0] or '').rstrip('/'):`
  - `scripts/bz_flip.py` L1138: `if j0 is None and home.getProperty('bz_warmrow') and home.getProperty('bz_warmrow') == (sig[0] or '').rstrip('/'):`

### `bz_xalb`
- set/clear sites: 2 · read sites: 2
  - `scripts/bz_flip.py` L689: `if not home.getProperty('bz_xalb_on'): home.clearProperty('bz_xalb')`
  - `scripts/bz_flip.py` L703: `if _alb and not os.path.basename(_alb.rstrip('/')).startswith('Default'): home.setProperty('bz_xalb', _alb); home.setProperty('bz_xalb_on', '1')`
  - `xml/Includes_Bezel.xml` L2601: `<control type="image"><visible>$EXP[bz_navmenu] + Window.IsActive(videos) + !String.IsEmpty(Window(Home).Property(bz_xalb_on)) + !String.IsEmpty(Window(Home).Pr`
  - `xml/Includes_Bezel.xml` L2604: `<texture background="true">$INFO[Window(Home).Property(bz_xalb)]</texture>`

### `bz_xalb_on`
- set/clear sites: 3 · read sites: 2
  - `scripts/bz_flip.py` L684: `else: home.clearProperty('bz_xalb_on')   # held Music album fades out under the incoming poster A/B`
  - `scripts/bz_flip.py` L689: `if not home.getProperty('bz_xalb_on'): home.clearProperty('bz_xalb')`
  - `scripts/bz_flip.py` L703: `if _alb and not os.path.basename(_alb.rstrip('/')).startswith('Default'): home.setProperty('bz_xalb', _alb); home.setProperty('bz_xalb_on', '1')`
  - `xml/Includes_Bezel.xml` L2601: `<control type="image"><visible>$EXP[bz_navmenu] + Window.IsActive(videos) + !String.IsEmpty(Window(Home).Property(bz_xalb_on)) + !String.IsEmpty(Window(Home).Pr`
  - `scripts/bz_flip.py` L720: `if enter_music or home.getProperty('bz_xalb_on'): _xfade_out(enter_music)   # 5.33.204 mvidfade (BUG-010: poster lane released after the 1.5 s fade)`

### `bz_xfade`
- set/clear sites: 5 · read sites: 2
  - `scripts/bz_flip.py` L719: `home.clearProperty('bz_xfade'); home.clearProperty('bz_xfin'); home.clearProperty('bz_arthold')   # 5.33.147: fade-in only`
  - `scripts/bz_flip.py` L725: `home.clearProperty('bz_xfin'); home.clearProperty('bz_xfade')   # 5.33.147: no section dim-out / no bz_xfin arm — fade-in only via art hold then release`
  - `scripts/bz_flip.py` L744: `home.clearProperty('bz_mmwarm'); home.clearProperty('bz_xfade')   # t4333: fade back in`
  - `xml/Includes_Tuner.xml` L2294: `<item><label>Glow style</label><label2>$VAR[BzATVal_mmglowsty]</label2><property name="info">$VAR[BzMMGlowInfo]</property><property name="kind">slider</property`
  - `scripts/bz_dbg.py` L3: `P = ('bz_nav', 'bz_mmwarm', 'bz_xfade', 'bz_mmpick', 'bz_mmlock', 'bz_mmpos', 'bz_mmlive', 'bz_navroot', 'bz_mmstart')`

### `bz_xfin`
- set/clear sites: 5 · read sites: 1
  - `scripts/bz_flip.py` L719: `home.clearProperty('bz_xfade'); home.clearProperty('bz_xfin'); home.clearProperty('bz_arthold')   # 5.33.147: fade-in only`
  - `scripts/bz_flip.py` L725: `home.clearProperty('bz_xfin'); home.clearProperty('bz_xfade')   # 5.33.147: no section dim-out / no bz_xfin arm — fade-in only via art hold then release`
  - `scripts/bz_flip.py` L725: `home.clearProperty('bz_xfin'); home.clearProperty('bz_xfade')   # 5.33.147: no section dim-out / no bz_xfin arm — fade-in only via art hold then release`
  - `xml/Includes_Bezel.xml` L630: `<variable name="BzGDimCol"><value>00FFFFFF</value></variable><!-- 4.7.2: Global dimmer LOOK → MM scrim alpha --><include name="BezelSecDim"><!-- 5.33.147: warm `

