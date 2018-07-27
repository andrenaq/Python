# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:28:34 2017

@author: andre
"""

myTuple = ('hello', 'October', 2016, 'it', 'is', 'now, 21.5' ,'Celsius' )
mySubTuple = ('October', 2016, 21.5)
print (myTuple) # Prints a complete tuple
print (myTuple[2]) # Prints the first element of the tuple
print (myTuple[2:5]) # Prints elements starting from 3rd till 6th
print (myTuple[3:]) # Prints elements starting from 4th element
print (mySubTuple * 2) # Prints myTtuple two times
print (myTuple + mySubTuple) # Prints concatenated tuple



mySubTuple [2]= 18.8 #TypeError: 'tuple' object does not support item assignment
myList =['October', 2016, 21.5] #--------- valid/invalid? Valid
mySubTuple[2] = 18.8 #----------------- valid/invalid? Invalid