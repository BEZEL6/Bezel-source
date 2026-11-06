// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#pragma once
#include "Types.h"
#include <map>
namespace bezel {
// One atlas per pack (kAtlasesPerPack). STUB: currently each named region = full texture.
struct AtlasRegion { unsigned tex = 0; float uv[4] = {0,0,1,1}; int frames = 1; };
class Atlas {
public:
  bool AddRegion(const std::string& name, unsigned tex, int frames = 1);   // enforces kMaxPackTextures
  const AtlasRegion* Find(const std::string& name) const;
  size_t Count() const { return m_regions.size(); }
private: std::map<std::string, AtlasRegion> m_regions;
};
}
