#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 09:33:40 2022

@author: windhoos
"""

from latex import config as cfg
from latex import balk, arrow
from latex import table_builder
        
def get_rib():
    ribmax=cfg.ribmax
    
    #####
    #DIEPTE - globaal
    #lengte,breedie,dikte,xloc,yloc,zloc,rx,ry,rz
    #selecteer 1 rib, die met de maximale xloc
    xmax = ribmax.loc[ribmax['xloc'].idxmax()]
    xmax = xmax[3]  #<--- waarde max xloc
    diepte=ribmax.loc[ribmax['xloc'] == xmax]
    #selecteer horizontale componenten
    diepte=diepte.loc[diepte['rz'] == 90]
    #selecteer bovenste ligger
    ymax=diepte.loc[diepte['lengte'].idxmax()]
    ymax=ymax[0] #<--- waarde max yloc
    cfg.step3_diepte=ymax+cfg.balk_dikte*2+2*cfg.plank_dikte
    
    #BREEDTE - globaal
    xmax = ribmax.loc[ribmax['xloc'].idxmax()]
    xmax = xmax[2]
    cfg.step3_breedte=xmax
    
    #HOOGTE - globaal
    xmax = ribmax.loc[ribmax['xloc'].idxmax()]
    xmax = xmax[3]
    hoogte = ribmax.loc[ribmax['xloc'] == xmax]
    hoogte = hoogte.loc[hoogte['ry'] == 90]
    hoogte = hoogte.iloc[0,0]
    cfg.step3_hoogte = hoogte
    
    cfg.step3_Ox=xmax
    cfg.step3_Oy=0.
    cfg.step3_Oz=cfg.step3_hoogte/2.
    
    #print(cfg.step3_hoogte,cfg.step3_breedte,cfg.step3_diepte)
    #print(cfg.step3_Ox,cfg.step3_Oy,cfg.step3_Oz)
    #####

    #selecteer de rijen met de grootste x
    #selecteer de rijen met de grootste lengte
    vert = ribmax.loc[ribmax['xloc'] == xmax]
    vertmax = vert.loc[vert['lengte'].idxmax()]
    vertmax = vertmax[0]
    #vert = vert.loc[vert['lengte'] == vertmax]
    vert = vert.loc[ribmax['ry'] == 90]
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
    horiz = horiz.loc[ribmax['rz'] == 90]
    #horiz = horiz.loc[horiz['lengte'] == horizmax]
    horiz = horiz.reset_index(drop=True)

    #selecteer rijen met maximum waarde in column xloc
    #ribmax = ribmax.loc[ribmax['xloc'] == xmax]
    #ribmax = ribmax.reset_index(drop=True)

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

def build_pointer(arrowlist):
    pointerlist=[]
    for member in range(len(arrowlist)):
        links=arrowlist[member][0]
        rechts=arrowlist[member][1]
        dikte=arrowlist[member][4]
        
        x0l=links[0]
        y0l=links[1] +dikte*1.5 + dikte*5
        z0l=links[2] -dikte*2 - dikte*5
        
        x1l=links[0]
        y1l=links[1] +dikte*1.5
        z1l=links[2] -dikte*2
        
        x1r=rechts[0]
        y1r=rechts[1] -dikte*1.5
        z1r=rechts[2] -dikte*2
        
        x0r=rechts[0]
        y0r=rechts[1] -dikte*1.5 - dikte*5
        z0r=rechts[2] -dikte*2 - dikte*5
        
        pointer_links=arrow.pointer(x0l,y0l,z0l,x1l,y1l,z1l)
        pointer_rechts=arrow.pointer(x0r,y0r,z0r,x1r,y1r,z1r)
        pointerlist.append([pointer_links,pointer_rechts])
        
    cfg.step3_pointer=pointerlist

def build(path, lang):
    arrowlist=get_rib()
    build_arrow(arrowlist)
    build_pointer(arrowlist)
    
    table_builder.latex([cfg.ribmax],path,lang,3)