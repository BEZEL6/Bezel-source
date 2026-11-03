# Sway animations — shared clock, album, poster, stub cast

**Object:** Shared sway clock + album / poster rotatey + stub cast opacity  
**Where:** Music big album (Dialogue FS / Play Next / viz) · Movies/TV poster (`BezelVPLPoster`) · stub side casts (`pn_cast.png`)  
**Last updated:** 2026-11-03 · 5.33.408 NOROCK/SWAYSTART
**Status:** Live. One Python clock drives the album and poster sway flags. The album cast sits outside the sway group (5.33.205) and, since 5.33.299, outside the album slide rails too (include `BezelAlbumCast`). Draft: not Rob-approved, not re-smoked.  
**Skin:** skin.bezel2 (Estuary fork)

> Per-object behavior file (same family as `mm-list.md`). Documents **current live math and settings**. Tuner can patch some XML times; clock reads `D` from live XML.

---

## Overview

Three layers: **Simple** (below), **How it works** (plain English, below), **Wiring** (Code map and every technical section after it, taken from the live tree).

### Simple
- The big album (Music) and the poster (Movies/TV) slowly sway (3D turn left and right). There is no 2D rock any more (5.33.408).
- The soft shadows beside the album get darker and lighter in time with that sway.
- When the screen reloads, the sway starts again from flat instead of jumping.
- A few Tuner sliders change how long it pauses and how fast it moves.

### How it works

Sway is the slow left–right tip of the big Music album and the Movies/TV poster. It is not a one-shot animation Kodi runs and forgets. A small Python script keeps a shared **clock**, and the skin XML listens to flags that clock turns on. Stub side-cast shadows (the soft dark fall beside the album) also read that same clock so they brighten and fade in step with the tip.

**The shared clock (`sway_clock` in `bz_flip.py`).**  
While the skin script is running it wakes every twentieth of a second. It remembers one start time (`t0`, also stored as Home property `bz_sway_t0`). Everything else is “how long since t0?” From that age it sets a few Home properties that the XML watches:

- still / waiting → no swing yet  
- `bz_sway_go` → lead-in: ease from flat into the first tipped angle  
- `bz_sway_pulse` → looping swing between the two tipped extremes  
- `bz_sway_pulse2` → later gate (kept for a cross-wobble that album no longer uses)

**Shared art clock (5.33.391).** Poster and album sway on ONE clock. `poster_clock` still raises `bz_pswayon` (+4 s) → `bz_ppulse` (+9 s) → `bz_ppulse2` (+14 s), but its anchor is no longer "now": `_art_sw_anchor()` places the poster's pulse onset on the album pulse grid (`t0 + 7.4 + k·24.5 s`, 24.5 s = Kodi pulse cycle of the 12250 ms anim). Master epoch = album `t0` while the music latch is on; with no music a free-running epoch (`sway['art0']`, set once) stands in. Published as Home `bz_art_t0`. So across a Music↔Videos crossfade in group 6400 both layers are at the same point of the swing. Title changes do **not** restart the poster sway. Limits: the anchor is taken when the poster arms (entering Videos); if the album clock restarts while the poster is already swinging, the poster keeps its old phase until Videos is left and re-entered. Tuner hold `D` changes the album period only (poster XML stays 12250 ms) — at default D=2.0 they match. Mirror direction is unchanged (album −13→+13, poster +13→−13, same timing).


