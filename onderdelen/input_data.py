#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:49 2022

@author: windhoos
"""

from onderdelen import config as cfg

def input_data():
    #global breedte_kast,hoogte_kast,diepte_kast,breedte_plank,lengte_plank,dikte_plank,niveaus,tussenschot,plankhoogte,hoogte_voet
    indeling_correct = False
    while indeling_correct == False:
        #cfg.breedte_kast=200#float(input('Wat is de breedte van de kast in cm? '))
        #cfg.hoogte_kast=300#float(input('Wat is de hoogte van de kast in cm? '))
        #cfg.diepte_kast=80#float(input('Wat is de diepte van de kast in cm? '))
        voetjes=str('ja')#str(input('heeft de kast pootjes? [y/n] '))
        if voetjes == ('ja' or 'JA') or ('Ja' or 'YES') or ('yes' or 'Yes') or ('j' or 'y'):
            cfg.hoogte_voet=10#float(input('Hoe hoog zijn de pootjes in cm? '))
        else:
            cfg.hoogte_voet = 0.
        #cfg.hoogte_kast=cfg.hoogte_kast
        cfg.breedte_plank=30.#float(input('Wat is de breedte van de plank in cm? '))
        cfg.lengte_plank=600.#float(input('Wat is de lengte van de plank in cm? '))
        cfg.dikte_plank=3.2#float(input('Wat is de dikte van de plank in cm? '))
        cfg.niveaus=3#int(input('Hoeveel niveaus wil je ? '))
        #cfg.tussenschot =int(input('Hoeveel tussenschotten wil je ? '))
        if cfg.hoogte_kast > cfg.lengte_plank:
            print('De kast is hoger dan de hoogte van de plank dat is niet mogelijk!')
            print('Voer de waarden opnieuw in.')
        if cfg.breedte_kast > cfg.lengte_plank:
            print('De kast is breder dan de hoogte van de plank dat is niet mogelijk!')
            print('Voer de waarden opnieuw in.')
        else:
            indeling_correct = True
    
    indeling_correct=False
    while indeling_correct == False:
        cfg.plankhoogte=[]
        print('Totale hoogte van de kast is %.1f cm' % (cfg.hoogte_kast))
        if cfg.hoogte_voet != 0:
            print('Hoogte van het voetje is %.1f cm' % (cfg.hoogte_voet))
        print('Hoogte onderste plank van kast is %.1f cm' % (cfg.hoogte_voet+cfg.dikte_plank))
        cfg.plankhoogte.append(cfg.hoogte_voet+cfg.dikte_plank)
        niveau=0
        max_planken = False
        while max_planken == False:
            print('Er is nog %.1f cm ruimte boven de plank' % (cfg.hoogte_kast - cfg.dikte_plank - cfg.plankhoogte[niveau]))
            cfg.plankhoogte.append(100)#float(input('Wat is de afstand tot de onderkant van de volgende plank in cm ? '))+cfg.dikte_plank+cfg.plankhoogte[niveau])
            print('Er is nog %.1f cm ruimte boven de plank' % (cfg.hoogte_kast - cfg.dikte_plank - cfg.plankhoogte[-1]))
            check='N'#input('Moet er nog een plank worden toegevoegd ? Y/N '))
            if check == 'N':
                max_planken = True
            niveau=niveau+1
        check='Y' #input('Bent u tevreden met deze indeling ? Y/N '))
        if check == 'Y':
            indeling_correct = True
            
    del cfg.plankhoogte[0]
    cfg.niveaus = len(cfg.plankhoogte)