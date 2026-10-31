# Home / startup splash

**Last updated:** 2026-10-31 · live tree 5.33.196 warm-gate hang fix

The startup splash is now the **warm gate** of the WARM system. Its full spec (sequence, styling, flags, 5 s cap, fade-out) is in **mm-warm.md → Warm gate**.

- `Home.xml` onload still seeds Tuner, starts `bz_flip.py`/`bz_precache.py`, and runs `bz_cmd.py start` (MM-first: `bz_mmstartrow`/`bz_mmstartsec` from `bz_at_mmdef`, `bz_mmstart`, `bz_nav`, Music → artists underlay). `start` waits for `bz_splash_done`, which the warm gate sets on its fade-out dismiss.

Related: mm-warm.md · mm-list.md · section-transitions.md · dust.md
