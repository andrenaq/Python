# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:38:28 2017

@author: andre
"""

f14 = open('file2.txt')
f014=open ('file14.txt','a+')
i=1
for _ in f14:
    print(_.rstrip())
    f014.write(str(i)+": "+_)
    i=i+1
f14.close()
f014.close()