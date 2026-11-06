#include <algorithm>
// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#include "PackLoader.h"
#include "MiniJson.h"
#include <cstdlib>
#include <fstream>
#include <map>
#include <sstream>
namespace bezel {
std::vector<std::string> PackLoader::CandidateRoots(const std::string& ov, const std::string& skin, const std::string& addon) {
  std::vector<std::string> r; if (!ov.empty()) r.push_back(ov + "/");
  if (!skin.empty()) r.push_back(skin + "/viz.addons/");   // skin = translated special://skin
  if (!addon.empty()) r.push_back(addon + "/resources/packs/");  // bundled pack (Windows engine-only install)
  return r;
}
PackManifest PackLoader::BuiltinDefault() {
  PackManifest p; p.id = "builtin"; p.name = "Builtin solid"; p.version = "0";
  auto mk = [](const char* id, LayerKind k, float px){ LayerDef L; L.id = id; L.kind = k; L.texture = "glow_disc"; L.parallax = px; return L; };
  p.layers = {mk("light_behind", LayerKind::LightBehind, 0.1f), mk("haze", LayerKind::Haze, 0.3f),
              mk("dust", LayerKind::Dust, 0.8f), mk("strobe", LayerKind::StrobeFx, 0.f)};
  p.textures = {"glow_disc"}; return p;
}
static bool kindFrom(const std::string& k, LayerKind& out) {
  static const std::map<std::string, LayerKind> m = {{"light_behind", LayerKind::LightBehind}, {"haze", LayerKind::Haze},
    {"dust", LayerKind::Dust}, {"strobe_fx", LayerKind::StrobeFx}, {"strobe", LayerKind::StrobeFx}, {"debug", LayerKind::Debug},
    {"hair", LayerKind::HairMass}, {"hair_mass", LayerKind::HairMass}, {"topbar", LayerKind::TopBar}};
  auto it = m.find(k); if (it == m.end()) return false; out = it->second; return true;
}
static bool hexColor(const std::string& h, Color& c) {
  if (h.size() != 7 || h[0] != '#') return false;
  long v = std::strtol(h.c_str() + 1, nullptr, 16);
  c.r = ((v >> 16) & 255) / 255.f; c.g = ((v >> 8) & 255) / 255.f; c.b = (v & 255) / 255.f; c.a = 1; return true;
}
static void readRect(const JVal* o, float* d, const char* const* keys, int n) {
  if (!o) return; for (int i = 0; i < n; ++i) d[i] = o->num(keys[i], d[i]);
}
bool PackLoader::Load(const std::vector<std::string>& roots, const std::string& id, PackManifest& out) {
  for (auto& r : roots) {
    std::ifstream f(r + id + "/manifest.json"); if (!f) continue;
    std::stringstream ss; ss << f.rdbuf(); JVal j;
    if (!ParseJson(ss.str(), j) || j.t != JVal::Obj) continue;   // malformed manifest -> try next root / builtin
    PackManifest p = BuiltinDefault();
    p.root = r + id + "/"; p.id = j.str("id", id); p.name = j.str("name", id); p.version = j.str("version", "0");
    if (auto d = j.get("defaults")) { p.particleCap = (int)d->num("particle_cap", (float)kDefaultParticleCap);
      p.spawnRate = d->num("spawn_rate", 60.f); p.swirl = d->num("swirl", 0.3f); p.drift = d->num("drift", 0.05f); }
    if (auto t = j.get("textures"); t && t->t == JVal::Arr) { p.textures.clear(); for (auto& e : t->a) if (e.t == JVal::Str) p.textures.push_back(e.s); }
    std::map<std::string, Color> pal;
    if (auto pv = j.get("palette"); pv && pv->t == JVal::Obj) for (auto& kv : pv->o) { Color c; if (kv.second.t == JVal::Str && hexColor(kv.second.s, c)) pal[kv.first] = c; }
    if (auto ls = j.get("layers"); ls && ls->t == JVal::Arr && !ls->a.empty()) {
      p.layers.clear();
      for (auto& e : ls->a) {
        if (e.t != JVal::Obj) continue; LayerDef L;
        if (!kindFrom(e.str("kind", "dust"), L.kind)) continue;
        L.id = e.str("id", "layer"); L.texture = e.str("texture", "glow_disc"); L.additive = e.boolean("additive", true); L.front = e.boolean("front", false);
        L.parallax = e.num("parallax", 0.5f); L.role = e.str("role"); L.density = e.num("density", 0.5f); L.dissolve = e.boolean("dissolve", false);
        if (L.role == "hair") L.kind = LayerKind::HairMass;   // haze/dust with role hair -> soft-mass hair renderer
        std::string col = e.str("color"); Color c; if (pal.count(col)) L.color = pal[col]; else if (hexColor(col, c)) L.color = c;
        std::string b = e.str("band", "level"); L.band = b == "low" ? Band::Low : b == "mid" ? Band::Mid : b == "high" ? Band::High : Band::Level;
        if (auto rr = e.get("radius"); rr && rr->t == JVal::Arr && rr->a.size() >= 2) { L.radius[0] = (float)rr->a[0].n; L.radius[1] = (float)rr->a[1].n; }
        if (auto ev = e.get("envelope")) { L.env.attack = ev->num("attack", L.env.attack); L.env.release = ev->num("release", L.env.release);
          L.env.grow = ev->num("grow", L.env.grow); L.env.fadeMin = ev->num("fade_min", L.env.fadeMin); }
        if (auto po = e.get("pose")) { L.pose = true; L.restLen = po->num("rest_len", L.restLen); L.wildLen = po->num("wild_len", L.wildLen);
          L.restArc = po->num("rest_arc", L.restArc); L.restHang = po->num("rest_hang", L.restHang); L.wildSpread = po->num("wild_spread", L.wildSpread);
          L.poseThreshold = std::clamp(po->num("threshold", L.poseThreshold), 0.f, 0.95f); L.poseKnee = std::max(0.2f, po->num("knee", L.poseKnee)); L.tremble = po->num("tremble", L.tremble); L.poseGain = po->num("gain", L.poseGain); L.wildBias = po->num("wild_bias", L.wildBias); L.idleMotion = po->num("idle_motion", L.idleMotion); L.idleLean = po->num("idle_lean", L.idleLean); L.idleMorph = po->num("idle_morph", L.idleMorph); L.biasVary = po->num("bias_vary", L.biasVary); L.idleRoam = po->num("idle_roam", L.idleRoam); L.arcCenter = po->num("arc_center", L.arcCenter); L.timeScale = po->num("time_scale", L.timeScale); L.edgeFade = po->num("edge_fade", L.edgeFade); L.drift = po->num("lean_dir", L.drift); L.articJoint = std::clamp(po->num("artic_joint", L.articJoint), 0.f, 0.9f); L.articHang = std::clamp(po->num("artic_hang", L.articHang), 0.f, 1.f); L.articLift = po->num("artic_lift", L.articLift); L.articSwing = po->num("artic_swing", L.articSwing); }
        if (auto sp = e.get("spikes")) { L.spikes = std::clamp((int)sp->num("count", (float)L.spikes), 3, 64); L.spikeLen = sp->num("length", L.spikeLen);
          L.spikeWidth = sp->num("width", L.spikeWidth); L.jitter = sp->num("jitter", L.jitter); L.spin = sp->num("spin", L.spin); L.sway = sp->num("sway", L.sway); }
        if (auto tb = e.get("topbar")) { L.columns = std::clamp((int)tb->num("columns", (float)L.columns), 4, 128); L.barH = tb->num("bar_h", L.barH);
          L.barPulse = tb->num("bar_pulse", L.barPulse); L.smearMax = tb->num("smear_max", L.smearMax); L.hueSpan = tb->num("hue_span", L.hueSpan);
          L.sat = tb->num("sat", L.sat); L.glow = tb->num("glow", L.glow); L.blur = tb->num("blur", L.blur); L.smearAlpha = tb->num("smear_alpha", L.smearAlpha); L.colMix = tb->num("column_mix", L.colMix); L.colFill = std::clamp(tb->num("column_fill", L.colFill), 0.1f, 1.5f); }
        p.layers.push_back(L);
      }
      if (p.layers.empty()) p.layers = BuiltinDefault().layers;
    }
    if (auto ch = j.get("character"); ch && ch->t == JVal::Obj && !ch->str("sprite").empty()) {
      p.character.present = true; p.character.sprite = ch->str("sprite"); p.character.chroma = ch->str("chroma_key", "auto");
      p.character.overlay = ch->str("overlay"); p.character.overlayOpacity = std::clamp(ch->num("overlay_opacity", 1.f), 0.f, 1.f);
      static const char* const rk[] = {"x", "y", "w", "h"}; static const char* const ak[] = {"x", "y", "r"};
      readRect(ch->get("rect"), p.character.rect, rk, 4); readRect(ch->get("hair_anchor"), p.character.anchor, ak, 3);
    }
    if ((int)p.layers.size() > kMaxLayers) p.layers.resize(kMaxLayers);
    if ((int)p.textures.size() > kMaxPackTextures) p.textures.resize(kMaxPackTextures);
    out = p; return true;
  }
  out = BuiltinDefault(); return false;
}
}
