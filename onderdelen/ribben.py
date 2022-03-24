#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 18:14:51 2022

@author: windhoos
"""

from onderdelen import plank as p
from onderdelen import config as cfg
import pandas as pd

def maak():
    breedte_kast=cfg.breedte_kast
    dikte_plank=cfg.dikte_plank
    dikte_rib=cfg.dikte_rib
    
    riblist=[]
    riblist.append(rib(breedte_kast/2.-dikte_plank-dikte_rib/2.))

    rib_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/150)):
            rib_extra=rib_extra+1
        if rib_extra > 3:
            rib_extra=3
    
    if rib_extra > 0:
        #for r in range(rib_extra):
        if rib_extra == 1:
            riblist.append(rib(0))

        elif rib_extra == 2:
            ux=(breedte_kast-dikte_plank*2-dikte_rib)/6.
            riblist.append(rib(ux))
            riblist.append(rib(-ux))
            
        elif rib_extra >= 3:
            riblist.append(rib(0))
            ux=(breedte_kast-dikte_plank*2-dikte_rib)/4.
            riblist.append(rib(ux))
            riblist.append(rib(-ux))
                
    riblist.append(rib(-(breedte_kast/2.-dikte_plank-dikte_rib/2.)))
    
    combined_riblist=[]
    for i in range(len(riblist)):
        combined_riblist=combined_riblist+riblist[i]
    
    return combined_riblist
    
def rib(ux):
    hoogte_kast=cfg.hoogte_kast
    #breedte_kast=cfg.breedte_kast
    diepte_kast=cfg.diepte_kast
    dikte_plank=cfg.dikte_plank
    
    hoogte_voet=cfg.hoogte_voet
    
    breedte_rib=cfg.breedte_rib
    lengte_rib=cfg.lengte_rib
    dikte_rib=cfg.dikte_rib
    
    niveaus=cfg.niveaus
    plank_hoogte=cfg.plankhoogte
    
    Ribben=[]

    #rib1 - onder
    r1=p.plank(lengte_rib,breedte_rib,dikte_rib)

    r1.plank_zagen(diepte_kast-2*dikte_plank,breedte_rib,dikte_rib)

    rx,ry,rz=0,0,90
    #ux=breedte_kast/2.-dikte_plank-dikte_rib/2.
    uy=0
    uz=hoogte_voet+dikte_plank+dikte_rib/2.
    sx,sy,sz=1,1,1
    r1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    rib1=r1.balk()
    Ribben.append(rib1)
    
    try:
        if cfg.df_ribben == []:
            df_ribben = pd.DataFrame({
                "naam":         ['ribben'],
                "subnaam":      ['onder'],
                "type":         ['balk'],
                "nummer":       [0],
                "lengte":       [diepte_kast-2*dikte_plank],
                "breedte":      [breedte_rib],
                "dikte":        [dikte_rib],
                "xloc":         [ux],
                "yloc":         [uy],
                "zloc":         [uz],
                "rx":           [rx],
                "ry":           [ry],
                "rz":           [rz],
                "opmerking":    [''],
                })
            cfg.df_ribben=df_ribben
                
    except ValueError:
        df_ribben_append = pd.DataFrame({
            "naam":         ['ribben'],
            "subnaam":      ['onder'],
            "type":         ['balk'],
            "nummer":       [cfg.df_ribben.shape[0]],
            "lengte":       [diepte_kast-2*dikte_plank],
            "breedte":      [breedte_rib],
            "dikte":        [dikte_rib],
            "xloc":         [ux],
            "yloc":         [uy],
            "zloc":         [uz],
            "rx":           [rx],
            "ry":           [ry],
            "rz":           [rz],
            "opmerking":    [''],
            })
        
        cfg.df_ribben=pd.concat([cfg.df_ribben,df_ribben_append],ignore_index=True)

    #rib2 - ene zeide
    r2=p.plank(lengte_rib,breedte_rib,dikte_rib)

    r2.plank_zagen(hoogte_kast-2*dikte_plank-hoogte_voet-2*dikte_rib,breedte_rib,dikte_rib)

    rx,ry,rz=0,90,0
    #ux=breedte_kast/2.-dikte_plank-dikte_rib/2.
    uy=diepte_kast/2.-dikte_plank-dikte_rib/2.
    uz=hoogte_voet+dikte_plank+(hoogte_kast-dikte_plank*2-hoogte_voet)/2.
    sx,sy,sz=1,1,1
    r2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    rib2=r2.balk()
    Ribben.append(rib2)
    
    try:
        if cfg.df_ribben == []:
            df_ribben = pd.DataFrame({
                "naam":         ['ribben'],
                "subnaam":      ['zeide'],
                "type":         ['balk'],
                "nummer":       [0],
                "lengte":       [hoogte_kast-2*dikte_plank-hoogte_voet-2*dikte_rib],
                "breedte":      [breedte_rib],
                "dikte":        [dikte_rib],
                "xloc":         [ux],
                "yloc":         [uy],
                "zloc":         [uz],
                "rx":           [rx],
                "ry":           [ry],
                "rz":           [rz],
                "opmerking":    [''],
                })
            cfg.df_ribben=df_ribben
                
    except ValueError:
        df_ribben_append = pd.DataFrame({
            "naam":         ['ribben'],
            "subnaam":      ['zeide'],
            "type":         ['balk'],
            "nummer":       [cfg.df_ribben.shape[0]],
            "lengte":       [hoogte_kast-2*dikte_plank-hoogte_voet-2*dikte_rib],
            "breedte":      [breedte_rib],
            "dikte":        [dikte_rib],
            "xloc":         [ux],
            "yloc":         [uy],
            "zloc":         [uz],
            "rx":           [rx],
            "ry":           [ry],
            "rz":           [rz],
            "opmerking":    [''],
            })
        
        cfg.df_ribben=pd.concat([cfg.df_ribben,df_ribben_append],ignore_index=True)
    
    #rib3 - andere zeide
    r3=p.plank(lengte_rib,breedte_rib,dikte_rib)

    r3.plank_zagen(hoogte_kast-2*dikte_plank-hoogte_voet-2*dikte_rib,breedte_rib,dikte_rib)

    rx,ry,rz=0,90,0
    #ux=breedte_kast/2.-dikte_plank-dikte_rib/2.
    uy=-(diepte_kast/2.-dikte_plank-dikte_rib/2.)
    uz=hoogte_voet+dikte_plank+(hoogte_kast-dikte_plank*2-hoogte_voet)/2.
    sx,sy,sz=1,1,1
    r3.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    rib3=r3.balk()
    Ribben.append(rib3)
    
    try:
        if cfg.df_ribben == []:
            df_ribben = pd.DataFrame({
                "naam":         ['ribben'],
                "subnaam":      ['zeide'],
                "type":         ['balk'],
                "nummer":       [0],
                "lengte":       [hoogte_kast-2*dikte_plank-hoogte_voet-2*dikte_rib],
                "breedte":      [breedte_rib],
                "dikte":        [dikte_rib],
                "xloc":         [ux],
                "yloc":         [uy],
                "zloc":         [uz],
                "rx":           [rx],
                "ry":           [ry],
                "rz":           [rz],
                "opmerking":    [''],
                })
            cfg.df_ribben=df_ribben
                
    except ValueError:
        df_ribben_append = pd.DataFrame({
            "naam":         ['ribben'],
            "subnaam":      ['zeide'],
            "type":         ['balk'],
            "nummer":       [cfg.df_ribben.shape[0]],
            "lengte":       [hoogte_kast-2*dikte_plank-hoogte_voet-2*dikte_rib],
            "breedte":      [breedte_rib],
            "dikte":        [dikte_rib],
            "xloc":         [ux],
            "yloc":         [uy],
            "zloc":         [uz],
            "rx":           [rx],
            "ry":           [ry],
            "rz":           [rz],
            "opmerking":    [''],
            })
        
        cfg.df_ribben=pd.concat([cfg.df_ribben,df_ribben_append],ignore_index=True)
    
    
    #rib4 - bovenkant
    r4=p.plank(lengte_rib,breedte_rib,dikte_rib)

    r4.plank_zagen(diepte_kast-2*dikte_plank,breedte_rib,dikte_rib)

    rx,ry,rz=0,0,90
    #ux=breedte_kast/2.-dikte_plank-dikte_rib/2.
    uy=0
    uz=hoogte_kast-dikte_rib/2.-dikte_plank
    sx,sy,sz=1,1,1
    r4.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    rib4=r4.balk()
    Ribben.append(rib4)
    
    try:
        if cfg.df_ribben == []:
            df_ribben = pd.DataFrame({
                "naam":         ['ribben'],
                "subnaam":      ['boven'],
                "type":         ['balk'],
                "nummer":       [0],
                "lengte":       [diepte_kast-2*dikte_plank],
                "breedte":      [breedte_rib],
                "dikte":        [dikte_rib],
                "xloc":         [ux],
                "yloc":         [uy],
                "zloc":         [uz],
                "rx":           [rx],
                "ry":           [ry],
                "rz":           [rz],
                "opmerking":    [''],
                })
            cfg.df_ribben=df_ribben
                
    except ValueError:
        df_ribben_append = pd.DataFrame({
            "naam":         ['ribben'],
            "subnaam":      ['boven'],
            "type":         ['balk'],
            "nummer":       [cfg.df_ribben.shape[0]],
            "lengte":       [diepte_kast-2*dikte_plank],
            "breedte":      [breedte_rib],
            "dikte":        [dikte_rib],
            "xloc":         [ux],
            "yloc":         [uy],
            "zloc":         [uz],
            "rx":           [rx],
            "ry":           [ry],
            "rz":           [rz],
            "opmerking":    [''],
            })
        
        cfg.df_ribben=pd.concat([cfg.df_ribben,df_ribben_append],ignore_index=True)
    
    ph=0
    for niveau in range(niveaus):
        #ph=ph+plank_hoogte[niveau]
        ph=plank_hoogte[niveau]
        r5=p.plank(lengte_rib,breedte_rib,dikte_rib)

        r5.plank_zagen(diepte_kast-2*dikte_plank-2*dikte_rib,breedte_rib,dikte_rib)

        rx,ry,rz=0,0,90
        #ux=breedte_kast/2.-dikte_plank-dikte_rib/2.
        uy=0
        uz=ph-dikte_rib/2.-cfg.dikte_plank+cfg.hoogte_voet+cfg.dikte_plank
        sx,sy,sz=1,1,1
        r5.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        rib5=r5.balk()
        Ribben.append(rib5)
        
        try:
            if cfg.df_ribben == []:
                df_ribben = pd.DataFrame({
                    "naam":         ['ribben'],
                    "subnaam":      ['tussen'],
                    "type":         ['balk'],
                    "nummer":       [0],
                    "lengte":       [diepte_kast-2*dikte_plank-2*dikte_rib],
                    "breedte":      [breedte_rib],
                    "dikte":        [dikte_rib],
                    "xloc":         [ux],
                    "yloc":         [uy],
                    "zloc":         [uz],
                    "rx":           [rx],
                    "ry":           [ry],
                    "rz":           [rz],
                    "opmerking":    [''],
                    })
                cfg.df_ribben=df_ribben
                    
        except ValueError:
            df_ribben_append = pd.DataFrame({
                "naam":         ['ribben'],
                "subnaam":      ['tussen'],
                "type":         ['balk'],
                "nummer":       [cfg.df_ribben.shape[0]],
                "lengte":       [diepte_kast-2*dikte_plank-2*dikte_rib],
                "breedte":      [breedte_rib],
                "dikte":        [dikte_rib],
                "xloc":         [ux],
                "yloc":         [uy],
                "zloc":         [uz],
                "rx":           [rx],
                "ry":           [ry],
                "rz":           [rz],
                "opmerking":    [''],
                })
            
            cfg.df_ribben=pd.concat([cfg.df_ribben,df_ribben_append],ignore_index=True)

    return Ribben