// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#pragma once
#include "Engine.h"
#include <chrono>
#include <kodi/addon-instance/Visualization.h>
class ATTR_DLL_LOCAL CVisualizationBezel : public kodi::addon::CInstanceVisualization {
public:
  explicit CVisualizationBezel(const kodi::addon::IInstanceInfo& instance)
    : kodi::addon::CInstanceVisualization(instance) {}
  ~CVisualizationBezel() override = default;
  bool Start(int channels, int samplesPerSec, int bitsPerSample, const std::string& songName) override;
  void Stop() override;
  void Render() override;
  void AudioData(const float* audioData, size_t audioDataLength) override;
  // Kodi 21+: frequency bins arrive via AudioData; no GetInfo. Optional sync delay:
  int GetSyncDelay() override { return 0; }
  ADDON_STATUS SetSetting(const std::string& name, const kodi::addon::CSettingValue& value);
private:
  bezel::Engine m_engine; bool m_started = false;
  std::chrono::steady_clock::time_point m_last;
};

// Multi-instance addon base: Kodi 21 calls CreateInstance explicitly.
class ATTR_DLL_LOCAL CBezelAddon : public kodi::addon::CAddonBase {
public:
  CBezelAddon() = default;
  ADDON_STATUS CreateInstance(const kodi::addon::IInstanceInfo& instance,
                              KODI_ADDON_INSTANCE_HDL& hdl) override {
    if (instance.IsType(ADDON_INSTANCE_VISUALIZATION)) {
      m_viz = new CVisualizationBezel(instance);
      hdl = m_viz;
      return ADDON_STATUS_OK;
    }
    return ADDON_STATUS_NOT_IMPLEMENTED;
  }
  void DestroyInstance(const kodi::addon::IInstanceInfo&, const KODI_ADDON_INSTANCE_HDL hdl) override {
    if (hdl == m_viz) m_viz = nullptr;
  }
  ADDON_STATUS SetSetting(const std::string& n, const kodi::addon::CSettingValue& v) override {
    return m_viz ? m_viz->SetSetting(n, v) : ADDON_STATUS_OK;
  }
private:
  CVisualizationBezel* m_viz = nullptr;
};