**Sway only, armed at startup (5.33.408 NOROCK/SWAYSTART, Rob pt2914u).** Album rock is gone; both art layers sway from Home cold start:
- **Poster:** `poster_clock` sets `sw = [_art_sw_anchor(time.time())]` when the thread starts (Home onload runs `bz_flip.py`), before any loop `continue`, on the shared art clock (`bz_art_t0`). `bz_pswayon` (+4 s) → `bz_ppulse` (+9 s) → `bz_ppulse2` (+14 s) then advance in every window. Never disarmed; flags clear only on Bezel leave.
- **Album, no music (idle big album):** `bt0` is set on the first `sway_clock` tick with the latch off, i.e. at startup. `bz_big_go` (+2.5 s) / `bz_big_pulse` (+7.5 s) now drive a **rotatey SWAY** on the idle album stack group (Includes_Bezel ~l.1071, `<camera x="1440" y="570"/>`): lead-in 0→−13° in 5 s, then the same pulse as the playing album (12250 ms, −13↔+13 sine, 2 s still). Gates: `!Window.IsActive(1120) + !Window.IsActive(visualisation)`. The old 2D `rotate` ±4° rock (8.5 s pulse) was removed. `bz_big_go` still also fades the idle glare.
- **Album, music playing:** rotatey sway on `bz_audio_latch` / `bz_sway_go` / `bz_sway_pulse` unchanged.
- Tuner: the **Idle rock** row is removed (`BzATVal_idlerock` left as an unused var reading "OFF (sway only)"; `bz_idlerock` unused). Sway controls stay under ALBUM / POSTER › SWAY.
- Idle album phase is on its own `bt0` (startup / music stop), not snapped to `bz_art_t0`; at cold start they are within a tick of each other.
- Leaf flip (`bz_leafflip`, default OFF) does not gate either sway.

**Hold and restart.**  
When art must remount cleanly (window reload, etc.), the script sets `bz_sway_hold`, briefly freezes the swing, clears the hold, resets `t0`, and lets the Conditional animations start again from flat. While hold is set, phase flags stay off so XML does not keep swinging on a stale timeline. `bz_sway_restart` is the explicit “start over from flat” path.

**What XML does.**  
Album and poster groups use Kodi **Conditional** `rotatey` effects gated on those flags (sine in-out). Lead-in is a one-way tip; pulse uses `pulse="true"` so Kodi reverses the whole effect set and the art rocks forever. Short sway (Tuner) is a simpler wider tip without the long pulse cycle. Cast textures are separate images whose **opacity** the script publishes as `bz_castL` / `bz_castR` (stepped); the XML only maps those numbers to fades — casts do **not** own their own timers (BUG-021).

**Tuner knobs.**  
Some times and lengths can be patched from Tuner; the script re-reads hold duration \(D\) from the live album pulse XML so cast math stays locked to whatever swing the skin is using. Overall cast strength follows Viz opacity.

**Big picture.**  
One clock → phase flags → Conditional rotatey on art + script-driven cast opacity. Restart clears hold and re-anchors `t0` so Conditional anims remount from flat. Math and exact numbers are below.

---

## Code map (Wiring)
| Piece | Location |
|-------|----------|
| Shared clock + cast | `scripts/bz_flip.py` — `_sn`, `_cast_D`, `_bz_cast`, `sway_clock` (~L146–220) |
| Poster phase timer | `scripts/bz_flip.py` — `poster_clock` (~L293–393) |
| Album rotatey / glares / short sway | `xml/Includes_Bezel.xml` ~L1060–1100, glare block ~L1148+ |
| Stub cast images | `Includes_Bezel.xml` — `bezel/pn_cast.png` 270×540 (left flipx, right unflipped) |
| Poster rotatey | `Includes_Bezel.xml` `BezelVPLPoster` ~L2495–2520 |
| Cast opacity consumers | Conditional fades on `bz_castL` / `bz_castR` (5% steps) |

---

## Shared helpers (Python)

### Sine ease (0→1)
\[
\_sn(x)=\frac{1-\cos(\pi\,x)}{2},\quad x\in[0,1]\ \text{(clamped)}
\]

### Hold duration \(D\) from live XML (`_cast_D`)
Finds the album pulse pair:
`rotatey 0→0 time=N` immediately before `rotatey −13→13 … time=10000`.

\[
D=\frac{N-10250}{1000}\ \text{seconds},\quad\text{only if}\ 0\le N-10250\le 5000
\]

**Current live:** \(N=12250\) → **\(D=2.0\) s** (default / cache start = 2.0). Cached on `Includes_Bezel.xml` mtime.

### Half-cycle length
\[
T = D + 10.25\ \text{s}
\]
With \(D=2\): **\(T=12.25\) s**. Full pulse round-trip = \(2T = 24.5\) s (Kodi `pulse="true"` reverses the whole effect set).

---

## Shared sway clock (`sway_clock`)

