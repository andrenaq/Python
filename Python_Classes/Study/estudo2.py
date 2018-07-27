# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:08:55 2017

@author: andre
"""

teste = {1:2,2:3,3:4,4:5,5:6}

print((teste.items()))

c={'do':1,'tr':8,'ha':9}
for a,b in c.items() :
    print(a,b)
    
    
dict = {'a2':'3', 'k1':'89', 'z4':'5', 'd3':'0'} 
sortedDict = sorted(dict.items()) 
for k,v in sortedDict: 
    print (k, v)