# Playlists — playlists

**Object:** `playlists` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/playlists.md) · [layout](../layout/playlists.md) · [state](../state/playlists.md) · [motion](../motion/playlists.md) · [art](../art/playlists.md) · [input](../input/playlists.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_backdrop`
- set/clear sites: 21 · read sites: 21
  - `xml/MyPlaylist.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/MyPlaylist.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/Settings.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/Includes_Bezel.xml` L542: `<!-- 4.6.5 Section Settings description on the void (Tuner B positions, outside the clip) --><control type="group"><visible>$EXP[bz_navmenu] + String.IsEqual(Wi`
  - `xml/Includes_Bezel.xml` L3048: `<texture colordiffuse="$VAR[BezelBackdropAlpha]">$INFO[Window(Home).Property(bz_backdrop)]</texture>`
  - `xml/Includes_Bezel.xml` L3049: `<visible>String.IsEmpty(Window(Home).Property(bz_npdlg)) + [Skin.HasSetting(bezel_norotate) | String.IsEmpty(Control.GetLabel(9880))] + String.IsEmpty(ListItem.`

### `bz_backdrop_last`
- set/clear sites: 14 · read sites: 1
  - `xml/MyPlaylist.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/MyPlaylist.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `xml/Settings.xml` L4: `<onunload>SetProperty(bz_backdrop_last,$INFO[Window(Home).Property(bz_backdrop)],home)</onunload><onunload>ClearProperty(bz_backdrop,home)</onunload><!-- 4.7.5:`
  - `scripts/bz_cmd.py` L83: `cur = home.getProperty('bz_backdrop') or home.getProperty('bz_backdrop_last')  # 4.7.5: cleared on window close`

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_ctx`
- set/clear sites: 0 · read sites: 14
  - `xml/Custom_1119_SecCtx.xml` L45: `<control type="button" id="7904"><label>Favourite</label><onclick>RunScript(special://skin/scripts/bz_ctx.py,fav)</onclick><visible>[Window.IsActive(programs) |`
  - `xml/Custom_1119_SecCtx.xml` L56: `<control type="button" id="7947"><label>Favourite</label><onclick>RunScript(special://skin/scripts/bz_ctx.py,fav)</onclick><visible>Window.IsActive(pictures)</v`
  - `xml/DialogMusicInfo.xml` L14: `<control type="grouplist" id="9000"><left>582</left><top>166</top><width>360</width><height>420</height><itemgap>2</itemgap><orientation>vertical</orientation><`

### `bz_dtap`
- set/clear sites: 0 · read sites: 7
  - `xml/Includes_Tuner.xml` L498: `<!-- Kodi resets only the first Visible/Hidden animation of a control, so a changed step must not stay applied: any change marks bz_tune_dirty and bz_dtap.py re`
  - `xml/Includes_Tuner.xml` L2410: `<item><label>5.33.11  Settings strip</label><property name="kind">btn</property><property name="id"></property><property name="info">bezel/info/ver_5_33_10.png<`
  - `scripts/bz_cmd.py` L42: `xbmc.executebuiltin('RunScript(special://skin/scripts/bz_dtap.py)')   # BETA 2.8: double-tap Select service (guards itself)`

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

### `bz_sway_restart`
- set/clear sites: 4 · read sites: 5
  - `xml/MyPlaylist.xml` L10: `<onload>SetProperty(bz_sway_restart,true,home)</onload>`
  - `xml/MusicVisualisation.xml` L15: `<onload>SetProperty(bz_sway_restart,true,home)</onload>`
  - `xml/MyMusicNav.xml` L18: `<onload>SetProperty(bz_sway_restart,true,home)</onload>`
  - `xml/Custom_1121_MusicFanartFS.xml` L19: `<!-- no bz_sway_restart: sway must stay unbroken (Music never remounts) -->`
  - `xml/Includes_Tuner.xml` L2075: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),swayshort)">Skin.Reset(bz_swayright)</onleft><onleft condition="String.IsEqual(Container`
  - `xml/Includes_Tuner.xml` L2075: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),swayshort)">Skin.Reset(bz_swayright)</onleft><onleft condition="String.IsEqual(Container`

