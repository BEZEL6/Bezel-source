// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine) shared by GL + DX11 sprite backends
#pragma once
#include <algorithm>
#include <vector>
namespace bezel {
// chroma: 0 none, 1 key black only if no alpha channel, 2 always key black. px is RGBA8 (stb forced 4ch).
inline void ApplyChromaKey(unsigned char* px, int w, int h, int ch, int chroma) {
  if (chroma == 2 || (chroma == 1 && ch < 4)) {
    // Key out near-black background connected to the image border (flood fill), so dark clothes/eyes keep opacity.
    // Soft ramp on luma 0.03..0.12 to avoid fringing.
    auto lum = [&](int i){ unsigned char* p = px + i * 4; return std::max({p[0], p[1], p[2]}) / 255.f; };
    std::vector<unsigned char> seen(w * h, 0); std::vector<int> st;
    auto seed = [&](int x, int y){ int i = y * w + x; if (!seen[i] && lum(i) < 0.12f) { seen[i] = 1; st.push_back(i); } };
    for (int x = 0; x < w; ++x) { seed(x, 0); seed(x, h - 1); } for (int y = 0; y < h; ++y) { seed(0, y); seed(w - 1, y); }
    while (!st.empty()) { int i = st.back(); st.pop_back(); int x = i % w, y = i / w;
      float a = std::clamp((lum(i) - 0.03f) / 0.09f, 0.f, 1.f); px[i * 4 + 3] = (unsigned char)std::min<float>(px[i * 4 + 3], a * 255.f);
      if (x > 0) seed(x - 1, y); if (x < w - 1) seed(x + 1, y); if (y > 0) seed(x, y - 1); if (y < h - 1) seed(x, y + 1); }
  }
}
}
