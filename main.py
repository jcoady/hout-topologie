#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:40:57 2022

@author: windhoos
"""

from onderdelen import input_data, voeten, onderstel, ribben
from onderdelen import config as cfg
from onderdelen import plotter

def main():
    input_data.input_data()
    
    Voeten=voeten.maak()
    Onderstel=onderstel.maak()
    Ribben=ribben.maak()
    
    #plotten
    print(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast)
    amax=max(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast)
    print(amax)
    
    plotter.multiplot(cfg.breedte_kast,cfg.hoogte_kast,cfg.diepte_kast,amax,'iso',Voeten,Onderstel,Ribben[0])
main()