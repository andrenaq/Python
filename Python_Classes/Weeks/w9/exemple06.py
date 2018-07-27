# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:58:37 2017

@author: andre
"""

f4 = open('file4.txt','w')
wr4=f4.write('Hellp Ru')
strg=f4.read(15)
pos = f4.tell()
print('The current pos is :',pos)
f4.write("the string is: ",strg)
pos = f4.tell()
print(' the current file position is: ',pos)
rd4 = f4.read()
print (rd4)
f4.close()
