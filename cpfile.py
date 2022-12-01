#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:58:07 2022

@author: avadhpatel
"""

import xml.etree.ElementTree as ET
import pathlib
import shutil
import os
for filename in os.listdir():
    temp = 'template.xml'
    if filename.endswith('.jpeg'):
        #print(filename)
        pathname,extension = os.path.splitext(filename)
        #name = filename.stem
        copy = pathname + '.xml'
        with open(temp) as f:
            with open(copy,'w') as f1:
                for line in f:
                    f1.write(line)
        f1.close()
        f.close()
        print(copy)
        shutil.copyfile(temp,copy)
    print(filename)