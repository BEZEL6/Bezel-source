# BEZEL Tuner

**Object:** Bezel's own settings screen · Kodi: group `6975` in `Includes_Tuner.xml` (section rail `7001`, rows `6970`, info panel), BEZEL settings list `6968`, `scripts/bz_tune.py` + `bz_tune.json`, `scripts/bz_tune_patch.py`, `scripts/bz_dtap.py` (debounced reload)
**Where:** over the MM (rail on the stage, rows in the strip, info on the right)
**Last updated:** 2026-11-04 · 5.33.474 · **Status:** live (rail layout approved 439) · **Lock:** none

## Simple
The Tuner is where every Bezel look and timing is set. A rail on the left lists the sections (Album / Poster, Poster glare, List, Fanart stage, Warm, Main menu, Music, Dust, Look, Fullscreen music, System, Maps, About, All, Reset); the strip shows that section's rows; the right side shows a picture and description of the focused row. Left / Right change a value at once (a bar and the value text show where you are); presets set many rows together. Changes that need a skin reload are batched and applied 1.2 s after your last change. Back on a row returns to the rail; Back on the rail returns to whoever opened the Tuner (the power menu, or fullscreen music + its controls).

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Rail | open the Tuner | Right / Select → rows; Back → opener | section names (no counts) |
| Rows | Right / Select on the rail | Back / Left on a sub-row → rail | rows of that section, value bars, info panel |
| Applying | a reload-type change | 1.2 s after the last change | skin reloads once; list position kept |
| Closed | Back on the rail | — | power menu (from power) or fullscreen music + controls (from music controls) |

### Timeline
| What | Duration |
|---|---|
| value step | immediate on screen |
| batched reload | 1.2 s after the last change |
| first start after an update with new defaults | one reload (defaults seeded once per version) |

### Interruptions
- Quick Back Back Back: power menu, then the MM; never a random window.
- Re-entering after leaving works every time.

### Continuity
- Leaving the Tuner leaves the MM exactly as it was (strip, dust, art); the Tuner is never drawn behind the power menu.
- Values persist; Reset returns a section to Rob's defaults.

### Layering
MM art + dim < Tuner (rail, rows, info panel) < power menu < dialogs.

### Geometry
| Piece | Value |
|---|---|
| Rail | x 120 (stage), top 200, 450 × 812 |
| Rows | in the strip, top 196, h 812 |
| Info panel | 1040–1800: image box 1040, 120, 760 × 500 (83 % scale); title / value 640, description 710, hints 962 |

### Art
Per-row info image; value bars (4- to 17-step bar images); rows in the strip style.

### Input
| Action | Rail | Rows |
|---|---|---|
| Up / Down | move | move |
| Right / Select | rows | step / run (button, sub, preset) |
| Left | — | step back; on a sub / button row → rail |
| Back | close to opener | rail |

### Speed targets
Value text updates the same frame; reload ≤ a few seconds.

### Never
- No rail counts / localized numbers (462).
- No nav legend (456).
- No Tuner drawn under the power menu; no missing colour strip after exit (465 → 467).
- Re-entry always works (469).
- No fullscreen music shadow rows (473: removed, they broke the transport bar).
- Fanart and colour strip settings live together in FANART STAGE (474), not spread over List / Look.
- No cast "animated" row (468), no MM auto-hide park row (398; the 428 auto-hide row is the current one).

### Acceptance checks
1. Power → TUNER → rail → Right → rows → Right steps a value → bar moves.
2. Back → rail; Back → power menu with the strip; TUNER → back in.
3. Change a Dust value twice quickly → one reload 1.2 s after the last.
4. Music controls → TUNER → Back on the rail → fullscreen music + controls.

## Kodi implementation (sandbox)

