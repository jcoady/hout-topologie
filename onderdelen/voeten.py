#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:49 2022

@author: windhoos
"""

from onderdelen import plank as p
from onderdelen import config as cfg
import pandas as pd

def maak():
    breedte_kast=cfg.breedte_kast
    hoogte_voet=cfg.hoogte_voet
    diepte_kast=cfg.diepte_kast
    dikte_plank=cfg.dikte_plank
    dikte_rib=cfg.dikte_rib
    
    Voeten=[]
    #bereken hoeveelheid voeten
    voet_extra=0
    if breedte_kast >= 170:
        for i in range(int(breedte_kast/150)):
            voet_extra=voet_extra+1

    v=hoogte_voet

    #voet1
    v1=p.plank(v,v,v)
    rx,ry,rz=0,0,0
    ux,uy,uz=breedte_kast/2.-v/2.-dikte_plank,diepte_kast/2.-v/2.-dikte_plank,v/2.
    sx,sy,sz=1,1,1
    v1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet1=v1.balk()
    Voeten.append(voet1)
    
    df_voet = pd.DataFrame({
        "naam":         ['voet'],
        "subnaam":      [''],
        "type":         ['blok'],
        "nummer":       [0],
        "lengte":       [v],
        "breedte":      [v],
        "dikte":        [v],
        "xloc":         [ux],
        "yloc":         [uy],
        "zloc":         [uz],
        "rx":           [rx],
        "ry":           [ry],
        "rz":           [rz],
        "opmerking":    [''],
    })

    
    #voet2
    v2=p.plank(v,v,v)
    rx,ry,rz=0,0,0
    ux,uy,uz=breedte_kast/2.-v/2.-dikte_plank,-diepte_kast/2.+v/2.+dikte_plank,v/2.
    sx,sy,sz=1,1,1
    v2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet2=v2.balk()
    Voeten.append(voet2)
    
    #new_row = {'naam':'voet','subnaam':'','index':2,'lengte':v,'breedte':v,'dikte':v,'type':'blok','opmerking':''}
    #df_voet = df_voet.append(new_row, ignore_index=True)
    
    df_voet_append = pd.DataFrame({
        "naam":         ['voet'],
        "subnaam":      [''],
        "type":         ['blok'],
        "nummer":       [1],
        "lengte":       [v],
        "breedte":      [v],
        "dikte":        [v],
        "xloc":         [ux],
        "yloc":         [uy],
        "zloc":         [uz],
        "rx":           [rx],
        "ry":           [ry],
        "rz":           [rz],
        "opmerking":    [''],
    })
    
    df_voet=pd.concat([df_voet,df_voet_append],ignore_index=True)
    
    #voet3
    v3=p.plank(v,v,v)
    rx,ry,rz=0,0,0
    ux,uy,uz=-breedte_kast/2.+v/2.+dikte_plank,-diepte_kast/2.+v/2.+dikte_plank,v/2.
    sx,sy,sz=1,1,1
    v3.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet3=v3.balk()
    Voeten.append(voet3)
    
    #new_row = {'naam':'voet','subnaam':'','index':3,'lengte':v,'breedte':v,'dikte':v,'type':'blok','opmerking':''}
    #df_voet = df_voet.append(new_row, ignore_index=True)
    
    df_voet_append = pd.DataFrame({
        "naam":         ['voet'],
        "subnaam":      [''],
        "type":         ['blok'],
        "nummer":       [2],
        "lengte":       [v],
        "breedte":      [v],
        "dikte":        [v],
        "xloc":         [ux],
        "yloc":         [uy],
        "zloc":         [uz],
        "rx":           [rx],
        "ry":           [ry],
        "rz":           [rz],
        "opmerking":    [''],
    })
    
    df_voet=pd.concat([df_voet,df_voet_append],ignore_index=True)
    
    #voet4
    v4=p.plank(v,v,v)
    rx,ry,rz=0,0,0
    ux,uy,uz=-breedte_kast/2.+v/2.+dikte_plank,diepte_kast/2.-v/2.-dikte_plank,v/2.
    sx,sy,sz=1,1,1
    v4.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
    voet4=v4.balk()
    Voeten.append(voet4)
    
    #new_row = {'naam':'voet','subnaam':'','index':4,'lengte':v,'breedte':v,'dikte':v,'type':'blok','opmerking':''}
    #df_voet = df_voet.append(new_row, ignore_index=True)
    
    df_voet_append = pd.DataFrame({
        "naam":         ['voet'],
        "subnaam":      [''],
        "type":         ['blok'],
        "nummer":       [3],
        "lengte":       [v],
        "breedte":      [v],
        "dikte":        [v],
        "xloc":         [ux],
        "yloc":         [uy],
        "zloc":         [uz],
        "rx":           [rx],
        "ry":           [ry],
        "rz":           [rz],
        "opmerking":    [''],
    })
    
    df_voet=pd.concat([df_voet,df_voet_append],ignore_index=True)
    
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

            #ux=(breedte_kast-2*dikte_plank)/6.
            ux=(breedte_kast-dikte_plank*2-dikte_rib)/6.
            uy=diepte_kast/2.-v/2.-dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete1=ve1.balk()
            Voeten.append(voete1)
            
            ve1=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            #ux=-(breedte_kast-2*dikte_plank)/6.
            ux=-(breedte_kast-dikte_plank*2-dikte_rib)/6.
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

            #ux=(breedte_kast-2*dikte_plank)/4.
            ux=(breedte_kast-dikte_plank*2-dikte_rib)/4.
            uy=diepte_kast/2.-v/2.-dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete1=ve1.balk()
            Voeten.append(voete1)
            
            ve1=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            #ux=-(breedte_kast-2*dikte_plank)/4.
            ux=-(breedte_kast-dikte_plank*2-dikte_rib)/4.
            uy=diepte_kast/2.-v/2.-dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve1.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete1=ve1.balk()
            Voeten.append(voete1)
            
        #new_row = {'naam':'voet','subnaam':'','index':df_voet.shape[0]+1,'lengte':v,'breedte':v,'dikte':v,'type':'blok','opmerking':''}
        #df_voet = df_voet.append(new_row, ignore_index=True)
        
        df_voet_append = pd.DataFrame({
            "naam":         ['voet'],
            "subnaam":      [''],
            "type":         ['blok'],
            "nummer":       [df_voet.shape[0]],
            "lengte":       [v],
            "breedte":      [v],
            "dikte":        [v],
            "xloc":         [ux],
            "yloc":         [uy],
            "zloc":         [uz],
            "rx":           [rx],
            "ry":           [ry],
            "rz":           [rz],
            "opmerking":    [''],
            })
    
        df_voet=pd.concat([df_voet,df_voet_append],ignore_index=True)
        
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
            #ux=(breedte_kast-2*dikte_plank)/6.
            ux=(breedte_kast-dikte_plank*2-dikte_rib)/6.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2=ve2.balk()
            Voeten.append(voete2)
            
            ve2=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            #ux=-(breedte_kast-2*dikte_plank)/6.
            ux=-(breedte_kast-dikte_plank*2-dikte_rib)/6.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2=ve2.balk()
            Voeten.append(voete2)
            
        elif voet_extra >= 3:
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
            #ux=(breedte_kast-2*dikte_plank)/4.
            ux=(breedte_kast-dikte_plank*2-dikte_rib)/4.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2=ve2.balk()
            Voeten.append(voete2)
            
            ve2=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            #ux=-(breedte_kast-2*dikte_plank)/4.
            ux=-(breedte_kast-dikte_plank*2-dikte_rib)/4.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2=ve2.balk()
            Voeten.append(voete2)
            
        #new_row = {'naam':'voet','subnaam':'','index':df_voet.shape[0]+1,'lengte':v,'breedte':v,'dikte':v,'type':'blok','opmerking':''}
        #df_voet = df_voet.append(new_row, ignore_index=True)
        
        df_voet_append = pd.DataFrame({
            "naam":         ['voet'],
            "subnaam":      [''],
            "type":         ['blok'],
            "nummer":       [df_voet.shape[0]],
            "lengte":       [v],
            "breedte":      [v],
            "dikte":        [v],
            "xloc":         [ux],
            "yloc":         [uy],
            "zloc":         [uz],
            "rx":           [rx],
            "ry":           [ry],
            "rz":           [rz],
            "opmerking":    [''],
            })
        
        df_voet=pd.concat([df_voet,df_voet_append],ignore_index=True)
        
    cfg.df_voet=df_voet
    print(cfg.df_voet)

    return Voeten