- Thread while `bz_flip_running == true`; poll **every 0.05 s**.
- Anchor `sway['t0']` → Home `bz_sway_t0` (`%.3f`).
- Each tick: phase props + `_bz_cast(t0)` + longtitle/pingpong.

### Restart (`bz_sway_restart`)
When a music window reloads (and no flip busy, no `bz_backanim`):
1. Set `bz_flipping` + `bz_sway_hold`
2. Wait **0.25 s**
3. Clear hold; `t0 = now`
4. Wait **0.3 s**
5. Clear `bz_flipping` (if still not busy)

Art restarts from flat.

### Music album phase table
Let \(u = now - t0\). Only while `bz_sway_hold` empty:

| \(u\) (s) | Property | Meaning |
|----------:|----------|---------|
| 0 – 2.4 | — | still hold (flat) |
| ≥ 2.4 | `bz_sway_go` | lead-in starts |
| ≥ 7.4 | `bz_sway_pulse` | pulsed swing |
| ≥ 12.4 | `bz_sway_pulse2` | cross wobble gate (quarter cycle after swing; rotatex currently unused on album) |

Timeline: **2.4** still → **5 s** lead-in → pulse from **7.4** (= 2.4 + 5).

### Big album idle clock (`bt0`)
Runs only while **no** music (`bz_audio_latch` empty). Latch set → `bt0 = None`.

| Delay | Property |
|------:|----------|
| +2.5 s | `bz_big_go` |
| +7.5 s | `bz_big_pulse` |

---

## Album sway XML (current settings)

**Center:** x **1440** (camera ~1440,520). Gate: `bz_audio_latch` + empty `bz_sway_hold`.

### Normal sway (not Short)
| Phase | Condition | rotatey | time | tween |
|-------|-----------|---------|-----:|-------|
| Lead-in | `bz_sway_go` + empty pulse | **0 → 13°** | **5000 ms** | sine inout |
| Pulse hold | `bz_sway_pulse` | **0 → 0** (anchor) | **12250 ms** | — |
| Pulse swing | same, delay 2000 | **13 → −13°** | **10000 ms** | sine inout, `pulse=true` |

(Opposite face / shadow counter-rotation uses **0 → −13** lead-in and **−13 → 13** pulse — same \(D\), mirrored.)

### Short sway (`Skin.HasSetting(bz_swayright)`)
| Phase | rotatey | time |
|-------|---------|-----:|
| From go, pulse | **0 → −30°** (main) / **0 → 30°** (mirror face) | **5500 ms** sine inout |

No separate still/pulse props beyond `bz_sway_go`; cast uses the 11 s short formula below.

### Glares (3.5.7 — visible last ~25% of swing toward that end)
Typical (inside 12250 pulse window):
- Fade 100→0: **3450 ms**, delay **2000**
- Counterpart 0→100: **3450 ms**, delay **8550**
- First appearance 0→100: **2700 ms**, delay **4700**
- Right-sway glares: 0→100 **1810 ms**, delay **3690**; held 0 until `bz_sway_go`

---

## Poster sway (Movies / TV) — `poster_clock`

**Center:** x **1290**. Shared by Movies + TV; Music untouched.

### Arming
- Arms once: `bz_pready` after real item + **0.25 s** quiet, not scrolling.
- Phase timer `sw[0] = now` at arm.
- **Title changes never remount** (t4815). Cleared only when Videos is left.

### Phase table (\(e = now - sw0\))
| \(e\) (s) | Property | Meaning |
|----------:|----------|---------|
| ≥ 4 | `bz_pswayon` | lead-in (0.5 delay + 1.5 fade + 2 still ≈ 4) |
| ≥ 9 | `bz_ppulse` | pulsed swing |
| ≥ 14 | `bz_ppulse2` | quarter-cycle gate |

### XML (current)
| Phase | rotatey | time |
|-------|---------|-----:|
| Lead-in (`pswayon`, no pulse) | **0 → −13°** (poster) / **0 → 13°** (cast grow) | **5000 ms** sine inout |
| Pulse | **0→0** **12250** + **−13→13** **10000** delay 2000 | same \(D=2\), \(T=12.25\) |
| Cast on pulse | mirrored **13→−13** + zoom/fade tip | half-swing **5000** |

