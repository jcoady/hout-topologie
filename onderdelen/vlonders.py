#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 18:14:51 2022

@author: windhoos
"""

from onderdelen import plank as p
from onderdelen import config as cfg
from math import floor
    
def maak():
    lengte=cfg.breedte_kast-2*cfg.dikte_plank-1.
    #hoogte_kast=cfg.hoogte_kast
    #breedte_kast=cfg.breedte_kast
    #diepte_kast=cfg.diepte_kast
    dikte_plank=cfg.dikte_plank
    
    #hoogte_voet=cfg.hoogte_voet
    
    #breedte_rib=cfg.breedte_rib
    #lengte_rib=cfg.lengte_rib
    #dikte_rib=cfg.dikte_rib
    
    niveaus=cfg.niveaus
    plank_hoogte=cfg.plankhoogte
    
    ph=0
    for niveau in range(niveaus):
        #ph=ph+plank_hoogte[niveau]
        ph=plank_hoogte[niveau]
        uz=ph-dikte_plank/2.
        Vlonder=vlonder(lengte,uz)
        if niveau == 0:
            Vlonderlist=Vlonder
        else:
            Vlonderlist=Vlonderlist+Vlonder

    return Vlonderlist

def vlonder(lengte_vlonder,uz):
    Balken=[]
    Breedtes=[]
    
    diepte_kast=cfg.diepte_kast
    breedte_plank=cfg.breedte_plank
    lengte_plank=cfg.lengte_plank
    dikte_plank=cfg.dikte_plank
    #breedte_kast=cfg.breedte_kast
    #hoogte_voet=cfg.hoogte_voet

    #breedte_rib=cfg.breedte_rib
    #engte_rib=cfg.lengte_rib
    dikte_rib=cfg.dikte_rib
    
    d=float(diepte_kast-2*dikte_plank-2*dikte_rib)
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
    
    ux=0.
    uy=diepte_kast/2.- dikte_plank - dikte_rib

    Breedtes.reverse()
    for planken in range(len(Breedtes)):
        plank=p.plank(lengte_plank,breedte_plank,dikte_plank)
        plank.plank_zagen(lengte_vlonder,Breedtes[planken],dikte_plank)
        rx,ry,rz=0,0,0

        if planken == 0:
            uy = uy - Breedtes[planken]/2.
        else:
            uy = uy - Breedtes[planken]/2. - Breedtes[planken-1]/2.
        
        sx,sy,sz=1,1,1
        plank.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        balk=plank.balk()
        Balken.append(balk)
        
    return Balken
    