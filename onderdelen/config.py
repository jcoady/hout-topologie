#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 22:42:49 2022

@author: windhoos
"""

breedte_kast=0
hoogte_kast=0
diepte_kast=0

breedte_plank=0
lengte_plank=0
dikte_plank=0

niveaus=1
plankhoogte=[]

hoogte_voet=0

breedte_rib=5
lengte_rib=240
dikte_rib=breedte_rib

voorplank_breedte=0

df_voet=[]
df_onderstel=[]
df_zeiplank=[]
df_achterplank=[]
df_voorkant=[]
df_ribben=[]
df_vlonders=[]

procent=0

start=0
end=0

graphics=0
sliders=[]
sliders_update=[]
update_graph=False

reset=False
reset_loop=True

knoppen=[]
input_velden=[]
build_state=False

finish_drawing = False

wt_error=0
error_message = ' '
error_message0 = ' '
error_message1 = '                                                                        <b>ERROR</b>'