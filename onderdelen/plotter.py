#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:49 2022

@author: windhoos
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def multiplot(breedte,hoogte,diepte,amax,aanzicht,*args):
    
    fig = plt.figure(dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    
    for arg in args:
        for balk in range(len(arg)):
            vlakken = arg[balk]
            #print('balk: '+str(balk+1))
            #print(vlakken[balk])
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
    
def onderdeelplot(breedte,hoogte,diepte,amax,*args):  
    
    fig = plt.figure(dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    
    for arg in args:
        for balk in range(len(arg)):
            vlakken = arg[balk]
            #print('balk: '+str(balk+1))
            #print(vlakken[balk])
            faces = Poly3DCollection(vlakken, linewidths=.1, edgecolors='k')
            faces.set_facecolor((0.45,0.1,0,1))
            ax.add_collection3d(faces)
            #print('')
    
    plt.title('Kast assembly')
    ax.autoscale(True)
    ax.set_aspect('auto')
    ax.view_init(45, 45)
    #ax.view_init(0, 0)
    ax.set_xlabel('x-as - %s cm' % int(breedte))
    ax.set_ylabel('y-as - %s cm' % int(diepte))
    ax.set_zlabel('z-as - %s cm' % int(hoogte))
    ax.set_xlim(-amax*1.1/2., amax*1.1/2.)
    ax.set_ylim(-amax*1.1/2., amax*1.1/2.)
    ax.set_zlim(0., amax*1.1/2.)
    plt.tight_layout()
    print('kast assembly')
    plt.show()
    plt.clf()