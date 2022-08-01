#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:38:59 2022

@author: windhoos
"""

from latex import config as cfg

import pandas as pd
import os.path

def build():
    parent_dir = '/home/windhoos/hout-topologie/users'
    directory = '01-08-2022-17-50-28-test'
    path = os.path.join(parent_dir, directory)
    
    path2= os.path.join(path,'stuklijst-FINAL.xlsx')
    cfg.stuklijst=pd.read_excel(path2)
    
    path3= os.path.join(path,'plankenlijst-FINAL.xlsx')
    cfg.plankenlijst=pd.read_excel(path3)
    plankenlijst = cfg.plankenlijst.copy()
    
    #voeten
    print('\n voeten')
    colum = 'naam'
    sub = 'voet'
    voeten = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    voeten = voeten.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    voeten = voeten.reset_index(drop=True)
    cfg.voeten=voeten
    print(cfg.voeten)
    
    #onderplanken
    print('\n onderkant')
    colum = 'naam'
    sub = 'onderstel'
    onderkant = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    colum = 'subnaam'
    sub = 'onderkant'
    onderkant = onderkant[onderkant[colum].str.contains(sub, regex=False, case=False, na=False)]
    onderkant = onderkant.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    onderkant = onderkant.reset_index(drop=True)
    cfg.onderkant=onderkant
    print(cfg.onderkant)
    
    #onder ribben
    print('\n onder ribben')
    colum = 'naam'
    sub = 'ribben'
    rib1 = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    sub2 = 'subnaam'
    rib1 = rib1.loc[rib1[sub2] == 'onder']
    rib1 = rib1.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    rib1 = rib1.reset_index(drop=True)
    cfg.rib_onder=rib1
    print(cfg.rib_onder)
    
    #bouw ribmax
    print('\n ribmax')
    colum = 'naam'
    sub = 'ribben'
    ribmax = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    ribmax = ribmax[~ribmax.select_dtypes(['object']).eq('onder').any(1)]
    ribmax = ribmax.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    ribmax = ribmax.reset_index(drop=True)
    cfg.ribmax=ribmax
    print(cfg.ribmax)
    
    #bouw bovenkant
    print('\n bovenkant')
    colum = 'naam'
    sub = 'onderstel'
    bovenkant = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    colum = 'subnaam'
    sub = 'bovenkant'
    bovenkant = bovenkant[bovenkant[colum].str.contains(sub, regex=False, case=False, na=False)]
    bovenkant = bovenkant.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    bovenkant = bovenkant.reset_index(drop=True)
    cfg.bovenkant=bovenkant
    print(cfg.bovenkant)
    
    #achterrib
    print('\n achterrib')
    colum = 'naam'
    sub = 'ribben'
    achterrib = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    colum = 'subnaam'
    sub = 'achter'
    achterrib = achterrib[achterrib[colum].str.contains(sub, regex=False, case=False, na=False)]
    achterrib = achterrib.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    achterrib = achterrib.reset_index(drop=True)
    cfg.achterrib=achterrib
    print(cfg.achterrib)
    
    #vlonders
    print('\n vlonders')
    colum = 'naam'
    sub = 'vlonders'
    vlonders = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    #colum = 'subnaam'
    #sub = 'achter'
    #vlonders = vlonders[vlonders[colum].str.contains(sub, regex=False, case=False, na=False)]
    vlonders = vlonders.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    vlonders = vlonders.reset_index(drop=True)
    cfg.vlonders=vlonders
    print(cfg.vlonders)
    
    #zeide links
    print('\n zeide links')
    colum = 'naam'
    sub = 'zeiplanken'
    zeidelinks = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    colum = 'subnaam'
    sub = 'links'
    zeidelinks = zeidelinks[zeidelinks[colum].str.contains(sub, regex=False, case=False, na=False)]
    zeidelinks = zeidelinks.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    zeidelinks = zeidelinks.reset_index(drop=True)
    cfg.zeidelinks=zeidelinks
    print(cfg.zeidelinks)
    
    #zeide rechts
    print('\n zeide rechts')
    colum = 'naam'
    sub = 'zeiplanken'
    zeiderechts = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    colum = 'subnaam'
    sub = 'rechts'
    zeiderechts = zeiderechts[zeiderechts[colum].str.contains(sub, regex=False, case=False, na=False)]
    zeiderechts = zeiderechts.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    zeiderechts = zeiderechts.reset_index(drop=True)
    cfg.zeiderechts=zeiderechts
    print(cfg.zeiderechts)
    
    #achterkant
    print('\n achterkant')
    colum = 'naam'
    sub = 'achterplank'
    achterkant = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    #colum = 'subnaam'
    #sub = 'rechts'
    #achterkant = achterkant[achterkant[colum].str.contains(sub, regex=False, case=False, na=False)]
    achterkant = achterkant.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    achterkant = achterkant.reset_index(drop=True)
    cfg.achterkant=achterkant
    print(cfg.achterkant)
    
    #voorkant
    print('\n voorkant')
    colum = 'naam'
    sub = 'voorkant'
    voorkant = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    colum = 'subnaam'
    sub = 'voorplank'
    voorkant = voorkant[voorkant[colum].str.contains(sub, regex=False, case=False, na=False)]
    voorkant = voorkant.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    voorkant = voorkant.reset_index(drop=True)
    cfg.voorkant=voorkant
    print(cfg.voorkant)
    
    #deur
    print('\n deur')
    colum = 'naam'
    sub = 'voorkant'
    deur = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    colum = 'subnaam'
    sub = 'deur'
    deur = deur[deur[colum].str.contains(sub, regex=False, case=False, na=False)]
    sub2 = 'opmerking'
    deur = deur.loc[deur[sub2] == 1.0]
    deur = deur.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    deur = deur.reset_index(drop=True)
    cfg.deur=deur
    print(cfg.deur)
    
    #deur volledig
    print('\n deur volledig')
    colum = 'naam'
    sub = 'voorkant'
    deur = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    colum = 'subnaam'
    sub = 'deur'
    deur = deur[deur[colum].str.contains(sub, regex=False, case=False, na=False)]
    deur = deur.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    deur = deur.reset_index(drop=True)
    cfg.deur_volledig=deur
    print(cfg.deur_volledig)
    
    #stut
    print('\n stut')
    colum = 'naam'
    sub = 'voorkant'
    stut = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    colum = 'subnaam'
    sub = 'stut'
    stut = stut[stut[colum].str.contains(sub, regex=False, case=False, na=False)]
    sub2 = 'opmerking'
    stut = stut.loc[stut[sub2] == 1.0]
    stut = stut.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    stut = stut.reset_index(drop=True)
    cfg.stut=stut
    print(cfg.stut)
    
    #stut volledig
    print('\n stut volledig')
    colum = 'naam'
    sub = 'voorkant'
    stut = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    colum = 'subnaam'
    sub = 'stut'
    stut = stut[stut[colum].str.contains(sub, regex=False, case=False, na=False)]
    stut = stut.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    stut = stut.reset_index(drop=True)
    cfg.stut_volledig=stut
    print(cfg.stut_volledig)
    
    #scharnier
    print('\n scharnier')
    colum = 'naam'
    sub = 'voorkant'
    scharnier = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    colum = 'subnaam'
    sub = 'scharnier'
    scharnier = scharnier[scharnier[colum].str.contains(sub, regex=False, case=False, na=False)]
    #sub2 = 'opmerking'
    #scharnier = scharnier.loc[scharnier[sub2] == 1.0]
    scharnier = scharnier.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    scharnier = scharnier.reset_index(drop=True)
    cfg.scharnier=scharnier
    print(cfg.scharnier)
    
    #slot
    print('\n slot')
    colum = 'naam'
    sub = 'voorkant'
    slot = plankenlijst[plankenlijst[colum].str.contains(sub, regex=False, case=False, na=False)]
    colum = 'subnaam'
    sub = 'slot'
    slot = slot[slot[colum].str.contains(sub, regex=False, case=False, na=False)]
    #sub2 = 'opmerking'
    #slot = slot.loc[slot[sub2] == 1.0]
    slot = slot.filter(['lengte','breedte','dikte','xloc','yloc','zloc','rx','ry','rz'])
    slot = slot.reset_index(drop=True)
    cfg.slot=slot
    print(cfg.slot)
    
    plank=onderkant.loc[onderkant['lengte'].idxmax()]
    cfg.plank_dikte=plank[2]
    
    balk=rib1.loc[rib1['lengte'].idxmax()]
    cfg.balk_dikte=balk[1]
    
    poot=voeten.loc[voeten['lengte'].idxmax()]
    poot=poot[0]
    cfg.poot_hoogte=poot