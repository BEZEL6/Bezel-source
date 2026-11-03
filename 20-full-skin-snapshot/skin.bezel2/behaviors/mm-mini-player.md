# MM mini-player

**Object:** `Includes_Bezel.xml` audio row `6957` Prev · `6958` Play/Pause · `6959` Next · `6961` Stop · `6960` FULL; video group (t4304, `Player.HasVideo`) `6966` Play/Pause · `6967` Stop  
**Where:** Above the MM strip (the strip slides down 120 when `Player.HasMedia`)  
**Last updated:** 2026-10-31 · 5.33.207  
**Status:** draft. This doc matches the live 5.33.207 tree. Rob has not approved it and it has not been re-smoked.  
**Skin:** skin.bezel2

Each section has three layers: **Simple** (what it does and why), **How it works** (the flow end to end, with the order and the races), and **Wiring** (props, conditions, controls, scripts and timings, all read from the live tree).

---

## What it is

**Simple.** While something plays, a small player sits on top of the Main Menu. Press Up from MUSIC to reach it. Down goes back to the strip.

**How it works.** List 6996 is shifted 0,120 by a Conditional slide when `Player.HasMedia`, which frees the top band. 6996 `onup` from the first row goes to `6966` when video plays and to `6958` when audio plays (mm-list.md). WARM 2.0: while audio plays under the MM, the poster lane hides (`bz_mmmushide`, latch ≥ 2.5 s, K22, see mm-warm.md).

## Audio row

**Wiring.** Buttons at top 80, 44×46, no textures. Icon images are 28×28 and a 24×3 white underline shows on focus.
| id | left | Icon | onclick | left / right |
|---|---|---|---|---|
| 6957 | 124 | `np_prev.png` | `PlayerControl(Previous)` | noop / 6958 |
| 6958 | 166 | `np_pause.png` (`!Player.Paused`) / `np_play.png` (Paused) | `PlayerControl(Play)` | 6957 / 6959 |
| 6959 | 208 | `np_next.png` | `PlayerControl(Next)` | 6958 / 6961 |
| 6961 | 250 | `np_stop.png` | `PlayerControl(Stop)` (+1120/bz_np/Back extras) | 6959 / 6960 |
| 6960 | 302, top 86, 76×34 | label FULL, font `bz_mm17`, `mm_full_ol.png` / `mm_full.png` (border 12, "FULL pill B") | see below | 6959 / noop |

- 6957–6959 extra clicks: 1120 active → `Dialog.Close(1120)`. Otherwise `ClearProperty(bz_np,home)` + `Action(Back)`.
- 6960: 1112 active → `Dialog.Close(1112,true)`. Clear `bz_nav` / `bz_navtune` / `bz_navbez`. `Player.HasVideo` → `ActivateWindow(fullscreenvideo)`, else `ActivateWindow(visualisation)`. From any section, Music included, this lands on real Fanart FS (`MusicVisualisation.xml`) with the `<visualisation>` keymap — no Music bounce (removed t1584).
- A 350×2 divider (40% white) sits at top 140.

## Video group

**Wiring.** Group visible on `Player.HasVideo`, fade-in 200 ms. Poster `VideoPlayer.Art(poster)` 80×120 at 20,12. Title (`bz_mm22b`) at 116,12. Line 2 (`bz_mm17`, AA white) = year · time / duration.
| id | Pos | Label | onclick | left / right |
|---|---|---|---|---|
| 6966 | 112,78 122×44 | `$VAR[BzOSDPlayLbl]` | `PlayerControl(Play)` + the same 1120 / `bz_np` + Back clicks | noop / 6967 |
| 6967 | 242,78 122×44 | Stop | `PlayerControl(Stop)` only | 6966 / noop |
Focus shows a `mm_round.png` pill (border 20, 150 ms fade). Without focus there is a faint 1 px underline. Text F0 white, focused `FF23160E`.

## Keys (all buttons)

| Key | Behavior |
|---|---|
| Up | noop |
| Down | 6996 |
| Back | clear `bz_nav` / `bz_navtune` / `bz_navbez` (close MM) → 60 |

## Related
mm-list.md · np-bar.md · mm-warm.md

**5.33.210:** 6960 FULL (and 6910) with Music active + audio → `ActivateWindow(1121)` (Music Fanart FS, sway unbroken); other sections / kill switch `bz_m1121_off` → `ActivateWindow(visualisation)`.


## Wiring table (live XML, 5.33.267)
**Simple.** Every control with an id in the files this object names, read straight from the live tree. Positions are parent-relative skin units on the 1920×1080 canvas; nested `<include>`s are *not* expanded here (unverified beyond what is listed).

**Source:** `xml/Includes_Bezel.xml`

