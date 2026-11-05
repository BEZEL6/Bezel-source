# Now playing (dialog 1112) — now-playing

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `now-playing` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/now-playing.md) · [layout](../layout/now-playing.md) · [state](../state/now-playing.md) · [motion](../motion/now-playing.md) · [art](../art/now-playing.md) · [input](../input/now-playing.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

**See screen:** [now-playing baselines](../port-refs/now-playing/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/now-playing.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/now-playing.md).

## Control 100 · `button` · `xml/Includes_BezelDialogs.xml` L119
| field | value |
|---|---|
| onup | `304` |
| ondown | `120` |

## Control 6299 · `button` · `xml/Custom_1112_NowPlaying.xml` L44
| field | value |
|---|---|
| left | `-400` |
| top | `0` |
| width | `10` |
| height | `10` |

## Control 6299 · `button` · `xml/Includes_Bezel.xml` L3063
| field | value |
|---|---|
| left | `-400` |
| top | `0` |
| width | `10` |
| height | `10` |
| onleft | `60` |
| onright | `60` |
| onup | `60` |
| ondown | `60` |

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

## Control 6381 · `button` · `xml/Custom_1112_NowPlaying.xml` L32
| field | value |
|---|---|
| left | `1040` |
| top | `120` |
| width | `800` |
| height | `800` |
| visible | `String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_flipping)) + String.IsEmpty(Window(Home).Property(bz_backanim))` |

## Control 6382 · `grouplist` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `1920` |
| height | `1080` |
| orientation | `horizontal` |
| itemgap | `0` |
| scrolltime | `180` |
| visible | `String.IsEqual(Skin.String(bz_at_fsslide),4)` |

## Control 6385 · `button` · `xml/Custom_1112_NowPlaying.xml` L45
| field | value |
|---|---|
| left | `-400` |
| top | `40` |
| width | `10` |
| height | `10` |

## Control 6387 · `button` · `xml/Custom_1112_NowPlaying.xml` L41
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `120` |
| height | `116` |
| onclick (first) | `ClearProperty(bz_np,home)` |

## Control 6387 · `visualisation` · `xml/Includes_Bezel.xml` L2875
| field | value |
|---|---|
| left | `120` |
| top | `120` |
| width | `840` |
| height | `900` |

## Control 6390 · `button` · `xml/Includes_Bezel.xml` L2951
| field | value |
|---|---|
| left | `120` |
| top | `120` |
| width | `840` |
| height | `900` |
| onclick (first) | `SetProperty(bz_pnfoc,6403,home)` |

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

## Control 6396 · `button` · `xml/Includes_Bezel.xml` L2971
| field | value |
|---|---|
| left | `150` |
| top | `346` |
| width | `1` |
| height | `1` |
| onleft | `6390` |
| onright | `SetProperty(bz_noop,1,home)` |
| onup | `Control.Move(6395,-1)` |
| ondown | `Control.Move(6395,1)` |
| onback | `6390` |
| onclick (first) | `RunScript(special://skin/scripts/bz_cmd.py,upnext_goto,$INFO[Container(6395).CurrentItem])` |

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

