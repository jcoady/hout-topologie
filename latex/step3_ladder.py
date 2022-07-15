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
    
    #vind de maximale lengte in de lijst
    zmax = ribmax.loc[ribmax['lengte'].idxmax()]
    zmax = zmax[5]#-(zmax[0]- zmax[5])
    
    cfg.step3_zmax=zmax
    
    #selecteer de rijen met de grootste x
    #selecteer de rijen met de grootste lengte
    vert = ribmax.loc[ribmax['xloc'] == xmax]
    vertmax = vert.loc[vert['lengte'].idxmax()]
    vertmax = vertmax[0]
    vert = vert.loc[vert['lengte'] == vertmax]
    vert = vert.reset_index(drop=True)
    
    #selecteer de rijen met de kleinste lengte
    #selecteer de rijen met de grootste x
    #horiz = ribmax.loc[ribmax['lengte'].idxmin()]
    #horizmin=horiz[0]
    #horiz = ribmax.loc[ribmax['lengte'] == horizmin]
    #oriz = horiz.loc[horiz['xloc'] == xmax]
    #horiz = horiz.reset_index(drop=True)
    
    #selecteer de rijen met de grootste x
    #selecteer de rijen met de grootste lengte
    horiz = ribmax.loc[ribmax['xloc'] == xmax]
    horizmax = horiz.loc[horiz['lengte'].idxmin()]
    horizmax = horizmax[0]
    horiz = horiz.loc[horiz['lengte'] == horizmax]
    horiz = horiz.reset_index(drop=True)

    #selecteer rijen met maximum waarde in column xloc
    ribmax = ribmax.loc[ribmax['xloc'] == xmax]
    ribmax = ribmax.reset_index(drop=True)

    #zet alle verticale elementen in een afbeelding
    rows=len(vert.index)
    arrowlist=[]
    for row in range(rows):
        x0=vert.loc[row,'xloc']
        y0=vert.loc[row,'yloc']
        z0=vert.loc[row,'zloc']
        l=vert.loc[row,'lengte']
        w=vert.loc[row,'breedte']
        h=vert.loc[row,'dikte']
        xa=vert.loc[row,'rx']
        ya=vert.loc[row,'ry']
        za=vert.loc[row,'rz']
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step3_ribben_vert.append(B)
        pa=B[-2]
        pb=B[-1]
        arrowlist.append([pa,pb,l,w,h])
    
    #zet alle horizontale elementen in een afbeelding
    rows=len(horiz.index)
    arrowlist2=[]    
    for row in range(rows):
        x0=horiz.loc[row,'xloc']
        y0=horiz.loc[row,'yloc']
        z0=horiz.loc[row,'zloc']
        l=horiz.loc[row,'lengte']
        w=horiz.loc[row,'breedte']
        h=horiz.loc[row,'dikte']
        xa=horiz.loc[row,'rx']
        ya=horiz.loc[row,'ry']
        za=horiz.loc[row,'rz']
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step3_ribben_horiz.append(B)
        pa=B[-2]
        pb=B[-1]
        arrowlist2.append([pa,pb,l,w,h])
        
    arrowlist3=[]    
    for i in range(len(arrowlist2)):
        arrowlist3.append(arrowlist2[-(i+1)])
            
    return arrowlist3
        
def build_arrow(arrowlist):
    for a in range(len(arrowlist)):
        if a != 0:
            x0=arrowlist[0][0][0] 
            y0=arrowlist[0][0][1] - arrowlist[0][3]
            z0=arrowlist[0][0][2] + arrowlist[0][4]/2

            x1=arrowlist[0][0][0] 
            y1=arrowlist[0][0][1] - arrowlist[0][3] - arrowlist[0][3]*a*8
            z1=arrowlist[0][0][2] + arrowlist[0][4]/2
            
            x2=arrowlist[-a][0][0] 
            y2=arrowlist[-a][0][1] - arrowlist[0][3] - arrowlist[0][3]*a*8
            z2=arrowlist[-a][0][2] + arrowlist[0][4]/2
            
            thickness = arrowlist[0][4]
            
            A=get_arrow(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness)
            cfg.step3_arrow.append(A)
        
def get_arrow(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness):
    case = 3
    A=arrow.build(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case)
    return A

def build():
    arrowlist=get_rib()
    build_arrow(arrowlist)