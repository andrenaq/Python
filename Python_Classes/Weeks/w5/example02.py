# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:04:10 2017

@author: andre
"""
totalHours = float(input("How many hours do you work: "))
hourlyWage = float(input("What is your hourly wage: "))
if totalHours <= 40:
    totalWages = hourlyWage*totalHours
else:
    overtime = totalHours - 40
    totalWages = hourlyWage*40 + (1.5*hourlyWage)*overtime
print ("The total wage is " + str(totalWages))
