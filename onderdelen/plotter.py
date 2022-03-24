#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:49 2022

@author: windhoos
"""

from onderdelen import config as cfg

#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d.art3d import Poly3DCollection
#import mayavi.mlab
from vpython import vertex, vec, quad, color, cylinder, vector, canvas, checkbox, button, slider,wtext,menu,winput

def build_scene():
    global scene
    scene = canvas(title='Kast 3D model \n\n', width=800, height=600, center=vector(0,0,0), background=color.white)
    scene.userzoom = False
    scene.userpan = False
    
    scene.append_to_title('width ')
    winput( bind=input_raam , width=56, pos=scene.title_anchor, id=1)
    scene.append_to_title(' cm , height ')
    winput( bind=input_raam , width=56, pos=scene.title_anchor, id=2)
    scene.append_to_title(' cm , depth ')
    winput( bind=input_raam , width=56, pos=scene.title_anchor,id=3)
    scene.append_to_title(' cm ')
    build_knop=button(text='BUILD', bind=building, pos=scene.title_anchor)
    scene.append_to_title(' ')
    reset_knop=button(text='RESET', bind=reset, pos=scene.title_anchor)
    scene.append_to_title(' ')
    plank_knop=button(text='Add plank \n', bind=knop_niveau ,pos=scene.title_anchor)
    scene.append_to_title(' ')
    menu_knop=menu(choices=['Door closed', 'Door open', 'Door gone'], index=0, bind=menu_deur,pos=scene.title_anchor)
    
    scene.forward = vector(0,-1,0)
    scene.up = vector(0,0,1)
    
    scene.autoscale = True
    
    reset_knop.disabled = True
    menu_knop.disabled = True
    plank_knop.disabled = True
    
    cfg.knoppen=[build_knop,reset_knop,plank_knop,menu_knop]
   
def vpythonplot(breedte,hoogte,diepte,amax,aanzicht,Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Voorkant120,Scharnier,Scharnier120):
    matrix=[Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Voorkant120, Scharnier, Scharnier120]
    #cfg.matrix=matrix
    graphics=[]
    
    for part in range(len(matrix)):
        #print(part)
        graphics.append([])
        if part == 9:
            kleur=color.gray(0.5)
        elif part == 10:
            kleur=color.gray(0.5)
        else:
            kleur=vector(0.4,0.3,0.2)
            
        for balk in range(len(matrix[part])):
            graphics[part].append([])
            vlakken = matrix[part][balk]
            for i in range(6):
                #graphics[part][balk].append([])
                x1=vlakken[i][0][0]
                x2=vlakken[i][1][0]
                x3=vlakken[i][2][0]
                x4=vlakken[i][3][0]
                y1=vlakken[i][0][1]
                y2=vlakken[i][1][1]
                y3=vlakken[i][2][1]
                y4=vlakken[i][3][1]
                z1=vlakken[i][0][2] - cfg.hoogte_kast/2.
                z2=vlakken[i][1][2] - cfg.hoogte_kast/2.
                z3=vlakken[i][2][2] - cfg.hoogte_kast/2.
                z4=vlakken[i][3][2] - cfg.hoogte_kast/2.
    
                a = vertex( pos=vec(x1,y1,z1) , color=kleur)
                b = vertex( pos=vec(x2,y2,z2) , color=kleur)
                c = vertex( pos=vec(x3,y3,z3) , color=kleur)
                d = vertex( pos=vec(x4,y4,z4) , color=kleur)
                Q = quad( v0=a, v1=b, v2=c, v3=d)
                    
                rod1 = cylinder(pos=vector(x1,y1,z1),axis=vector(x2-x1,y2-y1,z2-z2), radius=.3, color=color.black)
                rod2 = cylinder(pos=vector(x2,y2,z2),axis=vector(x3-x2,y3-y2,z3-z2), radius=.3, color=color.black)
                rod3 = cylinder(pos=vector(x3,y3,z3),axis=vector(x4-x3,y4-y3,z4-z3), radius=.3, color=color.black)
                rod4 = cylinder(pos=vector(x4,y4,z4),axis=vector(x1-x4,y1-y4,z1-z4), radius=.3, color=color.black)
                
                if part == 8:
                    Q.visible = False
                    rod1.visible = False
                    rod2.visible = False
                    rod3.visible = False
                    rod4.visible = False
                elif part == 10:
                    Q.visible = False
                    rod1.visible = False
                    rod2.visible = False
                    rod3.visible = False
                    rod4.visible = False
                
                graphics[part][balk].append([Q,rod1,rod2,rod3,rod4])
            
    cfg.graphics = graphics.copy()

    #sl = slider(min=cfg.hoogte_voet+cfg.dikte_plank , max=cfg.hoogte_kast-cfg.dikte_plank, value=cfg.hoogte_voet+cfg.dikte_plank+10., length=640, bind=setspeed, right=15, step=.1,id=1)
    sl = slider(min=cfg.breedte_rib*2+cfg.dikte_plank , max=cfg.hoogte_kast-cfg.dikte_plank-cfg.breedte_rib-cfg.hoogte_voet-cfg.dikte_plank, value=cfg.breedte_rib*2+cfg.dikte_plank, length=640, bind=setspeed, right=15, step=.1,id=1)
    wt = wtext(text='{:1.2f}'.format(sl.value),id=1)
    #scene.append_to_caption(' cm tov grond')
    #cfg.sliders.append([0,0,sl,wt])
    cfg.sliders_update.append([cfg.niveaus,sl.value,sl,wt])
    
def input_raam(s): 
    if s.id == 1:
        cfg.breedte_kast=s.number
    elif s.id == 2:
        cfg.hoogte_kast=s.number
    elif s.id == 3:
        cfg.diepte_kast=s.number
        
def menu_deur(m):
    val = m.selected
    voorkant=cfg.graphics[7]
    voorkant120=cfg.graphics[8]
    scharnier=cfg.graphics[9]
    scharnier120=cfg.graphics[10]
    if val == 'Door closed': 
        opacity(voorkant,True)
        opacity(voorkant120,False)
        opacity(scharnier,True)
        opacity(scharnier120,False)
    elif val == 'Door open': 
        opacity(voorkant,False)
        opacity(voorkant120,True)
        opacity(scharnier,False)
        opacity(scharnier120,True)
    elif val == 'Door gone': 
        opacity(voorkant,False)
        opacity(voorkant120,False)
        opacity(scharnier,False)
        opacity(scharnier120,False)
    
def opacity(element,TF):
    for balk in range(len(element)):
        for i in range(6):
            Q=element[balk][i][0]
            rod1=element[balk][i][1]
            rod2=element[balk][i][2]
            rod3=element[balk][i][3]
            rod4=element[balk][i][4]
            Q.visible = TF
            rod1.visible = TF
            rod2.visible = TF
            rod3.visible = TF
            rod4.visible = TF
            
def knop_niveau(b):
    niveaus=cfg.niveaus+1
    print('knop - added niveau',niveaus)
    scene.append_to_caption('\n \n')
    sl = slider(min=cfg.breedte_rib*2+cfg.dikte_plank , max=cfg.hoogte_kast-cfg.dikte_plank-cfg.breedte_rib-cfg.hoogte_voet-cfg.dikte_plank, value=cfg.breedte_rib*2+cfg.dikte_plank, length=640, bind=setspeed, right=15, step=.1,id=niveaus)
    wt = wtext(text='{:1.2f}'.format(sl.value),id=niveaus)
    #sl = slider(min=cfg.hoogte_voet+cfg.dikte_plank , max=cfg.hoogte_kast-cfg.dikte_plank, value=cfg.hoogte_voet+cfg.dikte_plank+10., length=640, bind=setspeed, right=15, step=.1,id=niveaus)
    #wt = wtext(text='{:1.2f}'.format(sl.value-(cfg.hoogte_voet+cfg.dikte_plank)),id=niveaus)
    #scene.append_to_caption(' cm tov grond')
    #cfg.sliders_update.append([niveaus,sl.value,sl,wt])
    cfg.sliders_update.append([cfg.niveaus,sl.value,sl,wt])
    cfg.update_graph=True
    
def reset(b):
    print('RESET')
    print('WERKT NOG NIET')
    #TODO: RESET KNOP MAKEN
    '''
    cfg.reset=True
    for i in range(len(cfg.sliders_update)):
        cfg.sliders_update[i][2].delete()
        cfg.sliders_update[i][3].delete()
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
    
    cfg.knoppen[0].disabled = False
    cfg.knoppen[1].disabled = True
    cfg.knoppen[2].disabled = True
    cfg.knoppen[3].disabled = True
    '''
    
def building(b):
    print('BUILD')
    #cfg.knoppen=[build_knop,reset_knop,plank_knop,menu_knop]
    if ((isinstance(cfg.breedte_kast, (int,float)) and isinstance(cfg.hoogte_kast, (int,float))) and isinstance(cfg.diepte_kast, (int,float))):
        if ((cfg.breedte_kast >= 45. and cfg.hoogte_kast >= 100.) and cfg.diepte_kast >= 25):
            cfg.build_state = True
            cfg.knoppen[0].disabled = True
            cfg.knoppen[1].disabled = False
            cfg.knoppen[2].disabled = False
            cfg.knoppen[3].disabled = False    
    
def setspeed(s):
    cfg.sliders_update[s.id-1][0]=s.id
    cfg.sliders_update[s.id-1][1]=s.value
    #wt = wtext(text='{:1.2f}'.format(s.value),id=s.id)
    wt=cfg.sliders_update[s.id-1][3]
    wt.text = '{:1.2f}'.format(s.value)
    cfg.update_graph=True
        
def plotniveau(Ribben,Vlonders,Achterrib):
    matrix=[Ribben,Vlonders,Achterrib]
    
    graphics_new=[]

    for part in range(len(matrix)):
        graphics_new.append([])
        kleur=vector(0.4,0.3,0.2)
            
        for balk in range(len(matrix[part])):
            graphics_new[part].append([])
            vlakken = matrix[part][balk]
            for i in range(6):
                x1=vlakken[i][0][0]
                x2=vlakken[i][1][0]
                x3=vlakken[i][2][0]
                x4=vlakken[i][3][0]
                y1=vlakken[i][0][1]
                y2=vlakken[i][1][1]
                y3=vlakken[i][2][1]
                y4=vlakken[i][3][1]
                z1=vlakken[i][0][2] - cfg.hoogte_kast/2.
                z2=vlakken[i][1][2] - cfg.hoogte_kast/2.
                z3=vlakken[i][2][2] - cfg.hoogte_kast/2.
                z4=vlakken[i][3][2] - cfg.hoogte_kast/2.
    
                a = vertex( pos=vec(x1,y1,z1) , color=kleur)
                b = vertex( pos=vec(x2,y2,z2) , color=kleur)
                c = vertex( pos=vec(x3,y3,z3) , color=kleur)
                d = vertex( pos=vec(x4,y4,z4) , color=kleur)
                Q = quad( v0=a, v1=b, v2=c, v3=d)
                    
                rod1 = cylinder(pos=vector(x1,y1,z1),axis=vector(x2-x1,y2-y1,z2-z2), radius=.3, color=color.black)
                rod2 = cylinder(pos=vector(x2,y2,z2),axis=vector(x3-x2,y3-y2,z3-z2), radius=.3, color=color.black)
                rod3 = cylinder(pos=vector(x3,y3,z3),axis=vector(x4-x3,y4-y3,z4-z3), radius=.3, color=color.black)
                rod4 = cylinder(pos=vector(x4,y4,z4),axis=vector(x1-x4,y1-y4,z1-z4), radius=.3, color=color.black)
                
                if part == 0:
                    #print(part,balk,i)
                    #print(cfg.graphics[2])
                    try:
                        cfg.graphics[2][balk][i][0].visible=False
                        cfg.graphics[2][balk][i][1].visible=False
                        cfg.graphics[2][balk][i][2].visible=False
                        cfg.graphics[2][balk][i][3].visible=False
                        cfg.graphics[2][balk][i][4].visible=False
                    except IndexError:
                        #break
                        pass
                elif part == 1:
                    try:
                        cfg.graphics[5][balk][i][0].visible=False
                        cfg.graphics[5][balk][i][1].visible=False
                        cfg.graphics[5][balk][i][2].visible=False
                        cfg.graphics[5][balk][i][3].visible=False
                        cfg.graphics[5][balk][i][4].visible=False
                    except IndexError:
                        #break
                        pass
                elif part == 2:
                    try:
                        cfg.graphics[6][balk][i][0].visible=False
                        cfg.graphics[6][balk][i][1].visible=False
                        cfg.graphics[6][balk][i][2].visible=False
                        cfg.graphics[6][balk][i][3].visible=False
                        cfg.graphics[6][balk][i][4].visible=False
                    except IndexError:
                        #break
                        pass
                
                graphics_new[part][balk].append([Q,rod1,rod2,rod3,rod4])
                
    cfg.graphics[2]=graphics_new[0].copy()
    cfg.graphics[5]=graphics_new[1].copy()
    cfg.graphics[6]=graphics_new[2].copy()