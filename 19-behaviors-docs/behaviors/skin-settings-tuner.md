# Skin settings / BEZEL Tuner

**Object:** `Includes_Tuner.xml`: group `6975`, Tuner list `6970` (left 570), BEZEL settings list `6968` · `SkinSettings.xml` · `scripts/bz_tune.py` + `bz_tune.json` · `scripts/bz_dtap.py` (`bz_tune_dirty` reload)
**Where:** Inside the MM void. Opened from Power › TUNER, from FS controls, or from the MM BEZEL settings list
**Last updated:** 2026-10-31
**Status:** Live in 5.33.207. Left/Right change a row's value straight away. Changes that need a skin reload are batched 1.2 s after the last change. Back returns to whoever opened the Tuner. There's **no touch master row** in the live tree. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## Open / close

### Simple
The Tuner is BEZEL's own settings list, drawn on the main menu's dark side. Open it from Power › TUNER (or from the music controls or BEZEL settings). Back takes you back to wherever you came from.

### How it works
- The Tuner is a group inside the MM include, shown only while the MM is open and `bz_navtune` is set.
- The opener records itself in `bz_tunesrc`.
- Back reads `bz_tunesrc` and returns to that opener:
  - `pwr` → Power menu 1118.
  - `fsctrl` → close the MM, then visualisation + music controls 1115.
  - Opened from the BEZEL settings list (`bz_navbez`) → back to list 6968.
  - Otherwise → the MM strip 6996.
- Back always clears `bz_navtune` and `bz_tunesrc`, so the group hides immediately (BUG-007).

### Wiring
| Item | Value |
|---|---|
| Group 6975 | visible `$EXP[bz_navmenu]` + `bz_navtune` |
| List 6970 | left 570 · onup/ondown noop (native list move) |
| 6970 onback | `ClearProperty(bz_navtune)` · `pwr` → `ActivateWindow(1118)` · `fsctrl` → `ClearProperty(bz_nav)` + `ActivateWindow(visualisation)` + `ActivateWindow(1115)` · `bz_navbez` → 6968 · else 6996 · `ClearProperty(bz_tunesrc)` |
| List 6968 | BEZEL settings list, left 570 / top 140 / 390×870 |

---

## Changing values

### Simple
- Highlight a row and press Left or Right to step its value. A bar and the value text show where you are.
- On/Off rows flip.
- Section presets (Default, Subtle, Mid, High, Extreme) set many rows at once.

### How it works
- **Storage.** Every value lives in a Skin.String `bz_at_<id>` as a step index. Empty means the row's default (for example, `mmdbright` empty ≡ 6 = 60 %).
- **XML step chains.** 6970's onleft/onright carry generated per-row conditional `Skin.SetString` chains, so a step needs no Python start-up. Each step also sets `bz_tune_dirty`.
- **Display.** Rows show `BzATVal_<id>` (value text), `BzATStep_<id>` and `BzATBar_<id>` (bar image) variables.
- **Script actions.** `bz_tune.py` handles the bigger actions:
  - `preset,<sec>,<name|next>` (default / subtle / mid / high / extreme)
  - `reset[,force]`, `resetui`
  - `seed`: writes defaults once per DEF version into `bz_defseed`
  - `alldust`
  - `import` / `export`
- **Reload.** `bz_dtap.py`'s loop sees `bz_tune_dirty` and waits 1.2 s after the last change, then calls `reload_tuned()`. That runs `bz_tune_patch`, and does a `ReloadSkin()` only if the patched files actually changed, restoring the music/video path and list position afterwards. Values read live by XML apply instantly; values patched into XML wait for that one batched reload.
- **Loop tidy-up.** The same loop clears a stale `bz_navtune` whenever `bz_nav` isn't true (every 5 ticks).

