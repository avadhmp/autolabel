#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:52:41 2022

@author: avadhpatel
detect big valve
start 52
"""

import numpy as np
import argparse
import cv2
#import xml.etree.ElementTree as ET
import os
import os.path
from pascal_voc_writer import Writer

for filename in os.listdir():
    #xml1 = filename.endswith('.xml')
    
    if filename.endswith('.jpeg'):
        
        pathname,extension = os.path.splitext(filename)
        print(filename)
        img = str(filename)
        print(img)
        image = cv2.imread(img)
        
        # dup = str(image)
        # print(dup)
        hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        blue_lower = np.array([111,120,74], np.uint8)
        blue_upper = np.array([120, 180, 180], np.uint8)
# blue_lower = np.array([110, 50, 50], np.uint8)
# blue_upper = np.array([130, 255, 180], np.uint8)
        blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
        kernal = np.ones((5, 5), "uint8")
        blue_mask = cv2.dilate(blue_mask, kernal)
        res_blue = cv2.bitwise_and(image, image,
                                mask = blue_mask)

        contours, hierarchy = cv2.findContours(blue_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
#cv2.imshow('mask',blue_mask)
#cv2.imshow('bitwise',res_blue)
#print(contours)
#def find_contour_areas(contours):

        areas = [cv2.contourArea(cnt)for cnt in contours]
        max_index = np.argmax(areas)
        cnt = contours[max_index]
        x,y,w,h = cv2.boundingRect(cnt)

#dimensions = image.shape
        height = image.shape[0]
        width = image.shape[1]
        depth = 3
#print('dimensions',dimensions)

#print(x,y,w,h)

        xmin = x - w/2
        xmax = x+ w/2
        ymin = y - h/2
        ymax = y+ h/2
        
        # abs_path = os.path.abspath(str(filename))
        # absp = str(abs_path)
# create pascal voc writer (image_path, width, height)
        writer = Writer(filename, width, height,depth)

# add objects (class, xmin, ymin, xmax, ymax)
        writer.addObject('bvalve_0', xmin, ymin, xmax, ymax)
#writer.addObject('person', 40, 90, 100, 150)
        xml1 = pathname + '.xml'
# write to file
        print(xml1)
        writer.save(xml1)
        
#folder
#filename
#path 
#width,height,depth
#name
#xmin,xmax,ymin,ymax
 

#print(xadj,yadj,wadj,hadj)

#pascal vac is better one to one

#class x_center y_center width height
#imageFrame = cv2.rectangle(image, (x, y),
                                        # (x + w, y + h),
                                        # (255, 0, 0), 2)

# cv2.putText(imageFrame, "Blue Colour", (x, y),
#                         cv2.FONT_HERSHEY_SIMPLEX,
#                         1.0, (255, 0, 0))
            
#cv2.imshow("images", imageFrame)
#cv2.waitKey(0)
