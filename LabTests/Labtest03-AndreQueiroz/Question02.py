# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:02:16 2017

@author: andre queiroz
Question 02 Lab test 03
"""

choice = 'y'
print ('Hello!')
choice = input('Say hello again? (y/n): ')
while choice == 'y' or choice == 'Y':
    print ('Hello!')
    choice = input('Say hello again? (y/n): ')
print('Bye!')