Period comment in XML: **20 s** class (−13…+13); live pulse math matches album (\(2T\) with \(D\)).

---

## Album colour-strip cast (sway_shadow / BzCastTex_a)

**Geometry (current):** image `left=480`, `top=230`, `width=480`, `height=580` → **right edge x=960** = BezelColourBlock right edge (570+390). Grow/shrink Conditional zooms use **center="960,520"** so fade-in/out stay pinned to the strip edge (no drag toward the album). Was left=485 / center 965 (5px overhang).

## Stub album cast opacity (`_bz_cast`) — 5.33.170 / .171

**Texture:** `bezel/pn_cast.png`, **270×540**  
- Left stub: `left=270`, `flipx=true`  
- Right stub: `left=0`, unflipped  
**Gate:** neighbour `MusicPlayer.offset(∓1).Title` **and** `.Cover` non-empty (no cover → no cast).

Only when `bz_audio_latch=true` and no `bz_sway_hold`; \(u = now - t0\).

### Short sway (`bz_swayright`, \(u \ge 2.4\))
\[
w=(u-2.4)\bmod 11,\quad
q=\_sn\!\left(\frac{\min(w,\,11-w)}{5.5}\right)
\]
\[
L=40+60q,\qquad R=100-85q
\]

### Lead-in (\(2.4 \le u < 7.4\))
\[
q=\_sn\!\left(\frac{u-2.4}{5}\right),\qquad
L=40+60q,\qquad R=100-85q
\]

### Cyclic pulse (\(u \ge 7.4\))
\[
T=D+10.25,\quad
w=(u-7.4)\bmod(2T),\quad
f=\begin{cases}w & w<T\\ 2T-w & \text{else}\end{cases}
\]
\[
L=100-85\cdot\_sn\!\left(\frac{f-D}{5}\right),\qquad
R=15+85\cdot\_sn\!\left(\frac{f-D-5}{5}\right)
\]

**Bright ends:** \(L\) bright at **−13°**, \(R\) bright at **+13°** (5.33.74 levels).

Otherwise (no t0 / not latched / held): \(L=R=\texttt{None}\) → empty property = **100%**.

### Overall level (5.33.171)
Tuner › Fullscreen Music › **Viz opacity** `Skin.String(bz_at_fsvizop)` (same as stub/side albums):

| `bz_at_fsvizop` | Level \(v_b\) |
|----------------:|--------------:|
| empty / **11** (default) | **1.0** (100%) |
| 1…10 | \((v-1)/10\) → 0%…90% |

If \(v_b < 1\): \(L \leftarrow (L\ \text{or}\ 100)\,v_b\) (same for \(R\)).  
Clock = **timing only**; **no** art-brightness sampling.

### Publish
Home `bz_castL` / `bz_castR`:
\[
\text{round to nearest }5,\quad
\text{clamp }\begin{cases}[15,100] & v_b\ge 1\\ [0,100] & v_b<1\end{cases}
\]
Value **100** → property **cleared** (empty means 100). XML maps each 5% step to a static Conditional fade.

### BUG-021 (fixed 5.33.170)
Casts **do not** own Conditional timers. Mid-cycle stub / viz / Play Next load just reads current opacity from this clock — no re-zero.

---

## Current numeric cheat-sheet

| Constant | Value |
|----------|------:|
| Clock poll | 0.05 s |
| Still hold → go | 2.4 s |
| Lead-in duration | 5.0 s |
| Pulse start | 7.4 s |
| Pulse2 start | 12.4 s |
| Angle (normal) | ±13° |
| Angle (short) | ±30° |
| Lead-in XML time | 5000 ms |
| Pulse hold \(N\) | 12250 ms |
| Swing time | 10000 ms |
| Swing delay | 2000 ms |
| \(D = (N-10250)/1000\) | **2.0 s** |
| \(T = D+10.25\) | **12.25 s** |
| Short cycle | 5.5 s half / 11 s full |
| Big idle go / pulse | 2.5 / 7.5 s |
| Poster arm quiet | 0.25 s |
| Poster pswayon / ppulse / ppulse2 | 4 / 9 / 14 s |
| Restart hold / re-anchor | 0.25 / 0.3 s |
| Cast texture | pn_cast.png 270×540 |
| Cast step | 5% |
| Viz opacity default | 11 → 100% |
| Album center x | 1440 |
| Poster center x | 1290 |

