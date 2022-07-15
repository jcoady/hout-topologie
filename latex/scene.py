#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:57:36 2022

@author: windhoos
"""

from vpython import canvas,vector
from latex import config as cfg

def start_scene(name):
    print(f'Scene {name} started')
    global sl
    sl = canvas(width=800, height=600, center=vector(0,0,0), background=vector(1,1,1))
    #title='                                                                  <b>Closet 3D model</b>    \n\n'
    sl.autoscale = True
    sl.userzoom = False
    sl.userpan = False
    #sl.append_to_title('onderschrift')
    
def capture(name):
    sl.capture(name)
    
def cam_reset(step):
    if step == 1:
        sl.ambient= vector(1,1,1)
        sl.forward = vector(0,0,1)
        sl.up = vector(0,1,0)
        x=cfg.step1_camera[0]
        y=cfg.step1_camera[1]
        z=cfg.step1_camera[2]
        sl.center = sl.center + vector(x,y,z)
    elif step == 2:
        sl.ambient= vector(1,1,1)
        sl.forward = vector(0,0,-1)
        sl.up = vector(0,1,0)
        x=-cfg.step2_camera[0]
        y=cfg.step2_camera[1]
        z=cfg.step2_camera[2]
        sl.center = sl.center + vector(x,y,z)
    elif step == 3:
        sl.ambient= vector(1,1,1)
        sl.forward = vector(-1,0,0)
        sl.up = vector(0,0,1)
        x=-cfg.step3_camera[0]+cfg.step3_xmax
        y=-cfg.step3_camera[1]
        z=cfg.step3_camera[2]+cfg.step3_zmax
        print(z,cfg.step3_camera[2],cfg.step3_zmax)
        sl.center = sl.center + vector(x,y,z)
        
    return sl.center

def zoom(value):
    sl.range = value
    
def delete():
    sl.delete()