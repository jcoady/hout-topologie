#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:49 2022

@author: windhoos
"""

from onderdelen import plank as p
from onderdelen import config as cfg

def maak():
    breedte_kast=cfg.breedte_kast
    hoogte_voet=cfg.hoogte_voet
    diepte_kast=cfg.diepte_kast
    dikte_plank=cfg.dikte_plank
    
    Voeten=[]
    #bereken hoeveelheid voeten
    voet_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/150)):
            voet_extra=voet_extra+1

    v=hoogte_voet

    #voet1
    v1=p.plank(v,v,v)
    v1.aantal=4+voet_extra
    rx,ry,rz=0,0,0
    ux,uy,uz=breedte_kast/2.-v/2.-dikte_plank,diepte_kast/2.-v/2.-dikte_plank,v/2.
    sx,sy,sz=1,1,1
    v1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet1=v1.balk()
    Voeten.append(voet1)
    
    #voet2
    v2=p.plank(v,v,v)
    rx,ry,rz=0,0,0
    ux,uy,uz=breedte_kast/2.-v/2.-dikte_plank,-diepte_kast/2.+v/2.+dikte_plank,v/2.
    sx,sy,sz=1,1,1
    v2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet2=v2.balk()
    Voeten.append(voet2)
    
    #voet3
    v3=p.plank(v,v,v)
    rx,ry,rz=0,0,0
    ux,uy,uz=-breedte_kast/2.+v/2.+dikte_plank,-diepte_kast/2.+v/2.+dikte_plank,v/2.
    sx,sy,sz=1,1,1
    v3.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet3=v3.balk()
    Voeten.append(voet3)
    
    #voet4
    v4=p.plank(v,v,v)
    rx,ry,rz=0,0,0
    ux,uy,uz=-breedte_kast/2.+v/2.+dikte_plank,diepte_kast/2.-v/2.-dikte_plank,v/2.
    sx,sy,sz=1,1,1
    v4.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet4=v4.balk()
    Voeten.append(voet4)
    
    if voet_extra > 0:
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
            
        elif voet_extra == 3:
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
        
        ve2=p.plank(v,v,v)
        rx,ry,rz=0,0,0
        if voet_extra == 1:
            ve2=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            ux=0.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2=ve2.balk()
            Voeten.append(voete2)
        elif voet_extra == 2:
            ve2=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            ux=breedte_kast/6.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2=ve2.balk()
            Voeten.append(voete2)
            
            ve2=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            ux=-breedte_kast/6.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2=ve2.balk()
            Voeten.append(voete2)
            
        elif voet_extra == 3:
            ve2=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            ux=0.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2=ve2.balk()
            Voeten.append(voete2)
            
            ve2=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            ux=breedte_kast/4.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2=ve2.balk()
            Voeten.append(voete2)
            
            ve2=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            ux=-breedte_kast/4.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2=ve2.balk()
            Voeten.append(voete2)

    return Voeten