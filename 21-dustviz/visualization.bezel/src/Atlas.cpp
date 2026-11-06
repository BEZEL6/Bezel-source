// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#include "Atlas.h"
namespace bezel {
bool Atlas::AddRegion(const std::string& n, unsigned tex, int frames) {
  if ((int)m_regions.size() >= kMaxPackTextures) return false;
  AtlasRegion r; r.tex = tex; r.frames = frames; m_regions[n] = r; return true;
}
const AtlasRegion* Atlas::Find(const std::string& n) const { auto it = m_regions.find(n); return it == m_regions.end() ? nullptr : &it->second; }
}
