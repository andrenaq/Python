# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 10:39:48 2017

@author: andre
"""
def getHours():
    while True:
        try:
            return float(input('How many hours do you work a month?\n'))
        except ValueError:
            print ('Invalid number, try again')
def getPay():
    while True:
        try:
            return float(input('How much do you recieve for each hour?\n'))
        except ValueError:
            print ('Invalid number, try again')
def main():
    hours= getHours()
    hourlyPay = getPay()
    
    
    
if __name__ == '__main__':
    main()