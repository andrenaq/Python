# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:28:59 2017

@author: andre
"""

num = int(input("enter number: \n"))
if num%2==0:
    if num%3==0:
        print("Divisible by 3 and 2")
    else:
        print("Divisible by 2 not by 3")
else:
    if num%3==0:
        print("Divisible by 3 not by 2")
    else:
        print("Not divisible by 2 or by 3")