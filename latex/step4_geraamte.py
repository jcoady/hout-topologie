#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 09:33:40 2022

@author: windhoos
"""

from latex import config as cfg
from latex import balk, arrow

def get_feet():
    voeten=cfg.voeten
    rows=len(voeten.index)
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
        cfg.step4_feet.append(B)

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
        cfg.step4_bottom.append(B)
        
def get_rib():
    rib_onder=cfg.rib_onder
    rows=len(rib_onder.index)
    arrowlist=[]
    for row in range(rows):
        x0=rib_onder.loc[row,'xloc']
        y0=rib_onder.loc[row,'yloc']
        z0=rib_onder.loc[row,'zloc']
        l=rib_onder.loc[row,'lengte']
        w=rib_onder.loc[row,'breedte']
        h=rib_onder.loc[row,'dikte']
        xa=rib_onder.loc[row,'rx']
        ya=rib_onder.loc[row,'ry']
        za=rib_onder.loc[row,'rz']
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step4_rib_onder.append(B)
        pa=B[-2]
        pb=B[-1]
        arrowlist.append([pa,pb,l,w,h])
        
    arrowlist2=[]
    for i in range(len(arrowlist)):
        arrowlist2.append(arrowlist[-(i+1)])
            
    return arrowlist2
        
def get_rib_frame():
    ribmax=cfg.ribmax
    
    #####
    #DIEPTE
    #lengte,breedie,dikte,xloc,yloc,zloc,rx,ry,rz
    #selecteer 1 rib, die met de maximale xloc
    xmax = ribmax.loc[ribmax['xloc'].idxmax()]
    xmax = xmax[3]  #<--- waarde max xloc
    diepte=ribmax.loc[ribmax['xloc'] == xmax]
    #selecteer horizontale componenten
    diepte=diepte.loc[diepte['rz'] == 90]
    #selecteer bovenste ligger
    zmax=diepte.loc[diepte['zloc'].idxmax()]
    zmax=zmax[5] #<--- waarde max zloc
    diepte=diepte.loc[diepte['zloc'] == zmax]
    #tel de eerste en tweede cel bij elkaar op
    cfg.step4_diepte=diepte.iloc[0,0]+diepte.iloc[0,1]*2
    #print(breedte)
    
    #BREEDTE
    xmax = ribmax.loc[ribmax['xloc'].idxmax()]
    xmax = xmax[3]
    cfg.step4_breedte=xmax*2+cfg.balk_dikte
    
    #HOOGTE
    xmax = ribmax.loc[ribmax['xloc'].idxmax()]
    xmax = xmax[3]
    hoogte = ribmax.loc[ribmax['xloc'] == xmax]
    hoogte = hoogte.loc[hoogte['ry'] == 90]
    hoogte = hoogte.iloc[0,0]
    cfg.step4_hoogte = hoogte + cfg.poot_hoogte + cfg.plank_dikte

    cfg.step4_Ox=0.
    cfg.step4_Oy=0.
    cfg.step4_Oz=cfg.step4_hoogte/2.
    
    vertmax = ribmax.loc[ribmax['lengte'].idxmax()]
    vertmax = vertmax [0]
    #vert = ribmax.loc[ribmax['lengte'] == vertmax]
    vert = ribmax.loc[ribmax['rz'] == 90]
    vert = vert.reset_index(drop=True)
    
    horizmax = ribmax.loc[ribmax['lengte'].idxmin()]
    horizmax = horizmax[0]
    #horiz = ribmax.loc[ribmax['lengte'] == horizmax]
    horiz = ribmax.loc[ribmax['ry'] == 90]
    horiz = horiz.reset_index(drop=True)

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
        cfg.step4_ribben_vert.append(B)
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
        cfg.step4_ribben_horiz.append(B)
        pa=B[-2]
        pb=B[-1]
        arrowlist2.append([pa,pb,l,w,h])
        
    #arrowlist3=[]    
    #for i in range(len(arrowlist2)):
    #    arrowlist3.append(arrowlist2[-(i+1)])
            
    #return arrowlist3

def build_pointer(arrowlist):
    pointerlist=[]
    for member in range(len(arrowlist)):
        links=arrowlist[member][0]
        rechts=arrowlist[member][1]
        dikte=arrowlist[member][4]
        
        x0l=links[0]
        y0l=links[1] +dikte*1.5 + dikte*5
        z0l=links[2] +dikte*2 + dikte*5
        
        x1l=links[0]
        y1l=links[1] +dikte*1.5
        z1l=links[2] +dikte*2
        
        x1r=rechts[0]
        y1r=rechts[1] -dikte*1.5
        z1r=rechts[2] +dikte*2
        
        x0r=rechts[0]
        y0r=rechts[1] -dikte*1.5 - dikte*5
        z0r=rechts[2] +dikte*2 + dikte*5
        
        pointer_links=arrow.pointer(x0l,y0l,z0l,x1l,y1l,z1l)
        pointer_rechts=arrow.pointer(x0r,y0r,z0r,x1r,y1r,z1r)
        pointerlist.append([pointer_links,pointer_rechts])
        
    cfg.step4_pointer=pointerlist

def build():
    get_feet()
    get_bottom()
    arrowlist=get_rib()
    get_rib_frame()
    build_pointer(arrowlist)