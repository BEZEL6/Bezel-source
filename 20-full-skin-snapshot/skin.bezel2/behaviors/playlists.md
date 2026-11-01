# Playlists

**Object:** `MyPlaylist.xml` (default `60`, side `9000`: shuffle `20`, repeat `26`, save `21`, clear `22`) · `MyMusicPlaylistEditor.xml` (default `6`, grouplist `9000`, buttons `6`/`7`/`8`, lists `50`/`100`, scrollbars `60`/`61`) · section menu `1119` (7911–7919)
**Where:** Now-playing queue (musicplaylist / videoplaylist) and saved playlists
**Last updated:** 2026-10-31
**Status:** Live in 5.33.207. The queue opens from Up next (1115 6409) or the side Playlist button 612. MM PLAYLISTS opens the saved music playlists. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## Open / close

### Simple
- **PLAYLISTS** on the main menu shows your saved music playlists.
- **Up next** in the music controls (or the Playlist side button) shows what's queued now.
- Back returns to where you came from.

### How it works
- **Saved playlists** are a music-window path, so they open through `bz_cmd.py tomusic` with the normal load-then-close MM handoff (the section stays hidden until the list and art are in, capped at 3 s). After that it's a normal music list 60.
- **The queue window (MyPlaylist):**
  - On load it picks a backdrop, starts `bz_flip.py` if it isn't running, and sets `bz_sway_restart` so the art sway restarts.
  - On unload it saves and clears the backdrop.
  - It fades in with `BezelWindowFade` under `BezelSecDim`.

### Wiring
| Item | Value |
|---|---|
| MM opener | `GO['playlists']`: `RunScript(bz_cmd.py,tomusic,special://musicplaylists/)` |
| Queue openers | 1115 `6409` (Up next) · side button `612` |
| MyPlaylist onload | `bz_cmd.py backdrop` · `!bz_flip_running` → `RunScript(bz_flip.py)` · `SetProperty(bz_sway_restart,true,home)` |
| MyPlaylist onunload | `SetProperty(bz_backdrop_last,…)` · `ClearProperty(bz_backdrop,home)` |
| defaultcontrol | `always` 60 |
| Anim | `BezelWindowFade` (400 ms fade) · `BezelSecDim` |

---

## Queue side menu

### Simple
The side menu has Shuffle, Repeat, Save and Clear.

### How it works
- These are Kodi's standard playlist button IDs, so Kodi supplies the behaviour.
- The 1119 section menu drives the same buttons by ID (`SendClick`), so menu and side buttons always match.

### Wiring
| ID | Type | Label |
|---|---|---|
| 20 | radiobutton | `$LOCALIZE[191]` Shuffle |
| 26 | button | Repeat |
| 21 | button | `$LOCALIZE[190]` Save |
| 22 | button | `$LOCALIZE[192]` Clear |
| 203 | label | `$LOCALIZE[31020]` header |

---

## Section menu (1119) and double-tap

### Simple
Menu or double-tap on a queued item gives: Play from here, Item info, Move up, Move down, Remove, Shuffle, Repeat, Save, Clear.

### How it works
- `musicplaylist` and `videoplaylist` are in `bz_dtap.py` SECW, so a double tap or the context keys open 1119.
- Each item closes 1119, then fires on a 0 s `AlarmClock(bzsc,…)` against the playlist window.

### Wiring
| ID | Label | Action (after `Dialog.Close(1119,true)`) |
|---|---|---|
| 7911 | Play from here | `Action(Select)` |
| 7912 | Item info | `Action(Info)` |
| 7913 | Move up | `Action(MoveItemUp)` |
| 7914 | Move down | `Action(MoveItemDown)` |
| 7915 | Remove from playlist | `Action(Delete)` |
| 7916 | Shuffle | `SendClick(20)` |
| 7917 | Repeat | `SendClick(26)` |
| 7918 | Save playlist | `SendClick(21)` |
| 7919 | Clear playlist | `SendClick(22)` |
| 7904 | Favourite | `RunScript(bz_ctx.py,fav)` |

---

## Playlist editor

### Simple
The music playlist editor has a button column and two lists. Left and Right move between the buttons and the lists.

### How it works
- Focus starts on button 6.
- The grouplist and the two scrollbars form a ring: 9000 → right 50 / left 100; scrollbar 60 between 50 and 100; scrollbar 61 between 100 and 9000.

### Wiring
| Control | Nav |
|---|---|
| defaultcontrol | `always` 6 |
| 9000 grouplist | onright 50 · onleft 100 |
| 6 / 7 / 8 | `$LOCALIZE[502]` / `[190]` / `[192]` |
| 60 scrollbar | onleft 50 · onright 100 |
| 61 scrollbar | onleft 100 · onright 9000 |

---

## Keys
| Key | Behavior |
|---|---|
| Up / Down | Move |
| Select | Play from item |
| Menu / double-tap | Section menu 1119 |
| Back | Previous window |
| Editor Left / Right | 9000 ↔ lists 50/100 via scrollbars 60/61 |

## Touch
Double-tap = 1119.

## Related
context-menu.md · music-controls.md · music-list.md · section-transitions.md
