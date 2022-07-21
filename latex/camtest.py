#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 22:15:08 2022

@author: windhoos
"""

from vpython import vector,cone,cylinder,text, canvas

def origin(O):
    xp = cylinder(pos=O, axis=vector(1,0,0), radius=10, color=vector(1,0,0), length=50)
    Ox=O+vector(50,0,0)
    xc = cone(pos=Ox, axis=vector(1,0,0),radius=20, color=vector(1,0,0), length = 20)
    xt = text(text='x', pos = xc.pos + xc.axis +vector(10,0,0),align='center', color=vector(1,0,0), axis=vector(1,0,0), height = 20)
    
    yp = cylinder(pos=O, axis=vector(0,1,0), radius=10, color=vector(0,1,0), length=50)
    Oy=O+vector(0,50,0)
    yc = cone(pos=Oy, axis=vector(0,1,0),radius=20, color=vector(0,1,0), length = 20)
    yt = text(text='y', pos = yc.pos + yc.axis +vector(0,10,0),align='center', color=vector(0,1,0),axis=vector(0,1,0),  height = 20)
    
    zp = cylinder(pos=O, axis=vector(0,0,1), radius=10, color=vector(0,0,1), length=50)
    Oz=O+vector(0,0,50)
    zc = cone(pos=Oz, axis=vector(0,0,1),radius=20, color=vector(0,0,1), length = 20)
    zt = text(text='z', pos = zc.pos + zc.axis +vector(0,0,10),align='center', axis=vector(0,0,1), color=vector(0,0,1), height = 20)
    
def main():
    global sl
    sl = canvas(width=800, height=600, center=vector(0,0,0), background=vector(1,1,1))
    sl.autoscale = False
    
    O=vector(0,0,0)
    origin(O)
    
    print('sl.center')
    sl.center = vector(0,0,0)
    print(0,0,0)
    print(sl.center)
        
    print('sl.camera.pos')
    sl.camera.pos = vector(200,0,0)
    print(200,0,0)
    print(sl.camera.pos)
    
    print('sl.camera.axis')
    sl.camera.axis = vector(-200,0,0)
    print(-200,0,0)
    print(sl.camera.axis)
    
    sl.up = vector(0,0,1)
    
main()