// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#pragma once
#include "Particles.h"
namespace bezel {
// Advection / swirl / push-back / soft warp (CPU fake). STUB-level math, tune later.
struct ForceParams { float drift = 0.05f, swirl = 0.3f, pushBack = 0.f, warp = 0.f; Vec2 center; };
class Forces { public: void Apply(std::vector<Particle>& ps, const ForceParams& f, float dt); };
}
