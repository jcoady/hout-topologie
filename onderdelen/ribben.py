#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 18:14:51 2022

@author: windhoos
"""

import plank as p
import config as cfg

def maak():
    hoogte_kast=cfg.hoogte_kast
    breedte_kast=cfg.breedte_kast
    diepte_kast=cfg.diepte_kast
    dikte_plank=cfg.dikte_plank
    
    hoogte_voet=cfg.hoogte_voet
    
    breedte_rib=cfg.breedte_rib
    lengte_rib=cfg.lengte_rib
    dikte_rib=cfg.dikte_rib
    
    Ribben=[]
    #bereken hoeveelheid voeten
    rib_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/170)):
            rib_extra=rib_extra+1

    #rib1
    r1=p.plank(lengte_rib,breedte_rib,dikte_rib)
    print(r1.lengte,r1.breedte,r1.dikte)
    r1.plank_zagen(diepte_kast-2*dikte_plank,breedte_rib,dikte_rib)
    r1.aantal=2+rib_extra
    rx,ry,rz=0,0,90
    ux=breedte_kast/2.-dikte_plank-dikte_rib/2.
    uy=0
    uz=hoogte_voet+dikte_plank+dikte_rib/2.
    sx,sy,sz=1,1,1
    r1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    rib1=r1.balk()
    Ribben.append(rib1)
    
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