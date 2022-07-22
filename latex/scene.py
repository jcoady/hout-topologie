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
    sl = canvas(width=800, height=800, center=vector(0,0,0), background=vector(1,1,1))
    #title='                                                                  <b>Closet 3D model</b>    \n\n'
    sl.autoscale = True
    sl.userzoom = False
    sl.userpan = False
    #sl.append_to_title('onderschrift')
    
def capture(name):
    sl.capture(name)
    
def cam_reset(step):
    if step == 1:
        #sl.ambient= vector(1,1,1)
        #sl.forward = vector(0,0,1)
        #sl.up = vector(0,1,0)
        #x=cfg.step1_camera[0]
        #y=cfg.step1_camera[1]
        #z=cfg.step1_camera[2]
        #l.center = sl.center + vector(x,y,z)
        
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        camy_max=max(cfg.step1_ycam)
        Oy_cam = dist((cfg.step1_diepte/2,), (camy_max,)) / 2
        dist_max=-max(cfg.step1_diepte-Oy_cam,cfg.step1_breedte)
        sl.up=vector(0,1,0)
        sl.center = vector(cfg.step1_Ox,cfg.step1_Oy+Oy_cam,cfg.step1_Oz)
        sl.camera.pos = vector(0,0,dist_max)
        sl.camera.axis = vector(0,0,-dist_max)
        sl.center = vector(cfg.step1_Ox,cfg.step1_Oy+Oy_cam,cfg.step1_Oz)
        
    elif step == 2:
        #sl.ambient= vector(1,1,1)
        #sl.forward = vector(0,0,-1)
        #sl.up = vector(0,1,0)
        #x=-cfg.step2_camera[0]
        #y=cfg.step2_camera[1]
        #z=cfg.step2_camera[2]
        #l.center = sl.center + vector(x,y,z)
        
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        camx_max=-max(cfg.step2_xcam)
        Ox_cam = dist((cfg.step2_breedte/2,), (camx_max,)) / 2
        camy_max=max(cfg.step2_ycam)
        Oy_cam = dist((cfg.step2_diepte/2,), (camy_max,)) / 2
        dist_max=max(cfg.step2_diepte-Oy_cam,cfg.step2_breedte-Ox_cam)*1.5
        sl.up=vector(0,1,0)

        sl.center = vector(cfg.step2_Ox-Ox_cam,cfg.step2_Oy+Oy_cam,cfg.step2_Oz)
        sl.camera.pos = vector(0,0,dist_max)
        sl.camera.axis = vector(0,0,-dist_max)
        sl.center = vector(cfg.step2_Ox-Ox_cam,cfg.step2_Oy+Oy_cam,cfg.step2_Oz)
        
    elif step == 3:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        camy_max=max(cfg.step3_ycam)
        Oy_cam = dist((cfg.step3_diepte/2,), (camy_max,)) / 2
        dist_max=max(cfg.step3_diepte-Oy_cam,cfg.step3_hoogte)
        sl.up=vector(0,1,0)
        sl.center = vector(cfg.step3_Ox,cfg.step3_Oy-Oy_cam,cfg.step3_Oz)
        sl.camera.pos = vector(dist_max,0,0)
        sl.camera.axis = vector(-dist_max,0,0)
        sl.center = vector(cfg.step3_Ox,cfg.step3_Oy-Oy_cam,cfg.step3_Oz)

    elif step == 4:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        dist_max=max(cfg.step4_breedte, cfg.step4_diepte, cfg.step4_hoogte)
        sl.up=vector(0,0,1)
        sl.center = vector(cfg.step4_Ox,cfg.step4_Oy,cfg.step4_Oz)
        sl.camera.pos = vector(dist_max,dist_max/3,dist_max/3)
        sl.camera.axis = vector(-sl.camera.pos.x,-sl.camera.pos.y,-sl.camera.pos.z)
        sl.center = vector(cfg.step4_Ox,cfg.step4_Oy,cfg.step4_Oz)
        
    elif step == 51:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        camx_max=max(cfg.step5_xcam)
        Ox_cam = dist((cfg.step5_diepte/2,), (camx_max,)) / 2
        dist_max=max(cfg.step5_breedte-Ox_cam, cfg.step5_diepte, cfg.step5_hoogte)*0.8
        sl.up=vector(0,0,1)
        sl.center = vector(cfg.step5_Ox,cfg.step5_Oy,cfg.step5_Oz)
        sl.camera.pos = vector(dist_max,dist_max,dist_max/3)
        sl.camera.axis = vector(-sl.camera.pos.x,-sl.camera.pos.y,-sl.camera.pos.z)
        sl.center = vector(cfg.step5_Ox,cfg.step5_Oy,cfg.step5_Oz)
        
    elif step == 52:
        zoom=cfg.step5_zoom[0][1]
        sl.center = vector(zoom[0],zoom[1],zoom[2])
        dist_max=vector(50,50,5)
        sl.camera.pos = dist_max
        sl.camera.axis = vector(-sl.camera.pos.x,-sl.camera.pos.y,-sl.camera.pos.z)
        sl.center = vector(zoom[0],zoom[1],zoom[2])
        
    return sl.center
    
def delete():
    sl.delete()