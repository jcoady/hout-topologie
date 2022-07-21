#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:28:45 2022

@author: windhoos
"""

import pandas as pd

d = {'lengte' : [690.6, 690.6, 690.6, 690.6, 39.6, 39.6, 39.6, 39.6, 39.6, 39.6, 89.6, 89.6], 
     'breedte': [3,3,3,3,3,3,3,3,3,3,3,3],
     'dikte'  : [3,3,3,3,3,3,3,3,3,3,3,3],
     'xloc'   : [46.3, 46.3, -46.3, -46.3, 46.3, 46.3, -46.3, -46.3, 46.3, -46.3, 0,0],
     'yloc'   : [21.3,-21.3,21.3,-21.3,0,0,0,0,0,0,-21.3,-21.3],
     'zloc'   : [352.5, 352.5, 352.5, 352.5, 392.9, 264.0, 392.9, 264.0, 696.3, 696.3, 395.1, 266.2],
     'rx'     : [0,0,0,0,0,0,0,0,0,0,0,0],
     'ry'     : [90,90,90,90,0,0,0,0,0,0,0,0],
     'rz'     : [0,0,0,0,90,90,90,90,90,90,0,0]
     }
df = pd.DataFrame(data=d)

print(df)

#Select Rows where Column is Equal to Specific Value
dg=df.loc[df['lengte'] == 690.6]
print(dg)

#Select Rows where Column is Equal to Maximum Value
dh = df.loc[df['lengte'].idxmax()]
print(dh)
#print value from column of maximum value
print(dh[0])
print(dh[5])
#print row from column with maximum value
di = df.loc[df['zloc'] == dh[5]]
print(di)

#print dataframe with ry columns equal to 0
dj = df.loc[df['ry'] == 0]
print(dj)
#renumber rows
dj = dj.reset_index(drop=True)
print(dj)
#select minimum zloc from that dataframe
dk = dj.loc[dj['zloc'].idxmin()]
print(dk)
print(dk[5])
#print those rows
dl = dj.loc[dj['zloc'] == dk[5]]
print(dl)
#select row with largest xloc
dm = dl.loc[dl['xloc'].idxmax()]
dm = dm[3]
print(dm)
dn = dl.loc[dl['xloc'] == dm]
print(dn)
#filter on columns
do = dn.filter(['lengte','breedte','dikte'])
print(do)
#selecteer eerste cell
dp = do.iloc[0,0]
print(dp)
