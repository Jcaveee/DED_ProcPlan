"""
---------------------------------------
Time and material consumption estimates
---------------------------------------
Author: Jordan Cave
---------------------------------------
"""

import numpy as np
from sklearn import linear_model

def import_data(filename):
    """ Simple csv import """
    
    build_time = []
    length = []
    file = open(filename)
    garbageline = file.readline()
    for line in file:
        data = line.split(",")
        time = int(data[1])
        path = int(data[2])
        print(path)
        build_time.append(time)
        length.append(path)
    return build_time, length

def time_est(build_type, time_data, path_data):
    """ Linear regression training and predictions """
    
    if build_type == 0:
        train_X = path_data
        train_Y = time_data
        regr = linear_model.LinearRegression()
        regr.fit(train_X, train_Y)
        prediction = reg.predict(444)
        
    if build_tyype == 1:
        
        pass
    
    return prediction
    
class Estimates:
    """ Class for storing the estimated outputs from ML or other optimization modules
    
    Args: Full calculated toolpath
    
    Attributes: Build_time (s), wire consumption (inches), gas consumption (cfm), cost($)
    
    """
    def __init__(self, full_path):
        self.full_path = full_path
        
    def build_time(self):
        """ Build time estimate from STL and PP """
        
        pass

    def wire_cons(self):
        """ Wire consumption estimate """
    
        pass

    def gas_cons(self):
        """ Gas consumption estimate """
    
        pass

    def cost(self):
        """ Production cost estimates """
    
        pass
    
def main():
    time_data, length_data = import_data("build_data.csv")
    print(time_data, length_data)
    time_est(0, time_data, length_data)
    
        
if __name__ == "__main__":
    main()
    
