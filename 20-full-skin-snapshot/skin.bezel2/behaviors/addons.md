# Add-ons

**Object:** Add-ons hub and browser · Kodi: dialog `1131` (`Custom_1131_BzAddons.xml`, list `9140`), `AddonBrowser.xml` (list `60`, grouplist `9000`), `DialogAddonInfo.xml`, `scripts/bz_set.py` (`adload`, `ago`, `azip`), `bz_cmd.py backdrop`, `BezelFSUnderlay`
**Where:** MM ADD-ONS
**Last updated:** 2026-11-04 · 5.33.473 · **Status:** live · **Lock:** none

## Simple
ADD-ONS opens a Bezel hub styled like Settings: MY ADD-ONS (expands to Video / Music / Program / Services / Skins / All with counts), FROM REPOSITORY, FROM ZIP FILE, SEARCH, and pills for update mode, notifications and unknown sources. A "»" row opens Kodi's add-on browser as a Bezel strip list ("ADD-ONS · N ITEMS"), and Back from there returns to the hub, then to the main menu. Add-on info is a strip too (OPEN, enabled / auto-update pills, configure, update, versions, dependencies, install / uninstall). The browser shows a random backdrop each visit. With music playing, Tab opens fullscreen music over it.

## Feel contract (any framework)

### States
| State | How you get in | How you leave | On screen |
|---|---|---|---|
| Hub | MM ADD-ONS | Back → MM; » → Browser | title + breadcrumb, rows with ▾ / » / pills |
| Browser | » row | Back at root → Hub | strip list, 48 px rows with », random backdrop |
| Add-on info | Select an add-on | Back | strip of actions and pills |

### Timeline
| What | Duration | Curve |
|---|---|---|
| open | 400 fade-in | sine out |
| backdrop | new random image each visit (never the same twice) | — |

### Interruptions
The hub doesn't reopen if you went to the MM, a modal, fullscreen or a plugin path meanwhile.

### Continuity
Under the MM, the last Music / Movies / TV art is held (no blank). The big album stays with music playing.

### Layering
Backdrop < strip < MM / fullscreen.

### Geometry
Hub and browser in the strip column (Settings layout).

### Art
Random image from the skin's backdrop folder (or a pinned one).

### Input
Up / Down move; Select opens / toggles; Left → MM (browser); Right → side menu; Back up / hub / MM; double Select → section menu; Tab → fullscreen music (if playing).

### Speed targets
Counts appear without blocking the list.

### Never
No blank poster / art under Add-ons from the MM (370, 395, 399).

### Acceptance checks
MM → ADD-ONS → MY ADD-ONS ▾ → Video » → browser → Back → hub → Back → MM.

## Kodi implementation (sandbox)

### How it works
- `bz_mm.py` GO addons sets `bz_setopen`, clears `bz_nav`, opens 1131. » rows: `bz_set ago,<path>` closes 1131 and opens `addonbrowser` (path, return); on close `_reopen` brings 1131 back unless `bz_nav` / modal / fullscreen / plugin.
- AddonBrowser: defaultcontrol `always` 60; onload `bz_cmd.py backdrop`; onunload saves `bz_backdrop_last`, clears `bz_backdrop`, `bz_minibig`; list 60 onback at `addons://` (or empty) + `!bz_navmenu` → `bz_nav=true`; onleft `$EXP[bz_navok]` → `bz_nav=true`; onright 9000. `BezelMMFocusBounce*` while the MM is open. `BezelFSUnderlay` at the end of `<controls>` (472).
- Backdrop: `bz_cmd.py backdrop` lists `special://skin/extras/backdrop/`, excludes current + last; `Skin.String(bz_bdimg)` pins one.

### Wiring
| Item | Value |
|---|---|
| Home | `bz_backdrop`, `bz_backdrop_last`, `bz_setopen`, `bz_minibig` |
| Title var | `$VAR[BzAdTitle]` |
| Section menu | `addonbrowser` in SECW → 1119 |

### Kodi workarounds (do not port)
The close-and-reopen hub dance: Kodi's add-on browser is its own window.

## Related
[settings](settings.md) · [context-menu](context-menu.md) · [favourites](favourites.md) · [music-fanart-fs](music-fanart-fs.md)
