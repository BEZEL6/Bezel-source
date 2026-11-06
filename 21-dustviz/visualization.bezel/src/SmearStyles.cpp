// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine)
// Smear styles for the topbar layer. Style 0 is the 0.2.0 column smear; Top + default knobs
// keep that placement formula. Styles 1..6 are the DustViz looks selected by smear_style.
#include "Engine.h"
#include <algorithm>
#include <cmath>
namespace bezel {
namespace {
struct BarState {
  const LayerDef* L = nullptr;
  const TunerState* T = nullptr;
  Sprites* sp = nullptr;
  const std::vector<float>* cols = nullptr;
  float time = 0, beat = 0, A = 0, barFrac = 0, smearMax = 0;
  float x0 = -1, span = 2, cw = 0.1f;
  int N = 1;
  unsigned tBar = 0, tSmear = 0, tGlow = 0, tCascade = 0, tWhip = 0, tRain = 0, tFog = 0, tMirror = 0, tStagger = 0;
};
static Color hsv(float h, float s, float v) {
  h = (h - std::floor(h)) * 6.f; int i = (int)h; float f = h - i, p = v * (1 - s), q = v * (1 - s * f), t = v * (1 - s * (1 - f));
  switch (i % 6) {
    case 0: return {v, t, p, 1}; case 1: return {q, v, p, 1}; case 2: return {p, v, t, 1};
    case 3: return {p, q, v, 1}; case 4: return {t, p, v, 1}; default: return {v, p, q, 1};
  }
}
static Color tbColor(int pal, float t, float hueSpan, float sat) {
  switch (pal) {
    case 1: return hsv(-0.02f + t * 0.16f, sat, 1.f);
    case 2: return hsv(0.48f + t * 0.24f, sat, 1.f);
    case 3: return hsv(0.86f + t * 0.10f, sat, 1.f);
    case 4: return hsv(0.08f, 0.08f, 0.6f + 0.4f * std::fabs(std::sin(t * 9.f)));
    case 5: return hsv(0.02f + t * 0.09f, 0.95f, 0.75f + 0.25f * t);
    default: return hsv(t * hueSpan, sat, 1.f);
  }
}
static float fracf(float x) { return x - std::floor(x); }
static float hash1(float n) { return fracf(std::sin(n * 12.9898f) * 43758.5453f); }
// dir -1: image top (bright root) at the top of the quad. dir +1: root at the bottom, so rising trails stay bright at the bar.
static void setFallUV(Quad& q, float dir) {
  q.uv[0] = 0; q.uv[2] = 1;
  if (dir < 0.f) { q.uv[1] = 1; q.uv[3] = 0; }
  else { q.uv[1] = 0; q.uv[3] = 1; }
}
static float sampleCol(const BarState& S, float u) {
  if (!S.cols || S.cols->empty() || S.N <= 1) return S.cols && !S.cols->empty() ? (*S.cols)[0] : 0.f;
  float x = std::clamp(u, 0.f, 1.f) * (S.N - 1);
  int i = std::clamp((int)x, 0, S.N - 1);
  int j = std::min(i + 1, S.N - 1);
  float f = x - (float)i;
  return std::clamp(((*S.cols)[i] * (1.f - f) + (*S.cols)[j] * f) * S.T->tbSens, 0.f, 1.f);
}
static float colAt(const BarState& S, int i) {
  if (!S.cols || i < 0 || i >= (int)S.cols->size()) return 0.f;
  return std::clamp((*S.cols)[i] * S.T->tbSens, 0.f, 1.f);
}
static void push(BarState& S, Quad q, unsigned tex) { S.sp->Push(q, tex); }

// 0.2.0 top-bar smear. edge/dir generalize Top (edge=1, dir=-1) to Bottom and Mirror.
// Top + dir -1 reproduces pos.y = top - bh*0.5 and top - bh - len*0.5 + bh*0.3.
static void drawClassic(BarState& S, float edge, float dir, float amp) {
  const LayerDef& L = *S.L; const TunerState& T = *S.T;
  const float fill = T.tbFill > 0 ? std::clamp(T.tbFill / 100.f, 0.1f, 1.5f) : L.colFill;
  const float fk = fill / 0.62f;
  const float A = S.A * amp;
  const float blur = L.blur * T.tbBlur, glow = L.glow * T.tbGlow;
  S.sp->SetAdditive(true);
  for (int pass = 0; pass < 4; ++pass) {
    for (int i = 0; i < S.N; ++i) {
      float c = colAt(S, i), lv = (1.f - L.colMix) + L.colMix * c;
      Color col = tbColor(T.tbColors, (float)i / S.N, L.hueSpan, L.sat);
      float cx = S.x0 + S.cw * (i + 0.5f), bh = 2.f * S.barFrac * (1.f + L.barPulse * c);
      Quad q; q.col = col;
      if (pass == 0) {
        q.uv[0] = 0; q.uv[1] = 1; q.uv[2] = 1; q.uv[3] = 0;
        q.pos = {cx, edge + dir * bh * 0.5f}; q.size = {S.cw * 1.6f * fk, bh * 2.2f};
        q.col.a = glow * 0.35f * A * (0.6f + 0.4f * c); push(S, q, S.tGlow);
      } else if (pass == 1 || pass == 2) {
        float len = 2.f * S.smearMax * S.beat * (0.25f + 0.75f * lv) * (pass == 2 ? 1.35f : 1.f);
        if (len < 0.004f) continue;
        float w = S.cw * fk * (pass == 2 ? blur * 1.9f : blur);
        q.pos = {cx, edge + dir * (bh + len * 0.5f - bh * 0.3f)}; q.size = {w * 0.5f, len * 0.5f};
        setFallUV(q, dir);
        q.col.a = L.smearAlpha * A * (pass == 2 ? 0.35f : 0.7f) * (0.5f + 0.5f * S.beat); push(S, q, S.tSmear);
      } else {
        q.uv[0] = 0; q.uv[1] = 1; q.uv[2] = 1; q.uv[3] = 0;
        q.pos = {cx, edge + dir * bh * 0.5f}; q.size = {S.cw * fill, bh * 0.5f}; q.col.a = A; push(S, q, S.tBar);
        q.size = {S.cw * 1.1f * fk, bh * 0.75f}; q.col.a = 0.45f * A * std::min(2.f, T.tbGlow); push(S, q, S.tGlow);
      }
    }
    S.sp->Flush(true);
  }
}
static void drawEdgeBar(BarState& S, float edge, float dir, float amp, int pieces, float alphaScale) {
  const LayerDef& L = *S.L;
  float thick = std::clamp(S.T->tbThick, 0.15f, 3.f);
  float blurK = std::clamp(S.T->tbBlur, 0.f, 2.5f);
  float glowK = std::clamp(S.T->tbGlow, 0.f, 2.5f);
  for (int i = 0; i < pieces; ++i) {
    float u = (i + 0.5f) / pieces;
    float c = sampleCol(S, u);
    float bh = 2.f * S.barFrac * (1.f + L.barPulse * c);
    float cx = S.x0 + S.span * u, piece = S.span / pieces;
    Quad q; q.uv[0] = 0; q.uv[1] = 1; q.uv[2] = 1; q.uv[3] = 0; q.col = tbColor(S.T->tbColors, u, L.hueSpan, L.sat);
    q.pos = {cx, edge + dir * bh * 0.5f}; q.size = {piece * 0.52f, bh * 0.5f * thick / std::max(0.15f, thick)};
    q.size.y = bh * 0.5f;
    q.col.a = S.A * amp * alphaScale * (0.55f + 0.45f * c);
    push(S, q, S.tBar);
    if (glowK > 0.02f) {
      q.size = {piece * (0.85f + 0.25f * blurK), bh * (1.15f + 0.55f * blurK)};
      q.col.a = S.A * amp * 0.22f * glowK * alphaScale;
      push(S, q, S.tGlow);
    }
  }
}
static float driveOf(float c, float beat) { return std::clamp((0.25f + 0.75f * c) * beat, 0.f, 1.f); }

static void drawCascade(BarState& S, float edge, float dir, float amp) {
  const int ribbons = 7;
  float thick = std::clamp(S.T->tbThick, 0.2f, 3.f);
  float blurK = std::clamp(S.T->tbBlur, 0.f, 2.5f), glowK = std::clamp(S.T->tbGlow, 0.f, 2.5f);
  float spacing = S.span / ribbons;
  S.sp->SetAdditive(true);
  drawEdgeBar(S, edge, dir, amp, ribbons, 0.95f);
  for (int i = 0; i < ribbons; ++i) {
    float u = (i + 0.5f) / ribbons;
    float d = driveOf(sampleCol(S, u), S.beat);
    float len = std::min(1.85f, 2.f * S.smearMax * (0.32f + 0.68f * d));
    if (len < 0.02f) continue;
    Color col = tbColor(S.T->tbColors, u, S.L->hueSpan, S.L->sat);
    float bodyW = spacing * 0.62f * thick;
    const int segs = 18;
    for (int s = 0; s < segs; ++s) {
      float t = (s + 0.5f) / segs;
      float wave = std::sin(S.time * 1.25f + i * 0.95f + t * 4.2f) * 0.10f + std::sin(S.time * 0.52f + i * 1.4f) * 0.04f;
      float x = S.x0 + S.span * u + wave;
      float y = edge + dir * (0.02f + len * t);
      float fade = 1.f - 0.82f * t;
      float h = (len / segs) * 2.6f;
      float va = std::clamp(t - 0.5f / segs, 0.f, 1.f), vb = std::clamp(t + 0.5f / segs, 0.f, 1.f);
      Quad q; q.col = col; q.pos = {x, y};
      q.uv[0] = 0; q.uv[2] = 1; q.uv[1] = dir < 0.f ? vb : va; q.uv[3] = dir < 0.f ? va : vb;
      q.size = {bodyW * (1.35f + 0.7f * blurK) * 0.5f, h * 0.5f};
      q.col.a = S.A * amp * fade * (0.12f + 0.20f * glowK) * (0.5f + 0.5f * d);
      push(S, q, S.tCascade);
      q.size = {bodyW * (0.85f - 0.35f * t) * 0.5f, h * 0.46f};
      q.col.a = S.A * amp * fade * 0.72f * (0.45f + 0.55f * d);
      push(S, q, S.tCascade);
    }
  }
  S.sp->Flush(true);
}
static void drawWhip(BarState& S, float edge, float dir, float amp) {
  const int streaks = 8;
  float thick = std::clamp(S.T->tbThick, 0.2f, 3.f);
  float blurK = std::clamp(S.T->tbBlur, 0.f, 2.5f), glowK = std::clamp(S.T->tbGlow, 0.f, 2.5f);
  float reachK = std::min(1.6f, S.smearMax / 0.82f);
  S.sp->SetAdditive(true);
  drawEdgeBar(S, edge, dir, amp, 12, 0.85f);
  for (int i = 0; i < streaks; ++i) {
    float u = (i + 0.5f) / streaks;
    float d = driveOf(sampleCol(S, u), S.beat);
    float side = (i % 2) ? 1.f : -1.f;
    float ph = 0.5f + 0.5f * std::sin(S.time * (2.05f + 0.12f * i) + i * 1.35f);
    float origin = S.x0 + S.span * u;
    float reach = (0.16f + 0.70f * d) * S.span * 0.34f * reachK;
    float head = origin + side * reach * (0.30f + 0.70f * ph);
    float tail = head - side * reach;
    float y = edge + dir * (0.045f + thick * 0.008f + ((i + 0.5f) / streaks) * (0.045f + 0.09f * std::min(1.f, S.smearMax)));
    float hh = (0.011f + 0.010f * thick) * (0.75f + 0.45f * blurK);
    Color col = tbColor(S.T->tbColors, u, S.L->hueSpan, S.L->sat);
    Quad q; q.col = col; q.pos = {(head + tail) * 0.5f, y}; q.size = {std::abs(head - tail) * 0.5f, hh};
    if (side > 0.f) { q.uv[0] = 0; q.uv[2] = 1; } else { q.uv[0] = 1; q.uv[2] = 0; }
    q.uv[1] = 1; q.uv[3] = 0;
    q.col.a = S.A * amp * (0.30f + 0.70f * d);
    push(S, q, S.tWhip);
    q.uv[0] = 0; q.uv[1] = 0; q.uv[2] = 1; q.uv[3] = 1;
    q.pos = {head, y}; q.size = {hh * (2.4f + glowK), hh * (2.1f + 0.6f * glowK)};
    q.col.a = S.A * amp * 0.55f * glowK * (0.4f + 0.6f * d);
    if (glowK > 0.02f) push(S, q, S.tGlow);
  }
  S.sp->Flush(true);
}
static void drawRain(BarState& S, float edge, float dir, float amp) {
  const int drops = std::clamp(S.N * 3, 36, 96);
  float thick = std::clamp(S.T->tbThick, 0.2f, 3.f);
  float blurK = std::clamp(S.T->tbBlur, 0.f, 2.5f), glowK = std::clamp(S.T->tbGlow, 0.f, 2.5f);
  float spacing = S.span / drops;
  S.sp->SetAdditive(true);
  drawEdgeBar(S, edge, dir, amp, std::min(S.N, 24), 0.7f);
  for (int i = 0; i < drops; ++i) {
    float u = (i + 0.5f) / drops;
    float hsh = hash1(i * 1.7f + 3.1f);
    float c = sampleCol(S, u);
    float fall = fracf(S.time * (0.28f + 0.85f * hsh) * (0.65f + 0.35f * std::min(2.f, S.T->tbSens)) + hsh);
    float trail = std::min(1.8f, 2.f * S.smearMax * (0.30f + 0.70f * std::max(S.beat, 0.15f)) * (0.35f + 0.65f * c));
    float drop = std::max(0.028f, trail * (0.045f + 0.05f * hsh));
    float y = edge + dir * (0.03f + fall * std::max(drop, trail));
    float w = std::max(0.0075f, spacing * 0.62f * thick);
    Color col = tbColor(S.T->tbColors, u, S.L->hueSpan, std::min(1.f, S.L->sat + 0.1f));
    Quad q; setFallUV(q, dir); q.col = col; q.pos = {S.x0 + S.span * u + (hsh - 0.5f) * spacing * 0.8f, y};
    q.size = {w * (1.8f + blurK) * 0.5f, drop * 0.55f};
    q.col.a = S.A * amp * 0.16f * glowK * (0.35f + 0.65f * c);
    if (glowK > 0.02f) push(S, q, S.tGlow);
    q.size = {w * 0.5f, drop * 0.5f};
    q.col.a = S.A * amp * (0.45f + 0.5f * c) * (0.35f + 0.65f * S.beat);
    push(S, q, S.tRain);
  }
  S.sp->Flush(true);
}
static void drawFog(BarState& S, float edge, float dir, float amp) {
  const int blooms = 8;
  float blurK = std::clamp(S.T->tbBlur, 0.2f, 2.5f), glowK = std::clamp(S.T->tbGlow, 0.f, 2.5f);
  float thick = std::clamp(S.T->tbThick, 0.2f, 3.f);
  S.sp->SetAdditive(true);
  drawEdgeBar(S, edge, dir, amp, blooms, 0.28f);
  for (int i = 0; i < blooms; ++i) {
    float u = (i + 0.5f) / blooms;
    float c = sampleCol(S, u);
    float breathe = 0.86f + 0.14f * std::sin(S.time * 0.65f + i * 1.2f);
    float rad = 0.20f * (0.6f + 0.9f * c) * (0.65f + 0.55f * blurK) * (0.55f + 0.45f * std::min(1.f, S.smearMax)) * breathe;
    rad *= 0.75f + 0.25f * thick;
    float x = S.x0 + S.span * u + std::sin(S.time * 0.28f + i) * 0.04f;
    float y = edge + dir * (0.05f + rad * 0.72f);
    Color col = tbColor(S.T->tbColors, u, S.L->hueSpan, S.L->sat * 0.9f);
    Quad q; q.uv[0] = 0; q.uv[1] = 1; q.uv[2] = 1; q.uv[3] = 0; q.col = col; q.pos = {x, y};
    q.size = {rad * 1.35f, rad};
    q.col.a = S.A * amp * (0.07f + 0.06f * glowK) * (0.4f + 0.6f * std::max(S.beat, 0.25f));
    push(S, q, S.tFog);
    q.size = {rad * 0.72f, rad * 0.62f};
    q.col.a = S.A * amp * 0.11f * (0.45f + 0.55f * c);
    push(S, q, S.tFog);
  }
  S.sp->Flush(true);
}
static void drawMirrorTrails(BarState& S, float edge, float dir, float amp) {
  const int n = std::clamp(S.N, 8, 28);
  float thick = std::clamp(S.T->tbThick, 0.2f, 3.f);
  float blurK = std::clamp(S.T->tbBlur, 0.f, 2.5f), glowK = std::clamp(S.T->tbGlow, 0.f, 2.5f);
  float spacing = S.span / n;
  S.sp->SetAdditive(true);
  drawEdgeBar(S, edge, dir, amp, std::min(n, 16), 0.8f);
  for (int i = 0; i < n; ++i) {
    float u = (i + 0.5f) / n;
    float d = driveOf(sampleCol(S, u), S.beat);
    float len = std::min(0.74f, 2.f * S.smearMax * (0.38f + 0.62f * d));
    if (len < 0.02f) continue;
    Color col = tbColor(S.T->tbColors, u, S.L->hueSpan, S.L->sat);
    const int segs = 6;
    for (int s = 0; s < segs; ++s) {
      float t = (s + 0.5f) / segs;
      float x = S.x0 + S.span * u + std::sin(S.time * 0.8f + i * 0.55f + t * 2.2f) * 0.028f;
      float y = edge + dir * (0.02f + len * t);
      float fade = (1.f - t) * (1.f - t);
      float w = spacing * 0.55f * thick * (1.f - 0.55f * t) * (0.85f + 0.25f * blurK);
      Quad q; setFallUV(q, dir); q.col = col; q.pos = {x, y};
      q.size = {w * 0.5f, (len / segs) * 0.7f};
      q.col.a = S.A * amp * fade * (0.35f + 0.4f * glowK) * (0.4f + 0.6f * d);
      push(S, q, S.tMirror);
    }
  }
  S.sp->Flush(true);
}
static void drawStagger(BarState& S, float edge, float dir, float amp) {
  // One left-to-right sweep every 1/0.30 s, then a short rest (cycle 1.35).
  // age 0 is the wave front; the wake is behind it (smaller x) and ahead stays dark.
  const float wave = std::fmod(std::max(S.time, 0.f) * 0.30f, 1.35f);
  float thick = std::clamp(S.T->tbThick, 0.2f, 3.f);
  float blurK = std::clamp(S.T->tbBlur, 0.f, 2.5f), glowK = std::clamp(S.T->tbGlow, 0.f, 2.5f);
  S.sp->SetAdditive(true);
  for (int i = 0; i < S.N; ++i) {
    float pos = (i + 0.5f) / S.N;
    float age = wave - pos;
    float env = (age >= 0.f && age < 0.62f) ? std::exp(-age * 6.2f) : 0.f;
    float c = colAt(S, i);
    float bh = 2.f * S.barFrac * (1.f + S.L->barPulse * c);
    float cx = S.x0 + S.cw * (i + 0.5f);
    Color col = tbColor(S.T->tbColors, pos, S.L->hueSpan, S.L->sat);
    Quad q; q.uv[0] = 0; q.uv[1] = 1; q.uv[2] = 1; q.uv[3] = 0; q.col = col;
    q.pos = {cx, edge + dir * bh * 0.5f}; q.size = {S.cw * 0.48f, bh * 0.5f};
    q.col.a = S.A * amp * (0.12f + 0.88f * env);
    push(S, q, S.tBar);
    float len = std::min(1.7f, 2.f * S.smearMax * env * (0.35f + 0.65f * c) * (0.3f + 0.7f * std::max(S.beat, 0.2f)));
    if (len < 0.015f) continue;
    setFallUV(q, dir);
    q.pos = {cx, edge + dir * (bh + len * 0.5f)};
    q.size = {S.cw * 0.42f * thick * (0.75f + 0.4f * blurK), len * 0.5f};
    q.col.a = S.A * amp * (0.25f + 0.75f * env);
    push(S, q, S.tStagger);
    if (glowK > 0.02f && age >= 0.f && age < 0.1f) {
      q.uv[0] = 0; q.uv[1] = 0; q.uv[2] = 1; q.uv[3] = 1;
      q.pos = {cx, edge + dir * (bh + 0.02f)}; q.size = {S.cw * (1.4f + blurK), bh * (2.f + glowK)};
      q.col.a = S.A * amp * 0.45f * glowK;
      push(S, q, S.tGlow);
    }
  }
  S.sp->Flush(true);
}
static void drawStyled(BarState& S, int style, float edge, float dir, float amp) {
  switch (style) {
    case 1: drawCascade(S, edge, dir, amp); break;
    case 2: drawWhip(S, edge, dir, amp); break;
    case 3: drawRain(S, edge, dir, amp); break;
    case 4: drawFog(S, edge, dir, amp); break;
    case 5: drawMirrorTrails(S, edge, dir, amp); break;
    case 6: drawStagger(S, edge, dir, amp); break;
    default: drawClassic(S, edge, dir, amp); break;
  }
}
} // namespace

void Engine::DrawTopBar(const LayerDef& L, float e, float fade) {
  const TunerState& T = m_tuner.s;
  if (fade <= 0.001f || T.tbOpacity <= 0.001f) return;
  const int N = T.tbColumns > 0 ? std::clamp(T.tbColumns, 4, 128) : std::clamp(L.columns, 4, 128);
  m_env.Columns(N, m_dt, m_cols);
  auto tx = [&](const char* n) { const AtlasRegion* r = m_atlas.Find(n); return r ? r->tex : 0u; };
  float raw = std::clamp(e * T.tbSens * (1.f + L.env.grow), 0.f, 1.f);
  float rel = std::max(0.02f, L.env.release * T.tbRelease);
  m_tbBeat = raw > m_tbBeat ? raw : m_tbBeat + (raw - m_tbBeat) * std::min(1.f, m_dt / rel);
  BarState S;
  S.L = &L; S.T = &T; S.sp = &m_sprites; S.cols = &m_cols; S.time = m_time;
  S.beat = m_tbBeat * m_tbBeat * (3.f - 2.f * m_tbBeat);
  S.A = fade * T.intensity * std::clamp(T.tbOpacity, 0.f, 1.f);
  S.barFrac = L.barH * T.tbThick * T.tbHeight;
  S.smearMax = L.smearMax * T.tbSmear * T.tbHeight;
  S.span = T.tbAlign == 0 ? 2.f : 1.1f;
  S.x0 = (T.tbAlign == 1 ? -1.f : T.tbAlign == 3 ? 1.f - S.span : -S.span * 0.5f) + 2.f * std::clamp(T.tbOffX, -1.f, 1.f);
  S.cw = S.span / N; S.N = N;
  S.tBar = tx("bar_soft"); S.tSmear = tx("smear_fall"); S.tGlow = tx("glow_disc");
  S.tCascade = tx("cascade_trail"); S.tWhip = tx("whip_streak"); S.tRain = tx("rain_line");
  S.tFog = tx("fog_bloom"); S.tMirror = tx("mirror_trail"); S.tStagger = tx("stagger_pulse");
  float shift = 2.f * std::clamp(T.tbOffY, -1.f, 1.f);
  float top = 1.f - shift, bot = -1.f - shift;
  int style = std::clamp(T.smearStyle, 0, 6);
  int place = std::clamp(T.smearPlace, 0, 2);
  auto emit = [&](float edge, float dir, float amp) {
    if (style == 0) drawClassic(S, edge, dir, amp);
    else drawStyled(S, style, edge, dir, amp);
  };
  // Style E is the mirrored inward look: Top/Bottom bias one side and keep a ghost of the other.
  // Mirror placement draws both sides of every style. Bottom rises (dir +1).
  if (style == 5 && place != 2) {
    emit(top, -1.f, place == 0 ? 1.f : 0.42f);
    emit(bot, 1.f, place == 1 ? 1.f : 0.42f);
  } else if (place == 2) {
    emit(top, -1.f, 0.92f);
    emit(bot, 1.f, 0.92f);
  } else if (place == 1) {
    emit(bot, 1.f, 1.f);
  } else {
    emit(top, -1.f, 1.f);
  }
}
} // namespace bezel
