// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz) DX11 equivalent of GL/vert.glsl: pass-through, NDC in.
struct VS_IN  { float2 pos : POSITION; float2 uv : TEXCOORD0; float4 col : COLOR; };
struct VS_OUT { float4 pos : SV_POSITION; float2 uv : TEXCOORD0; float4 col : COLOR; };
VS_OUT main(VS_IN i) { VS_OUT o; o.pos = float4(i.pos, 0.0, 1.0); o.uv = i.uv; o.col = i.col; return o; }
