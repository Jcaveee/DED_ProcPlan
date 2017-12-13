#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-----------------
Rotation function
-----------------
Author: jcave
-----------------
"""

from math import sin, cos, pi
import numpy as np

def rotate_part(theta_X, theta_Y, theta_Z, mesh):   
    """ Define rotational angles according to coordinates // Rads -> Degrees """

    theta_X = theta_X*(pi/180)
    theta_Y = theta_Y*(pi/180)
    theta_Z = theta_Z*(pi/180)
    
    # Calculate the rotational transformation matrices
    R_X = np.array([[1,0,0],[0,cos(theta_X),-sin(theta_X)],[0,sin(theta_X), cos(theta_X)]])
    R_Y = np.array([[cos(theta_Y),0,sin(theta_Y)],[0,1,0],[-sin(theta_Y),0,cos(theta_Y)]])
    R_Z = np.array([[cos(theta_Z),-sin(theta_Z),0],[sin(theta_Z),cos(theta_Z),0],[0,0,1]])

    # Multiply every point in mesh with rot. mat's
    rot_mesh = []
    idx = 0
    while idx < len(mesh):
        rot_mesh.append(np.dot(np.dot(np.dot(mesh[idx],R_X),R_Y),R_Z))
        idx += 1
    
    return np.asarray(rot_mesh)

