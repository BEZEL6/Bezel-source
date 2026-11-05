# Home / startup splash — home-splash

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `home-splash` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/home-splash.md) · [layout](../layout/home-splash.md) · [state](../state/home-splash.md) · [motion](../motion/home-splash.md) · [art](../art/home-splash.md) · [input](../input/home-splash.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
At start, a splash covers the screen while BEZEL builds its windows and warms artwork. It stays at least 5 s and at most 15 s, then fades over 3 s straight onto the Main Menu. Nothing pops and nothing flashes blank.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

**See screen:** [home-splash baselines](../port-refs/home-splash/) — smoke baseline + port diff target.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_at_mmdef`
- set/clear sites: 14 · read sites: 8
  - `xml/Includes_Tuner.xml` L1603: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdef) + String.IsEqual(Skin.String(bz_at_mmdef),1)">Skin.SetString(bz_at_mmdef,3)</onle`
  - `xml/Includes_Tuner.xml` L1603: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdef) + String.IsEqual(Skin.String(bz_at_mmdef),1)">Skin.SetString(bz_at_mmdef,3)</onle`
  - `xml/Includes_Tuner.xml` L1603: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),mmdef) + String.IsEqual(Skin.String(bz_at_mmdef),1)">Skin.SetString(bz_at_mmdef,3)</onle`
  - `xml/Includes_Tuner.xml` L472: `<variable name="BzATVal_mmdef"><value condition="String.IsEqual(Skin.String(bz_at_mmdef),1)">MUSIC</value><value condition="String.IsEqual(Skin.String(bz_at_mmd`
  - `xml/Includes_Tuner.xml` L472: `<variable name="BzATVal_mmdef"><value condition="String.IsEqual(Skin.String(bz_at_mmdef),1)">MUSIC</value><value condition="String.IsEqual(Skin.String(bz_at_mmd`
  - `scripts/bz_cmd.py` L635: `# t5012: pill defaults on cold start — Artists / Titles / Shows (index 1). Tuner Startup highlight (bz_at_mmdef) untouched.`

### `bz_at_warmsplash`
- set/clear sites: 3 · read sites: 4
  - `xml/Includes_Tuner.xml` L1961: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),warmsplash)">Skin.SetString(bz_at_warmsplash,Off)</onleft><onright condition="String.IsE`
  - `xml/Includes_Tuner.xml` L1961: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),warmsplash)">Skin.SetString(bz_at_warmsplash,Off)</onleft><onright condition="String.IsE`
  - `xml/Startup.xml` L5: `<onload condition="!String.IsEqual(Skin.String(bz_at_warmsplash),Off)">SetProperty(bz_warm_gate,1,home)</onload>`
  - `xml/Includes_Bezel.xml` L3672: `<visible>!String.IsEmpty(Window(Home).Property(bz_warm_gate)) + !String.IsEqual(Skin.String(bz_at_warmsplash),Off)</visible>`
  - `xml/Includes_Tuner.xml` L116: `<variable name="BzATVal_warmsplash"><value condition="String.IsEqual(Skin.String(bz_at_warmsplash),Off)">Off (warm still runs)</value><value>On</value></variabl`
  - `xml/Startup.xml` L4: `<!-- Tuner WARM 2.0 > Startup splash (bz_at_warmsplash, default On): Off hides splash VISUALS only; warm-cache always runs. -->`

### `bz_attn_outline`
- set/clear sites: 1 · read sites: 1
  - `scripts/bz_cmd.py` L628: `xbmc.executebuiltin('Skin.SetString(bz_at_hishape,5)'); xbmc.executebuiltin('Skin.SetString(bz_attn_outline,1)')`
  - `scripts/bz_cmd.py` L627: `if not xbmc.getInfoLabel('Skin.String(bz_attn_outline)'):   # attnqueue #9: global outline bar default once (Tuner LOOK > bar shape still changes it)`

