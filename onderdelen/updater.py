#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 16:01:59 2022

@author: windhoos
"""

from onderdelen import config as cfg
from time import sleep
import pandas as pd
import os
import numpy as np


def update(path):
    #parent_dir = '/home/windhoos/hout-topologie/users'
    #directory = '01-08-2022-17-50-28-test'
    #path = os.path.join(parent_dir, directory)
    
    sleep(.5)

    a=[]
    b=[]
    for i in range(len(cfg.sliders)):
        a.append(cfg.sliders[i][1])
    for i in range(len(cfg.sliders_update)):
        b.append(cfg.sliders_update[i][1])
        
    if len(b) != 0:
        a=np.array(a)
        b=np.array(b)
    if len(a) != len(b):
        cfg.update_graph = True
    else:    
        if len(b) != 0:       
            if not (a == b).all():
                print('a!=b')
                cfg.update_graph = True
    
    if cfg.buy == True:
        cfg.update_graph = True
         
    #cfg.update_graph = True   
    if cfg.update_graph == True:
        cfg.update_graph = False
        
        excel_combine=[cfg.df_voet,cfg.df_onderstel,cfg.df_zeiplank,cfg.df_achterplank,cfg.df_voorkant,cfg.df_ribben,cfg.df_vlonders]
        for df in range(len(excel_combine)):
            if df == 0:
                excel=excel_combine[0]
            else:
                excel=pd.concat([excel,excel_combine[df]],ignore_index=True)
        excel=excel.sort_values(['naam','subnaam','type','dikte','breedte','lengte','xloc','yloc','zloc'], ascending=[False,False,False,False,False,False,False,False,False],ignore_index=True)        
        #excel.sort_values(by='naam')
        #if os.path.exists(os.path.join(path ,'plankenlijst.xlsx')):
        #    print('Delete excel')
        #    os.remove(os.path.join(path ,'plankenlijst.xlsx'))
        #print('Create excel')
        #excel.to_excel(os.path.join(path ,'plankenlijst.xlsx'))
        print(cfg.buy)
        if (os.path.exists(os.path.join(path ,'plankenlijst-FINAL.xlsx')) and cfg.buy==True):
            print('Delete excel-FINAL')
            os.remove(os.path.join(path ,'plankenlijst-FINAL.xlsx'))
        if cfg.buy==True:
            print('Create excel-FINAL')
            excel.to_excel(os.path.join(path ,'plankenlijst-FINAL.xlsx'))
            cfg.buy=False
        
        #excel=excel.sort_values(['lengte','breedte','dikte'], ascending=[False,False,False],ignore_index=True)
        
        #dups_excel = excel.pivot_table(columns=['type','dikte','breedte','lengte'], aggfunc='size')

        #if os.path.exists(os.path.join(path ,'stuklijst.xlsx')):
        #    print('Delete excel2')
        #    os.remove(os.path.join(path ,'stuklijst.xlsx'))
        #print('Create excel2')
        #dups_excel.to_excel(os.path.join(path ,'stuklijst.xlsx'))
        
        #if (os.path.exists(os.path.join(path ,'stuklijst-FINAL.xlsx')) and cfg.buy == True):
        #    print('Delete excel2-FINAL')
        #    os.remove(os.path.join(path ,'stuklijst-FINAL.xlsx'))
        #if cfg.buy == True:
        #    print('Create excel2-FINAL')
        #    dups_excel.to_excel(os.path.join(path ,'stuklijst-FINAL.xlsx'))
        #    cfg.buy=False
        
        cfg.sliders = cfg.sliders_update.copy()
        #cfg.sliders = copy.deepcopy(cfg.sliders_update)
        cfg.niveaus = len(cfg.sliders)
        plankhoogte = []
        for i in range(len(cfg.sliders)):
            plankhoogte.append(cfg.sliders[i][1])
        cfg.plankhoogte=plankhoogte
        
    else:
        sleep(.1)
        #print('pause')
    if cfg.reset == True:
        for i in range(len(cfg.input_velden)):
            cfg.input_velden[i].text=''
        for i in range(len(cfg.sliders_update)):
            cfg.sliders_update[i][5].text = ""
            cfg.sliders_update[i][5].delete()
            cfg.sliders_update[i][4].text = ""
            cfg.sliders_update[i][4].delete()
            cfg.sliders_update[i][3].text = ""
            cfg.sliders_update[i][3].delete()
            cfg.sliders_update[i][2].delete()
        cfg.sliders_update=[]
        
        for a in range(len(cfg.graphics)):
            for b in range(len(cfg.graphics[a])):
                for c in range(len(cfg.graphics[a][b])):
                    cfg.graphics[a][b][c][0].visible=False
                    cfg.graphics[a][b][c][1].visible=False
                    cfg.graphics[a][b][c][2].visible=False
                    cfg.graphics[a][b][c][3].visible=False
                    cfg.graphics[a][b][c][4].visible=False
                    del cfg.graphics[a][b][c][4]
                    del cfg.graphics[a][b][c][3]
                    del cfg.graphics[a][b][c][2]
                    del cfg.graphics[a][b][c][1]
                    del cfg.graphics[a][b][c][0]
        #cfg.knoppen=[build_knop,reset_knop,plank_knop,menu_knop]
        cfg.knoppen[0].disabled = False
        cfg.knoppen[1].disabled = True
        cfg.knoppen[2].disabled = True
        cfg.knoppen[3].disabled = True
        cfg.knoppen[4].disabled = True
    