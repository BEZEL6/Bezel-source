// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#include "DebugOverlay.h"
#include "AudioEnvelopes.h"
#include "Sprites.h"
#include <kodi/General.h>
namespace bezel {
void DebugOverlay::Draw(Sprites& sp, const AudioEnvelopes& e, float fps, const std::string& style, size_t n) {
  float v[3] = {e.low, e.mid, e.high};
  for (int i = 0; i < 3; ++i) { Quad q; q.size = {0.02f, 0.01f + v[i]*0.2f}; q.pos = {-0.95f + i*0.05f, -0.9f + q.size.y}; q.col = {0.2f+i*0.3f, 1, 0.3f, 0.8f}; sp.Push(q, 0); }
  sp.Flush(false);
  if ((m_logT += 1.f / (fps > 1 ? fps : 60)) > 5) { m_logT = 0; kodi::Log(ADDON_LOG_DEBUG, "BezelViz fps=%.1f style=%s particles=%zu L/M/H=%.2f/%.2f/%.2f", fps, style.c_str(), n, e.low, e.mid, e.high); }
}
}
