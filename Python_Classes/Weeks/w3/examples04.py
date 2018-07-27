# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:20:27 2017

@author: andre
"""

#!/usr/bin/python3
myList = [ 'Monday', 19 , 2000, 'is', 'forgotten' ]
mySubList = ['date', 0]
print (myList) # Prints complete list
print (myList [0]) # Prints first element of the list
print (myList [-2]) # Prints second elemt from right
print (myList [2:4]) # Prints elements starting from 2nd till 3rd
print (myList [3:]) # Prints elements starting from 3rd element
print (mySubList * 2) # Prints list two times
print (myList + mySubList) # Prints concatenated lists
print("hello\n", str(myList))
print("hello\n", (myList))
myList [4]= 'unforgotten'
print ("print an updated list", myList)
myList.append( "teste")
print ("print an updated list", myList)
print(myList.count("teste"))
print(myList.index("teste"))
myList.insert(2,"teste")
print ("print an updated list", myList)
tp = ('ff','rr')
l=list(tp)
print('l ',l)

