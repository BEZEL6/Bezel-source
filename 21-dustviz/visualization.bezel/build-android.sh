#!/usr/bin/env bash
# Builds the Shield (arm64-v8a GLES) addon zip. Only uses NDK + Kodi 21 headers (no full Kodi depends).
set -euo pipefail
export PATH="/workspace/toolchain/debsys/usr/bin:/workspace/toolchain/cmake/bin:/workspace/toolchain/bin:$PATH"
N=/workspace/android-tools/android-ndk-r28c; T=/workspace/android-tools; B=/workspace/visualization.bezel/build-android
rm -rf $B; mkdir -p $B; cd $B
cmake .. -DCMAKE_TOOLCHAIN_FILE=$N/build/cmake/android.toolchain.cmake -DANDROID_ABI=arm64-v8a -DANDROID_PLATFORM=android-21 \
  -DANDROID_STL=c++_static -DCMAKE_BUILD_TYPE=Release -DAPP_RENDER_SYSTEM=gles -DKodi_DIR=$T/kodi-android-cmake \
  -DKODI_INCLUDE_DIR=$T/inc/kodi -DGLM_INCLUDE_DIR=$T/inc -DCMAKE_INSTALL_PREFIX=$B/inst
make -j4 && make install
S=$(mktemp -d); mkdir -p $S/visualization.bezel
cp -r inst/share/kodi/addons/visualization.bezel/. $S/visualization.bezel/; find $S -name "*.bak*" -delete
$N/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-strip --strip-unneeded -o $S/visualization.bezel/visualization.bezel.so inst/lib/kodi/addons/visualization.bezel/visualization.bezel.so
sed -i 's#<platform></platform>#<platform>android</platform>#' $S/visualization.bezel/addon.xml
mkdir -p /workspace/deliverables/android
cd $S && python3 -c "import shutil;shutil.make_archive('/workspace/deliverables/android/visualization.bezel-0.2.1-smear-android-aarch64-gles','zip','.','visualization.bezel')"
echo done
