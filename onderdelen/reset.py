#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 21:41:02 2022

@author: windhoos
"""

from onderdelen import config as cfg

def reset():
    
    cfg.breedte_kast=0
    cfg.hoogte_kast=0
    cfg.diepte_kast=0
    
    cfg.breedte_plank=0
    cfg.lengte_plank=0
    cfg.dikte_plank=0
    
    cfg.niveaus=1
    cfg.plankhoogte=[]
    
    cfg.hoogte_voet=0
    
    cfg.breedte_rib=5
    cfg.lengte_rib=240
    cfg.dikte_rib=cfg.breedte_rib
    
    cfg.voorplank_breedte=0
    
    cfg.df_voet=[]
    cfg.df_onderstel=[]
    cfg.df_zeiplank=[]
    cfg.df_achterplank=[]
    cfg.df_voorkant=[]
    cfg.df_ribben=[]
    cfg.df_vlonders=[]
    
    cfg.procent=0
    
    cfg.start=0
    cfg.end=0
    
    cfg.graphics=0
    cfg.sliders=[]
    cfg.sliders_update=[]
    cfg.update_graph=False
    
    cfg.reset=False
    cfg.reset_loop=True
    
    #cfg.knoppen=[]
    #cfg.input_velden=[]
    cfg.build_state=False
    
    cfg.finish_drawing = False
    
    #cfg.wt_error=' '
    cfg.error_message = ' '
    cfg.error_message0 = ' '
    cfg.error_message1 = '                                                                        <b>ERROR</b>'