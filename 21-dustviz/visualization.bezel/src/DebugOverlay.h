// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine; structure derived from visualization.spectrum)
#pragma once
#include "Types.h"
namespace bezel {
class Sprites; class AudioEnvelopes;
// fps / bins / active style. STUB: draws 3 bin bars as quads; text (fps/style) logged, no font yet.
class DebugOverlay { public: void Draw(Sprites& sp, const AudioEnvelopes& e, float fps, const std::string& style, size_t particles); private: float m_logT = 0; };
}
