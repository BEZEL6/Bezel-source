# Sway animations

**Object:** the shared sway clock and everything that moves on it: big album sway, poster sway, album / poster glare, cast shadows, stub (side) casts · Kodi: `bz_flip.py` `sway_clock` + `poster_clock`, Home `bz_sway_*` / `bz_big_*` / `bz_p*`, XML Conditional pulses in `BezelMusicPlayingArt`, `BezelAlbumCast`, `BezelVPLPoster`, `BezelFSPlayNext`
**Where:** big album (every screen that shows it), Movies / TV poster, side albums in album views
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none (Rob rule: one continuous sway, never restarted by play / stop)

## Simple
The big album and the Movies / TV poster slowly turn left and right in 3D, like a card hanging on a thread. It starts a few seconds after Bezel starts and never stops or jumps: not when music starts or stops, not when you change section, not when you open fullscreen. A soft glare slides over the art as it tips, a shadow beside it grows and fades with the tip, and the soft shadows beside the side albums breathe in time. Album and poster move to the same beat.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Still | app start (first 2.4 s); after a sway re-anchor | 2.4 s | art flat |
| Lead-in | 2.4 s after the clock start | 5 s later | art eases from flat to −13° |
| Swinging | 7.4 s after the clock start | never (until Bezel closes) | endless swing −13° ↔ +13° |
| Short sway (Tuner option) | Tuner Short sway on | off | faster ±30° swing |
| Hidden-frozen | the art's screen is covered (Tuner) | uncovered | album and cast freeze together and resume together |

### Timeline
One clock, `t = 0` at app start (the moment the art system starts).
| t (s) | What | Duration | Curve |
|---|---|---|---|
| 0 – 2.4 | still, flat | 2.4 | — |
| 2.4 | lead-in: rotate about the vertical axis 0° → −13° | 5.0 | sine in-out |
| 7.4 | swing cycle begins (period 24.5 s): | | |
| +0 – 2 | hold at −13° | 2.0 | — |
| +2 – 12 | −13° → +13° | 10.0 | sine in-out |
| +12 – 12.5 | hold at +13° | 0.5 | — |
| +12.5 – 22.5 | +13° → −13° | 10.0 | sine in-out |
| +22.5 – 24.5 | hold at −13° | 2.0 | — |
- Pause at the −13° end = 4 s (Tuner Sway pause, default 4 s; it sets both 2 s holds).
- Short sway: 0 → −30° in 5.5 s, then a continuous 11 s cycle (5.5 s each way), no holds.
- **Poster**: same angles and period, pulse onsets placed on the album's grid (`t = 7.4 + k · 24.5`), so album and poster are always in step. Poster gates: lead-in 4 s after it first shows a real item (0.25 s quiet, not scrolling), swing 9 s, all snapped to the grid.
- **Glare** (album): visible during roughly the last quarter of each swing toward an end: fades 100 → 0 over 3.45 s starting 2 s into the cycle, and 0 → 100 over 3.45 s starting 8.55 s in; first appearance 0 → 100 over 2.7 s after 4.7 s. Idle and playing use one glare on the same 12.25 s half-cycle.
- **Cast shadow** (album, on the strip side): grows (horizontal scale 0 → 100 %) and fades in with the lead-in (5.5 s), then on each cycle shrinks / fades 100 → 0 over 3.5 s from 2 s, regrowing on the reverse.
- **Stub casts** (side albums): opacity follows the same clock in 5 % steps; strongest when the album tips toward that side.

### Interruptions
- Music starts / stops: **no change** to angle or phase (the idle and playing art share one clock; the playing art crossfades in at the same angle).
- Track change / album change: cover crossfades in place; the swing goes on.
- Section change, MM open / close, fullscreen open / close: no change.
- Sway re-anchor (only: Kodi FS window open, the Playlist window open, Tuner Short-sway toggle): art is held flat 0.25 s, the clock restarts, the still / lead-in plays again. Album and poster re-anchor together.
- Art covered by the Tuner: album and its cast freeze and resume together (never one without the other).

### Continuity
- One clock for album, poster, glare, cast, stub casts and lit dust. Nothing may run on a clock of its own.
- Never visibility-toggle anything between the sway and its glare / dust: hiding freezes the children and they drift out of phase. Use opacity.
- The swing never "snaps": every change of state starts from the current angle.

### Layering
Cast shadow (behind, on the strip) < art < glare < lit dust (see [dust](dust.md)) < bars / chrome.

### Geometry
| Piece | Value |
|---|---|
| Album rotation axis | vertical line x 1440 (album centre), camera ≈ 1440, 520 |
| Poster rotation axis | x 1290 |
| Album cast | anchored at the strip edge (x ≈ 1050), scale origin 1050, 520 |
| Stub cast texture | 270 × 540 per side |

### Art
- Glare: one 600 × 600 soft mask over the album (no split halves).
- Cast: soft gradient shadow; stub casts only beside a real cover.

### Input
None; Tuner rows: Sway pause, Short sway, cast / glare style and opacity.

### Speed targets
Clock resolution 50 ms; no visible step in the swing.

### Never
- No restart on song start / play / stop (452 "it should be unbroken animation"; 453 "use only 1 continuous unbroken sway anim … no reset on play"; 415 SWAYCONT).
- No 2D rock (408 "disable album rock, I just want sway").
- No glare out of sequence with the sway (448 IDLESEQ, 381 GLARESYNC, 421 IDLEGLARE).
- No cast that only shows while music plays (468 "it should be active all times"); no static cast (468 "just the default grow and fade").
- No cast drifting out of phase with the album (318 CASTSYNC, 440, 441, 445).
- No restart when the MM moves between Music and Movies / TV (314).

