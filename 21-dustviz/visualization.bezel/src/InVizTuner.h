// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine)
#pragma once
#include "Types.h"
#include <map>
namespace bezel {
class Sprites; class Tuner;
// LIVE in-viz tuner menu. Kodi gives viz addons no key input, so keys arrive as commands:
// keymap -> RunScript(resources/tuner_cmd.py,<cmd>) -> appends "<seq> <cmd>" to special://temp/bezelviz_cmd.txt
// -> engine polls (~10 Hz) and applies. Engine writes special://temp/bezelviz_state.txt ("open 0|1").
// Values are written back with kodi::addon::SetSettingInt, so they persist and match Kodi addon settings.
struct TunerItem { const char* id; const char* label; int min, max, step, def; const char* const* names = nullptr; const char* group = ""; };
class InVizTuner {
public:
  void Init(const std::string& addonPath, Sprites& sp, Tuner& t);
  void Poll(float dt, Tuner& t);                  // read new commands
  void Draw(Sprites& sp, float aspect, float time);
  bool Open() const { return m_open; }
  void Apply(const std::string& cmd, Tuner& t);   // up/down/left/right/toggle/close/reset/pageup/pagedown
  void SetSmear(bool smear);                     // topbar pack uses the smear tuner; hair pack keeps the legacy menu
private:
  void Text(Sprites& sp, const std::string& s, float x, float y, float h, Color c, float aspect);
  void WriteState();
  void DrawLegacy(Sprites& sp, float aspect, float time);
  void DrawSmear(Sprites& sp, float aspect, float time);
  void AdjustLegacy(const std::string& c, Tuner& t);
  void AdjustSmear(const std::string& c, Tuner& t);
  std::map<std::string, int> m_v; int m_sel = 0; bool m_open = false; unsigned m_font = 0, m_knob = 0;
  bool m_smear = false, m_haveMode = false;
  std::string m_cmdPath, m_statePath; long m_lastSeq = -1; float m_pollT = 0, m_flash = 0;
  bool m_primed = false;
};
}
