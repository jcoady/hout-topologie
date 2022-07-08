#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 22:12:02 2022

@author: windhoos
"""

from vpython import box,vector,cylinder
import numpy as np
from scipy.spatial.transform import Rotation as R

def s(a,b):
    c1=a[0]-b[0]
    c2=a[1]-b[1]
    c3=a[2]-b[2]
    #c=np.substract(a,b)
    return c1,c2,c3

def r(point,axis,angle):
    vec = point #[1,1,1]
    rotation_degrees = angle
    rotation_radians = np.radians(rotation_degrees)
    rotation_axis = np.array(axis) #np.array([0, 0, 1])
    rotation_vector = rotation_radians * rotation_axis
    rotation = R.from_rotvec(rotation_vector)
    rotated_vec = rotation.apply(vec)
    
    return rotated_vec

def rotate(p,xa,ya,za):
    p=[p[0],p[1],p[2]]
    p=r(p,[1,0,0],xa)
    p=r(p,[0,1,0],ya)
    p=r(p,[0,0,1],za)
    p=p[0],p[1],p[2]
    return p

def construct(x0,y0,z0,l,w,h,xa,ya,za):
    '''
           __________________________
          /                         /|
    ___  /_________________________/ |
     |   |         |z             |  |
     |   |         |_____ x       |  |  |
   H |   |        /               | /  /|
    _|_  |_______/_y______________|/  /W
                                    |/
         |-----------L------------| |
    '''
    
    '''
              z|_x
               \y
         
          ____________
         3\           \2
         4\___________\1
          |___________|
         7\           \6
         8\___________\5
    '''
    
    px1=x0+l/2
    py1=y0+w/2
    pz1=z0+h/2
    
    px2=x0+l/2
    py2=y0-w/2
    pz2=z0+h/2
    
    px3=x0-l/2
    py3=y0-w/2
    pz3=z0+h/2
    
    px4=x0-l/2
    py4=y0+w/2
    pz4=z0+h/2
    
    px5=x0+l/2
    py5=y0+w/2
    pz5=z0-h/2
    
    px6=x0+l/2
    py6=y0-w/2
    pz6=z0-h/2
    
    px7=x0-l/2
    py7=y0-w/2
    pz7=z0-h/2
    
    px8=x0-l/2
    py8=y0+w/2
    pz8=z0-h/2
        
    p0=x0,y0,z0
    p1=px1,py1,pz1
    p2=px2,py2,pz2
    p3=px3,py3,pz3
    p4=px4,py4,pz4
    p5=px5,py5,pz5
    p6=px6,py6,pz6
    p7=px7,py7,pz7
    p8=px8,py8,pz8
    
    paxis=x0+1,y0,z0
    pup=x0,y0,z0+1
    
    paxis=rotate(paxis,xa,ya,za)
    pup=rotate(pup,xa,ya,za)
    
    p1=rotate(p1,xa,ya,za)
    p2=rotate(p2,xa,ya,za)
    p3=rotate(p3,xa,ya,za)
    p4=rotate(p4,xa,ya,za)
    p5=rotate(p5,xa,ya,za)
    p6=rotate(p6,xa,ya,za)
    p7=rotate(p7,xa,ya,za)
    p8=rotate(p8,xa,ya,za)
    
    kleur =  vector(0.4,0.3,0.2)
    d1,d2,d3=s(p0,paxis)
    d4,d5,d6=s(p0,pup)
    balk =   box(pos=vector(x0,y0,z0), size=vector(l,h,w) , axis=vector(d1,d2,d3),up=vector(d4,d5,d6),color=kleur)
    balk.rotate(angle=xa,axis=vector(1,0,0),origin=vector(x0,y0,z0))
    balk.rotate(angle=ya,axis=vector(0,1,0),origin=vector(x0,y0,z0))
    balk.rotate(angle=za,axis=vector(0,0,1),origin=vector(x0,y0,z0))
    
    d1,d2,d3=s(p2,p1)
    rand1 =  cylinder(pos=vector(p1[0],p1[1],p1[2]),         axis=vector(d1,d2,d3), radius=.1,color=vector(0,0,0))
    
    d1,d2,d3=s(p3,p2)
    rand2 =  cylinder(pos=vector(p2[0],p2[1],p2[2]),         axis=vector(d1,d2,d3), radius=.1,color=vector(0,0,0))
    
    d1,d2,d3=s(p4,p3)
    rand3 =  cylinder(pos=vector(p3[0],p3[1],p3[2]),         axis=vector(d1,d2,d3), radius=.1,color=vector(0,0,0))
    
    d1,d2,d3=s(p4,p1)
    rand4 =  cylinder(pos=vector(p1[0],p1[1],p1[2]),         axis=vector(d1,d2,d3), radius=.1,color=vector(0,0,0))
    
    d1,d2,d3=s(p6,p5)
    rand5 =  cylinder(pos=vector(p5[0],p5[1],p5[2]),         axis=vector(d1,d2,d3), radius=.1,color=vector(0,0,0))
    
    d1,d2,d3=s(p7,p6)
    rand6 =  cylinder(pos=vector(p6[0],p6[1],p6[2]),         axis=vector(d1,d2,d3), radius=.1,color=vector(0,0,0))
    
    d1,d2,d3=s(p8,p7)
    rand7 =  cylinder(pos=vector(p7[0],p7[1],p7[2]),         axis=vector(d1,d2,d3), radius=.1,color=vector(0,0,0))
    
    d1,d2,d3=s(p5,p8)
    rand8 =  cylinder(pos=vector(p8[0],p8[1],p8[2]),         axis=vector(d1,d2,d3), radius=.1,color=vector(0,0,0))
    
    d1,d2,d3=s(p5,p1)
    rand9 =  cylinder(pos=vector(p1[0],p1[1],p1[2]),         axis=vector(d1,d2,d3), radius=.1,color=vector(0,0,0))
    
    d1,d2,d3=s(p6,p2)
    rand10 = cylinder(pos=vector(p2[0],p2[1],p2[2]),         axis=vector(d1,d2,d3), radius=.1,color=vector(0,0,0))
    
    d1,d2,d3=s(p7,p3)
    rand11 = cylinder(pos=vector(p3[0],p3[1],p3[2]),         axis=vector(d1,d2,d3), radius=.1,color=vector(0,0,0))
    
    d1,d2,d3=s(p8,p4)
    rand12 = cylinder(pos=vector(p4[0],p4[1],p4[2]),         axis=vector(d1,d2,d3), radius=.1,color=vector(0,0,0))
    
    p1,p2,p6,p5
    x1=(p1[0]+p2[0]+p3[0]+p4[0])/4
    y1=(p1[1]+p2[1]+p3[1]+p4[1])/4
    z1=(p1[2]+p2[2]+p3[2]+p4[2])/4
    x2=(p4[0]+p3[0]+p7[0]+p8[0])/4.
    y2=(p4[1]+p3[1]+p7[1]+p8[1])/4.
    z2=(p4[2]+p3[2]+p7[2]+p8[2])/4.
    pa=[x1,y1,z1]
    pb=[x2,y2,z2]
    return [balk,rand1,rand2,rand3,rand4,rand5,rand6,rand7,rand8,rand9,rand10,rand11,rand12,pa,pb]