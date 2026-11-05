# Keymaps (BEZEL profile keymaps) — keymaps

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `keymaps` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/keymaps.md) · [layout](../layout/keymaps.md) · [state](../state/keymaps.md) · [motion](../motion/keymaps.md) · [art](../art/keymaps.md) · [input](../input/keymaps.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
A skin cannot ship keymaps, so BEZEL writes its own into the Kodi profile while BEZEL is the skin. It removes them again as soon as you switch skins, so other skins behave normally.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_at_dtapwin`
- set/clear sites: 58 · read sites: 50
  - `xml/Includes_Tuner.xml` L1062: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtapwin) + String.IsEqual(Skin.String(bz_at_dtapwin),2)">Skin.SetString(bz_at_dtapwin,1)`
  - `xml/Includes_Tuner.xml` L1062: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtapwin) + String.IsEqual(Skin.String(bz_at_dtapwin),2)">Skin.SetString(bz_at_dtapwin,1)`
  - `xml/Includes_Tuner.xml` L1063: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtapwin) + String.IsEqual(Skin.String(bz_at_dtapwin),3)">Skin.SetString(bz_at_dtapwin,2)`
  - `xml/Includes_Tuner.xml` L334: `<variable name="BzATVal_dtapwin"><value condition="String.IsEqual(Skin.String(bz_at_dtapwin),1)">150 ms</value><value condition="String.IsEqual(Skin.String(bz_a`
  - `xml/Includes_Tuner.xml` L334: `<variable name="BzATVal_dtapwin"><value condition="String.IsEqual(Skin.String(bz_at_dtapwin),1)">150 ms</value><value condition="String.IsEqual(Skin.String(bz_a`
  - `xml/Includes_Tuner.xml` L334: `<variable name="BzATVal_dtapwin"><value condition="String.IsEqual(Skin.String(bz_at_dtapwin),1)">150 ms</value><value condition="String.IsEqual(Skin.String(bz_a`

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

