# Confirm dialog

**Object:** `DialogConfirm.xml` (Kodi yes/no) · include `BzStdProgress` (Includes_BezelDialogs ~514) or `BzRefreshProgress` (Includes_BezelRefresh ~112) · grouplist `9000` with buttons `10` / `11` / `12`  
**Where:** Colour strip at 570,120 (390×900) plus body text in the fanart block (140,220)  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## What it does

**Simple.** Kodi's yes/no question in the Main Menu style: a CONFIRM strip with rows and the message on the left. **No** is the first row and gets focus, so a stray Select never confirms by accident. BEZEL uses it for things like "Remove from library".

**How it works.** The buttons are vertical rows (BETA 2.7: "Buttons are rows; No (10) first = safe default"). When the yes/no shows over Music Information with a progress dialog (refresh), the window uses the refresh layout. Otherwise it uses the standard one.

**Wiring.**
- WindowOpen fade 200 ms cubic out · WindowClose fade 150 ms cubic in · `DepthDialog+`.
- `<defaultcontrol always="true">9000</defaultcontrol>`.
- Layout: `Window.IsActive(musicinformation) + Window.IsActive(progressdialog)` → `BzRefreshProgress`, else `BzStdProgress`.
- `BzStdProgress`: B3 black full-screen dim · strip `$VAR[BzMMStrip]` · "CONFIRM" title `bz_mm34` · grouplist 9000 (top 100, 390×754, vertical) with buttons 10 (No), 11 (Yes), 12 (custom), each 390×58 `bz_mm28` with focus bar `$VAR[BzATHiTex]` / `$VAR[BzMMBarCol]` · heading label 1 · textbox 9 (autoscroll 3000/4000/5000) · progress 20 (only with `progressdialog` and `System.Progressbar`).

## Keys

**Simple.** Up and Down move between No and Yes. Select chooses. Back cancels, which is the same as No.

**How it works.** 9000 is a vertical grouplist, so Up and Down move between rows. Left and Right have no skin handler.

**Wiring.** Kodi's own yes/no ids: 10 = No, 11 = Yes, 12 = custom (hidden when unused). Back = Kodi cancel.

## Where BEZEL calls it

**Wiring.** `bz_ctx.py remove <type> <id>`: yes/no "Remove from library" → on Yes `Dialog.Close(all)` → `VideoLibrary.Remove*` → `Container.Refresh`.

## Related
info-options.md · context-menu.md · dialog-busy.md
