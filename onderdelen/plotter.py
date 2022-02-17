#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:49 2022

@author: windhoos
"""

from onderdelen import config as cfg

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import mayavi.mlab
from vpython import vertex, vec, quad, color, cylinder, vector, canvas, checkbox, button, slider,wtext,menu
import time

def multiplot(breedte,hoogte,diepte,amax,aanzicht,Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Voorkant120,Scharnier,Scharnier120):
    
    fig = plt.figure(dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    
    teller=0
    
    matrix=[Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Voorkant120,Scharnier,Scharnier120]
    
    for part in range(len(matrix)):
        for balk in range(len(matrix[part])):
            vlakken = matrix[part][balk]
            if part != len(matrix)-1:
                teller=teller+6
                vlakken = matrix[part][balk]
                faces = Poly3DCollection(vlakken, linewidths=.1, edgecolors='k')
                faces.set_facecolor((0.45,0.1,0,1))
                ax.add_collection3d(faces)
            else:
                teller=teller+6
                vlakken = matrix[part][balk]
                faces = Poly3DCollection(vlakken, linewidths=.1, edgecolors='k')
                faces.set_facecolor((0.1,0,0.1))
                ax.add_collection3d(faces)

    cfg.procent=teller
    plt.title('Kast assembly')
    ax.autoscale(True)
    ax.set_aspect('auto')
    if aanzicht == 'zij':
        ax.view_init(0,0)
    elif aanzicht == 'boven':
        ax.view_init(90,0)
    elif aanzicht == 'voor':
        ax.view_init(0,90)
    else:
        ax.view_init(45,45)
    #ax.view_init(0, 0)
    ax.set_xlabel('x-as - %s cm' % int(breedte))
    ax.set_ylabel('y-as - %s cm' % int(diepte))
    ax.set_zlabel('z-as - %s cm' % int(hoogte))
    ax.set_xlim(-amax*1.1/2., amax*1.1/2.)
    ax.set_ylim(-amax*1.1/2., amax*1.1/2.)
    ax.set_zlim(0., amax*1.1)
    plt.tight_layout()
    plt.savefig('kast-matplotlib.png', dpi=300)
    plt.show()
    plt.clf()
        
def mayaviplot(breedte,hoogte,diepte,amax,aanzicht,Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Voorkant120,Scharnier,Scharnier120):
    mayavi.mlab.figure()
    
    #balken tekenen
    teller=0
    matrix=[Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Voorkant120,Scharnier,Scharnier120]
    
    for part in range(len(matrix)):
        for balk in range(len(matrix[part])):
            vlakken = matrix[part][balk]
            for i in range(6):
                x1=vlakken[i][0][0]
                x2=vlakken[i][1][0]
                x4=vlakken[i][2][0]
                x3=vlakken[i][3][0]
                y1=vlakken[i][0][1]
                y2=vlakken[i][1][1]
                y4=vlakken[i][2][1]
                y3=vlakken[i][3][1]
                z1=vlakken[i][0][2]
                z2=vlakken[i][1][2]
                z4=vlakken[i][2][2]
                z3=vlakken[i][3][2]
                teller=teller+1

                print('Voortgang: '+str(int((1000.*teller/cfg.procent))/10.)+'% - Mesh balk vlak: '+str(teller))
                if part != len(matrix)-1:
                    mayavi.mlab.mesh([[x1, x2],
                                  [x3, x4]],  # | => x coordinate
                
                                 [[y1, y2],
                                  [y3, y4]],  # | => y coordinate
                
                                 [[z1, z2],
                                  [z3, z4]],  # | => z coordinate
    
                                 color=(0.4,0.3,0.2))  # brown
                    
                    mayavi.mlab.plot3d([x1, x2],  # | => x coordinate
                                       [y1, y2],  # | => y coordinate
                                       [z1, z2],  # | => z coordinate
                                       
                                       color=(0,0,0), tube_radius=.15)
                    
                    mayavi.mlab.plot3d([x2, x4],  # | => x coordinate
                                       [y2, y4],  # | => y coordinate
                                       [z2, z4],  # | => z coordinate
                                       
                                       color=(0,0,0), tube_radius=.15)
                    
                    mayavi.mlab.plot3d([x4, x3],  # | => x coordinate
                                       [y4, y3],  # | => y coordinate
                                       [z4, z3],  # | => z coordinate
                                       
                                       color=(0,0,0), tube_radius=.15)
                    
                    mayavi.mlab.plot3d([x3, x1],  # | => x coordinate
                                       [y3, y1],  # | => y coordinate
                                       [z3, z1],  # | => z coordinate
                                       
                                       color=(0,0,0), tube_radius=.15)
                else:
                    mayavi.mlab.mesh([[x1, x2],
                                  [x3, x4]],  # | => x coordinate
                
                                 [[y1, y2],
                                  [y3, y4]],  # | => y coordinate
                
                                 [[z1, z2],
                                  [z3, z4]],  # | => z coordinate
    
                                 color=(0.1,0.,0.1))  # black
                    
                    mayavi.mlab.plot3d([x1, x2],  # | => x coordinate
                                       [y1, y2],  # | => y coordinate
                                       [z1, z2],  # | => z coordinate
                                       
                                       color=(0,0,0), tube_radius=.15)
                    
                    mayavi.mlab.plot3d([x2, x4],  # | => x coordinate
                                       [y2, y4],  # | => y coordinate
                                       [z2, z4],  # | => z coordinate
                                       
                                       color=(0,0,0), tube_radius=.15)
                    
                    mayavi.mlab.plot3d([x4, x3],  # | => x coordinate
                                       [y4, y3],  # | => y coordinate
                                       [z4, z3],  # | => z coordinate
                                       
                                       color=(0,0,0), tube_radius=.15)
                    
                    mayavi.mlab.plot3d([x3, x1],  # | => x coordinate
                                       [y3, y1],  # | => y coordinate
                                       [z3, z1],  # | => z coordinate
                                       
                                       color=(0,0,0), tube_radius=.15)
                
    #mayavi.mlab.axes(xlabel='x-as - %s cm' % int(breedte), ylabel='y-as - %s cm' % int(diepte), zlabel='z-as - %s cm' % int(hoogte))
    mayavi.mlab.savefig(filename='kast-mayavi.png')
    cfg.end = time.time()
    m, s = divmod(cfg.end-cfg.start, 60)
    print("Render mayavi afgerond")
    print("Runtime van programma is "+str(int(m))+ " : " + str(int(s)))
    mayavi.mlab.show()
    #mayavi.mlab.close()
    
def vpythonplot(breedte,hoogte,diepte,amax,aanzicht,Voeten,Onderstel,Ribben,Zeiden,Achterplank,Vlonders,Achterrib, Voorkant, Voorkant120,Scharnier,Scharnier120):
    global scene
    scene = canvas(title='Kast 3D model', width=800, height=600, center=vector(0,0,cfg.hoogte_kast/2.), background=color.white)
    
    scene.forward = vector(0,-1,0)
    scene.up = vector(0,0,1)
    
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
                z1=vlakken[i][0][2] 
                z2=vlakken[i][1][2] 
                z3=vlakken[i][2][2]
                z4=vlakken[i][3][2] 
    
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
                
    cfg.graphics=graphics
    
    #scene.capture('kast-vpython.png')
    scene.caption = "Vul hier onder je informatie in: \n\n"
    menu(choices=['Deur dicht', 'Deur open', 'Deur weg'], index=0, bind=M)
    scene.append_to_caption('\n\n')
    button(text='Voeg plank toe \n', bind=knop)
    sl = slider(min=cfg.hoogte_voet+cfg.dikte_plank , max=cfg.hoogte_kast-cfg.dikte_plank, value=cfg.hoogte_voet+cfg.dikte_plank+100., length=640, bind=setspeed, right=15, step=.1,id=1)
    wt = wtext(text='{:1.2f}'.format(sl.value),id=1)
    #cfg.sliders.append([0,0,sl,wt])
    cfg.sliders_update.append([cfg.niveaus,sl.value,sl,wt])
        
def M(m):
    val = m.selected
    voorkant=cfg.graphics[7]
    voorkant120=cfg.graphics[8]
    scharnier=cfg.graphics[9]
    scharnier120=cfg.graphics[10]
    if val == 'Deur dicht': 
        opacity(voorkant,True)
        opacity(voorkant120,False)
        opacity(scharnier,True)
        opacity(scharnier120,False)
    elif val == 'Deur open': 
        opacity(voorkant,False)
        opacity(voorkant120,True)
        opacity(scharnier,False)
        opacity(scharnier120,True)
    elif val == 'Deur weg': 
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
            
def knop(b):
    niveaus=cfg.niveaus+1
    print('knop - added niveau',niveaus)
    scene.append_to_caption('\n \n')
    sl = slider(min=cfg.hoogte_voet+cfg.dikte_plank , max=cfg.hoogte_kast-cfg.dikte_plank, value=cfg.hoogte_voet+cfg.dikte_plank+100., length=640, bind=setspeed, right=15, step=.1,id=niveaus)
    wt = wtext(text='{:1.2f}'.format(sl.value),id=niveaus)
    cfg.sliders_update.append([niveaus,sl.value,sl,wt])
    
    
def setspeed(s):
    cfg.sliders_update[s.id-1][0]=s.id
    cfg.sliders_update[s.id-1][1]=s.value
        
def plotniveau(Ribben,Vlonders,Achterrib):
    
    matrix=[Ribben,Vlonders,Achterrib]
    
    graphics=[]

    for part in range(len(matrix)):
        graphics.append([])
        kleur=vector(0.4,0.3,0.2)
            
        for balk in range(len(matrix[part])):
            graphics[part].append([])
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
                z1=vlakken[i][0][2] 
                z2=vlakken[i][1][2] 
                z3=vlakken[i][2][2]
                z4=vlakken[i][3][2] 
    
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
                    cfg.graphics[2][balk][i][1].visible=False
                    cfg.graphics[2][balk][i][2].visible=False
                    cfg.graphics[2][balk][i][3].visible=False
                    cfg.graphics[2][balk][i][4].visible=False
                elif part == 1:
                    cfg.graphics[5][balk][i][0].visible=False
                    cfg.graphics[5][balk][i][1].visible=False
                    cfg.graphics[5][balk][i][2].visible=False
                    cfg.graphics[5][balk][i][3].visible=False
                    cfg.graphics[5][balk][i][4].visible=False
                elif part == 2:
                    cfg.graphics[6][balk][i][0].visible=False
                    cfg.graphics[6][balk][i][1].visible=False
                    cfg.graphics[6][balk][i][2].visible=False
                    cfg.graphics[6][balk][i][3].visible=False
                    cfg.graphics[6][balk][i][4].visible=False
                
                graphics[part][balk].append([Q,rod1,rod2,rod3,rod4])
                
    for part in range(len(matrix)):
        for balk in range(len(matrix[part])):
            for i in range(6):
                if part == 0:
                    #print(cfg.graphics[2][balk][i])
                    del cfg.graphics[2][balk][i][4]
                    del cfg.graphics[2][balk][i][3]
                    del cfg.graphics[2][balk][i][2]
                    del cfg.graphics[2][balk][i][1]
                    del cfg.graphics[2][balk][i][0]
                    cfg.graphics[2][balk][i].append(graphics[part][balk][i][0])
                    cfg.graphics[2][balk][i].append(graphics[part][balk][i][1])
                    cfg.graphics[2][balk][i].append(graphics[part][balk][i][2])
                    cfg.graphics[2][balk][i].append(graphics[part][balk][i][3])
                    cfg.graphics[2][balk][i].append(graphics[part][balk][i][4])
                elif part == 1:
                    del cfg.graphics[5][balk][i][4]
                    del cfg.graphics[5][balk][i][3]
                    del cfg.graphics[5][balk][i][2]
                    del cfg.graphics[5][balk][i][1]
                    del cfg.graphics[5][balk][i][0]
                    cfg.graphics[5][balk][i].append(graphics[part][balk][i][0])
                    cfg.graphics[5][balk][i].append(graphics[part][balk][i][1])
                    cfg.graphics[5][balk][i].append(graphics[part][balk][i][2])
                    cfg.graphics[5][balk][i].append(graphics[part][balk][i][3])
                    cfg.graphics[5][balk][i].append(graphics[part][balk][i][4])
                elif part == 2:
                    del cfg.graphics[6][balk][i][4]
                    del cfg.graphics[6][balk][i][3]
                    del cfg.graphics[6][balk][i][2]
                    del cfg.graphics[6][balk][i][1]
                    del cfg.graphics[6][balk][i][0]
                    cfg.graphics[6][balk][i].append(graphics[part][balk][i][0])
                    cfg.graphics[6][balk][i].append(graphics[part][balk][i][1])
                    cfg.graphics[6][balk][i].append(graphics[part][balk][i][2])
                    cfg.graphics[6][balk][i].append(graphics[part][balk][i][3])
                    cfg.graphics[6][balk][i].append(graphics[part][balk][i][4])
