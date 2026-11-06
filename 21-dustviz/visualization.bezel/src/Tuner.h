// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#pragma once
#include "Types.h"
namespace bezel {
// Addon settings + skin property reads. Skin -> Window(Home) properties only (no touch input to viz).
struct TunerState { std::string activeStyle = "topbar_smear", packRoot; int particleCap = kDefaultParticleCap, idleMode = 1, tbColumns = 0, tbFill = 0, tbAlign = 0, tbColors = 0;
                    int smearStyle = 1, smearPlace = 0;   // 0 original, 1 cascade..6 stagger; place 0 top, 1 bottom, 2 mirror
                    float tbHeight = 1, tbOpacity = 1, tbSens = 1, tbSmear = 1, tbBlur = 1, tbGlow = 1, tbThick = 1, tbRelease = 1, tbOffX = 0, tbOffY = 0;
                    float hairTexOpacity = -1.f, hairOpacity = 1.f, articHang = -1.f, articJoint = -1.f; int hairColor = 0;   // <0 = pack value
                    float hairLen = 1.f, hinge2Pos = 0.55f, hinge2Amt = 0.35f, hinge3Pos = 0.8f, hinge3Amt = 0.35f; int hinges = 1;   // multi-hinge (0 = off)
                    float intensity = 1.f; bool strobes = false, debug = false; };
class Tuner {
public:
  void LoadSettings();                                   // kodi::addon::GetSetting*
  bool OnSetting(const std::string& name, const std::string& value);
  void PollSkinProperties(float dt);                     // STUB: rate-limited Window(Home).Property(BezelViz.*) reads
  TunerState s;
};
}
