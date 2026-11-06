// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine) DirectX 11 sprite backend for Kodi on Windows.
// Mirrors Sprites.cpp (GL) 1:1: same Quad batching, same vertex layout (pos2 uv2 col4), same blend modes.
// Pattern follows visualization.spectrum/src/directx_spectrum.cpp (context from Kodi Device()), but shaders are
// compiled at runtime from resources/shaders/DX11/*.hlsl via D3DCompile so no fxc build step is needed.
#ifdef BEZEL_DX11
#include "Sprites.h"
#include "ChromaKey.h"
#include <d3d11.h>
#include <d3dcompiler.h>
#include <cmath>
#include <cstring>
#include <fstream>
#include <sstream>
#include <vector>
#include <kodi/General.h>
#define STB_IMAGE_IMPLEMENTATION
#define STBI_ONLY_PNG
#include "third_party/stb_image.h"
#pragma comment(lib, "d3d11.lib")
#pragma comment(lib, "d3dcompiler.lib")
namespace bezel {
static ID3D11DeviceContext* g_ctx = nullptr;
void Sprites::SetDevice(void* ctx) { g_ctx = static_cast<ID3D11DeviceContext*>(ctx); }
template <class T> static void rel(T*& p) { if (p) { p->Release(); p = nullptr; } }
struct Sprites::DX {
  ID3D11Device* dev = nullptr; ID3D11DeviceContext* ctx = nullptr;
  ID3D11VertexShader* vs = nullptr; ID3D11PixelShader* ps = nullptr; ID3D11InputLayout* il = nullptr;
  ID3D11Buffer* vb = nullptr; UINT vbBytes = 0;
  ID3D11BlendState* bAdd = nullptr; ID3D11BlendState* bAlpha = nullptr;
  ID3D11SamplerState* smp = nullptr; ID3D11RasterizerState* rs = nullptr; ID3D11DepthStencilState* ds = nullptr;
  std::vector<ID3D11ShaderResourceView*> tex;   // handle h -> tex[h-1]; nullptr = freed slot
};
static std::string readFile(const std::string& p){ std::ifstream f(p, std::ios::binary); std::stringstream s; s << f.rdbuf(); return s.str(); }
static ID3DBlob* compileHlsl(const std::string& src, const char* target) {
  ID3DBlob *code = nullptr, *err = nullptr;
  HRESULT hr = D3DCompile(src.data(), src.size(), nullptr, nullptr, nullptr, "main", target, D3DCOMPILE_OPTIMIZATION_LEVEL3, 0, &code, &err);
  if (FAILED(hr)) { kodi::Log(ADDON_LOG_ERROR, "BezelViz DX11: shader %s failed: %s", target, err ? (const char*)err->GetBufferPointer() : "?"); rel(code); }
  rel(err); return code;
}
static unsigned makeTex(Sprites::DX* d, const unsigned char* px, int w, int h) {
  D3D11_TEXTURE2D_DESC td = {}; td.Width = w; td.Height = h; td.MipLevels = 1; td.ArraySize = 1;
  td.Format = DXGI_FORMAT_R8G8B8A8_UNORM; td.SampleDesc.Count = 1; td.Usage = D3D11_USAGE_IMMUTABLE; td.BindFlags = D3D11_BIND_SHADER_RESOURCE;
  D3D11_SUBRESOURCE_DATA sd = {}; sd.pSysMem = px; sd.SysMemPitch = w * 4;
  ID3D11Texture2D* t = nullptr; if (FAILED(d->dev->CreateTexture2D(&td, &sd, &t))) return 0;
  ID3D11ShaderResourceView* srv = nullptr; HRESULT hr = d->dev->CreateShaderResourceView(t, nullptr, &srv); t->Release();
  if (FAILED(hr)) return 0;
  d->tex.push_back(srv); return (unsigned)d->tex.size();
}
bool Sprites::Init(const std::string& dir) {
  if (!g_ctx) { kodi::Log(ADDON_LOG_ERROR, "BezelViz DX11: no device context from Kodi"); return false; }
  m_dx = new DX; DX& d = *m_dx; d.ctx = g_ctx; d.ctx->AddRef(); d.ctx->GetDevice(&d.dev);
  ID3DBlob* vsb = compileHlsl(readFile(dir + "vert.hlsl"), "vs_4_0_level_9_3");
  ID3DBlob* psb = compileHlsl(readFile(dir + "frag.hlsl"), "ps_4_0_level_9_3");
  if (!vsb || !psb) { rel(vsb); rel(psb); return false; }
  d.dev->CreateVertexShader(vsb->GetBufferPointer(), vsb->GetBufferSize(), nullptr, &d.vs);
  d.dev->CreatePixelShader(psb->GetBufferPointer(), psb->GetBufferSize(), nullptr, &d.ps);
  D3D11_INPUT_ELEMENT_DESC el[] = {
    {"POSITION", 0, DXGI_FORMAT_R32G32_FLOAT, 0, 0, D3D11_INPUT_PER_VERTEX_DATA, 0},
    {"TEXCOORD", 0, DXGI_FORMAT_R32G32_FLOAT, 0, 8, D3D11_INPUT_PER_VERTEX_DATA, 0},
    {"COLOR", 0, DXGI_FORMAT_R32G32B32A32_FLOAT, 0, 16, D3D11_INPUT_PER_VERTEX_DATA, 0}};
  d.dev->CreateInputLayout(el, 3, vsb->GetBufferPointer(), vsb->GetBufferSize(), &d.il);
  rel(vsb); rel(psb);
  if (!d.vs || !d.ps || !d.il) return false;
  D3D11_BLEND_DESC bd = {}; auto& rt = bd.RenderTarget[0];
  rt.BlendEnable = TRUE; rt.SrcBlend = D3D11_BLEND_SRC_ALPHA; rt.BlendOp = D3D11_BLEND_OP_ADD;
  rt.SrcBlendAlpha = D3D11_BLEND_ONE; rt.DestBlendAlpha = D3D11_BLEND_INV_SRC_ALPHA; rt.BlendOpAlpha = D3D11_BLEND_OP_ADD;
  rt.RenderTargetWriteMask = D3D11_COLOR_WRITE_ENABLE_ALL;
  rt.DestBlend = D3D11_BLEND_ONE; d.dev->CreateBlendState(&bd, &d.bAdd);
  rt.DestBlend = D3D11_BLEND_INV_SRC_ALPHA; d.dev->CreateBlendState(&bd, &d.bAlpha);
  D3D11_SAMPLER_DESC sm = {}; sm.Filter = D3D11_FILTER_MIN_MAG_MIP_LINEAR;
  sm.AddressU = sm.AddressV = sm.AddressW = D3D11_TEXTURE_ADDRESS_CLAMP; sm.MaxLOD = D3D11_FLOAT32_MAX; sm.ComparisonFunc = D3D11_COMPARISON_NEVER;
  d.dev->CreateSamplerState(&sm, &d.smp);
  D3D11_RASTERIZER_DESC rd = {}; rd.FillMode = D3D11_FILL_SOLID; rd.CullMode = D3D11_CULL_NONE; rd.DepthClipEnable = TRUE; rd.ScissorEnable = FALSE;
  d.dev->CreateRasterizerState(&rd, &d.rs);
  D3D11_DEPTH_STENCIL_DESC dsd = {}; dsd.DepthEnable = FALSE; dsd.StencilEnable = FALSE; d.dev->CreateDepthStencilState(&dsd, &d.ds);
  // same 64px soft glow disc fallback as GL
  const int S = 64; std::vector<unsigned char> px(S*S*4);
  for (int y=0;y<S;++y) for (int x=0;x<S;++x){ float dd=std::hypot(x-S/2+.5f,y-S/2+.5f)/(S/2); float a=dd<1?(1-dd)*(1-dd):0; unsigned char* p=&px[(y*S+x)*4]; p[0]=p[1]=p[2]=255; p[3]=(unsigned char)(a*255); }
  m_fallbackTex = makeTex(m_dx, px.data(), S, S);
  m_prog = 1; return m_fallbackTex != 0;
}
void Sprites::DeInit() {
  if (!m_dx) return; FreeLoaded(); DX& d = *m_dx;
  for (auto& s : d.tex) rel(s); d.tex.clear();
  rel(d.vb); rel(d.il); rel(d.vs); rel(d.ps); rel(d.bAdd); rel(d.bAlpha); rel(d.smp); rel(d.rs); rel(d.ds); rel(d.dev); rel(d.ctx);
  delete m_dx; m_dx = nullptr; m_fallbackTex = m_prog = 0;
}
unsigned Sprites::LoadTexturePNG(const std::string& path, int chroma, int* ow, int* oh) {
  int w = 0, h = 0, ch = 0;
  unsigned char* px = stbi_load(path.c_str(), &w, &h, &ch, 4);
  if (!px) { kodi::Log(ADDON_LOG_WARNING, "BezelViz: PNG load failed %s (%s), using soft disc", path.c_str(), stbi_failure_reason()); return m_fallbackTex; }
  ApplyChromaKey(px, w, h, ch, chroma);
  unsigned t = makeTex(m_dx, px, w, h); stbi_image_free(px);
  if (!t) return m_fallbackTex;
  m_loaded.push_back(t); if (ow) *ow = w; if (oh) *oh = h; return t;
}
void Sprites::FreeLoaded() { if (m_dx) for (auto t : m_loaded) if (t && t <= m_dx->tex.size()) rel(m_dx->tex[t-1]); m_loaded.clear(); }
float Sprites::ViewportAspect() const {
  if (!g_ctx) return 0.f; UINT n = 1; D3D11_VIEWPORT vp = {}; g_ctx->RSGetViewports(&n, &vp);
  return (n && vp.Height > 0) ? vp.Width / vp.Height : 0.f;
}
void Sprites::SetAdditive(bool a) { if (a != m_add) { Flush(m_add); m_add = a; } }
void Sprites::Begin(){ m_verts.clear(); m_curTex = 0; }
void Sprites::Push(const Quad& q, unsigned tex) {   // identical to GL backend
  if (m_curTex && (tex ? tex : m_fallbackTex) != m_curTex) Flush(m_add);
  m_curTex = tex ? tex : m_fallbackTex;
  float x0=q.pos.x-q.size.x, x1=q.pos.x+q.size.x, y0=q.pos.y-q.size.y, y1=q.pos.y+q.size.y;
  float v[6][4] = {{x0,y0,q.uv[0],q.uv[1]},{x1,y0,q.uv[2],q.uv[1]},{x1,y1,q.uv[2],q.uv[3]},{x0,y0,q.uv[0],q.uv[1]},{x1,y1,q.uv[2],q.uv[3]},{x0,y1,q.uv[0],q.uv[3]}};
  if (q.rot != 0.f) { float c = std::cos(q.rot), s = std::sin(q.rot), a = q.aspect > 0.f ? q.aspect : 1.f;
    for (auto& e : v) { float dx = (e[0]-q.pos.x)*a, dy = e[1]-q.pos.y; e[0] = q.pos.x + (dx*c - dy*s)/a; e[1] = q.pos.y + dx*s + dy*c; } }
  for (auto& e : v) { m_verts.insert(m_verts.end(), {e[0],e[1],e[2],e[3],q.col.r,q.col.g,q.col.b,q.col.a}); }
}
// NOTE UV: GL uploads PNG row 0 at v=0 and the engine's UVs were tuned for that; D3D also samples row 0 at v=0,
// so the same uv values map to the same texels. NDC y is +up in both APIs, so positions need no flip.
void Sprites::Flush(bool additive) {
  if (m_verts.empty() || !m_dx) return; DX& d = *m_dx;
  UINT bytes = (UINT)(m_verts.size() * sizeof(float));
  if (bytes > d.vbBytes) {
    rel(d.vb); UINT cap = bytes * 2; D3D11_BUFFER_DESC bd = {}; bd.ByteWidth = cap; bd.Usage = D3D11_USAGE_DYNAMIC;
    bd.BindFlags = D3D11_BIND_VERTEX_BUFFER; bd.CPUAccessFlags = D3D11_CPU_ACCESS_WRITE;
    if (FAILED(d.dev->CreateBuffer(&bd, nullptr, &d.vb))) { d.vbBytes = 0; m_verts.clear(); return; } d.vbBytes = cap;
  }
  D3D11_MAPPED_SUBRESOURCE m; if (FAILED(d.ctx->Map(d.vb, 0, D3D11_MAP_WRITE_DISCARD, 0, &m))) { m_verts.clear(); return; }
  memcpy(m.pData, m_verts.data(), bytes); d.ctx->Unmap(d.vb, 0);
  ID3D11ShaderResourceView* srv = (m_curTex && m_curTex <= d.tex.size()) ? d.tex[m_curTex-1] : nullptr;
  if (!srv && m_fallbackTex) srv = d.tex[m_fallbackTex-1];
  UINT stride = 8 * sizeof(float), off = 0; float bf[4] = {0,0,0,0};
  d.ctx->IASetInputLayout(d.il); d.ctx->IASetPrimitiveTopology(D3D11_PRIMITIVE_TOPOLOGY_TRIANGLELIST);
  d.ctx->IASetVertexBuffers(0, 1, &d.vb, &stride, &off);
  d.ctx->VSSetShader(d.vs, nullptr, 0); d.ctx->PSSetShader(d.ps, nullptr, 0);
  d.ctx->PSSetShaderResources(0, 1, &srv); d.ctx->PSSetSamplers(0, 1, &d.smp);
  d.ctx->RSSetState(d.rs); d.ctx->OMSetDepthStencilState(d.ds, 0);
  d.ctx->OMSetBlendState(additive ? d.bAdd : d.bAlpha, bf, 0xFFFFFFFF);
  d.ctx->Draw((UINT)(m_verts.size() / 8), 0);
  ID3D11ShaderResourceView* none = nullptr; d.ctx->PSSetShaderResources(0, 1, &none);
  m_verts.clear();
}
}
#endif // BEZEL_DX11
