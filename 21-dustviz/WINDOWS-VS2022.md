# Windows VS2022 build (not run here)

This environment has no DirectX 11 compiler or Windows SDK. Do not treat any GL screenshot as a Windows runtime test.

Source root (addon id = directory name):

`21-dustviz\visualization.bezel`

That directory contains `CMakeLists.txt`, `src\`, and `visualization.bezel\resources\packs\topbar_smear\` (textures + manifest). `APP_RENDER_SYSTEM` is forced to `dx11` when `WIN32` is set. GL and GLES shader files are still in `resources\shaders`.

From a Visual Studio 2022 x64 developer prompt, with a Kodi source tree that can build binary addons:

```
cmake -G "Visual Studio 17 2022" -A x64 -DCMAKE_BUILD_TYPE=Release ^
  -DADDONS_TO_BUILD=visualization.bezel ^
  -DADDON_SRC_PREFIX=C:\path\to\Bezel-source\21-dustviz ^
  -DCMAKE_INSTALL_PREFIX=C:\kodi-addons-out ^
  C:\path\to\xbmc\cmake\addons
cmake --build . --config Release --target visualization.bezel
```

Direct configure if `KodiConfig.cmake` is already installed (same flags the Linux box script uses, with the Windows generator):

```
cmake -G "Visual Studio 17 2022" -A x64 -S C:\path\to\Bezel-source\21-dustviz\visualization.bezel -B C:\path\to\bezel-build ^
  -DCMAKE_BUILD_TYPE=Release ^
  -DAPP_RENDER_SYSTEM=dx11 ^
  -DKodi_DIR=C:\path\to\kodi\cmake ^
  -DKODI_INCLUDE_DIR=C:\path\to\kodi\include\kodi ^
  -DGLM_INCLUDE_DIR=C:\path\to\kodi\include
cmake --build C:\path\to\bezel-build --config Release
```

After install, confirm these exist next to the DLL:

- `resources\packs\topbar_smear\manifest.json`
- `resources\packs\topbar_smear\textures\cascade_trail.png` (and the other style PNGs, plus `smear_fall.png`)
- `resources\settings.xml` default `active_style` = `topbar_smear`, `smear_style` = `1`

Copying only the DLL, without `resources\packs`, is the previous failure mode (engine falls through to the solid placeholder). This document does not install anything into a Kodi user profile.
