# Media sources

**Object:** `Custom_1117_MediaSources.xml` window `1117` · grouplist `9000` (125,128, 440 wide) with 11 rows `7101–7121` · grouplist `9001` (584,136) with `9101` / `9102` · bounce `6299`  
**Where:** Main Menu row MEDIA SOURCES  
**Last updated:** 2026-11-02 · 5.33.365
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## Open / close

**Simple.** MEDIA SOURCES in the Main Menu opens a BEZEL page with Videos, Music and Pictures sources and their library tools. Pick one to open Kodi's sources for it. Back from there returns to this page on the same row. Back here opens the Main Menu.

**How it works.** Picking a row stores which row it was (`bz_msfocus`) and a return flag (`bz_msret=1`), then opens the Kodi window with `return`. That media window's `onback` checks for the flag and a `sources://` path and re-opens 1117. On load, 1117 clears the flag and restores focus on a 1-second AlarmClock, so the focus lands after the rows exist. With no stored row, focus goes to 7101.

**Wiring.**
- MM row → clear `bz_nav` / `bz_navtune` / `bz_navbez` → `ActivateWindow(1117)`.
- `<defaultcontrol always="true">7101</defaultcontrol>`, `menucontrol` 9001, `BezelSecFadeIn` (5.33.177).
- `onload`: `ClearProperty(bz_msret)`. `bz_msfocus` set → `AlarmClock(bzmsf,SetFocus($INFO[bz_msfocus]),00:01,silent)`, else `SetFocus(7101)`.
- `6299` bounce → `bz_msfocus` or 7101.
- Return: Includes_Bezel lines ~1518 and ~2664, media-window `onback` with `bz_msret=1` + `FolderPath` starting `sources://` → `ActivateWindow(1117)`.

## Layout

**Wiring.** `BezelStdFrame`, title "Media sources", label "Settings / Media sources". DETAIL panel visible while `ControlGroup(9000).HasFocus` shows `$VAR[BzMSHead]` / `$VAR[BzMSBody]` for the focused row.

## Keys

**Simple.** Up and Down move through the rows and wrap. Left or Right goes to CANCEL / SETTINGS. Back opens the Main Menu.

**Wiring.**
- 7101: `bz_msret=1`, `bz_msfocus=7101`, `ActivateWindow(Videos,sources://video/,return)`. `onup` 7121 (wrap), `ondown` 7102, left/right 9001. Rows: 7101 VIDEOS SOURCES… · 7102 Update library · 7103 Clean library · 7104 Export library · 7105 Import library (`MediaSettings,library`) · 7111 MUSIC SOURCES… (`Music,sources://music/,return`) · 7112–7115 the same four library rows for music · 7121 PICTURES SOURCES… (`Pictures,sources://pictures/,return`). I did not re-trace the per-row actions of 7102–7104 / 7112–7114 for this doc.
- Every button in 9000: `onback` → `SetProperty(bz_nav,true,home)` (BUG-024).
- 9001: `9101` CANCEL → `Close` · `9102` SETTINGS → `ActivateWindow(MediaSettings)`.

## Related
mm-list.md · filebrowser.md · files-filemanager.md

