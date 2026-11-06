// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#pragma once
#include "Types.h"
namespace bezel {
struct Particle { Vec2 p, v; float life = 0, size = 0.02f, depth = 0.5f; int frame = 0; };
// Particle pool with hard cap. IMPLEMENTED (minimal spawn/integrate); sprite-sheet frame STUB.
class Particles {
public:
  void SetCap(int cap);
  void Update(float dt, float spawnRate, float depthParallax);
  std::vector<Particle>& Items() { return m_items; }
private:
  std::vector<Particle> m_items; int m_cap = kDefaultParticleCap; float m_acc = 0; unsigned m_seed = 1234;
};
}