### `bz_cmd`
- set/clear sites: 10 · read sites: 99
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/Includes_Tuner.xml` L1960: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),uadv)">Skin.ToggleSetting(bz_uadv_off)</onright><onleft condition="String.IsEqual(Conta`
  - `xml/MyPlaylist.xml` L3: `<onload>RunScript(special://skin/scripts/bz_cmd.py,backdrop)</onload>`
  - `xml/DialogSelect.xml` L8: `<!-- 5.0.2 Choose art: bz_artsel (set by bz_cmd.py chooseart) wins over Refresh / Std -->`
  - `xml/Includes_BezelChooseArt.xml` L2: `<!-- 5.0.2 Choose art (Rob t3826): type rows IN the colour strip; shaped thumbnail grid over the fanart only. Driven by bz_cmd.py chooseart via Home prop bz_art`

### `bz_defseed`
- set/clear sites: 1 · read sites: 2
  - `scripts/bz_tune.py` L78: `apply_defs('everything'); xbmc.executebuiltin('Skin.SetString(bz_defseed,%s)' % DEF.get('ver')); xbmc.sleep(300)`
  - `xml/Home.xml` L8: `<onload condition="!String.IsEqual(Skin.String(bz_defseed),5.0.20)">RunScript(special://skin/scripts/bz_tune.py,seed)</onload><!-- t4691: Rob default picks seed`
  - `scripts/bz_tune.py` L77: `if DEF and xbmc.getInfoLabel('Skin.String(bz_defseed)') != DEF.get('ver'):`

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

### `bz_last_mmsub_`
- set/clear sites: 2 · read sites: 2
  - `scripts/bz_cmd.py` L638: `xbmc.executebuiltin('Skin.SetString(bz_last_mmsub_%s,1)' % _pk)`
  - `scripts/bz_mm.py` L43: `xbmc.executebuiltin('Skin.SetString(bz_last_mmsub_%s,%d)' % (key, i)); home.setProperty('bz_mmsub_' + key, str(i))   # t4075 keep pill at last used`
  - `scripts/bz_cmd.py` L625: `_v = xbmc.getInfoLabel('Skin.String(bz_last_mmsub_%s)' % _k)`
  - `scripts/bz_mm.py` L51: `v = xbmc.getInfoLabel('Skin.String(bz_last_mmsub_%s)' % k)`

### `bz_mmstart`
- set/clear sites: 5 · read sites: 8
  - `scripts/bz_cmd.py` L648: `home.clearProperty('bz_navgrace'); home.setProperty('bz_mmstart', '1'); home.setProperty('bz_nav', 'true')`
  - `scripts/bz_cmd.py` L671: `home.clearProperty('bz_navgrace'); home.setProperty('bz_mmstart', '1'); home.setProperty('bz_nav', 'true')`
  - `scripts/bz_flip.py` L1022: `if xbmc.getCondVisibility('Control.HasFocus(6996)') and not home.getProperty('bz_mmstart'): home.setProperty('bz_mmlive', xbmc.getInfoLabel('Container(6996).Pos`
  - `scripts/bz_dbg.py` L3: `P = ('bz_nav', 'bz_mmwarm', 'bz_xfade', 'bz_mmpick', 'bz_mmlock', 'bz_mmpos', 'bz_mmlive', 'bz_navroot', 'bz_mmstart')`
  - `scripts/bz_flip.py` L523: `on = (home.getProperty('bz_nav') == 'true' and not home.getProperty('bz_mmstart') and not home.getProperty('bz_mmwarm')`
  - `scripts/bz_flip.py` L641: `if home.getProperty('bz_mmstart') or home.getProperty('bz_secload') or home.getProperty('bz_navsub') or home.getProperty('bz_navset') or home.getProperty('bz_na`

### `bz_mmstartrow`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_cmd.py` L647: `home.setProperty('bz_mmstartrow', str(_r)); home.setProperty('bz_mmstartsec', _secs[_r])`
  - `scripts/bz_flip.py` L1038: `else: xbmc.executebuiltin('SetFocus(6996,%s,absolute)' % (home.getProperty('bz_mmstartrow') or '0')); home.setProperty('bz_navstrip', home.getProperty('bz_mmsta`
  - `scripts/bz_flip.py` L1024: `_sr = home.getProperty('bz_mmstartrow') or '0'   # t4315: Startup highlight - land on the chosen row before releasing MM-start`

