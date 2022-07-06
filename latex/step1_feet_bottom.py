#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:49:59 2022

@author: windhoos
"""

from latex import config as cfg
from latex import balk,arrow
import pandas as pd

def get_feet():
    voeten=cfg.voeten
    rows=len(voeten.index)
    arrowlist=[]
    arrowlist2=[[],[],[]]
    for row in range(rows):
        x0=voeten.loc[row,'xloc']
        y0=voeten.loc[row,'yloc']
        z0=voeten.loc[row,'zloc']
        l=voeten.loc[row,'lengte']
        w=voeten.loc[row,'breedte']
        h=voeten.loc[row,'dikte']
        xa=voeten.loc[row,'rx']
        ya=voeten.loc[row,'ry']
        za=voeten.loc[row,'rz']
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step1.append(B)
        
        if y0 > 0:
            arrowlist.append([x0,y0,z0,l,w,h,xa,ya,za])
            
    for feet in range(len(arrowlist)):
        if feet != 0:
            xa0=arrowlist[0][0]+arrowlist[0][3]/2.
            xa1=arrowlist[feet][0]+arrowlist[feet][3]/2.
            arrowlist2[0].append([xa0,xa1])
    
    ya0=0
    for feet in range(len(arrowlist)):
        if feet != 0:
            ya0=max(ya0,arrowlist[feet][1])
            ya0=ya0#+8.
            ya1=ya0
            arrowlist2[1].append([ya0,ya1])
            
    for feet in range(len(arrowlist)):
        if feet != 0:
            za0=arrowlist[0][2]
            za1=arrowlist[feet][2]
            arrowlist2[2].append([za0,za1])
        
    return arrowlist2

def get_bottom():
    onderkant=cfg.onderkant
    rows=len(onderkant.index)
    for row in range(rows):
        x0=onderkant.loc[row,'xloc']
        y0=onderkant.loc[row,'yloc']
        z0=onderkant.loc[row,'zloc']
        l=onderkant.loc[row,'lengte']
        w=onderkant.loc[row,'breedte']
        h=onderkant.loc[row,'dikte']
        xa=onderkant.loc[row,'rx']
        ya=onderkant.loc[row,'ry']
        za=onderkant.loc[row,'rz']
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step1.append(B)
        
def build_arrow(arrowlist):
    print(arrowlist)
    for a in range(len(arrowlist[0])):
        x0=arrowlist[0][a][0]
        x1=arrowlist[0][a][1]
        y0=arrowlist[1][a][0]
        y1=arrowlist[1][a][1]
        z0=arrowlist[2][a][0]
        z1=arrowlist[2][a][1]
        A=get_arrow(x0,y0,z0,x1,y1,z1,0,0)
        cfg.step1arrow.append(A)
        
def get_arrow(x0,y0,z0,x1,y1,z1,label,angle):
    #A=arrow.build(235.6/2.,40,5,-235.6/2.,40,5,0,0)
    A=arrow.build(x0,y0,z0,x1,y1,z1,label,angle)
    return A

def build():
    arrowlist=get_feet()
    bottom=get_bottom()
    arrow=build_arrow(arrowlist)