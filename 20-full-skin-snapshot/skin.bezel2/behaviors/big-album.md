# Big album (dialog 1122)

**Object:** `xml/Custom_1122_BigAlbum.xml` (dialog 1122, zorder 0) · includes `BezelAlbumCast` + 2× `BezelMusicPlayingArt` · expressions `bz_railvis` / `bz_railc` (Includes_Bezel) · Home prop `bz_rail`
**Last updated:** 2026-11-03 · 5.33.417
**Status:** built (P1), awaiting device smoke

## Simple
The big playing album is one global layer that stays open across sections, like the dust. Changing section never remounts it, so the sway never restarts. Sections only say *where* it sits: home (right, x1140), centre (x660) or hidden.

## How it works
- 1122 has a `<visible>` tag (splash done, not fullscreen video / slideshow / screensaver / 1113), so Kodi opens it by itself, **modeless**. Modeless dialogs never get key actions — so **nothing focusable is inside it**. Touch/mouse still reaches it: tap 6180 on the album (Music only, `bz_pndlg_ok`) opens Play Next 1120.
- Shows when `$EXP[bz_railvis]`: Music lists (artists/albums/songs), MM open over **any** section while music plays (`bz_mmmushide` — incl. Music itself since 5.33.327, so Movies/TV→Music under MM never drops a frame while the Music container loads), Kodi FS (visualisation), Play Next 1120, Music fan art 1121 — and `bz_rail` is not `hide`. Inside, the old gate still applies: hidden by the grid (`bz_gridm`) unless Now Playing.
- Position: two real copies (as 5.33.307), each with its own real left, so each sway camera is right when it is at rest. **Both copies are always visible** — neither is ever set Visible=false, so the art and NP fade-ins inside `BezelMusicPlayingArt` never restart.
  - Home copy (left 0, at x 1140): Conditional slide −480 when `$EXP[bz_railc]`; goes alpha 0 only when the slide ends (fade time 0, delay = slide time).
  - Centre copy (left −480, at x 660): parked at home (Conditional slide +480 when `!$EXP[bz_railc]`) under alpha 0, same end-of-slide rule. WindowOpen hold at alpha 0 (600 ms) when the dialog opens at home, so it is not seen parking.
  - `$EXP[bz_railc]` = `bz_rail` is `centre`, OR (1121 or Kodi FS) and album viz (`bz_pnoff` ≠ 1).
  - Home↔centre is always **one continuous slide** at the FS Slide speed (`bz_at_fsslide` 1/2/empty-3/4 = 480/380/280/180 ms), both directions. Both copies move together and overlap during the slide; the arriving copy is drawn from the first frame (reverse restores its alpha at once). Never a fade, never a gap.
  - 5.33.309 bug (fixed): copies swapped by Visible, so the arriving copy remounted and its inner fade-ins replayed (~1 s with no album).
- Cast (`BezelAlbumCast`) is mounted once, outside both copies (CASTPIN, unchanged).
- The compact NP rides with the album because it is inside `BezelMusicPlayingArt`.

## Wiring
| Piece | Where |
|---|---|
| `bz_rail` = `centre` | 1120 onload; 6390 Select/Right, 6180 tap and 1115 Right set it just before `ActivateWindow(1120)` |
| `bz_rail` = `home` | 1120 onunload (then focus → 60, or 6996 when the MM is open) |
| `bz_rail` = `hide` | free for any section that wants the album off (nothing sets it yet) |
| 1121 / Kodi FS centre | follows `bz_pnoff` live (album viz vs fan art), no property needed |
| Removed | `BezelMusicRail` include + its mounts (Music View_60, MyVideoNav); MusicVisualisation's own album + cast copies |
| Restart | XML → ReloadSkin |
- 5.33.311: centre copy on Custom_1122 WindowOpen fade must end=100 (full alpha after 600ms); a fade ending at 0 leaves centre invisible after the slide.

## 5.33.314 — Background dim
- The visible album group in Custom_1122 (`$EXP[bz_railvis]` group: cast + art + NP) now takes `BezelSecDim`, so MM dim (`bz_at_mmdim`, MM open + not idle) and Global dim (`bz_at_gdim`, MM closed) fade the big album exactly like section content. No parallel dim system.
- MM Music focus no longer restarts sway (MyMusicNav onload restart removed).

## 5.33.332–333 — under Settings / Add-ons / Media Sources
- `bz_railvis` also true while audio plays (no video) and 1130, 1131, addonbrowser, 1117 or 1132 is visible (unless Tuner Album art during music = Off). Verified live on 334 with MM closed: shots `audit_settings_levels/334_album_{1130,1131,1117,1132}.png`.


## Art under the splash (5.33.412 ARTUNDERSPLASH)

**Simple.** Big album and poster (dialog 1122, group 6400) load **behind** the splash and dissolve in **with** the 3 s splash fade — no art pop after the splash closes. Dust (1114) still waits for `bz_splash_done`.

**Wiring.** 1122 `<visible>` has no `bz_splash_done` term (opens at startup, zorder 0, modeless). Group 6400 carries two Conditional fades: alpha 0 (time 0) while `bz_warm_gate` is set, and 0→100 over 3000 ms sine when `bz_warm_gate` clears (same moment `bz_warmgate.py dismiss()` starts the overlay's 3 s Hidden fade). Splash Off → gate never set → art shows at once. **5.33.417 ARTGATEFIX:** the hold fade is `start=100 end=0 time=0` — a reversed Kodi Conditional rests at its *start* value, so the old `start=0 end=0` hold rested at alpha 0 forever and the art never showed after the splash. List-60 section art (Music/Videos windows) already rendered under the overlay.