### `bz_mmstartsec`
- set/clear sites: 3 · read sites: 0
  - `scripts/bz_cmd.py` L647: `home.setProperty('bz_mmstartrow', str(_r)); home.setProperty('bz_mmstartsec', _secs[_r])`
  - `scripts/bz_flip.py` L1027: `home.setProperty('bz_navstrip', home.getProperty('bz_mmstartsec') or 'music'); home.setProperty('bz_mmlive', _sr); home.setProperty('bz_mmpos', _sr)`
  - `scripts/bz_flip.py` L1038: `else: xbmc.executebuiltin('SetFocus(6996,%s,absolute)' % (home.getProperty('bz_mmstartrow') or '0')); home.setProperty('bz_navstrip', home.getProperty('bz_mmsta`

### `bz_mmsub_`
- set/clear sites: 6 · read sites: 3
  - `scripts/bz_cmd.py` L626: `if _v and not home.getProperty('bz_mmsub_' + _k): home.setProperty('bz_mmsub_' + _k, _v)`
  - `scripts/bz_cmd.py` L626: `if _v and not home.getProperty('bz_mmsub_' + _k): home.setProperty('bz_mmsub_' + _k, _v)`
  - `scripts/bz_cmd.py` L637: `home.setProperty('bz_mmsub_' + _pk, '1')`
  - `scripts/bz_mm.py` L31: `# 4.2.0 O59 (D3): music / movies / tv open the primed sub (home bz_mmsub_<sec>, 1-based; empty = default Artists / Titles / Shows)`
  - `scripts/bz_mm.py` L39: `explicit = home.getProperty('bz_mmsub_' + key) != ''   # t4149: any set pill (incl. 1=Artists) opens that pill; empty = keep last location`
  - `scripts/bz_mm.py` L40: `try: i = int(home.getProperty('bz_mmsub_' + key) or d)`

### `bz_nav`
- set/clear sites: 75 · read sites: 103
  - `xml/Custom_1107_SearchDialog.xml` L23: `<control type="list" id="9000"><onback>SetProperty(bz_nav,true,home)</onback><onback>Dialog.Close(1107,true)</onback><!-- 5.33.235 Rob t1837: control onback con`
  - `xml/Custom_1112_NowPlaying.xml` L50: `<onfocus>ClearProperty(bz_nav,home)</onfocus><onfocus>ClearProperty(bz_navtune,home)</onfocus><onfocus>ClearProperty(bz_navbez,home)</onfocus><onfocus>SetFocus(`
  - `xml/Includes_Bezel.xml` L537: `<onclick>ClearProperty(bz_nav,home)</onclick><onclick>ClearProperty(bz_navtune,home)</onclick><onclick>ClearProperty(bz_navbez,home)</onclick><!-- MMHIDE: tap o`
  - `xml/Custom_1112_NowPlaying.xml` L15: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L16: `<onload condition="![String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visuali`
  - `xml/Custom_1112_NowPlaying.xml` L17: `<onload condition="[String.IsEqual(Window(Home).Property(bz_np),true) | [Window.IsActive(music) + Player.HasAudio + !Player.HasVideo + !Window.IsActive(visualis`

