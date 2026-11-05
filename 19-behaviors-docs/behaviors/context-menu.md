# Section menu (context)

**Object:** Bezel's context menu for non-library screens · Kodi: dialog `1119` (`Custom_1119_SecCtx.xml`), grouplist `9000`, rows `7901`–`7947`, `scripts/bz_ctx.py`, `scripts/bz_dtap.py`; source-row variant in `DialogContextMenu.xml` (`$EXP[bz_ctxwarm]`)
**Where:** Programs, Games, Add-ons, playlists, PVR, Pictures; source rows (Media sources, Pictures sources root)
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
Bezel replaces Kodi's context menu. Menu / C, long-press or double-Select opens the menu that fits the screen: Options + Info in Movies / TV / Music ([info-options](info-options.md)), this section menu in the other sections, and Kodi's own menu in the file pickers. It uses the same look as Options + Info: fanart crop on the left, title, rows in the strip column. Each screen shows only its own rows. Up / Down stop at the ends, Left / Right / Back close, Select runs the row on the item underneath.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Open | Menu / long-press / double Select | Back / Left / Right / a row | mask + logo + 450 fanart crop + title + rows |
| Source-row menu | Menu on a source row | Back | Kodi's source actions inside the strip chrome |

### Timeline
No pop-in animation; the row action fires right after the menu closes.

### Interruptions
If Kodi's own context menu opens first, it is closed before Bezel's opens.

### Continuity
The action always lands on the item that was focused when the menu opened.

### Layering
Screen < black left mask < fanart crop < rows < confirm dialogs.

### Geometry
Fanart crop 450 wide; title 150, 150; rows 582, 166; mask −60, −60, 630 × 1200 (on here, off in Info).

### Art
Item fanart crop.

### Input
| Action | Result |
|---|---|
| Up / Down | move (stops at the ends) |
| Left / Right / Back | close |
| Select | the row's action |

### Speed targets
—

### Never
Never Kodi's own context menu in Bezel screens (noctx), except the file pickers.

### Acceptance checks
Add-ons → Menu on an add-on → Add-on settings works; playlist → Menu → Move up works.

## Kodi implementation (sandbox)

### How it works
- noctx keymap: menu keys → `NotifyAll(bz,bz_ctx)`; handler closes Kodi's `contextmenu` (≤ 40 × 25 ms) then `info()`: filebrowser / filemanager → `Action(ContextMenu)`; SECW not on 1119 → `ActivateWindow(1119)`; else `Action(Info)`.
- Rows: `Dialog.Close(1119,true)` then `AlarmClock(bzsc,<action>,00:00)` on the window underneath. Visibility per `Window.IsActive(...)`.
- defaultcontrol `always` 9000, `DepthDialog+`, rows `BzCIBtn`.
- Source variant (242): `DialogContextMenu` with `$EXP[bz_ctxwarm]` hides `BezelStdFrame`, shows `BezelMMStripChrome` (w 450) at 570, 120.

### Wiring
| Screen | Rows |
|---|---|
| Programs / Games / Add-ons | Open 7901 · Add-on info 7902 · Add-on settings 7903 · Favourite 7904 · Check for updates 7905 · Sort 7906 · Order 7907 · Get more 7908 / 7909 · … |
| Playlists | 7911–7919 (see [playlists](playlists.md)) |
| PVR | Switch 7920 · Programme info 7921 · Record 7922 · Guide 7923 · Play / Recording info / Delete 7924–7926 · Timer edit / info / delete 7927–7929 · Search 7930 · Channel manager 7931 · PVR settings 7932 |
| Pictures | View 7940 · Open folder 7941 · Info 7942 · Slideshow 7943 · Recursive 7944 · Sort 7945 · Order 7946 · Favourite 7947 |
| Favourite rows | `bz_ctx.py fav` |

### Kodi workarounds (do not port)
Closing Kodi's menu after it opens; actions fired by a 0 s alarm so they hit the window underneath.

## Related
[info-options](info-options.md) · [keymaps](keymaps.md) · [favourites](favourites.md) · [pictures](pictures.md) · [playlists](playlists.md) · [media-sources](media-sources.md)
