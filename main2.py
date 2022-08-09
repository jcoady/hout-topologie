#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:26:30 2022

@author: windhoos
"""

from latex import get_excel, scene, step1_feet_bottom, step2_rib_bottom, step3_ladder, step4_geraamte, step5_achterrib, step6_vlonders, step7_boven, step8_linksrechts, step9_achter, step10_deurpost, step11_deur, step12_compleet
from latex import arrow
import time
import os
from latex import opencv as crop
from latex import stuklijst

def main():
    parent_dir = '/home/windhoos/hout-topologie/users'
    directory = '09-08-2022-22-35-17-test'
    path = os.path.join(parent_dir, directory)
    lang = 'EN'
    
    get_excel.build(path)
    
    bijsnijden = True
    
    runlist=[]
    if runlist == []:
        runlist=[1,2,3,4,5,6,7,8,9,10,11,12]
    for i in range(len(runlist)):
        run=runlist[i]
        if run == 1:
            name='scene 1 - bottom'
            scene.start_scene(name)
            step1_feet_bottom.build(path,lang)
            O=scene.cam_reset(1)
            #arrow.origin(O)
            scene.capture(path,name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 2:    
            name='scene 2 - bottom rib'
            scene.start_scene(name)
            step2_rib_bottom.build(path,lang)
            O=scene.cam_reset(2)
            #arrow.origin(O)
            scene.capture(path,name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 3:
            name='scene 3 - ladder'
            scene.start_scene(name)
            step3_ladder.build(path,lang)
            O=scene.cam_reset(3)
            #arrow.origin(O)
            scene.capture(path,name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 4:    
            name='scene 4 - geraamte'
            scene.start_scene(name)
            step4_geraamte.build(path,lang)
            O=scene.cam_reset(4)
            #arrow.origin(O)
            scene.capture(path,name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 5: 
            name='scene 5 - achterrib a'
            scene.start_scene(name)
            step5_achterrib.build(path,lang)
            O=scene.cam_reset(51)
            #arrow.origin(O)
            scene.capture(path,name)
            time.sleep(1)
            name='scene 5 - achterrib b'
            O=scene.cam_reset(52)
            #arrow.origin(O)
            scene.capture(path, name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 6: 
            name='scene 6 - vlonders a'
            scene.start_scene(name)
            step6_vlonders.build(path,lang)
            O=scene.cam_reset(61)
            #arrow.origin(O)
            scene.capture(path, name)
            time.sleep(1)
            name='scene 6 - vlonders b'
            O=scene.cam_reset(62)
            #arrow.origin(O)
            scene.capture(path, name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 7: 
            name='scene 7 - boven'
            scene.start_scene(name)
            step7_boven.build(path,lang)
            O=scene.cam_reset(7)
            #arrow.origin(O)
            scene.capture(path, name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 8: 
            name='scene 8 - links/rechts'
            scene.start_scene(name)
            step8_linksrechts.build(path,lang)
            O=scene.cam_reset(8)
            #arrow.origin(O)
            scene.capture(path, name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 9: 
            name='scene 9 - achterkant'
            scene.start_scene(name)
            step9_achter.build(path,lang)
            #O=scene.cam_reset(91)
            #arrow.origin(O)
            #scene.capture(path, name)
            time.sleep(1)
            #name='scene 9 - achterkant'
            O=scene.cam_reset(92)
            #arrow.origin(O)
            scene.capture(path, name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 10: 
            name='scene 10 - deurpost a'
            scene.start_scene(name)
            step10_deurpost.build(path,lang)
            O=scene.cam_reset(101)
            #arrow.origin(O)
            scene.capture(path,name)
            time.sleep(1)
            name='scene 10 - deurpost b'
            O=scene.cam_reset(102)
            scene.capture(path, name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 11: 
            name='scene 11 - deur'
            scene.start_scene(name)
            step11_deur.build(path,lang)
            O=scene.cam_reset(11)
            #arrow.origin(O)
            scene.capture(path, name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
        if run == 12: 
            name='scene 12 - compleet'
            scene.start_scene(name)
            step12_compleet.build(path,lang)
            O=scene.cam_reset(12)
            #arrow.origin(O)
            scene.capture(path, name)
            time.sleep(1)
            scene.delete()
            time.sleep(1)
            
    print('Rendering finished')
            
    input(f"Kopieer bestanden naar {path}")
        
    if bijsnijden == True:
        crop.cut(path)
        crop.canvas(path)
        print('Cropping finished')
        
    stuklijst.build(path,lang)

main()