### Wiring
| Item | Value |
|---|---|
| `bz_tune.json` | P: 89 slider rows (dust 43, list 9, ashadow 9, menu 6, pshadow 5, look 4, art / aglare / pglare 3, block 2, music 2) · TOG: 20 · SEC list |
| XML item kinds | slider 97 · toggle 48 · btn 32 · sub 20 · head 13 · preset 5 · pill 1 |
| Step | 6970 onleft/onright → conditional `Skin.SetString(bz_at_<id>,n)` chains + `SetProperty(bz_tune_dirty,…)` |
| Reload | `bz_dtap.py` → 1.2 s debounce → `reload_tuned()` (bz_tune_patch, `ReloadSkin` if changed) |
| Info art | every row has `property name="info"` (`media/bezel/info/`) |

---

## Touch-related rows

### Simple
Two rows control the remote double-tap: on/off, and how quick the double-tap has to be. There's no general "touch on/off" switch.

### How it works / Wiring
- `dtap` → `bz_dtap_off` (`BzATVal_dtap` ON/OFF).
- `dtapwin` → `bz_at_dtapwin`, 15 steps of 150–600 ms (`STEPS` in bz_dtap.py, default 0.3 s).
- No touch master row or setting was found in `Includes_Tuner.xml` or the scripts. See touch-group.md.

---

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move |
| Left / Right | Step value / toggle (sets `bz_tune_dirty`) |
| Select | Row action (button / sub / preset) |
| Back | Return to opener (`bz_tunesrc`) |

## Touch
None specified. Touch master isn't present.

## Related
power-menu.md · touch-group.md · dust.md · mm-warm.md · sway-animations.md

---

# Row reference (live)

## DUST (full row list → dust.md)
Size rows `d20fsize` Distant / `d20msize` Mid / `d20ssize` Ambient spin / `mmdsize` Menu dust: **90% / 100% / 125%** (defaults 90 / 90 / 100 / 90 %). Dust presets (subtle/mid/…) in `bz_tune.py` set these with density/brightness/fade/slide.

## DUST opacity sliders (5.33.147)
All dust opacity rows step 10% → 100% in 10% increments (stored index 1–10; empty = default):
- Empty-string defaults (from BzATVal_*): Distant `d20fbri` 70%, Mid `d20mbri` 70%, Ambient spin `d20sbri` 50%, Poster lit `pd3lit` 60%, Album lit `d3lit` 60%, Menu dust `mmdbright` 60%. (Row desc text for Distant/Mid/Spin/Poster says other defaults; desc text was not changed.)
- Menu dust (`bz_at_mmdbright` → `BzMMDustA`) was 5 steps 20–100%; now 10 steps 10–100%, alpha = round(255×n/10), default 60% (index 6 / empty). Saved values 1–5 from older builds now read as 10–50%.
- LEFT/RIGHT clamp at 10% / 100%; no 0% option.


## 5.33.163 FULLSCREEN MUSIC › VIZ › Slide speed
id `fsslide`, string `bz_at_fsslide` 1–4 (empty=3). Left/Right in 6970 nav block before fsvizop. Reset with fschrome reset.

## Other live sections (5.33.194)
- WARM 2.0.1 section (`warmmusicposters` On/Off → `bz_mmmushide`; `abfade` slider present but no effect since 5.33.192 — A/B fixed 1500 ms). See mm-warm.md.
- LOOK: Global dim `gdim` (values listed 90%→30%; bz_tune.json default index 7 = last entry — **unverified** vs Rob standard "default 60%"; flagged), fanart `fanop`, logo colour/opacity, colour block.
- MENU: `mmxfade` 0–5 s crossfade (MM-open only), `mmglow`.
- Shadows/glare: album `ac*`/`agl*`, poster `pc*`/`pgl*`.
- Sway timing: `swaypause`, `phold`, flip speed (sway-animations.md).
- Every row carries `property name="info"` infographic (`media/bezel/info/`).
- Opened from Power › TUNER (`bz_tunesrc=pwr`, focus 6970). Back restores opener.

