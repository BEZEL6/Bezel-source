// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#include "Tuner.h"
#include <kodi/General.h>
#include <utility>
namespace bezel {
void Tuner::LoadSettings() {
  s.activeStyle = kodi::addon::GetSettingString("active_style", "topbar_smear");
  s.packRoot = kodi::addon::GetSettingString("pack_root", "");
  s.particleCap = kodi::addon::GetSettingInt("particle_cap", kDefaultParticleCap);
  s.intensity = kodi::addon::GetSettingInt("intensity", 100) / 100.f;
  s.idleMode = kodi::addon::GetSettingInt("idle_mode", 1);
  s.strobes = kodi::addon::GetSettingBoolean("strobes", false);
  s.debug = kodi::addon::GetSettingBoolean("debug_overlay", false);
  s.tbColumns = kodi::addon::GetSettingInt("topbar_columns", 0);
  s.tbFill = kodi::addon::GetSettingInt("topbar_colwidth", 0);
  s.tbAlign = kodi::addon::GetSettingInt("topbar_align", 0);
  s.tbColors = kodi::addon::GetSettingInt("topbar_colors", 0);
  s.tbHeight = kodi::addon::GetSettingInt("topbar_height", 100) / 100.f;
  s.tbOpacity = kodi::addon::GetSettingInt("topbar_opacity", 100) / 100.f;
  s.tbSens = kodi::addon::GetSettingInt("topbar_sens", 100) / 100.f;
  s.tbSmear = kodi::addon::GetSettingInt("topbar_smear", 100) / 100.f;
  s.tbBlur = kodi::addon::GetSettingInt("topbar_blur", 100) / 100.f;
  s.tbGlow = kodi::addon::GetSettingInt("topbar_glow", 100) / 100.f;
  s.tbThick = kodi::addon::GetSettingInt("topbar_thick", 100) / 100.f;
  s.tbRelease = kodi::addon::GetSettingInt("topbar_release", 100) / 100.f;
  s.tbOffX = kodi::addon::GetSettingInt("topbar_offx", 0) / 100.f;
  s.tbOffY = kodi::addon::GetSettingInt("topbar_offy", 0) / 100.f;
  s.smearStyle = kodi::addon::GetSettingInt("smear_style", 1);
  s.smearPlace = kodi::addon::GetSettingInt("smear_place", 0);
  OnSetting("hair_tex_opacity", std::to_string(kodi::addon::GetSettingInt("hair_tex_opacity", -5)));
  OnSetting("hair_opacity", std::to_string(kodi::addon::GetSettingInt("hair_opacity", 100)));
  OnSetting("hair_color", std::to_string(kodi::addon::GetSettingInt("hair_color", 0)));
  OnSetting("hair_artic_hang", std::to_string(kodi::addon::GetSettingInt("hair_artic_hang", -5)));
  for (auto& kv : {std::pair<const char*, int>{"hair_length", 100}, {"hair_hinges", 1}, {"hair_hinge2_pos", 55}, {"hair_hinge2_amt", 35}, {"hair_hinge3_pos", 80}, {"hair_hinge3_amt", 35}})
    OnSetting(kv.first, std::to_string(kodi::addon::GetSettingInt(kv.first, kv.second)));
  OnSetting("hair_artic_joint", std::to_string(kodi::addon::GetSettingInt("hair_artic_joint", -5)));
}
static float pctOrPack(const std::string& v) { int i = std::stoi(v); return i < 0 ? -1.f : i / 100.f; }
bool Tuner::OnSetting(const std::string& n, const std::string& v) {
  if (n == "active_style") s.activeStyle = v; else if (n == "pack_root") s.packRoot = v;
  else if (n == "particle_cap") s.particleCap = std::stoi(v); else if (n == "intensity") s.intensity = std::stoi(v) / 100.f;
  else if (n == "idle_mode") s.idleMode = std::stoi(v); else if (n == "strobes") s.strobes = v == "true";
  else if (n == "debug_overlay") s.debug = v == "true";
  else if (n == "topbar_columns") s.tbColumns = std::stoi(v); else if (n == "topbar_colwidth") s.tbFill = std::stoi(v);
  else if (n == "topbar_align") s.tbAlign = std::stoi(v); else if (n == "topbar_colors") s.tbColors = std::stoi(v);
  else if (n == "topbar_height") s.tbHeight = std::stoi(v) / 100.f;
  else if (n == "topbar_opacity") s.tbOpacity = std::stoi(v) / 100.f;
  else if (n == "topbar_sens") s.tbSens = std::stoi(v) / 100.f;
  else if (n == "topbar_smear") s.tbSmear = std::stoi(v) / 100.f;
  else if (n == "topbar_blur") s.tbBlur = std::stoi(v) / 100.f;
  else if (n == "topbar_glow") s.tbGlow = std::stoi(v) / 100.f;
  else if (n == "topbar_thick") s.tbThick = std::stoi(v) / 100.f;
  else if (n == "topbar_release") s.tbRelease = std::stoi(v) / 100.f;
  else if (n == "topbar_offx") s.tbOffX = std::stoi(v) / 100.f;
  else if (n == "topbar_offy") s.tbOffY = std::stoi(v) / 100.f;
  else if (n == "smear_style") s.smearStyle = std::stoi(v);
  else if (n == "smear_place") s.smearPlace = std::stoi(v);
  else if (n == "hair_tex_opacity") s.hairTexOpacity = pctOrPack(v);
  else if (n == "hair_opacity") s.hairOpacity = std::stoi(v) / 100.f;
  else if (n == "hair_color") s.hairColor = std::stoi(v);
  else if (n == "hair_artic_hang") s.articHang = pctOrPack(v);
  else if (n == "hair_artic_joint") s.articJoint = pctOrPack(v);
  else if (n == "hair_length") s.hairLen = std::stoi(v) / 100.f;
  else if (n == "hair_hinges") s.hinges = std::stoi(v);
  else if (n == "hair_hinge2_pos") s.hinge2Pos = std::stoi(v) / 100.f; else if (n == "hair_hinge2_amt") s.hinge2Amt = std::stoi(v) / 100.f;
  else if (n == "hair_hinge3_pos") s.hinge3Pos = std::stoi(v) / 100.f; else if (n == "hair_hinge3_amt") s.hinge3Amt = std::stoi(v) / 100.f;
  else return false;
  return true;
}
// Planned property names (Window(Home)): BezelViz.Style, BezelViz.Intensity, BezelViz.Pulse, BezelViz.FocusX/FocusY,
// BezelViz.Strobe, BezelViz.Pause. STUB: viz-side read path for window properties to be confirmed against Kodi API.
void Tuner::PollSkinProperties(float) {}
}