### Acceptance checks
1. Cold start, no music: after ~2.4 s the album and poster ease into the swing; both reach −13° together.
2. Start a song mid-swing: angle continues, no flat reset.
3. Watch for a minute: glare brightens near each end; cast grows and shrinks with the tip; side stubs breathe.
4. Movies ↔ Music via the MM: album and poster stay in step.
5. Open the Tuner and close it: album and cast resume in step.

## Kodi implementation (sandbox)

### How it works
- **Clock (Intent).** `bz_flip.py sway_clock` (50 ms poll). `sway['bt0']` is set on the first tick after Bezel starts and never cleared by music; `sway['t0']` adopts it while playing (415 SWAYCONT). Effective `t0 = t0 or bt0`, published as `bz_sway_t0`.
- **Phase flags** (only while `bz_sway_hold` empty): `u ≥ 2.4` → `bz_sway_go`; `u ≥ 7.4` → `bz_sway_pulse`; `u ≥ 12.4` → `bz_sway_pulse2` (unused gate); idle-tree aliases `bz_big_go` / `bz_big_pulse`. Since 471 these are written and read through a 1 s owner shadow (`_sws` / `_swg`; 472 SHADOWHEAL re-reads Kodi every second).
- **XML pulses.** Conditionals with `pulse="true"`, `reversible="false"`: lead-in rotatey 0 → −13 (5000, centre 1440); pulse: rotatey hold 0 → 0 12250 + −13 → 13 10000 delay 2000. Kodi `pulse` plays forward then reverse, so the cycle is 24.5 s. Short sway (`Skin.HasSetting(bz_swayright)`): rotatey 0 → −30 5500.
- **Restart (`bz_sway_restart`).** From MusicVisualisation onload, MyPlaylist onload, Tuner Short-sway toggle only: `bz_flipping` + `bz_sway_hold`, wait 0.25 s, clear hold, `t0 = bt0 = now`, wait 0.3 s, clear `bz_flipping`.
- **Poster.** `poster_clock` arms at thread start (`sw = [_art_sw_anchor(now)]`); `_art_epoch()` = album `t0`, else `bt0` (464 SWAYEPOCH); `_art_sw_anchor` snaps onsets to `t0 + 7.4 + k · 24.5`. Flags `bz_pswayon` (+4) → `bz_ppulse` (+9) → `bz_ppulse2` (+14). `bz_pready` after 0.25 s quiet. Drawn only in 1122 layer 6401 (see [artwork-group](artwork-group.md)).
- **Album cast.** `BezelAlbumCast` in 1122, outside the album copies (CASTPIN); lead-in zoom/fade 5500 (centre 1050, 520) and per-cycle zoom/fade 3500 delay 2000; gated `!bz_sway_hold + bz_sway_go` (no music gate since 468); the same `!Player.HasAudio | !bz_navtune` gate as the album's ancestor (318).
- **Stub casts.** `_bz_cast(t0)` in sway_clock computes left / right opacity (5 % steps, Tuner `bz_at_fsvizop` level) → Home `bz_castL` / `bz_castR`; XML holds each step as a 0 ms Conditional fade.
- **Hold length.** `_cast_D` reads the live 12250 hold from the XML (`D = (N − 10250) / 1000` = 2 s; `T = D + 10.25` = 12.25 s) so the Python cast math follows Tuner changes.

### Wiring
| Constant | Value |
|---|---|
| Clock poll | 0.05 s |
| Still → go / pulse / pulse2 | 2.4 / 7.4 / 12.4 s |
| Lead-in | 5000 ms, 0 → −13° |
| Pulse | hold 12250 + swing 10000 delay 2000, ±13°, cycle 24.5 s (`ART_CYCLE`) |
| Short sway | ±30°, 5500 ms half, 11 s cycle |
| Poster flags | 4 / 9 / 14 s; arm quiet 0.25 s |
| Restart | hold 0.25 s, re-anchor + 0.3 s |
| Axes | album 1440, poster 1290 |
| Home | `bz_sway_t0`, `bz_sway_hold`, `bz_sway_go`, `bz_sway_pulse`, `bz_sway_pulse2`, `bz_big_go`, `bz_big_pulse`, `bz_pswayon`, `bz_ppulse`, `bz_ppulse2`, `bz_pready`, `bz_art_t0`, `bz_castL`, `bz_castR`, `bz_sway_restart`, `bz_flipping` |
| Tuner | `bz_at_swaypause` (default 4 s), `bz_swayright`, `bz_at_fsvizop`, album / poster shadow and glare rows |

### Kodi workarounds (do not port)
- Python setting Home flags that XML Conditionals listen to: Kodi XML has no clock. A port drives every sway-family animation from one timeline value (`t`) per frame.
- The 12250 ms "hold" rotatey 0 → 0: Kodi's way of padding a pulse cycle.
- Two art trees (idle and playing) swinging in lockstep with one hidden: Kodi can't swap a texture inside a running animation without a remount risk.
- `bz_sway_restart` on the Kodi FS window: the window switch tears down timing.
- Owner shadows (`_swg` / `_sws`): Kodi property reads are expensive.

## Related
[big-album](big-album.md) · [artwork-group](artwork-group.md) · [dust](dust.md) · [play-next](play-next.md) · [idle-big-album-fold](idle-big-album-fold.md) · [leaf-flip](leaf-flip.md) · [skin-settings-tuner](skin-settings-tuner.md)
