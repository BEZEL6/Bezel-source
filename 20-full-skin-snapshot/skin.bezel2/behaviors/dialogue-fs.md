# Dialogue FS

**Object:** `Custom_1120_PlayNext.xml` (album mode `bz_dfs_mode=album`) · `6400`/`6401`/`6405`/`6406`  
**Last updated:** 2026-10-31 · 5.33.194 (catch-up sync to live tree)  
**Status:** draft — matches live 5.33.194 (IDs/files re-verified Oct 31); not Rob-approved, not re-smoked

## Open / close
Opened from big album tap (Music section) or Music controls Right. Back closes (bz_fsret).

## Keys
| Key | Behavior |
|-----|----------|
| Select | Pause + ghost logo |
| Left/Right | Previous / Next (unless pill focused) |
| Up | Focus pill |
| Select/Left/Right on pill | Cycle ALBUM ↔ PREV/NEXT |
| Down from pill | Back to main control `6400` (live `6401` ondown=6400; **fixed 2026-10-31**, old doc said "Music controls") |
| Back | Close 1120 |

## Touch
Bezel logo = Back. Cast gated on Cover. Pause+cast same as Play Next.

## Code notes
Rob memory + live 1120

## Related
play-next.md · music-controls.md · fullscreen-pill.md


## 5.33.163 Slide speed (shared)
Dialogue FS stage slide (-1100 px) time follows Tuner › FULLSCREEN MUSIC › VIZ › Slide speed (`bz_at_fsslide`): 1 SLOW 480 ms (legacy), 2 MID-LOW 380, 3/empty MID-HIGH 280 (default), 4 FAST 180. Same string drives Dialogue FS slides (Includes_Bezel ×2, Custom_1112) and viz preview-next (MusicVisualisation ×2) so they stay synced. Grouplist 6397 scrolltime stays static 480 (Kodi scrolltime cannot be conditional).
Album grouplist `6397` scroll (open/close rail) uses the same setting via four speed-gated rails (5.33.165); default mid-high keeps 6397/6398/6399.

**5.33.166:** Ghost Bezel pause logo centred on the 600px album (was top-left 27,27).
**5.33.167:** Pause mark baked into same texture — `bezel/logo_pause.png` (Bezel logo + centered pause bars); still 111px ~35% at 245,245. `logo.png` unchanged for LOOK/home.

## Album strip / NP with big album (live 5.33.194)
- Dialogue album strip = album grouplist `6397` (four speed-gated rails, 5.33.165). Compact Music NP rides it (5.33.121), so album + NP move as one.
- Slide speed `bz_at_fsslide`: 1 Slow 480 · 2 Mid-low 380 · 3/empty Mid-high 280 (default) · 4 Fast 180 ms — shared by Dialogue FS stage slides, Custom_1112, viz preview-next.
- Pause logo `bezel/logo_pause.png` centred on 600px album (5.33.166–167).
