# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:43:03 2017

@author: andre
"""
file = open('write.txt','w+')
numList = ['13\n','14\n','15\n']
for x in numList:
    file.write(x)


for x in numList:
    x = x.strip()#the item to be striped('\n') is optional.
    file.write(x)

file.writelines(numList)
file.close()    
