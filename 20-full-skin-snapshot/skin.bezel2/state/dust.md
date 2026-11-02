# Dust (ambient particle layers) — dust

**Object:** `dust` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/dust.md) · [layout](../layout/dust.md) · [state](../state/dust.md) · [motion](../motion/dust.md) · [art](../art/dust.md) · [input](../input/dust.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Slow drifting dust in the black space of the screen. It starts once after the splash and keeps drifting across window changes, so it never restarts or jumps.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_adust_off`
- set/clear sites: 2 · read sites: 8
  - `xml/Includes_Tuner.xml` L1319: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),fs_ttl)">Skin.SetBool(bz_fs_ttl_off)</onleft><onright condition="String.IsEqual(Containe`
  - `xml/Includes_Tuner.xml` L1319: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),fs_ttl)">Skin.SetBool(bz_fs_ttl_off)</onleft><onright condition="String.IsEqual(Containe`
  - `xml/Includes_Dust3.xml` L27: `<include name="BezelLitDust"><control type="group"><visible>!Skin.HasSetting(bz_adust_off) + !Skin.HasSetting(bz_dust_off)</visible><control type="grouplist"><l`
  - `xml/Includes_Tuner.xml` L376: `<variable name="BzATVal_adust"><value condition="Skin.HasSetting(bz_adust_off)">OFF</value><value>ON</value></variable>`
  - `xml/Includes_Tuner.xml` L410: `<variable name="BzInfoD_adust"><value condition="Skin.HasSetting(bz_adust_off) | Skin.HasSetting(bz_dust_off)">1</value><value>0</value></variable>`

### `bz_amb_below`
- set/clear sites: 0 · read sites: 177
  - `xml/Includes_Bezel.xml` L413: `<include name="BezelRootArtHide"><control type="image"><left>962</left><top>0</top><width>958</width><height>1080</height><texture colordiffuse="FF000000">bezel`
  - `xml/Includes_Bezel.xml` L606: `<include name="BezelBlackSec"><control type="group"><visible>![Skin.HasSetting(bz_amb_below) + [Window.IsActive(music) | Window.IsActive(videos)]]</visible><inc`
  - `xml/Includes_Bezel.xml` L633: `<include name="BezelAmbientBelow"><control type="group"><visible>Skin.HasSetting(bz_amb_below) + !Skin.HasSetting(bz_dust_off) + String.IsEqual(Window(Home).Pro`

### `bz_at_mmdbright`
- set/clear sites: 38 · read sites: 36
  - `xml/Includes_Tuner.xml` L501: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdbright) + String.IsEmpty(Skin.String(bz_at_mmdbright))">Skin.SetString(bz_at_mmdbrig`
  - `xml/Includes_Tuner.xml` L501: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdbright) + String.IsEmpty(Skin.String(bz_at_mmdbright))">Skin.SetString(bz_at_mmdbrig`
  - `xml/Includes_Tuner.xml` L502: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdbright) + String.IsEqual(Skin.String(bz_at_mmdbright),1)">Skin.SetString(bz_at_mmdbr`
  - `xml/Includes_Tuner.xml` L63: `<variable name="BzMMDustA"><value condition="String.IsEqual(Skin.String(bz_at_mmdbright),1)">1AFFFFFF</value><value condition="String.IsEqual(Skin.String(bz_at_`
  - `xml/Includes_Tuner.xml` L63: `<variable name="BzMMDustA"><value condition="String.IsEqual(Skin.String(bz_at_mmdbright),1)">1AFFFFFF</value><value condition="String.IsEqual(Skin.String(bz_at_`
  - `xml/Includes_Tuner.xml` L63: `<variable name="BzMMDustA"><value condition="String.IsEqual(Skin.String(bz_at_mmdbright),1)">1AFFFFFF</value><value condition="String.IsEqual(Skin.String(bz_at_`

