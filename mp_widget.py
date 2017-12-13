#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
--------------------
Mplot3d widget class
--------------------
Author: Jordan Cave
--------------------
"""

import os
import sys

from PyQt4 import QtCore,  QtGui

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle

import numpy as np

class MyMplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        mplstyle.use('ggplot')
        self.axes.plot()

    def update_figure(self, layer_obj):
        self.axes.cla()
        mplstyle.use('ggplot')
        plot_polygon = layer_obj.polygon
        plot_polygon = np.append(plot_polygon, plot_polygon[0])
        plot_polygon = plot_polygon.reshape(-1,2)
        x_poly, y_poly = plot_polygon[:,0], plot_polygon[:,1]
        self.axes.plot(x_poly, y_poly, color = 'green')
        for line in layer_obj.infill:
            x_vec = [line[0][0], line[1][0]]
            y_vec = [line[0][1], line[1][1]]
            self.axes.plot(x_vec, y_vec, color = 'xkcd:pastel purple')
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mplQt = MPL_WIDGET_3D()
    mplQt.show()
    sys.exit(app.exec_())