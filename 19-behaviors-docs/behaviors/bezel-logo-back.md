# BEZEL logo / Back button

**Object:** `BezelLogo` include (Includes_Bezel ~559) · `BezelLogoButton` include (line 585) with button `6001` · logo spin in `scripts/bz_flip.py` (~917)  
**Where:** Top-left of every BEZEL window, at 28,26 (64×64). Hidden in FullscreenVideo / VideoOSD.  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## The logo

**Simple.** The BEZEL logo sits top-left and takes the skin tint. About every 30 seconds it does one spin.

**How it works.** The logo image takes its colour from `$PARAM[col]` (normally `BzLogoCol`). The spin is a conditional rotate animation that runs while Home prop `bz_biglogo_spin=true`. `bz_flip.py` pulses that prop on a 30 s clock and clears it after 1.2 s, so the 1.1 s animation finishes before the clear. It has no MM gate (t4985), so it spins while the Main Menu is open too. If the prop is still set when the clock fires, the script retries after 2 s instead of stacking a second spin.

**Wiring.**
- Image `bezel/logo.png`, 28,26, 64×64, `colordiffuse=$PARAM[col]`. Visible unless FullscreenVideo or VideoOSD is active.
- Spin: `rotate` 0 → -360, center 60,58, 1100 ms, tween back, easing out, `condition=String.IsEqual(Window(Home).Property(bz_biglogo_spin),true)`.
- `bz_flip.py` ~917: set `bz_biglogo_spin=true` every 30 s, clear after 1.2 s. Retry after 2 s if already set.

## Tap = Back (touch)

**Simple.** Tapping the logo is the same as pressing Back.

**How it works.** `BezelLogo` carries an unnamed button over the logo area that runs `Action(Back)`. It has the same visibility rule as the logo, so it does nothing in fullscreen video.

**Wiring.** Button at 0,0, 120×116, `onclick Action(Back)` (5.33.117 t816).

## Focusable logo 6001

**Simple.** On some screens you can move focus onto the logo and press Select. That steps back one level in the order that fits the screen.

**How it works.** The `onclick` actions are guarded so that only the first matching step runs:
1. Now Playing open (`bz_np`) → close it.
2. Else a video back layer (`bz_vback`) → raise `bz_vback_close`.
3. Else a back layer (`bz_back`) → raise `bz_back_close`.
4. Else focus the list: 60 if visible, otherwise 9000.
5. Else `Action(Back)`.

The close flags are latches that the owning layer watches, so the layer runs its own exit animation instead of the logo cutting it off.

**Wiring.**
- `BezelLogoButton`: 1 px precache image `bz_pc_img` at 0,1079, plus button `6001` 120×116.
- Visible: `!$EXP[bz_navmenu]` and not fullscreen video/OSD. Fades out while `bz_infoup`.
- Nav: `onright`/`ondown` → 60. `onleft` (`$EXP[bz_navok]`) → `SetProperty(bz_nav,true,home)` (opens MM). `onup` → 6001.
- A focus-only logo image shows while `Control.HasFocus(6001)`.

## Related
mm-list.md · dialogue-fs.md · fanart-fs.md · keymaps.md
