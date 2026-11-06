// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#include "Engine.h"
#include <algorithm>
#include <cmath>
#include <kodi/General.h>
#ifndef BEZEL_DX11
#include <kodi/gui/gl/GL.h>
#endif
namespace bezel {
bool Engine::Init(const std::string& addonPath, const std::string& skinPath, bool gles) {
  m_skinPath = skinPath; m_addonPath = addonPath; m_tuner.LoadSettings();
  m_ready = m_sprites.Init(addonPath +
#ifdef BEZEL_DX11
    std::string("/resources/shaders/DX11/"));
  (void)gles;
#else
    (gles ? "/resources/shaders/GLES/" : "/resources/shaders/GL/"));
#endif
  if (!m_ready) { kodi::Log(ADDON_LOG_ERROR, "BezelViz: sprite shader init failed"); return false; }
  m_menu.Init(addonPath, m_sprites, m_tuner);
  ReloadPack(); return true;
}
void Engine::DeInit() { m_sprites.DeInit(); m_ready = false; }
void Engine::ReloadPack() {
  auto roots = PackLoader::CandidateRoots(m_tuner.s.packRoot, m_skinPath, m_addonPath);
  const std::string want = m_tuner.s.activeStyle;
  bool found = m_loader.Load(roots, want, m_pack);
  if (!found && (want.empty() || want == "solid_test" || want == "builtin")) {
    kodi::Log(ADDON_LOG_WARNING, "BezelViz pack '%s' missing (placeholder); trying bundled topbar_smear", want.c_str());
    found = m_loader.Load(roots, "topbar_smear", m_pack);
  }
  kodi::Log(found ? ADDON_LOG_INFO : ADDON_LOG_WARNING, "BezelViz pack '%s' %s (%s)", m_pack.id.c_str(), found ? "loaded" : "not found, builtin", m_pack.root.c_str());
  m_sprites.FreeLoaded(); m_atlas = Atlas(); m_charTex = 0; m_ovTex = 0;
  for (auto& t : m_pack.textures) m_atlas.AddRegion(t, m_pack.root.empty() ? m_sprites.LoadTexturePNG("") : m_sprites.LoadTexturePNG(m_pack.root + "textures/" + t + ".png"));
  if (m_pack.character.present) {
    int mode = m_pack.character.chroma == "none" ? 0 : m_pack.character.chroma == "black" ? 2 : 1;
    m_charTex = m_sprites.LoadTexturePNG(m_pack.root + m_pack.character.sprite, mode, &m_charW, &m_charH);
    if (!m_pack.character.overlay.empty()) { int ow = 0, oh = 0; m_ovTex = m_sprites.LoadTexturePNG(m_pack.root + m_pack.character.overlay, 0, &ow, &oh); }
  }
  m_layerEnv.assign(m_pack.layers.size(), 0.f);
  m_caps.particleCap = std::min({m_tuner.s.particleCap, m_pack.particleCap, kHardParticleCap});
  m_parts.SetCap(m_caps.particleCap);
}
void Engine::Frame(float dt) {
  if (!m_ready) return;
  m_time += dt; m_fps = m_fps * 0.95f + (dt > 0 ? 1.f / dt : 60.f) * 0.05f;
  bool smear = false; for (const auto& L : m_pack.layers) if (L.kind == LayerKind::TopBar) smear = true;
  m_menu.SetSmear(smear);
  m_tuner.PollSkinProperties(dt); m_menu.Poll(dt, m_tuner); m_env.Tick(dt); m_dt = dt;
  // idle / silence: 0 freeze, 1 slow drift, 2 fade out
  bool silent = m_env.Silent(); float target = (silent && m_tuner.s.idleMode == 2) ? 0.f : 1.f;
  m_idleFade += (target - m_idleFade) * std::min(1.f, dt * 1.5f);
  float sim = (silent && m_tuner.s.idleMode == 0) ? 0.f : dt;
  ForceParams f; f.swirl = m_pack.swirl * (0.3f + m_env.mid); f.drift = m_pack.drift; f.pushBack = m_env.low * 0.05f; f.warp = m_env.high * 0.2f;
  m_forces.Apply(m_parts.Items(), f, sim);
  m_parts.Update(sim, m_pack.spawnRate * (silent ? 0.2f : 0.5f + m_env.level), 0.8f);
  { float va = m_sprites.ViewportAspect(); if (va > 0.f) m_aspect = va; }
  // per-layer grow/fade envelopes (attack/release in seconds) on each layer's band
  for (size_t i = 0; i < m_pack.layers.size() && i < m_layerEnv.size(); ++i) {
    const auto& L = m_pack.layers[i]; float raw = std::min(1.f, Band(L)), &v = m_layerEnv[i];
    float tc = raw > v ? L.env.attack : L.env.release; v += (raw - v) * (tc > 0.001f ? std::min(1.f, sim / tc) : 1.f);
  }
  // character image rect: fit inside manifest rect preserving PNG aspect (rect is 0..1 screen, y down)
  { const float* r = m_pack.character.rect; float rw = r[2] * m_aspect, rh = r[3], ia = (float)m_charW / std::max(1, m_charH);
    float dw = rw, dh = rw / ia; if (dh > rh) { dh = rh; dw = rh * ia; }
    float cx = r[0] + r[2] * 0.5f, cy = r[1] + r[3] * 0.5f, hw = dw / m_aspect * 0.5f, hh = dh * 0.5f;
    m_img[0] = (cx - hw) * 2 - 1; m_img[2] = (cx + hw) * 2 - 1; m_img[1] = 1 - (cy + hh) * 2; m_img[3] = 1 - (cy - hh) * 2; }
  // per-thrash direction: each new hard low hit (rising edge) picks a fresh side/angle, held through release
  { float k = m_env.low * 2.5f; if (m_hitArmed && k > 0.75f) { m_hitArmed = false; ++m_hitN;
      float h = std::sin(m_hitN * 78.233f + 1.7f) * 43758.5453f; h -= std::floor(h);           // 0..1
      float side = (m_hitN % 2) ? 1.f : -1.f; if (h < 0.3f) side = -side;                      // mostly alternate, sometimes repeat
      m_hitBias = (h < 0.15f) ? (h - 0.075f) * 4.f : side * (0.45f + 0.9f * h); }              // ~15% near straight up
    else if (k < 0.35f) m_hitArmed = true; }
  m_sprites.Begin();
  // back->front: non-hair layers, hair masses, static character (hairless, bg keyed) over hair; no front hair layer
  int n = 0;
  for (size_t i = 0; i < m_pack.layers.size(); ++i) { if (m_pack.layers[i].front) continue; if (n++ >= m_caps.maxLayers) break; DrawLayer(m_pack.layers[i], i, m_idleFade); }
  if (m_charTex) DrawCharacter(m_idleFade);
  for (size_t i = 0; i < m_pack.layers.size(); ++i) if (m_pack.layers[i].front) DrawLayer(m_pack.layers[i], i, m_idleFade);   // crown cap over scalp
  m_menu.Draw(m_sprites, m_aspect, m_time);   // live in-viz tuner (drawn last, over everything)
  if (m_tuner.s.debug) m_debug.Draw(m_sprites, m_env, m_fps, m_pack.id, m_parts.Items().size());
}
float Engine::Band(const LayerDef& L) const {
  switch (L.band) { case Band::Low: return m_env.low; case Band::Mid: return m_env.mid; case Band::High: return m_env.high; default: return m_env.level; }
}
void Engine::DrawCharacter(float fade) {
  Quad q; q.pos = {(m_img[0] + m_img[2]) * 0.5f, (m_img[1] + m_img[3]) * 0.5f}; q.size = {(m_img[2] - m_img[0]) * 0.5f, (m_img[3] - m_img[1]) * 0.5f};
  q.uv[0] = 0; q.uv[1] = 1; q.uv[2] = 1; q.uv[3] = 0;   // stb rows top-first
  q.col = {1, 1, 1, std::max(0.f, fade)};
  m_sprites.SetAdditive(false); m_sprites.Push(q, m_charTex); m_sprites.Flush(false);
  if (m_ovTex) {   // baked hair texture overlay (hairline F): alpha = tuner override or pack overlay_opacity
    float op = m_tuner.s.hairTexOpacity >= 0.f ? m_tuner.s.hairTexOpacity : m_pack.character.overlayOpacity;
    if (op > 0.002f) { q.col = {1, 1, 1, std::max(0.f, fade) * op}; m_sprites.Push(q, m_ovTex); m_sprites.Flush(false); }
  }
}
static float frac(float x) { return x - std::floor(x); }
static float hash1(float n) { return frac(std::sin(n * 12.9898f) * 43758.5453f); }
// Spiked soft-mass hair: N tapered soft flares (sunburst) radiating from the hair anchor. Each spike's length and
// alpha track the layer envelope (grow/fade with its band); per-spike phase gives uneven pulsing; whole crown slowly
// spins + each spike sways/curls so it reads as hair flowing in air. Base of each flare sits inside the scalp so the
// sprite's short base hair melts into it. No strands, no static hair texture. Budget: <= 32 quads per layer.
static Color hairPreset(int i, Color c) {
  switch (i) { case 1: return {0.90f, 0.06f, 0.08f, 1}; case 2: return {0.62f, 0.04f, 0.12f, 1}; case 3: return {1.f, 0.38f, 0.08f, 1};
               case 4: return {1.f, 0.31f, 0.54f, 1}; case 5: return {0.55f, 0.25f, 0.95f, 1}; case 6: return {1.f, 0.95f, 0.9f, 1}; default: return c; } }
