#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------
Methods connected to GUI
------------------------
Author: Jordan Cave
------------------------
"""
import settings
import ded_gui as gui
import mp3d_widget as mp3d
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import sys
import math
from PyQt4 import QtCore, QtGui
import numpy as np
import slicer as slicer
import layer as layer
import pathing as pathing
from stl import mesh


# Ensure an stl file is actually loaded before continuing
stl_load_state = False

def update_mpl3d(figure):
    """ Test figure updater for mp3d_widget.py """
    
    pass

def open_stl(widget):
    """ Generic STL file opener """
    new_widget = QtGui.QWidget()
    new_widget.resize(320, 240)
    new_widget.setWindowTitle("Select an STL file to import")
    filename = QtGui.QFileDialog.getOpenFileName(new_widget, 'Open File', '/')
    if filename == '':
        pass
    else:
        global stl_mesh
        stl_mesh = mesh.Mesh.from_file(filename)
        stl_mesh.rotate([-0.5, 0.0, 0.0], math.radians(90))
        widget.update_figure(stl_mesh)
    global stl_load_state
    stl_load_state = True
        
def slice_stl(widget):
    """ Update the mp3d viewer with slices """
    global stl_mesh
    global slice_data
    slice_data = slicer.slice_stl(stl_mesh)
    widget.update_slices(slice_data)

def read_bw_line(widget):
    """ Read in string or values from lineEdit widgets"""
    text = widget.text()
    settings.pp_bead_width = float(text)

def read_bh_line(widget):
    """ Read in string or values from lineEdit widgets"""
    text = widget.text()
    settings.pp_bead_height = float(text)
    
def read_path_num(widget):
    """ Read layer path number to display """
    global layer_num
    layer_num = widget.value()    

def clean_slice(dirty_slice):
    """ Helper function for calc_paths() to take slice polygon from lines to points"""
    dirty_slice = np.reshape(dirty_slice, (-1,1,3)).reshape(-1,3)
    dirty_slice = pathing.join_segments(dirty_slice)
    slice_poly = pathing.polar_order(dirty_slice)
    return slice_poly

def calc_paths(slice_coords):
    """ Calculate all toolpaths """
    global toolpaths
    global layers
    layers = []
    for slice_layer in slice_data:
        # NN_order/Polar for now
        layer_polygon = clean_slice(slice_layer)
        layer_obj = layer.Layer(layer_polygon[:,0:2], 'Transverse', 45)
        layers.append(layer_obj)

def plot_layer_path(widget, layer):
    widget.update_figure(layer)

def main():
    
    app = gui.QtGui.QApplication(sys.argv)
    MainWindow = gui.QtGui.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    # Open STL
    ui.pushButton.clicked.connect(lambda: open_stl(ui.graphicsView))
    
    # Read in parameters/slice STL/Calculate toolpaths
    ui.pushButton_2.clicked.connect(lambda: read_bw_line(ui.lineEdit_5))
    ui.pushButton_2.clicked.connect(lambda: read_bh_line(ui.lineEdit_6))
    ui.pushButton_2.clicked.connect(lambda: slice_stl(ui.graphicsView_3))
    ui.pushButton_2.clicked.connect(lambda: calc_paths(slice_data))

    # Display path for individual layers
    ui.pushButton_5.clicked.connect(lambda: read_path_num(ui.spinBox))
    ui.pushButton_5.clicked.connect(lambda: plot_layer_path(ui.matplotlibwidget, layers[layer_num]))

    sys.exit(app.exec_())
    
if __name__ == "__main__":
    print(__doc__)
    print(update_mpl3d.__doc__)
    main()