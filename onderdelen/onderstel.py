#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:49 2022

@author: windhoos
"""

from onderdelen import plank as p
from onderdelen import config as cfg
from math import floor

def maak():
    Breedtes=[]
    Balken=[]
    
    diepte_kast=cfg.diepte_kast
    breedte_plank=cfg.breedte_plank
    lengte_plank=cfg.lengte_plank
    dikte_plank=cfg.dikte_plank
    breedte_kast=cfg.breedte_kast
    hoogte_voet=cfg.hoogte_voet
    
    d=float(diepte_kast-2*dikte_plank)
    b=float(breedte_plank)
    
    fractie_planken=d/b
    hele_planken=int(floor(fractie_planken))
    over=fractie_planken-hele_planken
    
    if ((over > 0.0) and (hele_planken > 1)):
        hele_planken=hele_planken-1
        for planken in range(hele_planken):
            Breedtes.append(b)
        if hele_planken > 0:
            over=(b*(over+1.)/2.)
            Breedtes.append(over)
            Breedtes.append(over)
        else:
            over=(b*(over+1.)/2.)
            Breedtes.append(over)
            
    elif over > 0.0:
            over=(b*(over+1.)/2.)
            Breedtes.append(over)
            Breedtes.append(over)
    else:
        for planken in range(hele_planken):
            Breedtes.append(b)
    
    uy=diepte_kast/2.- dikte_plank

    Breedtes.reverse()
    for planken in range(len(Breedtes)):
        plank=p.plank(lengte_plank,breedte_plank,dikte_plank)
        plank.plank_zagen(breedte_kast-2*dikte_plank,Breedtes[planken],dikte_plank)
        rx,ry,rz=0,0,0
        ux=0.

        if planken == 0:
            uy = uy - Breedtes[planken]/2.
        else:
            uy = uy - Breedtes[planken]/2. - Breedtes[planken-1]/2.
        uz=hoogte_voet+dikte_plank/2.
        sx,sy,sz=1,1,1
        plank.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        balk=plank.balk()
        Balken.append(balk)
        
    return Balken