- WARM 2.0.1 `warmsplash` (Startup splash) On/Off → `bz_at_warmsplash`, default On; visuals only, warm-cache always runs. See mm-warm.md.

**5.33.210:** Tuner onback `bz_tunesrc=fsctrl` → `ActivateWindow(1121)` when `$EXP[bz_m1121ok]`, else `ActivateWindow(visualisation)`. All Fanart FS / visualisation tuner rows also apply to 1121 (shared includes).

## Strip-only list (5.33.298)
List 60 is always the colour-strip list — the old full-size off-strip list is parked at `/workspace/b401/parked_old_list/` (RESTORE.md). Every list view (Music L1–L3, Movies/TV, Music root, sources, files, non-library) draws in the strip: the list group is laid out 450×1038 at x120/y120 and always shrunk 86.67% (center 120,120) + slid 510 → on screen x570–960, y120–1020 (390×900, fills the strip, ~13.8 rows of 75). Grouplist clip (t4533) is 450×1038 so nothing paints past y1020. ALL row 6098 always rides the same shrink/slide. Left still goes to FULLSCREEN 6886 first on Music (5.33.297); Up/Down wrap to 6097/6098 unchanged; A–Z bars 6100/6500 stay at x78.
LIST Tuner rows after strip-only: none flushed (none were off-strip-only). Still wired to strip list 60: pingspeed, rowscroll, rowsoft, zoomtime, fanart, cascspeed, cascstag, hishape, zoomsize. zoomsize left at 100–115%: the focused-row zoom is scissored by the strip grouplist clip, so it cannot spill past the strip edge.

## Album shadow rows (5.33.300)
- **Cast offset X (`acx`) removed** — nothing read it after 5.33.299 CASTPIN. ALBUM SHADOW keeps Cast offset Y (`acy`), length (`aclen`), style (`acstyle`), soft, animated. Poster `pcx` unchanged. `bz_tune.json` may still list acx (python data; harmless, not edited — XML-only build).

### MAPS (5.33.303, Rob t2294u)
Section head `MAPS` (toggle `Skin.HasSetting(bz_topen_maps)`, `$VAR[BzTSec_maps]`), placed just before ABOUT / VERSIONS. Five read-only `btn` rows, ids `mapmusic1`–`mapmusic5` ("Music screens 1/5 … 5/5": Main Menu, Music section list, Music Fanart FS 1121, Dialogue FS 1120, Fullscreen visualisation). Info art `bezel/info/map_music_1..5.png` (1760×1620, generated by `/workspace/b401/music_screen_map/tuner_pages.py` from gen.py data). For `sec=MAPS` the BezelArtworkPanel 600×600 rocking art is hidden and a dedicated static image shows at **1000,210 880×810** (aspect keep, dark plate, bz_frame_soft border); caption/title labels above unchanged.

- **FULLSCREEN MUSIC > Open after 30 s idle in Music** (5.33.325, id `fsauto`, toggle, default ON, `bz_fsauto_off`): auto-opens Dialogue FS after 30 s idle in Music. Info art reuses `fs_music_delay.png`. See dialogue-fs.md.

## 5.33.334 — WARM folders merged (t2450)
- Row ids and handlers unchanged (same skin strings). `BzTSec_warmsys` variable kept but unused.

- 5.33.398: ALBUM / POSTER gains **Poster ↔ album fade** (`a2pfade`, slider, `bz_at_a2pfade` 1–7, default 4 = 400 ms; LEFT faster / RIGHT slower). Reset album clears it.

**No MM auto-hide (5.33.398 NOAUTOHIDE, Rob t2799u):** the strip 6996 / group 6894 stays visible and focusable the whole time MM is open. There is no idle fade, no park button 6897, no `bz_mmidle`, no idle label / clearart stage, no wake path (WAKEGRACE/IDLEPARK/IDLERESET), and no Tuner Auto-hide row. mmdim and the colour backdrop follow plain MM-open rules. MMHOLD on MM open is unchanged.
