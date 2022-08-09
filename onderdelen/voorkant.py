#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 18:14:51 2022

@author: windhoos
"""

from onderdelen import plank as p
from onderdelen import config as cfg

from math import floor,radians,degrees,cos,sin

import pandas as pd

def maak(theta):
    
    #hoogte_kast=cfg.hoogte_kast
    breedte_kast=cfg.breedte_kast
    #diepte_kast=cfg.diepte_kast
    
    dikte_plank=cfg.dikte_plank
    
    dikte_rib=cfg.dikte_rib
    
    plank_list=[]
    scharnier_list=[]
    
    nummer = 0
    
    if dikte_plank+dikte_rib <= 7.5:
        voorplank_breedte = 7.5
    else:
        voorplank_breedte = dikte_plank+dikte_rib
        
    cfg.voorplank_breedte = voorplank_breedte
    
    rib_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/150)):
            rib_extra=rib_extra+1
        if rib_extra > 3:
            rib_extra=3
            
    u0=-breedte_kast/2.+voorplank_breedte
    ui=(breedte_kast-voorplank_breedte)/(rib_extra+1)

    plank_list.append(voorplank(u0-voorplank_breedte,theta,nummer))
    plank_list.append(voorplank(-u0,theta,nummer))
    #plank_list.append(deur(breedte_kast/2. - voorplank_breedte))
    
    
    if rib_extra == 0:
        nummer=nummer+1
        plank_list.append(deur(u0+ui*0,theta,nummer))
        plank_list.append(stut(u0+ui*0,theta,nummer))
        scharnier_list.append(scharnier(u0+ui*0,theta,nummer))
    
    elif rib_extra == 1:
        nummer=nummer+1
        #plank_list.append(deur(voorplank_breedte/2.))
        plank_list.append(deur(u0+ui*0,theta,nummer))
        plank_list.append(stut(u0+ui*0,theta,nummer))
        scharnier_list.append(scharnier(u0+ui*0,theta,nummer))
        nummer=nummer+1
        plank_list.append(deur(u0+ui*1,theta,nummer))
        plank_list.append(stut(u0+ui*1,theta,nummer))
        scharnier_list.append(scharnier(u0+ui*1,theta,nummer))
        plank_list.append(voorplank(u0+ui*1-voorplank_breedte,theta,nummer))

    elif rib_extra == 2:
        nummer=nummer+1
        #ux=(breedte_kast-dikte_plank*2-dikte_rib)/6.
        #plank_list.append(voorplank(ux))
        #plank_list.append(voorplank(-ux))
        #plank_list.append(deur(ux-voorplank_breedte/2.))
        #plank_list.append(deur(-ux+voorplank_breedte/2.))
        plank_list.append(deur(u0+ui*0,theta,nummer))
        plank_list.append(stut(u0+ui*0,theta,nummer))
        scharnier_list.append(scharnier(u0+ui*0,theta,nummer))
        nummer=nummer+1
        plank_list.append(deur(u0+ui*1,theta,nummer))
        plank_list.append(stut(u0+ui*1,theta,nummer))
        scharnier_list.append(scharnier(u0+ui*1,theta,nummer))
        nummer=nummer+1
        plank_list.append(deur(u0+ui*2,theta,nummer))
        plank_list.append(stut(u0+ui*2,theta,nummer))
        scharnier_list.append(scharnier(u0+ui*2,theta,nummer))
        nummer=nummer+1
        plank_list.append(voorplank(u0+ui*1-voorplank_breedte,theta,nummer-1))
        plank_list.append(voorplank(u0+ui*2-voorplank_breedte,theta,nummer))
            
    elif rib_extra >= 3:
        nummer=nummer+1
        #plank_list.append(voorplank(0))
        #plank_list.append(deur(voorplank_breedte/2.))
        #ux=(breedte_kast-dikte_plank*2-dikte_rib)/4.
        #plank_list.append(voorplank(ux))
        #plank_list.append(voorplank(-ux))
        #plank_list.append(deur(ux-voorplank_breedte/2.))
        #plank_list.append(deur(-ux+voorplank_breedte/2.))
        plank_list.append(deur(u0+ui*0,theta,nummer))
        plank_list.append(stut(u0+ui*0,theta,nummer))
        scharnier_list.append(scharnier(u0+ui*0,theta,nummer))
        nummer=nummer+1
        plank_list.append(deur(u0+ui*1,theta,nummer))
        plank_list.append(stut(u0+ui*1,theta,nummer))
        scharnier_list.append(scharnier(u0+ui*1,theta,nummer))
        nummer=nummer+1
        plank_list.append(deur(u0+ui*2,theta,nummer))
        plank_list.append(stut(u0+ui*2,theta,nummer))
        scharnier_list.append(scharnier(u0+ui*2,theta,nummer))
        nummer=nummer+1
        plank_list.append(deur(u0+ui*3,theta,nummer))
        plank_list.append(stut(u0+ui*3,theta,nummer))
        scharnier_list.append(scharnier(u0+ui*3,theta,nummer))
        plank_list.append(voorplank(u0+ui*1-voorplank_breedte,theta,nummer-2))
        plank_list.append(voorplank(u0+ui*2-voorplank_breedte,theta,nummer-1))
        plank_list.append(voorplank(u0+ui*3-voorplank_breedte,theta,nummer))
    
    combined_list=[]
    for i in range(len(plank_list)):
        combined_list=combined_list+plank_list[i]
        
    combined_list2=[]
    for i in range(len(scharnier_list)):
        combined_list2=combined_list2+scharnier_list[i]
    
    return combined_list,combined_list2
    
def voorplank(ux,theta,nummer):
    hoogte_kast=cfg.hoogte_kast
    #breedte_kast=cfg.breedte_kast
    diepte_kast=cfg.diepte_kast
    
    dikte_plank=cfg.dikte_plank
    
    hoogte_voet=cfg.hoogte_voet
    
    #breedte_rib=cfg.breedte_rib
    #lengte_rib=cfg.lengte_rib
    dikte_rib=cfg.dikte_rib
    
    Balken=[]
    
    if dikte_plank+dikte_rib <= 7.5:
        voorplank_breedte = 7.5
    else:
        voorplank_breedte = dikte_plank+dikte_rib
    
    plank=p.plank(cfg.lengte_plank,cfg.breedte_plank,cfg.dikte_plank)
    plank.plank_zagen(hoogte_kast-hoogte_voet,voorplank_breedte,dikte_plank)
    rx,ry,rz=0,90,90
    ux=ux+voorplank_breedte/2.
    uy=diepte_kast/2. - dikte_plank/2.
    uz=hoogte_voet+(hoogte_kast-hoogte_voet)/2.
    sx,sy,sz=1,1,1
    plank.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    balk=plank.balk()
    Balken.append(balk)
    if theta == 0:
        try:
            if cfg.df_voorkant == []:
                df_voorkant = pd.DataFrame({
                    "naam":         ['voorkant'],
                    "subnaam":      ['voorplank'],
                    "type":         ['plank'],
                    "nummer":       [0],
                    "lengte":       [hoogte_kast-hoogte_voet],
                    "breedte":      [voorplank_breedte],
                    "dikte":        [dikte_plank],
                    "xloc":         [ux],
                    "yloc":         [uy],
                    "zloc":         [uz],
                    "rx":           [rx],
                    "ry":           [ry],
                    "rz":           [rz],
                    "opmerking":    [nummer],
                    })
                cfg.df_voorkant=df_voorkant
                
        except ValueError:
                df_voorkant_append = pd.DataFrame({
                    "naam":         ['voorkant'],
                    "subnaam":      ['voorplank'],
                    "type":         ['plank'],
                    "nummer":       [cfg.df_voorkant.shape[0]],
                    "lengte":       [hoogte_kast-hoogte_voet],
                    "breedte":      [voorplank_breedte],
                    "dikte":        [dikte_plank],
                    "xloc":         [ux],
                    "yloc":         [uy],
                    "zloc":         [uz],
                    "rx":           [rx],
                    "ry":           [ry],
                    "rz":           [rz],
                    "opmerking":    [nummer],
                    })
            
                cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant_append],ignore_index=True)
                #cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant],ignore_index=True)
            
        #cfg.df_voorkant=df_voorkant

    return Balken

def deur(ux,theta,nummer):
    hoogte_kast=cfg.hoogte_kast
    breedte_kast=cfg.breedte_kast
    diepte_kast=cfg.diepte_kast
    lengte_plank=cfg.lengte_plank
    dikte_plank=cfg.dikte_plank
    breedte_plank=cfg.breedte_plank
    #dikte_rib=cfg.dikte_rib
    
    hoogte_voet=cfg.hoogte_voet
    
    voorplank_breedte = cfg.voorplank_breedte
    
    Breedtes=[]
    Balken=[]
    
    rib_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/150)):
            rib_extra=rib_extra+1
        if rib_extra > 3:
            rib_extra=3
    
    d=float((breedte_kast-((rib_extra+2)*voorplank_breedte))/(rib_extra+1)) -.5

    #d=float(breedte_kast-3*voorplank_breedte)/(rib_extra+1)-0.5
    
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
            
    Breedtes.reverse()
    
    ux0=ux
    uy0=diepte_kast/2.+dikte_plank/2.
    
    for planken in range(len(Breedtes)):
        plank=p.plank(lengte_plank,breedte_plank,dikte_plank)
        plank.plank_zagen(hoogte_kast-hoogte_voet,Breedtes[planken],dikte_plank)
        rx,ry,rz=90,90,0-theta
        uy=diepte_kast/2.-dikte_plank/2.
        uz=hoogte_voet+(hoogte_kast-hoogte_voet)/2.
    
        if planken == 0:
            ux = ux + Breedtes[planken]/2.
        else:
            ux = ux + Breedtes[planken]/2. + Breedtes[planken-1]/2.
            
        uxa,uya = rotate_point(ux, uy, ux0, uy0, theta)
                
        sx,sy,sz=1,1,1
        plank.transformatie(rx,ry,rz,uxa,uya,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        balk=plank.balk()
        Balken.append(balk)
        if theta == 0:
            try:
                if cfg.df_voorkant == []:
                    df_voorkant = pd.DataFrame({
                        "naam":         ['voorkant'],
                        "subnaam":      ['deur'],
                        "type":         ['plank'],
                        "nummer":       [0],
                        "lengte":       [hoogte_kast-hoogte_voet],
                        "breedte":      [round(Breedtes[planken],1)],
                        "dikte":        [dikte_plank],
                        "xloc":         [ux],
                        "yloc":         [uy],
                        "zloc":         [uz],
                        "rx":           [rx],
                        "ry":           [ry],
                        "rz":           [rz],
                        "opmerking":    [nummer],
                        })
                    cfg.df_voorkant=df_voorkant
                
            except ValueError:
                df_voorkant_append = pd.DataFrame({
                    "naam":         ['voorkant'],
                    "subnaam":      ['deur'],
                    "type":         ['plank'],
                    "nummer":       [cfg.df_voorkant.shape[0]],
                    "lengte":       [hoogte_kast-hoogte_voet],
                    "breedte":      [round(Breedtes[planken],1)],
                    "dikte":        [dikte_plank],
                    "xloc":         [ux],
                    "yloc":         [uy],
                    "zloc":         [uz],
                    "rx":           [rx],
                    "ry":           [ry],
                    "rz":           [rz],
                    "opmerking":    [nummer],
                    })
            
                cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant_append],ignore_index=True)
                #cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant],ignore_index=True)
        
    return Balken

def stut(ux,theta,nummer):
    hoogte_kast=cfg.hoogte_kast
    breedte_kast=cfg.breedte_kast
    diepte_kast=cfg.diepte_kast
    lengte_plank=cfg.lengte_plank
    dikte_plank=cfg.dikte_plank
    breedte_plank=cfg.breedte_plank
    #dikte_rib=cfg.dikte_rib
    
    hoogte_voet=cfg.hoogte_voet
    
    voorplank_breedte = cfg.voorplank_breedte
    
    Balken=[]
    
    rib_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/150)):
            rib_extra=rib_extra+1
        if rib_extra > 3:
            rib_extra=3
    
    d=float((breedte_kast-((rib_extra+2)*voorplank_breedte))/(rib_extra+1)) #- .5
    
    ux0=ux
    uy0=diepte_kast/2.+dikte_plank/2.
    
    ux = ux + d/2.
    
    if cfg.hoogte_kast <= 3*cfg.breedte_plank:
        for i in range(2):
            plank=p.plank(lengte_plank,breedte_plank,dikte_plank)
            #plank.plank_zagen(d*.9,breedte_plank,dikte_plank)
            plank.plank_zagen(d*1.0,breedte_plank,dikte_plank)
            rx,ry,rz=90,0,0-theta
            uy=diepte_kast/2.-dikte_plank * 3/2.
            if i ==0 :
                uz = (hoogte_kast-hoogte_voet) *1/3. + hoogte_voet
            elif i == 1:
                uz = (hoogte_kast-hoogte_voet) *2/3. + hoogte_voet
        
            uxa,uya = rotate_point(ux, uy, ux0, uy0, theta)
            
            sx,sy,sz=1,1,1
            plank.transformatie(rx,ry,rz,uxa,uya,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            balk=plank.balk()
            Balken.append(balk)
            if theta == 0:
                try:
                    if cfg.df_voorkant == []:
                        df_voorkant = pd.DataFrame({
                            "naam":         ['voorkant'],
                            "subnaam":      ['stut'],
                            "type":         ['plank'],
                            "nummer":       [0],
                            #"lengte":       [round(d*.9,1)],
                            "lengte":       [round(d*1.0,1)],
                            "breedte":      [breedte_plank],
                            "dikte":        [dikte_plank],
                            "xloc":         [uxa],
                            "yloc":         [uya],
                            "zloc":         [uz],
                            "rx":           [rx],
                            "ry":           [ry],
                            "rz":           [rz],
                            "opmerking":    [nummer],
                            })
                        cfg.df_voorkant=df_voorkant
                    
                except ValueError:
                    df_voorkant_append = pd.DataFrame({
                        "naam":         ['voorkant'],
                        "subnaam":      ['stut'],
                        "type":         ['plank'],
                        "nummer":       [cfg.df_voorkant.shape[0]],
                        #"lengte":       [round(d*.9,1)],
                        "lengte":       [round(d*1.0,1)],
                        "breedte":      [breedte_plank],
                        "dikte":        [dikte_plank],
                        "xloc":         [uxa],
                        "yloc":         [uya],
                        "zloc":         [uz],
                        "rx":           [rx],
                        "ry":           [ry],
                        "rz":           [rz],
                        "opmerking":    [nummer],
                        })
                
                    cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant_append],ignore_index=True)
                    #cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant],ignore_index=True)
        
    else:
        for i in range(3):
            plank=p.plank(lengte_plank,breedte_plank,dikte_plank)
            #plank.plank_zagen(d*.9,breedte_plank,dikte_plank)
            plank.plank_zagen(d*1.0,breedte_plank,dikte_plank)
            rx,ry,rz=90,0,0-theta
            uy=diepte_kast/2.-dikte_plank * 3/2.
            if i ==0 :
                uz = (hoogte_kast-hoogte_voet) /2. + hoogte_voet
            elif i == 1:
                uz = (hoogte_kast-hoogte_voet) /6. + hoogte_voet
            elif i == 2:
                uz = (hoogte_kast-hoogte_voet) * 5/6. + hoogte_voet
        
            uxa,uya = rotate_point(ux, uy, ux0, uy0, theta)
            
            sx,sy,sz=1,1,1
            plank.transformatie(rx,ry,rz,uxa,uya,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            balk=plank.balk()
            Balken.append(balk)
            if theta == 0:
                try:
                    if cfg.df_voorkant == []:
                        df_voorkant = pd.DataFrame({
                            "naam":         ['voorkant'],
                            "subnaam":      ['stut'],
                            "type":         ['plank'],
                            "nummer":       [0],
                            #"lengte":       [round(d*.9,1)],
                            "lengte":       [round(d*1.0,1)],
                            "breedte":      [breedte_plank],
                            "dikte":        [dikte_plank],
                            "xloc":         [uxa],
                            "yloc":         [uya],
                            "zloc":         [uz],
                            "rx":           [rx],
                            "ry":           [ry],
                            "rz":           [rz],
                            "opmerking":    [nummer],
                            })
                        cfg.df_voorkant=df_voorkant
                    
                except ValueError:
                    df_voorkant_append = pd.DataFrame({
                        "naam":         ['voorkant'],
                        "subnaam":      ['stut'],
                        "type":         ['plank'],
                        "nummer":       [cfg.df_voorkant.shape[0]],
                        #"lengte":       [round(d*.9,1)],
                        "lengte":       [round(d*1.0,1)],
                        "breedte":      [breedte_plank],
                        "dikte":        [dikte_plank],
                        "xloc":         [uxa],
                        "yloc":         [uya],
                        "zloc":         [uz],
                        "rx":           [rx],
                        "ry":           [ry],
                        "rz":           [rz],
                        "opmerking":    [nummer],
                        })
                
                    cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant_append],ignore_index=True)
                    #cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant],ignore_index=True)
        
    return Balken

def scharnier(ux,theta,nummer):
    hoogte_kast=cfg.hoogte_kast
    breedte_kast=cfg.breedte_kast
    diepte_kast=cfg.diepte_kast
    lengte_plank=cfg.lengte_plank
    dikte_plank=cfg.dikte_plank
    breedte_plank=cfg.breedte_plank
    #dikte_rib=cfg.dikte_rib
    
    hoogte_voet=cfg.hoogte_voet
    
    lengte_clip=20.
    breedte_clip=7.
    dikte_clip=1.
    lengte_voet=5.
    breedte_voet=10.
    dikte_voet=1.
    
    Balken=[]
    
    voorplank_breedte = cfg.voorplank_breedte
    
    rib_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/150)):
            rib_extra=rib_extra+1
        if rib_extra > 3:
            rib_extra=3
    
    ux0=ux
    uy0=diepte_kast/2.+dikte_plank/2.
    
    uxr = ux0 + lengte_clip/2.
    uxs = ux0 - lengte_voet/2.
    
    uxe = ux0 + float((breedte_kast-((rib_extra+2)*voorplank_breedte))/(rib_extra+1)) * .9
    
    if cfg.hoogte_kast <= 3*cfg.breedte_plank:
        for i in range(2):
            #maak bewegende deel
            plank=p.plank(lengte_plank,breedte_plank,dikte_plank)
            plank.plank_zagen(lengte_clip,breedte_clip,dikte_clip)
            rx,ry,rz=90,0,0-theta
            uy=diepte_kast/2.+dikte_clip/2.
            if i ==0 :
                uz = (hoogte_kast-hoogte_voet) /3. + hoogte_voet
            elif i == 1:
                uz = (hoogte_kast-hoogte_voet) *2/3. + hoogte_voet
        
            uxa,uya = rotate_point(uxr, uy, ux0, uy0, theta)
            
            sx,sy,sz=1,1,1
            plank.transformatie(rx,ry,rz,uxa,uya,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            balk=plank.balk()
            Balken.append(balk)
            if theta == 0:
                try:
                    if cfg.df_voorkant == []:
                        df_voorkant = pd.DataFrame({
                            "naam":         ['voorkant'],
                            "subnaam":      ['scharnier'],
                            "type":         ['scharnier'],
                            "nummer":       [0],
                            "lengte":       [lengte_clip],
                            "breedte":      [breedte_clip],
                            "dikte":        [dikte_clip],
                            "xloc":         [uxa],
                            "yloc":         [uya],
                            "zloc":         [uz],
                            "rx":           [rx],
                            "ry":           [ry],
                            "rz":           [rz],
                            "opmerking":    [nummer],
                            })
                        cfg.df_voorkant=df_voorkant
                    
                except ValueError:
                    df_voorkant_append = pd.DataFrame({
                        "naam":         ['voorkant'],
                        "subnaam":      ['scharnier'],
                        "type":         ['scharnier'],
                        "nummer":       [cfg.df_voorkant.shape[0]],
                        "lengte":       [lengte_clip],
                        "breedte":      [breedte_clip],
                        "dikte":        [dikte_clip],
                        "xloc":         [uxa],
                        "yloc":         [uya],
                        "zloc":         [uz],
                        "rx":           [rx],
                        "ry":           [ry],
                        "rz":           [rz],
                        "opmerking":    [nummer],
                        })
                
                    cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant_append],ignore_index=True)
                    #cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant],ignore_index=True)
                    
            #maak stille deel
            plank=p.plank(lengte_plank,breedte_plank,dikte_plank)
            plank.plank_zagen(lengte_voet,breedte_voet,dikte_voet)
            rx,ry,rz=90,0,0
            uys=diepte_kast/2.+dikte_clip/2.
            if i ==0 :
                uzs = (hoogte_kast-hoogte_voet) /3. + hoogte_voet
            elif i == 1:
                uzs = (hoogte_kast-hoogte_voet) *2/3. + hoogte_voet
        
            #uxa,uya = rotate_point(ux, uy, ux0, uy0, theta)
            
            sx,sy,sz=1,1,1
            plank.transformatie(rx,ry,rz,uxs,uys,uzs,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            balk=plank.balk()
            Balken.append(balk)
            if theta == 0:
                try:
                    if cfg.df_voorkant == []:
                        df_voorkant = pd.DataFrame({
                            "naam":         ['voorkant'],
                            "subnaam":      ['scharnier'],
                            "type":         ['scharnier'],
                            "nummer":       [0],
                            "lengte":       [lengte_voet],
                            "breedte":      [breedte_voet],
                            "dikte":        [dikte_voet],
                            "xloc":         [uxs],
                            "yloc":         [uys],
                            "zloc":         [uzs],
                            "rx":           [rx],
                            "ry":           [ry],
                            "rz":           [rz],
                            "opmerking":    [nummer],
                            })
                        cfg.df_voorkant=df_voorkant
                    
                except ValueError:
                    df_voorkant_append = pd.DataFrame({
                        "naam":         ['voorkant'],
                        "subnaam":      ['scharnier'],
                        "type":         ['scharnier'],
                        "nummer":       [cfg.df_voorkant.shape[0]],
                        "lengte":       [lengte_voet],
                        "breedte":      [breedte_voet],
                        "dikte":        [dikte_voet],
                        "xloc":         [uxs],
                        "yloc":         [uys],
                        "zloc":         [uzs],
                        "rx":           [rx],
                        "ry":           [ry],
                        "rz":           [rz],
                        "opmerking":    [nummer],
                        })
                
                    cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant_append],ignore_index=True)
                    #cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant],ignore_index=True)
    
    for i in range(3):
        #maak bewegende deel
        plank=p.plank(lengte_plank,breedte_plank,dikte_plank)
        plank.plank_zagen(lengte_clip,breedte_clip,dikte_clip)
        rx,ry,rz=90,0,0-theta
        uy=diepte_kast/2.+dikte_clip/2.
        if i ==0 :
            uz = (hoogte_kast-hoogte_voet) /2. + hoogte_voet
        elif i == 1:
            uz = (hoogte_kast-hoogte_voet) /6. + hoogte_voet
        elif i == 2:
            uz = (hoogte_kast-hoogte_voet) * 5/6. + hoogte_voet
    
        uxa,uya = rotate_point(uxr, uy, ux0, uy0, theta)
        
        sx,sy,sz=1,1,1
        plank.transformatie(rx,ry,rz,uxa,uya,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        balk=plank.balk()
        Balken.append(balk)
        if theta == 0:
            try:
                if cfg.df_voorkant == []:
                    df_voorkant = pd.DataFrame({
                        "naam":         ['voorkant'],
                        "subnaam":      ['scharnier'],
                        "type":         ['scharnier'],
                        "nummer":       [0],
                        "lengte":       [lengte_clip],
                        "breedte":      [breedte_clip],
                        "dikte":        [dikte_clip],
                        "xloc":         [uxa],
                        "yloc":         [uya],
                        "zloc":         [uz],
                        "rx":           [rx],
                        "ry":           [ry],
                        "rz":           [rz],
                        "opmerking":    [nummer],
                        })
                    cfg.df_voorkant=df_voorkant
                
            except ValueError:
                df_voorkant_append = pd.DataFrame({
                    "naam":         ['voorkant'],
                    "subnaam":      ['scharnier'],
                    "type":         ['scharnier'],
                    "nummer":       [cfg.df_voorkant.shape[0]],
                    "lengte":       [lengte_clip],
                    "breedte":      [breedte_clip],
                    "dikte":        [dikte_clip],
                    "xloc":         [uxa],
                    "yloc":         [uya],
                    "zloc":         [uz],
                    "rx":           [rx],
                    "ry":           [ry],
                    "rz":           [rz],
                    "opmerking":    [nummer],
                    })
            
                cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant_append],ignore_index=True)
                #cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant],ignore_index=True)
        
        #maak stille deel
        plank=p.plank(lengte_plank,breedte_plank,dikte_plank)
        plank.plank_zagen(lengte_voet,breedte_voet,dikte_voet)
        rx,ry,rz=90,0,0
        uys=diepte_kast/2.+dikte_clip/2.
        if i ==0 :
            uzs = (hoogte_kast-hoogte_voet) /2. + hoogte_voet
        elif i == 1:
            uzs = (hoogte_kast-hoogte_voet) /6. + hoogte_voet
        elif i == 2:
            uzs = (hoogte_kast-hoogte_voet) * 5/6. + hoogte_voet
    
        #uxa,uya = rotate_point(ux, uy, ux0, uy0, theta)
        
        sx,sy,sz=1,1,1
        plank.transformatie(rx,ry,rz,uxs,uys,uzs,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        balk=plank.balk()
        Balken.append(balk)
        if theta == 0:
            try:
                if cfg.df_voorkant == []:
                    df_voorkant = pd.DataFrame({
                        "naam":         ['voorkant'],
                        "subnaam":      ['scharnier'],
                        "type":         ['scharnier'],
                        "nummer":       [0],
                        "lengte":       [lengte_voet],
                        "breedte":      [breedte_voet],
                        "dikte":        [dikte_voet],
                        "xloc":         [uxs],
                        "yloc":         [uys],
                        "zloc":         [uzs],
                        "rx":           [rx],
                        "ry":           [ry],
                        "rz":           [rz],
                        "opmerking":    [nummer],
                        })
                    cfg.df_voorkant=df_voorkant
                
            except ValueError:
                df_voorkant_append = pd.DataFrame({
                    "naam":         ['voorkant'],
                    "subnaam":      ['scharnier'],
                    "type":         ['scharnier'],
                    "nummer":       [cfg.df_voorkant.shape[0]],
                    "lengte":       [lengte_voet],
                    "breedte":      [breedte_voet],
                    "dikte":        [dikte_voet],
                    "xloc":         [uxs],
                    "yloc":         [uys],
                    "zloc":         [uzs],
                    "rx":           [rx],
                    "ry":           [ry],
                    "rz":           [rz],
                    "opmerking":    [nummer],
                    })
            
                cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant_append],ignore_index=True)
                #cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant],ignore_index=True)
        
    #slot
    plank=p.plank(lengte_plank,breedte_plank,dikte_plank)
    plank.plank_zagen(breedte_clip,breedte_clip,dikte_clip)
    rx,ry,rz=90,0,0-theta
    uy=diepte_kast/2.+dikte_clip/2.
    uz = (hoogte_kast-hoogte_voet) /2. + hoogte_voet
    
    uxa,uya = rotate_point(uxe, uy, ux0, uy0, theta)
    
    sx,sy,sz=1,1,1
    plank.transformatie(rx,ry,rz,uxa,uya,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    balk=plank.balk()
    Balken.append(balk)
    if theta == 0:
        try:
            if cfg.df_voorkant == []:
                    df_voorkant = pd.DataFrame({
                        "naam":         ['voorkant'],
                        "subnaam":      ['slot'],
                        "type":         ['slot'],
                        "nummer":       [0],
                        "lengte":       [breedte_clip],
                        "breedte":      [breedte_clip],
                        "dikte":        [dikte_clip],
                        "xloc":         [uxa],
                        "yloc":         [uya],
                        "zloc":         [uz],
                        "rx":           [rx],
                        "ry":           [ry],
                        "rz":           [rz],
                        "opmerking":    [nummer],
                        })
                    cfg.df_voorkant=df_voorkant
                
        except ValueError:
                df_voorkant_append = pd.DataFrame({
                    "naam":         ['voorkant'],
                    "subnaam":      ['slot'],
                    "type":         ['slot'],
                    "nummer":       [cfg.df_voorkant.shape[0]],
                    "lengte":       [breedte_clip],
                    "breedte":      [breedte_clip],
                    "dikte":        [dikte_clip],
                    "xloc":         [uxa],
                    "yloc":         [uya],
                    "zloc":         [uz],
                    "rx":           [rx],
                    "ry":           [ry],
                    "rz":           [rz],
                    "opmerking":    [nummer],
                    })
            
                cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant_append],ignore_index=True)
                #cfg.df_voorkant=pd.concat([cfg.df_voorkant,df_voorkant],ignore_index=True)
            
    return Balken

def rotate_point(pointX, pointY, originX, originY, angle):
    
    angle=radians(angle)

    x = cos(angle) * (pointX-originX) - sin(angle) * (pointY-originY) + originX
    y = sin(angle) * (pointX-originX) + cos(angle) * (pointY-originY) + originY
    return x,y