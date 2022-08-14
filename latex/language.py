#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 22:20:22 2022

@author: windhoos
"""

def caption(lang,step,text=None):
    if step == 'stuklijst':
        if lang == 'NL':
            lcaption = 'Stuklijst balken en planken'
        elif lang == 'EN':
            lcaption = 'Partlist beams and planks'
    elif step == 'kast afmetingen':
        if lang == 'NL':
            lcaption = 'Basis afmetingen kast'
        elif lang == 'EN':
            lcaption = 'Basic dimensions closet'
    elif step == 'balken_opt':
        if lang == 'NL':
            lcaption = 'Zaaglijst lengte per balk, Totaal: '+ text + ' balken'
        elif lang == 'EN':
            lcaption = 'Sawlist length per beam, Totalling to '+ text + ' beams'
    elif step == 'planken_opt':
        if lang == 'NL':
            lcaption = 'Zaaglijst lengte per plank, Totaal '+ text + ' planken'
        elif lang == 'EN':
            lcaption = 'Sawlist length per plank, Totalling to '+ text + ' planks'
    elif step == 'poten':
        if lang == 'NL':
            lcaption = 'Eigenschappen van kastpoten'
        elif lang == 'EN':
            lcaption = 'Propperties of closet legs'
    elif step == 'kooplijst':
        if lang == 'NL':
            lcaption = 'Benodigde planken en balken voor constructie'
        elif lang == 'EN':
            lcaption = 'Required planks and beams for construction'
    elif step == 'schroeven':
        if lang == 'NL':
            lcaption = 'Benodigde schroeven voor constructie'
        elif lang == 'EN':
            lcaption = 'Required screws for construction'
    elif step == 'elementen':
        if lang == 'NL':
            lcaption = 'Overige benodigde onderdelen voor constructie'
        elif lang == 'EN':
            lcaption = 'Additional required parts for construction'
    elif step == 1:
        if lang == 'NL':
            lcaption = 'Stap 1 Samenstelling poten en bodem'
        elif lang == 'EN':
            lcaption = 'Step 1 Assembly legs and bottom'
    elif step == 2:
        if lang == 'NL':
            lcaption = 'Stap 2 Samenstellling stap 1 en bodem rib'
        elif lang == 'EN':
            lcaption = 'Step 2 Assembly step 1 and bottom rib'
    elif step == 3:
        if lang == 'NL':
            lcaption = 'Stap 3 Ladder raamwerk'
        elif lang == 'EN':
            lcaption = 'Step 3 Ladder frame'
    elif step == 5:
        if lang == 'NL':
            lcaption = 'Stap 5 Samenstelling stap 2, stap 3 en achter rib'
        elif lang == 'EN':
            lcaption = 'Step 5 Assembly step 2, step 3 and back rib'
    elif step == 6:
        if lang == 'NL':
            lcaption = 'Stap 6 Samenstelling stap 5 en vlonders'
        elif lang == 'EN':
            lcaption = 'Step 6 Assembly step 5 and platforms'
    elif step == 7:
        if lang == 'NL':
            lcaption = 'Stap 7 Samenstelling stap 6 en bovenkant'
        elif lang == 'EN':
            lcaption = 'Step 7 Assembly step 6 and upper side'
    elif step == 8:
        if lang == 'NL':
            lcaption = 'Stap 8 Samenstelling stap 7 en zeiden'
        elif lang == 'EN':
            lcaption = 'Step 8 Assembly step 8 and sides'
    elif step == 9:
        if lang == 'NL':
            lcaption = 'Stap 9 Samenstelling stap 8 en achterkant'
        elif lang == 'EN':
            lcaption = 'Step 9 Assembly step 8 and back side'
    elif step == 10:
        if lang == 'NL':
            lcaption = 'Stap 10 Samenstelling en deurpost(en)'
        elif lang == 'EN':
            lcaption = 'Step 10 Assembly and door frame(s)'
    elif step == 11:
        if lang == 'NL':
            lcaption = 'Stap 11 Deur(en)'
        elif lang == 'EN':
            lcaption = 'Step 11 Door(s)'
    elif step == 12:
        if lang == 'NL':
            lcaption = 'Stap 12 Scharnieren'
        elif lang == 'EN':
            lcaption = 'Step 12 Hinges'
            
    return lcaption

def rename(df,lang,phase):
    if phase == 'steplist' or phase == 'kooplijst' or phase == 'stuklijst':
        if lang == 'EN':
            df = df.rename(columns={'aantal': 'ammount', 'lengte':'length', 'breedte':'width', 'dikte':'thickness'})
            df = df.replace('balk', 'beam',regex=True)
    elif phase == 'poten':
        if lang == 'EN':
            df = df.rename(columns={'aantal poten':'number of legs','hoogte':'height'})
    elif phase == 'planken opt' or phase == 'balken opt':
        if lang == 'EN':
            df = df.rename(columns={'aantal': 'ammount'})
    elif phase == 'schroeven':
        if lang == 'EN':
            df = df.rename(columns={'aantal': 'ammount','max lengte': 'max length'},index={'Schroef 1':'Screw 1', 'Schroef 2':'Screw 2', 'Schroef 3':'Screw 3'})
    elif phase == 'elementen':
        if lang == 'EN':
            df = df.rename(columns={'gaten raamwerk':'frame holes','aantal':'ammount'},index={'Hoek verbinding':'Corner connection', 'Scharnier':'Hinge', 'Slot':'Lock'})
    elif phase == 'kast afmetingen':
        if lang == 'EN':
            df = df.rename(columns={'diepte':'depth', 'breedte':'width', 'hoogte':'height'})
        
    return df
    