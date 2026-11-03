# Home properties catalog

**Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, generated from live tree · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Bezel's whole UI state lives in string properties on Kodi's Home window (`Window(Home).Property(bz_*)`) plus persistent `Skin.*` settings. A native port turns each into a field on one app-wide view-model/store; *set* = write, *read* = observe. Empty string = false/off.

## Deep (rebuild detail)
Counts are read sites across `xml/` + `scripts/`; *setters* = files that write/clear it. Per-object meaning lives in `state/<id>.md` and the behavior file.

### Fold (bz_hf_*)
| prop | reads | first read | setters |
|---|---|---|---|
| `bz_hf_ph` | 22 | Includes_Bezel.xml L1101 | bz_flip.py |
| `bz_hf_a` | 6 | Includes_Bezel.xml L1096 | bz_flip.py |
| `bz_hf_b` | 3 | Includes_Bezel.xml L1101 | bz_flip.py |

### Nav / MM
| prop | reads | first read | setters |
|---|---|---|---|
| `bz_casc` | 380 | Includes_Bezel.xml L1574 | bz_flip.py |
| `bz_navsub` | 48 | Includes_Bezel.xml L524 | Includes_Bezel.xml, bz_flip.py |
| `bz_nav` | 33 | Custom_1112_NowPlaying.xml L15 | AddonBrowser.xml, Custom_1107_SearchDialog.xml, Custom_1112_NowPlaying.xml, Custom_1115_MusicControls.xml, Custom_1117_MediaSources.xml, Custom_1118_PowerMenu.xml, Custom_1130_BzSettings.xml, Custom_1131_BzAddons.xml, FileManager.xml, Includes_Bezel.xml, Includes_Tuner.xml, MyMusicNav.xml, MyPics.xml, MyVideoNav.xml, MyWeather.xml, Settings.xml, SettingsSystemInfo.xml, bz_cmd.py, bz_flip.py, bz_mm.py, bz_set.py |
| `bz_mmsub_movies` | 28 | Includes_Bezel.xml L514 | Includes_Bezel.xml |
| `bz_mmsub_tv` | 28 | Includes_Bezel.xml L515 | Includes_Bezel.xml |
| `bz_mmsub_music` | 24 | Includes_Bezel.xml L513 | Includes_Bezel.xml |
| `bz_pos_on` | 16 | Includes_Bezel.xml L1202 | bz_flip.py |
| `bz_mmwarm` | 15 | Includes_Bezel.xml L6 | bz_flip.py |
| `bz_mmlive` | 15 | MyVideoNav.xml L6 | bz_flip.py |
| `bz_mmpick` | 14 | Includes_Bezel.xml L4 | bz_flip.py, bz_mm.py |
| `bz_mmidle` | 14 | Includes_Bezel.xml L540 | Includes_Bezel.xml, bz_flip.py |
| `bz_navtune` | 14 | Includes_Bezel.xml L540 | Custom_1112_NowPlaying.xml, Custom_1115_MusicControls.xml, Custom_1118_PowerMenu.xml, Custom_1130_BzSettings.xml, Includes_Bezel.xml, Includes_Tuner.xml, bz_cmd.py, bz_dtap.py, bz_flip.py, bz_tune.py |
| `bz_fan_on` | 11 | Includes_Bezel.xml L715 | — (read-only / Skin) |
| `bz_ab_live` | 11 | Includes_Bezel.xml L755 | bz_flip.py |
| `bz_navbez` | 10 | Includes_Bezel.xml L540 | Custom_1112_NowPlaying.xml, Custom_1118_PowerMenu.xml, Includes_Bezel.xml, Includes_Tuner.xml, bz_cmd.py |
| `bz_pos_empty` | 8 | Includes_Bezel.xml L1202 | — (read-only / Skin) |
| `bz_pos_side` | 8 | Includes_Bezel.xml L1209 | — (read-only / Skin) |
| `bz_mmstart` | 7 | bz_flip.py L523 | bz_cmd.py, bz_flip.py |
| `bz_navset` | 6 | Includes_Bezel.xml L542 | Custom_1118_PowerMenu.xml, bz_flip.py |
| `bz_fan_side` | 6 | Includes_Bezel.xml L755 | — (read-only / Skin) |
| `bz_navlock` | 4 | Includes_Bezel.xml L414 | bz_flip.py |
| `bz_navgrace` | 4 | Includes_Bezel.xml L414 | bz_cmd.py, bz_flip.py |
| `bz_navstrip` | 4 | Includes_Bezel.xml L523 | Includes_Bezel.xml, bz_flip.py |
| `bz_pos_a` | 4 | Includes_Bezel.xml L1212 | — (read-only / Skin) |
| `bz_pos_b` | 4 | Includes_Bezel.xml L1219 | — (read-only / Skin) |
| `bz_casc_fp` | 4 | Includes_Bezel.xml L1573 | bz_flip.py |
| `bz_mmsub_` | 4 | bz_cmd.py L626 | bz_cmd.py, bz_mm.py |
| `bz_navroot` | 4 | bz_flip.py L958 | Includes_Bezel.xml, bz_flip.py, bz_mm.py |
| `bz_fan_a` | 3 | Includes_Bezel.xml L759 | — (read-only / Skin) |
| `bz_fan_b` | 3 | Includes_Bezel.xml L766 | — (read-only / Skin) |
| `bz_mmpos` | 3 | MyVideoNav.xml L6 | bz_flip.py |
| `bz_casc_force` | 3 | bz_flip.py L834 | bz_cmd.py, bz_flip.py |
| `bz_ab_vis` | 2 | Includes_Bezel.xml L430 | bz_cmd.py |
| `bz_mmstartrow` | 2 | bz_flip.py L1024 | bz_cmd.py |
| `bz_mmstartsec` | 2 | bz_flip.py L1027 | bz_cmd.py |
| `bz_mmlock` | 1 | bz_mm.py L60 | bz_mm.py |
| `bz_navcard2` | 1 | bz_flip.py L1041 | MyMusicNav.xml, MyVideoNav.xml, bz_flip.py |
| `bz_mmidle_set` | 1 | bz_flip.py L1445 | bz_flip.py |

