#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:39:28 2022

@author: windhoos
"""

from vpython import vector,cylinder,cone, compound, quad, vertex, text
import numpy as np
from math import sqrt,pi
from latex import config as cfg

def build(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case):
    a=direction(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case)
    return a

def direction(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case):
    if case == 1:#(z0 == z1 and z0==z2 and y1 == y2 and x0 == x1 and y0 < y1):
        vrichting = vector(1,0,0)
        a=arrow1(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    elif case==2:#(z0 == z1 and z0==z2 and y1 == y2 and x0 == x1 and y0 > y1):
        vrichting = vector(-1,0,0)
        a=arrow2(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting)
        return a
    elif (y0 == y1 and y0==y2 and z1 == z2 and x0 == x1 and z0 > z1):
        return 3
    elif (y0 == y1 and y0==y2 and z1 == z2 and x0 == x1 and z0 < z1):
        return 4
    elif (z0 == z1 and z0==z2 and x1 == x2 and y0 == y1 and x0 > x1):
        return 5
    elif (z0 == z1 and z0==z2 and x1 == x2 and y0 == y1 and x0 < x1):
        return 6
    elif (x0 == x1 and x0==x2 and z1 == z2 and y0 == y1 and z0 > z1):
        return 7
    elif (x0 == x1 and x0==x2 and z1 == z2 and y0 == y1 and z0 < z1):
        return 8
    elif (x0 == x1 and x0==x2 and y1 == y2 and z0 == z1 and y0 < y1):
        return 9
    elif (x0 == x1 and x0==x2 and y1 == y2 and z0 == z1 and y0 > y1):
        return 10
    elif (y0 == y1 and y0==y2 and x1 == x2 and z0 == z1 and x0 > x1):
        return 11
    elif (y0 == y1 and y0==y2 and x1 == x2 and z0 == z1 and x0 < x1):
        return 12
    
def arrow1(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):
    '''
            |z       // 0
            |       //
   2 =======|======// 1
            |_______x
            /
           /
          / y
    '''
    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    if x0 != x1:
        x_old=cfg.step1_camera[0]
        y_old=cfg.step1_camera[1]
        z_old=cfg.step1_camera[2]
        x_new=thickness*2+abs(x0-x1)/2
        y_new=y_old
        z_new=z_old
        cfg.step1_camera[0]=x_new
        cfg.step1_camera[1]=y_new
        cfg.step1_camera[2]=z_new
    elif y0 != y1:
        x_old=cfg.step1_camera[0]
        y_old=cfg.step1_camera[1]
        z_old=cfg.step1_camera[2]
        x_new=x_old
        y_new=thickness*2+abs(y0-y1)/2
        z_new=z_old
        cfg.step1_camera[0]=x_new
        cfg.step1_camera[1]=y_new
        cfg.step1_camera[2]=z_new
    elif z0 != z1:
        x_old=cfg.step1_camera[0]
        y_old=cfg.step1_camera[1]
        z_old=cfg.step1_camera[2]
        x_new=x_old
        y_new=y_old
        z_new=thickness*2+abs(z0-z1)/2
        cfg.step1_camera[0]=x_new
        cfg.step1_camera[1]=y_new
        cfg.step1_camera[2]=z_new
    
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=-1*head_length*uv[0]
    y1e=-1*head_length*uv[1]
    z1e=-1*head_length*uv[2]
    
    x2e=1*head_length*uv[0]
    y2e=1*head_length*uv[1]
    z2e=1*head_length*uv[2]
    
    red = 0.75
    
    head=cone(pos=vector(x1-x1e,y1-y1e,z1-z1e), axis=vector(x1e,y1e,z1e), radius=head_thickness, color=vector(red,0,0))
    tail=cone(pos=vector(x2-x2e,y2-y2e,z2-z2e), axis=vector(x2e,y2e,z2e), radius=head_thickness, color=vector(red,0,0))
    body=cylinder(pos=vector(x1-x1e,y1-y1e,z1-z1e), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,0,0), radius = body_thickness )

    t=text(text=f'{dtot} cm', pos= body.pos+0.5*body.axis+vector(0,thickness*(1+2/3),0) ,axis = vrichting, align='center', height=3*thickness, color=vector(red,0,0))
    t.rotate(angle=pi, axis=vector(0,1,0),origin=body.pos+0.5*body.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x2,y0,z0+thickness), color=vector(red,0,0))
    va2=vertex(pos=vector(x2,y0,z0-thickness), color=vector(red,0,0))
    va3=vertex(pos=vector(x2,y2+thickness*2,z2-thickness), color=vector(red,0,0))
    va4=vertex(pos=vector(x2,y2+thickness*2,z2+thickness), color=vector(red,0,0))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x1,y0,z0+thickness), color=vector(red,0,0))
    vb2=vertex(pos=vector(x1,y0,z0-thickness), color=vector(red,0,0))
    vb3=vertex(pos=vector(x1,y1+thickness*2,z1-thickness), color=vector(red,0,0))
    vb4=vertex(pos=vector(x1,y1+thickness*2,z1+thickness), color=vector(red,0,0))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])   
    
    arrow = compound([head, body, tail,slaba,slabb,t])
    return arrow
    
def arrow2(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,vrichting):
    '''
            |z       
            |       
   2 =======|========// 1
            |______x//
            /      // 0
           /
          / y
    '''
    d1=x2-x1
    d2=y2-y1
    d3=z2-z1
    if x0 != x1:
        x_old=cfg.step2_camera[0]
        y_old=cfg.step2_camera[1]
        z_old=cfg.step2_camera[2]
        x_new=thickness*2+abs(x0-x1)/2
        y_new=y_old
        z_new=z_old
        cfg.step2_camera[0]=x_new
        cfg.step2_camera[1]=y_new
        cfg.step2_camera[2]=z_new
    elif y0 != y1:
        x_old=cfg.step2_camera[0]
        y_old=cfg.step2_camera[1]
        z_old=cfg.step2_camera[2]
        x_new=x_old
        y_new=thickness*2+abs(y0-y1)/2
        z_new=z_old
        cfg.step2_camera[0]=x_new
        cfg.step2_camera[1]=y_new
        cfg.step2_camera[2]=z_new
    elif z0 != z1:
        x_old=cfg.step2_camera[0]
        y_old=cfg.step2_camera[1]
        z_old=cfg.step2_camera[2]
        x_new=x_old
        y_new=y_old
        z_new=thickness*2+abs(z0-z1)/2
        cfg.step2_camera[0]=x_new
        cfg.step2_camera[1]=y_new
        cfg.step2_camera[2]=z_new
    
    dtot=round(sqrt(d1**2+d2**2+d3**2),1)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length    = 3* thickness
    
    x1e=-1*head_length*uv[0]
    y1e=-1*head_length*uv[1]
    z1e=-1*head_length*uv[2]
    
    x2e=1*head_length*uv[0]
    y2e=1*head_length*uv[1]
    z2e=1*head_length*uv[2]
    
    red = 0.75
    
    head=cone(pos=vector(x1-x1e,y1-y1e,z1-z1e), axis=vector(x1e,y1e,z1e), radius=head_thickness, color=vector(red,0,0))
    tail=cone(pos=vector(x2-x2e,y2-y2e,z2-z2e), axis=vector(x2e,y2e,z2e), radius=head_thickness, color=vector(red,0,0))
    body=cylinder(pos=vector(x1-x1e,y1-y1e,z1-z1e), axis=vector(x2-x1-x2e+x1e,y2-y1-y2e+y1e,z2-z1-z2e+z1e), color=vector(red,0,0), radius = body_thickness )

    t=text(text=f'{dtot} cm', pos= body.pos+0.5*body.axis+vector(0,thickness*(1+2/3),0) ,axis=vrichting,align='center', height=3*thickness, color=vector(red,0,0))
    t.rotate(angle=pi, axis=vector(0,1,0),origin=body.pos+0.5*body.axis+vector(0,thickness*(1+2/3),0))
    
    va1=vertex(pos=vector(x2,y0,z0+thickness), color=vector(red,0,0))
    va2=vertex(pos=vector(x2,y0,z0-thickness), color=vector(red,0,0))
    va3=vertex(pos=vector(x2,y2+thickness*2,z2-thickness), color=vector(red,0,0))
    va4=vertex(pos=vector(x2,y2+thickness*2,z2+thickness), color=vector(red,0,0))
    slaba=quad(vs=[va1,va2,va3,va4])   
    
    vb1=vertex(pos=vector(x1,y0,z0+thickness), color=vector(red,0,0))
    vb2=vertex(pos=vector(x1,y0,z0-thickness), color=vector(red,0,0))
    vb3=vertex(pos=vector(x1,y1+thickness*2,z1-thickness), color=vector(red,0,0))
    vb4=vertex(pos=vector(x1,y1+thickness*2,z1+thickness), color=vector(red,0,0))
    slabb=quad(vs=[vb1,vb2,vb3,vb4])   
    
    arrow = compound([head, body, tail,slaba,slabb,t])
    return arrow