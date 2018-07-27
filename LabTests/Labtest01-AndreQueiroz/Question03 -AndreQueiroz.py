# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:01:10 2017

@author: andre
"""

firstName = input("Please input your First name: ")
lastName = input("Please input your Last name: ")
numberPapers = int(input("Please input the namber of papers you would like to mark: "))

#numberPapers = input("Please input the namber of papers you would like to mark: ")
#For any value of numberPapers (Ex. "Five")

print("Hi %s %s. You have been assigned %s yellow tests to distribute." %(firstName,lastName,numberPapers))
print("Hi {} {}. You have been assigned {} yellow tests to distribute.".format(firstName,lastName,numberPapers))