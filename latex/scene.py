#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:57:36 2022

@author: windhoos
"""

from vpython import canvas,vector
from latex import config as cfg
from math import dist

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
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        camy_max=max(cfg.step3_ycam)
        Oy_cam = dist((cfg.step3_diepte/2,), (camy_max,)) / 2
        dist_max=max(cfg.step3_diepte-Oy_cam,cfg.step3_hoogte)*0.7
        sl.up=vector(0,1,0)
        sl.center = vector(cfg.step3_Ox,cfg.step3_Oy-Oy_cam,cfg.step3_Oz)
        sl.camera.pos = vector(dist_max,0,0)
        sl.camera.axis = vector(-dist_max,0,0)
        sl.center = vector(cfg.step3_Ox,cfg.step3_Oy-Oy_cam,cfg.step3_Oz)

    elif step == 4:
        sl.ambient= vector(1,1,1)
        sl.forward = vector(-1.5,-1.5,-1)
        sl.up = vector(0,0,1)
        x=0 #-cfg.step4_camera[0]+cfg.step4_xmax
        y=-cfg.step4_camera[1]
        z=cfg.step4_camera[2]+cfg.step4_zmax - cfg.voeten.iloc[0]['lengte']*2 - cfg.onderkant.iloc[0]['dikte']*2
        
        sl.center = sl.center #+ vector(x,y,z)
    elif step == 51:
        sl.ambient= vector(1,1,1)
        sl.forward = vector(-.4,-1,-.2)
        sl.up = vector(0,0,1)
        sl.range = cfg.step5_xmax*1.75
        #x=0 #-cfg.step5_camera[0]+cfg.step5_xmax
        #y=-cfg.step5_camera[1]
        #z=cfg.step5_camera[2]+cfg.step5_zmax - cfg.voeten.iloc[0]['lengte']*2 - cfg.onderkant.iloc[0]['dikte']*2
        #sl.center = sl.center + vector(x,y,z)
        #sl.camera.pos=(-sl.center+sl.camera.pos)*0.6
        sl.camera.pos=(-sl.center+sl.camera.pos)*0.7
        sl.camera.pos.x=sl.camera.pos.x*0.1
        sl.camera.pos.y=sl.camera.pos.y*0.1
        #sl.center = cfg.step5_cam22 
        #sl.center.x = sl.center.x - sl.camera.pos.x*0.3
        #print(sl.camera.pos.x)
        
    elif step == 52:
        sl.forward = vector(-.4,-1,-0.05)
        sl.up = vector(0,0,1)
        sl.center = cfg.step5_cam22 # - vector(9,6,-3)
        sl.camera.pos = sl.center + vector(30,60,10)
        
    return sl.center
    
def delete():
    sl.delete()