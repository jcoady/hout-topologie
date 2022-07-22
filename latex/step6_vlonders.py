#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 09:33:40 2022

@author: windhoos
"""

from latex import config as cfg
from latex import balk, arrow
from vpython import vector

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
        cfg.step6_feet.append(B)

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
        cfg.step6_bottom.append(B)
        
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
        cfg.step6_rib_onder.append(B)
        pa=B[-2]
        pb=B[-1]
        arrowlist.append([pa,pb,l,w,h])
        
    #arrowlist2=[]
    #for i in range(len(arrowlist)):
    #    arrowlist2.append(arrowlist[-(i+1)])
            
    #return arrowlist2
        
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
    cfg.step6_diepte=diepte.iloc[0,0]+diepte.iloc[0,1]*2
    #print(breedte)
    
    #BREEDTE
    xmax = ribmax.loc[ribmax['xloc'].idxmax()]
    xmax = xmax[3]
    cfg.step6_breedte=xmax*2+cfg.balk_dikte
    
    #HOOGTE
    xmax = ribmax.loc[ribmax['xloc'].idxmax()]
    xmax = xmax[3]
    hoogte = ribmax.loc[ribmax['xloc'] == xmax]
    hoogte = hoogte.loc[hoogte['ry'] == 90]
    hoogte = hoogte.iloc[0,0]
    cfg.step6_hoogte = hoogte + cfg.poot_hoogte + cfg.plank_dikte

    cfg.step6_Ox=0.
    cfg.step6_Oy=0.
    cfg.step6_Oz=cfg.step6_hoogte/2.
    
    vertmax = ribmax.loc[ribmax['lengte'].idxmax()]
    vertmax = vertmax [0]
    #vert = ribmax.loc[ribmax['lengte'] == vertmax]
    vert = ribmax.loc[ribmax['ry'] == 90]
    vert = vert.reset_index(drop=True)
    
    horizmax = ribmax.loc[ribmax['lengte'].idxmin()]
    horizmax = horizmax[0]
    #horiz = ribmax.loc[ribmax['lengte'] == horizmax]
    horiz = ribmax.loc[ribmax['rz'] == 90]
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
        cfg.step6_ribben_vert.append(B)
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
        cfg.step6_ribben_horiz.append(B)

        if x0 == xmax:
            pa=B[-2]
            pb=B[-1]
            arrowlist2.append([pa,pb,l,w,h])
        
    arrowlist3=[]    
    for i in range(len(arrowlist2)):
        arrowlist3.append(arrowlist2[-(i+1)])
        
    return arrowlist3
    
def get_achterrib():
    achterrib=cfg.achterrib
    rows=len(achterrib.index)
    arrowlist=[]
    arrowlist_small=[]
    
    xmax = achterrib.loc[achterrib['xloc'].idxmax()]
    xmax = xmax[3]
    
    for row in range(rows):
        x0=achterrib.loc[row,'xloc']
        y0=achterrib.loc[row,'yloc']
        z0=achterrib.loc[row,'zloc']
        l=achterrib.loc[row,'lengte']
        w=achterrib.loc[row,'breedte']
        h=achterrib.loc[row,'dikte']
        xa=achterrib.loc[row,'rx']
        ya=achterrib.loc[row,'ry']
        za=achterrib.loc[row,'rz']
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step6_achterrib.append(B)
        pa=B[-2]
        pb=B[-1]
        arrowlist.append([pa,pb,l,w,h])
        if x0==xmax:
            arrowlist_small.append([pa,pb,l,w,h])
            
    cfg.step6_zoom=arrowlist
        
    arrowlist2=[]
    for i in range(len(arrowlist)):
        arrowlist2.append(arrowlist[-(i+1)])
    
    #arrowlist_small2=[]
    #for i in range(len(arrowlist_small)):
    #    arrowlist_small2.append(arrowlist_small[-(i+1)])
            
    return arrowlist2,arrowlist_small

def get_vlonders():
    vlonders=cfg.vlonders
    rows=len(vlonders.index)
    for row in range(rows):
        x0=vlonders.loc[row,'xloc']
        y0=vlonders.loc[row,'yloc']
        z0=vlonders.loc[row,'zloc']
        l=vlonders.loc[row,'lengte']
        w=vlonders.loc[row,'breedte']
        h=vlonders.loc[row,'dikte']
        xa=vlonders.loc[row,'rx']
        ya=vlonders.loc[row,'ry']
        za=vlonders.loc[row,'rz']
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step6_vlonders.append(B)
        
def build_arrow(arrowlist,arrowlist2):
    arrowlist.reverse()
    middleIndex = int((len(arrowlist) - 1)/2)
    for a in range(len(arrowlist2)):

        x0=arrowlist[a][0][0] + arrowlist[a][3]/2
        y0=arrowlist[a][0][1] - arrowlist[a][3]/2
        z0=arrowlist[a][0][2] + arrowlist[a][4]/2

        x1=arrowlist[a][0][0] + arrowlist[a][3]/2  + arrowlist[0][3]*(a)*8 + arrowlist[0][3]*4 #+ arrowlist[0][3] + arrowlist[0][3]*a*8
        y1=arrowlist[a][0][1] - arrowlist[a][3]/2
        z1=arrowlist[a][0][2] + arrowlist[a][4]/2
            
        x2=arrowlist2[a][1][0] + arrowlist2[a][3]  + arrowlist[0][3]*(a)*8 + arrowlist[0][3]*4#+ arrowlist[0][3] + arrowlist[0][3]*a*8
        y2=arrowlist2[a][1][1]
        z2=arrowlist2[a][1][2] + arrowlist2[a][4]/2
            
        thickness = arrowlist[0][4]
        
        if a == 0:        
            cfg.step6_cam22=vector(x0,y0,z0)
        
        if a == middleIndex:
            cfg.step6_cam21=vector(0,0,abs(arrowlist[a][0][2]-arrowlist[a][1][2])/2.)
                
        A=get_arrow(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness)
        cfg.step6_arrow.append(A)

def get_arrow(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness):
    case = 6
    A=arrow.build(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case)
    return A

def build_pointer(arrowlist):
    pointerlist=[]
    for member in range(len(arrowlist)):
        links=arrowlist[member][0]
        rechts=arrowlist[member][1]
        dikte=arrowlist[member][4]
        
        x1r=links[0] + dikte*1.5
        y1r=links[1] 
        z1r=links[2] - dikte*2
        
        x0r=links[0] + dikte*1.5 + dikte*5
        y0r=links[1] 
        z0r=links[2] - dikte*2 - dikte*5

        x1l=rechts[0] - dikte*1.5
        y1l=rechts[1] 
        z1l=rechts[2] - dikte*2
        
        x0l=rechts[0] - dikte*1.5 - dikte*5
        y0l=rechts[1] 
        z0l=rechts[2] - dikte*2 - dikte*5
        
        pointer_links=arrow.pointer(x0l,y0l,z0l,x1l,y1l,z1l)
        pointer_rechts=arrow.pointer(x0r,y0r,z0r,x1r,y1r,z1r)
        pointerlist.append([pointer_links,pointer_rechts])
        
    cfg.step6_pointer=pointerlist

def build():
    get_feet()
    get_bottom()
    get_rib()
    arrowlist=get_rib_frame()
    arrowlist2,arrowlist_small2=get_achterrib()
    get_vlonders()
    build_arrow(arrowlist,arrowlist_small2)
    build_pointer(arrowlist2)