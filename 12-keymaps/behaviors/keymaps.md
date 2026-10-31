# Keymaps (BEZEL profile keymaps) — 5.33.194

**Object:** `scripts/bz_km.py`, `bz_dtap.py`, `bz_cmd.py keymap|keymap_leave`, `bz_flip.py km_leave_watch`, `resources/keymaps/bezel2_np_tab.xml`  
**Status:** draft — live 5.33.194 (not zipped)

**Last updated:** 2026-10-31 · 5.33.194 (catch-up sync to live tree)  

Kodi has no skin-scoped keymaps; anything in `special://profile/keymaps/` is global. BEZEL therefore installs its keymaps only while Bezel runs and removes them when the user leaves the skin (option one, "quarantine").

## Install (while on Bezel) — unchanged
- `bz_cmd.py keymap` (music window onload / bz_flip start): copies `resources/keymaps/bezel2_np_tab.xml` -> `zz_bezel2_np_tab.xml`, reloads keymaps, starts `bz_dtap.py`.
- `bz_dtap.py`: writes `zz_bezel2_noctx.xml` (`noctx()`) at start; installs `zz_bezel2_dtap.xml` while Skin setting `bz_dtap_off` is NOT set.
- `bz_dtap_off` ON (or normal Bezel quit) removes ONLY `zz_bezel2_dtap.xml` (as before).

## Leave (skin switch away from skin.bezel2) — new
`scripts/bz_km.py leave()`: deletes `zz_bezel2_np_tab.xml`, `zz_bezel2_dtap.xml`, `zz_bezel2_noctx.xml` (profile paths only), clears Home `bz_km_loaded`, runs `Action(reloadkeymaps)` if anything was deleted, logs `BEZEL keymap leave: removed ...` / `nothing to remove`.

Triggered by (whichever notices first; leave() is idempotent):
- `bz_dtap.py` main loop (~1 s check of `xbmc.getSkinDir()`), then loop exits; also in its `finally` if skin is no longer Bezel (even when aborting).
- `bz_flip.py` helper `km_leave_watch` (1 s poll) -> leave() + clears `bz_flip_running`; also in flip `finally` if not on Bezel.
- Manual: `RunScript(special://skin/scripts/bz_cmd.py,keymap_leave)`.

Kodi shutdown while still on Bezel does NOT run leave (exit-freeze guard). Keymaps return next time Bezel loads music / starts bz_flip.
