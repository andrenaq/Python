# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:25:27 2017

@author: andre
"""

dueAmount = float(input("How much is due? "))
dueAmount < 1000 
if dueAmount: 
   interest= dueAmount * 0.07 
   print ("the interest on", dueAmount, "is:", interest) 
#   var2 = 0 
elif dueAmount <10000: 
   interest= dueAmount * 0.15 
   print ("the interest on", dueAmount, "is:", interest) 
else: 
   interest= dueAmount * 0.25 
   print ("the interest on", dueAmount, "is:", interest) 
print ("See You Later")