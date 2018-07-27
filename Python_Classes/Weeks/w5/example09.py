# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:56:38 2017

@author: andre
"""

limit = 1000; interest = 0.1
balance = float(input('enter a balance: '))
while balance < limit:
    balance = balance +balance + interest
    print('the balance is now: ',balance)