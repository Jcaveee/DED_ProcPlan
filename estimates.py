"""
---------------------------------------
Time and material consumption estimates
---------------------------------------
Author: Jordan Cave
---------------------------------------
"""

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



