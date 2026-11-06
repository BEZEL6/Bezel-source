// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#pragma once
#include "AudioEnvelopes.h"
#include "Atlas.h"
#include "DebugOverlay.h"
#include "Forces.h"
#include "PackLoader.h"
#include "Particles.h"
#include "Sprites.h"
#include "Tuner.h"
#include "InVizTuner.h"
namespace bezel {
struct EngineCaps { int maxLayers = kMaxLayers; int maxTextures = kMaxPackTextures; int particleCap = kDefaultParticleCap; };
// Frame loop, layer stack (back->front), caps, idle/silence.
class Engine {
public:
  bool Init(const std::string& addonPath, const std::string& skinPath, bool gles);
  void DeInit();
  void ReloadPack();
  void OnAudio(const float* bins, size_t n) { m_env.Feed(bins, n, m_tuner.s.intensity); }
  void Frame(float dt);
  Tuner& GetTuner() { return m_tuner; }
private:
  void DrawLayer(const LayerDef& L, size_t idx, float idleFade);
  void DrawHair(const LayerDef& L, float e, float idleFade);
  void DrawCharacter(float idleFade);
  void DrawTopBar(const LayerDef& L, float e, float idleFade);
  std::vector<float> m_cols; float m_dt = 0.016f, m_tbBeat = 0.f;
  float Band(const LayerDef& L) const;
  AudioEnvelopes m_env; Particles m_parts; Forces m_forces; Sprites m_sprites; Atlas m_atlas;
  PackLoader m_loader; PackManifest m_pack; Tuner m_tuner; DebugOverlay m_debug; InVizTuner m_menu; EngineCaps m_caps;
  std::string m_skinPath, m_addonPath; float m_time = 0, m_fps = 60, m_idleFade = 1; bool m_ready = false;
  std::vector<float> m_layerEnv; unsigned m_charTex = 0, m_ovTex = 0; int m_charW = 16, m_charH = 9; float m_aspect = 16.f / 9.f;
  float m_hitBias = 0.f; int m_hitN = 0; bool m_hitArmed = true;   // per-thrash wild direction
  float m_img[4] = {-1, -1, 1, 1};   // character image rect in NDC (x0,y0,x1,y1), aspect-fitted
};
}
