#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:57:36 2022

@author: windhoos
"""

from vpython import canvas,vector
from latex import config as cfg
from math import dist
#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
import os

def start_scene(name):
    print(f'Scene {name} started')
    global sl
    sl = canvas(width=3200, height=3200, center=vector(0,0,0), background=vector(1,1,1))
    #title='                                                                  <b>Closet 3D model</b>    \n\n'
    sl.autoscale = True
    sl.userzoom = False
    sl.userpan = False
    #sl.append_to_title('onderschrift')
    
def capture(path, name):
    #options = webdriver.ChromeOptions() 
    #options.add_argument(f"download.default_directory={path}")
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    sl.capture(os.path.join(path , name))
    
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
        camy_max=max(cfg.step1_ycam, key=abs)
        Oy_cam = dist((cfg.step1_diepte/2,), (camy_max,)) / 2
        dist_max=-max(cfg.step1_diepte-Oy_cam,cfg.step1_breedte, key=abs)*1.5
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
        camx_max=-max(cfg.step2_xcam, key=abs)
        Ox_cam = dist((cfg.step2_breedte/2,), (camx_max,)) / 2
        camy_max=max(cfg.step2_ycam, key=abs)
        Oy_cam = dist((cfg.step2_diepte/2,), (camy_max,)) / 2
        dist_max=max(cfg.step2_diepte-Oy_cam,cfg.step2_breedte-Ox_cam, key=abs)*1.5
        sl.up=vector(0,1,0)

        sl.center = vector(cfg.step2_Ox-Ox_cam,cfg.step2_Oy+Oy_cam,cfg.step2_Oz)
        sl.camera.pos = vector(0,0,dist_max)
        sl.camera.axis = vector(0,0,-dist_max)
        sl.center = vector(cfg.step2_Ox-Ox_cam,cfg.step2_Oy+Oy_cam,cfg.step2_Oz)
        
    elif step == 3:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        camy_max=max(cfg.step3_ycam, key=abs)
        Oy_cam = dist((cfg.step3_diepte/2,), (abs(camy_max),)) / 2
        dist_max=max(cfg.step3_diepte-Oy_cam,cfg.step3_hoogte, key=abs)*1.5
        sl.up=vector(0,1,0)
        sl.center = vector(cfg.step3_Ox,cfg.step3_Oy-Oy_cam,cfg.step3_Oz)
        sl.camera.pos = vector(dist_max,0,0)
        sl.camera.axis = vector(-dist_max,0,0)
        sl.center = vector(cfg.step3_Ox,cfg.step3_Oy-Oy_cam,cfg.step3_Oz)

    elif step == 4:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        dist_max=max(cfg.step4_breedte, cfg.step4_diepte, cfg.step4_hoogte, key=abs)*1.5
        sl.up=vector(0,0,1)
        sl.center = vector(cfg.step4_Ox,cfg.step4_Oy,cfg.step4_Oz)
        sl.camera.pos = vector(dist_max,dist_max/3,dist_max/3)
        sl.camera.axis = vector(-sl.camera.pos.x,-sl.camera.pos.y,-sl.camera.pos.z)
        sl.center = vector(cfg.step4_Ox,cfg.step4_Oy,cfg.step4_Oz)
        
    elif step == 51:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        camx_max=max(cfg.step5_xcam, key=abs)
        Ox_cam = dist((cfg.step5_diepte/2,), (abs(camx_max),)) / 2
        dist_max=max(cfg.step5_breedte-Ox_cam, cfg.step5_diepte, cfg.step5_hoogte, key=abs)*1.5
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
        
    elif step == 61:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        camx_max=max(cfg.step6_xcam, key=abs)
        Ox_cam = dist((cfg.step6_diepte/2,), (abs(camx_max),)) / 2
        dist_max=max(cfg.step6_breedte-Ox_cam, cfg.step6_diepte, cfg.step6_hoogte, key=abs)*1.5
        sl.up=vector(0,0,1)
        sl.center = vector(cfg.step6_Ox,cfg.step6_Oy,cfg.step6_Oz)
        sl.camera.pos = vector(dist_max,dist_max,dist_max/3)
        sl.camera.axis = vector(-sl.camera.pos.x,-sl.camera.pos.y,-sl.camera.pos.z)
        sl.center = vector(cfg.step6_Ox,cfg.step6_Oy,cfg.step6_Oz)
        
    elif step == 62:
        zoom=cfg.step6_zoom[0][1]
        sl.center = vector(zoom[0],zoom[1],zoom[2])
        dist_max=vector(50,50,5)
        sl.camera.pos = dist_max
        sl.camera.axis = vector(-sl.camera.pos.x,-sl.camera.pos.y,-sl.camera.pos.z)
        sl.center = vector(zoom[0],zoom[1],zoom[2])
        
    elif step == 7:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        #camx_max=max(cfg.step7_xcam)
        camx_max=0
        Ox_cam = dist((cfg.step7_diepte/2,), (abs(camx_max),)) / 2
        dist_max=max(cfg.step7_breedte-Ox_cam, cfg.step7_diepte, cfg.step7_hoogte, key=abs)
        sl.up=vector(0,0,1)
        sl.center = vector(cfg.step7_Ox,cfg.step7_Oy,cfg.step7_Oz)
        sl.camera.pos = vector(dist_max,dist_max,dist_max)
        sl.camera.axis = vector(-sl.camera.pos.x,-sl.camera.pos.y,-sl.camera.pos.z)
        sl.center = vector(cfg.step7_Ox,cfg.step7_Oy,cfg.step7_Oz)
        
    elif step == 8:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        #camx_max=max(cfg.step8_xcam)
        camx_max=0
        Ox_cam = dist((cfg.step8_diepte/2,), (abs(camx_max),)) / 2
        dist_max=max(cfg.step8_breedte-Ox_cam, cfg.step8_diepte, cfg.step8_hoogte, key=abs)
        sl.up=vector(0,0,1)
        sl.center = vector(cfg.step8_Ox,cfg.step8_Oy,cfg.step8_Oz)
        sl.camera.pos = vector(dist_max,dist_max,dist_max)
        sl.camera.axis = vector(-sl.camera.pos.x,-sl.camera.pos.y,-sl.camera.pos.z)
        sl.center = vector(cfg.step8_Ox,cfg.step8_Oy,cfg.step8_Oz)
        
    elif step == 91:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        #camx_max=max(cfg.step8_xcam)
        camx_max=0
        Ox_cam = dist((cfg.step9_diepte/2,), (abs(camx_max),)) / 2
        dist_max=max(cfg.step9_breedte-Ox_cam, cfg.step9_diepte, cfg.step9_hoogte, key=abs)
        sl.up=vector(0,0,1)
        sl.center = vector(cfg.step9_Ox,cfg.step9_Oy,cfg.step9_Oz)
        sl.camera.pos = vector(dist_max,dist_max,dist_max)
        sl.camera.axis = vector(-sl.camera.pos.x,-sl.camera.pos.y,-sl.camera.pos.z)
        sl.center = vector(cfg.step9_Ox,cfg.step9_Oy,cfg.step9_Oz)
        
    elif step == 92:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        #camx_max=max(cfg.step8_xcam)
        camx_max=0
        Ox_cam = dist((cfg.step9_diepte/2,), (abs(camx_max),)) / 2
        dist_max=max(cfg.step9_breedte-Ox_cam, cfg.step9_diepte, cfg.step9_hoogte, key=abs)
        sl.up=vector(0,0,1)
        sl.center = vector(cfg.step9_Ox,cfg.step9_Oy,cfg.step9_Oz)
        sl.camera.pos = vector(dist_max,-dist_max,dist_max)
        sl.camera.axis = -sl.camera.pos
        sl.center = vector(cfg.step9_Ox,cfg.step9_Oy,cfg.step9_Oz)
        
    elif step == 101:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        camz_max=max(cfg.step10_zcam)
        Oz_cam = dist((cfg.step10_diepte/2,), (abs(camz_max),)) / 2
        dist_max=max(cfg.step10_breedte, cfg.step10_diepte, cfg.step10_hoogte, key=abs)*1.5
        sl.up=vector(0,0,1)
        sl.center = vector(cfg.step10_Ox,cfg.step10_Oy,cfg.step10_Oz-Oz_cam)
        sl.camera.pos = vector(dist_max*.2,dist_max,dist_max*.2)
        sl.camera.axis = -sl.camera.pos
        sl.center = vector(cfg.step10_Ox,cfg.step10_Oy,cfg.step10_Oz-Oz_cam/2)
        
    elif step == 102:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        #camz_max=max(cfg.step10_zcam)
        #Oz_cam = dist((cfg.step10_diepte/2,), (abs(camz_max),)) / 2
        #dist_max=max(cfg.step10_breedte, cfg.step10_diepte, cfg.step10_hoogte)*1.2
        sl.up=vector(0,0,1)
        sl.center = vector(cfg.step10_zoom[0],cfg.step10_zoom[1],cfg.step10_zoom[2])
        dist_max=vector(10,50,5)*1.5
        sl.camera.pos = dist_max
        sl.camera.axis = vector(-sl.camera.pos.x,-sl.camera.pos.y,-sl.camera.pos.z)
        sl.center = vector(cfg.step10_zoom[0],cfg.step10_zoom[1],cfg.step10_zoom[2])
        
    elif step == 11:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        camz_max=max(cfg.step11_zcam, key=abs)
        camx_max=max(cfg.step11_xcam, key=abs)
        Oz_cam = dist((cfg.step11_hoogte/2,), (abs(camz_max),)) / 2
        Ox_cam = dist((cfg.step11_breedte/2,), (abs(camx_max),)) / 2
        dist_max=max(cfg.step11_breedte, cfg.step11_diepte, cfg.step11_hoogte, key=abs)*2
        sl.up=vector(0,0,1)
        sl.center = vector(cfg.step11_Ox-Ox_cam/2,cfg.step11_Oy,cfg.step11_Oz+Oz_cam/3)
        sl.camera.pos = vector(dist_max*.05,-dist_max,dist_max*.05)
        sl.camera.axis = -sl.camera.pos
        sl.center = vector(cfg.step11_Ox-Ox_cam/2,cfg.step11_Oy,cfg.step11_Oz+Oz_cam/3)
        
    elif step == 12:
        sl.autoscale = False
        sl.ambient= vector(1,1,1)
        camz_max=0 #max(cfg.step12_zcam)
        Oz_cam = 0 #dist((cfg.step12_diepte/2,), (abs(camz_max),)) / 2
        dist_max=max(cfg.step12_breedte, cfg.step12_diepte, cfg.step10_hoogte, key=abs)
        sl.up=vector(0,0,1)
        sl.center = vector(cfg.step12_Ox,cfg.step12_Oy,cfg.step12_Oz-Oz_cam)
        sl.camera.pos = vector(dist_max*.75,dist_max,dist_max*.75)
        sl.camera.axis = -sl.camera.pos
        sl.center = vector(cfg.step12_Ox,cfg.step12_Oy,cfg.step12_Oz-Oz_cam/2)
        
    return sl.center
    
def delete():
    sl.delete()