### Other
| prop | reads | first read | setters |
|---|---|---|---|
| `bz_drumdir` | 176 | Includes_Tuner.xml L9 | bz_flip.py |
| `bz_ci_more` | 98 | Includes_BezelInfo.xml L20 | DialogMusicInfo.xml, DialogVideoInfo.xml |
| `bz_pnoff` | 79 | Custom_1112_NowPlaying.xml L37 | Custom_1121_MusicFanartFS.xml, Includes_Bezel.xml, MusicVisualisation.xml |
| `bz_setpg` | 58 | Custom_1130_BzSettings.xml L13 | Custom_1130_BzSettings.xml, bz_set.py |
| `bz_audio_latch` | 45 | Custom_1112_NowPlaying.xml L33 | bz_flip.py |
| `bz_grest` | 39 | Includes_Bezel.xml L3086 | bz_flip.py |
| `bz_vback` | 38 | Includes_Bezel.xml L645 | MyVideoNav.xml, bz_flip.py |
| `bz_setx` | 38 | Custom_1130_BzSettings.xml L15 | Custom_1130_BzSettings.xml, bz_set.py |
| `bz_np` | 37 | Custom_1112_NowPlaying.xml L15 | Custom_1112_NowPlaying.xml, Custom_1121_MusicFanartFS.xml, Includes_Bezel.xml, MusicVisualisation.xml, MyMusicNav.xml, bz_cmd.py, bz_flip.py |
| `bz_msx` | 32 | Custom_1117_MediaSources.xml L20 | bz_set.py |
| `bz_kbcaps` | 30 | Includes_BezelDialogs.xml L536 | DialogKeyboard.xml, Includes_BezelDialogs.xml |
| `bz_gslot` | 29 | Includes_Bezel.xml L354 | bz_flip.py |
| `bz_sway_hold` | 29 | Includes_Bezel.xml L1130 | bz_flip.py |
| `bz_gscroll` | 28 | Includes_Bezel.xml L3251 | bz_flip.py |
| `bz_back` | 26 | Custom_1112_NowPlaying.xml L33 | MyMusicNav.xml, bz_flip.py |
| `bz_backdrop` | 24 | MyPlaylist.xml L4 | AddonBrowser.xml, FileManager.xml, MyFavourites.xml, MyGames.xml, MyPlaylist.xml, MyPrograms.xml, Settings.xml, bz_cmd.py, bz_flip.py |
| `bz_flip_running` | 24 | MyPlaylist.xml L9 | bz_flip.py |
| `bz_tovideo` | 24 | Includes_Bezel.xml L456 | MyVideoNav.xml, bz_cmd.py |
| `bz_sway_go` | 24 | Includes_Bezel.xml L1130 | bz_flip.py |
| `bz_big_pulse` | 19 | Includes_Bezel.xml L1066 | bz_flip.py |
| `bz_backanim` | 17 | Custom_1112_NowPlaying.xml L33 | MyMusicNav.xml, bz_flip.py |
| `bz_msret` | 17 | Includes_Bezel.xml L1594 | Custom_1117_MediaSources.xml, Custom_1132_BzSources.xml |
| `bz_sway_pulse` | 14 | Includes_Bezel.xml L1152 | bz_flip.py |
| `bz_ppulse` | 14 | Includes_Bezel.xml L2566 | — (read-only / Skin) |
| `bz_fsret` | 13 | Custom_1112_NowPlaying.xml L37 | Custom_1120_PlayNext.xml, Includes_Bezel.xml, Timers.xml |
| `bz_tunesrc` | 13 | Custom_1118_PowerMenu.xml L10 | Custom_1115_MusicControls.xml, Custom_1118_PowerMenu.xml, Custom_1130_BzSettings.xml, Includes_Tuner.xml |
| `bz_vizset` | 13 | Custom_1115_MusicControls.xml L3 | Custom_1115_MusicControls.xml |
| `bz_adx` | 13 | Custom_1131_BzAddons.xml L12 | bz_set.py |
| `bz_flipping` | 12 | Custom_1112_NowPlaying.xml L33 | bz_flip.py |
| `bz_npdlg` | 12 | Includes_Bezel.xml L55 | Custom_1112_NowPlaying.xml, bz_cmd.py |
| `bz_npctl` | 11 | Custom_1112_NowPlaying.xml L38 | bz_flip.py |
| `bz_cov_a` | 11 | Includes_Bezel.xml L131 | — (read-only / Skin) |
| `bz_splash_done` | 11 | Includes_Bezel.xml L633 | Startup.xml, bz_warmgate.py |
| `bz_evopt` | 11 | EventLog.xml L6 | EventLog.xml |
| `bz_vbackanim` | 10 | Includes_Bezel.xml L2577 | MyVideoNav.xml, bz_flip.py |
| `bz_vdtap` | 10 | Includes_Bezel.xml L2953 | Custom_1121_MusicFanartFS.xml, Includes_Bezel.xml, MusicVisualisation.xml |
| `bz_artsel` | 9 | DialogSelect.xml L4 | bz_cmd.py |
| `bz_artsec` | 9 | Includes_BezelChooseArt.xml L5 | bz_cmd.py |
| `bz_m2v` | 9 | Includes_Bezel.xml L3644 | bz_cmd.py |
| `bz_cov_b` | 8 | Includes_Bezel.xml L132 | — (read-only / Skin) |
| `bz_pready` | 8 | Includes_Bezel.xml L2559 | bz_flip.py |
| `bz_hold_poster` | 7 | Includes_Bezel.xml L160 | bz_flip.py |
| `bz_big_go` | 7 | Includes_Bezel.xml L1066 | bz_flip.py |
| `bz_kset` | 6 | Includes_Bezel.xml L434 | bz_flip.py |
| `bz_tv_list` | 6 | Includes_Bezel.xml L459 | MyMusicNav.xml, MyVideoNav.xml |
| `bz_lctl` | 6 | Includes_Bezel.xml L1391 | bz_flip.py |
| `bz_allup` | 6 | Includes_Bezel.xml L2196 | Includes_Bezel.xml, bz_flip.py |
| `bz_drumk` | 6 | Includes_Bezel.xml L2499 | bz_flip.py |
| `bz_tomusic` | 6 | Includes_Bezel.xml L2551 | bz_cmd.py |
| `bz_msfocus` | 6 | Custom_1117_MediaSources.xml L6 | Custom_1117_MediaSources.xml |
| `bz_vs1_lab` | 6 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs2_lab` | 6 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs3_lab` | 6 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs4_lab` | 6 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs5_lab` | 6 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs6_lab` | 6 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs7_lab` | 6 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_quit` | 6 | bz_precache.py L12 | bz_cmd.py |
| `bz_arthold` | 5 | Includes_Bezel.xml L149 | bz_flip.py |
| `bz_albvd` | 5 | Includes_Bezel.xml L371 | bz_flip.py |
| `bz_m2v_flat` | 5 | Includes_Bezel.xml L2280 | bz_cmd.py |
| `bz_clr_on` | 5 | Includes_Bezel.xml L2460 | — (read-only / Skin) |
| `bz_pswayon` | 5 | Includes_Bezel.xml L2566 | — (read-only / Skin) |
| `bz_mushref` | 5 | Includes_Bezel.xml L2605 | Includes_Tuner.xml |
| `bz_xi_cast0_name` | 5 | Includes_Bezel.xml L3503 | — (read-only / Skin) |
| `bz_arttitle` | 4 | Includes_BezelChooseArt.xml L4 | bz_cmd.py |
| `bz_albumid` | 4 | Includes_Bezel.xml L130 | bz_flip.py |
| `bz_back_fade` | 4 | Includes_Bezel.xml L455 | MyMusicNav.xml, bz_flip.py |
| `bz_warm_gate` | 4 | Includes_Bezel.xml L596 | Startup.xml, bz_warmgate.py |
| `bz_cov_side` | 4 | Includes_Bezel.xml L1196 | bz_flip.py |
| `bz_startfade` | 4 | Includes_Bezel.xml L1406 | bz_cmd.py |
| `bz_mart_on` | 4 | Includes_Bezel.xml L2605 | — (read-only / Skin) |
| `bz_mart_empty` | 4 | Includes_Bezel.xml L2605 | — (read-only / Skin) |
| `bz_vs0_lab` | 4 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_arttype` | 3 | Includes_BezelChooseArt.xml L5 | bz_cmd.py |
| `bz_biglogo_spin` | 3 | Includes_Bezel.xml L617 | bz_flip.py |
| `bz_clr_empty` | 3 | Includes_Bezel.xml L2461 | — (read-only / Skin) |
| `bz_minibig` | 3 | Includes_Bezel.xml L2548 | AddonBrowser.xml, MyFavourites.xml, MyGames.xml, MyPrograms.xml, MyVideoNav.xml, bz_flip.py |
| `bz_xalb_on` | 3 | Includes_Bezel.xml L2601 | bz_flip.py |
| `bz_fsnp` | 3 | Includes_Bezel.xml L2801 | Custom_1121_MusicFanartFS.xml, MusicVisualisation.xml |
| `bz_npinfo_prev` | 3 | Includes_Bezel.xml L3029 | Includes_Bezel.xml |
| `bz_xi_cast1_name` | 3 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast2_name` | 3 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast3_name` | 3 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast4_name` | 3 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast5_name` | 3 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast6_name` | 3 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast7_name` | 3 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast8_name` | 3 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast9_name` | 3 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast10_name` | 3 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast11_name` | 3 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_trailer` | 3 | Includes_Bezel.xml L3532 | — (read-only / Skin) |
| `bz_secfan` | 3 | Includes_BezelInfo.xml L16 | bz_dtap.py |
| `bz_secload` | 3 | MyVideoNav.xml L29 | bz_cmd.py |
| `bz_lastmusic` | 3 | bz_mm.py L47 | bz_flip.py |
| `bz_fpop` | 2 | Includes_Bezel.xml L55 | bz_flip.py |
| `bz_favpath` | 2 | Includes_Bezel.xml L89 | bz_fav.py |
| `bz_actthumb` | 2 | Includes_Bezel.xml L119 | bz_flip.py |
| `bz_actpath` | 2 | Includes_Bezel.xml L119 | bz_flip.py |
| `bz_hold_fanart` | 2 | Includes_Bezel.xml L149 | bz_flip.py |
| `bz_gtitle` | 2 | Includes_Bezel.xml L279 | bz_flip.py |
| `bz_albva` | 2 | Includes_Bezel.xml L371 | bz_flip.py |
| `bz_am_n2` | 2 | Includes_Bezel.xml L379 | bz_artist.py |
| `bz_sd_n2` | 2 | Includes_Bezel.xml L392 | — (read-only / Skin) |
| `bz_pwrswap` | 2 | Includes_Bezel.xml L540 | Custom_1118_PowerMenu.xml |
| `bz_pc_img` | 2 | Includes_Bezel.xml L638 | bz_precache.py |
| `bz_gb` | 2 | Includes_Bezel.xml L685 | bz_flip.py |
| `bz_pnfoc` | 2 | Includes_Bezel.xml L986 | Custom_1120_PlayNext.xml, Custom_1121_MusicFanartFS.xml, Includes_Bezel.xml, MusicVisualisation.xml |
| `bz_gridret` | 2 | Includes_Bezel.xml L1567 | MusicVisualisation.xml |
| `bz_fsbounce` | 2 | Includes_Bezel.xml L1579 | — (read-only / Skin) |
| `bz_rootarm` | 2 | Includes_Bezel.xml L2372 | bz_flip.py |
| `bz_atnavroot` | 2 | Includes_Bezel.xml L2372 | bz_flip.py |
| `bz_clr_side` | 2 | Includes_Bezel.xml L2461 | — (read-only / Skin) |
| `bz_dra_mma` | 2 | Includes_Bezel.xml L2501 | — (read-only / Skin) |
| `bz_dra_ppa` | 2 | Includes_Bezel.xml L2501 | — (read-only / Skin) |
| `bz_dra_mt` | 2 | Includes_Bezel.xml L2503 | — (read-only / Skin) |
| `bz_dra_me` | 2 | Includes_Bezel.xml L2503 | — (read-only / Skin) |
| `bz_dra_pt` | 2 | Includes_Bezel.xml L2505 | — (read-only / Skin) |
| `bz_dra_pe` | 2 | Includes_Bezel.xml L2505 | — (read-only / Skin) |
| `bz_dra_0e` | 2 | Includes_Bezel.xml L2507 | — (read-only / Skin) |
| `bz_drb_mma` | 2 | Includes_Bezel.xml L2511 | — (read-only / Skin) |
| `bz_drb_ppa` | 2 | Includes_Bezel.xml L2511 | — (read-only / Skin) |
| `bz_drb_mt` | 2 | Includes_Bezel.xml L2513 | — (read-only / Skin) |
| `bz_drb_me` | 2 | Includes_Bezel.xml L2513 | — (read-only / Skin) |
| `bz_drb_pt` | 2 | Includes_Bezel.xml L2515 | — (read-only / Skin) |
| `bz_drb_pe` | 2 | Includes_Bezel.xml L2515 | — (read-only / Skin) |
| `bz_drb_0e` | 2 | Includes_Bezel.xml L2517 | — (read-only / Skin) |
| `bz_from_music` | 2 | Includes_Bezel.xml L2546 | MyMusicNav.xml, MyVideoNav.xml, bz_cmd.py |
| `bz_pswipe` | 2 | Includes_Bezel.xml L2555 | — (read-only / Skin) |
| `bz_xalb` | 2 | Includes_Bezel.xml L2601 | bz_flip.py |
| `bz_mart_side` | 2 | Includes_Bezel.xml L2622 | — (read-only / Skin) |
| `bz_xi_fanart` | 2 | Includes_Bezel.xml L3481 | — (read-only / Skin) |
| `bz_xi_title` | 2 | Includes_Bezel.xml L3495 | — (read-only / Skin) |
| `bz_xi_f_res` | 2 | Includes_Bezel.xml L3498 | — (read-only / Skin) |
| `bz_xi_f_hdr` | 2 | Includes_Bezel.xml L3498 | — (read-only / Skin) |
| `bz_xi_f_ac` | 2 | Includes_Bezel.xml L3498 | — (read-only / Skin) |
| `bz_xi_f_ch` | 2 | Includes_Bezel.xml L3498 | — (read-only / Skin) |
| `bz_xi_resume` | 2 | Includes_Bezel.xml L3529 | — (read-only / Skin) |
| `bz_vpill` | 2 | Includes_Bezel.xml L3613 | Includes_Bezel.xml |
| `bz_secfanlbl` | 2 | Includes_BezelInfo.xml L16 | bz_dtap.py |
| `bz_precache_running` | 2 | Home.xml L10 | bz_precache.py |
| `bz_gpend` | 2 | MyVideoNav.xml L29 | MyVideoNav.xml, bz_flip.py |
| `bz_secfade` | 2 | MyVideoNav.xml L30 | bz_cmd.py |
| `bz_tunapplied` | 2 | DialogNotification.xml L12 | DialogNotification.xml |
| `bz_vs0_val` | 2 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs1_val` | 2 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs2_val` | 2 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs3_val` | 2 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs4_val` | 2 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs5_val` | 2 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs6_val` | 2 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_vs7_val` | 2 | Custom_1115_MusicControls.xml L48 | — (read-only / Skin) |
| `bz_fa_seen` | 2 | bz_firstalbum.py L9 | bz_firstalbum.py |
| `bz_xinfo` | 2 | bz_cmd.py L134 | Custom_1111_XInfo.xml, bz_cmd.py |
| `bz_warm_ready_` | 2 | bz_warmgate.py L145 | bz_warmgate.py |
| `bz_longt` | 2 | bz_flip.py L126 | bz_flip.py |
| `bz_sway_pulse2` | 2 | bz_flip.py L217 | bz_flip.py |
| `bz_movposter_hold` | 2 | bz_flip.py L370 | bz_flip.py |
| `bz_movfanart_hold` | 2 | bz_flip.py L373 | bz_flip.py |
| `bz_music_underlay` | 2 | bz_flip.py L632 | bz_flip.py, bz_mm.py |
| `bz_randpend` | 2 | bz_flip.py L678 | bz_flip.py |
| `bz_logospin` | 2 | bz_flip.py L979 | bz_flip.py |
| `bz_warmrow` | 2 | bz_flip.py L1138 | bz_flip.py |
| `bz_srclab` | 1 | Custom_1132_BzSources.xml L9 | Custom_1117_MediaSources.xml |
| `bz_srcwin` | 1 | Custom_1132_BzSources.xml L10 | Custom_1117_MediaSources.xml |
| `bz_srcpath` | 1 | Custom_1132_BzSources.xml L10 | Custom_1117_MediaSources.xml |
| `bz_am_thumb` | 1 | Includes_Bezel.xml L377 | bz_artist.py |
| `bz_am_n1` | 1 | Includes_Bezel.xml L378 | bz_artist.py |
| `bz_am_counts` | 1 | Includes_Bezel.xml L380 | bz_artist.py |
| `bz_sd_thumb` | 1 | Includes_Bezel.xml L390 | — (read-only / Skin) |
| `bz_sd_n1` | 1 | Includes_Bezel.xml L391 | — (read-only / Skin) |
| `bz_sd_meta` | 1 | Includes_Bezel.xml L394 | — (read-only / Skin) |
| `bz_sd_alb` | 1 | Includes_Bezel.xml L395 | — (read-only / Skin) |
| `bz_tv_up` | 1 | Includes_Bezel.xml L498 | MyMusicNav.xml, MyVideoNav.xml |
| `bz_from_video` | 1 | Includes_Bezel.xml L1172 | bz_cmd.py |
| `bz_cov_next` | 1 | Includes_Bezel.xml L1194 | bz_flip.py |
| `bz_clr_a` | 1 | Includes_Bezel.xml L2461 | — (read-only / Skin) |
| `bz_clr_b` | 1 | Includes_Bezel.xml L2462 | — (read-only / Skin) |
| `bz_dra_ma` | 1 | Includes_Bezel.xml L2503 | — (read-only / Skin) |
| `bz_dra_ms` | 1 | Includes_Bezel.xml L2503 | — (read-only / Skin) |
| `bz_dra_pa` | 1 | Includes_Bezel.xml L2505 | — (read-only / Skin) |
| `bz_dra_ps` | 1 | Includes_Bezel.xml L2505 | — (read-only / Skin) |
| `bz_dra_0a` | 1 | Includes_Bezel.xml L2507 | — (read-only / Skin) |
| `bz_dra_0s` | 1 | Includes_Bezel.xml L2507 | — (read-only / Skin) |
| `bz_dra_0t` | 1 | Includes_Bezel.xml L2507 | — (read-only / Skin) |
| `bz_drb_ma` | 1 | Includes_Bezel.xml L2513 | — (read-only / Skin) |
| `bz_drb_ms` | 1 | Includes_Bezel.xml L2513 | — (read-only / Skin) |
| `bz_drb_pa` | 1 | Includes_Bezel.xml L2515 | — (read-only / Skin) |
| `bz_drb_ps` | 1 | Includes_Bezel.xml L2515 | — (read-only / Skin) |
| `bz_drb_0a` | 1 | Includes_Bezel.xml L2517 | — (read-only / Skin) |
| `bz_drb_0s` | 1 | Includes_Bezel.xml L2517 | — (read-only / Skin) |
| `bz_drb_0t` | 1 | Includes_Bezel.xml L2517 | — (read-only / Skin) |
| `bz_pfanart` | 1 | Includes_Bezel.xml L2589 | bz_flip.py |
| `bz_mart_a` | 1 | Includes_Bezel.xml L2622 | — (read-only / Skin) |
| `bz_mart_b` | 1 | Includes_Bezel.xml L2622 | — (read-only / Skin) |
| `bz_npmlabel` | 1 | Includes_Bezel.xml L3020 | Custom_1121_MusicFanartFS.xml, Includes_Bezel.xml |
| `bz_xi_year` | 1 | Includes_Bezel.xml L3496 | — (read-only / Skin) |
| `bz_xi_details` | 1 | Includes_Bezel.xml L3500 | — (read-only / Skin) |
| `bz_xi_plot` | 1 | Includes_Bezel.xml L3502 | — (read-only / Skin) |
| `bz_xi_cast0_role` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast0_thumb` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast1_role` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast1_thumb` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast2_role` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast2_thumb` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast3_role` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast3_thumb` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast4_role` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast4_thumb` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast5_role` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast5_thumb` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast6_role` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast6_thumb` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast7_role` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast7_thumb` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast8_role` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast8_thumb` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast9_role` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast9_thumb` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast10_role` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast10_thumb` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast11_role` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_xi_cast11_thumb` | 1 | Includes_Bezel.xml L3522 | — (read-only / Skin) |
| `bz_ms_n_video` | 1 | Custom_1117_MediaSources.xml L21 | — (read-only / Skin) |
| `bz_ms_n_music` | 1 | Custom_1117_MediaSources.xml L28 | — (read-only / Skin) |
| `bz_ms_n_pictures` | 1 | Custom_1117_MediaSources.xml L35 | — (read-only / Skin) |
| `bz_adgo` | 1 | AddonBrowser.xml L24 | bz_set.py |
| `bz_vs_name` | 1 | Custom_1115_MusicControls.xml L46 | bz_vizset.py |
| `bz_vs_n` | 1 | Custom_1115_MusicControls.xml L47 | bz_vizset.py |
| `bz_ad_n_video` | 1 | Custom_1131_BzAddons.xml L27 | — (read-only / Skin) |
| `bz_ad_n_audio` | 1 | Custom_1131_BzAddons.xml L28 | — (read-only / Skin) |
| `bz_ad_n_exec` | 1 | Custom_1131_BzAddons.xml L29 | — (read-only / Skin) |
| `bz_ad_n_svc` | 1 | Custom_1131_BzAddons.xml L30 | — (read-only / Skin) |
| `bz_ad_n_skin` | 1 | Custom_1131_BzAddons.xml L31 | — (read-only / Skin) |
| `bz_ad_n_all` | 1 | Custom_1131_BzAddons.xml L32 | — (read-only / Skin) |
| `bz_np_focus` | 1 | MyMusicNav.xml L25 | MyMusicNav.xml |
| `bz_fa_busy` | 1 | bz_firstalbum.py L9 | bz_firstalbum.py |
| `bz_quit_dtap` | 1 | bz_cmd.py L24 | bz_dtap.py |
| `bz_km_loaded` | 1 | bz_cmd.py L52 | bz_cmd.py, bz_km.py |
| `bz_flip_ver` | 1 | bz_cmd.py L70 | bz_flip.py |
| `bz_backdrop_last` | 1 | bz_cmd.py L83 | AddonBrowser.xml, FileManager.xml, MyFavourites.xml, MyGames.xml, MyPlaylist.xml, MyPrograms.xml, Settings.xml |
| `bz_xi_dbtype` | 1 | bz_cmd.py L191 | — (read-only / Skin) |
| `bz_xi_dbid` | 1 | bz_cmd.py L191 | — (read-only / Skin) |
| `bz_vistoggle_t` | 1 | bz_cmd.py L256 | bz_cmd.py |
| `bz_qs_audio` | 1 | bz_cmd.py L389 | bz_cmd.py |
| `bz_grid_target` | 1 | bz_cmd.py L484 | bz_flip.py |
| `bz_vosdc` | 1 | bz_cmd.py L542 | bz_cmd.py |
| `bz_started` | 1 | bz_cmd.py L631 | bz_cmd.py |
| `bz_artback` | 1 | bz_cmd.py L714 | Includes_BezelChooseArt.xml, bz_cmd.py |
| `bz_warmgate_running` | 1 | bz_warmgate.py L93 | bz_warmgate.py |
| `bz_adx_seen` | 1 | bz_set.py L90 | bz_set.py |
| `bz_msx_seen` | 1 | bz_set.py L98 | bz_set.py |
| `bz_lp` | 1 | bz_flip.py L128 | bz_flip.py |
| `bz_sway_restart` | 1 | bz_flip.py L192 | Includes_Tuner.xml, MusicVisualisation.xml, MyMusicNav.xml, MyPlaylist.xml, bz_flip.py |
| `bz_sway_t0` | 1 | bz_flip.py L201 | bz_flip.py |
| `bz_back_pick` | 1 | bz_flip.py L267 | Includes_Bezel.xml, bz_flip.py |
| `bz_back_close` | 1 | bz_flip.py L272 | Includes_Bezel.xml, MyMusicNav.xml, bz_flip.py |
| `bz_back_ret` | 1 | bz_flip.py L275 | — (read-only / Skin) |
| `bz_allret` | 1 | bz_flip.py L316 | bz_cmd.py, bz_flip.py |
| `bz_pfkey` | 1 | bz_flip.py L406 | bz_flip.py |
| `bz_vback_fade` | 1 | bz_flip.py L423 | MyVideoNav.xml, bz_flip.py |
| `bz_vback_close` | 1 | bz_flip.py L426 | Includes_Bezel.xml, MyVideoNav.xml, bz_flip.py |
| `bz_vback_key` | 1 | bz_flip.py L426 | bz_flip.py |
| `bz_tabq` | 1 | bz_flip.py L931 | bz_flip.py |
| `bz_setret` | 1 | bz_flip.py L1045 | Custom_1130_BzSettings.xml, bz_flip.py |
| `bz_dr` | 1 | bz_flip.py L1254 | bz_flip.py |
| `bz_dtap_running` | 1 | bz_dtap.py L110 | bz_dtap.py |
| `bz_tune_dirty` | 1 | bz_dtap.py L126 | Includes_Tuner.xml, bz_cmd.py, bz_dtap.py, bz_tune.py |

### Settings mirror (bz_set_*)
| prop | reads | first read | setters |
|---|---|---|---|
| `bz_set_videolibrary_updateonstartup` | 2 | Custom_1117_MediaSources.xml L26 | — (read-only / Skin) |
| `bz_set_musiclibrary_updateonstartup` | 2 | Custom_1117_MediaSources.xml L33 | — (read-only / Skin) |
| `bz_set_lookandfeel_enablerssfeeds` | 2 | Custom_1130_BzSettings.xml L48 | — (read-only / Skin) |
| `bz_set_screensaver_usedimonpause` | 2 | Custom_1130_BzSettings.xml L49 | — (read-only / Skin) |
| `bz_set_videolibrary_backgroundupdate` | 1 | Custom_1117_MediaSources.xml L37 | — (read-only / Skin) |
| `bz_set_filelists_showextensions` | 1 | Custom_1130_BzSettings.xml L35 | — (read-only / Skin) |
| `bz_set_filelists_ignorethewhensorting` | 1 | Custom_1130_BzSettings.xml L36 | — (read-only / Skin) |
| `bz_set_myvideos_selectaction` | 1 | Custom_1130_BzSettings.xml L37 | — (read-only / Skin) |
| `bz_set_filelists_showhidden` | 1 | Custom_1130_BzSettings.xml L38 | — (read-only / Skin) |
| `bz_set_services_devicename` | 1 | Custom_1130_BzSettings.xml L79 | — (read-only / Skin) |
| `bz_set_services_upnp` | 1 | Custom_1130_BzSettings.xml L80 | — (read-only / Skin) |
| `bz_set_services_webserver` | 1 | Custom_1130_BzSettings.xml L81 | — (read-only / Skin) |
| `bz_set_services_esenabled` | 1 | Custom_1130_BzSettings.xml L82 | — (read-only / Skin) |
| `bz_set_services_airplay` | 1 | Custom_1130_BzSettings.xml L83 | — (read-only / Skin) |
| `bz_set_services_zeroconf` | 1 | Custom_1130_BzSettings.xml L84 | — (read-only / Skin) |
| `bz_set_videoplayer_adjustrefreshrate` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_videoplayer_usedisplayasclock` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_audiooutput_passthrough` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_audiooutput_guisoundmode` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_audiooutput_streamsilence` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_audiooutput_volumesteps` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_input_enablemouse` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_input_enablejoystick` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_powermanagement_displaysoff` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_powermanagement_shutdowntime` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_debug_showloginfo` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_eventlog_enabled` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_lookandfeel_skinzoom` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_screensaver_time` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_gamesgeneral_enable` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_gamesgeneral_showosdhelp` | 1 | Custom_1130_BzSettings.xml L102 | — (read-only / Skin) |
| `bz_set_general_addonupdates` | 1 | Custom_1131_BzAddons.xml L36 | — (read-only / Skin) |
| `bz_set_general_addonnotifications` | 1 | Custom_1131_BzAddons.xml L37 | — (read-only / Skin) |
| `bz_set_addons_unknownsources` | 1 | Custom_1131_BzAddons.xml L38 | — (read-only / Skin) |

