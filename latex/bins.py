#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 23:37:17 2022

@author: windhoos
"""

import binpacking

b = { 'a': 10, 'b': 10, 'c':11, 'd':1, 'e': 2,'f':7 }

b = list(b.values())
bins = binpacking.to_constant_volume(b,11)
print("===== list\n",b,"\n",bins)