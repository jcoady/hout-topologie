#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 22:16:39 2022

@author: windhoos
"""

import cv2
import numpy as np
import os
from PIL import Image as im

def resizeAndPad(img, size, padColor=0):

    h, w = img.shape[:2]
    sh, sw = size
    
    # interpolation method
    if h > sh or w > sw: # shrinking image
        interp = cv2.INTER_AREA
    
    else: # stretching image
        interp = cv2.INTER_CUBIC
    
    # aspect ratio of image
    aspect = float(w)/h 
    saspect = float(sw)/sh
    
    if (saspect > aspect) or ((saspect == 1) and (aspect <= 1)):  # new horizontal image
        new_h = sh
        new_w = np.round(new_h * aspect).astype(int)
        pad_horz = float(sw - new_w) / 2
        pad_left, pad_right = np.floor(pad_horz).astype(int), np.ceil(pad_horz).astype(int)
        pad_top, pad_bot = 0, 0
    
    elif (saspect < aspect) or ((saspect == 1) and (aspect >= 1)):  # new vertical image
        new_w = sw
        new_h = np.round(float(new_w) / aspect).astype(int)
        pad_vert = float(sh - new_h) / 2
        pad_top, pad_bot = np.floor(pad_vert).astype(int), np.ceil(pad_vert).astype(int)
        pad_left, pad_right = 0, 0
    
    # set pad color
    if len(img.shape) == 3 and not isinstance(padColor, (list, tuple, np.ndarray)): # color image but only one color provided
        padColor = [padColor]*3
    
    # scale and pad
    scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)
    scaled_img = cv2.copyMakeBorder(scaled_img, pad_top, pad_bot, pad_left, pad_right, borderType=cv2.BORDER_CONSTANT, value=-padColor)
    
    return scaled_img

def canvas():
    parent_dir = '/home/windhoos/hout-topologie'
    directory = 'testfiles'
    path = os.path.join(parent_dir, directory)
    
    for images in os.listdir(path):
        # check if the image ends with png
        if (images.endswith(".png")):
            images2=os.path.join(path, images)
            img = cv2.imread(images2)
            scaled_img = resizeAndPad(img, (1200,1200), 255)
            data = im.fromarray(scaled_img)
            data.save('gfg_dummy_pic.png')
            #cv2.imwrite(os.path.join(path , data))
canvas()