# Bezel-source (organized by system)

Source: live Bezel **5.33.369** (`skin.bezel2`) — copies only, no code changes.
Built from the development tree; laptop Downloads stays for finished zips only.

Each numbered folder is one system. Overlap is intentional (e.g. splash ⊂ warm-gate).
`20-full-skin-snapshot/skin.bezel2` is the complete installable tree.

## Systems

- `01-skin-core/` — Addon root, fonts, colors, language, themes, shared includes entry
- `02-warm-system/` — WARM 2.0 underlay + warm-gate cold-start cache (mm-warm)
- `03-splash/` — Startup splash visuals (warm-gate UI) — overlaps warm-system; kept separate per request
- `04-tuner/` — Skin Settings Tuner (6970) rows and tune script
- `05-python-scripts/` — All Bezel Python scripts (current .py/.json only, no bak)
- `06-textures-media/` — All skin textures / media
- `07-mm-list/` — Main menu strip 6996
- `08-movies-list/` — Movies section list / posters
- `09-tv-list/` — TV Shows section list
- `10-music-list/` — Music section list / album strip
- `11-dust/` — Dust 2.0 / Dust3 particle system
- `12-keymaps/` — Bezel keymaps install/leave (zz_bezel2_*)
- `13-dialogue-fs/` — Dialogue FS 1120 / album mode
- `14-fanart-fs/` — Fanart FS / viz keys + touch
- `15-now-playing/` — Now Playing 1112 + NP bar
- `16-section-transitions/` — Section fade-in transitions
- `17-sway-animations/` — Shared sway / poster rotate / stub cast
- `18-dialogs-overlays/` — Busy, confirm, pause, context, search, power, info
- `19-behaviors-docs/` — Full behaviors/ documentation set (current .md only)
- `20-full-skin-snapshot/` — Complete skin.bezel2 5.33.369 tree snapshot for reference (current files; bak ignored). `media/` comes from the 5.33.365 full zip.

## Packaging note

mockups/ is excluded from this repo and from skin zips � design comps stay out of the Bezel package.

