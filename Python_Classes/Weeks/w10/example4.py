# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:22:17 2017

@author: andre
"""

f14 = open('file2.txt')
f014=open ('file14.txt','a+')
for _ in f14:
    print(_.rstrip())
    f014.write(_)
f14.close()
f014.close()