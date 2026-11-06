// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#include "AudioEnvelopes.h"
#include "Types.h"
#include <algorithm>
#include <cmath>
namespace bezel {
void AudioEnvelopes::Feed(const float* b, size_t n, float gain) {
  if (!b || n < 3) return;
  raw.assign(b, b + n); for (auto& v : raw) v = std::fabs(v) * gain;
  size_t l = n / 8, m = n / 2; // rough splits: 0..1/8 low, ..1/2 mid, rest high
  auto avg = [&](size_t s, size_t e){ float a = 0; for (size_t i = s; i < e; ++i) a += std::fabs(b[i]); return e > s ? a / (e - s) : 0.f; };
  m_rawL = avg(0, std::max<size_t>(l,1)) * gain; m_rawM = avg(l, m) * gain; m_rawH = avg(m, n) * gain;
}
void AudioEnvelopes::Tick(float dt) {
  auto env = [&](float& v, float raw){ float k = raw > v ? 0.5f : 0.08f; v += (std::min(raw, 1.f) - v) * k; };
  env(low, m_rawL); env(mid, m_rawM); env(high, m_rawH);
  level = (low + mid + high) / 3.f;
  m_silentFor = level < kSilenceThreshold ? m_silentFor + dt : 0.f;
}
void AudioEnvelopes::Columns(int n, float dt, std::vector<float>& out) {
  if ((int)out.size() != n) out.assign(n, 0.f); if ((int)m_peak.size() != n) m_peak.assign(n, 0.05f);
  size_t N = raw.size(); size_t lo = 1;
  for (int i = 0; i < n; ++i) {
    float v = 0.f;
    if (N > 4) { size_t s = lo + (size_t)((N * 0.7f - lo) * std::pow((float)i / n, 1.6f)), e = lo + (size_t)((N * 0.7f - lo) * std::pow((float)(i + 1) / n, 1.6f));
      if (e <= s) e = s + 1; e = std::min(e, N); for (size_t k = s; k < e; ++k) v = std::max(v, raw[k]); }
    float& pk = m_peak[i]; pk = std::max(v, pk * (1.f - 0.25f * dt)); pk = std::max(pk, 0.02f);
    float t = std::min(1.f, v / pk), &o = out[i]; float k = t > o ? std::min(1.f, dt * 18.f) : std::min(1.f, dt * 3.f); o += (t - o) * k;
  }
}
}
