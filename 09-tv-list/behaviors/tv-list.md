# TV Shows list

**Object:** `MyVideoNav.xml` · list `60` (tvshows / seasons / episodes) · grouplist (Includes_Bezel ~L2638) · ALL `6098` · A–Z `6500` · clearlogo `BzTVClear`
**Where:** Main menu TV → video window
**Last updated:** 2026-10-31
**Status:** Live in 5.33.207. Shares the Movies list nav (edge-to-ALL, no wrap, Left/Back → MM). Seasons never rest on `..`. Clearlogo/title sits on the colour strip with Year/Genre underneath. Known open issue: the Movies→TV highlight can jump back to Movies. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## Open

### Simple
TV on the main menu (or one of its pills) opens your shows behind the menu, then fades them in.

### How it works
1. The MM row sets `bz_navroot` to `videodb://tvshows/titles/`.
2. It then runs `bz_cmd.py go` with that path.
3. The video window loads behind the menu, held hidden (`bz_secload`) until the list and focused art are in, with a 3 s cap.
4. The MM then closes and the section fades in once (400 ms, `bz_secfade`).
5. If MM warm already put this exact list under the menu, the menu just closes.

Pill subs come from `bz_mm.py SUBS`. See mm-warm.md → Section enter / exit, and section-transitions.md.

Pills: SHOWS → WATCHING → YEARS → ACTORS → RECENT → GENRES.

### Wiring
| Item | Value |
|---|---|
| GO | `SetProperty(bz_navroot,videodb://tvshows/titles/,home)` · `RunScript(bz_cmd.py,go,videodb://tvshows/titles/)` |
| SUBS | `tvshows/titles/`, `inprogresstvshows/`, `tvshows/years/`, `tvshows/actors/`, `recentlyaddedepisodes/`, `tvshows/genres/` |

---

## List 60 navigation

### Simple
- **Up / Down** move through the list. At the top or bottom edge, focus jumps to the **ALL** row if it's showing. Otherwise it stays put and doesn't wrap around to the far end.
- **Left** opens the main menu whenever the A–Z bar isn't on screen.
- **Back** steps out of folders, and at the section's home level it opens the main menu.

### How it works
- **Edges and wrap:**
  - List 60 sits inside a vertical grouplist that's 450×900 with a true clip. The grouplist owns onup/ondown, because Kodi overwrites a single child's nav.
  - At an edge, the grouplist sends focus to ALL `6098` when that row is visible. Otherwise it only writes the marker props `bz_topedge` / `bz_bottomedge`; no script reads them.
  - Kodi's native wrap is caught by `bz_flip.py`. When a poll sees the list jump from the top row to the bottom, it focuses ALL if that's shown, or snaps back to the top row (`SetFocus(60,0,absolute)`).
  - A folder change (open/Back) is never counted as a wrap.
- **Left:**
  1. `bz_vback` set (video back-face) → `bz_vback_close`.
  2. Otherwise, if `!Control.IsVisible(6500)` and `$EXP[bz_navok]` → `bz_nav=true` (MM).
- **Right:** `bz_vback` → 6291. If the grid entry 6600 is visible → `bz_cmd gridenter`.
- **Back, first match wins:**
  1. `bz_vback` → close the back-face.
  2. `bz_msret=1` on `sources://` → `ActivateWindow(1117)`.
  3. MM open → clear `bz_nav`/`bz_navtune`/`bz_navbez`.
  4. `bz_atroot` + navok → `bz_nav=true`.
  - Otherwise → 6299, which is Kodi's normal parent-folder Back.
- **Root arm:**
  - `bz_atroot` needs `bz_rootarm`. `bz_flip` sets that once the folder has shown for 0.6 s and is one of the section ROOTS, or equals `bz_navroot` (which also sets `bz_atnavroot`).
  - So a fast Back-Back from a subfolder doesn't overshoot into the MM.
  - `$EXP[bz_navok]` = `bz_navlock` empty + `bz_navgrace` empty + `bz_nav`≠true.

### Wiring
| Handler | Value (MyVideoNav.xml, Includes_Bezel ~L2638–2650) |
|---|---|
| grouplist onup | `Control.IsVisible(6098)` → 6098 · else `SetProperty(bz_topedge,1,home)` |
| grouplist ondown | `Control.IsVisible(6098)` → 6098 · else `SetProperty(bz_bottomedge,1,home)` |
| onleft | `bz_vback` → `bz_vback_close` · `!Control.IsVisible(6500)` + `$EXP[bz_navok]` → `SetProperty(bz_nav,true,home)` |
| onright | `bz_vback` → 6291 · 6600 visible → `RunScript(bz_cmd.py,gridenter)` |
| onback | order above; fallback 6299 |
| Wrap catch | `bz_flip.py` ~L333–345 (`sw_top` / `sw_prev`; 0.8 s after a folder change) |
| Root arm | `bz_flip.py` ~L711 `bz_rootarm` · `bz_atroot` Includes_Bezel ~L2323 |

