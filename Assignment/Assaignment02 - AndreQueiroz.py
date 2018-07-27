# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:13:52 2017

@author: andre
"""
import calendar as c
import re
#import os #imported to clear screen after the program runs
def enterQuantity(day): # checks the amont of bottles colected in a day
    numberDay = input('Please input the number of bottles collected on {}: \n'.format(c.day_name[day]))
    while not re.match(r'^[0-9]+\.?[0]?$',numberDay): #validates the entry
        print()
        numberDay = input('Something was wrong with the inputed number! \n\a Please input the number of bottles collected on {}: \n'.format(c.day_name[day]))
    return float(numberDay)

def runAgain(): #evaluates if the user wants to run the program again
    answer = input('Do you want to run the program again?(y/n)')
    while answer.lower() != 'y' and answer.lower() !='n': #validates the entry
        answer = input('\aDo you want to run the program again?(y/n)')
    runAgain = True if answer.lower()== 'y' else False
    return runAgain

def printResults(pce,ttl):
    print()
    for i in range(0,7):
        print('{:7.0f}\tbottles were colected On {} '.format(ttl[i],c.day_name[i]))
    print('The total number of bottles collected was {:.0f}'.format(sum(ttl)))
    print('The total paid out was {:.2f}'.format(pce*sum(ttl)))
    
def main_program():
    rAgain = True
    while rAgain:
        #os.system('cls' if os.name == 'nt' else 'clear') #comand to clear the pront after the first run
        totalBottles = []
        price = 0.1
        for i in range(0,7):
            totalBottles.append(enterQuantity(i))
        printResults(price,totalBottles)
        rAgain = runAgain()
    
main_program()
#Write a program in python that will allow a grocery store to keep track of the 
#total number of bottles collected for seven days.  The program should allow the 
#user to enter the total number of bottles returned for seven days.  The program 
#will calculate the total number of bottles returned for the week and the amount 
#paid out (the total returned times .10 cents).  The output of the program should 
#include the total number of bottles returned and the total paid out. Make sure 
#to use functions and repetition structures. All data entered must be validated. 
#Users should be allowed to run the program again.