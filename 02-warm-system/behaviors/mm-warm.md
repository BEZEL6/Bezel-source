# MM warm (WARM 2.0) — LOCKED

**Object:** Main Menu warm underlay (`scripts/bz_flip.py` → `mm_warm`) + cold-start warm gate (`scripts/bz_warmgate.py`)  
**Where:** Under `$EXP[bz_navmenu]`, strip `6996` focused  
**Last updated:** 2026-10-31  
**Status:** LOCKED — live as of 5.33.203 (Rob approved Oct 31 2026). This file describes the current state, not a changelog. Any change needs Rob's approval.  

**Startup random row (5.33.204 RANDSTART):** startup seeds a random list-60 row (skip `..` / *All), not only the GetDirectory art window — `bz_warmgate.py` `randstart()` after LAND for the first section; `bz_flip.py` `_restore` picks + seeds `SS[sec].row/path` via `_randrow()` when a section has no session row. Strip 6996 focus bounced back.

**Skin:** skin.bezel2

## Locked summary (live 5.33.203)
| Setting | Live value |
|---------|-----------|
| Park delay | `0.2 × bz_at_mmwarm` (1–10 → 0.2–2.0 s, default 0.2 s); ≥ 0.5 s parked before ActivateWindow |
| Music underlay | always `musicdb://artists/` (+ `bz_music_underlay` guard); Select returns to `bz_lastmusic` |
| Section swap | fade-in only: `bz_arthold` hold → release when new list has item + family art (≤ ~0.9 s, 45×20 ms); no `bz_xfin`/`bz_xfade` dim-out |
| Family split (BUG-010) | Music ↔ Movies/TV: poster lane cleared at once, fanart-only hold. Movies ↔ TV: poster + fanart hold (`bz_hold_poster`, poster/tvshow.poster only) |
| A/B lanes | `fan`, `pos`, `clr`: settle 0.25 s → LOAD_WAIT 0.5 s → side flip → 1500 ms sine Visible/Hidden crossfade (fixed) |
| Lane not fed | live MM twin image, `fadetime` 3000 |
| Backdrop cycle | 10 s parked → new random `extras/backdrop/` image |
| Music playing (`bz_mmmushide`) | MM poster lane hidden, album art (`BzWarmMusicArt`) in poster slot, fade 600 in / 300 out, re-latch 400 ms |
| Warm gate | MIN 5.0 s · CAP 15.0 s · FADE 3.0 s; random 400-item GetDirectory window per section |
| GBD | `BezelGlobalBackdrop` hidden while `bz_warm_gate` set |
| Tuner WARM 2.0 rows | Startup splash (`bz_at_warmsplash`, default On) · Album art during music (`bz_at_warmmusicposters`, default On) · A/B fade length (`bz_at_abfade`, **no effect** — XML fixed 1500 ms) |

## Warm park (unchanged)
| Item | Behavior |
|------|----------|
| Park | Highlight Music / Movies / TV, hold `0.2 × bz_at_mmwarm` (0.2–2.0 s, default 0.2 s) → underlay loads |
| Window switch | ≥ 0.5 s parked before ActivateWindow |
| Same window + same path | No-op (row already kept) |

## Session store (in memory, not Skin.String)
| Key | Fields |
|-----|--------|
| `music` · `movies` · `tv` | `row` (0-based, for `SetFocus(60,N,absolute)`), `path` (FolderPath), `backdrop`, `timer_on`, `parked_since` |
- Cleared when MM closes (`bz_nav` empty). Nothing saved across sessions.

## (1) Position map
| Step | Behavior |
|------|----------|
| Before swap | Snapshot leaving underlay: `Container(60).CurrentItem − 1` + FolderPath + backdrop |
| After settle | `!Container.IsUpdating` and FolderPath == saved path → `SetFocus(60,row,absolute)` then same-frame `_bzstrip` → `6996` |
| Movies / TV | Share Videos window — always save/restore from memory (list is not kept alive) |
| Music | Path + row must both match (last Music folder) |
| Row 0 / Select during warm | No restore |

## (2) Backdrop cache
- One image per section. On warm start to a cached section, `Home.Property(bz_backdrop)` is set to the cached path **before** the swap → fade lands on that image.
- MyMusicNav / MyVideoNav onload only picks when `bz_backdrop` is empty (5.33.142), so no random overwrite.
- No cache yet → normal first pick, then stored.

