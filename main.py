#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-----------------------------------------
Main call for DED Process Planning Module
-----------------------------------------
Author: Jordan Cave
-----------------------------------------
"""

import settings
import gui_methods

#for cxfreeze
import numpy.core._methods
import numpy.lib.format 
from matplotlib import docstring
from matplotlib import legend_handler

if __name__ == '__main__':
    settings.init()
    gui_methods.main()

