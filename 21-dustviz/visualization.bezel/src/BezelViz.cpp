// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#include "BezelViz.h"
#include <kodi/Filesystem.h>
// Frequency bins are delivered through AudioData on Kodi 21+.
bool CVisualizationBezel::Start(int, int, int, const std::string&) {
#if defined(HAS_GLES)
  const bool gles = true;
#else
  const bool gles = false;
#endif
  bezel::Sprites::SetDevice(Device());   // DX11 context on Windows; ignored on GL/GLES
  std::string skin = kodi::vfs::TranslateSpecialProtocol("special://skin/");
  m_started = m_engine.Init(kodi::addon::GetAddonPath(), skin, gles);
  m_last = std::chrono::steady_clock::now();
  return m_started;
}
void CVisualizationBezel::Stop() { if (m_started) m_engine.DeInit(); m_started = false; }
void CVisualizationBezel::AudioData(const float* d, size_t n) { m_engine.OnAudio(d, n); }
void CVisualizationBezel::Render() {
  if (!m_started) return;
  auto now = std::chrono::steady_clock::now();
  float dt = std::chrono::duration<float>(now - m_last).count(); m_last = now;
  m_engine.Frame(dt > 0.1f ? 0.1f : dt);   // never draws Kodi UI; viz rect only
}
ADDON_STATUS CVisualizationBezel::SetSetting(const std::string& n, const kodi::addon::CSettingValue& v) {
  if (!m_engine.GetTuner().OnSetting(n, v.GetString())) return ADDON_STATUS_UNKNOWN;
  if (n == "active_style" || n == "pack_root" || n == "particle_cap") m_engine.ReloadPack();
  return ADDON_STATUS_OK;
}
ADDONCREATOR(CBezelAddon)
