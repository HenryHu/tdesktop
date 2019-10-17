# This file is part of Telegram Desktop,
# the official desktop application for the Telegram messaging service.
#
# For license and copyright information please follow this link:
# https://github.com/telegramdesktop/tdesktop/blob/master/LEGAL

{
  'variables': {
    'variables': {
      'variables': {
        'variables': {
          'variables': {
            'conditions': [
              [ 'build_macold', {
                'qt_version%': '5.3.2',
              }, {
                'qt_version%': '%%QT_VERSION%%',
              }]
            ],
          },
          'qt_libs': [
            'Qt5Network',
            'Qt5Widgets',
            'Qt5Gui',
          ],
          'qt_version%': '<(qt_version)',
          'conditions': [
            [ 'build_macold', {
              'linux_path_qt%': '/usr/local/macold/Qt-<(qt_version)',
            }, {
              'linux_path_qt%': '%%LOCALBASE%%/lib/qt',
            }]
          ]
        },
        'qt_version%': '<(qt_version)',
        'qt_loc_unix': '<(linux_path_qt)',
        'conditions': [
          [ 'build_win', {
            'qt_lib_prefix': '<(ld_lib_prefix)',
            'qt_lib_debug_postfix': 'd<(ld_lib_postfix)',
            'qt_lib_release_postfix': '<(ld_lib_postfix)',
            'qt_libs': [
              '<@(qt_libs)',
              'Qt5Core',
              'qtmain',
              'qwindows',
              'qtfreetype',
              'qtpcre',
            ],
          }],
          [ 'build_mac', {
            'qt_lib_prefix': '<(ld_lib_prefix)',
            'qt_lib_debug_postfix': '_debug<(ld_lib_postfix)',
            'qt_lib_release_postfix': '<(ld_lib_postfix)',
            'qt_libs': [
              '<@(qt_libs)',
              'Qt5Core',
              'qgenericbearer',
              'qcocoa',
            ],
          }],
          [ 'build_mac and not build_macold', {
            'qt_libs': [
              '<@(qt_libs)',
              'Qt5Core',
              'qtfreetype',
              'qtpcre',
            ],
          }],
          [ 'build_linux', {
            'qt_lib_prefix': '',
            'qt_lib_debug_postfix': '',
            'qt_lib_release_postfix': '',
            'qt_libs': [
              '<@(qt_libs)',
              'Qt5DBus',
              'Qt5Core',
            ],
          }],
        ],
      },
      'qt_version%': '<(qt_version)',
      'qt_loc_unix': '<(qt_loc_unix)',
      'qt_version_loc': '<!(%%PYTHON_CMD%% -c "print(\'<(qt_version)\'.replace(\'.\', \'_\'))")',
      'qt_libs_debug': [
        '<!@(%%PYTHON_CMD%% -c "for s in \'<@(qt_libs)\'.split(\' \'): print(\'<(qt_lib_prefix)\' + s + \'<(qt_lib_debug_postfix)\')")',
      ],
      'qt_libs_release': [
        '<!@(%%PYTHON_CMD%% -c "for s in \'<@(qt_libs)\'.split(\' \'): print(\'<(qt_lib_prefix)\' + s + \'<(qt_lib_release_postfix)\')")',
      ],
    },
    'qt_libs_debug': [ '<@(qt_libs_debug)' ],
    'qt_libs_release': [ '<@(qt_libs_release)' ],
    'qt_version%': '<(qt_version)',
    'conditions': [
      [ 'build_win', {
        'qt_loc': '<(DEPTH)/../../../Libraries/qt<(qt_version_loc)/qtbase',
      }, {
        'qt_loc': '<(qt_loc_unix)',
      }],
    ],

    # If you need moc sources include a line in your 'sources':
    # '<!@(python <(DEPTH)/list_sources.py [sources] <(qt_moc_list_sources_arg))'
    # where [sources] contains all your source files
    'qt_moc_list_sources_arg': '--moc-prefix SHARED_INTERMEDIATE_DIR/<(_target_name)/moc/moc_',
  },

  'configurations': {
    'Debug': {
      'conditions' : [
        [ 'build_win', {
          'msvs_settings': {
            'VCLinkerTool': {
              'AdditionalDependencies': [
                '<@(qt_libs_debug)',
              ],
            },
          },
        }],
        [ 'build_mac', {
          'xcode_settings': {
            'OTHER_LDFLAGS': [
              '<@(qt_libs_debug)',
              '/usr/local/lib/libz.a',
            ],
          },
        }],
      ],
    },
    'Release': {
      'conditions' : [
        [ 'build_win', {
          'msvs_settings': {
            'VCLinkerTool': {
              'AdditionalDependencies': [
                '<@(qt_libs_release)',
              ],
            },
          },
        }],
        [ 'build_mac', {
          'xcode_settings': {
            'OTHER_LDFLAGS': [
              '<@(qt_libs_release)',
              '/usr/local/lib/libz.a',
            ],
          },
        }],
      ],
    },
  },

  'include_dirs': [
    '%%QT_INCDIR%%',
    '%%QT_INCDIR%%/QtCore',
    '%%QT_INCDIR%%/QtGui',
    '%%QT_INCDIR%%/QtDBus',
    '%%QT_INCDIR%%/QtCore/<(qt_version)',
    '%%QT_INCDIR%%/QtGui/<(qt_version)',
    '%%QT_INCDIR%%/QtCore/<(qt_version)/QtCore',
    '%%QT_INCDIR%%/QtGui/<(qt_version)/QtGui',
  ],
  'library_dirs': [
    '%%LOCALBASE%%/lib',
    '%%QT_LIBDIR%%/',
    '<(qt_loc)/plugins/bearer',
    '<(qt_loc)/plugins/platforms',
    '<(qt_loc)/plugins/imageformats',
  ],
  'defines': [
    'QT_WIDGETS_LIB',
    'QT_NETWORK_LIB',
    'QT_GUI_LIB',
    'QT_CORE_LIB',
  ],
  'conditions': [
    [ 'build_linux', {
      'library_dirs': [
        '<(qt_loc)/plugins/platforminputcontexts',
      ],
      'libraries': [
        '<@(qt_libs_release)',
        '-lcrypto',
        '-lX11',
        '-lglib-2.0',
        '-lpthread',
      ],
      'include_dirs': [
        '%%QMAKESPEC%%',
      ],
      'ldflags': [
        '-pthread',
        '-rdynamic',
      ],
    }],
    [ 'build_mac', {
      'xcode_settings': {
        'OTHER_LDFLAGS': [
          '-lcups',
        ],
      },
    }],
  ],
}
