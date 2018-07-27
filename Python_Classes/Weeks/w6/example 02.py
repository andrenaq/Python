# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 08:47:30 2017

@author: andre
"""

for x in list(range (1,4)): 
    num = int(input ('enter a number')) 
    while num <= 10: 
        print ('the number ', num,' is good') 
        num+=1 
    else: print ('the number ', num,' is not good') 
else: 
    print ('sorry! No more chance')
    
    
print(list(range(1,4)))
print(str([1,2,3]))
print([1,2,3])
print("1")