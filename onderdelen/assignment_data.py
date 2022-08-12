#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:15:40 2022

@author: windhoos
"""

import os

def build(path,username,day,ct,closet_data,plank_data,state):
    lines = [str(path), str(username), str(day), str(ct), str(closet_data), str(plank_data), str(state)]
    path_file = os.path.join(path ,'assignment.txt')
    with open(path_file, 'w') as f:
        f.truncate()
        for line in lines:
            f.write(line)
            f.write('\n')
    f.close()
'''            
def main():
    parent_dir = '/home/windhoos/hout-topologie/users'
    directory = '09-08-2022-22-35-17-test'
    path = os.path.join(parent_dir, directory)
    build(path,'test',[1,2,3,4],[20,2.2,400],'complete')
main()
'''