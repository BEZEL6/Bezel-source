# Home / startup splash

**Last updated:** 2026-10-31 · live 5.33.203 (Warm 2.0 locked)

The startup splash is now the **warm gate** of the WARM system. Its full spec (sequence, styling, flags, MIN 5 s / CAP 15 s / 3 s fade-out, random 400-item art warm) is in **mm-warm.md → Warm gate**.

- While `bz_warm_gate` is set, `BezelGlobalBackdrop` (inside `BezelBlack`) is hidden so Music/Videos first paint is solid black under the splash, not the glow backdrop flash.
- `Home.xml` onload still seeds Tuner, starts `bz_flip.py`/`bz_precache.py`, and runs `bz_cmd.py start` (MM-first: `bz_mmstartrow`/`bz_mmstartsec` from `bz_at_mmdef`, `bz_mmstart`, `bz_nav`, Music → artists underlay). `start` waits for `bz_splash_done`, which the warm gate sets on its fade-out dismiss.

Related: mm-warm.md · mm-list.md · section-transitions.md · dust.md
