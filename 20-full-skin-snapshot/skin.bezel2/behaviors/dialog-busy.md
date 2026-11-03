# Busy dialog

**Object:** `DialogBusy.xml` (Kodi `busydialog`) · label `10` hidden · include `BezelATBusyOpen` (Includes_Tuner line 11)  
**Where:** Over any window while Kodi is working  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## What it does

**Simple.** It is Kodi's "working…" indicator, restyled. It waits a moment before showing, so quick loads never flash it. It stays out of the way during music, video, caching and flips.

**How it works.** The open fade has a Tuner delay. A load that finishes inside the delay closes the dialog before anything is drawn. The visible group then hides itself in every case where BEZEL already shows its own feedback or where a spinner would cover playback. The close fade waits 500 ms, so a busy that blinks off and back on does not flicker. That close fade only runs when no video is playing.

**Wiring.**
- `BezelATBusyOpen`: WindowOpen fade 0→100 over 200 ms, delay from `Skin.String(bz_at_busydelay)`: 1=150 · 2/empty=300 (default) · 3=500 · 4=800 · 5=1200 ms.
- WindowClose: fade 100→0 over 300 ms, delay 500, only when `!Player.HasVideo` (4.0.1 O32).
- Group visible only when all of these hold: CinemaVision not running · startup window not active · `!Player.Caching` · not audio-only playback · `Window(Home).Property(bz_flipping)` empty · no video and not fullscreenvideo · not `[Player.HasMedia` without audio`]`.
- Visible fade 300 ms, `DepthMax`. Label 10 `visible=false`. No BEZEL logo.

## Keys

**Simple.** None. Kodi's own cancel handling applies where Kodi allows it. The np_tab keymap maps Tab/Display in `busydialog`/`busydialognocancel` to `bz_tabq=true`, (keymaps.md). This doc does not trace what reads `bz_tabq`.

## Related
dialog-confirm.md · keymaps.md · skin-settings-tuner.md


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/DialogBusy.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| 10 | label | —,— | —×— | `—/—/—/—` | `false` |

**Source:** `xml/Includes_Tuner.xml` include `BezelATBusyOpen`

_No id’d controls in this file (layout comes from includes)._

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/dialog-busy.md) · [state](../state/dialog-busy.md) · [motion](../motion/dialog-busy.md) · [art](../art/dialog-busy.md) · [input](../input/dialog-busy.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)
