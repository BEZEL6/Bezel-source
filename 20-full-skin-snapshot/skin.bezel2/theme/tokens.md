# Theme tokens

> **RETIRED 5.33.473.** This layer is frozen at 5.33.267 and may be out of date. The current port blueprint is the behavior file with the same name in [behaviors/](../behaviors/README.md) (Feel contract + Kodi implementation). Kept for history only.


**Last updated:** 2026-11-01 · 5.33.267 · **Status:** current-state, generated from live tree · [PORT_INDEX](../PORT_INDEX.md)

## Simple
Colours are ARGB hex (`AARRGGBB`). Each section has its own colour (Movies blue, TV green, Music cyan…) used on the MM strip and branding. Fonts are Ubuntu (Regular/Bold) with Raleway on the splash. Global Dim is a black scrim 30–100 % (default 60 %) always on under MM; glare and dim are Tuner-driven. Theme packs in `colors/*.xml` only swap 4 accent colours.

## Deep (rebuild detail)
### Base palette (`colors/defaults.xml`)
| name | ARGB |
|---|---|
| `dialog_tint` | `FF141414` |
| `background` | `FF000000` |
| `bg_image` | `FF909090` |
| `bg_overlay` | `30FFFFFF` |
| `black` | `FF000000` |
| `white` | `FFF0F0F0` |
| `grey` | `FFA0A0A0` |
| `blue` | `FF7ACAFE` |
| `red` | `FFCE4421` |
| `button_focus` | `FF0B5F86` |
| `button_alt_focus` | `8012A0C7` |
| `text_shadow` | `22000000` |
| `border_alpha` | `60FFFFFF` |
| `disabled` | `40FFFFFF` |
| `selected` | `FFFFB70F` |
| `invalid` | `FFFF0000` |
| `bz_addons` | `FFFF0000` |
| `bz_addons_d` | `FFC00000` |
| `bz_movies` | `FF0077CC` |
| `bz_movies_d` | `FF005A9C` |
| `bz_tv` | `FF3CB54A` |
| `bz_tv_d` | `FF2A8A35` |
| `bz_music` | `FF00B4E6` |
| `bz_music_d` | `FF0089B0` |
| `bz_pictures` | `FFF080C0` |
| `bz_pictures_d` | `FFB85C92` |
| `bz_system` | `FFE000E0` |
| `bz_system_d` | `FF9A009A` |
| `bz_info` | `FF0E77A8` |
| `bz_accent` | `FF29ABE2` |
| `bz_new` | `FF0F5C78` |
| `bz_recent` | `FF3A3A3A` |
| `bz_party` | `FFD01010` |
| `bz_fav` | `FF7A6448` |
| `bz_text` | `FFF0F0F0` |
| `bz_dim` | `FF808080` |
| `bz_r1` | `FF9E1B1E` |
| `bz_r2` | `FFA14A1E` |
| `bz_r3` | `FF9E6A1C` |
| `bz_r4` | `FF9C9A10` |
| `bz_r5` | `FF2E7D32` |
| `bz_r6` | `FF006B3C` |
| `bz_r7` | `FF00799E` |
| `bz_r8` | `FF00527E` |
| `bz_r9` | `FF1E2470` |
| `bz_r10` | `FF4E1E6E` |
| `bz_r11` | `FF9E0E5E` |
| `bz_r12` | `FF9E1030` |
| `bz_dimmed` | `FFEDEDED` |
| `bz_dimtext` | `FF8C8C8C` |
| `bz_dimoverlay` | `12000000` |

### Theme packs (`colors/<pack>.xml` override)
| pack | dialog_tint | button_focus | selected |
|---|---|---|---|
| brown | `FF282524` | `FF83513F` | `FFFF4400` |
| charcoal | `FF262626` | `FFA2A2A2` | `FFFFB70F` |
| chartreuse | `FF202920` | `FF4FAF00` | `FF24C6C9` |
| concrete | `FF242728` | `FF607D8B` | `FFFF8C00` |
| gold | `FF2B2B22` | `FFCFA700` | `FFFFF000` |
| green | `FF1F2722` | `FF24CA7A` | `FF14D519` |
| maroon | `FF262020` | `FFC40300` | `FF24C6C9` |
| midnight | `FF181B1E` | `FF2866A4` | `FF5BE5EE` |
| orange | `FF2B2621` | `FFFF9800` | `FFFFF100` |
| pink | `FF2B2225` | `FFE91E63` | `FF94D800` |
| rose | `FF251F24` | `FFFF8EC4` | `FFFF0261` |
| teal | `FF222A2A` | `FF009688` | `FFC67F03` |
| violet | `FF27222A` | `FFC050FF` | `FFFF0054` |