---

## Open bugs (cast phase)
| Bug | Status | Note |
|-----|--------|------|
| BUG-021 | FIXED 5.33.170 | Shared clock |
| BUG-009 | open / retest | Wrong sway phase — reverse = swap L/R formulas (or \(f\) offset), not new timers |
| BUG-019 | open | Sequence needs switched |
| BUG-014 | open | Right stub missing cast; casts above overlays/titles |

`bugs.md` BUG-009 still shows a stray “fixed 5.33.152” line that describes BUG-008 poster-hold removal — treat BUG-009 as **open / retest**.

---

## Re-verify vs live 5.33.194 (2026-10-31)
- Every function / property named in this doc still exists in live `bz_flip.py` / XML (`sway_clock`, `poster_clock`, `_bz_cast`, `bz_castL`/`bz_castR`, `bz_sway_restart`, `bz_pswayon`/`bz_ppulse`/`bz_ppulse2`).
- `bz_flip.py`: no sway/cast changes after .182.
- XML changes since .182: **5.33.184** default poster cast = *bloom wide soft haze* (Rob approved; was cast_mp_current; soft/hard via `bz_at_pcsoft` / `bz_at_pcstyle`). **5.33.193** mushide re-latch touched hide gates only (comment-marked "sway untouched").

## Related
`play-next.md` · `dialogue-fs.md` · `fanart-fs.md` · `now-playing.md` · `music-viz-settings.md` · `skin-settings-tuner.md` · `mm-list.md` · `bugs.md` (BUG-009 / 014 / 019 / 021)

---

## Album cast strip-edge pin (5.33.205)

**Bug:** Album cast soft shadow on the colour strip showed a couple of pixels of edge drift at the strip’s right edge (x 960) while sway ran.

**Cause:** Cast lived *inside* the 3D sway `rotatey` group with a child counter-`rotatey`. Nested perspective does not cancel perfectly, so the cast’s right edge wobbles in screen space against the flat strip.

**Fix (code only):** Move album cast (`BzCastTex_a`, left 480 × width 480 → right edge 960) **outside** the flip/sway rotate tree in `BezelMusicPlayingArt`. Keep zoom+fade grow about `960,520`. Remove all cast `rotatey` / counter-`rotatey`. Vis still gated on `Player.HasAudio`, sway mode, and `bz_back`. Poster cast unchanged.

**Smoke:** ReloadSkin (or FULL restart if props sticky). Music playing, watch strip right edge through short and long sway peak — cast edge should stay flush, no crawl.

## Idle (no audio) big album — current (5.33.231)
- Idle album: bz_big_go / bz_big_pulse drive rotatey sway (no rock) from startup (5.33.408).
- Idle hinge flip every 10 s — see music-list.md.

## Idle Big Album fold (current state, 5.33.245)
> Leaf flip is its own behaviour — [leaf-flip.md](leaf-flip.md); it does not use the sway clock (section below is history; locked look = idle-big-album-fold.md).
- Where: big-album group in `xml/Includes_Bezel.xml` (1140,220 600×600, same rect/zoom as the Music sway album). Driver: `scripts/bz_flip.py` `idle_hinge()`.
- When: idle only. That means no audio, Music window open, list 60 focused, not under MM/nav/randpend/back.
- Cycle: an artist row steps through that artist's albums by year and wraps. An album row alternates between the album and the artist face. Any change of focus or playback resets the cycle.
- Fold: phase 1 folds the right half of the current cover onto itself (rotatey 0→-90 about x1440, 2200 ms sine in). Phase 2 unfolds the next cover's left half (90→0, 2200 ms sine out). The next cover's right half is visible underneath the whole time. When the fold ends, A := B, so the cover lines up with no jump. The baked shadows `hf_shd_r` / `hf_shd_l` and the 45% darkening fade with the fold.
- Hold: 10 s between folds.
- Preload: `bz_hf_b` (the next cover) is set as soon as the hold starts and is drawn under A for the whole 10 s. B textures load sync, so nothing is blank mid-fold.
- Rock: removed in 5.33.408; no Tuner row.

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/sway-animations.md) · [state](../state/sway-animations.md) · [motion](../motion/sway-animations.md) · [art](../art/sway-animations.md) · [input](../input/sway-animations.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)