void Engine::DrawHair(const LayerDef& L0, float e, float fade) {
  LayerDef L = L0; const TunerState& TS = m_tuner.s;   // tuner overrides (hair_* settings)
  L.color = hairPreset(TS.hairColor, L.color); L.density *= TS.hairOpacity;
  if (TS.articHang >= 0.f) L.articHang = TS.articHang; if (TS.articJoint >= 0.f) L.articJoint = TS.articJoint;
  if (TS.hinges <= 0) L.articJoint = 0.f;
  const AtlasRegion* r = m_atlas.Find(L.texture); unsigned tex = r ? r->tex : 0;
  const auto& a = m_pack.character.anchor;
  float iw = m_img[2] - m_img[0], ih = m_img[3] - m_img[1];
  float ax = m_img[0] + a[0] * iw, ay = m_img[3] - a[1] * ih;      // anchor relative to drawn character image
  float unitY = ih, unitX = ih / m_aspect;
  float g = std::min(1.f, e * (1.f + L.env.grow));
  if (L.pose) { float k = std::clamp((e * L.poseGain - L.poseThreshold) / (1.f - L.poseThreshold), 0.f, 1.f);
                g = std::pow(k * k * (3.f - 2.f * k), L.poseKnee); }   // sharp threshold: mid hits ~0, hard low hits slam to 1
  float R = (L.radius[0] + (L.radius[1] - L.radius[0]) * g);
  float alpha = std::clamp(L.density * (L.env.fadeMin + (1.f - L.env.fadeMin) * g), 0.f, 1.f) * fade * m_tuner.s.intensity;
  if (alpha <= 0.002f) return;
  int count = std::clamp(L.spikes, 3, 64);
  float seed = (float)(L.id.size() * 7 + count);
  float spin = m_time * L.spin;                                    // slow whole-crown drift
  m_sprites.SetAdditive(L.additive);
  const float th0 = 1.5707963f;
  for (int i = 0; i < count; ++i) {
    float h = hash1(seed + i), h2 = hash1(seed * 3.1f + i * 1.7f);
    float th = 6.2831853f * (i + (h - 0.5f) * L.jitter) / count + spin
             + L.sway * std::sin(m_time * (0.35f + 0.3f * h2) + i * 2.1f);   // per-spike sway = air flow
    // per-spike pulse: envelope drives the whole set; phase offset makes neighbours breathe unevenly
    float pulse = 0.55f + 0.45f * std::sin(m_time * (0.8f + h * 0.9f) + i * 1.3f) * (0.4f + 0.6f * g);
    float len = R * L.spikeLen * (0.6f + 0.6f * h) * (0.7f + 0.5f * g) * (0.85f + 0.3f * pulse) * TS.hairLen;
    float wid = R * L.spikeWidth * (0.7f + 0.6f * h2);
    float aMul = 0.55f + 0.45f * pulse, base = R * 0.25f; float ax2 = ax, ay2 = ay;
    if (L.dissolve) { float ph = frac(m_time * (0.12f + 0.08f * h) + h2); base += R * 0.6f * ph; aMul *= (1.f - ph) * std::min(1.f, ph * 5.f); }
    float cy = std::sin(th), cx = std::cos(th);
    if (L.pose) {
      const float T = m_time * L.timeScale;   // per-layer motion speed (split halves)
      // KEY0: crown arc whose strands bend down under gravity; KEY1: full fanned halo. Sharp threshold morph.
      float tt = g;
      float u = (i + 0.5f + (h - 0.5f) * L.jitter) / count - 0.5f;
      float sw = L.sway * std::sin(T * (0.35f + 0.3f * h2) + i * 2.1f);
      float im = L.idleMotion * (1.f - 0.7f * tt), ib = std::sin(T * (0.5f + 0.6f * h) + i * 1.9f);   // low-vol breathing
      // sound-independent whole-mass sway (lean) + slow shape morph (arc breathes), run at silence too
      float lean = L.idleLean * std::sin(T * 0.23f + seed * 0.1f) + 0.5f * L.idleLean * std::sin(T * 0.11f + 1.3f);
      float arcM = 1.f + L.idleMorph * std::sin(T * 0.17f + seed * 0.3f);
      float tr = th0 + L.arcCenter + lean * L.drift + u * 2.f * L.restArc * arcM + sw + im * 0.6f * std::sin(T * (0.3f + 0.4f * h2) + i * 2.7f), tw = 1.5707963f + L.arcCenter + L.wildBias * (1.f - L.biasVary) + m_hitBias * L.biasVary + u * 2.f * L.wildSpread + sw * 0.5f;
      tw += tt * L.tremble * std::sin(T * (37.f + 23.f * h) + i * 5.3f);       // vibrating suspended strands
      // 2D roam: whole mass drifts up/down/left/right on incommensurate slow sines (sound independent)
      float rmx = L.idleRoam * (std::sin(T * 0.21f + 0.7f) + 0.5f * std::sin(T * 0.083f + 2.1f));
      float rmy = L.idleRoam * (std::sin(T * 0.29f + 1.9f) + 0.5f * std::sin(T * 0.13f + 0.4f));
      float rx = std::cos(tr) + rmx, ry = std::sin(tr) - L.restHang * (1.f - 0.6f * rmy / std::max(1e-3f, L.idleRoam * 1.5f + 1e-3f)) + rmy; float rn = std::sqrt(rx * rx + ry * ry) + 1e-4f; rx /= rn; ry /= rn;
      cx = rx + (std::cos(tw) - rx) * tt; cy = ry + (std::sin(tw) - ry) * tt; float cn = std::sqrt(cx * cx + cy * cy) + 1e-4f; cx /= cn; cy /= cn;
      th = std::atan2(cy, cx);
      if (L.edgeFade > 0.f) { float ef = std::clamp((0.5f - std::fabs(u)) / (0.5f * L.edgeFade), 0.f, 1.f); aMul *= ef * ef * (3.f - 2.f * ef); }   // soft blend at half seam
      len = R * (L.restLen + (L.wildLen - L.restLen) * tt) * (0.75f + 0.5f * h) * (1.f + tt * L.tremble * 2.f * std::sin(T * 29.f + i * 3.7f));
      len *= (1.f + im * ib) * (1.f + L.idleMorph * 0.5f * std::sin(T * 0.19f + u * 3.f));
      len *= TS.hairLen;
      base = R * (0.15f - 0.15f * tt); wid *= 1.f + tt * 0.9f;   // frizz: locks fatten into a full blowout mass
      // root sits on the crown arc so the cut grows from the scalp, not a point
      float rr = R * 0.6f * (1.f - tt * 0.85f); ax2 = ax + std::cos(tr) * rr * unitX; ay2 = ay + std::max(0.f, std::sin(tr)) * rr * 0.9f * unitY;
    }
    if (L.pose && L.articJoint > 0.f) {
      // MULTI-HINGE ARTICULATION: up to 3 joints along each radial (hinge 1 = pack/tuner joint+hang, hinges 2/3 = tuner
      // pos/amount). Each joint bends the remaining strand further toward gravity, outward on its side (left->left,
      // right->right). Beats weaken all hangs (artic_lift); pendulum swing grows toward the tip.
      const float T = m_time * L.timeScale;
      float jp[4] = {L.articJoint, TS.hinge2Pos, TS.hinge3Pos, 1.f}, ja[3] = {L.articHang, TS.hinge2Amt, TS.hinge3Amt};
      int nh = std::clamp(TS.hinges, 1, 3);
      for (int k = 1; k < nh; ++k) jp[k] = std::max(jp[k], jp[k - 1] + 0.05f);   // keep joints ordered
      if (jp[nh - 1] > 0.95f) jp[nh - 1] = 0.95f; jp[nh] = 1.f;
      float side = (ax2 + cx * 1e-3f < ax) ? -1.f : (cx < -0.02f ? -1.f : 1.f);
      float gx = side * 0.6f, gy = -0.8f, gn = std::sqrt(gx * gx + gy * gy); gx /= gn; gy /= gn;
      float dx = cx, dy = cy, dth = th;   // current segment direction
      float px = ax2 + cx * base * unitX, py = ay2 + cy * base * 0.9f * unitY;
      Color col = {L.color.r, L.color.g, L.color.b, std::min(1.f, alpha * aMul)};
      float prev = 0.f;
      for (int k = 0; k <= nh; ++k) {
        float sl = len * (jp[k] - prev) * (k ? 1.04f : 1.f), m = sl * 0.5f - (k ? len * 0.01f : 0.f);
        Quad q; q.pos = {px + dx * m * unitX, py + dy * m * 0.9f * unitY}; q.size = {wid * (1.f - 0.06f * k) * unitX, sl * 0.5f * unitY};
        q.rot = dth - 1.5707963f; q.aspect = m_aspect; q.uv[1] = prev; q.uv[3] = jp[k]; q.col = col; m_sprites.Push(q, tex);
        if (k == nh) break;
        px += dx * len * (jp[k] - prev) * unitX; py += dy * len * (jp[k] - prev) * 0.9f * unitY; prev = jp[k];
        float hang = std::clamp(ja[k] * (1.f - L.articLift * g), 0.f, 1.f);
        float sx = dx + (gx - dx) * hang, sy = dy + (gy - dy) * hang, sn = std::sqrt(sx * sx + sy * sy) + 1e-4f;
        dth = std::atan2(sy / sn, sx / sn) + L.articSwing * (1.f + 0.5f * k) / nh * std::sin(T * (0.9f + 0.7f * h + 0.3f * k) + i * 1.7f + k) * (0.5f + 0.5f * g);
        dx = std::cos(dth); dy = std::sin(dth);
      }
      continue;
    }
    float mid = base + len * 0.5f;
    Quad q; q.pos = {ax2 + cx * mid * unitX, ay2 + (cy * mid * 0.9f) * unitY};
    q.size = {wid * unitX, len * 0.5f * unitY}; q.rot = th - 1.5707963f; q.aspect = m_aspect;
    q.col = {L.color.r, L.color.g, L.color.b, std::min(1.f, alpha * aMul)};
    m_sprites.Push(q, tex);
  }
  m_sprites.Flush(L.additive);
}
// DrawTopBar lives in SmearStyles.cpp (original smear + styles A-F).
void Engine::DrawLayer(const LayerDef& L, size_t idx, float fade) {
  if (L.kind == LayerKind::TopBar) { DrawTopBar(L, idx < m_layerEnv.size() ? m_layerEnv[idx] : 0.f, fade); return; }
  if (L.kind == LayerKind::HairMass) { DrawHair(L, idx < m_layerEnv.size() ? m_layerEnv[idx] : 0.f, fade); return; }
  m_sprites.SetAdditive(L.additive);
  const AtlasRegion* r = m_atlas.Find(L.texture); unsigned tex = r ? r->tex : 0;
  switch (L.kind) {
    case LayerKind::LightBehind: { Quad q; q.size = {0.6f + m_env.low*0.4f, 0.6f + m_env.low*0.4f}; q.col = {1, 0.85f, 0.6f, (0.25f + m_env.low*0.6f)*fade}; m_sprites.Push(q, tex); break; }
    case LayerKind::Haze: { Quad q; q.size = {1.2f, 1.2f}; q.col = {0.6f, 0.7f, 1, 0.08f*fade*(1+m_env.mid)}; m_sprites.Push(q, tex); break; }
    case LayerKind::Dust: for (auto& p : m_parts.Items()) { Quad q; float s = p.size*(1+m_env.high); q.pos = p.p; q.size = {s, s}; q.col = {1, 0.95f, 0.85f, std::min(1.f, p.life)*0.7f*fade*(0.3f+p.depth)}; m_sprites.Push(q, tex); } break;
    case LayerKind::StrobeFx: if (m_tuner.s.strobes && m_env.low > 0.6f) { Quad q; q.size = {1, 1}; q.col = {1,1,1,0.15f*fade}; m_sprites.Push(q, tex); } break; // STUB beat detect
    case LayerKind::Debug: case LayerKind::HairMass: case LayerKind::TopBar: break;
  }
  m_sprites.Flush(L.additive);
}
}
