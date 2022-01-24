#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 18:14:51 2022

@author: windhoos
"""

from onderdelen import plank as p
from onderdelen import config as cfg

def maak():
    breedte_kast=cfg.breedte_kast
    dikte_plank=cfg.dikte_plank
    dikte_rib=cfg.dikte_rib
    
    riblist=[]

    rib_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/150)):
            rib_extra=rib_extra+1
    
    if rib_extra == 0:
        #lengte=(breedte_kast-2*dikte_plank-(2+rib_extra)*dikte_rib)/(1+rib_extra)
        lengte=breedte_kast-2*dikte_plank-2*dikte_rib
        ux=0.
        
        riblist.append(rib(lengte,ux))
        
    elif rib_extra == 1:
        #lengte=(breedte_kast-2*dikte_plank-(2+rib_extra)*dikte_rib)/(1+rib_extra)
        lengte=(breedte_kast-2*dikte_plank-3*dikte_rib)/2.
        uxl=lengte/2.+dikte_rib/2.
        uxr=-uxl
        
        riblist.append(rib(lengte,uxl))
        riblist.append(rib(lengte,uxr))

    elif rib_extra == 2:
        #lengte=(breedte_kast-2*dikte_plank-(2+rib_extra)*dikte_rib)/(1+rib_extra)
        lengte=(breedte_kast-2*dikte_plank-4*dikte_rib)/3.
        ux=0.
        riblist.append(rib(lengte,ux))
        uxl=lengte/2.+dikte_rib+lengte/2.
        uxr=-uxl
        
        riblist.append(rib(lengte,uxl))
        riblist.append(rib(lengte,uxr))
            
    elif rib_extra >= 3:
        #lengte=(breedte_kast-2*dikte_plank-(2+rib_extra)*dikte_rib)/(1+3)
        lengte=(breedte_kast-2*dikte_plank-5*dikte_rib)/4.
        uxl=dikte_rib/2.+lengte/2.
        uxll=dikte_rib/2.+lengte+dikte_rib+lengte/2.
        uxr=-uxl
        uxrr=-uxll
        
        riblist.append(rib(lengte,uxl))
        riblist.append(rib(lengte,uxll))
        riblist.append(rib(lengte,uxr))
        riblist.append(rib(lengte,uxrr))

    combined_riblist=[]
    for i in range(len(riblist)):
        combined_riblist=combined_riblist+riblist[i]
    
    return combined_riblist
    
def rib(lengte,ux):
    #hoogte_kast=cfg.hoogte_kast
    #breedte_kast=cfg.breedte_kast
    diepte_kast=cfg.diepte_kast
    dikte_plank=cfg.dikte_plank
    
    #hoogte_voet=cfg.hoogte_voet
    
    breedte_rib=cfg.breedte_rib
    lengte_rib=cfg.lengte_rib
    dikte_rib=cfg.dikte_rib
    
    niveaus=cfg.niveaus
    plank_hoogte=cfg.plankhoogte
    
    Ribben=[]
    
    uy=-(diepte_kast-2*dikte_plank)/2.+dikte_rib/2.
    
    ph=0
    for niveau in range(niveaus):
        #ph=ph+plank_hoogte[niveau]
        ph=plank_hoogte[niveau]
        r1=p.plank(lengte_rib,breedte_rib,dikte_rib)

        r1.plank_zagen(lengte,breedte_rib,dikte_rib)
        rx,ry,rz=0,0,0
        uz=ph-dikte_rib/2.
        sx,sy,sz=1,1,1
        r1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        rib1=r1.balk()
        Ribben.append(rib1)

    return Ribben