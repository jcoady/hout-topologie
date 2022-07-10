#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:57:36 2022

@author: windhoos
"""

from vpython import canvas,vector
from latex import config as cfg

def start_scene():
    print('Scene started')
    global sl
    sl = canvas(title='                                                                  <b>Closet 3D model</b>    \n\n', width=800, height=600, center=vector(0,0,0), background=vector(1,1,1))
    sl.autoscale = True
    sl.userzoom = False
    sl.userpan = False
    sl.append_to_title('onderschrift') 
    sl.ambient= vector(1,1,1)
    sl.forward = vector(0,-.1,1)
    sl.up = vector(0,1,0)
    
def capture(name):
    sl.capture(name)
    
def cam_reset():
    x=cfg.step1_camera[0]
    y=cfg.step1_camera[1]
    z=cfg.step1_camera[2]
    sl.center = sl.center + vector(x,y,z)