// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#pragma once
#include <cstddef>
#include <vector>
namespace bezel {
// Low/mid/high envelopes from Kodi AudioData bins (attack/release smoothing). IMPLEMENTED (basic).
class AudioEnvelopes {
public:
  void Feed(const float* bins, size_t count, float gain);
  void Tick(float dt);               // decays toward silence; updates idle timer
  float low = 0, mid = 0, high = 0, level = 0;
  // per-column levels (log-spaced over bins, auto-gained, smoothed) for TopBar
  void Columns(int n, float dt, std::vector<float>& out);
  std::vector<float> raw;
  bool Silent() const { return m_silentFor > 1.5f; }
private:
  std::vector<float> m_peak; float m_silentFor = 0, m_rawL = 0, m_rawM = 0, m_rawH = 0;
};
}
