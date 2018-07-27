# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:14:32 2017

@author: andre
"""

import random
print('returns a random number from range(100): ', random.choice(range(100)))
print('returns a random element from list [1,2,3,5,9]: ', random.choice([1,5,3,9,'11']))
print("returns a random element from string 'Hello World' : ", random.choice('Hello World'))
print (random.random()) #Random number between 0-1
print ("random float uniform 10>= r < 15) : ", random.uniform(10,15))