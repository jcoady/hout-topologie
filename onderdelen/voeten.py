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
    print('voet extra:',voet_extra)
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
            
        elif voet_extra == 2:
            ve1a=p.plank(v,v,v)
            rx,ry,rz=0,0,0

            #ux=(breedte_kast-2*dikte_plank)/6.
            ux=(breedte_kast-dikte_plank*2-dikte_rib)/6.
            uy=diepte_kast/2.-v/2.-dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve1a.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete1a=ve1a.balk()
            Voeten.append(voete1a)
            
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
            
            ve1b=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            #ux=-(breedte_kast-2*dikte_plank)/6.
            ux=-(breedte_kast-dikte_plank*2-dikte_rib)/6.
            uy=diepte_kast/2.-v/2.-dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve1b.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete1b=ve1b.balk()
            Voeten.append(voete1b)
            
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
            
        elif voet_extra >= 3:
            ve1a=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            ux=0
            uy=diepte_kast/2.-v/2.-dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve1a.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete1a=ve1a.balk()
            Voeten.append(voete1a)
            
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
            
            ve1b=p.plank(v,v,v)
            rx,ry,rz=0,0,0

            #ux=(breedte_kast-2*dikte_plank)/4.
            ux=(breedte_kast-dikte_plank*2-dikte_rib)/4.
            uy=diepte_kast/2.-v/2.-dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve1b.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete1b=ve1b.balk()
            Voeten.append(voete1b)
            
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
            
            ve1c=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            #ux=-(breedte_kast-2*dikte_plank)/4.
            ux=-(breedte_kast-dikte_plank*2-dikte_rib)/4.
            uy=diepte_kast/2.-v/2.-dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve1c.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete1c=ve1c.balk()
            Voeten.append(voete1c)
            
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
            
        #new_row = {'naam':'voet','subnaam':'','index':df_voet.shape[0]+1,'lengte':v,'breedte':v,'dikte':v,'type':'blok','opmerking':''}
        #df_voet = df_voet.append(new_row, ignore_index=True)
        
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
        elif voet_extra == 2:
            ve2a=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            #ux=(breedte_kast-2*dikte_plank)/6.
            ux=(breedte_kast-dikte_plank*2-dikte_rib)/6.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2a.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2a=ve2a.balk()
            Voeten.append(voete2a)
            
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
            
            ve2b=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            #ux=-(breedte_kast-2*dikte_plank)/6.
            ux=-(breedte_kast-dikte_plank*2-dikte_rib)/6.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2b.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2b=ve2b.balk()
            Voeten.append(voete2b)
            
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
            
        elif voet_extra >= 3:
            ve2a=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            ux=0.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2a.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2a=ve2a.balk()
            Voeten.append(voete2a)
            
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
            
            ve2b=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            #ux=(breedte_kast-2*dikte_plank)/4.
            ux=(breedte_kast-dikte_plank*2-dikte_rib)/4.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2b.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2b=ve2b.balk()
            Voeten.append(voete2b)
            
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
            
            ve2c=p.plank(v,v,v)
            rx,ry,rz=0,0,0
            #ux=-(breedte_kast-2*dikte_plank)/4.
            ux=-(breedte_kast-dikte_plank*2-dikte_rib)/4.
            uy=-diepte_kast/2.+v/2.+dikte_plank
            uz=v/2.
            sx,sy,sz=1,1,1
            ve2c.transformatie(rx,ry,rz,ux,uy,uz,sx,sy,sz) #rx,ry,rz,ux,uy,uz,sx,sy,sz 
            voete2c=ve2c.balk()
            Voeten.append(voete2c)
            
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
            
        #new_row = {'naam':'voet','subnaam':'','index':df_voet.shape[0]+1,'lengte':v,'breedte':v,'dikte':v,'type':'blok','opmerking':''}
        #df_voet = df_voet.append(new_row, ignore_index=True)
        
    cfg.df_voet=df_voet

    return Voeten