### How it works
- **Show:** group 6975 visible `$EXP[bz_navmenu] + bz_navtune`. Opener stamps `bz_tunesrc` (`pwr` from 1118, `fsctrl` from 1115; `bz_navbez` from the BEZEL settings list).
- **Rail 7001** (ids albumposter, posterglare, list, fanartstage, warm20, mainmenu, music, dust, look, fsmusic, system, maps, about, all, reset → `bz_tune.py resetui open`). Right / OK → `SetFocus(6970,0,absolute)`. Back: `bz_tunesrc` ≠ `fsctrl` → `ActivateWindow(1118)` only (1118's onload clears `bz_tunesrc` / `bz_navtune`); `fsctrl` → clear `bz_nav` / `bz_navtune` / `bz_tunesrc` first, then 1121 (`$EXP[bz_m1121ok]`) or viz, then 1115.
- **FANART STAGE (474):** rows fanop, fantype (`Skin.String(bz_at_fantype)`: empty = Crossfade, 2 = Cut; `BzATVal_fantype`, `BzATBar_fantype` with `bar_2_*`), fanart, blockcol, blockop, Reset; `bz_tune_patch._bezel` bakes the section fanart `fadetime` to 0 for Cut, else Fade speed.
- **ABOUT art probe (475, diagnostics only):** five Select-only rows at the top of ABOUT / VERSIONS run `scripts/bz_probe_art.py` modes `read` (read only), `set` (test cover on one album, original art backed up first to `addon_data/skin.bezel2/art_probe_state.json`), `check`, `restore`, `folder` (create + delete a tiny temp file in that album folder). Results merge into `addon_data/skin.bezel2/art_probe.json`. Phase 1 of MANAGE ART (plan: project doc `claude/MEDIA_MANAGER_PLAN.md`); Kodi sandbox only, Bezel's own library replaces it later. No visual change outside the Tuner.
- **Rows 6970:** show items whose `sec` = `Container(7001).ListItem.Property(id)`; `bz_topen_<sub>` bools fold sub-sections; onback → `SetFocus(7001)`.
- **Values:** `Skin.String(bz_at_<id>)` step index (empty = default). onleft / onright carry generated conditional `Skin.SetString` chains + `SetProperty(bz_tune_dirty,1)`. Display `BzATVal_<id>`, `BzATStep_<id>`, `BzATBar_<id>`.
- **Script actions** (`bz_tune.py`): `preset,<sec>,<name|next>`, `reset[,force]`, `resetui`, `seed` (DEF once per `bz_defseed` ver 5.0.20), `fastseed` (471 FAST block once per `bz_fastseed` 5.33.471), `reset,stage` (474: fanart opacity / fade speed / colour strip back to DEF, Fade type to Crossfade), `alldust`, `import` / `export`.
- **Reload:** `bz_dtap.py` loop sees `bz_tune_dirty`, waits 1.2 s, `reload_tuned()` → `bz_tune_patch.patch()` (bakes timings into XML through temp files) → `ReloadSkin()` only if files changed, restoring path and row. The loop also clears a stale `bz_navtune` when `bz_nav` isn't true.
- **Data** (`bz_tune.json`, compact one-line JSON): `P` slider rows `[id, sec, default, steps, labels]`, `V` value tables (e.g. rowscroll ms, cascspeed ms, fanart ms, mmxfade ms), `TOG` toggles, `SEC`, `DEF` (Rob's defaults: `str`, `on`, `off`), `FAST`.

### Wiring (key defaults, DEF 5.0.20 + FAST 5.33.471)
| Row | Default |
|---|---|
| List › Row scroll | 0.7× (271 ms), cubic |
| List › Cascade speed / stagger | 1.4× (286 ms) / 30 ms |
| Fanart stage › Fanart opacity | 30 % (DEF step 4) |
| Fanart stage › Fade type | Crossfade (Cut = instant) |
| Fanart stage › Fade speed | 150 ms |
| Fanart stage › Colour strip / opacity | Red / 60 % |
| Main menu › Open / Close speed | 1.4× (286 / 250 ms) |
| Main menu › MM-open art crossfade | 0.5 s |
| Main menu › Section fade | step 5 (only logged by mm_warm; no visible effect) |
| Main menu › Auto-hide | Off |
| Album › Sway pause | 4 s |
| Album › Leaf flip | Off |
| Album / Poster › Poster ↔ album fade | 400 ms |
| Album / Poster › MM album fade | 400 ms |
| Fullscreen music › Slide speed | Mid-high (280 ms) |
| Double-tap / window | On / 300 ms |
| Dust | see [dust](dust.md) |
| Warm › Startup splash / Album art during music | On / On |

### Kodi workarounds (do not port)
- Bake-and-reload: Kodi can't change animation times at runtime. A port applies values live.
- Generated XML step chains: avoid a script start per keypress.
- `bz_tunesrc` ordering around modal `ActivateWindow`.

## Related
[power-menu](power-menu.md) · [music-controls](music-controls.md) · [dust](dust.md) · [sway-animations](sway-animations.md) · [section-transitions](section-transitions.md) · [touch-group](touch-group.md)
