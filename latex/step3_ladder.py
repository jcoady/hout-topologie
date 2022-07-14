#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 09:33:40 2022

@author: windhoos
"""

from latex import config as cfg
from latex import balk, arrow
        
def get_rib():
    ribmax=cfg.ribmax
    #vind maximale waarde in df
    xmax = ribmax.loc[ribmax['xloc'].idxmax()]
    xmax = xmax[3]
    cfg.step3_xmax=xmax
    zmax = ribmax.loc[ribmax['lengte'].idxmax()]
    zmax = zmax[5]
    cfg.step3_zmax=zmax
    #selecteer rijen met maximum waarde in column xloc
    ribmax = ribmax.loc[ribmax['xloc'] == xmax]
    ribmax = ribmax.reset_index(drop=True)
    print(ribmax)
    rows=len(ribmax.index)
    arrowlist=[]
    for row in range(rows):
        x0=ribmax.loc[row,'xloc']
        y0=ribmax.loc[row,'yloc']
        z0=ribmax.loc[row,'zloc']
        l=ribmax.loc[row,'lengte']
        w=ribmax.loc[row,'breedte']
        h=ribmax.loc[row,'dikte']
        xa=ribmax.loc[row,'rx']
        ya=ribmax.loc[row,'ry']
        za=ribmax.loc[row,'rz']
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step3_ribben.append(B)
        pa=B[-2]
        pb=B[-1]
        arrowlist.append([pa,pb,l,w,h])
        
    arrowlist2=[]
    for i in range(len(arrowlist)):
        arrowlist2.append(arrowlist[-(i+1)])
            
    return arrowlist2
        
def build_arrow(arrowlist):
    for a in range(len(arrowlist)):
        if a != 0:
            x0=arrowlist[0][1][0] - arrowlist[0][4]/2
            y0=arrowlist[0][1][1]
            z0=arrowlist[0][1][2]

            x1=arrowlist[0][1][0] - arrowlist[0][4]/2
            y1=arrowlist[0][1][1] + arrowlist[0][4]*a*6 + arrowlist[0][4]
            z1=arrowlist[0][1][2]
            
            x2=arrowlist[a][1][0] - arrowlist[0][4]/2
            y2=arrowlist[a][1][1] + arrowlist[0][4]*a*6 + arrowlist[0][4]
            z2=arrowlist[a][1][2]
            
            thickness = arrowlist[0][4]
            
            A=get_arrow(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness)
            cfg.step2_arrow.append(A)
            
def build_arrow2(arrowlist):
    #pa,pb,l,w,h]
    x0=arrowlist[0][0][0] - arrowlist[0][3]/2
    y0=arrowlist[0][0][1]
    z0=arrowlist[0][0][2]

    x1=arrowlist[0][0][0] - arrowlist[0][3]/2 - arrowlist[0][3]
    y1=arrowlist[0][0][1]
    z1=arrowlist[0][0][2]
    
    x2=arrowlist[0][0][0] - arrowlist[1][3]/2 - arrowlist[0][3]
    y2=arrowlist[0][0][1] - arrowlist[1][3]
    z2=arrowlist[0][0][2]
    
    thickness = arrowlist[0][4]
    
    A=get_arrow2(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness)
    cfg.step2_arrow.append(A)
        
def get_arrow(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness):
    case = 21
    A=arrow.build(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case)
    return A

def get_arrow2(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness):
    case = 22
    A=arrow.build(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case)
    return A

def build():
    arrowlist=get_rib()
    #build_arrow(arrowlist)
    #build_arrow2(arrowlist)