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

def update():
    sleep(.5)
    #print('update - sliders_update ',cfg.sliders_update,' sliders ',  cfg.sliders)
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
        if os.path.exists('plankenlijst.xlsx'):
            print('Delete excel')
            os.remove('plankenlijst.xlsx')
        print('Create excel')
        excel.to_excel('plankenlijst.xlsx')
        #excel=excel.sort_values(['lengte','breedte','dikte'], ascending=[False,False,False],ignore_index=True)
        
        dups_excel = excel.pivot_table(columns=['type','dikte','breedte','lengte'], aggfunc='size')

        if os.path.exists('stuklijst.xlsx'):
            print('Delete excel2')
            os.remove('stuklijst.xlsx')
        print('Create excel2')
        dups_excel.to_excel('stuklijst.xlsx')
        
        cfg.sliders = cfg.sliders_update.copy()
        cfg.niveaus = len(cfg.sliders)
        plankhoogte = []
        for i in range(len(cfg.sliders)):
            plankhoogte.append(cfg.sliders[i][1])
        cfg.plankhoogte=plankhoogte
    else:
        sleep(.5)
        #print('pause')