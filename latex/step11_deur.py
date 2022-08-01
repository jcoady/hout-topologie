#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 09:33:40 2022

@author: windhoos
"""

from latex import config as cfg
from latex import balk, arrow
from vpython import vector

def get_deur():
    deur=cfg.deur
    stut=cfg.stut
    #####
    #DIEPTE
    cfg.step11_breedte = deur['breedte'].sum()
    #HOOGTE
    cfg.step11_hoogte = deur.iloc[0,0]
    #DIKTE
    cfg.step11_dikte = deur.iloc[0,2] + stut.iloc[0,2]

    #zet alle verticale elementen in een afbeelding
    rows=len(deur.index)
    arrowlist=[]
    for row in range(rows):
        x0=deur.loc[row,'xloc']
        y0=deur.loc[row,'yloc']
        z0=deur.loc[row,'zloc']
        l=deur.loc[row,'lengte']
        w=deur.loc[row,'breedte']
        h=deur.loc[row,'dikte']
        xa=deur.loc[row,'rx']
        ya=deur.loc[row,'ry']
        za=deur.loc[row,'rz']
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step11_deur.append(B)
        pa=B[-2]
        pb=B[-1]
        arrowlist.append([pa,pb,l,w,h])
    
    #zet alle horizontale elementen in een afbeelding
    rows=len(stut.index)
    arrowlist2=[]    
    for row in range(rows):
        x0=stut.loc[row,'xloc']
        y0=stut.loc[row,'yloc']
        z0=stut.loc[row,'zloc']
        l=stut.loc[row,'lengte']
        w=stut.loc[row,'breedte']
        h=stut.loc[row,'dikte']
        xa=stut.loc[row,'rx']
        ya=stut.loc[row,'ry']
        za=stut.loc[row,'rz']
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step11_stut.append(B)
        pa=B[-2]
        pb=B[-1]
        arrowlist2.append([pa,pb,l,w,h])
        
    xminlist=[]
    xmaxlist=[]
    for i in range(len(arrowlist)):
        xminlist.append(arrowlist[i][0][0]-arrowlist[i][0][1])
        xmaxlist.append(arrowlist[i][0][0]+arrowlist[i][0][1])
        
    xmin=min(xminlist)
    xmax=max(xmaxlist)
    
    cfg.step11_Ox = (xmin + xmax)/2
    cfg.step11_Oy = (deur.iloc[0,4]+stut.iloc[0,4])/2
    cfg.step11_Oz = deur.iloc[0,5]
        
    return arrowlist,arrowlist2

def build_arrow(arrowlist, arrowlist2):
    
    #bepaal grootste x lijst in deur
    xmaxlist=[]
    for i in range(len(arrowlist)):
        if xmaxlist == []:
            xmaxlist=arrowlist[i]
        elif xmaxlist[0][0] < arrowlist[i][0][0]:
            xmaxlist=arrowlist[i]
            
    #bepaal grootste x lijst in stut
    yminlist=[]
    for i in range(len(arrowlist2)):
        if yminlist == []:
            yminlist=arrowlist2[i]
        elif yminlist[0][1] > arrowlist2[i][1][1]:
            yminlist=arrowlist2[i]
        
    x0=yminlist[1][0]
    y0=yminlist[1][1] 
    z0=yminlist[1][2] - yminlist[3]/2

    x1=yminlist[1][0]
    y1=yminlist[1][1] 
    z1=yminlist[1][2] + yminlist[3]/2 + (xmaxlist[0][2] - yminlist[1][2])
        
    x2=xmaxlist[1][0] + xmaxlist[3]/2
    y2=yminlist[1][1]
    z2=yminlist[1][2]  + yminlist[3]/2 + (xmaxlist[0][2] - yminlist[1][2])
        
    thickness = xmaxlist[4]
            
    A=get_arrow(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,1)
    cfg.step11_arrow.append(A)
    
    #bepaal kleinste x lijst in deur
    xmaxlist=[]
    for i in range(len(arrowlist)):
        if xmaxlist == []:
            xmaxlist=arrowlist[i]
        elif xmaxlist[0][0] > arrowlist[i][0][0]:
            xmaxlist=arrowlist[i]
            
    #bepaal kleinste x lijst in stut
    yminlist=[]
    for i in range(len(arrowlist2)):
        if yminlist == []:
            yminlist=arrowlist2[i]
        elif yminlist[0][1] < arrowlist2[i][1][1]:
            yminlist=arrowlist2[i]
            
    arrowlist2.reverse()
    
    #arrowlist = verticaal
    #arrowlist2 = horizontaal
    for a in range(len(arrowlist2)):
        x0=arrowlist2[0][1][0] - cfg.step11_breedte
        y0=arrowlist[0][1][1]
        z0=arrowlist[0][1][2]
    
        x1=arrowlist2[0][1][0] - cfg.step11_breedte*1.05 - arrowlist2[1][3]*a*1.5
        y1=arrowlist[0][1][1]
        z1=arrowlist[0][1][2]
            
        x2=arrowlist2[0][1][0] - cfg.step11_breedte*1.05 - arrowlist2[1][3]*a*1.5
        y2=arrowlist[0][1][1]
        z2=arrowlist2[a][0][2] - arrowlist2[a][3]/2
            
        thickness = arrowlist[0][4]
                    
        A=get_arrow(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,2)
        cfg.step11_arrow.append(A)
            
        if a == 0:
            cfg.step11_zoom = [x0,y0,z0]
           
def get_arrow(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case):
    if case == 1:
        case = 111
        A=arrow.build(x0,y0,z0,x1,y1,z1,x2,y2,z2,thickness,case)
    elif case ==2:
        case = 112
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
        
    cfg.step11_pointer=pointerlist

def build():
    arrowlist,arrowlist2=get_deur()
    build_arrow(arrowlist,arrowlist2)
    #build_pointer(arrowlist2)
