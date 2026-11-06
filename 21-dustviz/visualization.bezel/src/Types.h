// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#pragma once
#include <cstddef>
#include <string>
#include <vector>
namespace bezel {
// v1 engine-owned budget (Rob OK'd Nov 1 2026). Not Kodi limits; raise after Shield profiling.
constexpr int kMinLayers = 3, kDefaultLayers = 5, kMaxLayers = 12;    // light-behind, haze, dust, strobe/fx, debug
constexpr int kAtlasesPerPack = 1;                                   // one atlas per style pack
constexpr int kMinPackTextures = 4, kMaxPackTextures = 16;           // glow discs, sheets, warps
constexpr int kDefaultParticleCap = 400, kHardParticleCap = 2000;    // particles are the real throttle
constexpr float kSilenceThreshold = 0.02f, kSilenceSeconds = 1.5f;
struct Vec2 { float x = 0, y = 0; };
struct Color { float r = 1, g = 1, b = 1, a = 1; };
struct Quad { Vec2 pos; Vec2 size; float uv[4] = {0, 0, 1, 1}; Color col; float rot = 0.f, aspect = 1.f; };  // rot (rad) about pos in aspect-corrected space
enum class LayerKind { LightBehind, Haze, Dust, StrobeFx, Debug, HairMass, TopBar };   // TopBar: full-width multi-color bar, beat smears colors down + blur   // HairMass: spiked soft-mass radial flares (sunburst) around a hair anchor
} // namespace bezel
