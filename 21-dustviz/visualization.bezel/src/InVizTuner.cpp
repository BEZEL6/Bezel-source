// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine)
#include "InVizTuner.h"
#include "Sprites.h"
#include "Tuner.h"
#include <kodi/General.h>
#include <kodi/Filesystem.h>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <sstream>
namespace bezel {
static const char* kColors[] = {"PACK", "RED", "CRIMSON", "EMBER", "HOT PINK", "VIOLET", "WHITE"};
static const char* kHinges[] = {"OFF", "1", "2", "3"};
// -5 on pack-able knobs = use pack value (shown as PACK)
static const TunerItem kItems[] = {
  {"hair_color",       "HAIR COLOR",       0,   6,  1,   0, kColors, "HAIR"},
  {"hair_opacity",     "LIVE OPACITY %",  10, 200, 10, 100, nullptr, "HAIR"},
  {"hair_length",      "HAIR LENGTH %",   30, 250, 10, 100, nullptr, "HAIR"},
  {"hair_tex_opacity", "BAKED TEXTURE %", -5, 100,  5,  -5, nullptr, "HAIR"},
  {"hair_hinges",      "HINGES",           0,   3,  1,   1, kHinges, "HINGES"},
  {"hair_artic_joint", "HINGE 1 HEIGHT %",-5,  60,  5,  -5, nullptr, "HINGES"},
  {"hair_artic_hang",  "HINGE 1 DROOP %", -5, 100,  5,  -5, nullptr, "HINGES"},
  {"hair_hinge2_pos",  "HINGE 2 HEIGHT %",10,  95,  5,  55, nullptr, "HINGES"},
  {"hair_hinge2_amt",  "HINGE 2 DROOP %",  0, 100,  5,  35, nullptr, "HINGES"},
  {"hair_hinge3_pos",  "HINGE 3 HEIGHT %",10,  95,  5,  80, nullptr, "HINGES"},
  {"hair_hinge3_amt",  "HINGE 3 DROOP %",  0, 100,  5,  35, nullptr, "HINGES"},
  {"intensity",        "INTENSITY %",     10, 200, 10, 100, nullptr, "GENERAL"},
  {"topbar_opacity",   "TOP BAR OPACITY %",0, 100,  5, 100, nullptr, "GENERAL"},
  {"topbar_height",    "TOP BAR HEIGHT %",10, 300, 10, 100, nullptr, "GENERAL"},
};
static const int kN = sizeof(kItems) / sizeof(kItems[0]);
static const char* kStyles[] = {"Original", "A - Cascade", "B - Side whip", "C - Neon rain", "D - Fog bloom", "E - Mirror", "F - Stagger"};
static const char* kPlaces[] = {"Top", "Bottom", "Mirror"};
static const char* kPals[] = {"Rainbow", "Warm", "Cool", "Neon pink", "White", "Ember"};
static const TunerItem kSmear[] = {
  {"smear_style",    "Style",         0,   6,  1,   1, kStyles, "SMEAR"},
  {"smear_place",    "Placement",     0,   2,  1,   0, kPlaces, "SMEAR"},
  {"topbar_opacity", "Opacity",       0, 100,  5, 100, nullptr, "SMEAR"},
  {"topbar_colors",  "Colors",        0,   5,  1,   0, kPals,   "SMEAR"},
  {"topbar_sens",    "Sensitivity",  25, 300, 25, 100, nullptr, "SMEAR"},
  {"topbar_smear",   "Trail length", 20, 200, 10, 100, nullptr, "SMEAR"},
  {"topbar_blur",    "Blur",         20, 250, 10, 100, nullptr, "SMEAR"},
  {"topbar_glow",    "Glow",          0, 250, 10, 100, nullptr, "SMEAR"},
  {"topbar_thick",   "Bar thickness",30, 300, 10, 100, nullptr, "SMEAR"},
  {"topbar_release", "Fade time",    20, 400, 20, 100, nullptr, "SMEAR"},
};
static const int kSmearN = sizeof(kSmear) / sizeof(kSmear[0]);
void InVizTuner::SetSmear(bool smear) {
  if (m_haveMode && m_smear == smear) return;
  if (m_haveMode && m_smear != smear) m_sel = 0;
  m_smear = smear; m_haveMode = true;
  int n = m_smear ? kSmearN : kN; if (m_sel < 0 || m_sel >= n) m_sel = 0;
}
void InVizTuner::Init(const std::string& addonPath, Sprites& sp, Tuner& t) {
  m_font = sp.LoadTextureKeep(addonPath + "/resources/font_mono.png");
  m_knob = sp.LoadTextureKeep(addonPath + "/resources/glow_disc.png");
  for (auto& it : kItems) m_v[it.id] = kodi::addon::GetSettingInt(it.id, it.def);
  for (auto& it : kSmear) m_v[it.id] = kodi::addon::GetSettingInt(it.id, it.def);
  std::string tmp = kodi::vfs::TranslateSpecialProtocol("special://temp/");
  m_cmdPath = tmp + "bezelviz_cmd.txt"; m_statePath = tmp + "bezelviz_state.txt";
  m_primed = false; m_open = false; WriteState(); (void)t;
}
void InVizTuner::WriteState() { std::ofstream f(m_statePath, std::ios::trunc); f << "open " << (m_open ? 1 : 0) << "\nsel " << m_sel << "\n"; }
void InVizTuner::Poll(float dt, Tuner& t) {
  m_flash = std::max(0.f, m_flash - dt);
  if ((m_pollT += dt) < 0.08f) return; m_pollT = 0;
  std::ifstream f(m_cmdPath); if (!f) { m_primed = true; return; }
  std::string line; long maxSeq = m_lastSeq;
  while (std::getline(f, line)) { std::istringstream ls(line); long seq; std::string cmd; if (!(ls >> seq >> cmd)) continue;
    if (seq <= m_lastSeq) continue; maxSeq = std::max(maxSeq, seq); if (m_primed) Apply(cmd, t); }
  m_lastSeq = maxSeq; m_primed = true;   // first read after start skips stale commands
}
void InVizTuner::Apply(const std::string& c, Tuner& t) {
  if (c == "toggle") { m_open = !m_open; WriteState(); return; }
  if (c == "close") { m_open = false; WriteState(); return; }
  if (c == "open") { m_open = true; WriteState(); return; }
  if (!m_open) return;
  if (m_smear) AdjustSmear(c, t); else AdjustLegacy(c, t);
  WriteState();
}
void InVizTuner::AdjustLegacy(const std::string& c, Tuner& t) {
  if (c == "up") m_sel = (m_sel + kN - 1) % kN; else if (c == "down") m_sel = (m_sel + 1) % kN;
  else if (c == "left" || c == "right" || c == "reset") {
    const TunerItem& it = kItems[m_sel]; int& v = m_v[it.id];
    if (c == "reset") v = it.def; else if (it.min < 0 && v < 0 && c == "right") { std::string id = it.id; v = id == "hair_artic_joint" ? 25 : id == "hair_tex_opacity" ? 100 : 50; }
    else { v += (c == "right" ? it.step : -it.step); if (it.min < 0 && v < 0) v = -5; if (it.names == kColors) { if (v > it.max) v = it.min; if (v < it.min) v = it.max; } v = std::clamp(v, it.min, it.max); }
    t.OnSetting(it.id, std::to_string(v)); kodi::addon::SetSettingInt(it.id, v); m_flash = 0.35f;
  }
}
void InVizTuner::AdjustSmear(const std::string& c, Tuner& t) {
  if (m_sel < 0 || m_sel >= kSmearN) m_sel = 0;
  if (c == "up") m_sel = (m_sel + kSmearN - 1) % kSmearN; else if (c == "down") m_sel = (m_sel + 1) % kSmearN;
  else if (c == "left" || c == "right" || c == "reset") {
    const TunerItem& it = kSmear[m_sel]; int& v = m_v[it.id];
    if (c == "reset") v = it.def;
    else if (it.names) { if (c == "right") v = v >= it.max ? it.min : v + 1; else v = v <= it.min ? it.max : v - 1; }
    else { v += c == "right" ? it.step : -it.step; v = std::clamp(v, it.min, it.max); }
    t.OnSetting(it.id, std::to_string(v)); kodi::addon::SetSettingInt(it.id, v); m_flash = 0.35f;
  }
}
void InVizTuner::Text(Sprites& sp, const std::string& s, float x, float y, float h, Color c, float aspect) {
  float w = h * (32.f / 48.f) / aspect;   // NDC width per glyph (cell 32x48)
  for (char ch : s) { int i = (unsigned char)ch - 32; if (i < 0 || i > 95) i = 0;
    if (i) { Quad q; q.pos = {x + w * 0.5f, y}; q.size = {w * 0.5f, h * 0.5f};
      float u0 = (i % 16) / 16.f, v0 = (i / 16) / 6.f; q.uv[0] = u0; q.uv[2] = u0 + 1 / 16.f; q.uv[1] = v0 + 1 / 6.f; q.uv[3] = v0; q.col = c; sp.Push(q, m_font); }
    x += w * 0.92f; }
}
static std::string valStr(const TunerItem& it, int v) {
  if (it.names) return it.names[std::clamp(v, it.min, it.max)];
  if (it.min < 0 && v < 0) return "PACK"; return std::to_string(v);
}
void InVizTuner::Draw(Sprites& sp, float aspect, float time) {
  if (!m_open || !m_font) return;
  if (m_smear) DrawSmear(sp, aspect, time); else DrawLegacy(sp, aspect, time);
}
void InVizTuner::DrawLegacy(Sprites& sp, float aspect, float time) {
  auto solid = [&](float cx, float cy, float hw, float hh, Color c) { Quad q; q.pos = {cx, cy}; q.size = {hw, hh};
    float u0 = 15 / 16.f + 0.01f, v0 = 5 / 6.f + 0.02f; q.uv[0] = u0; q.uv[2] = u0 + 0.04f; q.uv[1] = v0 + 0.1f; q.uv[3] = v0; q.col = c; sp.Push(q, m_font); };
  const float rowH = 0.072f, x0 = 0.30f, x1 = 0.97f, top = 0.94f, th = 0.05f;
  const float H = 0.20f + rowH * kN + 0.08f + 3 * 0.04f;
  sp.SetAdditive(false);
  solid((x0 + x1) * 0.5f, top - H * 0.5f, (x1 - x0) * 0.5f, H * 0.5f, {0.02f, 0.02f, 0.04f, 0.78f});
  solid((x0 + x1) * 0.5f, top - 0.004f, (x1 - x0) * 0.5f, 0.004f, {0.95f, 0.25f, 0.2f, 0.9f});
  Text(sp, "BEZEL VIZ  LIVE TUNER", x0 + 0.03f, top - 0.06f, 0.06f, {1, 1, 1, 1}, aspect);
  float y = top - 0.15f; const char* grp = "";
  for (int k = 0; k < kN; ++k) {
    const TunerItem& it = kItems[k]; int v = m_v[it.id]; bool sel = k == m_sel;
    if (std::string(grp) != it.group) { grp = it.group; y -= 0.04f; Text(sp, grp, x0 + 0.03f, y + rowH * 0.55f, 0.032f, {0.95f, 0.45f, 0.35f, 0.9f}, aspect); }
    bool dim = (std::string(it.id).rfind("hair_hinge2", 0) == 0 && m_v["hair_hinges"] < 2) || (std::string(it.id).rfind("hair_hinge3", 0) == 0 && m_v["hair_hinges"] < 3)
            || ((std::string(it.id) == "hair_artic_joint" || std::string(it.id) == "hair_artic_hang") && m_v["hair_hinges"] < 1);
    if (sel) { float p = 0.75f + 0.25f * std::sin(time * 4.f) + m_flash;
      solid((x0 + x1) * 0.5f, y, (x1 - x0) * 0.5f - 0.01f, rowH * 0.46f, {0.85f, 0.15f, 0.12f, 0.45f * std::min(1.4f, p)}); }
    Color c = dim ? Color{0.55f, 0.55f, 0.6f, 0.6f} : Color{1, 1, 1, sel ? 1.f : 0.85f};
    Text(sp, it.label, x0 + 0.05f, y, 0.045f, c, aspect);
    // value: slider bar for numeric, text for named
    float vx = x0 + (x1 - x0) * 0.62f, vw = (x1 - x0) * 0.24f;
    if (!it.names && !(it.min < 0 && v < 0)) { float f = float(v - std::max(0, it.min)) / float(it.max - std::max(0, it.min));
      solid(vx + vw * 0.5f, y, vw * 0.5f, 0.006f, {1, 1, 1, 0.25f});
      solid(vx + vw * f * 0.5f, y, vw * f * 0.5f, 0.006f, {0.95f, 0.3f, 0.25f, dim ? 0.4f : 0.95f}); }
    std::string vs = (sel ? "< " : "  ") + valStr(it, v) + (sel ? " >" : "");
    Text(sp, vs, x1 - 0.02f - vs.size() * 0.045f * (32.f / 48.f) / aspect * 0.92f, y, 0.045f, c, aspect);
    y -= rowH;
  }
  Text(sp, "UP/DN SELECT  L/R ADJUST  OK RESET  BACK CLOSE", x0 + 0.03f, y + rowH * 0.2f, 0.032f, {0.8f, 0.8f, 0.85f, 0.8f}, aspect);
  sp.Flush(false);
}
static std::string smearVal(const TunerItem& it, int v) {
  if (std::string(it.id) == "topbar_release") { char b[24]; std::snprintf(b, sizeof b, "%.1f s", 0.55f * v / 100.f); return b; }
  if (it.names) return it.names[std::clamp(v, it.min, it.max)];
  return std::to_string(v) + "%";
}
void InVizTuner::DrawSmear(Sprites& sp, float aspect, float time) {
  auto solid = [&](float cx, float cy, float hw, float hh, Color c) { Quad q; q.pos = {cx, cy}; q.size = {hw, hh};
    float u0 = 15 / 16.f + 0.01f, v0 = 5 / 6.f + 0.02f; q.uv[0] = u0; q.uv[2] = u0 + 0.04f; q.uv[1] = v0 + 0.1f; q.uv[3] = v0; q.col = c; sp.Push(q, m_font); };
  auto glyphW = [&](float h) { return h * (32.f / 48.f) / std::max(0.1f, aspect) * 0.92f; };
  const float x0 = 0.16f, x1 = 0.96f, top = 0.90f, rowH = 0.056f;
  const float bottom = top - 0.36f - rowH * (kSmearN - 1) - 0.08f;
  const Color cyan{0.18f, 0.78f, 0.96f, 1.f};
  sp.SetAdditive(false);
  solid((x0 + x1) * 0.5f, (top + bottom) * 0.5f, (x1 - x0) * 0.5f, (top - bottom) * 0.5f, {0.05f, 0.06f, 0.08f, 0.94f});
  solid((x0 + x1) * 0.5f, top - 0.003f, (x1 - x0) * 0.5f, 0.003f, {0.25f, 0.28f, 0.32f, 0.9f});
  solid((x0 + x1) * 0.5f, bottom + 0.003f, (x1 - x0) * 0.5f, 0.003f, {0.25f, 0.28f, 0.32f, 0.9f});
  solid(x0 + 0.003f, (top + bottom) * 0.5f, 0.003f, (top - bottom) * 0.5f, {0.25f, 0.28f, 0.32f, 0.9f});
  solid(x1 - 0.003f, (top + bottom) * 0.5f, 0.003f, (top - bottom) * 0.5f, {0.25f, 0.28f, 0.32f, 0.9f});
  Text(sp, "SMEAR TUNER", x0 + 0.04f, top - 0.055f, 0.050f, {1, 1, 1, 1}, aspect);
  Text(sp, "Concept preview", x0 + 0.04f, top - 0.100f, 0.028f, {0.62f, 0.66f, 0.70f, 1}, aspect);
  float y = top - 0.165f;
  const TunerItem& st = kSmear[0];
  bool styleSel = m_sel == 0;
  float boxTop = y + 0.032f, boxBot = y - 0.032f;
  solid((x0 + x1) * 0.5f, y, (x1 - x0) * 0.5f - 0.03f, 0.032f, {0.03f, 0.04f, 0.05f, 1});
  Color edge = styleSel ? cyan : Color{0.28f, 0.32f, 0.36f, 1};
  if (m_flash > 0 && styleSel) edge = {1, 1, 1, 1};
  solid((x0 + x1) * 0.5f, boxTop, (x1 - x0) * 0.5f - 0.03f, 0.0025f, edge);
  solid((x0 + x1) * 0.5f, boxBot, (x1 - x0) * 0.5f - 0.03f, 0.0025f, edge);
  solid(x0 + 0.03f, y, 0.0025f, 0.032f, edge);
  solid(x1 - 0.03f, y, 0.0025f, 0.032f, edge);
  Text(sp, "<", x0 + 0.05f, y, 0.036f, edge, aspect);
  Text(sp, ">", x1 - 0.07f, y, 0.036f, edge, aspect);
  std::string sn = smearVal(st, m_v[st.id]);
  Text(sp, sn, (x0 + x1) * 0.5f - sn.size() * glyphW(0.038f) * 0.5f, y, 0.038f, {1, 1, 1, 1}, aspect);
  y -= 0.050f;
  Text(sp, "A Cascade   B Side whip   C Neon rain", x0 + 0.04f, y, 0.024f, {0.62f, 0.66f, 0.70f, 1}, aspect);
  y -= 0.030f;
  Text(sp, "D Fog bloom   E Mirror   F Stagger   + Original", x0 + 0.04f, y, 0.024f, {0.62f, 0.66f, 0.70f, 1}, aspect);
  y -= 0.040f;
  for (int k = 1; k < kSmearN; ++k) {
    const TunerItem& it = kSmear[k]; int v = m_v[it.id]; bool sel = k == m_sel;
    if (sel) solid((x0 + x1) * 0.5f, y, (x1 - x0) * 0.5f - 0.02f, rowH * 0.42f, {0.10f, 0.28f, 0.36f, 0.55f});
    Color c{1, 1, 1, sel ? 1.f : 0.82f};
    Text(sp, it.label, x0 + 0.04f, y, 0.034f, c, aspect);
    std::string vs = smearVal(it, v); if (sel) vs = "< " + vs + " >";
    float vw = vs.size() * glyphW(0.032f);
    if (!it.names) {
      float f = float(v - it.min) / float(std::max(1, it.max - it.min));
      float sx0 = x0 + (x1 - x0) * 0.48f, sx1 = x1 - 0.04f - vw - 0.03f;
      if (sx1 > sx0 + 0.04f) {
        solid((sx0 + sx1) * 0.5f, y, (sx1 - sx0) * 0.5f, 0.0045f, {0.28f, 0.31f, 0.35f, 1});
        solid(sx0 + (sx1 - sx0) * f * 0.5f, y, (sx1 - sx0) * f * 0.5f, 0.0045f, cyan);
        if (m_knob) { Quad kq; kq.pos = {sx0 + (sx1 - sx0) * f, y}; kq.size = {0.012f / std::max(0.1f, aspect), 0.012f}; kq.col = {1, 1, 1, 1}; sp.Push(kq, m_knob); }
      }
    }
    Text(sp, vs, x1 - 0.03f - vw, y, 0.032f, c, aspect);
    y -= rowH;
  }
  Text(sp, "UP/DN Select   L/R Adjust   OK Reset   Back Close   T Toggle", x0 + 0.03f, y + 0.01f, 0.022f, {0.55f, 0.58f, 0.62f, 1}, aspect);
  sp.Flush(false);
}
}