### `bz_back`
- set/clear sites: 4 · read sites: 27
  - `xml/Includes_Bezel.xml` L646: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !String.IsEmpty(Window(Home).Property(bz_back))">SetProperty(bz_back_clos`
  - `xml/MyMusicNav.xml` L13: `<onload>ClearProperty(bz_back,home)</onload>`
  - `scripts/bz_flip.py` L279: `home.clearProperty('bz_back'); on = False`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L455: `<visible>Player.HasAudio + !String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_back_fade))</visible>`
  - `xml/Includes_Bezel.xml` L647: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !!String.IsEmpty(Window(Home).Property(bz_back)) + Control.IsVisible(60)"`

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_dust_nocut`
- set/clear sites: 0 · read sites: 2
  - `xml/Custom_1114_Dust.xml` L11: `<control type="group"><visible>Skin.HasSetting(bz_amb_below) + !Skin.HasSetting(bz_dust_nocut)</visible><!-- 4.7.2 BELOW: void-clipped -->`
  - `xml/Custom_1114_Dust.xml` L92: `<control type="group"><visible>!Skin.HasSetting(bz_amb_below) | Skin.HasSetting(bz_dust_nocut)</visible><!-- 4.7.2 ABOVE: full screen over panels / art (layer-s`

### `bz_dust_off`
- set/clear sites: 2 · read sites: 18
  - `xml/Includes_Tuner.xml` L1318: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dust)">Skin.SetBool(bz_dust_off)</onleft><onright condition="String.IsEqual(Container(69`
  - `xml/Includes_Tuner.xml` L1318: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dust)">Skin.SetBool(bz_dust_off)</onleft><onright condition="String.IsEqual(Container(69`
  - `xml/Includes_Dust3.xml` L27: `<include name="BezelLitDust"><control type="group"><visible>!Skin.HasSetting(bz_adust_off) + !Skin.HasSetting(bz_dust_off)</visible><control type="grouplist"><l`
  - `xml/Includes_Dust3.xml` L52: `<include name="BezelLitDustP"><control type="group"><visible>!Skin.HasSetting(bz_dust_off)</visible><control type="grouplist"><left>$PARAM[bl]</left><top>$PARAM`
  - `xml/Includes_Bezel.xml` L633: `<include name="BezelAmbientBelow"><control type="group"><visible>Skin.HasSetting(bz_amb_below) + !Skin.HasSetting(bz_dust_off) + String.IsEqual(Window(Home).Pro`

### `bz_gridset`
- set/clear sites: 0 · read sites: 10
  - `xml/Includes_Bezel.xml` L357: `<expression name="bz_gridset">[Window.IsActive(music) + Skin.HasSetting(bz_grid_music)] | [Window.IsActive(videos) + Skin.HasSetting(bz_grid_video)]</expression`
  - `xml/Includes_Bezel.xml` L431: `<variable name="BezelViewName"><value condition="$EXP[bz_gridset]">GRID</value><value condition="Window.IsActive(music) + Skin.HasSetting(bz_albumlist)">ALBUM L`
  - `xml/Custom_1114_Dust.xml` L12: `<control type="group"><visible>Window.IsActive(music) + !$EXP[bz_gridset] + !$EXP[bz_np] + String.IsEmpty(Window(Home).Property(bz_back)) + [!true | Player.HasA`

### `bz_np`
- set/clear sites: 33 · read sites: 98
  - `xml/Custom_1112_NowPlaying.xml` L19: `<onunload condition="!Window.IsActive(visualisation)">ClearProperty(bz_np,home)</onunload>`
  - `xml/Custom_1112_NowPlaying.xml` L42: `<onclick>ClearProperty(bz_np,home)</onclick><onclick>Dialog.Close(1112)</onclick></control>`
  - `xml/Custom_1112_NowPlaying.xml` L44: `<control type="button" id="6299"><left>-400</left><top>0</top><width>10</width><height>10</height><label></label><texturefocus></texturefocus><texturenofocus></`
  - `xml/Custom_1112_NowPlaying.xml` L3: `list view (view 60, not the grid): bz_cmd.py np (logo menu entry, 60 s idle open) sets bz_npdlg + bz_np and opens it. Every other route keeps the in-place panel`
  - `xml/Custom_1112_NowPlaying.xml` L4: `Back / Left / the logo close it; bz_flip.py closes it if bz_np is cleared elsewhere.`
  - `xml/Custom_1112_NowPlaying.xml` L13: `and run Kodi's fullscreen music window (the old route). Opened by bz_cmd.py (menu card, idle) bz_np is already set. -->`

### `bz_splash_done`
- set/clear sites: 2 · read sites: 12
  - `xml/Startup.xml` L6: `<onload>ClearProperty(bz_splash_done,home)</onload>`
  - `scripts/bz_warmgate.py` L89: `home.setProperty('bz_splash_done', '1')`
  - `xml/Includes_Bezel.xml` L633: `<include name="BezelAmbientBelow"><control type="group"><visible>Skin.HasSetting(bz_amb_below) + !Skin.HasSetting(bz_dust_off) + String.IsEqual(Window(Home).Pro`
  - `xml/Custom_1114_Dust.xml` L7: `<visible>String.IsEqual(Window(Home).Property(bz_splash_done),1) + !Skin.HasSetting(bz_dust_off) + !Window.IsActive(fullscreenvideo) + !Window.IsActive(slidesho`
  - `scripts/bz_cmd.py` L660: `# not after bz_splash_done, so the splash fades straight onto the Main menu instead of Music first, menu ~later.`

### `bz_tune`
- set/clear sites: 0 · read sites: 96
  - `xml/Home.xml` L8: `<onload condition="!String.IsEqual(Skin.String(bz_defseed),5.0.20)">RunScript(special://skin/scripts/bz_tune.py,seed)</onload><!-- t4691: Rob default picks seed`
  - `xml/Includes_Tuner.xml` L1414: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),alldust)">RunScript(special://skin/scripts/bz_tune.py,alldust,off)</onleft><onright cond`
  - `xml/Includes_Tuner.xml` L1414: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),alldust)">RunScript(special://skin/scripts/bz_tune.py,alldust,off)</onleft><onright cond`

### `bz_tune_patch`
- set/clear sites: 0 · read sites: 18
  - `xml/Includes_Bezel.xml` L529: `<!-- BEZEL 3.1 slide menu (gen/gen_menu31.py): drops from the block top; one open / one close anim (BezelATMenuAnim, written by bz_tune_patch._tuner); everythin`
  - `xml/Includes_Bezel.xml` L1619: `<control type="group"><!-- 4.3 item 18 + 4.0.1 O21: rows 1-15 drop 40 px; time = speed x (1 + 0.35 row/14), quadratic out; delay = row x stagger, both scaled by`
  - `xml/Includes_Bezel.xml` L1640: `<control type="group"><!-- 4.3 item 18 + 4.0.1 O21: rows 1-15 drop 40 px; time = speed x (1 + 0.35 row/14), quadratic out; delay = row x stagger, both scaled by`

