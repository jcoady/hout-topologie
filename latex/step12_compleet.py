#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 09:33:40 2022

@author: windhoos
"""

from latex import config as cfg
from latex import balk, arrow
from vpython import vector
from latex import table_builder

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
        
        cfg.schroef=cfg.schroef+2
        cfg.aantal_voeten=cfg.aantal_voeten+1
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step12_feet.append(B)

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
        cfg.step12_bottom.append(B)
        
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
        cfg.step12_rib_onder.append(B)
        
        cfg.schroef=cfg.schroef+len(cfg.onderkant)
        
        cfg.hoek=cfg.hoek+2
        cfg.schroef_kort=cfg.schroef_kort+8
        #pa=B[-2]
        #pb=B[-1]
        #arrowlist.append([pa,pb,l,w,h])
        
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
    cfg.step12_diepte=diepte.iloc[0,0]+diepte.iloc[0,1]*2+cfg.plank_dikte*2
    #print(breedte)
    
    #BREEDTE
    xmax = ribmax.loc[ribmax['xloc'].idxmax()]
    xmax = xmax[3]
    cfg.step12_breedte=xmax*2+cfg.balk_dikte
    
    #HOOGTE
    xmax = ribmax.loc[ribmax['xloc'].idxmax()]
    xmax = xmax[3]
    hoogte = ribmax.loc[ribmax['xloc'] == xmax]
    hoogte = hoogte.loc[hoogte['ry'] == 90]
    hoogte = hoogte.iloc[0,0]
    cfg.step12_hoogte = hoogte + cfg.poot_hoogte + cfg.plank_dikte*2

    cfg.step12_Ox=0.
    cfg.step12_Oy=0.
    cfg.step12_Oz=cfg.step12_hoogte/2.
    
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
        cfg.step12_ribben_vert.append(B)
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
        
        cfg.hoek=cfg.hoek+2
        cfg.schroef_kort=cfg.schroef_kort+8
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step12_ribben_horiz.append(B)

    #    if x0 == xmax:
    #        pa=B[-2]
    #        pb=B[-1]
    #        arrowlist2.append([pa,pb,l,w,h])
        
    #arrowlist3=[]    
    #for i in range(len(arrowlist2)):
    #    arrowlist3.append(arrowlist2[-(i+1)])
        
    #return arrowlist3
    
def get_achterrib():
    achterrib=cfg.achterrib
    rows=len(achterrib.index)
    #arrowlist=[]
    #arrowlist_small=[]
    
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
        
        cfg.hoek=cfg.hoek+2
        cfg.schroef_kort=cfg.schroef_kort+8
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step12_achterrib.append(B)
    #    pa=B[-2]
    #    pb=B[-1]
    #    arrowlist.append([pa,pb,l,w,h])
    #    if x0==xmax:
    #        arrowlist_small.append([pa,pb,l,w,h])
            
    #cfg.step6_zoom=arrowlist
        
    #arrowlist2=[]
    #for i in range(len(arrowlist)):
    #    arrowlist2.append(arrowlist[-(i+1)])
    
    #arrowlist_small2=[]
    #for i in range(len(arrowlist_small)):
    #    arrowlist_small2.append(arrowlist_small[-(i+1)])
            
    #return arrowlist2,arrowlist_small

def get_vlonders():
    vlonders=cfg.vlonders
    rows=len(vlonders.index)
    z_verdieping=[]
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
        
        if z_verdieping.count(z0) == 0:
            z_verdieping.append(z0)
            cfg.aantal_verdiepingen=cfg.aantal_verdiepingen+1
        
        cfg.schroef=cfg.schroef+cfg.aantal_voeten/2
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step12_vlonders.append(B)
        
def get_boven():
    bovenkant=cfg.bovenkant
    rows=len(bovenkant.index)
    for row in range(rows):
        x0=bovenkant.loc[row,'xloc']
        y0=bovenkant.loc[row,'yloc']
        z0=bovenkant.loc[row,'zloc']
        l=bovenkant.loc[row,'lengte']
        w=bovenkant.loc[row,'breedte']
        h=bovenkant.loc[row,'dikte']
        xa=bovenkant.loc[row,'rx']
        ya=bovenkant.loc[row,'ry']
        za=bovenkant.loc[row,'rz']
        
        cfg.schroef=cfg.schroef+cfg.aantal_voeten/2
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step12_bovenkant.append(B)
        
def get_links():
    zeidelinks=cfg.zeidelinks
    rows=len(zeidelinks.index)
    for row in range(rows):
        x0=zeidelinks.loc[row,'xloc']
        y0=zeidelinks.loc[row,'yloc']
        z0=zeidelinks.loc[row,'zloc']
        l=zeidelinks.loc[row,'lengte']
        w=zeidelinks.loc[row,'breedte']
        h=zeidelinks.loc[row,'dikte']
        xa=zeidelinks.loc[row,'rx']
        ya=zeidelinks.loc[row,'ry']
        za=zeidelinks.loc[row,'rz']
        
        cfg.schroef=cfg.schroef+cfg.aantal_verdiepingen
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step12_zeidelinks.append(B)
        
def get_rechts():
    zeiderechts=cfg.zeiderechts
    rows=len(zeiderechts.index)
    for row in range(rows):
        x0=zeiderechts.loc[row,'xloc']
        y0=zeiderechts.loc[row,'yloc']
        z0=zeiderechts.loc[row,'zloc']
        l=zeiderechts.loc[row,'lengte']
        w=zeiderechts.loc[row,'breedte']
        h=zeiderechts.loc[row,'dikte']
        xa=zeiderechts.loc[row,'rx']
        ya=zeiderechts.loc[row,'ry']
        za=zeiderechts.loc[row,'rz']
        
        cfg.schroef=cfg.schroef+cfg.aantal_verdiepingen
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step12_zeiderechts.append(B)
        
def get_achter():
    achterkant=cfg.achterkant
    rows=len(achterkant.index)
    for row in range(rows):
        x0=achterkant.loc[row,'xloc']
        y0=achterkant.loc[row,'yloc']
        z0=achterkant.loc[row,'zloc']
        l=achterkant.loc[row,'lengte']
        w=achterkant.loc[row,'breedte']
        h=achterkant.loc[row,'dikte']
        xa=achterkant.loc[row,'rx']
        ya=achterkant.loc[row,'ry']
        za=achterkant.loc[row,'rz']
        
        cfg.schroef=cfg.schroef+cfg.aantal_verdiepingen
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step12_achterkant.append(B)
        
def get_deurpost():
    voorkant=cfg.voorkant
    rows=len(voorkant.index)
    for row in range(rows):
        x0=voorkant.loc[row,'xloc']
        y0=voorkant.loc[row,'yloc']
        z0=voorkant.loc[row,'zloc']
        l=voorkant.loc[row,'lengte']
        w=voorkant.loc[row,'breedte']
        h=voorkant.loc[row,'dikte']
        xa=voorkant.loc[row,'rx']
        ya=voorkant.loc[row,'ry']
        za=voorkant.loc[row,'rz']
        
        cfg.schroef=cfg.schroef+cfg.aantal_verdiepingen
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step12_deurpost.append(B)
        
def get_deur():
    unit=cfg.deur_volledig
    rows=len(unit.index)
    for row in range(rows):
        x0=unit.loc[row,'xloc']
        y0=unit.loc[row,'yloc']
        z0=unit.loc[row,'zloc']
        l=unit.loc[row,'lengte']
        w=unit.loc[row,'breedte']
        h=unit.loc[row,'dikte']
        xa=unit.loc[row,'rx']
        ya=unit.loc[row,'ry']
        za=unit.loc[row,'rz']
        
        cfg.aantal_deur_planken=cfg.aantal_deur_planken+1
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step12_deur.append(B)
        
def get_stut():
    unit=cfg.stut_volledig
    rows=len(unit.index)
    aantal_deuren=len(cfg.deur_volledig)/len(cfg.deur)
    for row in range(rows):
        x0=unit.loc[row,'xloc']
        y0=unit.loc[row,'yloc']
        z0=unit.loc[row,'zloc']
        l=unit.loc[row,'lengte']
        w=unit.loc[row,'breedte']
        h=unit.loc[row,'dikte']
        xa=unit.loc[row,'rx']
        ya=unit.loc[row,'ry']
        za=unit.loc[row,'rz']
        
        cfg.aantal_stut_planken=cfg.aantal_stut_planken+1
        
        cfg.schroef_deur=cfg.schroef_deur+cfg.aantal_deur_planken/aantal_deuren
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za)
        cfg.step12_stut.append(B)
        
def get_scharnier():
    unit=cfg.scharnier
    rows=len(unit.index)
    for row in range(rows):
        x0=unit.loc[row,'xloc']
        y0=unit.loc[row,'yloc']
        z0=unit.loc[row,'zloc']
        l=unit.loc[row,'lengte']
        w=unit.loc[row,'breedte']
        h=unit.loc[row,'dikte']
        xa=unit.loc[row,'rx']
        ya=unit.loc[row,'ry']
        za=unit.loc[row,'rz']
        
        cfg.schroef_deur=cfg.schroef_deur+15/2
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za,kleur=vector(.5,.5,.5))
        cfg.step12_scharnier.append(B)
        
        cfg.scharnier_aantal = cfg.scharnier_aantal + 1
        
    cfg.scharnier_aantal=cfg.scharnier_aantal/2
        
def get_slot():
    unit=cfg.slot
    rows=len(unit.index)
    for row in range(rows):
        x0=unit.loc[row,'xloc']
        y0=unit.loc[row,'yloc']
        z0=unit.loc[row,'zloc']
        l=unit.loc[row,'lengte']
        w=unit.loc[row,'breedte']
        h=unit.loc[row,'dikte']
        xa=unit.loc[row,'rx']
        ya=unit.loc[row,'ry']
        za=unit.loc[row,'rz']
        
        B=balk.construct(x0,y0,z0,l,w,h,xa,ya,za,kleur=vector(.5,.5,.5))
        cfg.step12_slot.append(B)
        
        cfg.slot_aantal = cfg.slot_aantal + 1

def build(path,lang):
    get_feet()
    get_bottom()
    get_rib()
    get_rib_frame()
    get_achterrib()
    get_vlonders()
    get_boven()
    get_links()
    get_rechts()
    get_achter()
    get_deurpost()
    get_deur()
    get_stut()
    get_scharnier()
    get_slot()
    table_builder.latex([cfg.scharnier],path,lang,12)