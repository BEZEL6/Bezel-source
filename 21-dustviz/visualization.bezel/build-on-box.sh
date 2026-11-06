#!/usr/bin/env bash
set -euo pipefail
export PATH="/workspace/toolchain/debsys/usr/bin:/workspace/toolchain/cmake/bin:/workspace/toolchain/bin:$PATH"
ROOT=/workspace/visualization.bezel
mkdir -p "$ROOT/build" && cd "$ROOT/build"
cmake .. -DCMAKE_BUILD_TYPE=Debug -DAPP_RENDER_SYSTEM=gl \
  -DCMAKE_C_COMPILER=/workspace/toolchain/debsys/usr/bin/gcc-14 \
  -DCMAKE_CXX_COMPILER=/workspace/toolchain/debsys/usr/bin/g++-14 \
  -DKodi_DIR=/usr/lib/x86_64-linux-gnu/kodi/cmake
cmake --build . -j"$(nproc)"
# refresh addon.xml requires/library if cmake regenerated a thin one
python3 - <<'PY'
from pathlib import Path
p = Path('/workspace/visualization.bezel/build/visualization.bezel/addon.xml')
xml = '''<?xml version="1.0" encoding="UTF-8"?>
<addon id="visualization.bezel" version="0.2.1" name="Bezel Viz" provider-name="Rob / DustViz">
  <requires>
    <import addon="kodi.binary.global.main" minversion="2.0.0" version="2.0.2"/>
    <import addon="kodi.binary.global.gui" minversion="5.15.0" version="5.15.0"/>
    <import addon="kodi.binary.global.filesystem" minversion="1.1.7" version="1.1.8"/>
    <import addon="kodi.binary.instance.visualization" minversion="4.0.0" version="4.0.0"/>
  </requires>
  <extension point="xbmc.player.musicviz" library_linux="visualization.bezel.so.0.1.0"/>
  <extension point="xbmc.addon.metadata">
    <platform></platform>
    <license>GPL-2.0-or-later</license>
    <summary lang="en_GB">Bezel viz engine: soft sprite style packs driven by audio bins</summary>
    <description lang="en_GB">Bezel viz smear engine. Default pack topbar_smear is bundled in resources/packs. Styles: original plus cascade, side whip, neon rain, fog bloom, mirror, stagger.</description>
    <assets><icon>resources/icon.png</icon></assets>
  </extension>
</addon>
'''
p.write_text(xml)
PY
SHARE=/usr/share/kodi/addons/visualization.bezel
LIB=/usr/lib/x86_64-linux-gnu/kodi/addons/visualization.bezel
sudo mkdir -p "$SHARE/resources" "$LIB"
sudo cp "$ROOT/build/visualization.bezel/addon.xml" "$SHARE/"
sudo cp -a "$ROOT/visualization.bezel/resources/." "$SHARE/resources/"
sudo cp "$ROOT/build/visualization.bezel.so.0.1.0" "$LIB/"
sudo ln -sfn visualization.bezel.so.0.1.0 "$LIB/visualization.bezel.so.21.2"
sudo ln -sfn visualization.bezel.so.21.2 "$LIB/visualization.bezel.so"
mkdir -p "$HOME/.kodi/addons/visualization.bezel/resources"
cp "$ROOT/build/visualization.bezel/addon.xml" "$HOME/.kodi/addons/visualization.bezel/"
cp -f "$ROOT/build/visualization.bezel.so.0.1.0" "$HOME/.kodi/addons/visualization.bezel/"
cp -a "$ROOT/visualization.bezel/resources/." "$HOME/.kodi/addons/visualization.bezel/resources/"
echo "Installed visualization.bezel 0.2.1 (lib .so.0.1.0)"
