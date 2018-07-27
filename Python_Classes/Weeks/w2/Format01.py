# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:49:15 2017

@author: andre
"""

instructor = input("Enter the prof's name: ")
subject= input("Enter the subject name: ")
term = input("Enter the term: ")
format= '{} will teach {} in {} term . '
format02=('{1} will be taght by {0} in {2} term')
print(format.format (instructor,subject,term))
print(format02.format(instructor,subject,term))
