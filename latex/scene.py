#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:57:36 2022

@author: windhoos
"""

from vpython import canvas,vector,color

def start_scene():
    print('Scene started')
    global sl
    sl = canvas(title='                                                                  <b>Closet 3D model</b>    \n\n', width=800, height=600, center=vector(0,0,0), background=color.white)
    sl.autoscale = True
    sl.userzoom = False
    sl.userpan = False
    sl.append_to_title('onderschrift')  
    sl.forward = vector(0,-1,0)
    sl.up = vector(0,0,1)