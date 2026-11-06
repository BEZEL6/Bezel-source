#version 100
attribute vec2 a_pos; attribute vec2 a_uv; attribute vec4 a_col;
varying vec2 v_uv; varying vec4 v_col;
void main(){ v_uv=a_uv; v_col=a_col; gl_Position=vec4(a_pos,0.0,1.0); }
