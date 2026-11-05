# Keyboard

**Object:** on-screen keyboard · Kodi: `DialogKeyboard.xml` (10103), includes `BzStripKeyboard` (default), `BzRefreshKeyboard` (music info refresh), `BzStdKeyboard` (File Manager), `scripts/bz_kb.py`
**Where:** strip keyboard left of the colour strip (group 170, 120, 380 × 900)
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
Text entry uses the Bezel strip keyboard: three upright drums (A–Z, 0–9, symbols) spin under a fixed highlight, Select types the drum's character into the edit line, and pills give SPACE, DEL, DONE and CANCEL. Left on the letters toggles caps. Music info Refresh uses a 10 × 10 strip grid; File Manager keeps the stock-style keyboard.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Strip keyboard | any text field (search, sources, rename, add-on text) | DONE / CANCEL / Back | panel, title, edit line, 3 drums, 4 pills |
| Caps | Left on the A–Z drum | Left again / close | upper-case letters |
| Refresh grid | music info refresh | same | 10 × 10 grid |
| File Manager | File Manager | same | stock-style keyboard |

### Timeline
| What | Duration | Curve |
|---|---|---|
| open | panel slides in from +380 x with a fade, 300 | cubic out |
| close | fade 200 | — |
| drum spin | per row (list scroll) | — |

### Interruptions
Typing appends to the current edit text; caps clears on close.

### Continuity
Focus starts on the A–Z drum; the highlight never moves, the drum does.

### Layering
Screen < keyboard panel (94 % dark) < drums / pills.

### Geometry
Panel 170, 120, 380 × 900; title 20, 14; edit 16, 64 (348 × 46); drums at x 22 / 136 / 250, y 162 (100 × 506, items 46); pills y 706: SPACE 20 (78), DEL 104 (78), DONE 188 (82), CANCEL 276 (86); hint 26, 800.

### Art
Focused drum item = Bezel highlight; unfocused drums a 24 % pill ghost; DONE cream pill with dark text; SPACE / DEL 27 % white.

### Input
Up / Down spin; Left / Right move between drums and pills (Left on A–Z = caps); Select types / runs a pill; Back cancels.

### Speed targets
Each character appears at once.

### Never
No bare-number labels (Kodi reads them as string ids): digits use number formatting.

### Acceptance checks
Search → type "abc 1" → DONE → search runs; Back → cancelled.

## Kodi implementation (sandbox)

### How it works
#### Simple
On-screen keyboard. Search, sources, renames and most text fields use the Bezel strip keyboard (A–Z / 0–9 / symbols bars left of the colour strip); Music info Refresh uses a 10×10 strip grid; File Manager keeps the stock-style wide keyboard.

#### How it works / Wiring (deep)

#### Which keyboard shows
- Over Music info (Refresh flow) → `BzRefreshKeyboard` (strip-format 10×10 grid).
- File Manager (`filemanager`) → `BzStdKeyboard` (wide MM block, popup anim) — File Manager left stock by Rob.
- Everywhere else (Search, Add/Edit Source, rename, playlist name, add-on text settings, etc.) → `BzStripKeyboard`: vbar keyboard left of the colour strip, focus on A–Z 9601.

#### Strip keyboard essentials
Bars 9601 A–Z / 9602 0–9 / 9603 symbols (wraplists, focus row 5). Select → `bz_kb.py` appends the char via JSON `Input.SendText` (done=false) to the text read from `Control.GetLabel(312).index(1)`. Pills 32 SPACE, 8 DEL, 300 DONE, 9604 CANCEL (5.33.354). Caps: Left on the A–Z bar 9601 toggles Home `bz_kbcaps` (letters redraw upper/lower; no caps pill since 5.33.231). Digits use `$NUMBER[n]` labels (a bare number label is read as a localized string id).

#### Strip keyboard — How it works (deep)
**Simple.** Three upright drums (letters, digits, symbols) spin under a fixed highlight; Select types the drum's current character into the edit line; three pills below give space, delete and done.

