#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-------------------
toolpath object
-------------------
Author: Jordan Cave
-------------------
"""

import numpy as np

class toolpath:
    """ Class  for holding all types of path outputs
    
    Accepts multiple layer objects and can create multiple output formats
    
    Toolpaths can be outputted to txt files for use with Siemens 840D \
    
    Controllers, LAWS, or Karel systems. Also plain text coordinates available.
    """
    def __init__(self, layers):
        self.layers = layers # Note need to concatenate layer objects correctly
        self.path = self.clean_path()
        self.gcode = []
        self.winlaws  = []
        self.karel = []
        
    def clean_path(self):
        """ Clean path from layer object - write to txt file """
        self.path = np.asarray(self.layers)
        self.path = np.reshape(self.path, (-1,2))
        idx = 0
        clean_path = []
        while idx in range(self.path.shape[0]):
            if idx%2 == 0:
                clean_path.append(self.path[idx])
            idx+=1
        clean_path.append(self.path[self.path.shape[0]-1])
        self.path = np.asarray(clean_path)
        return self.path
    
    def gcode_path(self, speed):
        """Siemens 840D g-code translation """
        speed = int(25.4*speed) #in/min to mm/min
        doc1, doc2, doc3 = "(Siemens 840D Automated G-Code)", "(ECN Systems)", "(Notes: ) \n"
        ref = "G28 X Y Z;"
        start = "G90;"
        stop = "M02;"
        linear = "G01"
        feed_1 = speed
        feed_2 = speed*2
        
        g_code = [doc1, doc2, doc3, ref, start]
        Z=0
        for line in self.clean_path():
            g_line = "G01 X{0} Y{1} Z{2} F{3};".format(line[0], line[1], Z, feed_1)
            g_code.append(g_line)
        g_code.append(stop)
        return g_code
    
    def winlaws_path(self):
        """ TBD """
        pass
    
    def karel_path(self):
        """ TBD """
        pass
    
    def publish_path(self, path_type):
        """ Output to file """
        if path_type == 'plaintext':
            np.savetxt('test.txt', self.clean_path(), delimiter = ',')
            return True
        if path_type == 'gcode':
            np.savetxt('test.txt', self.gcode_path(3), fmt='%s', delimiter = ',')
            return True
        if path_type == 'winlaws':
            pass
        if path_type == 'karel':
            pass
        else:
            raise Exception('Not a valid path type')
    

def main():
    
    test_path = np.array([[[0,0], [1,1]], [[1,1], [2,2]], [[2,2],[3,3]],[[3,3],[4,4]], [[4,4], [5,5]]])
    test_toolpath  = toolpath(test_path)
    print(test_toolpath.clean_path())
    #test_toolpath.publish_path('plaintext')
    #print(test_toolpath.gcode_path())
    test_toolpath.publish_path('gcode')

if __name__ == '__main__':
    print(__doc__)
    main()