#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 22:10:10 2022

@author: windhoos
"""

import os
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from latex import language

def latex(df_list,path,lang,step):
    df_list=df_list.copy()
    if len(df_list) >= 2:
        latex=pd.concat(df_list)
    else:
        latex=df_list[0]
    
    #\usepackage{booktabs}
    if step == 1:
        save = 's1-voeten.tex'
    elif step == 2:
        save = 's2-rib_bottom.tex'
    elif step == 3:
        save = 's3-ladder.tex'
    elif step == 5:
        save = 's5-achterrib.tex'
    elif step == 6:
        save = 's6-vlonder.tex'
    elif step == 7:
        save = 's7-boven.tex'
    elif step == 8:
        save = 's8-zeiden.tex'
    elif step == 9:
        save = 's9-achterkant.tex'
    elif step == 10:
        save = 's10-deurpost.tex'
    elif step == 11:
        save = 's11-deur.tex'
    elif step == 12:
        save = 's12-sloten.tex'
    else:
        save=step
    
    latex = latex.drop(['xloc','yloc','zloc','rx','ry','rz'],axis=1)
    latex = latex.round(1)
    latex = latex.groupby(latex.columns.tolist(),as_index=False).size()
    latex = latex.rename(columns={'size': 'aantal'})
    
    lcaption = language.caption(lang, step)
    latex = language.rename(latex, lang, 'steplist')
    
    latex = latex.to_latex(index=False, position='h!',na_rep = '', float_format="%.1f", decimal=',',caption=f'{lcaption}')  
    
    path = os.path.join(path, save )
    with open(path, 'w') as fout:
        for i in range(len(latex)):
            fout.write(latex[i])