### `bz_navgrace`
- set/clear sites: 5 · read sites: 4
  - `scripts/bz_cmd.py` L648: `home.clearProperty('bz_navgrace'); home.setProperty('bz_mmstart', '1'); home.setProperty('bz_nav', 'true')`
  - `scripts/bz_cmd.py` L671: `home.clearProperty('bz_navgrace'); home.setProperty('bz_mmstart', '1'); home.setProperty('bz_nav', 'true')`
  - `scripts/bz_flip.py` L1007: `if nav_was[0] and not nv: home.setProperty('bz_navgrace', 'true'); navgr[0] = now`
  - `xml/Includes_Bezel.xml` L414: `<expression name="bz_navok">String.IsEmpty(Window(Home).Property(bz_navlock)) + String.IsEmpty(Window(Home).Property(bz_navgrace)) + !String.IsEqual(Window(Home`
  - `scripts/bz_flip.py` L1003: `if not nv and not home.getProperty('bz_navgrace') and not home.getProperty('bz_navlock'):`
  - `scripts/bz_flip.py` L1005: `# BEZEL 3.0: one close routine. Any close sets bz_navgrace (0.5 s lock + 0.3 s grace); every open path checks $EXP[bz_navok],`

### `bz_nomenustart`
- set/clear sites: 0 · read sites: 3
  - `scripts/bz_cmd.py` L640: `if first and not xbmc.getCondVisibility('Skin.HasSetting(bz_nomenustart)'):`
  - `scripts/bz_cmd.py` L664: `if xbmc.getCondVisibility('!Skin.HasSetting(bz_nomenustart) + Window.IsActive(music)') and not home.getProperty('bz_nav'):`
  - `scripts/bz_cmd.py` L670: `if xbmc.getCondVisibility('!Skin.HasSetting(bz_nomenustart) + Window.IsActive(music)') and not home.getProperty('bz_nav'):`

### `bz_precache`
- set/clear sites: 0 · read sites: 2
  - `xml/Includes_Bezel.xml` L637: `<!-- BEZEL 3.0: artwork pre-cache target (bz_precache.py): 1 px, alpha 1/255, so Kodi loads + caches the texture -->`
  - `xml/Home.xml` L10: `<onload condition="!String.IsEqual(Window(Home).Property(bz_precache_running),true)">RunScript(special://skin/scripts/bz_precache.py)</onload><!-- BEZEL 3.0: ar`

### `bz_precache_running`
- set/clear sites: 3 · read sites: 2
  - `scripts/bz_precache.py` L24: `home.setProperty('bz_precache_running', 'true')`
  - `scripts/bz_precache.py` L41: `if not mon.abortRequested(): home.clearProperty('bz_pc_img'); home.clearProperty('bz_precache_running')   # BEZEL 3.0 exit fix`
  - `scripts/bz_cmd.py` L21: `for k in ('bz_flip_running', 'bz_dtap_running', 'bz_precache_running'): home.clearProperty(k)`
  - `xml/Home.xml` L10: `<onload condition="!String.IsEqual(Window(Home).Property(bz_precache_running),true)">RunScript(special://skin/scripts/bz_precache.py)</onload><!-- BEZEL 3.0: ar`
  - `scripts/bz_precache.py` L23: `if home.getProperty('bz_precache_running') != 'true':`

### `bz_showall_inited`
- set/clear sites: 1 · read sites: 2
  - `scripts/bz_cmd.py` L620: `xbmc.executebuiltin('Skin.SetString(bz_showall_inited,1)')`
  - `scripts/bz_cmd.py` L616: `# Skin.HasSetting is false both when unset and when user turned Off, so only apply once per userdata via bz_showall_inited.`
  - `scripts/bz_cmd.py` L617: `if not xbmc.getInfoLabel('Skin.String(bz_showall_inited)'):`

### `bz_showall_sync`
- set/clear sites: 0 · read sites: 3
  - `scripts/bz_cmd.py` L565: `def _bz_showall_sync(only=None):`
  - `scripts/bz_cmd.py` L584: `_bz_showall_sync(_sa)`
  - `scripts/bz_cmd.py` L622: `_bz_showall_sync()`

