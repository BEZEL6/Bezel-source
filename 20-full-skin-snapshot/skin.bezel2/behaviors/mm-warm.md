> **5.33.187 (Oct 31 2026, Rob voice):** warm = 5.33.151 base **plus two kept post-151 features**:
> 1. Music underlay always `musicdb://artists/` (.164) + `bz_music_underlay` guard; Select still returns to `bz_lastmusic` (bz_mm); BUG-016 (.168) already-warm Music = artists root only.
> 2. BUG-010 (.161) Music vs poster family split: `_clear_poster_lane`, same-family `_ahold` (poster/tvshow.poster only), `_ab_poster` Videos-only, BezelPoster60/hold Videos-only.
> Rolled back to 151: fade-in-only .160 (BZMMXF fadetime 3000 back; A/B lanes 1500 in/out), .162/.185 lane-a/b hold timings, BUG-011 .186 mmstart hold, BUG-015 .175 1.5 s empty hold + .178 bz_pos_drop gate, movposter_hold (t4813) + held-poster staging into lane restored.

# MM warm (WARM 2.0)

**Object:** Main Menu warm underlay (`scripts/bz_flip.py` → `mm_warm`)  
**Where:** Under `$EXP[bz_navmenu]`, strip `6996` focused  
**Last updated:** 2026-10-31 · live 5.33.200 (+ uncommitted: GlobalBackdrop hide during warm gate)  
**Status:** live 5.33.200 — WARM 2.0 through .193 mushide; A/B fixed 1500 ms (.192); warm-gate overlay 199+; GBD hidden while `bz_warm_gate`  
**Skin:** skin.bezel2

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

## Section fade (5.33.196)
Warm swaps no longer arm `bz_xfin` / BezelSecDim parent zero→100 fade. Held art stays up, then new art shows (poster-style fade-in only). No dim-out on section change.

## MM-only A/B preload (5.33.148, WARM 2.0)
Helper: `bz_flip.py` `_ABLane(prefix, settle=0.25, load_wait=0.5, empty_flag)` driven by `ab_clock` (50 ms tick).
Flow per lane: target settles 0.25 s → staged on hidden side `bz_<p>_a|b` → 0.5 s LOAD_WAIT → `bz_<p>_side` flips → XML Visible/Hidden 1500 ms sine fades crossfade.
| Gate | Behavior |
|------|----------|
| `bz_nav == true` (MM open), no Container.IsUpdating / modal | Lanes armed and staging |
| MM close | Pending stage dropped (hidden side reset to last shown); last shown art kept; nothing cleared |
| Lane never fed (`bz_<p>_on` empty) | Original live MM twin (fadetime 3000) shows |

Lanes (order built): 1) `fan` — BezelFanartLayer MM twin → `bz_fan_a/b`, `bz_fan_side`, `bz_fan_on` (chain mirrors BezelFanart browse branches, Container(60)). 2) `pos` — list-60 big poster MM twin → `bz_pos_a/b`, `bz_pos_side`, `bz_pos_on`, `bz_pos_empty` (mirrors BezelPoster60; Default* icons = empty → stand-in). 3) `clr` — TV clearlogo/clearart colour-strip header → `bz_clr_a/b`, `bz_clr_side`, `bz_clr_on`, `bz_clr_empty` (same settle/load + 1500 ms sine as fan/pos). 4) Album browse — music flip faces A/B MM twins reuse `pos` lane only when `!Player.HasAudio + bz_cov_<face>` empty; playing cover (bz_cov_a/b flip) always wins.
Untouched: section (`!bz_navmenu`) twins, list rows/grids, in-section art.

## WARM 2.0 (5.33.191)
- Expression `bz_mmmushide` = Player.HasAudio + !Player.HasVideo + bz_navmenu + bz_at_warmmusicposters != Off.
- While true: BezelVPLPoster MM poster images (BezelPoster60 fallback + pos A/B) hidden; album art `Player.Art(thumb)` drawn at bz_art_x/bz_top 600 x bz_h, aspect keep, fade 600/300. Fanart lane (bz_fan_*) unchanged. Music album group untouched (already playing-cover wins).
- `bz_at_abfade` (Tuner WARM 2.0 slider): 1=2500 2=2000 3=1800 4/empty=1500 5=1200 6=1000 7=800 ms; applied to the 8 MM fan/pos A/B side controls as conditional Visible/Hidden fades. Left = longer, Right = faster.
- Note: toggling Off while music already plays relies on next A/B refresh; set before playback shows posters immediately.
- 5.33.192: XML abfade chains removed — fan/pos A/B back to fixed 1500ms; Tuner slider remains for later (no effect for now).

