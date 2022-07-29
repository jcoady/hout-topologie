#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:26:30 2022

@author: windhoos
"""

from latex import get_excel, scene, step1_feet_bottom, step2_rib_bottom, step3_ladder, step4_geraamte, step5_achterrib, step6_vlonders, step7_boven, step8_linksrechts, step9_achter, step10_deurpost, step11_deur, step12_compleet, arrow
#from latex import config as cfg
import time

def main():
    get_excel.build()
    runlist=[1,2,3,4,5,6,7,8,9,10,11]
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
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 6: 
            name='scene 6 - vlonders a'
            scene.start_scene(name)
            step6_vlonders.build()
            O=scene.cam_reset(61)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            name='scene 6 - vlonders b'
            O=scene.cam_reset(62)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 7: 
            name='scene 7 - boven'
            scene.start_scene(name)
            step7_boven.build()
            O=scene.cam_reset(7)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 8: 
            name='scene 8 - links/rechts'
            scene.start_scene(name)
            step8_linksrechts.build()
            O=scene.cam_reset(8)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 9: 
            name='scene 9 - achterkant a'
            scene.start_scene(name)
            step9_achter.build()
            O=scene.cam_reset(91)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            name='scene 9 - achterkant b'
            O=scene.cam_reset(92)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 10: 
            name='scene 10 - deurpost a'
            scene.start_scene(name)
            step10_deurpost.build()
            O=scene.cam_reset(101)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            name='scene 10 - deurpost b'
            O=scene.cam_reset(102)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 11: 
            name='scene 11 - deur'
            scene.start_scene(name)
            step11_deur.build()
            O=scene.cam_reset(11)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 12: 
            name='scene 12 compleet'
            scene.start_scene(name)
            step12_compleet.build()
            O=scene.cam_reset(12)
            #arrow.origin(O)
            scene.capture(name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
    
main()