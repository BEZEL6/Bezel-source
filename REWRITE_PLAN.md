# BEZEL foundation rewrite — handoff plan

**Prepared:** 2026-11-03 (session with Rob, after 5.33.455).
**Next session:** after 12:51 am. Rob will say "go" before any build.
**Goal:** keep BEZEL's look and behaviour, but rebuild the foundations: layout from constants, one Python service instead of 19 polling threads, and no dead code. This is a staged rebuild under the current look, **not** a from-scratch rewrite. Each step is one commit, and builds happen only on Rob's go.

Read only this file at the start. Don't re-read the full CLAUDE_CHANGELOG (about 70 KB) unless a step needs its history.

---

## 0. Where things are

| What | Where |
|---|---|
| Repos (identical content) | `github.com/BEZEL6/Bezel` and `github.com/BEZEL6/Bezel-source`. Push branches only, never main. |
| Full skin | `20-full-skin-snapshot/skin.bezel2/` in either repo. It is byte-identical to the shipped zip contents (verified for 455). |
| Latest shipped build | **5.33.456** (branch `claude/5.33.456`): the 455 fixes (IDLEHOLD, TRANSCENTRE, MMCLEANFADE, TUNERCLEAN, GLOWSHIFT, FSTITLE) plus rewrite **P1A**. Rob has it in Downloads. |
| Next work | Branch off `claude/5.33.456`. Name builds `claude/5.33.457` and so on. |
| Tools | `tools/geom455/` (geometry resolver + plan/diff), `tools/rewrite/` (inventories), `tools/sync_lint.py`, `tools/xbt_pack.py`, `tools/xbt_verify.py` |
| Changelog for the main BEZEL agent | Repo root `CLAUDE_CHANGELOG.md` (full), the project doc `claude/CLAUDE_CHANGELOG.md` (part 1) and `claude/CLAUDE_CHANGELOG_part2_424-444.md`, and Downloads `CLAUDE_CHANGELOG.md`. Add every new build to all of them. |

### Build recipe (fresh container)
1. `git clone https://github.com/BEZEL6/Bezel && cd Bezel && git checkout <branch>`.
2. Bump `addon.xml` `version="5.33.N"`. Add an entry at the top of `changelog.txt`. Update `CLAUDE_CHANGELOG.md` in the skin copy and the repo root (they are the same file).
3. If anything under `media/` changed: rebuild the texture bundle with `python3 tools/xbt_pack.py <skin>/media <skin>/media/Textures.xbt <liblzo2.so>`.
   - pip and apt are blocked. Get LZO from GitHub (`jd-boyd/python-lzo` repo ships lzo sources; build `liblzo2.so` with `gcc -shared -fPIC`).
   - Images over 512 px stay loose files and aren't packed. That includes the 960×540 glow textures, so they need no repack.
4. Zip with top folder `skin.bezel2/`. Exclude `bak_*`, `port-refs/` and `__pycache__/`. The snapshot has none of these, so zipping it whole is right. Name: `skin.bezel2-5.33.N.zip`.
5. Deliver the zip:
   - `SendUserFile` the zip.
   - `device_commit_files` to `~/Downloads/`, passing the fileUuid (a stagedPath fails for big files).
   - Also commit `CLAUDE_CHANGELOG.md` to `~/Downloads/`.
6. Commit, then `git push -u origin claude/5.33.N` on **both** repos (copy the same files into the second repo).
7. Project doc: `project_write` needs a full Read of the local file first. Part 1 is about 30 KB, which is fine.

### Rules (Rob, standing)
- No visual change and nothing broken unless Rob asks for it. Refactor steps must give a **zero geometry diff** (see the tools below).
- **Leaf flip look and timing: LOCKED.** `behaviors/mm-warm.md` is LOCKED; restructure is allowed only if nothing visibly changes.
- One fix per commit, so any single fix can be reverted. Wait for Rob's "go" before a build, so builds batch up.
- **446 lesson:** Python timing and thread changes go one per build, and Rob A/B-tests each against the previous build. TICKCACHE (a per-tick cache) caused 20 s stalls and was reverted.
- Rob skipped for now: a glow texture remake without the strip panel, and the Up Next "playing item drawn multiple times" report.

---

## 1. Tools (use them, they save a lot of reading)
- **`tools/geom455/geom.py <skin>/xml out.json`**
  - Expands includes, params and constants for every window.
  - Writes each control's absolute x box: `x0`, `x1`, `src` (file:line), ordinals of its `left`/`width`/`right` elements (`lo`/`wo`/`ro`), and the param origin when the value came from an include param (`lpo`/`wpo`).
  - Also gives `id_`/`pid` for the tree. Runs in about 3 s.