## Album cast — strip binding (5.33.299 CASTPIN, current)
- **Rule (Rob):** the album cast gets its *timing* from big-album sway (`bz_audio_latch` / `bz_sway_go` / `bz_sway_hold` / `bz_sway_pulse` Conditional zoom+fade, 5500 ms short pulse) but *draws only on the fanart-stage colour strip*. Its right edge is bound to the strip edge **x960** in every scenario — no exceptions.
- **Where:** `Includes_Bezel.xml` include `BezelAlbumCast` (fixed screen space, 480×580 at x480,y230, right edge x960). Mounted once in the Music window right before the album rails (6367/6377/6397/6382), and once in `MusicVisualisation.xml` before the PlayNext `-480` mount. No longer inside `BezelMusicPlayingArt`, so rail scroll, the 1121 / Play Next slide and the -480 offset never move it.
- **Tuner:** `acx` (cast X) row removed in 5.33.300 (dead since .299); right edge cannot leave x960. `acy` still slides vertically. `aclen` / `acstyle` zooms are horizontal about `960,520` so the right edge stays pinned; long lengths grow leftward only.
- Still fades out (250 ms) when 1120 / 1121 / visualisation is active; static (`bz_acast_static`) and animated variants unchanged.

## Cast pin + clip + poster zero (5.33.300 CAST300, current)
- **Album clip:** `BezelAlbumCast` body sits in a clip `grouplist` left 570 / width 390 / height 1080 (`usecontrolcoords`), inner group left −570 so child coords stay screen-space. Cast can only draw inside the colour strip x570–960; Soft / Long 170% / Length 125–175% spill is clipped at x570 instead of painting meta/list (Rob t2254u). Zero unchanged: 480/230/480×580, zoom centre 960,520, right edge x960.
- **Poster cast zero:** Movies/TV strip cast (BezelVPLPoster) and Info-block cast — animated + static — now left **480** (was 485), zoom centre **960,570** (was 965,570), width 480 → right edge **x960** = strip edge, same as album. Poster cast is not clipped.
- **Removed:** old BETA 2.2 Short cast grouplist (`cast_shadow_short.png`, `visible=false`) deleted; Tuner `acx` row + its Val/Step/Bar vars + L/R handlers deleted.

## Album change while playing (5.33.301 ALBUM SWAY NEXT SONG FADE)
- Next song from a **different album**: `bz_flip.py` sets `bz_cov_x` (new art, preloaded `LOAD_WAIT`), then `bz_cov_xf` → an overlay image on top of the front face (both faces carry it, inside the sway rotatey tree) fades 0→100 in **900 ms** while sway keeps running — the cover stays tipped.
- After 1.0 s the front face (`bz_cov_<side>`) adopts the new art; 0.4 s later `bz_cov_xf` clears (instant, same art beneath).
- **No** `bz_cov_side` change, **no** `bz_sway_hold`, **no** `bz_flipping` glare dip, **no** sway restart on this path. Full spin parked for next-song.
- Same album: art stays, no fade. Play start: front face takes the cover, no flip. Rock clock and idle leaf untouched.

## 5.33.307 — Fanart FS album viz sway follows the album (Rob)
- In Fanart FS (1121) album viz, the playing album now moves with a real left -480 (the same as MusicVisualisation.xml), not a Conditional slide. The sway camera moves with it, so the album sways centred at 660 and the tip no longer freezes.
- On each FS Slide speed rail, an outer slot holds two inner copies: one normal, and one at left -480 shown when Fanart FS is open with bz_pnoff not 1. The rail ignores a child's left, which is why the outer slot is there. Each copy slides in over the rail's speed (480/380/280/180 ms).


