// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#include "Particles.h"
#include <algorithm>
namespace bezel {
static float rnd(unsigned& s){ s = s * 1664525u + 1013904223u; return (s >> 8) / 16777216.f; }
void Particles::SetCap(int c){ m_cap = std::clamp(c, 0, kHardParticleCap); if ((int)m_items.size() > m_cap) m_items.resize(m_cap); }
void Particles::Update(float dt, float rate, float parallax) {
  m_acc += rate * dt;
  while (m_acc >= 1 && (int)m_items.size() < m_cap) {
    Particle q; q.p = {rnd(m_seed)*2-1, rnd(m_seed)*2-1}; q.depth = rnd(m_seed); q.life = 3 + rnd(m_seed)*4;
    q.size = 0.01f + 0.04f*q.depth; m_items.push_back(q); m_acc -= 1;
  }
  if (m_acc > 1) m_acc = 1;
  for (auto& q : m_items) { float s = 0.3f + parallax*q.depth; q.p.x += q.v.x*dt*s; q.p.y += q.v.y*dt*s; q.life -= dt; /* STUB: q.frame sprite-sheet advance */ }
  m_items.erase(std::remove_if(m_items.begin(), m_items.end(), [](const Particle& q){ return q.life <= 0; }), m_items.end());
}
}
