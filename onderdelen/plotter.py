#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:49 2022

@author: windhoos
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import mayavi.mlab
import numpy as np

def multiplot(breedte,hoogte,diepte,amax,aanzicht,*args):
    
    fig = plt.figure(dpi=100)
    ax = fig.add_subplot(111, projection='3d')

    for arg in args:
        for balk in range(len(arg)):
            vlakken = arg[balk]
            faces = Poly3DCollection(vlakken, linewidths=.1, edgecolors='k')
            faces.set_facecolor((0.45,0.1,0,1))
            ax.add_collection3d(faces)
            #print('')
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
    print('kast assembly')
    plt.show()
    plt.clf()
        
def mayaviplot(breedte,hoogte,diepte,amax,aanzicht,*args):
    mayavi.mlab.figure()
    
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
    
    mayavi.mlab.show()
    mayavi.mlab.clf()