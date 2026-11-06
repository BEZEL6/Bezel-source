// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz engine)
#include "Sprites.h"
#ifndef BEZEL_DX11   // GL/GLES backend; DX11 lives in SpritesDX11.cpp
#include <kodi/gui/gl/GL.h>
#include <algorithm>
#include <cmath>
#include <fstream>
#include <sstream>
#include <vector>
#include <kodi/General.h>
#include "ChromaKey.h"
#define STB_IMAGE_IMPLEMENTATION
#define STBI_ONLY_PNG
#include "third_party/stb_image.h"
namespace bezel {
static std::string readFile(const std::string& p){ std::ifstream f(p); std::stringstream s; s << f.rdbuf(); return s.str(); }
static GLuint compile(GLenum t, const std::string& src){ GLuint s = glCreateShader(t); const char* c = src.c_str(); glShaderSource(s,1,&c,nullptr); glCompileShader(s); return s; }
bool Sprites::Init(const std::string& dir) {
  GLuint vs = compile(GL_VERTEX_SHADER, readFile(dir + "vert.glsl")), fs = compile(GL_FRAGMENT_SHADER, readFile(dir + "frag.glsl"));
  m_prog = glCreateProgram(); glAttachShader(m_prog, vs); glAttachShader(m_prog, fs); glLinkProgram(m_prog);
  glDeleteShader(vs); glDeleteShader(fs);
  GLint ok = 0; glGetProgramiv(m_prog, GL_LINK_STATUS, &ok); if (!ok) return false;
  m_aPos = glGetAttribLocation(m_prog,"a_pos"); m_aUv = glGetAttribLocation(m_prog,"a_uv"); m_aCol = glGetAttribLocation(m_prog,"a_col");
  glGenBuffers(1, &m_vbo);
  // generated 64px soft glow disc fallback (so something visible draws without pack PNGs)
  const int S = 64; std::vector<unsigned char> px(S*S*4);
  for (int y=0;y<S;++y) for (int x=0;x<S;++x){ float d=std::hypot(x-S/2+.5f,y-S/2+.5f)/(S/2); float a=d<1?(1-d)*(1-d):0; unsigned char* p=&px[(y*S+x)*4]; p[0]=p[1]=p[2]=255; p[3]=(unsigned char)(a*255); }
  glGenTextures(1,&m_fallbackTex); glBindTexture(GL_TEXTURE_2D,m_fallbackTex);
  glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR); glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
  glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,S,S,0,GL_RGBA,GL_UNSIGNED_BYTE,px.data());
  return true;
}
void Sprites::DeInit(){ FreeLoaded(); if (m_vbo) glDeleteBuffers(1,&m_vbo); if (m_fallbackTex) glDeleteTextures(1,&m_fallbackTex); if (m_prog) glDeleteProgram(m_prog); m_vbo=m_fallbackTex=m_prog=0; }
unsigned Sprites::LoadTexturePNG(const std::string& path, int chroma, int* ow, int* oh) {
  int w = 0, h = 0, ch = 0;
  unsigned char* px = stbi_load(path.c_str(), &w, &h, &ch, 4);
  if (!px) { kodi::Log(ADDON_LOG_WARNING, "BezelViz: PNG load failed %s (%s), using soft disc", path.c_str(), stbi_failure_reason()); return m_fallbackTex; }
  ApplyChromaKey(px, w, h, ch, chroma);
  GLuint t = 0; glGenTextures(1, &t); glBindTexture(GL_TEXTURE_2D, t);
  glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR); glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
  glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_EDGE); glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_EDGE);
  glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,w,h,0,GL_RGBA,GL_UNSIGNED_BYTE,px);
  stbi_image_free(px); m_loaded.push_back(t); if (ow) *ow = w; if (oh) *oh = h; return t;
}
void Sprites::FreeLoaded() { for (auto t : m_loaded) { GLuint g = t; glDeleteTextures(1, &g); } m_loaded.clear(); }
float Sprites::ViewportAspect() const { GLint vp[4] = {0,0,0,0}; glGetIntegerv(GL_VIEWPORT, vp); return vp[3] > 0 ? (float)vp[2] / vp[3] : 0.f; }
void Sprites::SetDevice(void*) {}
void Sprites::SetAdditive(bool a) { if (a != m_add) { Flush(m_add); m_add = a; } }
void Sprites::Begin(){ m_verts.clear(); m_curTex = 0; }
void Sprites::Push(const Quad& q, unsigned tex) {
  if (m_curTex && (tex ? tex : m_fallbackTex) != m_curTex) Flush(m_add);   // batch break on texture change (atlas makes this rare)
  m_curTex = tex ? tex : m_fallbackTex;
  float x0=q.pos.x-q.size.x, x1=q.pos.x+q.size.x, y0=q.pos.y-q.size.y, y1=q.pos.y+q.size.y;
  float v[6][4] = {{x0,y0,q.uv[0],q.uv[1]},{x1,y0,q.uv[2],q.uv[1]},{x1,y1,q.uv[2],q.uv[3]},{x0,y0,q.uv[0],q.uv[1]},{x1,y1,q.uv[2],q.uv[3]},{x0,y1,q.uv[0],q.uv[3]}};
  if (q.rot != 0.f) { float c = std::cos(q.rot), s = std::sin(q.rot), a = q.aspect > 0.f ? q.aspect : 1.f;
    for (auto& e : v) { float dx = (e[0]-q.pos.x)*a, dy = e[1]-q.pos.y; e[0] = q.pos.x + (dx*c - dy*s)/a; e[1] = q.pos.y + dx*s + dy*c; } }
  for (auto& e : v) { m_verts.insert(m_verts.end(), {e[0],e[1],e[2],e[3],q.col.r,q.col.g,q.col.b,q.col.a}); }
}
void Sprites::Flush(bool additive) {
  if (m_verts.empty()) return;
  glUseProgram(m_prog); glEnable(GL_BLEND); glBlendFunc(GL_SRC_ALPHA, additive ? GL_ONE : GL_ONE_MINUS_SRC_ALPHA);
  glActiveTexture(GL_TEXTURE0); glBindTexture(GL_TEXTURE_2D, m_curTex);
  glBindBuffer(GL_ARRAY_BUFFER, m_vbo); glBufferData(GL_ARRAY_BUFFER, m_verts.size()*sizeof(float), m_verts.data(), GL_STREAM_DRAW);
  const GLsizei st = 8*sizeof(float);
  glVertexAttribPointer(m_aPos,2,GL_FLOAT,GL_FALSE,st,(void*)0); glEnableVertexAttribArray(m_aPos);
  glVertexAttribPointer(m_aUv,2,GL_FLOAT,GL_FALSE,st,(void*)(2*sizeof(float))); glEnableVertexAttribArray(m_aUv);
  glVertexAttribPointer(m_aCol,4,GL_FLOAT,GL_FALSE,st,(void*)(4*sizeof(float))); glEnableVertexAttribArray(m_aCol);
  glDrawArrays(GL_TRIANGLES, 0, (GLsizei)(m_verts.size()/8));
  glDisableVertexAttribArray(m_aPos); glDisableVertexAttribArray(m_aUv); glDisableVertexAttribArray(m_aCol);
  glBindBuffer(GL_ARRAY_BUFFER,0); glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA); glUseProgram(0);
  m_verts.clear();
}
}
#endif // !BEZEL_DX11
