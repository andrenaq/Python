# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:39:19 2017

@author: andre
"""

#reading a file; it must be created first.
f2 = open("file1.txt", "r") #try r+ and with no mode specified, try also after deleting the file1
strg=f2.read(50)
print (" The sring is: ", strg,"\n")
# Close opened file
f2.close()
