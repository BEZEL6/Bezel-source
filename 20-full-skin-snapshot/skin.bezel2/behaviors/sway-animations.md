# Sway animations — shared clock, album, poster, stub cast

**Object:** Shared sway clock + album / poster rotatey + stub cast opacity  
**Where:** Music big album (Dialogue FS / Play Next / viz) · Movies/TV poster (`BezelVPLPoster`) · stub side casts (`pn_cast.png`)  
**Last updated:** 2026-10-31 · 5.33.194 (re-verified vs live .194)  
**Status:** draft — matches live 5.33.194 (IDs/files re-verified Oct 31); not Rob-approved, not re-smoked  
**Skin:** skin.bezel2 (Estuary fork)

> Per-object behavior file (same family as `mm-list.md`). Documents **current live math and settings**. Tuner can patch some XML times; clock reads `D` from live XML.

---

## How it works (plain English)

Sway is the slow left–right tip of the big Music album and the Movies/TV poster. It is not a one-shot animation Kodi runs and forgets. A small Python script keeps a shared **clock**, and the skin XML listens to flags that clock turns on. Stub side-cast shadows (the soft dark fall beside the album) also read that same clock so they brighten and fade in step with the tip.

**The shared clock (`sway_clock` in `bz_flip.py`).**  
While the skin script is running it wakes every twentieth of a second. It remembers one start time (`t0`, also stored as Home property `bz_sway_t0`). Everything else is “how long since t0?” From that age it sets a few Home properties that the XML watches:

- still / waiting → no swing yet  
- `bz_sway_go` → lead-in: ease from flat into the first tipped angle  
- `bz_sway_pulse` → looping swing between the two tipped extremes  
- `bz_sway_pulse2` → later gate (kept for a cross-wobble that album no longer uses)

Movies/TV use a **separate poster clock** (`poster_clock`) with the same idea: `bz_pswayon` then `bz_ppulse` / `bz_ppulse2`. Title changes do **not** restart the poster sway.

**Hold and restart.**  
When art must remount cleanly (window reload, etc.), the script sets `bz_sway_hold`, briefly freezes the swing, clears the hold, resets `t0`, and lets the Conditional animations start again from flat. While hold is set, phase flags stay off so XML does not keep swinging on a stale timeline. `bz_sway_restart` is the explicit “start over from flat” path.

**What XML does.**  
Album and poster groups use Kodi **Conditional** `rotatey` effects gated on those flags (sine in-out). Lead-in is a one-way tip; pulse uses `pulse="true"` so Kodi reverses the whole effect set and the art rocks forever. Short sway (Tuner) is a simpler wider tip without the long pulse cycle. Cast textures are separate images whose **opacity** the script publishes as `bz_castL` / `bz_castR` (stepped); the XML only maps those numbers to fades — casts do **not** own their own timers (BUG-021).

**Tuner knobs.**  
Some times and lengths can be patched from Tuner; the script re-reads hold duration \(D\) from the live album pulse XML so cast math stays locked to whatever swing the skin is using. Overall cast strength follows Viz opacity.

**Big picture.**  
One clock → phase flags → Conditional rotatey on art + script-driven cast opacity. Restart clears hold and re-anchors `t0` so Conditional anims remount from flat. Math and exact numbers are below.

---

## Code map
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
