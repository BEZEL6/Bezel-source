# MM auto-hide (5.33.428, fresh)

**Object:** `scripts/bz_flip.py` `mm_autohide` + `$EXP[bz_mmhid]` (Includes_Bezel) + Tuner MAIN MENU > Auto-hide menu (`bz_at_mmhide`)
**Status:** new build, not device-smoked. Replaces nothing (the 5.33.216-397 park-based auto-hide was removed in 398).

**Simple.** After the chosen idle time (Off / 30 s / 1 / 2 / 5 min) the Main menu strip, colour strip and colour backdrop fade out; the art keeps playing. The clear logo (or the title) of the art shown sits on the fanart stage and PRESS ANY BUTTON shows right of the BEZEL logo. Any key brings the menu back on the row you left; that first key only wakes.

**How it works.** Opacity only: `Home.bz_mmhide` drives Conditional fade pairs (1500 ms out / 250 ms back, reversible=false) on group 6894, the MM veil group and BezelGlobalBackdrop. Focus stays on 6996 the whole time. Idle comes from `xbmc.getGlobalIdleTime()`; when it drops, the menu wakes (`bz_mmwake` latch 0.35 s). 6996 Select/Left/Right/Back actions carry `String.IsEmpty(bz_mmhide)` so the wake key does nothing; Up/Down that moved the strip (or left it for the mini player) is undone with `SetFocus(6996,<row>,absolute)`. mm_warm does not warm while hidden or latched.

**Wiring.** Hide only when: setting on, `bz_nav=true`, strip focused, splash done, no Tuner/Settings card/submenu/kset/mmstart/pick/secload, no modal, not fullscreen video. Stage props `bz_mmh_logo` / `bz_mmh_title` refresh every 50 ms while hidden (virtual row: `bz_vart_logo` / `bz_vart_title` from vwarm; else list 60 clearlogo / tvshow.clearlogo / artist.clearlogo / clearart and Label or TVShowTitle). Positions: label 108,36 / 108,58; logo 150,660 640x250 bottom-left keep; title 150,920 (bz_b46 alone, bz_mm24 under a logo).
