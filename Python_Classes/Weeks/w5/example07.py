# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:46:53 2017

@author: andre
"""

amount = 0
count = int(input("enter a number smaller then 10: \n"))
while (amount <= 10000 and count < 10):
    amount+= 100
    count+=1
    print(amount, count)
print (" This was an example of while!")
