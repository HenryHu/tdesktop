# This file is part of Telegram Desktop,
# the official desktop application for the Telegram messaging service.
#
# For license and copyright information please follow this link:
# https://github.com/telegramdesktop/tdesktop/blob/master/LEGAL

{
  'conditions': [[ 'build_linux', {
    'variables': {
      'not_need_gtk%': '<!(%%PYTHON_CMD%% -c "print(\'TDESKTOP_DISABLE_GTK_INTEGRATION\' in \'<(build_defines)\')")',
      'pkgconfig_libs': [
# In order to work libxkbcommon must be linked statically,
# PKGCONFIG links it like "-L/usr/local/lib -lxkbcommon"
# which makes a dynamic link which leads to segfault in
# QApplication() -> createPlatformIntegration -> QXcbIntegrationPlugin::create
        #'xkbcommon',
      ],
      'linux_path_ffmpeg%': '/usr/local',
      'linux_path_openal%': '/usr/local',
      'linux_path_va%': '/usr/local',
      'linux_path_vdpau%': '/usr/local',
      'linux_path_breakpad%': '/usr/local',
      'linux_path_opus_include%': '%%LOCALBASE%%/include/opus',
      'linux_path_range%': '/usr/local',
    },
    'include_dirs': [
      '/usr/include/openssl-1.0',
      '/usr/local/include',
      '<(linux_path_ffmpeg)/include',
      '<(linux_path_openal)/include',
      '<(linux_path_breakpad)/include/breakpad',
      '<(linux_path_opus_include)',
      '<(linux_path_range)/include',
    ],
    'library_dirs': [
      '/usr/lib/openssl-1.0',
      '/usr/local/lib',
      '<(linux_path_ffmpeg)/lib',
      '<(linux_path_openal)/lib',
      '<(linux_path_va)/lib',
      '<(linux_path_vdpau)/lib',
      '<(linux_path_breakpad)/lib',
    ],
    'libraries': [
      'openal',
      'avformat',
      'avcodec',
      'swresample',
      'swscale',
      'avutil',
      'minizip',
      'opus',
      'z',
#      '<!(pkg-config 2> /dev/null --libs <@(pkgconfig_libs))',
    ],
    'cflags_cc': [
      '-Wno-strict-overflow',
    ],
    'ldflags': [
      '-Wl,-wrap,aligned_alloc',
      '-Wl,-wrap,secure_getenv',
      '-Wl,--no-as-needed,-lrt',
    ],
    'configurations': {
      'Release': {
        'cflags_c': [
          '-Ofast',
          '-fno-strict-aliasing',
        ],
        'cflags_cc': [
          '-Ofast',
          '-fno-strict-aliasing',
        ],
        'ldflags': [
          '-Ofast',
        ],
      },
    },
    'conditions': [
      [ '"<!(uname -m)" == "x86_64"', {
        # 32 bit version can't be linked with debug info or LTO,
        # virtual memory exhausted :(
        'cflags_c': [ '-g' ],
        'cflags_cc': [ '-g' ],
        'ldflags': [ '-g' ],
        'configurations': {
          'Release': {
            'cflags_c': [ %%CFLAGS%% ],
            'cflags_cc': [ %%CXXFLAGS%% ],
            'ldflags': [ %%LDFLAGS%% ],
          },
        },
      }, {
        'ldflags': [
          '-Wl,-wrap,__divmoddi4',
        ],
      }], ['not_need_gtk!="True"', {
        'cflags_cc': [
          '<!(pkg-config 2> /dev/null --cflags gtk+-3.0)',
        ],
      }]
    ],
    'cmake_precompiled_header': '<(src_loc)/stdafx.h',
    'cmake_precompiled_header_script': 'PrecompiledHeader.cmake',
  }]],
}
