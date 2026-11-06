// Headless GL smoke for visualization.bezel smear. Not Kodi. Not Windows.
#include "Engine.h"
#include <kodi/General.h>
#include <GL/osmesa.h>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <fstream>
#include <iostream>
#include <sys/stat.h>
#include <vector>
static const int W = 1280, H = 720;
static void bins(float* b, int n) {
  for (int i = 0; i < n; ++i) {
    float u = (i + 0.5f) / n;
    float v = 0.35f
      + 0.9f * std::exp(-std::pow((u - 0.08f) / 0.07f, 2.f))
      + 0.75f * std::exp(-std::pow((u - 0.30f) / 0.08f, 2.f))
      + 0.8f * std::exp(-std::pow((u - 0.55f) / 0.09f, 2.f))
      + 0.65f * std::exp(-std::pow((u - 0.80f) / 0.08f, 2.f));
    b[i] = std::max(0.f, v);
  }
}
static void saveRaw(const std::string& path, const std::vector<unsigned char>& top) {
  std::ofstream f(path, std::ios::binary); f.write((char*)top.data(), top.size());
}
static std::vector<unsigned char> readTop() {
  std::vector<unsigned char> src(W * H * 4), top(W * H * 4);
  glReadPixels(0, 0, W, H, GL_RGBA, GL_UNSIGNED_BYTE, src.data());
  for (int y = 0; y < H; ++y) std::memcpy(top.data() + y * W * 4, src.data() + (H - 1 - y) * W * 4, W * 4);
  return top;
}
static float luma(const std::vector<unsigned char>& p, int x, int y) {
  int i = (y * W + x) * 4; return (p[i] + p[i + 1] + p[i + 2]) / (3.f * 255.f);
}
static float region(const std::vector<unsigned char>& p, int x0, int y0, int x1, int y1) {
  double s = 0; int n = 0;
  for (int y = y0; y < y1; y += 2) for (int x = x0; x < x1; x += 2) { s += luma(p, x, y); ++n; }
  return n ? (float)(s / n) : 0;
}
static int fails = 0;
static void expect(bool ok, const std::string& msg) {
  std::cout << (ok ? "PASS " : "FAIL ") << msg << "\n"; if (!ok) ++fails;
}
int main(int argc, char** argv) {
  std::string root = argc > 1 ? argv[1] : ".";
  std::string shots = root + "/tools/shots";
  mkdir("/tmp/bezelviz-smoke", 0777);
  std::remove("/tmp/bezelviz-smoke/bezelviz_cmd.txt");
  std::remove("/tmp/bezelviz-smoke/bezelviz_state.txt");
  mkdir(shots.c_str(), 0777);
  std::vector<unsigned char> buf(W * H * 4);
  OSMesaContext ctx = OSMesaCreateContextExt(OSMESA_RGBA, 16, 0, 0, nullptr);
  if (!ctx || !OSMesaMakeCurrent(ctx, buf.data(), GL_UNSIGNED_BYTE, W, H)) {
    std::cerr << "BLOCKER OSMesa context failed\n"; return 2;
  }
  glViewport(0, 0, W, H);
  std::string addon = root + "/visualization.bezel/visualization.bezel";
  std::string skin = root + "/tools/empty-skin";
  mkdir(skin.c_str(), 0777);
  bezel::Engine eng;
  if (!eng.Init(addon, skin, false)) { std::cerr << "BLOCKER engine init failed\n"; return 2; }
  expect(kodi::LogText().find("topbar_smear") != std::string::npos && kodi::LogText().find("loaded") != std::string::npos, "bundled topbar_smear loaded");
  expect(kodi::LogText().find("resources/packs/topbar_smear") != std::string::npos, "pack path is addon resources/packs");
  expect(eng.GetTuner().s.activeStyle == "topbar_smear", "default active_style topbar_smear");
  expect(eng.GetTuner().s.smearStyle == 1, "default smear style A cascade");
  expect(eng.GetTuner().s.smearPlace == 0, "default placement top");
  float b[256]; bins(b, 256);
  auto step = [&](float dt) { glClearColor(0, 0, 0, 1); glClear(GL_COLOR_BUFFER_BIT); eng.OnAudio(b, 256); eng.Frame(dt); };
  for (int i = 0; i < 90; ++i) step(1.f / 60.f);
  auto cascade = readTop(); saveRaw(shots + "/cascade-top.raw", cascade);
  float topE = region(cascade, 0, 0, W, H / 3), botE = region(cascade, 0, 2 * H / 3, W, H);
  std::cout << "cascade topE=" << topE << " botE=" << botE << "\n";
  expect(topE > 0.02f, "cascade drew pixels");
  expect(topE > botE, "cascade top placement is brighter toward the top");
  eng.GetTuner().OnSetting("smear_place", "1"); step(1.f / 60.f);
  auto bottom = readTop(); saveRaw(shots + "/cascade-bottom.raw", bottom);
  float bTop = region(bottom, 0, 0, W, H / 3), bBot = region(bottom, 0, 2 * H / 3, W, H);
  std::cout << "bottom topE=" << bTop << " botE=" << bBot << "\n";
  expect(bBot > bTop, "bottom placement rises (brighter toward the bottom)");
  eng.GetTuner().OnSetting("smear_place", "2"); step(1.f / 60.f);
  auto mirror = readTop(); saveRaw(shots + "/cascade-mirror.raw", mirror);
  float mTop = region(mirror, 0, 0, W, H / 5), mBot = region(mirror, 0, 4 * H / 5, W, H);
  std::cout << "mirror edgeTop=" << mTop << " edgeBot=" << mBot << "\n";
  expect(mTop > 0.015f && mBot > 0.015f, "mirror placement draws both edges");
  eng.GetTuner().OnSetting("smear_place", "0");
  for (int i = 0; i < 5; ++i) step(1.f / 60.f);
  std::ofstream cmd("/tmp/bezelviz-smoke/bezelviz_cmd.txt"); cmd << "10 toggle\n"; cmd.close();
  step(0.1f);
  std::ifstream st("/tmp/bezelviz-smoke/bezelviz_state.txt"); std::string state((std::istreambuf_iterator<char>(st)), {});
  expect(state.find("open 1") != std::string::npos, "T/toggle opens tuner");
  auto tuner = readTop(); saveRaw(shots + "/tuner-open.raw", tuner);
  expect(region(tuner, (int)(W * 0.62f), 0, W, H) > 0.01f, "tuner panel has pixels on the right");
  std::ofstream cmd2("/tmp/bezelviz-smoke/bezelviz_cmd.txt", std::ios::app); cmd2 << "11 down\n"; cmd2.close();
  step(0.1f);
  expect(eng.GetTuner().s.smearPlace == 0, "down from style lands on placement still Top");
  std::ofstream cmd3("/tmp/bezelviz-smoke/bezelviz_cmd.txt", std::ios::app); cmd3 << "12 right\n"; cmd3.close();
  step(0.1f);
  expect(eng.GetTuner().s.smearPlace == 1, "right adjusts placement to Bottom");
  auto tuned = readTop(); saveRaw(shots + "/tuner-place-bottom.raw", tuned);
  std::ofstream cmd4("/tmp/bezelviz-smoke/bezelviz_cmd.txt", std::ios::app); cmd4 << "13 reset\n14 close\n"; cmd4.close();
  step(0.1f);
  expect(eng.GetTuner().s.smearPlace == 0, "OK resets placement to Top");
  std::ifstream st2("/tmp/bezelviz-smoke/bezelviz_state.txt"); std::string state2((std::istreambuf_iterator<char>(st2)), {});
  expect(state2.find("open 0") != std::string::npos, "Back/close shuts tuner");
  struct Shot { int style; const char* name; };
  Shot more[] = {{0, "original-top"}, {2, "whip"}, {3, "rain"}, {4, "fog"}, {5, "mirror-style"}, {6, "stagger"}};
  for (auto& s : more) {
    eng.GetTuner().OnSetting("smear_style", std::to_string(s.style));
    eng.GetTuner().OnSetting("smear_place", "0");
    step(1.f / 60.f);
    auto im = readTop();
    saveRaw(shots + "/" + s.name + ".raw", im);
    std::cout << s.name << " topE=" << region(im, 0, 0, W, H / 3) << " botE=" << region(im, 0, 2 * H / 3, W, H)
              << " leftE=" << region(im, 0, 0, W / 2, H) << " rightE=" << region(im, W / 2, 0, W, H) << "\n";
  }
  std::cout << (fails ? "SMOKE FAIL\n" : "SMOKE PASS\n");
  return fails ? 1 : 0;
}
