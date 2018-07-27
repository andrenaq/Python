# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 09:23:49 2017

@author: andre
"""
from math import Random

def main():
    acre = 43560
    lArea = landArea()
    cArea = calcArea(acre,lArea)
    displayArea(cArea)
    
def landArea():
    while True:
        try:
            return float(input("Enter the total square feet in tract of land.\n->"))
        except ValueError:
            print('That was not a valid number!!!!! \a')
main()

def calcArea(ac,list):
    return ( list/ ac)
def displayArea(cA):
    print('Total area is: {:.2f} acres'.format(cA))
number = Random.random()
number = Random.randomfloat()