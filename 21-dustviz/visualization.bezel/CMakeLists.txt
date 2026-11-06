cmake_minimum_required(VERSION 3.18)
project(visualization.bezel)

# Spectrum-derived build (GL/GLES). Engine-only addon; style packs live in the Bezel skin.
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${PROJECT_SOURCE_DIR})
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Kodi REQUIRED)

# Windows (Kodi is DX11-only there): select the DirectX 11 sprite backend, as visualization.spectrum does.
if(WIN32 OR APP_RENDER_SYSTEM STREQUAL "dx11")
  set(APP_RENDER_SYSTEM dx11)
endif()

if(APP_RENDER_SYSTEM STREQUAL "dx11")
  add_definitions(-DBEZEL_DX11 -D_WIN32PC -D_USRDLL -DNOMINMAX -D_USE_MATH_DEFINES)
  set(DEPLIBS d3d11 d3dcompiler dxguid)
  set(INCLUDES)
elseif(APP_RENDER_SYSTEM STREQUAL "gl" OR NOT APP_RENDER_SYSTEM)
  find_package(glm REQUIRED)
  find_package(OpenGl REQUIRED)
  set(DEPLIBS ${OPENGL_LIBRARIES})
  set(INCLUDES ${OPENGL_INCLUDE_DIR})
  add_definitions(${OPENGL_DEFINITIONS})
elseif(APP_RENDER_SYSTEM STREQUAL "gles")
  find_package(glm REQUIRED)
  find_package(OpenGLES REQUIRED)
  set(DEPLIBS ${OPENGLES_LIBRARIES})
  set(INCLUDES ${OPENGLES_INCLUDE_DIR})
  add_definitions(${OPENGLES_DEFINITIONS})
endif()

set(BEZEL_SOURCES
  src/BezelViz.cpp
  src/Engine.cpp
  src/SmearStyles.cpp
  src/AudioEnvelopes.cpp
  src/Particles.cpp
  src/Forces.cpp
  src/Sprites.cpp
  src/SpritesDX11.cpp
  src/Atlas.cpp
  src/PackLoader.cpp
  src/MiniJson.cpp
  src/Tuner.cpp
  src/DebugOverlay.cpp
  src/InVizTuner.cpp)

set(BEZEL_HEADERS
  src/BezelViz.h
  src/Engine.h
  src/AudioEnvelopes.h
  src/Particles.h
  src/Forces.h
  src/Sprites.h
  src/ChromaKey.h
  src/Atlas.h
  src/PackLoader.h
  src/MiniJson.h
  src/Tuner.h
  src/DebugOverlay.h
  src/Types.h)

message(STATUS "Configured render system: ${APP_RENDER_SYSTEM}")

include_directories(${INCLUDES}
                    ${GLM_INCLUDE_DIR}
                    ${KODI_INCLUDE_DIR}/..)

build_addon(visualization.bezel BEZEL DEPLIBS)

include(CPack)