- **`tools/geom455/xedit.py`:** edits elements by ordinal and keeps comments (`index`, `apply`, `check`). Ordinals match geom's `_o`. Always run `xedit.check` on all files first.
- **Zero-diff check for refactors:** resolve before and after, then compare boxes pairwise. They must be identical, as in P1A (0 changed out of 18,603).
- **Reference audit:** compare include, `$VAR` and `$EXP` definitions against uses (see the snippet used for GRIDDEL). There are 20 known false positives (`$VAR[X,prefix,suffix]` forms).
- **`tools/sync_lint.py`:** groups sway-family animations by trigger. Run it after any sway, glare or cast change.

---

## 2. Phases

### P1 — Layout from constants
- **P1A (DONE, branch `claude/rewrite-p1`):**
  - Added `bz_stage_x` 120, `bz_stage_w` 930, `bz_strip_x` 660 and `bz_strip_w` 390.
  - 395 exact literals and params now use them.
  - `bz_block_x` (stale value 570, never used) is now 660.
  - Zero geometry change; no constant leaks outside position tags.
- **P1B: strip content relative to the strip.**
  - Kodi constants can't do arithmetic, so absolute siblings like 690, 694 and 1026 still hard-code the strip position.
  - For each strip-family window, find the topmost strip-box controls with geom: box inside 660–1050, ancestors not inside it. That's `rules.S()` with the edges moved +90. 1050 is the strip right edge.
  - Wrap the run of siblings in `<control type="group"><left>bz_strip_x</left><top>0</top>…</control>` and subtract 660 from their lefts.
  - The rules:
    - Only wrap siblings that are consecutive and all strip-box; don't change draw order.
    - Children carrying `<right>` or `%` positions are skipped and listed.
    - An include used both inside and outside the strip gets a param `sx` (default 0) instead.
  - Acceptance: zero geometry diff, XML parses, reference audit clean.
  - Then moving the strip again is one constant change, which can be tested by setting `bz_strip_x` to 661 and checking that only strip boxes shift by 1.
- **P1C: stage and art.**
  - The block-left fills (120 w540, 18 of them, see the 455 BLOCK list in the changelog) become `bz_block_w` 540.
  - `bz_art_x` 1140 already exists; also use it for the poster and album sway centres 1440 = `bz_art_cx`.
  - The FS transport centre 585 and the in-place NP column 150–1020 get constants too.
  - Acceptance: zero diff.
- **P1D: one strip, one stage.**
  - Many dialogs inline their own strip background, frame and dims.
  - Fold them into the shared includes that already exist: `BezelMMStripChrome`, the `BzDlgFrame` / `BezelBrowseChrome` family at Includes_Bezel ~3770, `BezelRefreshStripBG`, `BzCIStripBG` and `BezelPVRStage`.
  - Do it one window per commit, zero diff each.

### P2 — One Python service (`scripts/bz_flip.py`, 2,116 lines, 19 threads)
The inventory is in `tools/rewrite/threads.json`: each thread's function line, poll intervals, the Home properties it touches, and its condition, label and builtin call counts.

The 445 perf log, in Kodi calls per second:
- About 3,000 calls/s in total.
- `nav_menu` about 1,110, `poster_clock` 520, `sway_clock` 475, `ab_clock` 265, `mm_autohide` 190, `mm_warm` 120, `vwarm` 97.
- Everything else is under 60.

PERFCOUNT logs a `BEZEL perf` line every 60 s to kodi.log for 15 minutes. Use it to measure each step.

Order: lowest risk first, **one per build**, with Rob A/B-testing each.
1. **Delete `grid_sync`** (line ~1590, 139 lines). It has been dead since GRIDDEL (455) but still polls at 20 Hz. Also delete the `gridfocus` branch in `bz_cmd.py` (~line 237) and the `bz_grid_*` handling in `nav_menu` (~1298, 1340, 1646).
2. **Merge the slow watchers into one 0.5 s loop:** `km_leave_watch` (1.0 s), `fpop_clock` (1.0), `allcnt` (0.4), `album_id` (0.5) and `cw_clock` (2/1). The behaviour stays the same; this just cuts thread count.
3. **Drop `bz_big_*`.** `bz_flip` still sets them, but no XML has read them since ONESWAY (453). Check with grep first.
4. **One clock, `sway_clock`.**
   - It owns `bz_sway_go`, `bz_sway_hold`, `bz_sway_pulse` and `bz_sway_restart`, plus the stub-cast anchor (`_sway_anchor`, `_bz_cast`).
   - Fold `poster_clock`'s sway part (`bz_pswayon`, `bz_ppulse`) and `idle_hinge` timing into it, so all motion reads one t0.
   - This is the structural end of the sync-drift bugs (440, 441, 445, 452, 453).