## (3) Gated backdrop cycle
| Condition | Behavior |
|-----------|----------|
| MM open + strip 6996 focused + section parked & warm done | Timer runs |
| Held **10 s** | New random image from `extras/backdrop/` (not the current one), cache updated, 10 s restarts |
| Scroll away | Timer frozen (`timer_on=False`), backdrop snapshotted |
| Return | Cached image; 10 s restarts from the new park |
| Tuner fixed backdrop (`bz_bdimg`) or < 2 images | No cycle |

## Rules
- Strip `6996` always owns focus under MM; list 60 only for the restore frame.
- No K40 open-anim gates.

## Section fade
Warm swaps do not arm `bz_xfin` / BezelSecDim parent zero→100 fade. Held art stays up, then new art shows (poster-style fade-in only). No dim-out on section change.

## MM-only A/B preload
Helper: `bz_flip.py` `_ABLane(prefix, settle=0.25, load_wait=0.5, empty_flag)` driven by `ab_clock` (50 ms tick).
Flow per lane: target settles 0.25 s → staged on hidden side `bz_<p>_a|b` → 0.5 s LOAD_WAIT → `bz_<p>_side` flips → XML Visible/Hidden 1500 ms sine fades crossfade.
| Gate | Behavior |
|------|----------|
| `bz_nav == true` (MM open), no Container.IsUpdating / modal | Lanes armed and staging |
| MM close | Pending stage dropped (hidden side reset to last shown); last shown art kept; nothing cleared |
| Lane never fed (`bz_<p>_on` empty) | Original live MM twin (fadetime 3000) shows |

Lanes (order built): 1) `fan` — BezelFanartLayer MM twin → `bz_fan_a/b`, `bz_fan_side`, `bz_fan_on` (chain mirrors BezelFanart browse branches, Container(60)). 2) `pos` — list-60 big poster MM twin → `bz_pos_a/b`, `bz_pos_side`, `bz_pos_on`, `bz_pos_empty` (mirrors BezelPoster60; Default* icons = empty → stand-in). 3) `clr` — TV clearlogo/clearart colour-strip header → `bz_clr_a/b`, `bz_clr_side`, `bz_clr_on`, `bz_clr_empty` (same settle/load + 1500 ms sine as fan/pos). 4) Album browse — music flip faces A/B MM twins reuse `pos` lane only when `!Player.HasAudio + bz_cov_<face>` empty; playing cover (bz_cov_a/b flip) always wins.
Untouched: section (`!bz_navmenu`) twins, list rows/grids, in-section art.

## Music playing under MM
- Expression `bz_mmmushide` = Player.HasAudio + !Player.HasVideo + bz_navmenu + bz_at_warmmusicposters != Off.
- While true: BezelVPLPoster MM poster images (BezelPoster60 fallback + pos A/B) hidden; album art `Player.Art(thumb)` drawn at bz_art_x/bz_top 600 x bz_h, aspect keep, fade 600/300. Fanart lane (bz_fan_*) unchanged. Music album group untouched (already playing-cover wins).
- Note: toggling Off while music already plays relies on next A/B refresh; set before playback shows posters immediately.
- `bz_at_abfade` Tuner slider (A/B fade length) exists but is not wired: fan/pos/clr A/B fades are fixed 1500 ms in XML.

### Album art during music toggle
- Row renamed "Album art during music" (On/empty = hide MM poster lane + album art in slot; Off = posters show). Skin.String meaning unchanged.
- mushide gate covers poster, cast shadow (animated + static), blur/frame, LOOK, glare/lit dust in BezelVPLPoster. Fanart lane never gated.
- Album slot uses `BzWarmMusicArt`: thumb > album.thumb > MusicPlayer.Cover > Player.Icon > DefaultAlbumCover.png.
- Toggle Left/Right sets `bz_mushref` (AlarmClock clears after 1s); poster/album images re-latch with a 400 ms Conditional fade. Sway props untouched, so the sway keeps running.

## Warm gate — cold-start splash (MIN 5 s / CAP 15 s / FADE 3 s)
The splash is the WARM system's cold-start gate. **5.33.199 sequence:** (1) splash draws first (2) main section windows/layouts/controls build **under** the splash (3) artwork cache loads (4) splash fades — no pop, no blank.

