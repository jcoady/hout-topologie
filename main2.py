#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:26:30 2022

@author: windhoos
"""

from latex import get_excel, scene, step1_feet_bottom, step2_rib_bottom, step3_ladder, arrow
import time

def main():
    get_excel.build()
    
    name='scene 1 - bottom'
    scene.start_scene(name)
    step1_feet_bottom.build()
    #arrow.origin()
    scene.cam_reset(1)
    scene.capture(name)
    scene.delete()
    time.sleep(1)
    
    name='scene 2 - bottom rib'
    scene.start_scene(name)
    step2_rib_bottom.build()
    #arrow.origin()
    scene.cam_reset(2)
    scene.capture(name)
    scene.delete()
    time.sleep(1)
    
    name='scene 3 - ladder'
    scene.start_scene(name)
    step3_ladder.build()
    #arrow.origin()
    scene.cam_reset(3)
    scene.capture(name)
    #scene.delete()
    #time.sleep(1)  
main()