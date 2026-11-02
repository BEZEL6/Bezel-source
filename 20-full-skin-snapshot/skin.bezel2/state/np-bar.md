# NP bar / now-playing chrome — np-bar

**Object:** `np-bar` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/np-bar.md) · [layout](../layout/np-bar.md) · [state](../state/np-bar.md) · [motion](../motion/np-bar.md) · [art](../art/np-bar.md) · [input](../input/np-bar.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_audio_latch`
- set/clear sites: 4 · read sites: 47
  - `scripts/bz_flip.py` L946: `if home.getProperty('bz_np') and home.getProperty('bz_audio_latch') != 'true': home.clearProperty('bz_np')`
  - `scripts/bz_flip.py` L1516: `home.setProperty('bz_audio_latch', 'true'); sway['t0'] = time.time()   # sway (keyed on the latch) starts from flat`
  - `scripts/bz_flip.py` L1519: `if gone >= 2.5 or xbmc.getCondVisibility('Player.HasVideo'): home.clearProperty('bz_audio_latch'); gone = 0.0; sway['t0'] = None; had = False`
  - `xml/Custom_1112_NowPlaying.xml` L14: `<!-- BETA 1.1b: the gate below uses Player.HasAudio directly (the debounced bz_audio_latch from bz_flip.py may not be set yet on the first Tab after Kodi start;`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L125: `<expression name="bz_audio">[Player.HasAudio + !Player.HasVideo] | String.IsEqual(Window(Home).Property(bz_audio_latch),true)</expression>`

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_fsnp`
- set/clear sites: 5 · read sites: 2
  - `xml/MusicVisualisation.xml` L11: `<onload>SetProperty(bz_fsnp,true,home)</onload>`
  - `xml/MusicVisualisation.xml` L16: `<onunload condition="String.IsEqual(Window(Home).Property(bz_fsnp),true)">ClearProperty(bz_np,home)</onunload>`
  - `xml/MusicVisualisation.xml` L17: `<onunload condition="!$EXP[bz_navmenu]">AlarmClock(bz_vizret,SetFocus(60),00:00,silent)</onunload><!-- 5.33.112 t786: Play Next / viz exit -> section list 60 --`
  - `xml/Includes_Bezel.xml` L2801: `<expression name="bz_np">String.IsEqual(Window(Home).Property(bz_np),true) + [Window.IsActive(music) | String.IsEqual(Window(Home).Property(bz_fsnp),true)] + St`
  - `xml/MusicVisualisation.xml` L21: `<visible>String.IsEqual(Window(Home).Property(bz_fsnp),true)</visible>`

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