### Fonts (`xml/Font.xml`, default fontset)
| name | file | size |
|---|---|---|
| `bz_list_music` | Ubuntu-Regular.ttf | 28 |
| `bz_value_sm` | Ubuntu-Bold.ttf | 22 |
| `bz_bio` | Ubuntu-Regular.ttf | 19 |
| `bz_tiny` | Ubuntu-Regular.ttf | 21 |
| `bz_small_s` | Ubuntu-Regular.ttf | 19 |
| `bz_value_s` | Ubuntu-Bold.ttf | 22 |
| `bz_mini_title` | Ubuntu-Bold.ttf | 30 |
| `bz_mini_title28` | Ubuntu-Bold.ttf | 28 |
| `bz_plot_s` | Ubuntu-Regular.ttf | 20 |
| `bz_r22` | Ubuntu-Regular.ttf | 22 |
| `bz_b22` | Ubuntu-Bold.ttf | 22 |
| `bz_b32` | Ubuntu-Bold.ttf | 32 |
| `bz_b26` | Ubuntu-Bold.ttf | 26 |
| `bz_r20` | Ubuntu-Regular.ttf | 20 |
| `bz_r18` | Ubuntu-Regular.ttf | 18 |
| `bz_b18` | Ubuntu-Bold.ttf | 18 |
| `bz_r26` | Ubuntu-Regular.ttf | 26 |
| `bz_r21` | Ubuntu-Regular.ttf | 21 |
| `bz_b21` | Ubuntu-Bold.ttf | 21 |
| `bz_b46` | Ubuntu-Bold.ttf | 46 |
| `bz_b34` | Ubuntu-Bold.ttf | 34 |
| `bz_b60` | Ubuntu-Bold.ttf | 60 |
| `bz_b16` | Ubuntu-Bold.ttf | 16 |
| `bz_b15` | Ubuntu-Bold.ttf | 15 |
| `bz_b12` | Ubuntu-Bold.ttf | 12 |
| `bz_splash60` | Raleway-Light.ttf | 60 |
| `bz_splash_sup` | Raleway-SemiBold.ttf | 26 |
| `bz_ral21` | Raleway-SemiBold.ttf | 21 |
| `bz_splash_kv` | Ubuntu-Regular.ttf | 22 |
| `bz_fsttl_t1` | Ubuntu-Bold.ttf | 41 |
| `bz_fsttl_a1` | Ubuntu-Bold.ttf | 25 |
| `bz_fsttl_l1` | Ubuntu-Regular.ttf | 22 |
| `bz_fsttl_t3` | Ubuntu-Bold.ttf | 58 |
| `bz_fsttl_a3` | Ubuntu-Bold.ttf | 35 |
| `bz_fsttl_l3` | Ubuntu-Regular.ttf | 31 |
| `bz_list_music` | arial.ttf | 28 |
| `bz_value_sm` | Ubuntu-Bold.ttf | 22 |
| `bz_bio` | arial.ttf | 19 |
| `bz_tiny` | arial.ttf | 21 |
| `bz_small_s` | arial.ttf | 19 |
| `bz_value_s` | arial.ttf | 22 |
| `bz_mini_title` | arial.ttf | 30 |
| `bz_plot_s` | arial.ttf | 20 |
| `bz_r22` | arial.ttf | 22 |
| `bz_b22` | arial.ttf | 22 |
| `bz_b32` | arial.ttf | 32 |
| `bz_b26` | arial.ttf | 26 |
| `bz_r20` | arial.ttf | 20 |
| `bz_r18` | arial.ttf | 18 |
| `bz_b18` | arial.ttf | 18 |
| `bz_r26` | arial.ttf | 26 |
| `bz_r21` | arial.ttf | 21 |
| `bz_b21` | arial.ttf | 21 |
| `bz_b46` | arial.ttf | 46 |
| `bz_b34` | arial.ttf | 34 |
| `bz_b60` | arial.ttf | 60 |
| `bz_b16` | arial.ttf | 16 |
| `bz_b15` | arial.ttf | 15 |
| `bz_b12` | arial.ttf | 12 |
| `bz_splash60` | Raleway-Light.ttf | 60 |
| `bz_splash_sup` | Raleway-SemiBold.ttf | 26 |
| `bz_ral21` | Raleway-SemiBold.ttf | 21 |
| `bz_splash_kv` | Ubuntu-Regular.ttf | 22 |
| `bz_fsttl_t1` | arial.ttf | 40 |
| `bz_fsttl_a1` | arial.ttf | 25 |
| `bz_fsttl_l1` | arial.ttf | 22 |
| `bz_fsttl_t3` | arial.ttf | 55 |
| `bz_fsttl_a3` | arial.ttf | 35 |
| `bz_fsttl_l3` | arial.ttf | 31 |

### Dim / glare / opacity (Tuner-driven — values are Home props, see [home-properties](../state/home-properties.md))
| token | prop | notes |
|---|---|---|
| Global dim (MM closed) | `bz_at_gdim` | 30–100 %, default 60 %, always on; every under-MM panel inside `BezelSecDim`. Does **not** touch the big album. |
| MM dim (MM open) | `bz_at_mmdim` | separate from gdim (mmdim ≠ gdim, rule) |
| Album glare | `bz_at_aglop` / `bz_at_agltint` / `bz_at_aglstyle` → `$VAR[BzATGlare8C]`, `$VAR[BzATGlareTex]` | |
| Poster glare | `bz_at_pglop` / `bz_at_pgltint` / `bz_at_pglstyle` | |
| Bar opacity | `bz_at_mmbar` | 30–100 |
| Colour block | `bz_at_blockcol` / `bz_at_blockop` | LOOK row |
| Logo | `bz_at_logocol` / `bz_at_logoop` | |
| Shadow | `bz_at_shadowop` | |
| Highlight | `bz_at_hicol` / `bz_at_hiop` / `bz_at_hishape` | |
Strip branding: section name sits **inside** the colour strip (standing design).
