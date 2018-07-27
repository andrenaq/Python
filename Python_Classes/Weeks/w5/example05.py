# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:36:24 2017

@author: andre
"""
import re


var = input('enter something from keyboard: \n')
if len(var) ==1 and re.match('^[ac]',var):
    print("1 - Got a true expression value")
    print(var)
else:
    print("Thanks")
    