# Skin settings / BEZEL Tuner

**Object:** `SkinSettings.xml`, `Includes_Tuner.xml` (focus 6970)  
**Last updated:** 2026-10-31 · 5.33.194 (catch-up sync to live tree)  
**Status:** draft — matches live 5.33.194 (IDs/files re-verified Oct 31); not Rob-approved, not re-smoked

## Open / close
Power menu → TUNER.

## Keys
| Key | Behavior |
|-----|----------|
| Up/Down | Move |
| Select | Change setting |

## Touch
Touch master On/Off lives here.

## Code notes
bz_tune.py

## Related
power-menu.md · touch-group.md

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
- WARM 2.0 section (`warmmusicposters` On/Off → `bz_mmmushide`; `abfade` slider present but no effect since 5.33.192 — A/B fixed 1500 ms). See mm-warm.md.
- LOOK: Global dim `gdim` (values listed 90%→30%; bz_tune.json default index 7 = last entry — **unverified** vs Rob standard "default 60%"; flagged), fanart `fanop`, logo colour/opacity, colour block.
- MENU: `mmxfade` 0–5 s crossfade (MM-open only), `mmglow`.
- Shadows/glare: album `ac*`/`agl*`, poster `pc*`/`pgl*`.
- Sway timing: `swaypause`, `phold`, flip speed (sway-animations.md).
- Every row carries `property name="info"` infographic (`media/bezel/info/`).
- Opened from Power › TUNER (`bz_tunesrc=pwr`, focus 6970). Back restores opener.

- WARM 2.0 `warmsplash` (Startup splash) On/Off → `bz_at_warmsplash`, default On; visuals only, warm-cache always runs. See mm-warm.md.
