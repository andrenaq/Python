# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:38:40 2017

@author: andre
"""

# Opening a file
f1 = open("file1.txt", "w")
print ("The name of the file is: ", f1.name)
print ("File closed : ", f1.closed)
print ("The opening mode is : ", f1.mode)
f1.close()
