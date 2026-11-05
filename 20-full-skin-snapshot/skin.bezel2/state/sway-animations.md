# Sway animations — shared clock, album, poster, stub cast — sway-animations

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `sway-animations` · **Layer:** state (props / flags) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/sway-animations.md) · [layout](../layout/sway-animations.md) · [state](../state/sway-animations.md) · [motion](../motion/sway-animations.md) · [art](../art/sway-animations.md) · [input](../input/sway-animations.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
- The big album (Music) and the poster (Movies/TV) slowly rock left and right, like a picture tilting on a wall.

**This layer in one line:** the switches (Home window properties) that turn this object on/off and move it between states — a port makes these view-model fields.

## Deep (rebuild detail)
Every `bz_*` name this object's behavior references, with live definition sites (first 6). Global meanings: [home-properties](home-properties.md).

### `bz_at_fsvizop`
- set/clear sites: 41 · read sites: 55
  - `xml/Includes_Tuner.xml` L1808: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),fsvizop) + String.IsEqual(Skin.String(bz_at_fsvizop),2)">Skin.SetString(bz_at_fsvizop,1)`
  - `xml/Includes_Tuner.xml` L1808: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),fsvizop) + String.IsEqual(Skin.String(bz_at_fsvizop),2)">Skin.SetString(bz_at_fsvizop,1)`
  - `xml/Includes_Tuner.xml` L1809: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),fsvizop) + String.IsEqual(Skin.String(bz_at_fsvizop),3)">Skin.SetString(bz_at_fsvizop,2)`
  - `xml/Includes_Bezel.xml` L1015: `<control type="group"><!-- 5.33.156: Viz opacity (bz_at_fsvizop) also drives stub/side album opacity --><animation effect="fade" start="0" end="0" time="0" cond`
  - `xml/Includes_Bezel.xml` L1015: `<control type="group"><!-- 5.33.156: Viz opacity (bz_at_fsvizop) also drives stub/side album opacity --><animation effect="fade" start="0" end="0" time="0" cond`
  - `xml/Includes_Bezel.xml` L1015: `<control type="group"><!-- 5.33.156: Viz opacity (bz_at_fsvizop) also drives stub/side album opacity --><animation effect="fade" start="0" end="0" time="0" cond`

