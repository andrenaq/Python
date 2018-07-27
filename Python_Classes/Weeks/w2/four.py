# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:49:15 2017

@author: andre
"""

instructor = input("Enter the prof's name: ")
subject= input("Enter the subject name: ")
term = input("Enter the term: ")
format= '{} will teach {} in {} . '
print(format.format (instructor,subject,term))
