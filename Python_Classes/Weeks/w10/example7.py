# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:58:11 2017

@author: andre
"""
import re
color = re.sub(r'brown','blue','The color brown')
with open('colours.txt','w+') as fh:
    fh.write(color)