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
    locatie = 0

    rib_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/150)):
            rib_extra=rib_extra+1
        if rib_extra > 3:
            rib_extra=3
    
    if rib_extra == 0:
        #lengte=(breedte_kast-2*dikte_plank-(2+rib_extra)*dikte_rib)/(1+rib_extra)
        lengte=breedte_kast-2*dikte_plank-2*dikte_rib
        ux=0.
        
        riblist.append(rib(lengte,ux,locatie))
        
    elif rib_extra == 1:
        #lengte=(breedte_kast-2*dikte_plank-(2+rib_extra)*dikte_rib)/(1+rib_extra)
        lengte=(breedte_kast-2*dikte_plank-3*dikte_rib)/2.
        uxl=lengte/2.+dikte_rib/2.
        uxr=-uxl
        
        riblist.append(rib(lengte,uxl,locatie))
        riblist.append(rib(lengte,uxr,locatie+1))

    elif rib_extra == 2:
        #lengte=(breedte_kast-2*dikte_plank-(2+rib_extra)*dikte_rib)/(1+rib_extra)
        lengte=(breedte_kast-2*dikte_plank-4*dikte_rib)/3.
        ux=0.
        riblist.append(rib(lengte,ux,locatie+1))
        uxl=lengte/2.+dikte_rib+lengte/2.
        uxr=-uxl
        
        riblist.append(rib(lengte,uxl,locatie))
        riblist.append(rib(lengte,uxr,locatie+2))
            
    elif rib_extra >= 3:
        #lengte=(breedte_kast-2*dikte_plank-(2+rib_extra)*dikte_rib)/(1+3)
        lengte=(breedte_kast-2*dikte_plank-5*dikte_rib)/4.
        uxl=dikte_rib/2.+lengte/2.
        uxll=dikte_rib/2.+lengte+dikte_rib+lengte/2.
        uxr=-uxl
        uxrr=-uxll
        
        riblist.append(rib(lengte,uxl,locatie+1))
        riblist.append(rib(lengte,uxll,locatie))
        riblist.append(rib(lengte,uxr,locatie+2))
        riblist.append(rib(lengte,uxrr,locatie+3))

    combined_riblist=[]
    for i in range(len(riblist)):
        combined_riblist=combined_riblist+riblist[i]
    
    return combined_riblist
    
def rib(lengte,ux,locatie):
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
        uz=ph-dikte_rib/2.+cfg.hoogte_voet+cfg.dikte_plank
        sx,sy,sz=1,1,1
        r1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
        rib1=r1.balk()
        Ribben.append(rib1)
        
        try:
            if cfg.df_ribben == []:
                df_ribben = pd.DataFrame({
                    "naam":         ['ribben'],
                    "subnaam":      ['achter'],
                    "type":         ['balk'],
                    "nummer":       [0],
                    "lengte":       [lengte],
                    "breedte":      [breedte_rib],
                    "dikte":        [dikte_rib],
                    "xloc":         [ux],
                    "yloc":         [uy],
                    "zloc":         [uz],
                    "rx":           [rx],
                    "ry":           [ry],
                    "rz":           [rz],
                    "opmerking":    [locatie],
                    })
                cfg.df_ribben=df_ribben
                    
        except ValueError:
            df_ribben_append = pd.DataFrame({
                "naam":         ['ribben'],
                "subnaam":      ['achter'],
                "type":         ['balk'],
                "nummer":       [cfg.df_ribben.shape[0]],
                "lengte":       [lengte],
                "breedte":      [breedte_rib],
                "dikte":        [dikte_rib],
                "xloc":         [ux],
                "yloc":         [uy],
                "zloc":         [uz],
                "rx":           [rx],
                "ry":           [ry],
                "rz":           [rz],
                "opmerking":    [locatie],
                })
            
            cfg.df_ribben=pd.concat([cfg.df_ribben,df_ribben_append],ignore_index=True)

    return Ribben