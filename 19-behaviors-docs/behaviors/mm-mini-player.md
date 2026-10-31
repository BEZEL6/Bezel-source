# MM mini-player

**Object:** `Includes_Bezel.xml` audio row `6957` Prev · `6958` Play/Pause · `6959` Next · `6960` Fullscreen; video row `6966` Play/Pause · `6967` Stop  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
Transport row above the MM strip while media plays. It is reached with Up from the top MM row (6996 onup: video → 6966, audio → 6958).

## Keys
| Key | Behavior |
|---|---|
| Left / Right | Audio 6957 ↔ 6958 ↔ 6959 ↔ 6960 (ends noop); video 6966 ↔ 6967 |
| Up | noop |
| Down | Back to strip 6996 |
| Select | 6957 Previous · 6958/6966 Play-Pause · 6959 Next · 6967 Stop · 6960 closes 1112 if open, clears nav, → fullscreenvideo (video) or visualisation (audio) |
| Back | Clear `bz_nav`/`bz_navtune`/`bz_navbez` (close MM) → list 60 |

Transport clicks also close 1120 if it's active; otherwise they clear `bz_np` + Back.
WARM 2.0: while audio plays under MM the poster lane hides (`bz_mmmushide`, mm-warm.md). Latch ≥ 2.5 s (K22).

## Related
mm-list.md · np-bar.md · mm-warm.md
