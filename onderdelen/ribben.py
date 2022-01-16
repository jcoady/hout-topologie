#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 18:14:51 2022

@author: windhoos
"""

import plank as p
import config as cfg

def maak():
    breedte_kast=cfg.breedte_kast
    dikte_plank=cfg.dikte_plank
    dikte_rib=cfg.dikte_rib
    
    riblist=[]
    riblist.append(rib(  breedte_kast/2.-dikte_plank-dikte_rib/2.))

    rib_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/170)):
            rib_extra=rib_extra+1
    
    if rib_extra > 0:
        for r in range(rib_extra):
            if rib_extra == 1:
                riblist.append(rib(0))

            elif rib_extra == 2:
                riblist.append(rib( breedte_kast/6.))
                riblist.append(rib(-breedte_kast/6.))
                
            elif rib_extra >= 3:
                riblist.append(rib(0))
                riblist.append(rib( breedte_kast/4.))
                riblist.append(rib(-breedte_kast/4.))
                
    riblist.append(rib(-(breedte_kast/2.-dikte_plank-dikte_rib/2.)))
    
    return riblist
    
def rib(ux):
    
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
    
    Ribben=[]
    #bereken hoeveelheid voeten
    rib_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/170)):
            rib_extra=rib_extra+1

    #rib1
    r1=p.plank(lengte_rib,breedte_rib,dikte_rib)

    r1.plank_zagen(diepte_kast-2*dikte_plank-2*dikte_rib,breedte_rib,dikte_rib)
    r1.aantal=2+rib_extra
    rx,ry,rz=0,0,90
    #ux=breedte_kast/2.-dikte_plank-dikte_rib/2.
    uy=0
    uz=hoogte_voet+dikte_plank+dikte_rib/2.
    sx,sy,sz=1,1,1
    r1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    rib1=r1.balk()
    Ribben.append(rib1)
    
    #rib2
    r2=p.plank(lengte_rib,breedte_rib,dikte_rib)

    r2.plank_zagen(hoogte_kast-dikte_plank-hoogte_voet,breedte_rib,dikte_rib)
    r1.aantal=r1.aantal+1
    rx,ry,rz=0,90,0
    #ux=breedte_kast/2.-dikte_plank-dikte_rib/2.
    uy=diepte_kast/2.-dikte_plank-dikte_rib/2.
    uz=hoogte_voet+dikte_plank+(hoogte_kast-dikte_plank-hoogte_voet)/2.
    sx,sy,sz=1,1,1
    r2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    rib2=r2.balk()
    Ribben.append(rib2)
    
    #rib3
    r3=p.plank(lengte_rib,breedte_rib,dikte_rib)

    r3.plank_zagen(hoogte_kast-dikte_plank-hoogte_voet,breedte_rib,dikte_rib)
    r1.aantal=r1.aantal+1
    rx,ry,rz=0,90,0
    #ux=breedte_kast/2.-dikte_plank-dikte_rib/2.
    uy=-(diepte_kast/2.-dikte_plank-dikte_rib/2.)
    uz=hoogte_voet+dikte_plank+(hoogte_kast-dikte_plank-hoogte_voet)/2.
    sx,sy,sz=1,1,1
    r3.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    rib3=r3.balk()
    Ribben.append(rib3)
    
    #rib4
    r4=p.plank(lengte_rib,breedte_rib,dikte_rib)

    r4.plank_zagen(diepte_kast-2*dikte_plank-2*dikte_rib,breedte_rib,dikte_rib)
    r1.aantal=r1.aantal+1
    rx,ry,rz=0,0,90
    #ux=breedte_kast/2.-dikte_plank-dikte_rib/2.
    uy=0
    uz=hoogte_kast-dikte_rib/2.
    sx,sy,sz=1,1,1
    r4.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    rib4=r4.balk()
    Ribben.append(rib4)
    
    ph=0
    for niveau in range(niveaus):
        ph=ph+plank_hoogte[niveau]
        r5=p.plank(lengte_rib,breedte_rib,dikte_rib)

        r5.plank_zagen(diepte_kast-2*dikte_plank-2*dikte_rib,breedte_rib,dikte_rib)
        r1.aantal=r1.aantal+1
        rx,ry,rz=0,0,90
        #ux=breedte_kast/2.-dikte_plank-dikte_rib/2.
        uy=0
        uz=ph-dikte_rib/2.
        sx,sy,sz=1,1,1
        r5.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        rib5=r5.balk()
        Ribben.append(rib5)
        
    
    '''
    #voet2
    v2=p.plank(v,v,v)
    rx,ry,rz=0,0,0
    ux,uy,uz=breedte_kast/2.-v/2.-dikte_plank,-diepte_kast/2.+v/2.+dikte_plank,v/2.
    sx,sy,sz=1,1,1
    v2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet2=v2.balk()
    Voeten.append(voet2)
    
    if voet_extra > 0:
        for voet in range(voet_extra):
            ve1=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            if voet_extra == 1:
                ve1=p.plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=0.
                uy=diepte_kast/2.-v/2.-dikte_plank
                uz=v/2.
                sx,sy,sz=1,1,1
                ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete1=ve1.balk()
                Voeten.append(voete1)
            elif voet_extra == 2:
                ve1=p.plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=breedte_kast/6.
                uy=diepte_kast/2.-v/2.-dikte_plank
                uz=v/2.
                sx,sy,sz=1,1,1
                ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete1=ve1.balk()
                Voeten.append(voete1)
                
                ve1=p.plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=-breedte_kast/6.
                uy=diepte_kast/2.-v/2.-dikte_plank
                uz=v/2.
                sx,sy,sz=1,1,1
                ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete1=ve1.balk()
                Voeten.append(voete1)
                
            elif voet_extra >= 3:
                ve1=p.plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=0
                uy=diepte_kast/2.-v/2.-dikte_plank
                uz=v/2.
                sx,sy,sz=1,1,1
                ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete1=ve1.balk()
                Voeten.append(voete1)
                
                ve1=p.plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=breedte_kast/4.
                uy=diepte_kast/2.-v/2.-dikte_plank
                uz=v/2.
                sx,sy,sz=1,1,1
                ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete1=ve1.balk()
                Voeten.append(voete1)
                
                ve1=p.plank(v,v,v)
                rx,ry,rz=0,0,0
                ux=-breedte_kast/4.
                uy=diepte_kast/2.-v/2.-dikte_plank
                uz=v/2.
                sx,sy,sz=1,1,1
                ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
                voete1=ve1.balk()
                Voeten.append(voete1)
    '''
    return Ribben