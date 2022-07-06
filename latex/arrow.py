#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:39:28 2022

@author: windhoos
"""

from vpython import vector,cylinder,cone, compound, quad, vertex
import numpy as np
from math import sqrt

def build(x0,y0,z0,x1,y1,z1,x2,y2,z2,label,thickness):
    x0,y0,z0,x1,y1,z1,x2,y2,z2,label,thickness=direction(x0,y0,z0,x1,y1,z1,x2,y2,z2,label,thickness)
    a=arrow(x0,y0,z0,x1,y1,z1,x2,y2,z2,label,thickness)
    return a

def direction(x0,y0,z0,x1,y1,z1,x2,y2,z2,label,thickness):
    if (z0 == z1 and z0==z2 and y1 == y2 and x0 == x1 and y0 < y1):
        return 1
    elif (z0 == z1 and z0==z2 and y1 == y2 and x0 == x1 and y0 > y1):
        return 2
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
    
def arrow(x2,y2,z2,x0,y0,z0,x1,y1,z1,label,thickness):
    d1=x1-x0
    d2=y1-y0
    d3=z1-z0
    
    #dtot=sqrt(d1**2+d2**2+d3**2)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness =    thickness
    head_thickness = 2* thickness
    head_length =    3* thickness
    
    x0e=-1*head_length*uv[0]
    y0e=-1*head_length*uv[1]
    z0e=-1*head_length*uv[2]
    
    x1e=1*head_length*uv[0]
    y1e=1*head_length*uv[1]
    z1e=1*head_length*uv[2]
    
    head=cone(pos=vector(x0-x0e,y0-y0e,z0-z0e), axis=vector(x0e,y0e,z0e), radius=head_thickness, color=vector(1,0,0))
    tail=cone(pos=vector(x1-x1e,y1-y1e,z1-z1e), axis=vector(x1e,y1e,z1e), radius=head_thickness, color=vector(1,0,0))
    body=cylinder(pos=vector(x0-x0e,y0-y0e,z0-z0e), axis=vector(x1-x0-x1e+x0e,y1-y0-y1e+y0e,z1-z0-z1e+z0e), color=vector(1,0,0), radius = body_thickness )
    v1=vertex(pos=vector(x0,y0-head_thickness,z0-head_thickness), color=vector(1,0,0))
    v2=vertex(pos=vector(x0,y0-head_thickness,z0+head_thickness), color=vector(1,0,0))
    v3=vertex(pos=vector(x0,y0+head_thickness,z0+head_thickness), color=vector(1,0,0))
    v4=vertex(pos=vector(x0,y0+head_thickness,z0-head_thickness), color=vector(1,0,0))
    slab=quad(vs=[v1,v2,v3,v4])
    
    va=vertex(pos=vector(x0,y0-head_thickness,z0-head_thickness), color=vector(1,0,0))
    va=vertex(pos=vector(x0,y0-head_thickness,z0+head_thickness), color=vector(1,0,0))
    va=vertex(pos=vector(x0,y0+head_thickness,z0+head_thickness), color=vector(1,0,0))
    va=vertex(pos=vector(x0,y0+head_thickness,z0-head_thickness), color=vector(1,0,0))
    slab=quad(vs=[va,va,va,va])   
    
    arrow = compound([head, body, tail,slab])
    return arrow
    