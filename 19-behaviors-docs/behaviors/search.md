# Search

**Object:** `Custom_1107_SearchDialog.xml` dialog `1107` · list `9000`  
**Last updated:** 2026-10-31 · 5.33.194  
**Status:** draft — verified against live 5.33.194 tree (not Rob-approved, not re-smoked)

## What it does
Opened from MM SEARCH (`GO['search']`). Three rows: Global search (`script.globalsearch`), Add-on search (`addons://search/`), and YouTube search (`plugin.video.youtube` kodion search). Missing add-ons are installed, disabled ones enabled. Every run does `Dialog.Close(all)` first. Footer: "OK select · BACK close".

## Keys
| Key | Behavior |
|---|---|
| Up / Down / Left / Right | Stay in 9000 |
| Select | Run row |
| Back | Close → MM (`bz_nav=true`) |

## Related
mm-list.md
