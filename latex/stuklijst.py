#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 13:55:43 2022

@author: windhoos
"""

from latex import config as cfg
from latex import table_builder, language
import pandas as pd
import os

def build(path,lang):
    print('Build partlist')
    hoek=[4,cfg.hoek]
    schroef=[cfg.plank_dikte+cfg.balk_dikte,cfg.schroef]
    schroef_kort=[cfg.balk_dikte,cfg.schroef_kort]
    schroef_deur=[2*cfg.plank_dikte, cfg.schroef_deur]
    slot = ['max 4', cfg.slot_aantal]
    scharnier = ['max 10', cfg.scharnier_aantal]
    
    excel=cfg.plankenlijst.copy()
    excel.drop(excel.loc[excel['subnaam']=='scharnier'].index, inplace=True)
    excel.drop(excel.loc[excel['subnaam']=='slot'].index, inplace=True)
    excel.drop(excel.loc[excel['type']=='blok'].index, inplace=True)
    excel = excel.round({'dikte': 1, 'breedte': 1, 'lengte':1})
    excel = excel.pivot_table(columns=['type','dikte','breedte','lengte'], aggfunc='size')
    excel = excel.reset_index()
    excel = excel.rename(index=str,columns={0:'aantal'})
    
    lcaption = language.caption(lang, 'stuklijst')
    excel = language.rename(excel, lang, 'stuklijst')
    
    excel = excel.to_latex(index=False, position='h!',na_rep = '', float_format="%.1f", decimal=',',caption=f'{lcaption}')  
    save = 's0-stuklijst_hout.tex'
    path1 = os.path.join(path, save )
    with open(path1, 'w') as fout:
        for i in range(len(excel)):
            fout.write(excel[i])
    
    data_schroeven=[schroef,schroef_kort,schroef_deur]
    schroeven=pd.DataFrame(data_schroeven, columns=['max lengte','aantal'],index=['Schroef 1', 'Schroef 2', 'Schroef 3'])
    schroeven = language.rename(schroeven, lang, 'schroeven')
    lcaption = language.caption(lang, 'schroeven')
    #schroeven.to_excel('schroeven.xlsx')
    schroeven = schroeven.to_latex(index=True, position='h!',na_rep = '', float_format="%d", decimal=',',caption=f'{lcaption}')  
    save = 's0-schroeven.tex'
    path2 = os.path.join(path, save )
    with open(path2, 'w') as fout:
        for i in range(len(schroeven)):
            fout.write(schroeven[i])
    
    data_elementen=[hoek,scharnier,slot]
    elementen=pd.DataFrame(data_elementen, columns=['gaten raamwerk','aantal'],index=['Hoek frame', 'Scharnier', 'Slot'])
    elementen = language.rename(elementen, lang, 'elementen')
    lcaption = language.caption(lang, 'elementen')
    #elementen.to_excel('elementen.xlsx')
    elementen = elementen.to_latex(index=True, position='h!',na_rep = '', float_format="%d", decimal=',',caption=f'{lcaption}')  
    save = 's0-elementen.tex'
    path3 = os.path.join(path, save )
    with open(path3, 'w') as fout:
        for i in range(len(elementen)):
            fout.write(elementen[i])