### `bz_dtap_off`
- set/clear sites: 4 · read sites: 10
  - `xml/Includes_Tuner.xml` L1606: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtap)">Skin.SetBool(bz_dtap_off)</onleft><onright condition="String.IsEqual(Container(69`
  - `xml/Includes_Tuner.xml` L1606: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),dtap)">Skin.SetBool(bz_dtap_off)</onleft><onright condition="String.IsEqual(Container(69`
  - `scripts/bz_tune.py` L110: `if 'dtap' in st: xbmc.executebuiltin('Skin.SetBool(bz_dtap_off)' if st['dtap'].get('value') == 'OFF' else 'Skin.Reset(bz_dtap_off)')`
  - `xml/Includes_Bezel.xml` L44: `<control type="group"><visible>!Window.IsActive(1120) + !Skin.HasSetting(bz_dtap_off) + [Control.IsVisible(60) | Control.IsVisible(63) | [Control.IsVisible(50) `
  - `xml/Includes_Tuner.xml` L474: `<variable name="BzATVal_dtap"><value condition="Skin.HasSetting(bz_dtap_off)">OFF</value><value>ON</value></variable>`
  - `xml/Includes_Tuner.xml` L2434: `<variable name="BzATPillOff"><value condition="Skin.HasSetting(bz_dtap_off)">FF3D6FA0</value><value>40FFFFFF</value></variable>`

### `bz_dtap_running`
- set/clear sites: 4 · read sites: 2
  - `scripts/bz_cmd.py` L21: `for k in ('bz_flip_running', 'bz_dtap_running', 'bz_precache_running'): home.clearProperty(k)`
  - `scripts/bz_dtap.py` L111: `home.setProperty('bz_dtap_running', 'true')`
  - `scripts/bz_dtap.py` L146: `home.clearProperty('bz_dtap_running')`
  - `scripts/bz_dtap.py` L2: `# Service (one instance, guard bz_dtap_running). While it runs and Skin setting bz_dtap_off is NOT set it installs`
  - `scripts/bz_dtap.py` L110: `if home.getProperty('bz_dtap_running') != 'true':`

### `bz_dtapinfo`
- set/clear sites: 6 · read sites: 0
  - `scripts/bz_dtap.py` L100: `home.setProperty('bz_dtapinfo', '1'); info(); threading.Timer(0.8, lambda: home.clearProperty('bz_dtapinfo')).start(); return`
  - `scripts/bz_dtap.py` L100: `home.setProperty('bz_dtapinfo', '1'); info(); threading.Timer(0.8, lambda: home.clearProperty('bz_dtapinfo')).start(); return`
  - `scripts/bz_dtap.py` L105: `st['pend'] = False; home.setProperty('bz_dtapinfo', '1'); info(); threading.Timer(0.8, lambda: home.clearProperty('bz_dtapinfo')).start()   # 5.0.3 #5: double t`

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

### `bz_km`
- set/clear sites: 1 · read sites: 12
  - `scripts/bz_flip.py` L462: `bz_km.leave(); home.clearProperty('bz_flip_running'); return`
  - `scripts/bz_cmd.py` L39: `sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import bz_km; bz_km.leave()`
  - `scripts/bz_cmd.py` L39: `sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import bz_km; bz_km.leave()`
  - `scripts/bz_flip.py` L459: `import sys as _s; _s.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import bz_km`

### `bz_km_loaded`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_km.py` L18: `try: xbmcgui.Window(10000).clearProperty('bz_km_loaded')`
  - `scripts/bz_cmd.py` L66: `home.setProperty('bz_km_loaded', 'np3')`
  - `scripts/bz_cmd.py` L52: `if bytes(new) != bytes(old) or home.getProperty('bz_km_loaded') != 'np3':`

### `bz_navlock`
- set/clear sites: 1 · read sites: 6
  - `scripts/bz_flip.py` L815: `elif now - navlk[0] >= 0.25: home.clearProperty('bz_navlock'); navlk[0] = 0.0`
  - `xml/Includes_Bezel.xml` L414: `<expression name="bz_navok">String.IsEmpty(Window(Home).Property(bz_navlock)) + String.IsEmpty(Window(Home).Property(bz_navgrace)) + !String.IsEqual(Window(Home`
  - `scripts/bz_flip.py` L812: `# BETA 1.3: slide menu: Up / Down set bz_navlock (XML); further presses are ignored until the bar glide (280 ms) is done`
  - `scripts/bz_flip.py` L813: `if home.getProperty('bz_navlock'):`

### `bz_navtune`
- set/clear sites: 21 · read sites: 45
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`
  - `xml/Includes_Bezel.xml` L540: `<!-- 4.1 O43: logo / glow / Kodi text removed. O46: strip-list Main menu. O47: black fade in, list slides in behind the strip, menu fades in; select fades the a`

### `bz_quit_dtap`
- set/clear sites: 1 · read sites: 1
  - `scripts/bz_dtap.py` L151: `if home.getProperty('bz_quit'): home.setProperty('bz_quit_dtap', 'true')`
  - `scripts/bz_cmd.py` L24: `while time.time() - t0 < 1.5 and not home.getProperty('bz_quit_dtap'): xbmc.sleep(50)`

### `bz_secfan`
- set/clear sites: 2 · read sites: 2
  - `scripts/bz_dtap.py` L136: `if home.getProperty('bz_secfan') != f: home.setProperty('bz_secfan', f)`
  - `scripts/bz_dtap.py` L136: `if home.getProperty('bz_secfan') != f: home.setProperty('bz_secfan', f)`
  - `xml/Includes_BezelInfo.xml` L16: `<variable name="BzCIStageFan"><!-- 5.33.31 t265: same image the section stage shows (9880 rotation mirror) = one fanart, not a swap/second copy --><value condit`
  - `xml/Includes_BezelInfo.xml` L16: `<variable name="BzCIStageFan"><!-- 5.33.31 t265: same image the section stage shows (9880 rotation mirror) = one fanart, not a swap/second copy --><value condit`

### `bz_secfanlbl`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_dtap.py` L137: `if home.getProperty('bz_secfanlbl') != l: home.setProperty('bz_secfanlbl', l)`
  - `scripts/bz_dtap.py` L137: `if home.getProperty('bz_secfanlbl') != l: home.setProperty('bz_secfanlbl', l)`
  - `xml/Includes_BezelInfo.xml` L16: `<variable name="BzCIStageFan"><!-- 5.33.31 t265: same image the section stage shows (9880 rotation mirror) = one fanart, not a swap/second copy --><value condit`

### `bz_sel`
- set/clear sites: 0 · read sites: 3
  - `scripts/bz_dtap.py` L4: `# fullscreen video) as NotifyAll(bz,bz_sel). One tap -> Action(Select) once the window (tuner bz_at_dtapwin, 200-500 ms, default 300) has passed;`
  - `scripts/bz_dtap.py` L12: `SEL = 'NotifyAll(bz,bz_sel)'`
  - `scripts/bz_dtap.py` L101: `if not method.endswith('bz_sel'): return`

### `bz_setback`
- set/clear sites: 0 · read sites: 3
  - `scripts/bz_dtap.py` L30: `''.join('\t<%s>\n\t\t<keyboard><backspace>NotifyAll(bz,bz_setback)</backspace></keyboard>\n\t\t<remote><back>NotifyAll(bz,bz_setback)</back></remote>\n\t</%s>\n`
  - `scripts/bz_dtap.py` L30: `''.join('\t<%s>\n\t\t<keyboard><backspace>NotifyAll(bz,bz_setback)</backspace></keyboard>\n\t\t<remote><back>NotifyAll(bz,bz_setback)</back></remote>\n\t</%s>\n`
  - `scripts/bz_dtap.py` L93: `if method.endswith('bz_setback'):   # 5.33.11: Settings Back - sub-list (grouplist 5) -> parent category list 3, else normal Back`

### `bz_tabq`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_flip.py` L933: `if time.time() - tabq[0] > 20: home.clearProperty('bz_tabq'); tabq[0] = 0`
  - `scripts/bz_flip.py` L935: `home.clearProperty('bz_tabq'); tabq[0] = 0`
  - `scripts/bz_flip.py` L931: `if home.getProperty('bz_tabq'):`

### `bz_tune_dirty`
- set/clear sites: 5 · read sites: 39
  - `scripts/bz_cmd.py` L104: `home.setProperty('bz_tune_dirty', '1')`
  - `scripts/bz_dtap.py` L129: `st['dirty_t'] = None; home.clearProperty('bz_tune_dirty'); reload_tuned()`
  - `scripts/bz_tune.py` L17: `def setv(i, v): xbmcgui.Window(10000).setProperty('bz_tune_dirty', '1'); xbmc.executebuiltin('Skin.SetString(bz_at_%s,%s)' % (i, v)) if v else xbmc.executebuilt`
  - `xml/Includes_Tuner.xml` L498: `<!-- Kodi resets only the first Visible/Hidden animation of a control, so a changed step must not stay applied: any change marks bz_tune_dirty and bz_dtap.py re`
  - `xml/Includes_Tuner.xml` L498: `<!-- Kodi resets only the first Visible/Hidden animation of a control, so a changed step must not stay applied: any change marks bz_tune_dirty and bz_dtap.py re`
  - `xml/Includes_Tuner.xml` L498: `<!-- Kodi resets only the first Visible/Hidden animation of a control, so a changed step must not stay applied: any change marks bz_tune_dirty and bz_dtap.py re`

