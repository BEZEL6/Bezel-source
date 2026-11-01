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
