# TV Shows list

**Object:** `MyVideoNav.xml` · list `60` (tvshows / seasons / episodes) · grouplist (Includes_Bezel ~L2638) · ALL `6098` · A–Z `6500` · clearlogo `BzTVClear`
**Where:** Main menu TV → video window
**Last updated:** 2026-11-01 (5.33.292)
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

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/tv-list.md) · [state](../state/tv-list.md) · [motion](../motion/tv-list.md) · [art](../art/tv-list.md) · [input](../input/tv-list.md) · [theme](../theme/tokens.md) · [screens](../port-refs/tv-list/) · [PORT_INDEX](../PORT_INDEX.md)

## L1 titles strip style (5.33.283, current)
On the L1 titles path (`$EXP[bz_vstrip]`: videodb://movies/titles/ or videodb://tvshows/titles/, list view, not grid/actors) list 60 group + ALL row 6098 ride into the colour strip 570..960 (zoom 86.67% @120,120 + slide 510 — same as Music `bz_mstrip`). Strip info pairs / plot / TV clearlogo + fanart title are faded off. Meta lives **inside the fanart stage only** at 150,196: small line (Movies: director · TV: studio), big uppercase title 150,226 (bz_mm34), outlined pills y296 (year, MPAA, runtime[movies], genre), plot textbox 150,346 400×620. Hidden under MM / Info / `..`. Poster group (BezelVPLPoster) scaled 66.67% and moved into the big-album slot 1140,220 600×600 (2:3 kept → 400×600 centred). Nav/focus/MM warm unchanged.

## L1 strip clearart (5.33.285, Rob approved)
On L1 titles strip (`bz_vstrip`): when the item has clearlogo (preferred) or clearart, it replaces the big title in the fanart meta block — image at 150,211, 430×90, left/centre, aspect keep (`BzVStripLogo`). No logo/clearart → bold uppercase text title. Director (Movies) / Studio (TV), pills and plot unchanged. Colour-strip clearart stays off on L1. Hides with the meta group (Info up / MM open / `..`). Poster size unchanged.

**Current (5.33.290, Rob t2221):** TV L1 clearart/clearlogo sits at **150,228, 430×64** (left/centre keep) — between the studio line (196..226) and the pills (296), so it no longer clips the meta. Movies unchanged at 150,211 430×90 (separate control gated `!Container.Content(tvshows)`).

## L1 meta (5.33.291)
Studio is a Bezel pill in the meta pill row (YEAR → STUDIO → MPAA → GENRE), TV only; no separate studio text line. Clearart/clearlogo at 150,200 430×92 (title label when no art), pills at 296. Title + clearart carry L1→L3 (L2/L3 mocks pending 👍).

---

## Strip-list levels L1–L3 (5.33.292, Rob approved build t2226)

### Simple
TV Shows (L1), Seasons (L2) and Episodes (L3) under `videodb://tvshows/titles/` all use the strip-list look: plain list in the colour strip (no thumbnails in rows), meta + description in the fanart stage, big poster on the right unchanged.

### How it works
- `bz_vstrip` covers tvshows **and** seasons/episodes when the path starts `videodb://tvshows/titles/`.
- Clearart (150,200 430×92) uses `BzTVClear` (item clearlogo → tvshow.clearlogo → clearart → tvshow.clearart), so the show's logo carries L1→L3. No logo / `bz_tvclear_off` → show title (`BzTVShowName`) at 150,226.
- Pills row 150,296: S×E (episodes) · Year · Studio (all TV levels) · MPAA · Runtime (movies + episodes) · Genre.
- L2/L3: season/episode name at 150,342; plot slides down 40.
- 5.33.293: TV RECENT (`videodb://recentlyaddedepisodes/`, episodes) also on strip-list (same meta/clearart/SxE+studio pills/plot, poster slot).
- Other TV pills (WATCHING, YEARS, ACTORS, GENRES) keep the old strip layout.

## Strip-list coverage (5.33.294)
bz_vstrip (L1 strip-list) now covers every pill path once the list holds titles: Movies TITLES, RECENTLY ADDED, YEARS, ACTORS, SETS, GENRES; TV SHOWS (+L2 seasons/L3 episodes), WATCHING, YEARS, ACTORS, RECENT, GENRES. Gated on Container.Content(movies / tvshows|seasons|episodes), so category folder lists (year/actor/genre/set names) keep the old layout.

## Folder-name levels (5.33.295)
Year/actor/genre/set/tag name rows (Content years/actors/genres/sets/tags under videodb://movies/ or tvshows/) use strip-list via `bz_vfold` ⊂ `bz_vstrip`; folder name shows as title, no clearart/pills unless present.

## Strip-only list (5.33.298)
List 60 is always the colour-strip list — the old full-size off-strip list is parked at `/workspace/b401/parked_old_list/` (RESTORE.md). Every list view (Music L1–L3, Movies/TV, Music root, sources, files, non-library) draws in the strip: the list group is laid out 450×1038 at x120/y120 and always shrunk 86.67% (center 120,120) + slid 510 → on screen x570–960, y120–1020 (390×900, fills the strip, ~13.8 rows of 75). Grouplist clip (t4533) is 450×1038 so nothing paints past y1020. ALL row 6098 always rides the same shrink/slide. Left still goes to FULLSCREEN 6886 first on Music (5.33.297); Up/Down wrap to 6097/6098 unchanged; A–Z bars 6100/6500 stay at x78.

## 5.33.334 — list flush in strip (t2443)
- Measured on 333: strip x 570–959, top 120; video list highlight x 563–951 (7 px left of the strip). Video list group + ALLROW 6098 slide 510 → 517 (same as Music 5.33.304). Shots `audit_settings_levels/tv/L2.png` (before) / `334_L2.png` (after).
- L3 (seasons): the `..` parent row draws above the strip at y≈45 (outside strip top 120). Flagged, not fixed (clip/parent-row logic, see AUDIT.md).
- No leftover old meta found in the colour strip at L1–L3 (left panel: clearlogo, pills, plot, season label only).

## 5.33.337 (t2458): seasons `..` above the strip (STILL OPEN)
- Added `!ListItem.IsParentFolder | !$EXP[bz_allpull120]` visibility guards to the BezelVPLRows label and to the non-music labels in the main list itemlayouts. The `..` is still drawn at top (shot `tv/337_L3_up.png`). The source is not yet identified; it may be a different control from the row labels.

## 5.33.338 (t2458): seasons `..` above the strip, FIXED
- Cause: in L3 seasons the list is slid up 120 px (bz_allpull120) to hide the stock *All row. That also pulled the `..` row to about y45, above the strip, which starts at 120.
- Fix: a group-level item guard in every list-60 item/focused layout, next to the artist-albums one: `<visible>!ListItem.IsParentFolder | !Container.Content(seasons)</visible>`. Same pattern as L2 artist albums. Label-level guards and `$EXP[bz_allpull120]` inside the layout did not apply.
- Bezel already skips past the parent row: Up from SEASON 1 goes to ALL SEASONS (6098). L2 TV shows still shows `..` as the first row inside the strip (unchanged).
- Shots: tv/338_L2.png, tv/338_L3.png, tv/338_L3_up.png
- Note: until 338, the 337 smokes used ReloadSkin without copying to the deployed addon (/tmp/bz2home/.kodi/addons/skin.bezel2). After an XML edit, copy xml/ there before ReloadSkin, or use r_live.sh.
- 5.33.342: The seasons `..` hide (338) now also requires System.GetBool(videolibrary.showallitems). With Kodi's All row the list pulls up and `..` stays hidden. Without it (setting off), `..` shows in the top slot instead of leaving a blank row. Container(60).ListItemAbsolute refs do not resolve inside itemlayouts, which caused a regression (`..` drawn above the strip). Gap: flatten=never + single season would still hide `..` (no such show in library).
- 5.33.343: TV episodes (L3 + recent episodes), strip-list mode. The old 3.5.6 info pairs, divider, Description label and plot no longer draw over the list (!$EXP[bz_vstrip]); meta and plot stay on the fanart stage, and the drum thumbs are unchanged.
