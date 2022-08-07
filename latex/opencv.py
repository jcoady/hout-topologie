#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 21:26:56 2022

@author: windhoos
"""

import cv2
import numpy as np
import os
from PIL import Image as im

def cut():
    parent_dir = '/home/windhoos/hout-topologie/users'
    directory = '01-08-2022-17-50-28-test'
    path = os.path.join(parent_dir, directory)
    
    for images in os.listdir(path):
        # check if the image ends with png
        if (images.endswith(".png")):
            images2=os.path.join(path, images)
            #print(images2)
            img = cv2.imread(images2)
            
            info = np.iinfo(img.dtype) # Get the information of the incoming image type
            img = img.astype(np.float64) / info.max # normalize the data to 0 - 1
            img = 255 * img # Now scale by 255
            img = img.astype(np.uint8)
            ## (1) Convert to gray, and threshold
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            th, threshed = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)
            
            ## (2) Morph-op to remove noise
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
            morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)
            
            ## (3) Find contours
            contours, hierarchy = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            xmin=[]
            xmax=[]
            ymin=[]
            ymax=[]
            for c in contours:
                x,y,w,h = cv2.boundingRect(c)
                xmin.append(x)
                xmax.append(x+w)
                ymin.append(y)
                ymax.append(y+h)
                
            xmin=min(xmin)
            xmax=max(xmax)
            ymin=min(ymin)
            ymax=max(ymax)
            cv2.rectangle(img, (xmin-10, ymin-10), (xmax+10, ymax+10), (255,255,255), 2)
            #cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0,0,0), 2)
            dst = img[ymin:ymax, xmin:xmax]
            print(images)
            cv2.imwrite(os.path.join(path , images), dst)
            
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
    scaled_img = cv2.copyMakeBorder(scaled_img, pad_top, pad_bot, pad_left, pad_right, borderType=cv2.BORDER_CONSTANT, value=padColor)
    
    return scaled_img

def canvas():
    parent_dir = '/home/windhoos/hout-topologie/users'
    directory = '01-08-2022-17-50-28-test'
    path = os.path.join(parent_dir, directory)
    for images in os.listdir(path):
        # check if the image ends with png
        if (images.endswith(".png")):
            images2=os.path.join(path, images)
            img = cv2.imread(images2)
            scaled_img = resizeAndPad(img, (800,800), 255)
            data = im.fromarray(scaled_img)
            size = len(images)
            images2 = images[:size - 4]
            data.save(f"{path}/{images2}.png")