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
    breedte_kast=cfg.breedte_kast
    dikte_plank=cfg.dikte_plank
    dikte_rib=cfg.dikte_rib

    vlonder_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/150)):
            vlonder_extra=vlonder_extra+1

    if vlonder_extra== 0:
        breedte_vlonder=breedte_kast-2*dikte_plank-dikte_rib/2.
        vlonderlist=vlonder_plaatsen(breedte_vlonder,0)

    elif vlonder_extra == 1:
        breedte_vlonder=(breedte_kast-2*dikte_plank)/2.-dikte_rib/2.
        uxlinks=(breedte_kast-dikte_plank)/2.
        uxrechts=-uxlinks
        vlonderlist=vlonder_plaatsen(breedte_vlonder,uxlinks)
        vlonderlist=vlonderlist+vlonder_plaatsen(breedte_vlonder,uxrechts)

    elif vlonder_extra == 2:
        breedte_vlonder=(breedte_kast-2*dikte_plank)/3.-dikte_rib/2.
        uxlinks=(breedte_kast-dikte_plank)/3.
        uxmidden=0.
        uxrechts=-uxlinks
        vlonderlist=vlonder_plaatsen(breedte_vlonder,uxlinks)
        vlonderlist=vlonderlist+vlonder_plaatsen(breedte_vlonder,uxmidden)
        vlonderlist=vlonderlist+vlonder_plaatsen(breedte_vlonder,uxrechts)
            
    elif vlonder_extra >= 3:
        breedte_vlonder=(breedte_kast-2*dikte_plank)/4.-dikte_rib/2.
        uxlinkslinks=(breedte_kast-dikte_plank)/2.
        uxlinks=(breedte_kast-dikte_plank)/4.
        uxrechts=-uxlinks
        uxrechtsrechts=-uxlinkslinks
        vlonderlist=vlonder_plaatsen(breedte_vlonder,uxlinkslinks)
        vlonderlist=vlonderlist+vlonder_plaatsen(breedte_vlonder,uxlinks)
        vlonderlist=vlonderlist+vlonder_plaatsen(breedte_vlonder,uxrechts)
        vlonderlist=vlonderlist+vlonder_plaatsen(breedte_vlonder,uxrechtsrechts)
    
    return vlonderlist
    
def vlonder_plaatsen(lengte,ux):
    hoogte_kast=cfg.hoogte_kast
    breedte_kast=cfg.breedte_kast
    diepte_kast=cfg.diepte_kast
    dikte_plank=cfg.dikte_plank
    
    hoogte_voet=cfg.hoogte_voet
    
    breedte_rib=cfg.breedte_rib
    lengte_rib=cfg.lengte_rib
    dikte_rib=cfg.dikte_rib
    
    niveaus=cfg.niveaus
    plank_hoogte=cfg.plankhoogte
    
    ph=0
    for niveau in range(niveaus):
        ph=ph+plank_hoogte[niveau]
        uz=ph+dikte_plank/2.
        Vlonder=vlonder(lengte,ux,uz)
        if niveau == 0:
            Vlonderlist=Vlonder
        else:
            Vlonderlist=Vlonderlist+Vlonder

    return Vlonderlist

def vlonder(lengte_vlonder,ux,uz):
    Balken=[]
    Breedtes=[]
    
    diepte_kast=cfg.diepte_kast
    breedte_plank=cfg.breedte_plank
    lengte_plank=cfg.lengte_plank
    dikte_plank=cfg.dikte_plank
    breedte_kast=cfg.breedte_kast
    #hoogte_voet=cfg.hoogte_voet

    breedte_rib=cfg.breedte_rib
    lengte_rib=cfg.lengte_rib
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