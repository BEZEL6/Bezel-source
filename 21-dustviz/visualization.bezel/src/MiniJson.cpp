// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine)
#include "MiniJson.h"
#include <cstdlib>
namespace bezel {
namespace {
struct P {
  const std::string& s; size_t i = 0; bool ok = true;
  void ws() { while (i < s.size() && (s[i]==' '||s[i]=='\n'||s[i]=='\r'||s[i]=='\t')) ++i; }
  bool lit(const char* w) { size_t n = 0; while (w[n]) ++n; if (s.compare(i, n, w) == 0) { i += n; return true; } return false; }
  std::string string() {
    std::string r; ++i;
    while (i < s.size() && s[i] != '"') {
      if (s[i] == '\\' && i + 1 < s.size()) { ++i; char c = s[i]; r += c=='n'?'\n':c=='t'?'\t':c=='u'?'?':c; if (c=='u') i += 4; ++i; }
      else r += s[i++];
    }
    if (i >= s.size()) ok = false; else ++i; return r;
  }
  void value(JVal& v) {
    ws(); if (i >= s.size()) { ok = false; return; }
    char c = s[i];
    if (c == '{') { v.t = JVal::Obj; ++i; ws(); if (s[i]=='}') { ++i; return; }
      while (ok) { ws(); if (s[i] != '"') { ok = false; return; } std::string k = string(); ws(); if (s[i] != ':') { ok = false; return; } ++i;
        value(v.o[k]); ws(); if (s[i] == ',') { ++i; continue; } if (s[i] == '}') { ++i; return; } ok = false; } }
    else if (c == '[') { v.t = JVal::Arr; ++i; ws(); if (s[i]==']') { ++i; return; }
      while (ok) { v.a.emplace_back(); value(v.a.back()); ws(); if (s[i] == ',') { ++i; continue; } if (s[i] == ']') { ++i; return; } ok = false; } }
    else if (c == '"') { v.t = JVal::Str; v.s = string(); }
    else if (lit("true")) { v.t = JVal::Bool; v.b = true; }
    else if (lit("false")) { v.t = JVal::Bool; v.b = false; }
    else if (lit("null")) { v.t = JVal::Null; }
    else { char* e = nullptr; v.n = std::strtod(s.c_str() + i, &e); if (e == s.c_str() + i) { ok = false; return; } v.t = JVal::Num; i = e - s.c_str(); }
  }
};
}
bool ParseJson(const std::string& text, JVal& out) { P p{text}; out = JVal(); p.value(out); return p.ok; }
}