### `bz_at_pcsoft`
- set/clear sites: 13 · read sites: 19
  - `xml/Includes_Tuner.xml` L1763: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),pcsoft) + [String.IsEmpty(Skin.String(bz_at_pcsoft)) | String.IsEqual(Skin.String(bz_at`
  - `xml/Includes_Tuner.xml` L1763: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),pcsoft) + [String.IsEmpty(Skin.String(bz_at_pcsoft)) | String.IsEqual(Skin.String(bz_at`
  - `xml/Includes_Tuner.xml` L1763: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),pcsoft) + [String.IsEmpty(Skin.String(bz_at_pcsoft)) | String.IsEqual(Skin.String(bz_at`
  - `xml/Includes_Bezel.xml` L628: `<variable name="BzCastTex_p"><value condition="String.IsEqual(Skin.String(bz_at_pcsoft),2)">bezel/sway_shadow.png</value><value condition="String.IsEqual(Skin.S`
  - `xml/Includes_Bezel.xml` L628: `<variable name="BzCastTex_p"><value condition="String.IsEqual(Skin.String(bz_at_pcsoft),2)">bezel/sway_shadow.png</value><value condition="String.IsEqual(Skin.S`
  - `xml/Includes_Bezel.xml` L628: `<variable name="BzCastTex_p"><value condition="String.IsEqual(Skin.String(bz_at_pcsoft),2)">bezel/sway_shadow.png</value><value condition="String.IsEqual(Skin.S`

### `bz_at_pcstyle`
- set/clear sites: 21 · read sites: 27
  - `xml/Includes_Tuner.xml` L1741: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),pcstyle) + [String.IsEmpty(Skin.String(bz_at_pcstyle)) | String.IsEqual(Skin.String(bz_`
  - `xml/Includes_Tuner.xml` L1741: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),pcstyle) + [String.IsEmpty(Skin.String(bz_at_pcstyle)) | String.IsEqual(Skin.String(bz_`
  - `xml/Includes_Tuner.xml` L1741: `<onright condition="String.IsEqual(Container(6970).ListItem.Property(id),pcstyle) + [String.IsEmpty(Skin.String(bz_at_pcstyle)) | String.IsEqual(Skin.String(bz_`
  - `xml/Includes_Bezel.xml` L628: `<variable name="BzCastTex_p"><value condition="String.IsEqual(Skin.String(bz_at_pcsoft),2)">bezel/sway_shadow.png</value><value condition="String.IsEqual(Skin.S`
  - `xml/Includes_Bezel.xml` L628: `<variable name="BzCastTex_p"><value condition="String.IsEqual(Skin.String(bz_at_pcsoft),2)">bezel/sway_shadow.png</value><value condition="String.IsEqual(Skin.S`
  - `xml/Includes_Bezel.xml` L628: `<variable name="BzCastTex_p"><value condition="String.IsEqual(Skin.String(bz_at_pcsoft),2)">bezel/sway_shadow.png</value><value condition="String.IsEqual(Skin.S`

### `bz_audio_latch`
- set/clear sites: 4 · read sites: 47
  - `scripts/bz_flip.py` L946: `if home.getProperty('bz_np') and home.getProperty('bz_audio_latch') != 'true': home.clearProperty('bz_np')`
  - `scripts/bz_flip.py` L1516: `home.setProperty('bz_audio_latch', 'true'); sway['t0'] = time.time()   # sway (keyed on the latch) starts from flat`
  - `scripts/bz_flip.py` L1519: `if gone >= 2.5 or xbmc.getCondVisibility('Player.HasVideo'): home.clearProperty('bz_audio_latch'); gone = 0.0; sway['t0'] = None; had = False`
  - `xml/Custom_1112_NowPlaying.xml` L14: `<!-- BETA 1.1b: the gate below uses Player.HasAudio directly (the debounced bz_audio_latch from bz_flip.py may not be set yet on the first Tab after Kodi start;`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L125: `<expression name="bz_audio">[Player.HasAudio + !Player.HasVideo] | String.IsEqual(Window(Home).Property(bz_audio_latch),true)</expression>`

### `bz_back`
- set/clear sites: 4 · read sites: 27
  - `xml/Includes_Bezel.xml` L646: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !String.IsEmpty(Window(Home).Property(bz_back))">SetProperty(bz_back_clos`
  - `xml/MyMusicNav.xml` L13: `<onload>ClearProperty(bz_back,home)</onload>`
  - `scripts/bz_flip.py` L279: `home.clearProperty('bz_back'); on = False`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L455: `<visible>Player.HasAudio + !String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_back_fade))</visible>`
  - `xml/Includes_Bezel.xml` L647: `<onclick condition="!$EXP[bz_np] + !!String.IsEmpty(Window(Home).Property(bz_vback)) + !!String.IsEmpty(Window(Home).Property(bz_back)) + Control.IsVisible(60)"`

### `bz_backanim`
- set/clear sites: 3 · read sites: 19
  - `xml/MyMusicNav.xml` L14: `<onload>ClearProperty(bz_backanim,home)</onload>`
  - `scripts/bz_flip.py` L284: `home.clearProperty('bz_backanim'); home.clearProperty('bz_back_fade'); closed_at = None`
  - `scripts/bz_flip.py` L1600: `for k in ('bz_back', 'bz_backanim', 'bz_back_pick', 'bz_albumid', 'bz_pswayon', 'bz_ppulse', 'bz_ppulse2', 'bz_pready', 'bz_vreq', 'bz_sway_pulse2', 'bz_castL',`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L1131: `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="!String.IsEmpty(Window(Home).Property(bz_back)) | !String.IsEmpty`
  - `xml/Includes_Bezel.xml` L1141: `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="!String.IsEmpty(Window(Home).Property(bz_back)) | !String.IsEmpty`

### `bz_big_go`
- set/clear sites: 1 · read sites: 10
  - `scripts/bz_flip.py` L1599: `home.clearProperty('bz_sway_pulse'); home.clearProperty('bz_sway_go'); home.clearProperty('bz_big_go'); home.clearProperty('bz_big_pulse')`
  - `xml/Includes_Bezel.xml` L1065: `<control type="group"><!-- BETA 2.5: +-4 deg idle sway on the whole album stack (inside the slide, so it pivots at the album's actual centre); bz_big_go / bz_bi`
  - `xml/Includes_Bezel.xml` L1066: `<animation effect="rotate" start="0" end="-4" center="1440,570" time="5000" tween="sine" easing="inout" condition="String.IsEqual(Window(Home).Property(bz_big_g`
  - `xml/Includes_Bezel.xml` L1077: `then a +-4 deg rotate about its centre (one-shot 0 -> 4 in 5 s at bz_big_go, then an 8.5 s sine in-out pulse 4 <-> -4 at bz_big_pulse, both from bz_flip.py); ev`

### `bz_big_pulse`
- set/clear sites: 1 · read sites: 22
  - `scripts/bz_flip.py` L1599: `home.clearProperty('bz_sway_pulse'); home.clearProperty('bz_sway_go'); home.clearProperty('bz_big_go'); home.clearProperty('bz_big_pulse')`
  - `xml/Includes_Bezel.xml` L1065: `<control type="group"><!-- BETA 2.5: +-4 deg idle sway on the whole album stack (inside the slide, so it pivots at the album's actual centre); bz_big_go / bz_bi`
  - `xml/Includes_Bezel.xml` L1066: `<animation effect="rotate" start="0" end="-4" center="1440,570" time="5000" tween="sine" easing="inout" condition="String.IsEqual(Window(Home).Property(bz_big_g`
  - `xml/Includes_Bezel.xml` L1077: `then a +-4 deg rotate about its centre (one-shot 0 -> 4 in 5 s at bz_big_go, then an 8.5 s sine in-out pulse 4 <-> -4 at bz_big_pulse, both from bz_flip.py); ev`

### `bz_cast`
- set/clear sites: 0 · read sites: 2
  - `scripts/bz_flip.py` L164: `def _bz_cast(t0):`
  - `scripts/bz_flip.py` L219: `try: _bz_cast(t0)   # 5.33.170 BUG-021: stub cast opacity from this same sway clock`

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

### `bz_flipping`
- set/clear sites: 5 · read sites: 14
  - `scripts/bz_flip.py` L195: `home.setProperty('bz_flipping', 'true'); home.setProperty('bz_sway_hold', 'true')`
  - `scripts/bz_flip.py` L199: `if not sway.get('busy'): home.clearProperty('bz_flipping')`
  - `scripts/bz_flip.py` L1564: `home.setProperty('bz_flipping', 'true')    # v0.1.23: glares fade out (150 ms) before the sway is held`
  - `xml/Custom_1112_NowPlaying.xml` L33: `<visible>String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_f`
  - `xml/Includes_Bezel.xml` L1131: `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="!String.IsEmpty(Window(Home).Property(bz_back)) | !String.IsEmpty`
  - `xml/Includes_Bezel.xml` L1141: `<animation effect="fade" start="100" end="0" time="300" tween="sine" easing="inout" condition="!String.IsEmpty(Window(Home).Property(bz_back)) | !String.IsEmpty`

### `bz_hf_b`
- set/clear sites: 1 · read sites: 5
  - `scripts/bz_flip.py` L1492: `home.setProperty('bz_hf_a', cv[idx]); home.setProperty('bz_hf_b', cv[nxt])`
  - `xml/Includes_Bezel.xml` L1094: `bz_flip.py idle_hinge(): bz_hf_a = shown cover, bz_hf_b = next, bz_hf_ph 1 = right half of A swings 0 -> -90 (2200 ms sine in, 5.33.245 slow fold), 2 = left hal`
  - `xml/Includes_Bezel.xml` L1101: `<control type="image"><left>1440</left><top>220</top><width>300</width><height>600</height><aspectratio align="right">scale</aspectratio><fadetime>0</fadetime><`
  - `xml/Includes_Bezel.xml` L1107: `<control type="image"><left>1140</left><top>220</top><width>300</width><height>600</height><aspectratio align="left">scale</aspectratio><fadetime>0</fadetime><t`

### `bz_idlerock`
- set/clear sites: 0 · read sites: 5
  - `xml/Includes_Tuner.xml` L418: `<variable name="BzATVal_idlerock"><value condition="Skin.HasSetting(bz_idlerock)">ON</value><value>OFF</value></variable><!-- 5.33.231 HINGEFLIP -->`
  - `xml/Includes_Tuner.xml` L1415: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),idlerock)">Skin.Reset(bz_idlerock)</onleft><onright condition="String.IsEqual(Container(`
  - `xml/Includes_Tuner.xml` L1415: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),idlerock)">Skin.Reset(bz_idlerock)</onleft><onright condition="String.IsEqual(Container(`

### `bz_ppulse`
- set/clear sites: 1 · read sites: 23
  - `scripts/bz_flip.py` L1600: `for k in ('bz_back', 'bz_backanim', 'bz_back_pick', 'bz_albumid', 'bz_pswayon', 'bz_ppulse', 'bz_ppulse2', 'bz_pready', 'bz_vreq', 'bz_sway_pulse2', 'bz_castL',`
  - `xml/Includes_Bezel.xml` L563: `Sway (2.0a3.3): one continuous sway like the album art (bz_pswayon then bz_ppulse, bz_flip.py), not reset by a new title; no zoom.`
  - `xml/Includes_Bezel.xml` L2537: `Sway (2.0a3.3): continuous, same as the album art (bz_pswayon, bz_ppulse); no zoom. A new title shows a blurred placeholder until the list has stopped for 2 s (`
  - `xml/Includes_Bezel.xml` L2564: `(bz_ppulse, -13 .. +13, 20 s period) and a small cross wobble (rotate x, a quarter cycle later: bz_ppulse2) keeps it moving through the turns.`

### `bz_ppulse2`
- set/clear sites: 1 · read sites: 5
  - `scripts/bz_flip.py` L1600: `for k in ('bz_back', 'bz_backanim', 'bz_back_pick', 'bz_albumid', 'bz_pswayon', 'bz_ppulse', 'bz_ppulse2', 'bz_pready', 'bz_vreq', 'bz_sway_pulse2', 'bz_castL',`
  - `xml/Includes_Bezel.xml` L2564: `(bz_ppulse, -13 .. +13, 20 s period) and a small cross wobble (rotate x, a quarter cycle later: bz_ppulse2) keeps it moving through the turns.`
  - `scripts/bz_flip.py` L358: `# into the sway over 5 s), bz_ppulse takes over the swing, bz_ppulse2 adds the cross wobble 5 s later.`
  - `scripts/bz_flip.py` L384: `# t4815 run-forever poster sway (Music sway_clock style): once armed, bz_pswayon/bz_ppulse/bz_ppulse2`

### `bz_pready`
- set/clear sites: 4 · read sites: 9
  - `scripts/bz_flip.py` L393: `home.setProperty('bz_pready', 'true')`
  - `scripts/bz_flip.py` L401: `if home.getProperty('bz_pready'): home.clearProperty('bz_pready')`
  - `scripts/bz_flip.py` L401: `if home.getProperty('bz_pready'): home.clearProperty('bz_pready')`
  - `xml/Includes_Bezel.xml` L2537: `Sway (2.0a3.3): continuous, same as the album art (bz_pswayon, bz_ppulse); no zoom. A new title shows a blurred placeholder until the list has stopped for 2 s (`
  - `xml/Includes_Bezel.xml` L2559: `<control type="image"><left>990</left><top>120</top><width>600</width><height>900</height><texture>bezel/poster_blur.png</texture><!-- 3.5.1: only while the lis`
  - `xml/Includes_Bezel.xml` L2560: `<control type="image"><left>990</left><top>120</top><width>600</width><height>900</height><texture border="6">bezel/frame.png</texture><visible>!String.IsEmpty(`

### `bz_pswayon`
- set/clear sites: 1 · read sites: 16
  - `scripts/bz_flip.py` L1600: `for k in ('bz_back', 'bz_backanim', 'bz_back_pick', 'bz_albumid', 'bz_pswayon', 'bz_ppulse', 'bz_ppulse2', 'bz_pready', 'bz_vreq', 'bz_sway_pulse2', 'bz_castL',`
  - `xml/Includes_Bezel.xml` L563: `Sway (2.0a3.3): one continuous sway like the album art (bz_pswayon then bz_ppulse, bz_flip.py), not reset by a new title; no zoom.`
  - `xml/Includes_Bezel.xml` L2537: `Sway (2.0a3.3): continuous, same as the album art (bz_pswayon, bz_ppulse); no zoom. A new title shows a blurred placeholder until the list has stopped for 2 s (`
  - `xml/Includes_Bezel.xml` L2563: `<!-- 2.0a3.4: the poster holds still for 2 s after it fades in, then eases into the sway (bz_pswayon, 13 deg, 5 s), the swing takes over`

### `bz_sway_go`
- set/clear sites: 5 · read sites: 28
  - `scripts/bz_flip.py` L203: `if go and not home.getProperty('bz_sway_go'): home.setProperty('bz_sway_go', 'true')`
  - `scripts/bz_flip.py` L203: `if go and not home.getProperty('bz_sway_go'): home.setProperty('bz_sway_go', 'true')`
  - `scripts/bz_flip.py` L204: `elif not go and home.getProperty('bz_sway_go'): home.clearProperty('bz_sway_go')`
  - `xml/Includes_Bezel.xml` L1130: `<animation effect="fade" start="100" end="0" time="200" tween="sine" easing="inout" reversible="false" condition="![String.IsEqual(Window(Home).Property(bz_audi`
  - `xml/Includes_Bezel.xml` L1132: `<animation type="Conditional" condition="String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_sway_hold)) + Stri`
  - `xml/Includes_Bezel.xml` L1140: `<animation effect="fade" start="100" end="0" time="200" tween="sine" easing="inout" reversible="false" condition="![String.IsEqual(Window(Home).Property(bz_audi`

### `bz_sway_hold`
- set/clear sites: 5 · read sites: 31
  - `scripts/bz_flip.py` L195: `home.setProperty('bz_flipping', 'true'); home.setProperty('bz_sway_hold', 'true')`
  - `scripts/bz_flip.py` L197: `home.clearProperty('bz_sway_hold'); sway['t0'] = time.time()`
  - `scripts/bz_flip.py` L1568: `home.setProperty('bz_sway_hold', 'true')`
  - `xml/Includes_Bezel.xml` L1130: `<animation effect="fade" start="100" end="0" time="200" tween="sine" easing="inout" reversible="false" condition="![String.IsEqual(Window(Home).Property(bz_audi`
  - `xml/Includes_Bezel.xml` L1132: `<animation type="Conditional" condition="String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_sway_hold)) + Stri`
  - `xml/Includes_Bezel.xml` L1140: `<animation effect="fade" start="100" end="0" time="200" tween="sine" easing="inout" reversible="false" condition="![String.IsEqual(Window(Home).Property(bz_audi`

### `bz_sway_pulse`
- set/clear sites: 5 · read sites: 15
  - `scripts/bz_flip.py` L206: `if on and not home.getProperty('bz_sway_pulse'): home.setProperty('bz_sway_pulse', 'true')`
  - `scripts/bz_flip.py` L206: `if on and not home.getProperty('bz_sway_pulse'): home.setProperty('bz_sway_pulse', 'true')`
  - `scripts/bz_flip.py` L207: `elif not on and home.getProperty('bz_sway_pulse'): home.clearProperty('bz_sway_pulse')`
  - `xml/Includes_Bezel.xml` L1152: `<animation effect="fade" start="100" end="0" time="200" tween="sine" easing="inout" reversible="false" condition="![String.IsEqual(Window(Home).Property(bz_audi`
  - `xml/Includes_Bezel.xml` L1154: `<animation type="Conditional" condition="String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_sway_hold)) + Stri`
  - `xml/Includes_Bezel.xml` L1155: `<animation type="Conditional" condition="String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_sway_hold)) + !Str`

### `bz_sway_pulse2`
- set/clear sites: 5 · read sites: 0
  - `scripts/bz_flip.py` L217: `if on2 and not home.getProperty('bz_sway_pulse2'): home.setProperty('bz_sway_pulse2', 'true')`
  - `scripts/bz_flip.py` L217: `if on2 and not home.getProperty('bz_sway_pulse2'): home.setProperty('bz_sway_pulse2', 'true')`
  - `scripts/bz_flip.py` L218: `elif not on2 and home.getProperty('bz_sway_pulse2'): home.clearProperty('bz_sway_pulse2')`

### `bz_sway_restart`
- set/clear sites: 4 · read sites: 5
  - `xml/MyPlaylist.xml` L10: `<onload>SetProperty(bz_sway_restart,true,home)</onload>`
  - `xml/MusicVisualisation.xml` L15: `<onload>SetProperty(bz_sway_restart,true,home)</onload>`
  - `xml/MyMusicNav.xml` L18: `<onload>SetProperty(bz_sway_restart,true,home)</onload>`
  - `xml/Custom_1121_MusicFanartFS.xml` L19: `<!-- no bz_sway_restart: sway must stay unbroken (Music never remounts) -->`
  - `xml/Includes_Tuner.xml` L2075: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),swayshort)">Skin.Reset(bz_swayright)</onleft><onleft condition="String.IsEqual(Container`
  - `xml/Includes_Tuner.xml` L2075: `<onleft condition="String.IsEqual(Container(6970).ListItem.Property(id),swayshort)">Skin.Reset(bz_swayright)</onleft><onleft condition="String.IsEqual(Container`

### `bz_sway_t0`
- set/clear sites: 2 · read sites: 0
  - `scripts/bz_flip.py` L201: `if home.getProperty('bz_sway_t0') != ('%.3f' % t0 if t0 is not None else ''): home.setProperty('bz_sway_t0', '%.3f' % t0 if t0 is not None else '')   # 3.5.3: f`
  - `scripts/bz_flip.py` L201: `if home.getProperty('bz_sway_t0') != ('%.3f' % t0 if t0 is not None else ''): home.setProperty('bz_sway_t0', '%.3f' % t0 if t0 is not None else '')   # 3.5.3: f`

### `bz_swayright`
- set/clear sites: 0 · read sites: 32
  - `xml/Includes_Bezel.xml` L1125: `<!-- BETA 2.2 B: Short sway (bz_swayright) cast shadow on the colour block (mockup castshadow/cast_short_v2): clipped to the block (x 570-960, y 120-1020) by a `
  - `xml/Includes_Bezel.xml` L1128: `<visible>Player.HasAudio + Skin.HasSetting(bz_swayright) + String.IsEmpty(Window(Home).Property(bz_back))</visible>`
  - `xml/Includes_Bezel.xml` L1132: `<animation type="Conditional" condition="String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_sway_hold)) + Stri`

