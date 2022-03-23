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
    breedte_kast=cfg.breedte_kast
    dikte_plank=cfg.dikte_plank
    
    zeilist=[]
    
    zeilist.append(zeide(breedte_kast/2.-dikte_plank/2.,'links'))
    zeilist.append(zeide(-(breedte_kast/2.-dikte_plank/2.),'rechts'))
    
    combined_zeilist=[]
    for zei in range(len(zeilist)):
        combined_zeilist=combined_zeilist+zeilist[zei]
    
    return combined_zeilist

def zeide(ux,sub):
    Breedtes=[]
    Balken=[]
    
    hoogte_kast=cfg.hoogte_kast
    diepte_kast=cfg.diepte_kast
    breedte_plank=cfg.breedte_plank
    lengte_plank=cfg.lengte_plank
    dikte_plank=cfg.dikte_plank
    #breedte_kast=cfg.breedte_kast
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
        plank.plank_zagen(hoogte_kast-hoogte_voet,Breedtes[planken],dikte_plank)
        rx,ry,rz=0,90,0

        if planken == 0:
            uy = uy - Breedtes[planken]/2.
        else:
            uy = uy - Breedtes[planken]/2. - Breedtes[planken-1]/2.
        uz=hoogte_voet+(hoogte_kast-hoogte_voet)/2.
        sx,sy,sz=1,1,1
        plank.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        balk=plank.balk()
        Balken.append(balk)
        
        try:
            if cfg.df_zeiplank == []:
                df_zeiplank = pd.DataFrame({
                "naam":         ['zeiplanken'],
                "subnaam":      [sub],
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
                cfg.df_zeiplank=df_zeiplank
                    
        except ValueError:
            df_zeiplank_append = pd.DataFrame({
                "naam":         ['zeiplanken'],
                "subnaam":      [sub],
                "type":         ['plank'],
                "nummer":       [cfg.df_zeiplank.shape[0]],
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
            
            cfg.df_zeiplank=pd.concat([cfg.df_zeiplank,df_zeiplank_append],ignore_index=True)
        
    return Balken