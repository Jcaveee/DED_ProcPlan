#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
---------------------------
Initialize global variables
---------------------------
Author: Jordan Cave
---------------------------
"""

def init():
    global pp_power, pp_travel_speed, pp_focal_distance, pp_feed_rate
    global pp_bead_width, pp_bead_height
    global pp_option
    pp_power, pp_travel_speed, pp_focal_distance, pp_feed_rate = 0.0 , 0.0, 0.0, 0.0
    pp_bead_width, pp_bead_height = 1.0, 1.0
    pp_option = 0 #ENUM SOMETHING HERE?!??!!?!
    