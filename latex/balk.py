#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 22:12:02 2022

@author: windhoos
"""

from vpython import box,vector,cyliner

def box(x0,y0,z0,l,w,h,a,xa,ya,za):
    kleur =  vector(0.4,0.3,0.2)
    balk =   box(pos=vector(x0,y0,z0), size=vector(l,h,w) , color=kleur)
    rand1 =  cylinder(pos=vector(x0,y0,z0),      axis=vector(5,0,0), radius=1)
    rand2 =  cylinder(pos=vector(0,2,1),         axis=vector(5,0,0), radius=1)
    rand3 =  cylinder(pos=vector(0,2,1),         axis=vector(5,0,0), radius=1)
    rand4 =  cylinder(pos=vector(0,2,1),         axis=vector(5,0,0), radius=1)
    rand5 =  cylinder(pos=vector(0,2,1),         axis=vector(5,0,0), radius=1)
    rand6 =  cylinder(pos=vector(0,2,1),         axis=vector(5,0,0), radius=1)
    rand7 =  cylinder(pos=vector(0,2,1),         axis=vector(5,0,0), radius=1)
    rand8 =  cylinder(pos=vector(0,2,1),         axis=vector(5,0,0), radius=1)
    rand9 =  cylinder(pos=vector(0,2,1),         axis=vector(5,0,0), radius=1)
    rand10 = cylinder(pos=vector(0,2,1),         axis=vector(5,0,0), radius=1)
    rand11 = cylinder(pos=vector(0,2,1),         axis=vector(5,0,0), radius=1)
    rand12 = cylinder(pos=vector(0,2,1),         axis=vector(5,0,0), radius=1)
    
    
    balk.rotate(angle=a,axis=vector(xa,ya,za),origin=vector(x0,y0,z0))
    return balk