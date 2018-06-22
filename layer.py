#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
--------------------
Layer infill object
--------------------
Author: Jordan Cave
--------------------
"""

import numpy as np    
import random
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
import pyclipper
import pickle
from pathing import NN_order, convex_hull, polar_order

class Layer:
	""" Class for holding data for layers of the sliced STL files
	
	Accepts user-defined path_type, fill_angle, hatch bool
	
	Possibly very inefficient and verbose....
	
	Main takeaway is the calculated path for plotting (Extra points for plotting lines)
	and the actual calculated tool path (Accurate, but unplottable)
	
	"""
	# Build Characteristics
	bead_width = 0.05 #Inches
	bead_height = 1.00 #Inches
	offset = 0.0 #Inches
	def __init__(self, polygon, path_type = 'Axial', fill_angle = 45, hatch = False, free_form = False):
		self.polygon = polygon # Points of polygon you need to fill
		self.path_type = path_type # Enum a list? straight hatch, idk
		self.fill_angle = fill_angle*math.pi/180 # Degrees to rads
		if self.fill_angle < 0 or self.fill_angle > math.pi/2:
			raise Exception('Fill angle must be in [0,90]°')
		self.hatch = hatch # Layer-to-layer orientation
		self.free_form = free_form # Optional FF Manufacturing
		self.bound_box = self.layer_bound()
		self.scan_list = self.get_scanlines()
		self.intersects = self.get_intersects()
		self.infill = self.get_infill()
		self.path_length = self.calc_length()
		
	def layer_bound(self):
		# Bounds of layer
		self.x_min, self.x_max = min(self.polygon[:,0]), max(self.polygon[:,0])
		self.y_min, self.y_max = min(self.polygon[:,1]), max(self.polygon[:,1])
		self.bb_points = np.asarray([[self.x_min, self.y_min],[self.x_max, self.y_max]])
		self.bound_box = self.bb_points
		return self.bound_box
	
	def get_scanlines(self):
		
		if self.fill_angle == 0:
			# Vertical
			bb = self.bound_box
			self.scan_inc = Layer.bead_width
			self.x = (self.x_min + (self.scan_inc/2))
			self.scan_list = [[[self.x, bb[0][1]],[self.x, bb[1][1]]]]
			while self.x < bb[1][0]:
				self.x += self.scan_inc
				self.scan_list.append([[self.x, bb[0][1]],[self.x, bb[1][1]]])
			self.scan_list = np.asarray(self.scan_list)
			self.scan_list.reshape(-1,2,2)
			return self.scan_list
		
		if self.fill_angle == math.pi/2:
			# Horizontal
			bb = self.bound_box
			self.scan_inc = Layer.bead_width
			self.y = (self.y_min + (self.scan_inc/2))
			self.scan_list = [[[bb[0][0], self.y],[bb[1][0], self.y]]]
			while self.y < bb[1][1]:
				self.y += self.scan_inc
				self.scan_list.append([[bb[0][0], self.y],[bb[1][0], self.y]])
			self.scan_list = np.asarray(self.scan_list)
			self.scan_list.reshape(-1,2,2)
			return self.scan_list
			
		else: # else...?
			# Angled
			bb = self.bound_box
			# Start point - One bead width from BB corner
			self.scan_inc = Layer.bead_width # for now
			self.inc_x = (self.scan_inc/math.cos(self.fill_angle))
			self.inc_y = (self.scan_inc/math.sin(self.fill_angle))
			self.scan_list = [[[self.x_min, self.y_min + (self.inc_y/2)], [self. x_min + (self.inc_x/2), self.y_min]]]
			self.x = (self.x_min + (self.inc_x/2))
			self.y = (self.y_min + (self.inc_y/2))
			self.ind = self.scan_inc
			bb_hyp = math.sqrt((bb[1][0]-bb[0][0])**2+(bb[1][1]-bb[0][1])**2)
			while self.ind < bb_hyp:
				self.x += self.inc_x
				self.y += self.inc_y
				self.scan_list.append([[self.x_min, self.y],[self.x, self.y_min]])
				self.ind += self.scan_inc
			self.scan_list = np.asarray(self.scan_list)    
			self.scan_list = self.scan_list.reshape(-1,2,2)
			return self.scan_list
		

	def get_intersects(self):
		scans = [[tuple(point) for point in line] for line in self.scan_list]
		poly = self.polygon
		pco = pyclipper.Pyclipper()
		pco.AddPaths(pyclipper.scale_to_clipper(scans), pyclipper.PT_SUBJECT, closed = False)
		#polygon = pyclipper.CleanPolygon(polygon, distance = 0.00005)
		if self.free_form == False:
			clip_poly = self._offset_profile(poly)
		elif self.free_form == True:
			clip_poly = poly
		else:
			raise Exception("Not a valid build type")
		pco.AddPath(pyclipper.scale_to_clipper(clip_poly), pyclipper.PT_CLIP, True)
		solution = pco.Execute2(pyclipper.CT_INTERSECTION)
		self.intersects = pyclipper.scale_from_clipper(pyclipper.PolyTreeToPaths(solution))
		#and sort intersects (bottom left to top right)
		self.intersects = self._sort_paths(self.intersects)
		return self.intersects
	
	def get_infill(self):
		# Improvement Ideas:
		# For transverse, use offset as the intermediary paths
		infill = np.reshape(self.intersects, (-1,2))
		
		if self.path_type == 'Axial':
			# Start all lines at same side of layer (They might be already)
			infill = np.reshape(infill, (-1,2,2))
			return infill

		if self.path_type == 'Transverse':
			# Include intermediary pathing between beads in 'zig-zag' config
			# For now just straight line segments between odd lines
			temp1, temp2 = [], []
			swap_idx = 2
			while swap_idx < len(infill):
				self._swap(infill, swap_idx)
				swap_idx+=4	
			t_infill = np.reshape(np.ones(4*len(infill)), (-1,2))
			idx = 0
			t_idx = 0
			while idx < len(infill):
				t_infill[t_idx] = infill[idx]
				t_infill[t_idx+1] = infill[idx]
				idx+=1
				t_idx+=2
			t_infill = np.reshape(t_infill[1:-1], (-1,2,2))
			return t_infill
	
	def plot_toolpath(self):
		plot_polygon = self.polygon
		plot_polygon = np.append(plot_polygon, plot_polygon[0])
		plot_polygon = plot_polygon.reshape(-1,2)
		mpl.style.use('ggplot')
		fig, ax = plt.subplots()
		ax.set_xlim([-1,1])
		ax.set_ylim([-1,1])
		x_poly, y_poly = plot_polygon[:,0], plot_polygon[:,1]
		plt.plot(x_poly, y_poly, color = 'green')
		
		for line in self.infill:
			x_vec = [line[0][0], line[1][0]]
			y_vec = [line[0][1], line[1][1]]
			plt.plot(x_vec, y_vec, color = 'xkcd:pastel purple')
			
	def calc_length(self):
		path_length = float(0)
		for pair in self.infill:
			one_dist = self._euclidean(pair)
			path_length += one_dist
		return path_length
	
	
	@staticmethod
	def _euclidean(pair):
		d_x_1 = math.fabs(pair[1][0] - pair[0][0])
		d_y_1 = math.fabs(pair[1][1] - pair[0][1])
		d_1 = math.sqrt(math.pow(d_x_1, 2) + math.pow(d_y_1, 2))		
		return d_1
	
	
	@staticmethod
	def _swap(paths, idx):
		temp1 = []
		temp2 = []
		for i in paths[idx]:
			temp1.append(i)
		for i in paths[idx+1]:
			temp2.append(i)
		paths[idx] = temp2
		paths[idx+1] = temp1

	@staticmethod
	def _sort_paths(paths):
		paths = np.reshape(np.asarray(paths), (-1, 4))
		paths = sorted(paths, key = lambda x: [x[0] + x[1]])
		paths = np.reshape(np.asarray(paths), (-1, 2, 2))
		return paths
	
	@staticmethod
	def _offset_profile(poly):
		pco = pyclipper.PyclipperOffset()
		pco.AddPath(pyclipper.scale_to_clipper(poly), pyclipper.JT_ROUND, pyclipper.ET_CLOSEDPOLYGON)
		offset = pco.Execute(-pyclipper.scale_to_clipper(Layer.bead_width/2))
		offset = pyclipper.scale_from_clipper(offset)
		offset = np.reshape(offset, (-1,2))
		return offset
	
def main():
		
		#Try loading polygon
		test_polygon = pickle.load(open('poly_data.pkl', 'rb'))

		#test_polygon = NN_order(test_polygon)
		#test_polygon = convex_hull(test_polygon)
		test_polygon = polar_order(test_polygon)
		test_polygon = test_polygon[:,0:2]
		test_infill = Layer(test_polygon, 'Transverse', 45)
		# Check with plotting
		test_polygon = np.append(test_polygon, test_polygon[0])
		test_polygon = test_polygon.reshape(-1,2)
		mpl.style.use('ggplot')
		fig, ax = plt.subplots()
		ax.set_xlim([-1.5,1.5])
		ax.set_ylim([-1.5,1.5])
		x_poly, y_poly = test_polygon[:,0], test_polygon[:,1]
		plt.plot(x_poly, y_poly, color = 'green')
		
		# Pretty plots
		#for line in test_infill.scan_list:
			#x_vec = [line[0][0], line[1][0]]
			#y_vec = [line[0][1], line[1][1]]
			#plt.plot(x_vec, y_vec, color = 'red')
		
		for line in test_infill.infill:
			x_vec = [line[0][0], line[1][0]]
			y_vec = [line[0][1], line[1][1]]
			plt.plot(x_vec, y_vec, color = 'xkcd:pastel purple')
		
		#test_infill.plot_toolpath()
		# Calculated again just for plottting
		clip_poly = Layer._offset_profile(test_infill.polygon)
		clip_poly = np.vstack((clip_poly, clip_poly[0]))
		print(clip_poly)
		x_vec_p = []
		y_vec_p = []
		#for line in clip_poly:
			#x_vec_p.append(line[0])
			#y_vec_p.append(line[1])
		#plt.plot(x_vec_p, y_vec_p, color = 'xkcd:sky blue', linestyle = 'dashed')
	
	
def complete_paths():
	""" Function for calculating complete pathing data for ALL layers of the model """
	
	pass


if __name__ == "__main__":
	print(__doc__)
	main()

    
    
    