---

## ALL row (6098)

### Simple
At the bottom of an album, season, or disc list there's an **ALL** row that opens everything at once. Up from it goes back to where you were.

### How it works
- `6098` is shown by `$EXP[bz_allrow]` when the MM is closed. It slides down by NumItems×60 so it sits under the last row.
- Select runs `bz_cmd allrow`. That opens the stock "All" node (`<path>-1/`), keeps the query, and stores `bz_allret` so Back from All lands on the ALL row.
- When `bz_flip` sends focus here after a wrap, it stores `bz_allup`, the row count. ALL's onup then restores that row with `SetFocus(60,n,absolute)`.
- TV seasons never rest on `..`: they open on the first real season, and Up off it goes to ALL SEASONS.

### Wiring
| Handler | Value |
|---|---|
| visible | `$EXP[bz_allrow] + !$EXP[bz_navmenu]` |
| onup | `bz_allup` set → `SetFocus(60,$INFO[Window(Home).Property(bz_allup)],absolute)` · else 60 |
| ondown | noop |
| onleft | `$EXP[bz_navok]` → `bz_nav=true` · else 6996 |
| onclick | `RunScript(bz_cmd.py,allrow)` |
| onback | 60 |

---

## A–Z jump bar

### Simple
For long lists, a strip of letters on the left lets you jump by letter. It's letters only, with no dark band behind it. While it's showing, Left uses the bar instead of opening the menu.

### How it works
- Grouplists `6100` (Music artists/songs, only when NumItems > 38) and `6500` (Movies/TV) sit at left 78, top 151. They're hidden while the MM is open.
- `BezelAZFade` is empty (the old `fade_top`/`fade_bottom` were removed Oct 31 2026).

### Wiring
- `6100` visible `!$EXP[bz_navmenu]` + NumItems > 38 · `6500` visible `!$EXP[bz_navmenu]` · left 78 / top 151.
- `BezelAZFade`: empty include.

---

## Seasons

### Simple
Opening a show lands on its first real season, never on the `..` row.

### How it works
- `bz_flip.py`: on a folder change into seasons with the focus on the parent item, it runs `Control.Move(60,1)`.
- Inside an All node, the hidden parent is bounced past.

### Wiring
- `bz_flip.py` ~L323 (`Container.Content(seasons) + ListItem.IsParentFolder` → `Control.Move(60,1)`) · ~L338 (Up off the first season → 6098 / first season).

---

## Clearlogo / clearart (colour strip)

### Simple
The show's logo sits at the top of the colour strip. If there's no logo, the title shows instead. Year and Genre sit underneath without clipping it.

### How it works
- **MM closed:** a single image with fadetime 300, the same as poster browse.
- **MM open:** an A/B lane. `bz_flip.py _ab_clear` drives `bz_clr_a/b`, `bz_clr_side`, `bz_clr_on` and `bz_clr_empty`, with the same settle (0.25 s) and load (0.5 s) as fanart/poster. The XML Visible/Hidden fade is 1500 ms sine inout.
- The title fallback is used when there's no clear art, or when `bz_tvclear_off` / `bz_clr_empty` is set.

### Wiring
| Item | Value |
|---|---|
| Logo / title box | left 600, top 130, height 150 (ends y 280) |
| Info pairs (Year / Genre…) | grouplist left 600, top 290, height 354 |
| Description | divider / label / plot at 652 / 662 / 696 (Movies-aligned) |
| Source | Includes_Bezel t4153 / `BzTVClear` |

Movies poster hold and the fanart bridge don't apply to TV art.

---

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move; at an edge → ALL `6098` if visible, else stay (no wrap) |
| Select | Open season / episode / play |
| Left | `bz_vback` → close back-face · A–Z hidden + navok → MM |
| Right | `bz_vback` → 6291 · grid → `gridenter` |
| Back | back-face → mediasources return → MM close → root (`bz_atroot`) → MM · else parent folder |

## Touch
None specified.

## Related
mm-list.md · mm-warm.md · movies-list.md · section-transitions.md
