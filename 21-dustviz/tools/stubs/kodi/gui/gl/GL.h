#pragma once
#ifdef BEZEL_SMOKE_GLES
#include <GLES2/gl2.h>
#else
#define GL_GLEXT_PROTOTYPES
#include <GL/gl.h>
#include <GL/glext.h>
#endif
