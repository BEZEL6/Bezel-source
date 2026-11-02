// SPDX-License-Identifier: GPL-2.0-or-later  (Bezel viz) DX11 equivalent of GL/frag.glsl: texture * vertex colour.
Texture2D u_tex : register(t0); SamplerState u_smp : register(s0);
struct PS_IN { float4 pos : SV_POSITION; float2 uv : TEXCOORD0; float4 col : COLOR; };
float4 main(PS_IN i) : SV_TARGET { return u_tex.Sample(u_smp, i.uv) * i.col; }
