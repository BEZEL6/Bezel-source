// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#include "Forces.h"
#include <cmath>
namespace bezel {
void Forces::Apply(std::vector<Particle>& ps, const ForceParams& f, float dt) {
  for (auto& q : ps) {
    float dx = q.p.x - f.center.x, dy = q.p.y - f.center.y, r2 = dx*dx + dy*dy + 0.01f;
    q.v.x += (-dy * f.swirl + dx * f.pushBack / r2) * dt;   // swirl + radial push-back (beat)
    q.v.y += ( dx * f.swirl + dy * f.pushBack / r2 + f.drift) * dt;
    q.v.x += std::sin(q.p.y * 6.f) * f.warp * dt;           // soft warp STUB (cheap sine field)
    q.v.x *= 0.98f; q.v.y *= 0.98f;
  }
}
}
