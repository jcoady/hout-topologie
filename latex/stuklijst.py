#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 13:55:43 2022

@author: windhoos
"""

from latex import config as cfg
from latex import table_builder, language, bins
import pandas as pd
import os
import json
import shutil

def copy(path):
    src = '/home/windhoos/hout-topologie/latex/'
    dst = path
    
    src1 = os.path.join(src, 'schroeven.png')
    src2 = os.path.join(src, 'hoeken.png')
    src3 = os.path.join(src, 'main-NL.tex')
    src4 = os.path.join(src, 'main-EN.tex')
    
    dst1 = os.path.join(dst, 'schroeven.png')
    dst2 = os.path.join(dst, 'hoeken.png')
    dst3 = os.path.join(dst, 'main-NL.tex')
    dst4 = os.path.join(dst, 'main-EN.tex')
    
    shutil.copyfile(src1, dst1)
    shutil.copyfile(src2, dst2)
    shutil.copyfile(src3, dst3)
    shutil.copyfile(src4, dst4)

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
    
    excel = excel[['type','breedte','dikte','lengte','aantal']]
    
    excel2 = excel.copy()
    lcaption = language.caption(lang, 'stuklijst')
    excel2 = language.rename(excel2, lang, 'stuklijst')
    
    excel2 = excel2.to_latex(index=False, position='h!',na_rep = '', float_format="%.1f", decimal=',',caption=f'{lcaption}')  
    save = 's0-stuklijst_hout.tex'
    path1 = os.path.join(path, save )
    with open(path1, 'w') as fout:
        for i in range(len(excel2)):
            fout.write(excel2[i])
        fout.close()
    
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
        fout.close()
    
    data_elementen=[hoek,scharnier,slot]
    elementen=pd.DataFrame(data_elementen, columns=['gaten raamwerk','aantal'],index=['Hoek verbinding', 'Scharnier', 'Slot'])
    elementen = language.rename(elementen, lang, 'elementen')
    lcaption = language.caption(lang, 'elementen')
    #elementen.to_excel('elementen.xlsx')
    elementen = elementen.to_latex(index=True, position='h!',na_rep = '', float_format="%d", decimal=',',caption=f'{lcaption}')  
    save = 's0-elementen.tex'
    path3 = os.path.join(path, save )
    with open(path3, 'w') as fout:
        for i in range(len(elementen)):
            fout.write(elementen[i])
        fout.close()
            
    #optimaliseer zaaglijst
    # read the content of the file opened
    path4 = os.path.join(path, 'assignment.txt')
    assignment = open(path4)
    assignment = assignment.readlines()
    assignment2 = [x[:-1] for x in assignment]
    name =        assignment2[1]
    email =       assignment2[2]
    lang =        assignment2[3]
    #date =       assignment2[4]
    #time =       assignment2[5]
    kast_data =   json.loads(assignment2[6])
    plank_data =  json.loads(assignment2[7])
    #status =     assignment2[8]
    #bouw plank optimalisatie
    c=plank_data[2]
    w=[]
    for index, row in excel.iterrows():
        if row['type'] == 'plank':
            ammount = row['aantal']
            for i in range(int(ammount)):
                w.append(float(row['lengte']))
    aantal,binlist=bins.firstFitDec(w, c)
    cfg.plank_opt=aantal
    print('aantal planken: ',aantal, ' size: ', c)
    #print(binlist)
    #with open(path4, 'w') as f:
    #    f.truncate()
    #   f.write(str(aantal))
    #    f.write('\n')
    #   f.write(str(w))
    #    f.write('\n')
    #    f.write(str(binlist))
        
    planken_opt=pd.DataFrame(binlist)

    planken_opt.index += 1
    planken_opt.columns += 1

    planken_opt = planken_opt.fillna(0)

    planken_opt = planken_opt.pivot_table(columns=planken_opt.columns.values.tolist(), aggfunc='size')
    
    planken_opt = planken_opt.reset_index()
    planken_opt.index += 1

    planken_opt = planken_opt.rename(index=str,columns={0:'aantal'})
    
    planken_opt = language.rename(planken_opt, lang, 'planken opt')
    lcaption = language.caption(lang, 'planken opt',str(aantal))
    #elementen.to_excel('elementen.xlsx')
    planken_opt = planken_opt.to_latex(index=True, position='h!',na_rep = '', float_format="%.1f", decimal=',',caption=f'{lcaption}')  
    save = 's0-plank_opt.tex'
    path4 = os.path.join(path, save )
    with open(path4, 'w') as fout:
        for i in range(len(planken_opt)):
            fout.write(planken_opt[i])
        fout.close()
    
    #bouw balk optimalisatie
    c=plank_data[5]
    w=[]
    for index, row in excel.iterrows():
        if row['type'] == 'balk':
            ammount = row['aantal']
            for i in range(int(ammount)):
                w.append(float(row['lengte']))
    aantal,binlist=bins.firstFitDec(w, c)
    cfg.balk_opt=aantal
    print('aantal balken: ',aantal, ' size: ', c)
    #path4 = os.path.join(path, 'balk_opt.txt')
    #with open(path4, 'w') as f:
    #   f.truncate()
    #   f.write(str(aantal))
    #   f.write('\n')
    #   f.write(str(w))
    #    f.write('\n')
    #   f.write(str(binlist))
    
    balken_opt=pd.DataFrame(binlist)
    #balken_opt.fillna('-', inplace=True)
    balken_opt.index += 1
    balken_opt.columns += 1
    
    balken_opt = balken_opt.fillna(0)

    balken_opt = balken_opt.pivot_table(columns=balken_opt.columns.values.tolist(), aggfunc='size')
    
    balken_opt = balken_opt.reset_index()
    balken_opt.index += 1

    balken_opt = balken_opt.rename(index=str,columns={0:'aantal'})
    
    balken_opt = language.rename(balken_opt, lang, 'balken opt')
    lcaption = language.caption(lang, 'balken opt',str(aantal))
    #elementen.to_excel('elementen.xlsx')
    balken_opt = balken_opt.to_latex(index=True, position='h!',na_rep = '', float_format="%.1f", decimal=',',caption=f'{lcaption}')  
    save = 's0-balk_opt.tex'
    path5 = os.path.join(path, save )
    with open(path5, 'w') as fout:
        for i in range(len(balken_opt)):
            fout.write(balken_opt[i])
        fout.close()
            
    #maak houtlijst
    data = [['plank',round(plank_data[0],1),round(plank_data[1],1),round(plank_data[2],1),cfg.plank_opt],['balk',round(plank_data[3],1),round(plank_data[4],1),round(plank_data[5],1),cfg.balk_opt]]
    kooplijst = pd.DataFrame(data, columns=['type', 'breedte', 'dikte','lengte', 'aantal'])
    kooplijst = kooplijst.round({'dikte': 1, 'breedte': 1, 'lengte':1})
    kooplijst = kooplijst[['type','breedte','dikte','lengte','aantal']]
    
    lcaption = language.caption(lang, 'kooplijst')
    kooplijst2 = language.rename(kooplijst, lang, 'kooplijst')
    
    kooplijst2 = kooplijst2.to_latex(index=False, position='h!',na_rep = '', float_format="%.0f", decimal=',',caption=f'{lcaption}')  
    save = 's0-kooplijst_hout.tex'
    path6 = os.path.join(path, save )
    with open(path6, 'w') as fout:
        for i in range(len(kooplijst2)):
            fout.write(kooplijst2[i])
        fout.close()
            
    data = [[kast_data[0],kast_data[1],kast_data[2]]]
    kast_afmetingen = pd.DataFrame(data, columns=['breedte','hoogte','diepte'])
    lcaption = language.caption(lang, 'kast afmetingen')
    kast_afmetingen2 = language.rename(kast_afmetingen, lang, 'kast afmetingen')
    kast_afmetingen2 = kast_afmetingen2.to_latex(index=False, position='h!',na_rep = '', float_format="%.1f", decimal=',',caption=f'{lcaption}')  
    save = 's0-kast_afmetingen.tex'
    path7 = os.path.join(path, save )
    with open(path7, 'w') as fout:
        for i in range(len(kast_afmetingen2)):
            fout.write(kast_afmetingen2[i])
        fout.close()
            
    data = [[cfg.aantal_voeten,cfg.poot_hoogte]]
    poten = pd.DataFrame(data, columns=['aantal poten','hoogte'])
    lcaption = language.caption(lang, 'poten')
    poten2 = language.rename(poten, lang, 'poten')
    poten2 = poten2.to_latex(index=False, position='h!',na_rep = '', float_format="%.1f", decimal=',',caption=f'{lcaption}')  
    save = 's0-poten.tex'
    path8 = os.path.join(path, save )
    with open(path8, 'w') as fout:
        for i in range(len(poten2)):
            fout.write(poten2[i])
        fout.close()
    
    save = 'header.tex'
    path9 = os.path.join(path, save )
    lines=language.header(lang,name,email)
    with open(path9, 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
        f.close()
    
    print('Copy files')
    copy(path)
    
    
    print('Start pdf latex')
    if lang == 'NL':
        pdflatex_path = os.path.join(path, 'main-NL.tex' )
    elif lang == 'EN':
        pdflatex_path = os.path.join(path, 'main-EN.tex' )
        
    print(pdflatex_path)
    os.chdir(path)
    os.system("pdflatex %s" % pdflatex_path)
    
    os.system("pdflatex %s" % pdflatex_path)
    
    print('complete')