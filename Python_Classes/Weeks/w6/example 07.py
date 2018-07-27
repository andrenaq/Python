# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 09:54:10 2017

@author: andre
"""

for letter in 'English':
    if letter =='p':
        print('there is a letter',letter)
        break
else: print('we can\'t find a match letter')

print(list('English'))
letter = 'E'
if letter in 'English': print('ok')