#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------------------
Layer cleanup and outer contour
-------------------------------
Author: Jordan Cave
-------------------------------

"""

import numpy as np
import pickle
import math
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.transforms import Bbox
import matplotlib.patches as patches
from scipy import spatial
import scipy
import pyclipper
from slicer import plot_slice

BEAD_SIZE = 1.00
    
def segment(slice_data, hatch_spacing):
    
    # Check that only 2-point line segments are in slice
    if not test_slice(slice_data):
        raise TypeError("Slice contains non 2-point segments")
        
    # Main loop for all line segments in slice
    # We'll be using the Y-axis for spacing criteria (Hmmmm...)
    idx = 0
    for segment in slice_data:
        # Calculate each segments Y-height
        seg_height = abs(segment[0,2] - segment[1,2])
        
        # Subdivide each segment
        # For now, using disgusting "resolution" parameter
        seg_res = 0.05
        # Hmmmm or just usin arange(1000 points or something)
        if seg_height > seg_res:
            seg_seg = np.arange(segment[0,2])
        else:
            something = True        
        idx += 1
        
''' Test Function '''
def test_slice(slice_points):
    locs = []
    idx = 0
    for segment in slice_points:
        if segment.shape[0] != 2:
            locs.append(idx)
        idx+=1
    if not locs:
        return True
    else:
        return False
 
def join_segments(slice_points):
    idx = 0
    to_del = []
    for idx in range(len(slice_points)):
        # Points in X that are redundant
        test_x = np.where(np.isclose(slice_points[idx][0], slice_points[:,0], atol = 1e-5) == True)
        # Points in Y that are redundant
        test_y = np.where(np.isclose(slice_points[idx][1], slice_points[:,1], atol = 1e-5) == True)
        # Common list
        test = np.intersect1d(test_x,test_y)
        # Delete all but the FIRST entry
        new = np.delete(slice_points, test[-(len(test)-1)])
        to_del.append(test[-(len(test)-1)])
        idx+=1
    to_del = np.unique(to_del)
    joined = np.delete(slice_points,to_del, axis = 0)
    return joined
        
def e_dist(segment):
    dist = math.sqrt(segment[0]**2 + segment[1]**2)
    return dist

def NN_order(points):    
    x_y = points[:,0:2]
    z = points[:,2]
    # Initial setup for 1st point
    my_tree = scipy.spatial.cKDTree(x_y, leafsize=100)
    init_to_del = np.asarray([0,0])
    ordered_points = np.vstack((init_to_del,x_y[0]))
    x_y = np.delete(x_y, 0 , axis = 0)
    # Now loop for the rest of the points
    idx = 1    
    while len(x_y) > 0:
        my_tree = scipy.spatial.cKDTree(x_y, leafsize=100)
        nn = my_tree.query(ordered_points[idx], k=1, distance_upper_bound=25)
        nn, nn_d = nn[1], nn[0]
        ordered_points = np.vstack((ordered_points, x_y[nn]))
        x_y = np.delete(x_y, nn, axis = 0)       
        idx+=1
    # Remember to delete the initial [0,0]
    ordered_points = np.delete(ordered_points, 0 ,axis = 0)
    ordered_points = np.hstack((ordered_points, z[:, None]))
    return ordered_points

def convex_hull(points):
    hull = spatial.ConvexHull(points[:,0:2])
    plt.plot(points[:,0], points[:,1], 'o')
    for simplex in hull.simplices:
        plt.grid()
        plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
    return hull.points

def polar_order(points):
    cent =(sum([p[0] for p in points])/len(points), sum([p[1] for p in points])/len(points))
    points = sorted(points, key = lambda p: math.atan2(p[1]-cent[1],p[0]-cent[0]))
    points = np.asarray(points)
    points = points[:,0:2]
    return points

def create_path(points):
    verts = np.vstack((points,points[0]))
    x_vec, y_vec = verts[:,0].tolist(), verts[:,1].tolist()
    verts = list(zip(x_vec, y_vec))
    codes = [Path.MOVETO]
    idx = 1
    while idx < len(points):
        codes.append(Path.LINETO)
        idx+=1
    codes.append(Path.CLOSEPOLY)  
    path = Path(verts,codes)
    fig = plt.figure()    
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(path, facecolor='orange', lw=2)
    ax.add_patch(patch)
    ax.autoscale()
    plt.show()
    return path

def create_dumb_path(points):
    verts = np.vstack((points,points[0]))
    x_vec, y_vec = verts[:,0].tolist(), verts[:,1].tolist()
    verts = list(zip(x_vec, y_vec))
    path = Path(verts)
    fig = plt.figure()    
    ax = fig.add_subplot(111)
    patch = patches.PathPatch(path, facecolor='orange', lw=2)
    ax.add_patch(patch)
    ax.autoscale()
    plt.show()
    return path

def create_polys(points):
    x_vec = points[:,0]
    y_vec = points[:,1]
    points_list = np.column_stack((x_vec,y_vec))
    points_list = (tuple(map(tuple,points_list)),)
    
    points_list = pyclipper.scale_to_clipper(points_list)
    [[[int(i) for i in j] for j in k] for k in points_list] 
    
    simple_poly = pyclipper.SimplifyPolygon(points_list[0])
    
    simple_poly = pyclipper.scale_from_clipper(simple_poly)
    #simple_poly = np.asarray(simple_poly)
    return simple_poly


def main():
    
    # Raster angle for pathing
    RASTER_ANGLE = 45 # Degrees
    HATCH_SPACING = 0.25
    
    # Load data from DED_MOD_X.py    
    slice_dict = pickle.load(open('slice_data.pkl', 'rb'))    
    sample_slice = slice_dict[12]
    
    # Plot original slice
    plot_slice(sample_slice) 
    
    # Reshape into just vertices
    sample_slice = np.reshape(sample_slice,(-1,1,3)).reshape(-1,3)
    
    # Delete redundant points
    poly_points = join_segments(sample_slice)
    print("POLYS: ", "\n", poly_points)
    
    
    ###################################################################
    ### New Clipper Stuff
    ###################################################################
    # Need to A) Scale points for clipper
    #         B) Format both lines and polygon in clipper tuple format
    #         C) Start Clipping
    
    print(poly_points)
    
    
    # Pickle for further use
    output = open('poly_data.pkl', 'wb')
    pickle.dump(poly_points, output)
    output.close()    
    
    
    ####################################################################
    ### Point Ordering Options
    ####################################################################
    
    # Using Clipper
    
    #poly_points = create_polys(poly_points) 
    
    # NN Order
    #poly_points = NN_order(poly_points)
    
    
    #print("POLY_POINTS: " , "\n", poly_points.shape, "\n", poly_points)
    
    
    # Convex Hull
#    huh = convex_hull(poly_points)
    
    # Polar Order
#    poly_points = polar_order(poly_points)

    ####################################################################
    ####################################################################
    
    # Create an enclosing path
#    enc_path = create_path(poly_points)

    # Hatch it
#    create_hatch(enc_path, RASTER_ANGLE, HATCH_SPACING)

#    # Dumb path? - just as good it seems...
    #dumb_path = create_dumb_path(poly_points)


    
    #create_polys(poly_points)
if __name__ == "__main__":
    print(__doc__)
    main()
