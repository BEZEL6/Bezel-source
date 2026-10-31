# FORK 10 — 5.33.10 (Oct 29 2026)
Rob t130: change logs + milestone for each version in a Tuner menu button.
- Tuner: new head **ABOUT / VERSIONS** (skin bool `bz_topen_about`, var `BzTSec_about`), placed after SYSTEM, before ALL. 10 btn rows (newest first) 5.33.10 … 5.33.1; label = version + title, desc = Milestone + changes, onclick noop.
- Infographics 900×580: `media/bezel/info/ver_5_33_{1..10}.png` (timeline, gold dot = that version) + `ver_about.png` on the head.
- Content taken from notes/FORK1–9.md + STATUS.md.
- addon.xml 5.33.9 → 5.33.10 "BEZEL 5.33-fork.10".
- Backup: backups/pre-fork10-1523. XML parse OK. No zip. K40 not touched. ListThumbInfoPanel left as is (Rob: do not restore). Not live-smoked.

- Changelog rows now carry Files: + Risk: lines (break hunting), per Rob t132. Source: notes/BUILD_CHANGES.md. ver_*.png unchanged.
