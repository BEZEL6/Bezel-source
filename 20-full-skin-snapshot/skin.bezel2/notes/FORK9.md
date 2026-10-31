# FORK 9 — 5.33.9 (Oct 29 2026)
Rob t126: sections can switch Cascade ↔ Pop-in.
- Tuner LIST › **Section list anim** (id secanim, toggle, skin bool `bz_sec_popin`; unset = Cascade default). Info art `media/bezel/info/sec_anim_style.png` (900×580).
- Includes_Bezel.xml: the 6 list-60 cascade row groups (l.1423/1444/1713/1734/2464/2473) — cascade anims gated `+ !Skin.HasSetting(bz_sec_popin)`; added Pop-in anim (zoom 92→100 back-out 220 ms + fade 180 ms, no stagger) on the same `bz_casc=a` trigger. Same mechanism, fixed in place.
- Universal bar untouched; no scroll changes; non-section popups stay Pop-in (Animation_DialogPopupOpenClose).
- addon.xml 5.33.8 "fork.7" → 5.33.9 "BEZEL 5.33-fork.9".
- Backup: /workspace/bezel-533-fork/bak_5.33.8_pre_secanim. No zip. K40 not touched.