**How it works.**
1. DialogKeyboard opens (`defaultcontrol always` 300, but `onload` moves focus to 9601 whenever the strip variant is in use). The 380-wide panel slides in from +380 x with a fade (300 ms cubic out) and fades out 200 ms on close.
2. Up/Down spins the focused wraplist; focus row is fixed, so the character under the highlight changes, not the highlight.
3. Select on a drum runs `bz_kb.py <bar> <index>`. The script reads the current text from edit 312 (`Control.GetLabel(312).index(1)`), appends the one character (upper-cased on the A–Z bar when `bz_kbcaps` is set), and pushes the whole string back with JSON `Input.SendText` `done=false` — the dialog stays open.
4. Left on 9601 toggles caps (sets/clears Home `bz_kbcaps`); the A–Z labels come from `$VAR[BzKbCase0..25]` so they redraw instantly. Caps is cleared on `onunload`.
5. DONE (300) is Kodi's stock OK id; DEL (8) and SPACE (32) are stock keyboard button ids, so Kodi itself does the edit. Back = cancel (stock). **Remote path (5.33.354):** Right from #!? → SPACE → DEL → DONE → CANCEL (5.33.357: was landing on DEL). Pill row Left/Right wraps SPACE ↔ CANCEL; Up leaves the row.; CANCEL = `Action(Back)`.

#### Strip keyboard — Wiring (from `Includes_BezelDialogs.xml` L564+, design canvas 1920×1080)
| piece | id | x,y (in group 170,120) | w×h | nav L / R / U / D |
|---|---|---|---|---|
| panel bg | — | 0,0 | 380×900 | `white.png` diffuse `F2140808` |
| title "KEYBOARD" | 311 | 20,14 | 340×40 | font bz_mm24 |
| edit line | 312 | 16,64 | 348×46 | all → 9601 |
| A–Z drum | 9601 | 22,162 | 100×506, item 46 | caps toggle / 9602 / self / self |
| 0–9 drum | 9602 | 136,162 | 100×506 | 9601 / 9603 / self / self |
| #!? drum (`/:._-@\\!#$%&+=?`) | 9603 | 250,162 | 100×506 | 9602 / 32 (SPACE) / self / self |
| SPACE pill | 32 | 20,706 | 78×38 | 9604 / 8 / 9601 / 9601 |
| ← DEL pill | 8 | 104,706 | 78×38 | 32 / 300 / 9602 / 9602 |
| DONE pill | 300 | 188,706 | 82×38 | 8 / 9604 / 9603 / 9603 |
| CANCEL pill | 9604 | 276,706 | 86×38 | 300 / 32 / 9603 / 9603 · `Action(Back)` |
| hint label | — | 26,800 | 340×90 | bz_mm14 `AAFFFFFF` |

- Focused drum item: `$VAR[BzATHiTex]` tinted `$VAR[BzATHiCol]`, text `$VAR[BzATHiText]`, font bz_mm34; unfocused drum keeps a `3CFFFFFF` `np_pill32` ghost.
- DONE unfocused is a cream pill (`F0F5EBE1`) with dark text `FF3C0A0A`; SPACE/DEL unfocused `46FFFFFF`.
- Digits use `$NUMBER[n]` labels (a bare number is read as a string id).
- Variant choice lives in `DialogKeyboard.xml` include conditions: `musicinformation` visible → `BzRefreshKeyboard`; `filemanager` visible → `BzStdKeyboard` (+ `Animation_DialogPopupOpenClose`); else strip.
- *Unverified here:* `BzRefreshKeyboard` and `BzStdKeyboard` geometry is not re-read in this pass — see their includes.

### Wiring
See the detail above.

### Kodi workarounds (do not port)
`bz_kb.py` reads edit 312 and re-sends the whole text with JSON `Input.SendText`: Kodi has no "append character" call. `$NUMBER[n]` labels.

## Related
[search](search.md) · [media-sources](media-sources.md) · [files-filemanager](files-filemanager.md)