## 5.33.220 — Warm strip Media Sources (current state)
- Custom_1117 is still a window (6299 bounce, msret/msfocus kept) but now uses the strip chrome: VIDEOS ▾ / MUSIC ▾ / PICTURES ▾ (bz_msx), each with SOURCES » (count), library actions and an UPDATE ON START pill; ADD SOURCE » (sources://video/ with msret); LIBRARY SCAN pill (QUIET/SHOW). Wrap is 7100↔7131 and the default focus is 7100. Menucontrol 9001 has been removed.
- Back → MM unchanged. FileBrowser / add-source dialog are still stock.

## Focus highlight + pills (5.33.221)
- Focused row uses the **same highlight bar as Bezel lists**: full-row image 390×48, `$VAR[BzATHiTex]` tinted `$VAR[BzATHiCol]` (follows Tuner highlight shape/opacity); focused label colour `$VAR[BzATHiText]`.
- List rows (1131 list 9140, 1130 list 9130/9131, AddonBrowser list 60) put the bar in `focusedlayout` behind `Control.HasFocus(<list>)`.
- Button/radiobutton rows (1117, DialogAddonInfo) use `<texturefocus/>` plus a sibling image `visible Control.HasFocus(<id>)` — a `$VAR` inside button `texturefocus` did not render in these dialogs.
- Value pills (‹ AUTO ›, ‹ OFF ›, radios): Bezel pill `bezel/np_pill32.png` border 12 — 33FFFFFF fill for value / radio off, E6FFFFFF for radio on. Old `mm_pill_ol` outline and `ad_pill_on/off` are no longer used.
- Zip / repository / category follow-ons (AddonBrowser strip) get the same bar. File manager stays stock.

## Underlay + navigation (5.33.228, current state)
- **Art behind the strip:** 1117 draws the held MM warm lane (`bz_fan_a` / `bz_fan_b` by `bz_fan_side`, shown while `bz_fan_on` is set) at 120,120 840×900, right after `BezelStdFrame`, under the strip chrome. Same Tuner Fanart opacity (`bz_at_fanop`) as BezelFanartLayer. Not gated on `bz_navmenu`, so the art the MM row showed stays up after the window opens (it used to go black: StdFrame cover + empty `bz_backdrop`).
- **Keys:** every row has explicit `onup`/`ondown` with `bz_msx` conditions. The grouplist of wrapper groups did not move focus on its own (Down was stuck on VIDEOS). Order: VIDEOS → (its 6 rows if open) → MUSIC → (6 rows if open) → PICTURES → (SOURCES if open) → ADD SOURCE → LIBRARY SCAN → wraps to VIDEOS. Select on a header opens or closes its rows. Left/Right do nothing except change ‹VALUE› pills.
- **Keyboard:** no row in 1117 opens the on-screen keyboard. The Add Source dialog (DialogMediaSource) path/name fields open the Bezel **strip keyboard** — see the section below and `keyboard.md`.

## Add Source strip keyboard (5.33.229, current state)
**Simple.** Editing a path or the name in the Add Source dialog no longer opens Kodi's full-screen keyboard. A dark vbar keyboard slides in to the LEFT of the colour strip (x170–550, y120–1020); the strip stays put and the MM art stays behind.

**How it works.** `DialogKeyboard.xml` picks `BzStripKeyboard` while `Window.IsVisible(mediasource)` (and not musicinformation). Three wraplist bars float with the focused letter big in the centre: A–Z `9601`, 0–9 `9602`, symbols `9603` (`/ : . _ - @ \ ! # $ % & + = ?`). Up/Down slides a bar, Left/Right switches bars. Select runs `scripts/bz_kb.py <a|n|s>,<index>`, which reads the edit text (`Control.GetLabel(312).index(1)`) and sends text+char with JSON `Input.SendText` (done=false). Pills: SPACE (Kodi `32`), ← DEL (Kodi `8`), DONE (Kodi `300`, closes and writes the field). Caps: Left on A–Z `9601` toggles Home `bz_kbcaps` (letters show case; cleared on unload; caps pill removed 5.33.231). Back = cancel.

**Wiring.** Focus on open: `onload SetFocus(9601)` (mediasource only). Nav: A–Z Left = caps toggle (stays on bar); symbols Right → DONE (Select it to return to the strip); pills Up → bars, Down → bars (SPACE→A–Z, DEL→0–9, DONE→symbols); SPACE Left → DONE. Edit `312`/heading `311` are Kodi's own. Slide-in 300ms from the strip edge + fade; fade-out 200ms. Stock popup open/close anim skipped for mediasource. Source generated by `/workspace/b401/gen_kb229.py` into `Includes_BezelDialogs.xml`. Every other keyboard use is unchanged (BzStdKeyboard / BzRefreshKeyboard).

## Open draw (5.33.233, current state)
- No window-level fade (232). The strip group fades in 200 ms; the MM lane art draws at full on frame 1.
- Lane images load synchronously (no `background="true"`) and sit on an opaque black cover (visible while `bz_fan_on`), so StdFrame's `bz_backdrop` image never blinks through on open.
- Right panel (x1010+) shows no art (`showart=false`).

## SOURCES follow-on + art hold (5.33.232, current state)
- **SOURCES »** (7101 video / 7111 music / 7121 pictures) no longer opens Kodi's stock sources window. It sets `bz_srcpath` (`sources://video|music|pictures/`), `bz_srcwin` (Videos/Music/Pictures), `bz_srclab`, then opens dialog **1132** (`Custom_1132_BzSources.xml`): Warm strip box, title SOURCES, sub "MEDIA SOURCES · <type>", list 9150 filled from `<content>$INFO[bz_srcpath]</content>`, Bezel hi bar, » per row. 1132 has no window fade, no full-screen dim and no strip chrome of its own: 1117's strip chrome stays up underneath, only 1117's title/sub labels and grouplist 9000 hide while 1132 is active (5.33.243 — no blink, no double dim).
- Select a source → sets `bz_msret=1`, `ActivateWindow(<bz_srcwin>,<source path>,return)`, THEN `Dialog.Close(1132)` (nav before close, 5.33.243 — 1117 never draws a frame between); Back from that media window returns to 1117 (existing msret path). Back in 1132 → 1117 (same row).
- Edit / remove a source = Context Menu on the row (stock context menu — not yet strip).
- **Art:** window-level `BezelSecFadeIn` removed and the 200 ms WindowOpen fade moved to the strip group only, so the held MM fanart (bz_fan_a/b) draws full on frame 1 (no fade-from-black flash). Right art slot 1140,220 600×600 now held too: `bz_pos_a/b` by `bz_pos_side` while `bz_pos_on`, else music `bz_cov_a`, art_mask + frame.png.

## Underlay = MM look (5.33.234, current state)
- Fan lane (bz_fan_a/b) + right poster lane sit in one group dimmed by **MM dim** (`bz_at_mmdim`, time 0) — same brightness as with MM open, no change on open.
- Fan lane carries the default Fanart opacity 50% (empty/6) like BezelFanartLayer (was missing → art jumped brighter on open).
- Strip group WindowOpen fade (200ms) removed — strip is up on frame 1. No window-level fade. K40 gates not used.

## Source context menu (current, 5.33.242)
Menu on a source row (1117 / SOURCES 1132 / Pictures sources root) now draws Kodi's context menu in the Warm strip: `DialogContextMenu` with `$EXP[bz_ctxwarm]` hides BezelStdFrame, shows `BezelMMStripChrome` (w 450) at 570,120 titled with the item + `SOURCE · OPTIONS`, and slides grouplist 996 to 570,232. Rows are still Kodi's own (Edit source / Remove source …) — whatever Kodi offers for that list.

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/media-sources.md) · [state](../state/media-sources.md) · [motion](../motion/media-sources.md) · [art](../art/media-sources.md) · [input](../input/media-sources.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## 5.33.337 (t2458)
- ADD SOURCE (7130) now opens the stock "Add <type> source" dialog directly: `bz_set.py msadd,<m|p|v>` uses the expanded section, finds the `add` item in sources://, selects it, waits for the dialog to close, then goes back to 1117 with focus on 7130. Shots: `skip/337_addsource_dialog.png`, `skip/337_addsource_back.png`.
- IMPORT LIBRARY (7105) stays SKIP. Kodi has no ImportLibrary builtin, and the import runs only as a stock settings action through the file browser (it opens Settings/Media). Shot: `skip/337_import_library_stock.png`.

## Keyboard + CLEAN warning (5.33.354, current state)
- **Keyboard:** every text field in the Media Sources flows — ADD SOURCE path + name and EDIT SOURCE (context → Edit source) path + name in DialogMediaSource — opens the Bezel **strip keyboard** (DialogKeyboard picks `BzStripKeyboard` everywhere except Music Refresh and File Manager). No stock keyboard is left in these flows. The path **Browse** button still opens Kodi's stock file browser (a folder picker, not a keyboard).
- **Remote path on the keyboard:** bars A–Z → 0–9 → #!? ; Right from #!? (bar 3) → **← DEL** → **DONE** (save/enter) → **CANCEL** (new pill 9604, `Action(Back)`). Back also cancels. See `keyboard.md`.
- **CLEAN LIBRARY** (7103 video / 7113 music) runs `bz_set.py msclean,<video|music>`: Yes/No dialog "CLEAN VIDEO|MUSIC LIBRARY" first; only YES runs `CleanLibrary(<type>)`. NO / Back does nothing.

## Section options (5.33.356, current state)
Rows per section (▾ open):
- **VIDEOS:** SOURCES » (7101) · **ADD SOURCE » (7107)** · **REFRESH LIBRARY** (7102, `UpdateLibrary(video)`) · CLEAN LIBRARY (7103, Yes/No) · EXPORT LIBRARY (7104) · IMPORT LIBRARY (7105, still stock Settings — SKIP) · UPDATE ON START (7106).
- **MUSIC:** SOURCES » (7111) · **ADD SOURCE » (7117)** · **REFRESH LIBRARY** (7112) · CLEAN LIBRARY (7113, Yes/No) · EXPORT (7114) · IMPORT (7115, SKIP) · UPDATE ON START (7116).
- **PICTURES:** SOURCES » (7121) · **ADD SOURCE » (7122)**. No library scan/clean.
- Bottom rows unchanged: ADD SOURCE (7130, adds to the open section, default Videos) · LIBRARY SCAN pill (7131).
- Section ADD SOURCE runs `bz_set.py msadd,<v|m|p>,<row id>`; after the Add Source dialog closes, 1117 returns with focus on that same row (`bz_msfocus`).
- **EDIT / REMOVE:** on a source row in SOURCES 1132 (or the sources root), MENU opens the Warm-strip context menu (Edit source / Remove source, Kodi's own rows). 1132 footer hint now reads "MENU edit · remove". Edit fields use the strip keyboard.
- Down order inside a section: SOURCES → ADD SOURCE → REFRESH → … ; Up reverses. Detail panel (`BzMSHead/BzMSBody`) has text for 7107/7117/7122.


## Add Source dialog (DialogMediaSource, 5.33.359 — mock A)
Every control sits in the Warm colour strip (x570, 390×900) over the fanart stage, same look as Media Sources 1117 / SOURCES 1132.
Top to bottom: title (2) · NAME edit (12) · PATHS list (10, scrollbar 60) · divider · BROWSE » (11) · ADD PATH + (13) · REMOVE (14) · divider · OK (18) / CANCEL (19) pills.
Rows use the Warm highlight colour (BzATHiCol) on focus, dark text. Pills: translucent round pill, white when focused.
Nav: Up/Down runs NAME → PATHS → BROWSE → ADD PATH → REMOVE → OK/CANCEL and wraps (NAME Up → CANCEL, pills Down → NAME). Left/Right only moves between OK and CANCEL (wraps); elsewhere no-op. Default focus NAME.

## Add Source dialog (5.33.360)
DialogMediaSource = MS Warm strip at 570,120: BezelMMStripChrome (bar opacity/shadow/bezel), NAME/PATHS/BROWSE/ADD PATH/REMOVE rows with BzATHiTex hi bar, OK/CANCEL np pills. No own dim/fanart: 1117 art stays under; 1117 rows/labels hide while mediasource is active.

## Add Source dialog — current state (5.33.363)
- Opens over 1117 or over Videos (sources://). Over 1117: 1117's own underlay + strip chrome show; the dialog draws no underlay or chrome (no double opacity). Not over 1117: the dialog draws the 1117 underlay itself (StdFrame, held fanart lane bz_fan_a/b at MM dim + fanart opacity, art) plus strip chrome (box).
- Title: ADD VIDEO SOURCE (etc., from control 2), font bz_mm28.
- Right art: a movie/TV poster (bz_pos_a/b) sits in the real poster slot, x990 y120, 600×900, same as Videos/1117, with a white frame. When there's no poster but music art (bz_cov_a), the album cover goes in the square album slot, x1140 y220, 600×600.
- StdFrame's thin underline (x1040 y998) is covered in this dialog, so no white bar shows under the art.

## SOURCES list click (5.33.363, current state)
- SOURCES » (7101/7111/7121) opens 1132, which lists **every** source for that type (multi-source, filled from sources://<type>/).
- Select on a source: `bz_msret=1` → `Dialog.Close(1132,true)` → `ActivateWindow(<win>,<source path>,return)`. The close has to come first: Kodi refuses ActivateWindow while modal 1132 is open (before .363, clicking a source did nothing). Back from the media window returns to 1117.
- MENU on a source row = Kodi's source context menu (edit/remove).


## SOURCES per-source dropdown (5.33.364, current)
**Simple.** In SOURCES (1132), Select on a source row opens a Warm dropdown in the same strip. The source name is the strip title (colour strip label, bz_mm34) with "<TYPE> SOURCE · OPTIONS" under it. Rows: **OPEN »**, **RENAME**, **REMOVE**, **REFRESH** (REFRESH hidden for Pictures). No EDIT.
**Wiring.** list 9150 onclick → bz_srcsel/bz_srcname, `bz_srcdd=1`, SetFocus(9161). Grouplist 9160: 9161 OPEN (`bz_set.py mssrc,open`: close 1132, ActivateWindow(<win>,path,return)), 9162 RENAME (keyboard → Kodi context Edit source → name field 12 → OK 18), 9163 REMOVE (Kodi context Remove source → Warm Yes/No), 9164 REFRESH (`UpdateLibrary(video|music,path)`; `!String.IsEqual(bz_srcwin,Pictures)`). Back on any row → `ddback` (reopens 1132 on the list). bz_srcdd cleared on load/unload. Needs FULL restart (.py).

## Add Source — Set content + open (current, 5.33.365)
- Videos Add Source → OK → **Set content** is `DialogContentSettings.xml` (Bezel Warm): BzMSUnderlay + MM strip chrome at 570,120; settings rows (Kodi tpl ids 7/8/9/12/13, group 5) in the colour strip with BzATHiTex hi bar; OK/CANCEL/extra (28/29/30) as np pills; title id 2 uppercase in the strip. No stock/Estuary fallback.
- Open: DialogMediaSource and DialogContentSettings have **no window-level fade** — underlay (black base, StdFrame, held fanart/poster) draws at full on frame 1; only the strip group fades in (400ms sine). Underlay art loads sync (`background="false"`) so first open has no late art.
- Poster: StdFrame underline is off in BzMSUnderlay (`showline=false`); no black cover bar under the poster.
