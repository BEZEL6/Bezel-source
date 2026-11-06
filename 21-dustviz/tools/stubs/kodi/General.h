#pragma once
#include <cstdarg>
#include <cstdio>
#include <map>
#include <string>
enum ADDON_LOG { ADDON_LOG_DEBUG = 0, ADDON_LOG_INFO, ADDON_LOG_WARNING, ADDON_LOG_ERROR, ADDON_LOG_FATAL };
namespace kodi {
inline std::string& LogText() { static std::string s; return s; }
inline void Log(ADDON_LOG, const char* fmt, ...) {
  char buf[1200]; va_list ap; va_start(ap, fmt); std::vsnprintf(buf, sizeof buf, fmt, ap); va_end(ap);
  LogText() += buf; LogText() += '\n'; std::fprintf(stderr, "%s\n", buf);
}
namespace addon {
inline std::map<std::string, std::string>& Settings() { static std::map<std::string, std::string> m; return m; }
inline std::string GetSettingString(const std::string& n, const std::string& d) {
  auto it = Settings().find(n); return it == Settings().end() ? d : it->second;
}
inline int GetSettingInt(const std::string& n, int d) {
  auto it = Settings().find(n); if (it == Settings().end()) return d; return std::stoi(it->second);
}
inline bool GetSettingBoolean(const std::string& n, bool d) {
  auto it = Settings().find(n); if (it == Settings().end()) return d; return it->second == "true" || it->second == "1";
}
inline void SetSettingInt(const std::string& n, int v) { Settings()[n] = std::to_string(v); }
}
namespace vfs {
inline std::string& TempRoot() { static std::string t = "/tmp/bezelviz-smoke/"; return t; }
inline std::string TranslateSpecialProtocol(const std::string& s) {
  if (s.rfind("special://temp/", 0) == 0) return TempRoot();
  return s;
}
}
}