| id | type | x,y | w×h | nav L/R/U/D | visible |
|---|---|---|---|---|---|
| $PARAM[id] | button | 590,150 | 350×$PARAM[h] | `SetFocus(60)/SetFocus(6192)/noop/noop` | `$PARAM[vis]` |
| 6185 | list | 0,0 | 600×480 | `SetProperty(bz_back_close,true,home)/6185/6185/6185` | `—` |
| 6899 | group | —,— | —×— | `—/—/—/—` | `!Window.IsActive(fullscreenvideo) + !Window.IsActive(visualisation)` |
| 6898 | button | 0,0 | 1920×1080 | `6996/ClearProperty(bz_nav,home)/6996/6996` | `$EXP[bz_navmenu]` |
| 6894 | group | —,— | —×— | `—/—/—/—` | `String.IsEmpty(Window(Home).Property(bz_mmidle))` |
| 6957 | button | 124,80 | 44×46 | `noop/6958/noop/6996` | `—` |
| 6958 | button | 166,80 | 44×46 | `6957/6959/noop/6996` | `—` |
| 6959 | button | 208,80 | 44×46 | `6958/6961/noop/6996` | `—` |
| 6961 | button | 250,80 | 44×46 | `6959/6960/noop/6996` | `—` |
| 6960 | button | 302,86 | 76×34 | `6961/noop/noop/6996` | `—` |
| 6966 | button | 112,78 | 122×44 | `noop/6967/noop/6996` | `—` |
| 6967 | button | 242,78 | 122×44 | `6966/noop/noop/6996` | `—` |
| 6996 | list | 0,40 | 390×728 | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMPrev_music])/Skin.SetString(bz_last_mmsub_music,$VAR[BzMMNext_music])/6966/SetFocus(6996,0,absolute)` | `$EXP[bz_navmenu] + !Window.IsVisible(1118) + !String.IsEqual(Window(Home).Property(bz_n…` |
| 6910 | button | 318,34 | 116×52 | `noop/noop/noop/6996` | `—` |
| 6900 | grouplist | 20,128 | 410×720 | `—/—/6910/—` | `—` |
| 6901 | button | —,— | 410×64 | `—/—/6910/—` | `—` |
| 6941 | button | —,— | 410×46 | `—/—/ClearProperty(bz_navsub,home)/—` | `String.IsEqual(Window(Home).Property(bz_navsub),music)` |
| 6942 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),music)` |
| 6943 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),music)` |
| 6944 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),music)` |
| 6945 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),music)` |
| 6946 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),music)` |
| 6947 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),music)` |
| 6902 | button | —,— | 410×64 | `—/—/—/—` | `—` |
| 6951 | button | —,— | 410×46 | `—/—/ClearProperty(bz_navsub,home)/—` | `String.IsEqual(Window(Home).Property(bz_navsub),movies)` |
| 6952 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),movies)` |
| 6953 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),movies)` |
| 6954 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),movies)` |
| 6955 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),movies)` |
| 6956 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),movies)` |
| 6903 | button | —,— | 410×64 | `—/—/—/—` | `—` |
| 6961 | button | —,— | 410×46 | `—/—/ClearProperty(bz_navsub,home)/—` | `String.IsEqual(Window(Home).Property(bz_navsub),tv)` |
| 6962 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),tv)` |
| 6963 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),tv)` |
| 6964 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),tv)` |
| 6965 | button | —,— | 410×46 | `—/—/—/—` | `String.IsEqual(Window(Home).Property(bz_navsub),tv)` |
| 6904 | button | —,— | 410×64 | `—/—/—/—` | `—` |
| 6908 | button | —,— | 410×64 | `—/—/—/6906` | `—` |
| 6906 | button | —,— | 410×53 | `—/—/6908/—` | `—` |
| 6907 | button | —,— | 410×34 | `—/—/—/—` | `—` |
| 6919 | button | —,— | 410×34 | `—/—/—/—` | `—` |
| … | 127 more ids not listed | | | | |

Actions (`onclick`/`onload`/`onback`) found:
- `$PARAM[main]`
- `$PARAM[onclick]`
- `60`
- `6299`
- `6390`
- `6901`
- `6902`
- `6903`
- `Action(Back)`
- `Action(Info)`
- `Action(PageDown)`
- `Action(PageUp)`
- `Action(Select)`
- `Action(firstpage)`
- `Action(lastpage)`
- `Action(nextletter)`
- `ActivateWindow(1107)`
- `ActivateWindow(1115)`
- `ActivateWindow(1117)`
- `ActivateWindow(1120)`
- `ActivateWindow(1121)`
- `ActivateWindow(12006)`
- `ActivateWindow(Favourites)`
- `ActivateWindow(Settings)`
- `ActivateWindow(ShutdownMenu)`

<!-- PORTLINKS -->
---
**Port blueprint (feel layer — Simple above, Deep = How it works + Wiring):** [layout](../layout/mm-mini-player.md) · [state](../state/mm-mini-player.md) · [motion](../motion/mm-mini-player.md) · [art](../art/mm-mini-player.md) · [input](../input/mm-mini-player.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)


**5.33.371 (t2665, mockup A):** audio row adds `6961` Stop between Next and FULL. Prev 124 · Play 166 · Next 208 · Stop 250 (42px pitch); FULL 302 w76. 6996 onup still → 6958 for audio.
