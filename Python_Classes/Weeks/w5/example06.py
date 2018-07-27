# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:52:58 2017

@author: andre
"""
salary=int(input("enter a salary: \n")) 
yearOnJob=int(input("enter years of experience: \n"))

if salary>=3000: 
       if yearOnJob>=3: 
             print("you qualify for a loan") 
       else: 
             print("you qualify for a half of a loan") 
else: 
        if yearOnJob>=10: 
             print("you qualify for a half of a 25% of a loan ") 
        else: 
             print("You do not qualify for loans")
             