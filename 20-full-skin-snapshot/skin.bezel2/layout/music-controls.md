# Music controls (dialog 1115) — music-controls

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Object:** `music-controls` · **Layer:** layout (geometry) · **Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, extracted from live XML/Python
**Blueprint siblings:** [behavior](../behaviors/music-controls.md) · [layout](../layout/music-controls.md) · [state](../state/music-controls.md) · [motion](../motion/music-controls.md) · [art](../art/music-controls.md) · [input](../input/music-controls.md) · [theme](../theme/tokens.md) · [PORT_INDEX](../PORT_INDEX.md)

## Simple
The music controls panel is the "remote control" menu for music: play/pause, skip, shuffle, repeat, Up next, choose a visualisation, tweak its settings, or jump to the Tuner. It opens automatically when Kodi would show its music OSD, and from the fan art pill or the music list. Left always closes it.

**This layer in one line:** where every control of this object sits on the 1920×1080 canvas, and which control focus moves to on each direction.

## Deep (rebuild detail)
> **Verification (phase 2 hand-check):** auto-extracted rows are kept only where the control id is named in [behavior](../behaviors/music-controls.md); others were stripped as stray. Kept rows are *unverified at runtime* unless a section says hand-verified.
Coordinates are Kodi skin units on the **1920×1080** design canvas (see [resolution](resolution.md)). Values copied from live XML; `—` = not set on that control (inherits/fills parent). Visibility strings are geometry context — names are defined in [state](../state/music-controls.md).

## Control 100 · `button` · `xml/Includes_BezelDialogs.xml` L119
| field | value |
|---|---|
| onup | `304` |
| ondown | `120` |

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

## Control 6402 · `button` · `xml/Includes_Bezel.xml` L1038
| field | value |
|---|---|
| left | `96` |
| top | `252` |
| width | `96` |
| height | `96` |
| onleft | `6404` |
| onright | `6403` |
| onup | `6401` |
| onback | `Dialog.Close(1120)` |
| onclick (first) | `PlayerControl(Previous)` |

## Control 6402 · `button` · `xml/Custom_1115_MusicControls.xml` L27
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6401` |
| ondown | `6403` |
| onclick (first) | `PlayerControl(Previous)` |

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

## Control 6404 · `button` · `xml/Includes_Bezel.xml` L1038
| field | value |
|---|---|
| left | `408` |
| top | `252` |
| width | `96` |
| height | `96` |
| onleft | `6403` |
| onright | `6402` |
| onup | `6401` |
| onback | `Dialog.Close(1120)` |
| onclick (first) | `PlayerControl(Next)` |

## Control 6404 · `button` · `xml/Custom_1115_MusicControls.xml` L29
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6403` |
| ondown | `6405` |
| onclick (first) | `PlayerControl(Rewind)` |

## Control 6405 · `button` · `xml/Custom_1120_PlayNext.xml` L25
| field | value |
|---|---|
| left | `90` |
| top | `250` |
| width | `540` |
| height | `540` |
| visible | `!String.IsEqual(Skin.String(bz_dfs_mode),album) + !String.IsEmpty(MusicPlayer.offset(-1).Title)` |
| onclick (first) | `Playlist.PlayOffset(music,-1)` |

## Control 6405 · `button` · `xml/Custom_1115_MusicControls.xml` L30
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6404` |
| ondown | `6406` |
| onclick (first) | `PlayerControl(Forward)` |

## Control 6406 · `button` · `xml/Custom_1120_PlayNext.xml` L25
| field | value |
|---|---|
| left | `1290` |
| top | `250` |
| width | `540` |
| height | `540` |
| visible | `!String.IsEqual(Skin.String(bz_dfs_mode),album) + !String.IsEmpty(MusicPlayer.offset(1).Title)` |
| onclick (first) | `Playlist.PlayOffset(music,1)` |

## Control 6406 · `button` · `xml/Custom_1115_MusicControls.xml` L31
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6405` |
| ondown | `6407` |
| onclick (first) | `PlayerControl(Stop)` |

## Control 6407 · `button` · `xml/Custom_1115_MusicControls.xml` L33
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6406` |
| ondown | `6408` |
| onclick (first) | `PlayerControl(Random)` |

## Control 6408 · `button` · `xml/Custom_1115_MusicControls.xml` L34
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6407` |
| ondown | `6409` |
| onclick (first) | `PlayerControl(Repeat)` |

## Control 6409 · `button` · `xml/Custom_1115_MusicControls.xml` L36
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6408` |
| ondown | `6411` |
| onclick (first) | `Dialog.Close(1115)` |

## Control 6410 · `button` · `xml/Custom_1115_MusicControls.xml` L41
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6413` |
| ondown | `6401` |
| onclick (first) | `Dialog.Close(1115)` |

## Control 6411 · `button` · `xml/Custom_1115_MusicControls.xml` L37
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6409` |
| ondown | `6412` |
| onclick (first) | `Dialog.Close(1115)` |

## Control 6412 · `button` · `xml/Custom_1115_MusicControls.xml` L38
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6411` |
| ondown | `6413` |
| onclick (first) | `SetProperty(bz_vizset,1)` |

## Control 6413 · `button` · `xml/Custom_1115_MusicControls.xml` L40
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `Dialog.Close(1115)` |
| onright | `Dialog.Close(1115,true)` |
| onup | `6412` |
| ondown | `6410` |
| onclick (first) | `SetProperty(bz_tunesrc,fsctrl,home)` |

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

## Control 6427 · `button` · `xml/Custom_1115_MusicControls.xml` L48
| field | value |
|---|---|
| left | `0` |
| top | `0` |
| width | `390` |
| height | `56` |
| onleft | `RunScript(special://skin/scripts/bz_vizset.py,step,7,-1)` |
| onright | `RunScript(special://skin/scripts/bz_vizset.py,step,7,1)` |
| onup | `6426` |
| ondown | `6429` |
| onback | `ClearProperty(bz_vizset)` |
| onclick (first) | `RunScript(special://skin/scripts/bz_vizset.py,step,7,1)` |

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

## Control 6970 · `list` · `xml/Includes_Tuner.xml` L497
| field | value |
|---|---|
| left | `570` |
| top | `140` |
| width | `390` |
| height | `870` |
| orientation | `vertical` |
| scrolltime | `200` |
| onleft | `SetProperty(bz_tune_dirty,1,home)` |
| onright | `SetProperty(bz_tune_dirty,1,home)` |
| onup | `noop` |
| ondown | `noop` |
| onback | `ClearProperty(bz_navtune,home)` |

