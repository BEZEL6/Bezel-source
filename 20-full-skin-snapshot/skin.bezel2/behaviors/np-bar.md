# NP bar / now-playing chrome

**Object:** `Includes_Bezel.xml` expression `bz_np` (L2746) · Home prop `bz_np` · `MyMusicNav.xml` proxy `6385`, NP block `6390` · `BezelMiniPlayer`
**Where:** Section screens while media plays
**Last updated:** 2026-11-02 · 5.33.309
**Status:** Live in 5.33.207. `bz_np` marks NP mode. The music window saves it on unload and can refocus the NP block on load. Under the MM, transport is the mini-player. Draft: not Rob-approved.
**Skin:** skin.bezel2

Each section has three layers: **Simple**, **How it works**, **Wiring** (live tree).

---

## NP mode flag

### Simple
BEZEL keeps one switch saying "Now Playing is showing". Everything that draws or hides the now-playing chrome reads that switch.

### How it works
- The Home property `bz_np` is set by the Now Playing open paths (1112 onload, `bz_cmd tab/np`) and cleared by every close path.
- `$EXP[bz_np]` is the effective test. It's true only when all of these hold:
  - the prop is true;
  - the music window is up, or full-screen NP is (`bz_fsnp`);
  - the debounced audio latch is set;
  - no video is playing.

### Wiring
| Item | Value |
|---|---|
| `$EXP[bz_np]` | `bz_np`=true + [`Window.IsActive(music)` \| `bz_fsnp`=true] + `bz_audio_latch`=true + `!Player.HasVideo` |
| MyMusicNav onunload | `SetProperty(bz_np_was,$INFO[Window(Home).Property(bz_np)],home)` |
| MyMusicNav onload | `bz_np_focus`=true → `SetFocus(6390)`, then `ClearProperty(bz_np_focus)` |
| List 60 onback (music) | `bz_np` → clear `bz_np` + 6299 (before root/MM checks) |

---

## NP toggle proxy (6385)

### Simple
An invisible button acts as the "now playing" switch. When focus lands on it during playback, you jump to the NP block and the controls open. Without playback, you go to the side menu.

### How it works
- 6385 sits off-screen at x −400. Its handling depends on `$EXP[bz_np]`:
  - **True:** focus 6390 and run `bz_cmd.py npctl,toggle`, which opens or closes the 1115 colour-block controls.
  - **False:** focus the side menu 9000.
- The same proxy ID exists in 1112 and MusicVisualisation, so shared includes work everywhere.

### Wiring
- `MyMusicNav.xml` ~L111: onfocus `$EXP[bz_np]` → `SetFocus(6390)` + `RunScript(bz_cmd.py,npctl,toggle)` · `!$EXP[bz_np]` → `SetFocus(9000)`.
- Also in `Custom_1112_NowPlaying.xml` (unconditional) and `MusicVisualisation.xml`.

---

## Mini-player and compact NP

### Simple
On the main menu, playback shows as the small mini-player. In Music, the compact NP view moves together with the big album.

### How it works
- `BezelMiniPlayer` is included in the music window next to 6385.
- MM behaviour is covered in mm-mini-player.md.
- The Music compact NP rides grouplist 6397 (now-playing.md).

### Wiring
- `MyMusicNav.xml`: `<include>BezelMiniPlayer</include>` after 6385.
- See mm-mini-player.md.

---

## Keys
| Key | Behavior |
|---|---|
| Focus lands on 6385 | NP → 6390 + npctl · else → 9000 |
| Back in list with NP | Clear `bz_np`, go to 6299 |

## Touch
None specified.

## Related
mm-mini-player.md · now-playing.md · music-list.md · music-controls.md

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/np-bar.md) · [state](../state/np-bar.md) · [motion](../motion/np-bar.md) · [art](../art/np-bar.md) · [input](../input/np-bar.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## 5.33.302 current state (Music Fanart FS 1121)
- Pill→progress bar (FSMETA, 150,296): the fill `progress` now has a real clear `texturebg` (np_pill32, border 12, 00FFFFFF) so Kodi scales the fill to the 24px track inside the 780×32 pill. (Empty texturebg left the fill at native 32px height, off-centre below the pill — worst at low % / long files / paused entry.)
- Old Fanart-FS cycle-pill **shadow** grouplist (530,130, BzFSShSlide L1 + 4 rings) is gated exactly like pill 6391: hidden while 1121 is visible and in album viz. 1121 draws its own cycle pill 6421 at 140,136 (no shadow).


## Big album (5.33.309 P1)
The big album, its sway, next-song fade, cast and compact NP no longer live in this screen. They live in the always-open dialog **1122** — see [big-album.md](big-album.md). This screen only decides where the album sits (Home prop `bz_rail`: `home` / `centre` / `hide`). The old album grouplists 6367/6377/6397/6382 and their focus buttons (6368/6369, 6378/6379, 6398/6399, 6383/6384) are deleted; nothing focuses into an album rail any more.