### Persistent skin settings (`Skin.HasSetting/String`)
| setting | refs |
|---|---|
| `bz_at_spinspd` | 3687 |
| `bz_spin_ccw` | 3421 |
| `bz_at_mmdim` | 562 |
| `bz_at_fsshop` | 518 |
| `bz_at_fsshmix` | 417 |
| `bz_at_fsshtint` | 387 |
| `bz_at_acx` | 341 |
| `bz_at_d3lit` | 317 |
| `bz_at_d20ffade` | 313 |
| `bz_at_d20fslide` | 313 |
| `bz_at_d20mfade` | 313 |
| `bz_at_d20mslide` | 313 |
| `bz_at_d20sfade` | 313 |
| `bz_at_pd3lit` | 295 |
| `bz_at_pcx` | 281 |
| `bz_at_lspinspd` | 277 |
| `bz_at_plspinspd` | 277 |
| `bz_at_blockcol` | 232 |
| `bz_topen_resetsys` | 217 |
| `bz_at_fschromecol` | 207 |
| `bz_at_blockop` | 200 |
| `bz_at_epease` | 198 |
| `bz_at_eposlide` | 192 |
| `bz_at_fschromeop` | 189 |
| `bz_at_fanop` | 179 |
| `bz_amb_below` | 174 |
| `bz_amb_off` | 173 |
| `bz_at_fsshdist` | 166 |
| `bz_at_pingspeed` | 142 |
| `bz_at_fsshang` | 133 |
| `bz_at_fsslide` | 129 |
| `bz_at_mmbar` | 124 |
| `bz_lspin_cw` | 121 |
| `bz_plspin_cw` | 121 |
| `bz_at_d3glow` | 118 |
| `bz_at_logocol` | 114 |
| `bz_at_logoop` | 114 |
| `bz_sec_popin` | 97 |
| `bz_at_flip` | 88 |
| `bz_at_rowscroll` | 88 |
| `bz_at_zoomtime` | 88 |
| `bz_at_cascspeed` | 88 |
| `bz_at_cascstag` | 88 |
| `bz_at_menuopen` | 88 |
| `bz_at_menuclose` | 88 |
| `bz_at_mctrl` | 88 |
| `bz_at_mmglowsty` | 84 |
| `bz_at_swaypause` | 78 |
| `bz_at_fanart` | 78 |
| `bz_at_dtapwin` | 78 |
| `bz_at_d3speed` | 78 |
| `bz_at_phold` | 78 |
| `bz_at_aclen` | 74 |
| `bz_at_acy` | 74 |
| `bz_at_gbdop` | 71 |
| `bz_at_fsvizop` | 71 |
| `bz_at_acstyle` | 68 |
| `bz_at_d20fbri` | 64 |
| `bz_at_d20mbri` | 64 |
| `bz_at_d20sbri` | 64 |
| `bz_at_pclen` | 62 |
| `bz_at_pcy` | 62 |
| `bz_at_agltint` | 60 |
| `bz_at_pgltint` | 60 |
| `bz_at_hicol` | 60 |
| `bz_d3l0_off` | 59 |
| `bz_d3l1_off` | 59 |
| `bz_spin_off` | 59 |
| `bz_topen_dust` | 59 |
| `bz_at_hiop` | 59 |
| `bz_at_mmxfade` | 58 |
| `bz_at_d3goff` | 58 |
| `bz_at_aglop` | 57 |
| `bz_at_pglop` | 57 |
| `bz_at_gbdcol` | 54 |
| `bz_at_shadowop` | 54 |
| `bz_at_mmdbright` | 53 |
| `bz_at_d3amb` | 53 |
| `bz_at_mmdfade` | 52 |
| `bz_at_mmwarm` | 52 |
| `bz_at_hishape` | 50 |
| `bz_blockcol` | 46 |
| `bz_at_acop` | 46 |
| `bz_at_gdim` | 43 |
| `bz_at_fsshblur` | 43 |
| `bz_at_aglstyle` | 41 |
| `bz_at_pglstyle` | 41 |
| `bz_at_pcop` | 40 |
| `bz_at_mmsecfade` | 38 |
| `bz_at_zoomsize` | 38 |
| `bz_at_mmdslide` | 37 |
| `bz_at_pcstyle` | 37 |
| `bz_at_ashstyle` | 35 |
| `bz_at_fsemb` | 35 |
| `bz_topen_albumposter` | 34 |
| `bz_at_d3dens` | 33 |
| `bz_at_fibamt` | 33 |
| `bz_at_flkamt` | 33 |
| `bz_at_pfibamt` | 33 |
| `bz_at_pflkamt` | 33 |
| `bz_at_fslp` | 33 |
| `bz_at_shadowtex` | 33 |
| `bz_at_rowsoft` | 33 |
| `bz_at_fsglow` | 32 |
| `bz_at_autonp` | 32 |
| `bz_at_ashop` | 31 |
| `bz_at_abfade` | 30 |
| `bz_at_d3lsize` | 29 |
| `bz_at_pd3lsize` | 29 |
| `bz_at_sdbright` | 28 |
| `bz_at_mmglow` | 26 |
| `bz_at_fsttlsize` | 26 |
| `bz_at_ashsize` | 26 |
| `bz_at_ashshape` | 26 |
| `bz_at_acsoft` | 25 |
| `bz_at_pcsoft` | 25 |
| `bz_swayright` | 25 |
| `bz_topen_mainmenu` | 25 |
| `bz_at_mmdsize` | 24 |
| `bz_topen_fsmusic` | 24 |
| `bz_at_d20fdens` | 20 |
| `bz_at_d20mdens` | 20 |
| `bz_at_d20sdens` | 20 |
| `bz_grid_music` | 20 |
| `bz_at_d20fsize` | 20 |
| `bz_at_d20msize` | 20 |
| `bz_at_d20ssize` | 20 |
| `bz_dfs_mode` | 19 |
| `bz_at_d3asize` | 18 |
| `bz_at_sdsize` | 18 |
| `bz_topen_posterglare` | 16 |
| `bz_topen_fs_overlay` | 16 |
| `bz_topen_look` | 16 |
| `bz_dust_off` | 15 |
| `bz_fssh_off` | 15 |
| `bz_ps_art` | 14 |
| `bz_ps_list` | 14 |
| `bz_ps_menu` | 14 |
| `bz_ps_music` | 14 |
| `bz_ps_dust` | 14 |
| `bz_fib_off` | 13 |
| `bz_flk_off` | 13 |
| `bz_pfib_off` | 13 |
| `bz_pflk_off` | 13 |
| `bz_bigalb_off` | 13 |
| `bz_topen_al_shadow` | 13 |
| `bz_topen_d20poster` | 12 |
| `bz_topen_d20album` | 12 |
| `bz_topen_about` | 11 |
| `bz_topen_list` | 10 |
| `bz_at_mmdef` | 10 |
| `bz_albumlist` | 9 |
| `bz_tvclear_off` | 9 |
| `bz_npmode` | 9 |
| `bz_at_gbdsty` | 9 |
| `bz_topen_warmsys` | 9 |
| `bz_at_mmsecdepth` | 9 |
| `bz_fs_pill_off` | 8 |
| `bz_topen_p_shadow` | 8 |
| `bz_topen_d20spin` | 8 |
| `bz_at_glareop` | 8 |
| `bz_at_epdim` | 8 |
| `bz_bdop` | 7 |
| `bz_topen_d20far` | 7 |
| `bz_topen_d20mid` | 7 |
| `bz_topen_all` | 7 |
| `bz_grid_video` | 6 |
| `bz_at_busydelay` | 6 |
| `bz_topen_al_dust` | 6 |
| `bz_topen_d20menu` | 6 |
| `bz_at_glaretex` | 6 |
| `bz_alit20` | 5 |
| `bz_plit20` | 5 |
| `bz_albview_a` | 5 |
| `bz_acast_static` | 5 |
| `bz_pcast_static` | 5 |
| `bz_at_pdust` | 5 |
| `bz_topen_al_glare` | 5 |
| `bz_topen_p_glare` | 5 |
| `bz_topen_warm20` | 5 |
| `bz_topen_music` | 5 |
| `bz_adust_off` | 4 |
| `bz_dtap_off` | 4 |
| `bz_topen_colourblock` | 4 |
| `bz_topen_autoadv` | 4 |
| `bz_topen_al_sway` | 4 |
| `bz_lspin_off` | 3 |
| `bz_plspin_off` | 3 |
| `bz_fs_fanartpop` | 3 |
| `bz_m1121_off` | 3 |
| `bz_gstyle_music` | 3 |
| `bz_gstyle_video` | 3 |
| `bz_at_warmhold` | 3 |
| `bz_at_warmsplash` | 3 |
| `bz_uadv_off` | 3 |
| `bz_topen_al_size` | 3 |
| `bz_topen_fs_viz` | 3 |
| `bz_topen_fs_clear` | 3 |
| `bz_fs_layout` | 3 |
| `bz_sdust_off` | 3 |
| `bz_at_warmmusicposters` | 2 |
| `bz_mmdust_off` | 2 |
| `bz_fschrome_fan` | 2 |
| `bz_fs_ttl_off` | 2 |
| `bz_fs_prog_off` | 2 |
| `bz_fs_tbar_off` | 2 |
| `bz_npmlbl_off` | 2 |
| `bz_at_mmdamt` | 2 |
| `bz_uadv_delay` | 2 |
| `bz_uadv_hold` | 2 |
| `bz_topen_p_sway` | 2 |
| `bz_bdimg` | 2 |
| `bz_topen_system` | 2 |
| `bz_blockcol_name` | 2 |
| `bz_at_lkgloss` | 2 |
| `bz_at_lkchrome` | 2 |
| `bz_at_lksatin` | 2 |
| `bz_at_lkfrost` | 2 |
| `bz_at_lkvig` | 2 |
| `bz_at_lkgrain` | 2 |
| `bz_at_lkleak` | 2 |
| `bz_at_lkholo` | 2 |
| `bz_at_lkprism` | 2 |
| `bz_at_lkrainbow` | 2 |
| `bz_d3l2_off` | 2 |
| `bz_dust_nocut` | 2 |
| `bz_pndlg_off` | 1 |
| `bz_lastart_music` | 1 |
| `bz_lastart_movies` | 1 |
| `bz_lastart_tv` | 1 |
| `bz_lastart_mv` | 1 |
| `bz_last_mmsub_music` | 1 |
| `bz_last_mmsub_movies` | 1 |
| `bz_last_mmsub_tv` | 1 |
| `bz_defseed` | 1 |
| `bz_at_` | 1 |
| `bz_topen_albumglare` | 1 |
| `bz_topen_albumshadow` | 1 |
| `bz_at_mmidle` | 1 |
| `bz_mclogo_off` | 1 |
| `bz_idlerock` | 1 |
| `bz_at_breathe` | 1 |
| `bz_at_glow0` | 1 |
| `bz_at_glow1` | 1 |
| `bz_at_glow2` | 1 |
| `bz_at_glow3` | 1 |
| `bz_at_glow4` | 1 |
| `bz_precache_off` | 1 |
| `bz_debug_mm` | 1 |
| `bz_allseasons` | 1 |
| `bz_allalbums` | 1 |
| `bz_ctl_backdrop` | 1 |