## Big album (5.33.309 P1)
The big album, its sway, next-song fade, cast and compact NP no longer live in this screen. They live in the always-open dialog **1122** — see [big-album.md](big-album.md). This screen only decides where the album sits (Home prop `bz_rail`: `home` / `centre` / `hide`). The old album grouplists 6367/6377/6397/6382 and their focus buttons (6368/6369, 6378/6379, 6398/6399, 6383/6384) are deleted; nothing focuses into an album rail any more.

## 5.33.314 — restart list (current)
`bz_sway_restart` fires only from: MusicVisualisation onload, MyPlaylist onload, Tuner Short-sway toggle. **Not** MyMusicNav (removed 314 — MM Music↔Movies/TV must not reset album sway) and not 1121.

## Album cast sync gate (5.33.318 CASTSYNC, current)
- **Bug (Rob t2398):** big-album colour-strip cast drifted out of phase with the album tip.
- **Cause:** Kodi stops processing (freezes) child animations of a hidden group. The album sway lives under `BezelMusicPlayingArt`'s top group (`!Player.HasAudio | !bz_navtune` — hidden under Tuner), but `BezelAlbumCast` in 1122 had no such gate, so under Tuner the album's Conditional pulse froze while the cast pulse kept running. Before 5.33.314 MyMusicNav's `bz_sway_restart` re-zeroed both and hid the drift; now nothing does.
- **Fix:** `BezelAlbumCast` outer grouplist carries the identical gate. Album and cast now hide/freeze and resume together, same phase. No new timer; still the same `bz_sway_go` / `bz_sway_pulse` Conditional zoom+fade.
- **Rule:** any gate on an album-sway ancestor must also be on `BezelAlbumCast` (and vice versa).


## Global artwork group (5.33.366)
See `artwork-group.md`. Big album + Compact NP now sit in 1122 group 6400 / album layer 6402, opacity-gated by `bz_railvis` (no Visible remount, sway clock unbroken). Poster layer 6401 pre-warms Videos poster and crossfades in during Music↔Movies/TV handoff. MM Warm underlay unchanged.

## 5.33.367 — poster stage
The swaying Movies/TV poster (BezelVPLPoster) now draws only in dialog 1122 layer 6401, fed by the bz_flip list-60 Home mirror (bz_v60_*, bz_vpl_on). Screens keep only the tap target. See `artwork-group.md`.

## 5.33.381 GLARESYNC rule
Glare + lit dust must ride the sway clock: never put a <visible> on any group between the sway group and the glare pulse groups (hidden = children frozen, pulse re-anchors on re-show = phase drift). Gate glare with Conditional fades only. Poster: glare block is a direct child of the 1440,570 camera group inside the BezelVPLPoster sway group, gated by fades on bz_ppulse/bz_pready/bz_vbackanim/bz_mmmushide. Album: glares inside covers, visible only Player.HasAudio/bz_swayright (stable while playing). Timings shared: hold 12250, swing 10000 d2000, glare A 100→0 3450 d2000, B 0→100 3450 d8550.
- MMAUDIO (5.33.397): while the MM is open and audio is playing (no video), `$EXP[bz_mmaudio]` keeps the big album (6402) up on every strip row — Music, Movies, TV, Recent, Favourites, Search, Pictures, Add-ons, Settings, Media Sources, Power. It forces `bz_railvis` true and `bz_artposter` false, so the poster layer 6401 stays down. With no audio, or with MM closed, the existing Music album / A2P poster rules apply. Includes_Bezel.xml.

## MM album fade (5.33.407 MIDLEFADE)
Idle Music big-album A/B dissolve (slots `bz_m_idle_a`/`bz_m_idle_b`, 6402 in Includes_Bezel) runs at `Skin.String(bz_at_midlefade)`: steps 1–7 = 200/250/300/400/500/600/800 ms, **default 400 ms** (empty|4). Tuner › ALBUM / POSTER › **MM album fade** (slider). bz_flip.py promote guard = fade + 50 ms (default 0.45 s). Separate from A2P (`bz_at_a2pfade`) and WARM art crossfade (`bz_at_mmxfade`). Reset art/everything clears it.
