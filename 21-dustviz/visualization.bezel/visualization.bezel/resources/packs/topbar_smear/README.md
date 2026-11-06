# topbar_smear — DustViz smear pack 0.2.1

Full-width audio bar with selectable smear styles. The engine setting `smear_style` picks the look (no pack reload):

| Style | id | Look |
| --- | --- | --- |
| Original | 0 | 0.2.0 column smear (`smear_fall` + `bar_soft` + `glow_disc`). Top placement matches the previous formula. |
| A Cascade | 1 | Liquid wavy glowing ribbons. Default. |
| B Side whip | 2 | Horizontal whip streaks off the bar. |
| C Neon rain | 3 | Fine short neon drops. |
| D Fog bloom | 4 | Soft wide color fog. |
| E Mirror | 5 | Tapered trails inward from the opposite edge as well. |
| F Stagger | 6 | Left-to-right delayed wave. |

Placement (`smear_place`): Top falls inward, Bottom rises inward, Mirror draws both. Style E always keeps a reflection of the other edge.

Textures are white RGB with shaped alpha so the palette vertex color tints them. Shipped inside the addon at `visualization.bezel/resources/packs/topbar_smear/` and here for `special://skin/viz.addons/`.
