# Music Fanart FS (dialog 1121) — music-fanart-fs

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `music-fanart-fs` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-fanart-fs.md) · [layout](../layout/music-fanart-fs.md) · [state](../state/music-fanart-fs.md) · [motion](../motion/music-fanart-fs.md) · [art](../art/music-fanart-fs.md) · [input](../input/music-fanart-fs.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
In Music, FULLSCREEN goes to a dialog copy of Fanart FS instead of Kodi's visualisation window. The Music window stays underneath, so the fanart stage and the swaying album never restart. Same look, same keys. Every other section still opens real Kodi visualisation.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/music-fanart-fs.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/music-fanart-fs.md).

## Control 6367 · `grouplist` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `1920` |
| height | `1080` |
| orientation | `horizontal` |
| itemgap | `0` |
| scrolltime | `480` |
| visible | `String.IsEqual(Skin.String(bz_at_fsslide),1)` |

## Control 6377 · `grouplist` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `1920` |
| height | `1080` |
| orientation | `horizontal` |
| itemgap | `0` |
| scrolltime | `380` |
| visible | `String.IsEqual(Skin.String(bz_at_fsslide),2)` |

## Control 6391 · `button` · `xml/Includes_Bezel.xml` L3011
| field | value |
|---|---|
| width | `auto` |
| height | `32` |
| onleft | `6390` |
| onright | `6392` |
| onup | `6390` |
| ondown | `ActivateWindow(1115)` |
| onback | `ClearProperty(bz_np,home)` |
| onclick (first) | `ActivateWindow(1115)` |

## Control 6397 · `grouplist` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `1920` |
| height | `1080` |
| orientation | `horizontal` |
| itemgap | `0` |
| scrolltime | `280` |
| visible | `[String.IsEmpty(Skin.String(bz_at_fsslide)) ¦ String.IsEqual(Skin.String(bz_at_fsslide),3)]` |

## Control 6399 · `button` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| width | `480` |
| height | `1` |
| onleft | `SetFocus(6398)` |
| onright | `SetFocus(6398)` |
| onup | `SetFocus(6398)` |
| ondown | `SetFocus(6398)` |
| onback | `SetFocus(6398)` |

## Control 6401 · `button` · `xml/Includes_Bezel.xml` L997
| field | value |
|---|---|
| width | `auto` |
| height | `32` |
| onleft | `Skin.Reset(bz_dfs_mode)` |
| onright | `Skin.Reset(bz_dfs_mode)` |
| onup | `$PARAM[main]` |
| ondown | `$PARAM[main]` |
| onback | `SetProperty(bz_fsret,true,home)` |
| onclick (first) | `Skin.Reset(bz_dfs_mode)` |

## Control 6401 · `button` · `xml/Custom_1115_MusicControls.xml` L26
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6410` |
| ondown | `6402` |
| onclick (first) | `PlayerControl(Play)` |

## Control 6403 · `button` · `xml/Includes_Bezel.xml` L1038
| field | value |
|---|---|
| left | `252` |
| top | `252` |
| width | `96` |
| height | `96` |
| onleft | `6402` |
| onright | `6404` |
| onup | `6401` |
| onback | `Dialog.Close(1120)` |
| onclick (first) | `PlayerControl(Play)` |

## Control 6403 · `button` · `xml/Custom_1115_MusicControls.xml` L28
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6402` |
| ondown | `6404` |
| onclick (first) | `PlayerControl(Next)` |

## Control 6420 · `button` · `xml/Custom_1121_MusicFanartFS.xml` L41
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `1920` |
| height | `1080` |
| onleft | `PlayerControl(Previous)` |
| onright | `PlayerControl(Next)` |
| onup | `6401` |
| ondown | `SetProperty(bz_noop,1,home)` |
| onback | `6422` |
| onclick (first) | `SetProperty(bz_pnfoc,6403,home)` |

## Control 6420 · `button` · `xml/Custom_1115_MusicControls.xml` L48
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `RunScript(special://skin/scripts/bz_vizset.py,step,0,-1)` |
| onright | `RunScript(special://skin/scripts/bz_vizset.py,step,0,1)` |
| onup | `6429` |
| ondown | `6421` |
| onback | `ClearProperty(bz_vizset)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_vizset.py,step,0,1)` |

## Control 6421 · `button` · `xml/Custom_1121_MusicFanartFS.xml` L33
| field | value |
|---|---|
| width | `auto` |
| height | `32` |
| onleft | `SendClick(6421)` |
| onright | `SendClick(6421)` |
| onup | `6420` |
| ondown | `ActivateWindow(1115)` |
| onback | `6422` |
| onclick (first) | `ActivateWindow(1115)` |

## Control 6421 · `button` · `xml/Custom_1115_MusicControls.xml` L48
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `RunScript(special://skin/scripts/bz_vizset.py,step,1,-1)` |
| onright | `RunScript(special://skin/scripts/bz_vizset.py,step,1,1)` |
| onup | `6420` |
| ondown | `6422` |
| onback | `ClearProperty(bz_vizset)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_vizset.py,step,1,1)` |

## Control 6422 · `button` · `xml/Custom_1121_MusicFanartFS.xml` L51
| field | value |
|---|---|
| left | `-400` |
| top | `40` |
| width | `10` |
| height | `10` |

## Control 6422 · `button` · `xml/Custom_1115_MusicControls.xml` L48
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `RunScript(special://skin/scripts/bz_vizset.py,step,2,-1)` |
| onright | `RunScript(special://skin/scripts/bz_vizset.py,step,2,1)` |
| onup | `6421` |
| ondown | `6423` |
| onback | `ClearProperty(bz_vizset)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_vizset.py,step,2,1)` |

## Control 6426 · `button` · `xml/Custom_1121_MusicFanartFS.xml` L59
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `120` |
| height | `116` |
| onclick (first) | `Dialog.Close(1121)` |

## Control 6426 · `button` · `xml/Custom_1115_MusicControls.xml` L48
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `RunScript(special://skin/scripts/bz_vizset.py,step,6,-1)` |
| onright | `RunScript(special://skin/scripts/bz_vizset.py,step,6,1)` |
| onup | `6425` |
| ondown | `6427` |
| onback | `ClearProperty(bz_vizset)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_vizset.py,step,6,1)` |

## Control 6429 · `button` · `xml/Custom_1121_MusicFanartFS.xml` L58
| field | value |
|---|---|
| left | `1100` |
| top | `220` |
| width | `680` |
| height | `680` |
| visible | `String.IsEqual(Window(Home).Property(bz_pnoff),1) + !String.IsEqual(Window(Home).Property(bz_npctl),true)` |
| onclick (first) | `PlayerControl(Play)` |

## Control 6429 · `button` · `xml/Custom_1115_MusicControls.xml` L49
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `ClearProperty(bz_vizset)` |
| onup | `6420` |
| ondown | `6420` |
| onback | `ClearProperty(bz_vizset)` |
| onclick (first) | `ClearProperty(bz_vizset)` |

## Control 6430 · `button` · `xml/Custom_1121_MusicFanartFS.xml` L57
| field | value |
|---|---|
| left | `960` |
| top | `0` |
| width | `960` |
| height | `1080` |
| visible | `String.IsEqual(Window(Home).Property(bz_pnoff),1) + !String.IsEqual(Window(Home).Property(bz_npctl),true)` |
| onclick (first) | `Skin.SetString(bz_npmode,upnext)` |

## Control 6886 · `button` · `xml/Includes_Bezel.xml` L2268
| field | value |
|---|---|
| width | `auto` |
| height | `32` |
| onleft | `60` |
| onright | `60` |
| onup | `60` |
| ondown | `60` |
| onback | `60` |
| onclick (first) | `ActivateWindow(1121)` |

## Control 6910 · `button` · `xml/Includes_Bezel.xml` L542
| field | value |
|---|---|
| left | `318` |
| top | `34` |
| width | `116` |
| height | `52` |
| onleft | `noop` |
| onright | `noop` |
| onup | `noop` |
| ondown | `6996` |
| onback | `ClearProperty(bz_nav,home)` |
| onclick (first) | `Dialog.Close(1112,true)` |

## Control 6960 · `button` · `xml/Includes_Bezel.xml` L540
| field | value |
|---|---|
| left | `286` |
| top | `86` |
| width | `86` |
| height | `34` |
| onleft | `6959` |
| onright | `noop` |
| onup | `noop` |
| ondown | `6996` |
| onback | `ClearProperty(bz_nav,home)` |
| onclick (first) | `Dialog.Close(1112,true)` |

