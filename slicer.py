#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------
Slicing Module
-------------------
Author: Jordan Cave
-------------------
 - Old, very repetetive, but it works
"""
import settings
import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, PathPatch
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib import cm
from rotate import rotate_part
import collections
import pickle
import math

# STL file for manual import
file_name = 'Weld_Neg.stl'

def plot_mesh(mesh):
    """ Load and plot initial """
    figure = plt.figure()
    axes = mplot3d.Axes3D(figure)
    if mesh[0].shape[0] == 9:
        axes.add_collection3d(mplot3d.art3d.Poly3DCollection(mesh.vectors))
        scale = mesh.points.flatten('C')
    if mesh[0].shape[0] == 3:
        axes.add_collection3d(mplot3d.art3d.Poly3DCollection(mesh))   
        scale = mesh.flatten('C')
    axes.auto_scale_xyz(scale, scale, scale)
    plt.show()
    
def mesh_stats(mesh):
    """ Stats from numpy-stl """
    volume, cog, inertia = mesh.get_mass_properties()
    print("Volume                                  = {0}".format(volume))
    print("Position of the center of gravity (COG) = {0}".format(cog))
    print("Inertia matrix at expressed at the COG  = {0}".format(inertia[0,:]))
    print("                                          {0}".format(inertia[1,:]))
    print("                                          {0}".format(inertia[2,:]))
    
def mesh_max(mesh_points):
    """ X,Y,Z Limits for plotting """
    x,y,z = np.zeros(len(mesh_points)),np.zeros(len(mesh_points)),np.zeros(len(mesh_points))
    for idx in range(len(mesh_points)):
        x[idx] = max(mesh_points[idx][:,0])    
        y[idx] = max(mesh_points[idx][:,1])
        z[idx] = max(mesh_points[idx][:,2])
    x_max, y_max, z_max = max(x), max(y), max(z)
    return(x_max,y_max,z_max)

def mesh_min(mesh_points):
    """ X,Y,Z Limits for plotting """
    x,y,z = np.zeros(len(mesh_points)),np.zeros(len(mesh_points)),np.zeros(len(mesh_points))
    for idx in range(len(mesh_points)):
        x[idx] = min(mesh_points[idx][:,0])    
        y[idx] = min(mesh_points[idx][:,1])
        z[idx] = min(mesh_points[idx][:,2])
    x_min, y_min, z_min = min(x), min(y), min(z)
    return(x_min,y_min,z_min)

def trim_tri_list(mesh_points, slice_height):
    idx = 0
    idx_list = []
    while idx < len(mesh_points):
        if min(mesh_points[idx][:,2]) > slice_height or \
           max(mesh_points[idx][:,2]) < slice_height:
            idx_list.append(idx)          
        idx+=1
    mesh_points = np.delete(mesh_points, idx_list,0)
    return mesh_points    

def get_intersects(tri_entry, layer_h):
    """ Calculate intersections for current triangles
    4 Cases   
    """
    #Case 1: 3 vertices on plane
    if check_points(tri_entry.flatten('C')[2::3], layer_h) == 3:
        return tri_entry
    # Case 2: 2 vertices on plane
    if check_points(tri_entry.flatten('C')[2::3], layer_h) == 2:
        return coords_on_plane(tri_entry, layer_h)          
    # Case 3: 1 vertex on plane
    if check_points(tri_entry.flatten('C')[2::3], layer_h) == 1:
        # 2 Sub cases    
        # (1) Other 2 points on opposited sides of slice
        if check_z(tri_entry, layer_h) == 0:
            intersect = vec_intersect(tri_entry, layer_h)
            return np.vstack((intersect, coords_on_plane(tri_entry, layer_h)))              
        # (2) Other 2 points on same side of slice
        if check_z(tri_entry, layer_h) == 1:
            return coords_on_plane(tri_entry, layer_h)         
    # Case 4: 0 vertices on plane
    if check_points(tri_entry.flatten('C')[2::3], layer_h) == 0:
        # Check which lines interesct
        a =  vec_intersect(tri_entry[0:2,:], layer_h)
        b =  vec_intersect(tri_entry[1:3,:], layer_h)
        c =  vec_intersect(tri_entry[[0,2]], layer_h)
        intersect = np.hstack((a, b, c))
        intersect = list(filter(None.__ne__,  intersect))
        intersect = np.reshape(intersect,(-1,3))
        return np.asarray(intersect)

def check_points(tri_list_entry, layer_h):
    """ Helper function for get_intersects
    Number of points on curr_z
    """
    count = collections.Counter(tri_list_entry)
    return count[layer_h]

def coords_on_plane(tri_list_entry, layer_h):
    """ Helper function for get_intersects
    Returns coordinates on slice plane
    """
    index = np.where(tri_list_entry[:,2] != layer_h)
    tri_list_entry = np.delete(tri_list_entry, index, 0)
    return tri_list_entry

def check_z(tri_list_entry, layer_h):
    """ Helper function for 1 point on slice case
    Returns 0 if points on opposite sides and 1 if same side (1 - point case)
    Could include: Check for single point on  plane
    """
    z_ind = np.where(tri_list_entry[:,2] != layer_h)
    z_vals = tri_list_entry[z_ind]
    if z_vals[0,2] > layer_h and z_vals[1,2] > layer_h:
        return 1
    if z_vals[0,2] < layer_h and z_vals[1,2] < layer_h:
        return 1
    else:
        return 0
    
def vec_intersect(tri_list_entry, layer_h):
    """ Calculate line intersects
    Break if points are on the same side of slice
    """
    if tri_list_entry[0,2] > layer_h and tri_list_entry[1,2] > layer_h:
        return    
    if tri_list_entry[0,2] < layer_h and tri_list_entry[1,2] < layer_h:
        return
    # Continue if they are on opposite sides
    x_int = (layer_h - tri_list_entry[0,2])*(tri_list_entry[1,0]-tri_list_entry[0,0])/(tri_list_entry[1,2]-tri_list_entry[0,2])+tri_list_entry[0,0]
    y_int = (layer_h - tri_list_entry[0,2])*(tri_list_entry[1,1]-tri_list_entry[0,1])/(tri_list_entry[1,2]-tri_list_entry[0,2])+tri_list_entry[0,1]
    z_int = layer_h    
    return np.array([x_int,y_int,z_int])

def x_y_vecs(intersects):
    """ Helper function for plotting """
    idx = 0
    while idx < len(intersects):
        if intersects[idx].shape[0] == 1:
            x_vec, y_vec = intersects[idx][0][0], intersects[idx][0][1]
        if intersects[idx].shape[0] == 2:
            x_vec, y_vec = [], []
            x_points, y_points = intersects[idx][:,0], intersects[idx][:,1] 
            x_vec, y_vec = np.hstack((x_vec,x_points)), np.hstack((y_vec,y_points))
        if intersects[idx].shape[0] == 3:
            x_vec, y_vec = [], []
            x_points, y_points = intersects[idx][:,0], intersects[idx][:,1] 
            x_vec, y_vec = np.hstack((x_vec,x_points)), np.hstack((y_vec,y_points))
        idx+=1
        return x_vec,y_vec

def plot_slice(intersects):
    """ Tri plotting SEGMENTS """
    fig, ax = plt.subplots()
    idx = 0
    while idx < len(intersects):
        if intersects[idx].shape[0] == 1:
            x_vec, y_vec = intersects[idx][0][0], intersects[idx][0][1]
            plt.scatter(x_vec, y_vec, color = 'red')
        if intersects[idx].shape[0] == 2:
            x_vec, y_vec = [], []
            x_points, y_points = intersects[idx][:,0], intersects[idx][:,1] 
            x_vec, y_vec = np.hstack((x_vec, x_points)), np.hstack((y_vec,y_points))
#            x_vec, y_vec = np.c_[intersects[idx][:,0],intersects[idx][:,1]]
            plt.plot(x_vec, y_vec, color = 'green')
        if intersects[idx].shape[0] == 3:
            x_vec, y_vec = [], []
            x_points, y_points = intersects[idx][:,0], intersects[idx][:,1] 
            x_vec, y_vec = np.hstack((x_vec, x_points)), np.hstack((y_vec,y_points))
#            x_vec, y_vec = np.c_[intersects[idx][:,0],intersects[idx][:,1]]
            plt.plot(x_vec, y_vec, color = 'blue')
        idx+=1
    plt.show()
    
def plot_slice_dict(slice_dict):
    """ Unsure """
    num_subplots = len(slice_dict)
    assert num_subplots != 0
    columns = 5
    rows = math.ceil(num_subplots/columns)
    idx = 1
    while idx <= num_subplots:
#        print("SLICE_DICT: ", slice_dict[idx-1].shape)
#        print(slice_dict[idx-1])
#        print("IDX: ", idx)
#        print(slice_dict[idx-1][:,0][:,0], slice_dict[idx-1][:,0][:,1])
        ax1 = plt.subplot(rows,columns,idx)
        if slice_dict[idx-1].shape[1] == 1:
            x_vec, y_vec = slice_dict[idx-1][0][0][0], slice_dict[idx-1][0][0][1]
            ax1.scatter(x_vec, y_vec, color = 'red')
        if slice_dict[idx-1].shape[1] == 2:
            x_vec, y_vec = [], []
            x_points, y_points = slice_dict[idx-1][:,0][:,0], slice_dict[idx-1][:,0][:,1] 
            x_vec, y_vec = np.hstack((x_vec, x_points)), np.hstack((y_vec,y_points))
#            x_vec, y_vec = np.c_[intersects[idx][:,0],intersects[idx][:,1]]
            ax1.scatter(x_vec, y_vec, color = 'green')
        if slice_dict[idx-1].shape[1] == 3:
            x_vec, y_vec = [], []
            x_points, y_points = slice_dict[idx-1][:,0][:,0], slice_dict[idx-1][:,0][:,1] 
            x_vec, y_vec = np.hstack((x_vec, x_points)), np.hstack((y_vec,y_points))
#            x_vec, y_vec = np.c_[intersects[idx][:,0],intersects[idx][:,1]]
            ax1.scatter(x_vec, y_vec, color = 'blue')
        idx+=1
    plt.show()
    

def plt_3d_slices(slice_dict):
    """ 3D Plot of Slices """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    num_slices = len(slice_dict)
    
    for key in slice_dict:
        intersects = slice_dict[key]
        idx = 0
        while idx < len(intersects):
            if intersects[idx].shape[0] == 1:
                x_vec, y_vec, z_vec = intersects[idx][0][0], intersects[idx][0][1], intersects[idx][0][2]
                ax.scatter(x_vec, y_vec, z_vec, color = 'green', s = 1)
            if intersects[idx].shape[0] == 2:
                x_vec, y_vec, z_vec = [], [], []
                x_points, y_points, z_points = intersects[idx][:,0], intersects[idx][:,1], intersects[idx][:,2]  
                x_vec, y_vec, z_vec = np.hstack((x_vec, x_points)), np.hstack((y_vec,y_points)), np.hstack((z_vec, z_points))
                ax.plot(x_vec, y_vec, z_vec ,color = 'green')
            if intersects[idx].shape[0] == 3:
                x_vec, y_vec, z_vec = [], [], []
                x_points, y_points, z_points = intersects[idx][:,0], intersects[idx][:,1], intersects[idx][:,2] 
                x_vec, y_vec, z_vec = np.hstack((x_vec, x_points)), np.hstack((y_vec,y_points)), np.hstack((z_vec, z_points))
                ax.plot(x_vec, y_vec, z_vec, color = 'blue')
            idx+=1
    plt.show()


def plt_3d_slices_2(slice_dict):
    """ 3D Plot of Slices """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    num_slices = len(slice_dict)
    
    for key in slice_dict:
        intersects = slice_dict[key]  
        ax.add_collection3d(mplot3d.art3d.Line3DCollection(intersects, color = 'green'))
    ax.auto_scale_xyz(intersects, intersects, intersects)
        
    plt.show()


def plot_slice_dict_weld(slice_dict):
    """ Unsure """
    num_subplots = len(slice_dict)
    assert num_subplots != 0
    columns = 5
    rows = math.ceil(num_subplots/columns)
    idx = 1
    while idx <= num_subplots:
        num_rows = list(slice_dict[idx-1].shape)
        ax1 = plt.subplot(rows,columns,idx)
        if len(num_rows) == 1:
            x_vec, y_vec = slice_dict[idx-1][0][0][0], slice_dict[idx-1][0][0][1]
            ax1.scatter(x_vec, y_vec, color = 'red', s = 10)
            idx+=1
            continue
        if num_rows[1] == 2:
            x_vec, y_vec = [], []
            x_points, y_points = slice_dict[idx-1][:,0][:,0], slice_dict[idx-1][:,0][:,1] 
            x_vec, y_vec = np.hstack((x_vec, x_points)), np.hstack((y_vec,y_points))
#            x_vec, y_vec = np.c_[intersects[idx][:,0],intersects[idx][:,1]]
            ax1.scatter(x_vec, y_vec, color = 'green', s = 10)
        if num_rows[1] == 3:
            x_vec, y_vec = [], []
            x_points, y_points = slice_dict[idx-1][:,0][:,0], slice_dict[idx-1][:,0][:,1] 
            x_vec, y_vec = np.hstack((x_vec, x_points)), np.hstack((y_vec,y_points))
#            x_vec, y_vec = np.c_[intersects[idx][:,0],intersects[idx][:,1]]
            ax1.scatter(x_vec, y_vec, color = 'blue')
        idx+=1
    plt.show()

    
def main():
    # Load up STL and Mesh
    z_inc = 0.04
    your_mesh = mesh.Mesh.from_file(file_name)
    new_mesh = []
    for idx in range(len(your_mesh)):
        new_entry = np.reshape(your_mesh.points[idx],(-1,3))
        new_mesh.append(new_entry)
    new_mesh = np.asarray(new_mesh)
    
    plot_mesh(your_mesh)
    
    # Optional rotation of part
    new_mesh = rotate_part(0,0,0,new_mesh)
    
    plot_mesh(new_mesh)
    
    # Get min/max for slicing
    model_max = mesh_max(new_mesh)[2]
    model_min = mesh_min(new_mesh)[2]   
    current_z = model_min +  z_inc
    slice_count = 0
    
    # Store each slice
    slice_dict = {}
    ord_slice_dict = collections.OrderedDict()
    
    # Slice N' Dice
    while current_z <= model_max:        
        # Triangles that intersect slice
        int_mesh = trim_tri_list(new_mesh, current_z) 
        
        #Calculate intersects
        int_list = []
        for idx in range(len(int_mesh)):
            int_list.append(get_intersects(int_mesh[idx], current_z))
            idx+=1
        int_list = np.asarray(int_list)
        
        # Plot each individual slice separately
        #plot_slice(int_list)
        
        # Increment for bead height
        current_z+=z_inc    
        # Store slice data
        slice_dict[slice_count] = int_list
                  
        # Ordered slice data
        ord_slice_dict[slice_count] = int_list
                      
        slice_count+=1
    
        # Pickle for further use
        output = open('slice_data.pkl', 'wb')
        pickle.dump(slice_dict, output)
        output.close()
             
    # 3D Plot of Slices
    plt_3d_slices_2(slice_dict)
    
    print("NUMBER OF SLICES: ", slice_count)
    print(slice_dict[0])

def slice_stl(mesh):
    """ For GUI version of main(): """
    # Import from file
    your_mesh = mesh
    new_mesh = []
    for idx in range(len(your_mesh)):
        new_entry = np.reshape(your_mesh.points[idx],(-1,3))
        new_mesh.append(new_entry)
    new_mesh = np.asarray(new_mesh)
    new_mesh = rotate_part(0,0,0,new_mesh)
    # Get min/max for slicing
    model_max = mesh_max(new_mesh)[2]
    model_min = mesh_min(new_mesh)[2]   
    current_z = model_min + (settings.pp_bead_height/2)
    slice_count = 0
    
    # Store each slice
    slice_list = []
    
    # Slice N' Dice
    while current_z <= model_max:        
        # Triangles that intersect slice
        int_mesh = trim_tri_list(new_mesh, current_z) 
        
        #Calculate intersects
        int_list = []
        for idx in range(len(int_mesh)):
            int_list.append(get_intersects(int_mesh[idx], current_z))
            idx+=1
        int_list = np.asarray(int_list)
        # Increment for bead height
        current_z+=settings.pp_bead_height
        
        # Store slice data
        slice_list.append(int_list)
                      
        slice_count+=1
    
    return np.asarray(slice_list)
  
if __name__ == "__main__":
    print(__doc__)
    main()