### 5.33.193 music-poster toggle
- Row renamed "Album art during music" (On/empty = hide MM poster lane + album art in slot; Off = posters show). Skin.String meaning unchanged.
- mushide gate covers poster, cast shadow (animated + static), blur/frame, LOOK, glare/lit dust in BezelVPLPoster. Fanart lane never gated.
- Album slot uses `BzWarmMusicArt`: thumb > album.thumb > MusicPlayer.Cover > Player.Icon > DefaultAlbumCover.png.
- Toggle Left/Right sets `bz_mushref` (AlarmClock clears after 1s); poster/album images re-latch with a 400 ms Conditional fade. Sway props untouched, so the sway keeps running.

## Warm gate — cold-start splash (Rob approved Oct 31 2026; non-modal overlay 5.33.199; min 5 / max 15 / fade 3 s — 5.33.201)
The splash is the WARM system's cold-start gate. **5.33.199 sequence:** (1) splash draws first (2) main section windows/layouts/controls build **under** the splash (3) artwork cache loads (4) splash fades — no pop, no blank.

**Objects:** `xml/Startup.xml` · include `BezelWarmGateOverlay` + `BezelWarmGate` (`Includes_Bezel.xml`) on Startup, `MyMusicNav.xml`, `MyVideoNav.xml` · `scripts/bz_warmgate.py` · `xml/Custom_1113_WarmGate.xml` (**not opened** — kept only so dialog id 1113 stays reserved)
**Properties (Home):** `bz_warm_gate` (overlay up) · `bz_warm_ready_music` / `_movies` / `_tv` · `bz_warmgate_running` · `bz_splash_done` (set on dismiss; releases `bz_cmd.py start`)

| Step | Behavior |
|------|----------|
| 0 — first paint | `Startup.xml` sets `bz_warm_gate=1`, clears `bz_splash_done`, starts `bz_warmgate.py`, then `ReplaceWindow(StartupWindow)`. Splash is `BezelWarmGateOverlay` (property-gated group), **not** modal dialog 1113. |
| 1 — underlay | Because nothing modal is open, `ReplaceWindow` to Music/Videos **succeeds**. Music or Videos builds layouts/controls while the overlay (same black + logo) continues on that window via `BezelWarmGateOverlay` drawn last in controls. |
| 2 — screen | Solid black 1920×1080, Bezel logo + `bezel/logoglow` pulse, version label, credit + flag (same `BezelWarmGate` art as before). Overlay Hidden animation = **3000 ms** sine fade-out (5.33.201). |
| 3 — wait land | Script waits until the Startup-highlight section's list 60 has items and is not updating (Music / Movies|sets / TV), or until the 5 s hard cap. |
| 4 — art warm | **After** land (or late in CAP): `Files.GetDirectory` for focused section first, then the other two, on a **background thread**. Ready flags flip success or fail. |
| 5 — dismiss | After `MIN`, clear `bz_warm_gate` → **3.0 s** overlay fade, then `bz_splash_done=1`. **Never** `ActivateWindow(1113)`. Ready early still waits until 5 s. |
| 6 — hard cap | **15.0 s** (`CAP`): watchdog force-dismiss if land/art still incomplete. |

- `bz_precache.py` stays idle while `bz_warm_gate` is set. `bz_flip.py` still treats visible 1113 as busy (harmless; 1113 is not opened).
- Keys can reach the underlay while the overlay is up (non-modal).
- **Startup flash fix (uncommitted):** `BezelGlobalBackdrop` (nested in `BezelBlack` on Home/Music/Videos) stays **hidden** while `Window(Home).Property(bz_warm_gate)` is set — visible rule is `!String.IsEqual(Skin.String(bz_at_gbdsty),off) + String.IsEmpty(Window(Home).Property(bz_warm_gate))` in `Includes_Bezel.xml`. Solid black from `BezelBlack` still paints under the splash; glow backdrop only returns when the gate clears (under the 3 s fade).

### Tuner toggle: Startup splash (WARM 2.0)
- Setting `Skin.String(bz_at_warmsplash)` = `On`/`Off`; **default On** (empty = On).
- Toggle controls splash **visuals only**. Warm-cache and ready flags **always run**.
- On: `bz_warm_gate` + `BezelWarmGateOverlay` on Startup/Music/Videos.
- Off: no gate property / no overlay; silent warm; `bz_splash_done=1` when ready or at CAP.

