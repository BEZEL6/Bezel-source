// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine)
#pragma once
// Tiny read-only JSON parser for pack manifests (objects, arrays, strings, numbers, bools, null).
#include <map>
#include <memory>
#include <string>
#include <vector>
namespace bezel {
struct JVal {
  enum T { Null, Bool, Num, Str, Arr, Obj } t = Null;
  bool b = false; double n = 0; std::string s; std::vector<JVal> a; std::map<std::string, JVal> o;
  const JVal* get(const std::string& k) const { if (t != Obj) return nullptr; auto it = o.find(k); return it == o.end() ? nullptr : &it->second; }
  std::string str(const std::string& k, const std::string& d = "") const { auto v = get(k); return v && v->t == Str ? v->s : d; }
  float num(const std::string& k, float d = 0) const { auto v = get(k); return v && v->t == Num ? (float)v->n : d; }
  bool boolean(const std::string& k, bool d = false) const { auto v = get(k); return v && v->t == Bool ? v->b : d; }
};
bool ParseJson(const std::string& text, JVal& out);
}
