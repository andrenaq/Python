# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:43:51 2017

@author: andre
"""

# Open a file for reading and writing
f3 = open("file1.txt", "r+")
strg = f3.read(10)
print ("The string is : ", strg)
# To return the current position of the file pointer
pos = f3.tell()
print (" The current file position is : ", pos)
pos = f3.seek(30, 0)
strg9 = f3.read(20)
print ("Now read String : ", strg9)
pos = f3.tell()
print (" The current file position is : ", pos)
f3.close()