**Objects:** `xml/Startup.xml` · include `BezelWarmGateOverlay` + `BezelWarmGate` (`Includes_Bezel.xml`) on Startup, `MyMusicNav.xml`, `MyVideoNav.xml` · `scripts/bz_warmgate.py` · `xml/Custom_1113_WarmGate.xml` (**not opened** — kept only so dialog id 1113 stays reserved)
**Properties (Home):** `bz_warm_gate` (overlay up) · `bz_warm_ready_music` / `_movies` / `_tv` · `bz_warmgate_running` · `bz_splash_done` (set on dismiss; releases `bz_cmd.py start`)

| Step | Behavior |
|------|----------|
| 0 — first paint | `Startup.xml` sets `bz_warm_gate=1`, clears `bz_splash_done`, starts `bz_warmgate.py`, then `ReplaceWindow(StartupWindow)`. Splash is `BezelWarmGateOverlay` (property-gated group), **not** modal dialog 1113. |
| 1 — underlay | Because nothing modal is open, `ReplaceWindow` to Music/Videos **succeeds**. Music or Videos builds layouts/controls while the overlay (same black + logo) continues on that window via `BezelWarmGateOverlay` drawn last in controls. |
| 2 — screen | Solid black 1920×1080, Bezel logo + `bezel/logoglow` pulse, version label, credit + flag (same `BezelWarmGate` art as before). Overlay Hidden animation = **3000 ms** sine fade-out (5.33.201). |
| 3 — wait land | Script waits until the Startup-highlight section's list 60 has items and is not updating (Music / Movies|sets / TV), or until the 15 s CAP. |
| 4 — art warm | **After** land (or late in CAP): `Files.GetDirectory` for focused section first, then the other two, on a **background thread**. Each section uses a **random** 400-item window (`limits.start` shuffled; size still 400). Ready flags flip success or fail. |
| 5 — dismiss | After `MIN`, clear `bz_warm_gate` → **3.0 s** overlay fade, then `bz_splash_done=1`. **Never** `ActivateWindow(1113)`. Ready early still waits until 5 s. |
| 6 — hard cap | **15.0 s** (`CAP`): watchdog force-dismiss if land/art still incomplete. |

- `bz_precache.py` stays idle while `bz_warm_gate` is set. `bz_flip.py` still treats visible 1113 as busy (harmless; 1113 is not opened).
- Keys can reach the underlay while the overlay is up (non-modal).
- **Startup flash fix:** `BezelGlobalBackdrop` (nested in `BezelBlack` on Home/Music/Videos) stays **hidden** while `Window(Home).Property(bz_warm_gate)` is set — visible rule is `!String.IsEqual(Skin.String(bz_at_gbdsty),off) + String.IsEmpty(Window(Home).Property(bz_warm_gate))` in `Includes_Bezel.xml`. Solid black from `BezelBlack` still paints under the splash; glow backdrop only returns when the gate clears (under the 3 s fade).

### Tuner toggle: Startup splash (WARM 2.0)
- Setting `Skin.String(bz_at_warmsplash)` = `On`/`Off`; **default On** (empty = On).
- Toggle controls splash **visuals only**. Warm-cache and ready flags **always run**.
- On: `bz_warm_gate` + `BezelWarmGateOverlay` on Startup/Music/Videos.
- Off: no gate property / no overlay; silent warm; `bz_splash_done=1` when ready or at CAP.


## Music ↔ Movies/TV artwork fade (live tree, after 5.33.203 — not yet zipped)
Applies to the album/poster image only on Music→Movies, Music→TV, Movies→Music, TV→Music. Movies↔TV is unchanged: it still holds the poster with `bz_hold_poster`. Fanart, strip, dim and labels are unchanged.
- **Video → Music:** the poster A/B lane (`bz_pos_a/b`, `bz_pos_on`) is kept through the window swap. When `_arel` runs (the new list has an item), `bz_pos_on` is cleared, so the poster fades out with its 1500 ms Hidden fade while the Music album appears with its texture fadetime of 3000 ms. After 1.7 s the poster textures are cleared, but only if `bz_pos_on` is still empty. This is the BUG-010 guard: no video poster stays on Music.
- **Music → Video:** `_ahold` saves the outgoing album as `bz_xalb` / `bz_xalb_on`. In Videos, a held-album image sits under the poster A/B lane. `_arel` clears `bz_xalb_on`, so the album fades out over 1500 ms while the new poster fades in over 1500 ms. `bz_xalb` is cleared after 1.7 s.
- Code: `bz_flip.py` `_xfade_out` / `_ahold` / `_arel`. XML: `Includes_Bezel.xml` held-album image before the MM album/poster slot. It does not use the `bz_xfin` dim-out.
