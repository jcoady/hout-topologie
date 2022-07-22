#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:26:30 2022

@author: windhoos
"""

from latex import get_excel, scene, step1_feet_bottom, step2_rib_bottom, step3_ladder, step4_geraamte, step5_achterrib, arrow
#from latex import config as cfg
import time

def main():
    get_excel.build()
    runlist=[1,2,3,4,5]
    for i in range(len(runlist)):
        run=runlist[i]
        if run == 1:
            name='scene 1 - bottom'
            scene.start_scene(name)
            step1_feet_bottom.build()
            O=scene.cam_reset(1)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 2:    
            name='scene 2 - bottom rib'
            scene.start_scene(name)
            step2_rib_bottom.build()
            O=scene.cam_reset(2)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 3:
            name='scene 3 - ladder'
            scene.start_scene(name)
            step3_ladder.build()
            O=scene.cam_reset(3)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 4:    
            name='scene 4 - geraamte'
            scene.start_scene(name)
            step4_geraamte.build()
            O=scene.cam_reset(4)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 5: 
            name='scene 5 - achterrib a'
            scene.start_scene(name)
            step5_achterrib.build()
            O=scene.cam_reset(51)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            name='scene 5 - achterrib b'
            O=scene.cam_reset(52)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
    
main()