5. **Make playback event-driven.** Use `xbmc.Player` callbacks (`onAVStarted`, `onPlayBackStopped`, `onPlayBackEnded`, `onPlayBackPaused`/`Resumed`) and `xbmc.Monitor.onNotification` instead of polling `Player.HasAudio` in several threads.
6. **Last and riskiest: `nav_menu`, `mm_warm`, `vwarm`, `ab_clock`, `mm_autohide`.**
   - These carry the warm-window system (behaviours locked, see `behaviors/mm-warm.md`).
   - Only reduce per-tick work: skip window checks when nothing changed, and read focus once per tick.
   - No per-tick caching (446).

### P3 — Dead code (inventory in `tools/rewrite/deadcode.json`)
- **31 unused includes**, e.g. `BezelXInfo`, `BezelSwingPoster`, `BezelRainbowRow`, `BezelNavLogoGlow`, `BzCIStripUnder`.
- **13 unused expressions**, including the `bz_gsm_*` / `bz_gsv_*` grid leftovers.
- **312 unused variables**, mostly Estuary-derived. Before deleting each one, check it isn't used by name from Python (`$VAR[` strings) or in `$INFO[...]`-built labels.
- **22 windows with no BEZEL include** (Estuary leftovers, e.g. DialogButtonMenu, DialogGameControllers, PVR dialogs). Kodi needs the window files, so don't delete them; restyle them later or leave them.
- **`<visible>false</visible>` parked controls:** 57 across 20 files. Tuner has 19; some are TUNERCLEAN (456) and must stay.
- `bak_*` and `port-refs/` folders exist in the old work copies but not in the snapshot.
- Acceptance: XML parses, the reference audit is clean, and the geometry diff is zero except for removed controls that were never visible.

### P4 — Built-in checks
Add a `tools/check_all.sh` that runs: XML parse, `py_compile`, the reference audit, geom zero-diff against the previous tag (refactor builds), `sync_lint`, and the xbt freshness check (any `media/*.png` ≤ 512² newer than Textures.xbt). Run it before every build.

---

## 3. Suggested first moves next session (low usage)
1. Clone one repo and check out `claude/5.33.456`. Read this file only.
2. Ask Rob for device results on 456. Check FSTITLE first: the title on the Kodi music fullscreen fanart stage was covered by the stage block, and the fix is reading-based, not device-tested.
3. Start with P2.1 (delete `grid_sync`) as its own commit, and P1B (zero diff, safe to batch). Build 457 when Rob says go. Rob A/Bs P2.1 against 456.

## 4. What 456 contains (built 2026-11-04)
- **IDLEHOLD:** "small black pulse on big album on music start".
  - The idle A/B slots faded on `Player.HasAudio` (`bz_at_midlefade`, 300 ms since 454) under the NP layer's 400 ms fade-in, which made a crossfade dip.
  - Now the slots fade only for the A/B side flip; the NP layer fades over them.
  - Includes_Bezel, BezelMusicPlayingArt idle stack, 14 conditions.
- **TRANSCENTRE:** "transport bar labels need to be centered for the new stage".
  - FS transport (BezelNPInPlace, the Transport bar group): the centre control and time labels sit symmetric about x 585; the pills stay at the stage edges.
- **MMCLEANFADE:** "transition in out from mm fades black then back".
  - The 22 `bz_at_mmdim` Background-dim fades on MM open now have `delay="1500"`, the MM art lane fade-in time, so the dim happens under the lane.
  - The exit reverse is immediate.
- **TUNERCLEAN:** "remove nav legend and section labels in the art window".
  - 5 labels hidden in Includes_Tuner: two UP/DOWN legends, the rail section name and the "N settings" label.
- **GLOWSHIFT:** "glow textures need to be redone for new larger stage position".
  - The 17 `media/bezel/glow/mm_glow_*.png` textures (960×540, drawn full screen) are shifted 45 px (90 on screen) so their baked strip panel sits behind the new strip.
  - Rob then said "skip glow", so no remake.
  - Removing the panel cleanly needs new textures, because the light effects are painted through it.
- **Not checked on device:** all 456 items. They were checked statically only (parse, audit, geometry).

---

