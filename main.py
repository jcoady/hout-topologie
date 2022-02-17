#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:40:57 2022

@author: windhoos
"""

<<<<<<< Updated upstream
from onderdelen import input_data, voeten, onderstel, ribben, zeiplanken, achterplank, vlonders, achterrib, voorkant
=======
from onderdelen import input_data, voeten, onderstel, ribben, zeiplanken, achterplank, vlonders, achterrib, voorkant,updater
>>>>>>> Stashed changes
from onderdelen import config as cfg
from onderdelen import plotter
import time

def main():
    input_data.input_data()
    
    cfg.start = time.time()
    
    Voeten=voeten.maak()
    Onderstel=onderstel.maak()
    Zeiden=zeiplanken.maak()
    Achterplank=achterplank.maak()
    Voorkant,Scharnier=voorkant.maak(0)
    Voorkant120,Scharnier120=voorkant.maak(120)
    
    Ribben=ribben.maak()
<<<<<<< Updated upstream
    Zeiden=zeiplanken.maak()
    Achterplank=achterplank.maak()
    Vlonders=vlonders.maak()
    Achterrib=achterrib.maak()
    Voorkant,Scharnier=voorkant.maak(0)
    
    #plotten
    amax=max(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast)

    #plotter.multiplot(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast,amax,'iso',Scharnier,Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant)
    #plotter.mayaviplot(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast,amax,'iso',Scharnier,Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant)
    plotter.vpythonplot(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast,amax,'iso',Scharnier,Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant)
    
=======
    Achterrib=achterrib.maak()
    Vlonders=vlonders.maak()
    
    #plotten
    amax=max(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast)
    
    #plotter.multiplot(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast,amax,'iso',Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Scharnier)
    #plotter.mayaviplot(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast,amax,'iso',Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Scharnier)
    plotter.vpythonplot(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast,amax,'iso',Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Voorkant120, Scharnier, Scharnier120)
    
    finish = False
    while finish != True:
        Ribben=ribben.maak()
        Achterrib=achterrib.maak()
        Vlonders=vlonders.maak()
        
        #plotter.multiplot(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast,amax,'iso',Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Scharnier)
        #plotter.mayaviplot(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast,amax,'iso',Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Scharnier)
        plotter.plotniveau(Ribben,Vlonders,Achterrib)

        updater.update()
        print(cfg.sliders)
        print(cfg.sliders_update)
    
>>>>>>> Stashed changes
main()