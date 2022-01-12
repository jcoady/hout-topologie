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
        cfg.breedte_kast=230 #float(input('Wat is de breedte van de kast in cm? '))
        voetjes=str('JA') #str(input('heeft de kast pootjes? [y/n] '))
        if voetjes == ('ja' or 'JA') or ('Ja' or 'YES') or ('yes' or 'Yes') or ('j' or 'y'):
            cfg.hoogte_voet = 10 #float(input('Hoe hoog zijn de pootjes in cm? '))
        else:
            cfg.hoogte_voet = 0.
        cfg.hoogte_kast=250 #float(input('Wat is de hoogte van de kast in cm? '))
        cfg.hoogte_kast=cfg.hoogte_kast-cfg.hoogte_voet
        cfg.diepte_kast=100 #float(input('Wat is de diepte van de kast in cm? '))
        cfg.breedte_plank=20 #float(input('Wat is de breedte van de plank in cm? '))
        cfg.lengte_plank=450 #float(input('Wat is de lengte van de plank in cm? '))
        cfg.dikte_plank=3.2 #float(input('Wat is de dikte van de plank in cm? '))
        cfg.niveaus=1 #int(input('Hoeveel niveaus wil je ? '))
        cfg.tussenschot = 1 #int(input('Hoeveel tussenschotten wil je ? '))
        if cfg.hoogte_kast > cfg.lengte_plank:
            print('De kast is hoger dan de hoogte van de plank dat is niet mogelijk!')
            print('Voer de waarden opnieuw in.')
        if cfg.breedte_kast > cfg.lengte_plank:
            print('De kast is breder dan de hoogte van de plank dat is niet mogelijk!')
            print('Voer de waarden opnieuw in.')
        else:
            indeling_correct = True
    cfg.plankhoogte=[]
    htot=0
    indeling_correct = False
    while indeling_correct == False:
        for niveau in range(cfg.niveaus):
            #print('Er zijn %d niveaus ' % (niveaus))
            if niveau == 0:
                afstand=30# int(input('Wat is de afstand van bodem tot plank %d in cm? ' % (niveau+1)))
                cfg.plankhoogte.append(afstand+cfg.dikte_plank)
                htot=htot+cfg.plankhoogte[niveau]
                print('Er is nu afstand %.1f cm van onder en nog %.1f cm vrije ruimte er boven' % (htot, cfg.hoogte_kast-htot-cfg.dikte_plank))
            else:
                cfg.afstand=30 #float(input('Wat is de afstand tussen plank %d en plank %d in cm? ' % (niveau,niveau+1)))
                if afstand != 0:  
                    cfg.plankhoogte.append(afstand+cfg.dikte_plank)
                    htot=htot+cfg.plankhoogte[niveau]
                print('Er is nu afstand %.1f cm van onder en nog %.1f cm vrije ruimte tot boven' % (htot, cfg.hoogte_kast-htot-cfg.dikte_plank))
        print('Het volgende is nu bekend van de indeling van de kast')
        print('Er zijn %d niveaus in de kast' % (cfg.niveaus+1))
        for niveau in range(cfg.niveaus):
            if niveau == 0:
                print('De afstand tot de grond tot de bovenkant van plank 1 is: %.1f cm' % (cfg.plankhoogte[niveau]))
            else:
                print('De afstand van plank %s tot plank %s is %.1f cm' % (niveau,niveau+1,cfg.plankhoogte[niveau]))
                if niveau == cfg.niveaus-1:
                    print('De afstand van de bovenkant van de bovenste plank tot de onderkant van de bovenplank van de kast is %.1f cm' % (cfg.hoogte_kast-cfg.dikte_plank-htot))
        check='ja' #raw_input('Ben je tevreden met deze waarden ? [Ja/Nee] ')
        if check == ('ja' or 'JA') or ('Ja' or 'YES') or ('yes' or 'Yes') or ('j' or 'y'):
            indeling_correct = True
        print('')