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
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d

import matplotlib.pyplot as plt

class QtMplCanvas(FigureCanvas):
    """ Base Mpl Canvas """
    def __init__(self, parent=None, width = 6.5, height = 5.5, dpi = 100, sharex = None, sharey = None, fig = None):
        if fig == None:
            self.fig = Figure(figsize = (width, height), dpi=dpi, facecolor = '#FFFFFF')
            self.axes = self.fig.add_subplot(111, projection='3d')
            self.fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9)
            self.axes.hold(True)
        else:
            self.fig = fig

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
    def sizeHint(self):
        w, h = self.get_width_height()
        return QtCore.QSize(w, h)

    def minimumSizeHint(self):
        return QtCore.QSize(10, 10)

    def sizeHint(self):
        w, h = self.get_width_height()
        return QtCore.QSize(w, h)

    def minimumSizeHint(self):
        return QtCore.QSize(10, 10)
    

class QtMplDynCanvas(QtMplCanvas):
    """ Hopefully a dynamic canvas that can be updated """
    
    def __init__(self, *args, **kwargs):
        QtMplCanvas.__init__(self, *args, **kwargs)
    
    def initial_figure(self):
        self.axes.plot([0,1,2,3], [0,1,2,3])
    
    def update_figure(self, mesh):
        """ Update canvas figure for stl file loader """
        self.axes.cla()
        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(mesh.vectors))
        self.scale = mesh.points.flatten('C')
        self.axes.auto_scale_xyz(self.scale, self.scale, self.scale)
        self.draw()
    
    def update_slices(self, slice_data):
        """ Updata slice canvas with all the slice data... """
        self.axes.cla()
        for i in range(len(slice_data)):
            intersects = slice_data[i]
            self.axes.add_collection3d(mplot3d.art3d.Line3DCollection(intersects, color = 'green'))
        self.axes.auto_scale_xyz(intersects, intersects, intersects)        
        self.draw()
        pass
    
    @staticmethod
    def _plt_3d_slices(slice_dict):
        """ Rehash of function in slicer.py for adding to canvas """
        for key in slice_dict:
            intersects = slice_dict[key]
            idx = 0
            while idx < len(intersects):
                if intersects[idx].shape[0] == 1:
                    x_vec, y_vec, z_vec = intersects[idx][0][0], intersects[idx][0][1], intersects[idx][0][2]
                    axes.add_collection3d(x_vec, y_vec, z_vec, color = 'green', s = 1)
                if intersects[idx].shape[0] == 2:
                    x_vec, y_vec, z_vec = [], [], []
                    x_points, y_points, z_points = intersects[idx][:,0], intersects[idx][:,1], intersects[idx][:,2]  
                    x_vec, y_vec, z_vec = np.hstack((x_vec, x_points)), np.hstack((y_vec,y_points)), np.hstack((z_vec, z_points))
                    axes.add_collection3d(x_vec, y_vec, z_vec ,color = 'green')
                if intersects[idx].shape[0] == 3:
                    x_vec, y_vec, z_vec = [], [], []
                    x_points, y_points, z_points = intersects[idx][:,0], intersects[idx][:,1], intersects[idx][:,2] 
                    x_vec, y_vec, z_vec = np.hstack((x_vec, x_points)), np.hstack((y_vec,y_points)), np.hstack((z_vec, z_points))
                    axes.add_collection3d(x_vec, y_vec, z_vec, color = 'blue')
                idx+=1                
    
    
class MyNavigationToolbar(NavigationToolbar) :
    def __init__(self, parent, canvas, direction = 'h' ) :

        self.canvas = canvas
        QWidget.__init__( self, parent )

        if direction=='h' :
            self.layout = QHBoxLayout( self )
        else :
            self.layout = QVBoxLayout( self )

        self.layout.setMargin( 2 )
        self.layout.setSpacing( 0 )

        NavigationToolbar2.__init__( self, canvas )


    def set_message( self, s ):
        pass


class MPL_WIDGET_3D(QtGui.QWidget):
    def __init__(self, parent = None, enableAutoScale = False, enableCSV = False, enableEdit = False, fig = None):
        QtGui.QWidget.__init__(self, parent)
        self.canvas = QtMplDynCanvas(fig)
        self.canvas.axes.mouse_init()
        self.toolbar = NavigationToolbar(self.canvas, self.canvas)
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.canvas)
        self.vbox.addWidget(self.toolbar)
        self.setLayout(self.vbox)


        ###########SAVING FIGURE TO CLIPBOARD##########
        self.cb = None #will be used for the clipboard
        self.tempPath = getHomeDir()
        self.tempPath = os.path.join(self.tempPath,'tempMPL.png')

        self.mpl2ClipAction = QtGui.QAction("Save to Clipboard",  self)
        self.mpl2ClipAction.setShortcut("Ctrl+C")
        self.addAction(self.mpl2ClipAction)
        QtCore.QObject.connect(self.mpl2ClipAction,QtCore.SIGNAL("triggered()"), self.mpl2Clip)

    def mpl2Clip(self):
        try:
            self.canvas.fig.savefig(self.tempPath)
            tempImg = QtGui.QImage(self.tempPath)
            self.cb = QtGui.QApplication.clipboard()
            self.cb.setImage(tempImg)
        except:
            print('Error copying figure to clipboard')
            errorMsg = "Sorry: %s\n\n:%s\n"%(sys.exc_type, sys.exc_value)
            print(errorMsg)

####USED TO GET THE USERS HOME DIRECTORY FOR USE OF A TEMP FILE

def valid(path):
    if path and os.path.isdir(path):
        return True
    return False

def env(name):
    return os.environ.get( name, '' )

def getHomeDir():
    if sys.platform != 'win32':
        return os.path.expanduser( '~' )

    homeDir = env( 'USERPROFILE' )
    if not valid(homeDir):
        homeDir = env( 'HOME' )
        if not valid(homeDir) :
            homeDir = '%s%s' % (env('HOMEDRIVE'),env('HOMEPATH'))
            if not valid(homeDir) :
                homeDir = env( 'SYSTEMDRIVE' )
                if homeDir and (not homeDir.endswith('\\')) :
                    homeDir += '\\'
                if not valid(homeDir) :
                    homeDir = 'C:\\'
    return homeDir


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mplQt = MPL_WIDGET_3D()
    mplQt.show()
    sys.exit(app.exec_())