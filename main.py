#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:40:57 2022

@author: windhoos
"""

from onderdelen import input_data, voeten, onderstel, ribben, zeiplanken, achterplank, vlonders, achterrib, voorkant, updater
from onderdelen import config as cfg
from onderdelen import plotter

#from importlib import reload

import time

def main():
    plotter.build_scene()
    wait=True
    while cfg.reset_loop == True:
        print('reloop')
        while wait == True:
            print('wait')
            time.sleep(1)
            if cfg.build_state == True:
                wait = False
        cfg.build_state = False
        wait=True
            
        input_data.input_data()
            
        Voeten=voeten.maak()
        Onderstel=onderstel.maak()
        Zeiden=zeiplanken.maak()
        Achterplank=achterplank.maak()
        Voorkant,Scharnier=voorkant.maak(0)
        Voorkant120,Scharnier120=voorkant.maak(120)
        
        Ribben=ribben.maak()
        Achterrib=achterrib.maak()
        Vlonders=vlonders.maak()
        
        #plotten
        amax=max(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast)
        
        plotter.vpythonplot(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast,amax,'iso',Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Voorkant120, Scharnier, Scharnier120)
        
        finish = False
        while finish != True:
            print('wait2')
            cfg.df_ribben=[]
            Ribben=ribben.maak()
            Achterrib=achterrib.maak()
            cfg.df_vlonders=[]
            Vlonders=vlonders.maak()
                
            plotter.plotniveau(Ribben,Vlonders,Achterrib)
    
            updater.update()
            
            if cfg.reset == True:
                print('reset triggered')
                finish = True
                
            if cfg.finish_drawing == True:
                cfg.reset_loop == False
                finish = True
        #reload(cfg)
main()