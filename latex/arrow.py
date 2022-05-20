#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:39:28 2022

@author: windhoos
"""

from vpython import vector,cylinder,cone, compound
import numpy as np
from math import sqrt

def build(x0,y0,z0,x1,y1,z1,label,angle):
    d1=x1-x0
    d2=y1-y0
    d3=z1-z0
    
    dtot=sqrt(d1**2+d2**2+d3**2)
    
    vec=np.array([d1,d2,d3])

    uv = vec / np.linalg.norm(vec)
    
    body_thickness= 2 #dtot*.05
    head_thickness= 3 #dtot*.1
    head_length=5 #dtot*.2
    
    x0e=-1*head_length*uv[0]
    y0e=-1*head_length*uv[1]
    z0e=-1*head_length*uv[2]
    
    x1e=1*head_length*uv[0]
    y1e=1*head_length*uv[1]
    z1e=1*head_length*uv[2]
    
    head=cone(pos=vector(x0-x0e,y0-y0e,z0-z0e), axis=vector(x0e,y0e,z0e), radius=head_thickness, color=vector(1,0,0))
    tail=cone(pos=vector(x1-x1e,y1-y1e,z1-z1e), axis=vector(x1e,y1e,z1e), radius=head_thickness, color=vector(1,0,0))
    body=cylinder(pos=vector(x0-x0e,y0-y0e,z0-z0e), axis=vector(x1-x0-x1e+x0e,y1-y0-y1e+y0e,z1-z0-z1e+z0e), color=vector(1,0,0), radius = body_thickness )
    
    arrow = compound([head, body, tail])
    return arrow