### `bz_splash_done`
- set/clear sites: 2 · read sites: 12
  - `xml/Startup.xml` L6: `<onload>ClearProperty(bz_splash_done,home)</onload>`
  - `scripts/bz_warmgate.py` L89: `home.setProperty('bz_splash_done', '1')`
  - `xml/Includes_Bezel.xml` L633: `<include name="BezelAmbientBelow"><control type="group"><visible>Skin.HasSetting(bz_amb_below) + !Skin.HasSetting(bz_dust_off) + String.IsEqual(Window(Home).Pro`
  - `xml/Custom_1114_Dust.xml` L7: `<visible>String.IsEqual(Window(Home).Property(bz_splash_done),1) + !Skin.HasSetting(bz_dust_off) + !Window.IsActive(fullscreenvideo) + !Window.IsActive(slidesho`
  - `scripts/bz_cmd.py` L660: `# not after bz_splash_done, so the splash fades straight onto the Main menu instead of Music first, menu ~later.`

### `bz_started`
- set/clear sites: 1 · read sites: 1
  - `scripts/bz_cmd.py` L632: `if first: home.setProperty('bz_started', 'true'); home.setProperty('bz_startfade', 'true')`
  - `scripts/bz_cmd.py` L631: `first = not home.getProperty('bz_started')`

### `bz_startfade`
- set/clear sites: 2 · read sites: 5
  - `scripts/bz_cmd.py` L632: `if first: home.setProperty('bz_started', 'true'); home.setProperty('bz_startfade', 'true')`
  - `scripts/bz_cmd.py` L672: `xbmc.Monitor().waitForAbort(6); home.clearProperty('bz_startfade')`
  - `xml/Includes_Bezel.xml` L1406: `<animation effect="fade" start="0" end="100" time="2500" tween="sine" easing="inout" condition="String.IsEqual(Window(Home).Property(bz_startfade),true)">Window`
  - `xml/Includes_Bezel.xml` L1543: `<animation effect="fade" start="0" end="100" time="1800" delay="1200" tween="sine" easing="inout" condition="String.IsEqual(Window(Home).Property(bz_startfade),`
  - `xml/Includes_Bezel.xml` L2277: `<animation effect="fade" start="0" end="100" time="1800" delay="1200" tween="sine" easing="inout" condition="String.IsEqual(Window(Home).Property(bz_startfade),`

### `bz_tune`
- set/clear sites: 0 · read sites: 96
  - `xml/Home.xml` L8: `<onload condition="!String.IsEqual(Skin.String(bz_defseed),5.0.20)">RunScript(special://skin/scripts/bz_tune.py,seed)</onload><!-- t4691: Rob default picks seed`
  - `xml/Includes_Tuner.xml` L1414: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),alldust)">RunScript(special://skin/scripts/bz_tune.py,alldust,off)</onleft><onright cond`
  - `xml/Includes_Tuner.xml` L1414: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),alldust)">RunScript(special://skin/scripts/bz_tune.py,alldust,off)</onleft><onright cond`

### `bz_tunever`
- set/clear sites: 1 · read sites: 2
  - `scripts/bz_cmd.py` L607: `xbmc.executebuiltin('Skin.SetString(bz_tunever,401)')`
  - `scripts/bz_cmd.py` L598: `if action == 'start' and xbmc.getInfoLabel('Skin.String(bz_tunever)') != '401':`
  - `scripts/bz_cmd.py` L600: `# once (bz_tunever=401), then the fixed-time steps are re-patched into the skin files so nothing shifts for existing users.`

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

### `bz_warmgate`
- set/clear sites: 0 · read sites: 2
  - `xml/Startup.xml` L7: `<onload>RunScript(special://skin/scripts/bz_warmgate.py)</onload>`
  - `xml/Custom_1113_WarmGate.xml` L2: `<!-- 1113 WARM GATE (legacy dialog). 5.33.199+: bz_warmgate.py does NOT ActivateWindow(1113) — type=dialog is modal and blocked Music (10502). Splash is BezelWa`

### `bz_warmgate_running`
- set/clear sites: 2 · read sites: 1
  - `scripts/bz_warmgate.py` L90: `home.clearProperty('bz_warmgate_running')`
  - `scripts/bz_warmgate.py` L95: `home.setProperty('bz_warmgate_running', '1')`
  - `scripts/bz_warmgate.py` L93: `if home.getProperty('bz_warmgate_running'):`