## 5. Progress log (P1B, session 2026-11-04, branch `claude/rewrite-p1b`, based on 456)
Tools: `geom455/p1b.py <geom.json> <xml> --base 570|0|120 [--apply]` (container conversion, consistency-checked),
`p1b_anchor.py` (full-screen/stage children -> `bz_strip_nx` / `bz_strip_tostage`), `zerodiff.py` (run with `ZD_GROUPS=1`:
groups draw nothing, so only drawn controls + absolute anim centres must match), `striptest.py` (strip+1 simulation:
set bz_strip_x 661, bz_strip_nx -661, bz_strip_tostage -541). Re-run geom after every --apply (inserted lefts shift ordinals).
New constants next to `bz_strip_x`: `bz_strip_nx` -660, `bz_strip_tostage` -540 (change with bz_strip_x; Kodi has no arithmetic).
Kodi facts checked in source: zoom without centre uses the control's own rect (safe); rotate without centre = parent origin
(none exist in BEZEL); constants resolve in `end`/`start`/`center` attributes but whole-value only.
- [x] part 1 (d35f4d1 / bc5ab22): 98 containers at old strip x 570 -> bz_strip_x. Strip test 859 -> 2,662.
- [x] part 2 (4eb21f5): 29 groups at x 0 holding only strip content -> bz_strip_x. Strip test 3,085.
- [x] part 3 (c77e443): 165 absolute strip elements (640 uses) wrapped in `<control type="group"><left>bz_strip_x</left><!-- P1B -->`,
      lefts/param origins/own centres -660 (`p1b_wrap.py`; compare with `unwrap_cmp.py`, which drops the marked wrappers).
      Strip test: **4,829 of 4,885** strip controls follow. Left on purpose: BigAlbum casts (strip in 1122, art elsewhere),
      grouplist children, legacy PVR windows.
- [x] P1C (87b143a): `bz_fill_w` 540 (= bz_strip_x - bz_stage_x) on the 18 stage fills; 60 screen-level 120 -> bz_stage_x;
      31 screen-level 1140 -> bz_art_x (`p1c.py`). Old `bz_block_x`/`bz_block_w` (390) = the strip in old naming, unused (P3).
- **Moving the strip now:** change `bz_strip_x`, and with it `bz_strip_nx` (= -bz_strip_x), `bz_strip_tostage`
  (= bz_stage_x - bz_strip_x) and `bz_fill_w` (= bz_strip_x - bz_stage_x). All four sit together in Includes_Bezel ~2570.
  Not covered: the library list slide 620.84 inside the zoom 86.67 group, and animation centres written as "x,y".
- [ ] P1D (fold inline strip copies into shared includes): not started. Judgment-heavy, one window per commit.
- [x] Build 457 = P1B + P1C (built 2026-11-04). Rob on device: "looks good so far".

## 6. Progress log (P2 + fixes, branch `claude/5.33.458`, based on 457)
- [x] 458 MMNODIM (a46ce55): Rob, on 457: the 456 MMCLEANFADE 1.5 s dim delay "makes it look broke"; "just have it fade in quick.
      no fade out of section". The 22 `bz_at_mmdim` fades are removed from BezelSecDim / BezelSecDimArt, so the section isn't dimmed
      under the MM. The Tuner "Background dim" row no longer affects the MM. The MM art lane fade (1500, locked mm-warm system) is unchanged.
- [x] P2.1 (3f89855): `grid_sync` deleted. 6600 doesn't exist since GRIDDEL; idle branch only. `bz_gpend` still cleared by the
      MyVideoNav onload AlarmClock. Left for P3: bz_cmd `gridenter/gridclick/gridfocus`, the 41 XML `6600` conditions (always false),
      `bz_gslot`/`bz_gtitle` consumers. Left for P2.6: nav_menu `bz_grid_*` checks (~1298, ~1340).
- [x] P2.3 (feb53ab): sway_clock no longer sets `bz_big_go` / `bz_big_pulse` (unread since 453). Exit cleanup still clears them.
- [x] Build 458 = MMNODIM + P2.1 + P2.3. Rob on device: "458 good".
- [ ] P2.2 **TRIED AND REVERTED.** Build 459 (fb02378) put the five slow watchers in one `slow_watch` thread (generators
      yielding their own waits; mock run showed unchanged intervals). Rob: "457 great", "458 good", "459 very bad",
      "backgrounds perform poorly". Reverted on `claude/5.33.459`; bz_flip.py = 458. Cause unknown: none of the five touches
      background art directly. Don't retry without a 459 kodi.log (BEZEL perf lines, "watcher crashed" lines).
      Suspects: `cw_build` thread start-up; fpop / album_id / allcnt sharing one thread when a call is slow; GIL scheduling.
- Next candidates (Python, one per build, A/B): P2.4 one sway clock. Or skip ahead to P3 dead code (XML only, safer).
- Build hygiene: `py_compile` leaves `scripts/__pycache__` in the snapshot. Delete it before zipping.
