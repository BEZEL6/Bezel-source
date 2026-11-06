// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#pragma once
#include "Types.h"
namespace bezel {
enum class Band { Low, Mid, High, Level };
// Grow/fade envelope for a layer, driven by one audio band (manifest "envelope").
struct EnvelopeDef { float attack = 0.05f, release = 0.4f, grow = 0.4f, fadeMin = 0.3f; };
struct LayerDef {
  std::string id; LayerKind kind = LayerKind::Dust; std::string texture; bool additive = true; float parallax = 0.5f;
  // hair / soft-mass extensions (role:"hair"); ignored by non-hair layers so solid_test is unchanged
  std::string role; Color color{1, 1, 1, 1}; Band band = Band::Level; float radius[2] = {0.1f, 0.2f}; float density = 0.5f;
  EnvelopeDef env; bool dissolve = false;
  // spiked radials: count, length/width as fraction of radius, jitter 0..1, drift rad/s, sway amplitude rad
  // keyframe pose morph (optional "pose" block): KEY0 rest hang <-> KEY1 wild halo, t = smoothstep(threshold,1,e)^knee
  bool pose = false; float restLen = 0.6f, wildLen = 1.4f, restArc = 2.5f, restHang = 1.2f, wildSpread = 3.0f,
        poseThreshold = 0.35f, poseKnee = 1.6f, tremble = 0.06f, poseGain = 1.f, wildBias = 0.f, idleMotion = 0.f, idleLean = 0.f, idleMorph = 0.f, biasVary = 0.f, idleRoam = 0.f, arcCenter = 0.f, timeScale = 1.f, edgeFade = 0.f, drift = 1.f, articJoint = 0.f, articHang = 0.f, articLift = 0.f, articSwing = 0.f; bool front = false;
  // topbar block (kind:"topbar")
  int columns = 48; float barH = 0.022f, barPulse = 0.4f, smearMax = 0.62f, hueSpan = 0.92f, sat = 0.85f, glow = 0.6f, blur = 1.8f, smearAlpha = 0.85f, colMix = 0.75f, colFill = 0.62f;
  int spikes = 12; float spikeLen = 1.0f, spikeWidth = 0.14f, jitter = 0.35f, spin = 0.05f, sway = 0.12f;
};
struct CharacterDef {
  bool present = false; std::string sprite;           // path relative to pack root
  float rect[4] = {0.3f, 0.18f, 0.4f, 0.78f};          // x,y,w,h in 0..1 screen space (y down)
  float anchor[3] = {0.5f, 0.3f, 0.11f};               // hair anchor x,y,r (0..1, r relative to height)
  std::string overlay; float overlayOpacity = 1.f;            // baked-hair overlay texture drawn over sprite (tunable alpha)
  std::string chroma = "auto";                         // auto: key out black if PNG has no alpha; "none"; "black"
};
struct PackManifest {
  std::string id, name, version, root;
  std::vector<LayerDef> layers;        // clamped to kMaxLayers
  std::vector<std::string> textures;   // clamped to kMaxPackTextures, one atlas
  CharacterDef character;
  int particleCap = kDefaultParticleCap; float spawnRate = 60.f, swirl = 0.3f, drift = 0.05f;
};
class PackLoader {
public:
  // order: settings override (pack_root) -> special://skin/viz.addons/
  static std::vector<std::string> CandidateRoots(const std::string& overrideRoot, const std::string& skinPath, const std::string& addonPath = {});
  bool Load(const std::vector<std::string>& roots, const std::string& packId, PackManifest& out);
  static PackManifest BuiltinDefault();   // used if no pack found (solid_test equivalent)
};
}
