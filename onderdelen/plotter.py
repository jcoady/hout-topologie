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
from vpython import vertex, vec, quad, color, cylinder, vector, canvas
import time

def multiplot(breedte,hoogte,diepte,amax,aanzicht,Scharnier,*args):
    
    fig = plt.figure(dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    
    teller=0
    
    #scharnieren tekenen
    for plaat in range(len(Scharnier)):
            vlakken = Scharnier[plaat]
            teller=teller+6
            vlakken = Scharnier[0]
            faces = Poly3DCollection(vlakken, linewidths=.1, edgecolors='k')
            faces.set_facecolor((0.1,0,0.1))
            ax.add_collection3d(faces)
    
    #balken tekenen
    for arg in args:
        for balk in range(len(arg)):
            teller=teller+6
            vlakken = arg[balk]
            faces = Poly3DCollection(vlakken, linewidths=.1, edgecolors='k')
            faces.set_facecolor((0.45,0.1,0,1))
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
        
def mayaviplot(breedte,hoogte,diepte,amax,aanzicht,Scharnier,*args):
    mayavi.mlab.figure()
    
    #balken tekenen
    teller=0
    for arg in args:
        for balk in range(len(arg)):
            vlakken = arg[balk]
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
    
    #scharnieren tekenen           
    for plaat in range(len(Scharnier)):
            vlakken = Scharnier[plaat]
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
                print('Voortgang: '+str(int((1000.*teller/cfg.procent))/10.)+'% - Mesh scharnier vlak: '+str(teller))
                
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
    
def vpythonplot(breedte,hoogte,diepte,amax,aanzicht,Scharnier,*args):
    scene = canvas(title='Kast 3D model', width=800, height=600, center=vector(0,0,cfg.hoogte_kast/2.), background=color.white)
    
    scene.forward = vector(0,-1,0)
    scene.up = vector(0,0,1)

    for arg in args:
        for balk in range(len(arg)):
            vlakken = arg[balk]
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
                
                a = vertex( pos=vec(x1,y1,z1) , color=vector(0.4,0.3,0.2))
                b = vertex( pos=vec(x2,y2,z2) , color=vector(0.4,0.3,0.2))
                c = vertex( pos=vec(x3,y3,z3) , color=vector(0.4,0.3,0.2))
                d = vertex( pos=vec(x4,y4,z4) , color=vector(0.4,0.3,0.2))
                Q = quad( v0=a, v1=b, v2=c, v3=d )
                
                rod = cylinder(pos=vector(x1,y1,z1),axis=vector(x2-x1,y2-y1,z2-z2), radius=.3, color=color.black)
                rod = cylinder(pos=vector(x2,y2,z2),axis=vector(x3-x2,y3-y2,z3-z2), radius=.3, color=color.black)
                rod = cylinder(pos=vector(x3,y3,z3),axis=vector(x4-x3,y4-y3,z4-z3), radius=.3, color=color.black)
                rod = cylinder(pos=vector(x4,y4,z4),axis=vector(x1-x4,y1-y4,z1-z4), radius=.3, color=color.black)
                
    #scharnieren tekenen           
    for plaat in range(len(Scharnier)):
            vlakken = Scharnier[plaat]
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

                a = vertex( pos=vec(x1,y1,z1) , color=color.gray(0.5))
                b = vertex( pos=vec(x2,y2,z2) , color=color.gray(0.5))
                c = vertex( pos=vec(x3,y3,z3) , color=color.gray(0.5))
                d = vertex( pos=vec(x4,y4,z4) , color=color.gray(0.5))
                Q = quad( v0=a, v1=b, v2=c, v3=d )
                
                rod = cylinder(pos=vector(x1,y1,z1),axis=vector(x2-x1,y2-y1,z2-z2), radius=.3, color=color.black)
                rod = cylinder(pos=vector(x2,y2,z2),axis=vector(x3-x2,y3-y2,z3-z2), radius=.3, color=color.black)
                rod = cylinder(pos=vector(x3,y3,z3),axis=vector(x4-x3,y4-y3,z4-z3), radius=.3, color=color.black)
                rod = cylinder(pos=vector(x4,y4,z4),axis=vector(x1-x4,y1-y4,z1-z4), radius=.3, color=color.black)
    
    scene.capture('kast-vpython.png')