// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#pragma once
#include "Types.h"
#include <vector>
namespace bezel {
// Soft textured-quad batcher (GL/GLES, pass-through shader only). IMPLEMENTED minimal; per-texture batching.
class Sprites {
public:
  bool Init(const std::string& shaderDir);   // compiles pass-through vert/frag
  void DeInit();
  // PNG decode via stb_image. chroma: 0 none, 1 key black only if no alpha channel, 2 always key black.
  // Returns fallback soft disc on failure (never 0). w/h optional out.
  unsigned LoadTexturePNG(const std::string& path, int chroma = 0, int* w = nullptr, int* h = nullptr);
  unsigned LoadTextureKeep(const std::string& path) { unsigned t = LoadTexturePNG(path); if (!m_loaded.empty() && m_loaded.back() == t) m_loaded.pop_back(); return t; }  // survives pack reloads
  void FreeLoaded();                          // delete textures loaded for the previous pack
  void Begin(); void SetAdditive(bool a);     // flushes if blend mode changes
  float ViewportAspect() const;               // backend viewport w/h, 0 if unknown
  static void SetDevice(void* ctx);           // DX11: ID3D11DeviceContext* from Kodi Device(); no-op on GL
  void Push(const Quad& q, unsigned tex); void Flush(bool additive); void Flush() { Flush(m_add); }
#ifdef BEZEL_DX11
  // Nested DX state must be visible to SpritesDX11.cpp free helpers (MSVC C2248 if private).
  struct DX; DX* m_dx = nullptr;
#endif
private:
  std::vector<float> m_verts; unsigned m_curTex = 0, m_prog = 0, m_vbo = 0, m_fallbackTex = 0;
  std::vector<unsigned> m_loaded; bool m_add = true;
  int m_aPos = -1, m_aUv = -1, m_aCol = -1;
};
}
