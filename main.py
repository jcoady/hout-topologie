#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:40:57 2022

@author: windhoos
"""

from onderdelen import input_data, voeten, onderstel, ribben, zeiplanken, achterplank, vlonders, achterrib, voorkant
from onderdelen import config as cfg
from onderdelen import plotter
import time

def main():
    input_data.input_data()
    
    cfg.start = time.time()
    
    Voeten=voeten.maak()
    Onderstel=onderstel.maak()
    Ribben=ribben.maak()
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
    
main()