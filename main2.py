#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:26:30 2022

@author: windhoos
"""

from latex import get_excel, scene, step1_feet_bottom

def main():
    get_excel.build()
    scene.start_scene()
    step1_feet_bottom.build()
    scene.cam_reset()
    scene.capture('step-1-bottom.png')
main()