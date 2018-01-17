#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
--------------------
py2exe setup file
--------------------
Author: Jordan Cave
--------------------
"""

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

executables = [
    Executable('main.py', base=base)
]
additional_mods = ['numpy.core._methods', 'numpy.lib.format']
setup(name='main',
      version='0.1',
      description='idk',
      options=options,
      executables=executables
      )