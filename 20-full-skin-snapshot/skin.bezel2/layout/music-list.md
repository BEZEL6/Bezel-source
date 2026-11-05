# Music section list — music-list

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `music-list` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-list.md) · [layout](../layout/music-list.md) · [state](../state/music-list.md) · [motion](../motion/music-list.md) · [art](../art/music-list.md) · [input](../input/music-list.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
, **How it works**, **Wiring** (live tree).

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

**See screen:** [music-list baselines](../port-refs/music-list/) — smoke baseline + port diff target.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/music-list.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/music-list.md).

## Control 612 · `button` · `xml/MyMusicNav.xml` L78
| field | value |
|---|---|
| visible | `Integer.IsGreater(Playlist.Length(music),0)` |
| onclick (first) | `ActivateWindow(musicplaylist)` |

## Control 6097 · `button` · `xml/Includes_Bezel.xml` L2196
| field | value |
|---|---|
| visible | `!$EXP[bz_covercol] ¦ $EXP[bz_allpick]` |

## Control 6100 · `grouplist` · `xml/Includes_Bezel.xml` L2222
| field | value |
|---|---|
| left | `78` |
| top | `151` |
| width | `36` |
| height | `837` |
| orientation | `vertical` |
| itemgap | `0` |
| onleft | `60` |
| onright | `60` |
| visible | `!$EXP[bz_navmenu]` |

## Control 6160 · `button` · `xml/Includes_Bezel.xml` L2286
| field | value |
|---|---|
| left | `1030` |
| top | `914` |
| width | `800` |
| height | `110` |
| onleft | `60` |
| onright | `60` |
| onup | `60` |
| ondown | `60` |
| visible | `Player.HasAudio + !$EXP[bz_np] + !Window.IsActive(visualisation) + String.IsEmpty(Window(Home).Property(bz_lctl)) + String.IsEmpty(Window(Home).Property(bz_tv_list)) + [!$EXP[bz_gridm] ¦ $EXP[bz_np]] + [Window.IsActive(m` |
| onclick (first) | `ActivateWindow(1115)` |

## Control 6180 · `button` · `xml/Includes_Bezel.xml` L1368
| field | value |
|---|---|
| left | `1140` |
| top | `220` |
| width | `600` |
| height | `600` |
| visible | `String.IsEqual(Window(Home).Property(bz_audio_latch),true) + String.IsEmpty(Window(Home).Property(bz_back)) + String.IsEmpty(Window(Home).Property(bz_flipping)) + String.IsEmpty(Window(Home).Property(bz_backanim))` |
| onclick (first) | `SetFocus(6369)` |

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

## Control 6299 · `button` · `xml/Custom_1117_MediaSources.xml` L10
| field | value |
|---|---|
| left | `-10` |
| top | `-10` |
| width | `1` |
| height | `1` |

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

## Control 6368 · `button` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| width | `1` |
| height | `1` |

## Control 6369 · `button` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| width | `480` |
| height | `1` |
| onleft | `SetFocus(6368)` |
| onright | `SetFocus(6368)` |
| onup | `SetFocus(6368)` |
| ondown | `SetFocus(6368)` |
| onback | `SetFocus(6368)` |

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

## Control 6378 · `button` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| width | `1` |
| height | `1` |

## Control 6379 · `button` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| width | `480` |
| height | `1` |
| onleft | `SetFocus(6378)` |
| onright | `SetFocus(6378)` |
| onup | `SetFocus(6378)` |
| ondown | `SetFocus(6378)` |
| onback | `SetFocus(6378)` |

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

## Control 6383 · `button` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| width | `1` |
| height | `1` |

## Control 6384 · `button` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| width | `480` |
| height | `1` |
| onleft | `SetFocus(6383)` |
| onright | `SetFocus(6383)` |
| onup | `SetFocus(6383)` |
| ondown | `SetFocus(6383)` |
| onback | `SetFocus(6383)` |

## Control 6385 · `button` · `xml/Custom_1112_NowPlaying.xml` L45
| field | value |
|---|---|
| left | `-400` |
| top | `40` |
| width | `10` |
| height | `10` |

## Control 6385 · `button` · `xml/MyMusicNav.xml` L111
| field | value |
|---|---|
| left | `-400` |
| top | `40` |
| width | `10` |
| height | `10` |

## Control 6390 · `button` · `xml/Includes_Bezel.xml` L2951
| field | value |
|---|---|
| left | `120` |
| top | `120` |
| width | `840` |
| height | `900` |
| onclick (first) | `SetProperty(bz_pnfoc,6403,home)` |

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

## Control 6398 · `button` · `xml/Includes_Bezel.xml` L2281
| field | value |
|---|---|
| width | `1` |
| height | `1` |

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

## Control 6500 · `grouplist` · `xml/Includes_Bezel.xml` L2748
| field | value |
|---|---|
| left | `78` |
| top | `151` |
| width | `36` |
| height | `837` |
| orientation | `vertical` |
| itemgap | `0` |
| onleft | `SetProperty(bz_nav,true,home)` |
| onright | `60` |
| visible | `!$EXP[bz_navmenu]` |

## Control 6600 · `panel` · `xml/Includes_Bezel.xml` L3091
| field | value |
|---|---|
| left | `962` |
| top | `90` |
| width | `904` |
| height | `984` |
| orientation | `vertical` |
| scrolltime | `350` |
| onleft | `60` |
| onback | `60` |
| visible | `$EXP[bz_gridm] + !$EXP[bz_np]` |
| onclick (first) | `RunScript(special://skin/scripts/bz_cmd.py,gridclick)` |

## Control 6600 · `panel` · `xml/Includes_Bezel.xml` L3143
| field | value |
|---|---|
| left | `962` |
| top | `90` |
| width | `888` |
| height | `975` |
| orientation | `vertical` |
| scrolltime | `350` |
| onleft | `SetProperty(bz_nav,true,home)` |
| onback | `60` |
| visible | `$EXP[bz_gridv]` |
| onclick (first) | `RunScript(special://skin/scripts/bz_cmd.py,gridclick)` |

## Control 6996 · `list` · `xml/Includes_Bezel.xml` L540
| field | value |
|---|---|
| left | `0` |
| top | `40` |
| width | `390` |
| height | `728` |
| scrolltime | `150` |
| onleft | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMPrev_music])` |
| onright | `Skin.SetString(bz_last_mmsub_music,$VAR[BzMMNext_music])` |
| onup | `6966` |
| ondown | `SetFocus(6996,0,absolute)` |
| visible | `$EXP[bz_navmenu] + !Window.IsVisible(1118) + !String.IsEqual(Window(Home).Property(bz_navtune),true) + !String.IsEqual(Window(Home).Property(bz_navbez),true)` |

## Control 9000 · `grouplist` · `xml/Includes_BezelDialogs.xml` L519
| field | value |
|---|---|
| left | `0` |
| top | `100` |
| width | `390` |
| height | `754` |
| orientation | `vertical` |
| itemgap | `0` |

## Control 9000 · `grouplist` · `xml/Custom_1117_MediaSources.xml` L19
| field | value |
|---|---|
| left | `0` |
| top | `112` |
| width | `390` |
| height | `720` |
| orientation | `vertical` |
| itemgap | `0` |
| visible | `!Window.IsActive(1132)` |

## Control 9000 · `grouplist` · `xml/MyMusicNav.xml` L57
| field | value |
|---|---|
| top | `50` |

