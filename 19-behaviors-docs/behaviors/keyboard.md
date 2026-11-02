# Keyboard (DialogKeyboard 10103)

**Object:** `xml/DialogKeyboard.xml` · includes `BzStdKeyboard` (Includes_BezelDialogs), `BzRefreshKeyboard` (Includes_BezelRefresh), `BzStripKeyboard` (Includes_BezelDialogs) · script `scripts/bz_kb.py`
**Last updated:** 2026-11-01 · 5.33.239
**Status:** draft. Strip keyboard smoked headless :77 (type/space/del/caps/done). Not yet seen on Shield.
**Skin:** skin.bezel2

## Simple
On-screen keyboard. Search, sources, renames and most text fields use the Bezel strip keyboard (A–Z / 0–9 / symbols bars left of the colour strip); Music info Refresh uses a 10×10 strip grid; File Manager keeps the stock-style wide keyboard.

## How it works / Wiring (deep)

## Which keyboard shows
- Over Music info (Refresh flow) → `BzRefreshKeyboard` (strip-format 10×10 grid).
- File Manager (`filemanager`) → `BzStdKeyboard` (wide MM block, popup anim) — File Manager left stock by Rob.
- Everywhere else (Search, Add/Edit Source, rename, playlist name, add-on text settings, etc.) → `BzStripKeyboard`: vbar keyboard left of the colour strip, focus on A–Z 9601.

## Strip keyboard essentials
Bars 9601 A–Z / 9602 0–9 / 9603 symbols (wraplists, focus row 5). Select → `bz_kb.py` appends the char via JSON `Input.SendText` (done=false) to the text read from `Control.GetLabel(312).index(1)`. Pills 32 SPACE, 8 DEL, 300 DONE. Caps: Left on the A–Z bar 9601 toggles Home `bz_kbcaps` (letters redraw upper/lower; no caps pill since 5.33.231). Digits use `$NUMBER[n]` labels (a bare number label is read as a localized string id).

## Strip keyboard — How it works (deep)
**Simple.** Three upright drums (letters, digits, symbols) spin under a fixed highlight; Select types the drum's current character into the edit line; three pills below give space, delete and done.

**How it works.**
1. DialogKeyboard opens (`defaultcontrol always` 300, but `onload` moves focus to 9601 whenever the strip variant is in use). The 380-wide panel slides in from +380 x with a fade (300 ms cubic out) and fades out 200 ms on close.
2. Up/Down spins the focused wraplist; focus row is fixed, so the character under the highlight changes, not the highlight.
3. Select on a drum runs `bz_kb.py <bar> <index>`. The script reads the current text from edit 312 (`Control.GetLabel(312).index(1)`), appends the one character (upper-cased on the A–Z bar when `bz_kbcaps` is set), and pushes the whole string back with JSON `Input.SendText` `done=false` — the dialog stays open.
4. Left on 9601 toggles caps (sets/clears Home `bz_kbcaps`); the A–Z labels come from `$VAR[BzKbCase0..25]` so they redraw instantly. Caps is cleared on `onunload`.
5. DONE (300) is Kodi's stock OK id; DEL (8) and SPACE (32) are stock keyboard button ids, so Kodi itself does the edit. Back = cancel (stock).

## Strip keyboard — Wiring (from `Includes_BezelDialogs.xml` L564+, design canvas 1920×1080)
| piece | id | x,y (in group 170,120) | w×h | nav L / R / U / D |
|---|---|---|---|---|
| panel bg | — | 0,0 | 380×900 | `white.png` diffuse `F2140808` |
| title "KEYBOARD" | 311 | 20,14 | 340×40 | font bz_mm24 |
| edit line | 312 | 16,64 | 348×46 | all → 9601 |
| A–Z drum | 9601 | 22,162 | 100×506, item 46 | caps toggle / 9602 / self / self |
| 0–9 drum | 9602 | 136,162 | 100×506 | 9601 / 9603 / self / self |
| #!? drum (`/:._-@\\!#$%&+=?`) | 9603 | 250,162 | 100×506 | 9602 / 300 / self / self |
| SPACE pill | 32 | 26,706 | 110×38 | 300 / 8 / 9601 / 9601 |
| ← DEL pill | 8 | 146,706 | 70×38 | 32 / 300 / 9602 / 9602 |
| DONE pill | 300 | 226,706 | 138×38 | 8 / 9603 / 9603 / 9603 |
| hint label | — | 26,800 | 340×90 | bz_mm14 `AAFFFFFF` |

- Focused drum item: `$VAR[BzATHiTex]` tinted `$VAR[BzATHiCol]`, text `$VAR[BzATHiText]`, font bz_mm34; unfocused drum keeps a `3CFFFFFF` `np_pill32` ghost.
- DONE unfocused is a cream pill (`F0F5EBE1`) with dark text `FF3C0A0A`; SPACE/DEL unfocused `46FFFFFF`.
- Digits use `$NUMBER[n]` labels (a bare number is read as a string id).
- Variant choice lives in `DialogKeyboard.xml` include conditions: `musicinformation` visible → `BzRefreshKeyboard`; `filemanager` visible → `BzStdKeyboard` (+ `Animation_DialogPopupOpenClose`); else strip.
- *Unverified here:* `BzRefreshKeyboard` and `BzStdKeyboard` geometry is not re-read in this pass — see their includes.

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/keyboard.md) · [state](../state/keyboard.md) · [motion](../motion/keyboard.md) · [art](../art/keyboard.md) · [input](../input/keyboard.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)
