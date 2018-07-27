# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:08:06 2017

@author: andre
"""

f6 = open('fileB.txt','r+')
strg = f6.read(3)
print('The string is: ',strg)
pos = f6.tell()
print('The current file position is: ',pos)
pos = f6.seek(6)
print('The current file position now is: ',pos)
strg6 = f6.read(15)
print(strg6)
pos = f6.tell()
print('The current file position now is really: ',pos)
f6.close()