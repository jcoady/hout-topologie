#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:49 2022

@author: windhoos
"""

from onderdelen import plank as p
from onderdelen import config as cfg
from math import floor
import pandas as pd

def maak():
    Breedtes=[]
    Balken=[]
    
    hoogte_kast=cfg.hoogte_kast
    diepte_kast=cfg.diepte_kast
    breedte_plank=cfg.breedte_plank
    lengte_plank=cfg.lengte_plank
    dikte_plank=cfg.dikte_plank
    breedte_kast=cfg.breedte_kast
    hoogte_voet=cfg.hoogte_voet
    
    d=float(breedte_kast)
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
    
    ux=breedte_kast/2.

    Breedtes.reverse()
    for planken in range(len(Breedtes)):
        plank=p.plank(lengte_plank,breedte_plank,dikte_plank)
        plank.plank_zagen(hoogte_kast-hoogte_voet,Breedtes[planken],dikte_plank)
        rx,ry,rz=0,90,90
        
        uy=-diepte_kast/2. + dikte_plank/2.

        if planken == 0:
            ux = ux - Breedtes[planken]/2.
        else:
            ux = ux - Breedtes[planken]/2. - Breedtes[planken-1]/2.
        uz=hoogte_voet+(hoogte_kast-hoogte_voet)/2.
        sx,sy,sz=1,1,1
        plank.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        balk=plank.balk()
        Balken.append(balk)
        
        if planken == 0:
            df_plank = pd.DataFrame({
                "naam":         ['achterplank'],
                "subnaam":      [''],
                "type":         ['plank'],
                "nummer":       [0],
                "lengte":       [hoogte_kast-hoogte_voet],
                "breedte":      [Breedtes[planken]],
                "dikte":        [dikte_plank],
                "xloc":         [ux],
                "yloc":         [uy],
                "zloc":         [uz],
                "rx":           [rx],
                "ry":           [ry],
                "rz":           [rz],
                "opmerking":    [''],
                })
            
        else:
            df_plank_append = pd.DataFrame({
                "naam":         ['achterplank'],
                "subnaam":      [''],
                "type":         ['plank'],
                "nummer":       [df_plank.shape[0]],
                "lengte":       [hoogte_kast-hoogte_voet],
                "breedte":      [Breedtes[planken]],
                "dikte":        [dikte_plank],
                "xloc":         [ux],
                "yloc":         [uy],
                "zloc":         [uz],
                "rx":           [rx],
                "ry":           [ry],
                "rz":           [rz],
                "opmerking":    [''],
                })
        
            df_plank=pd.concat([df_plank,df_plank_append],ignore_index=True)
        
    cfg.df_achterplank=df_plank
    print(cfg.df_achterplank)
        
    return Balken