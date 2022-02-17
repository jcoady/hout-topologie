#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:01:59 2022

@author: windhoos
"""

from onderdelen import config as cfg
from time import sleep

def update():
    sleep(.5)
    #print('update - sliders_update ',cfg.sliders_update,' sliders ',  cfg.sliders)
    if cfg.sliders != cfg.sliders_update:
        #print(cfg.sliders)
        #print(cfg.sliders_update)
        cfg.sliders = cfg.sliders_update
        cfg.niveaus = len(cfg.sliders)
        #print(cfg.sliders)
        #print(cfg.sliders_update)
        plankhoogte = []
        for i in range(len(cfg.sliders)):
            plankhoogte.append(cfg.sliders[i][1])
        cfg.plankhoogte=plankhoogte
    else:
        sleep(.5)
        print('pause')