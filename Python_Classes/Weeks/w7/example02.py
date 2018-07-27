# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:59:38 2017

@author: andre
"""

#Yum Yum Burger Joint
#the main function
def main():
    endProgram = 'no'
    print()
    while endProgram == 'no':
        totalBurger = 0
        totalFry = 0
        totalSoda = 0
        endOrder = 'no'
        while endOrder == 'no':
            print()
            print ('Enter 1 for Yum Yum Burger')
            print ('Enter 2 for Grease Yum Fries')
            print ('Enter 3 for Soda Yum')
            option = input('Enter now ->')
            if option == '1':
                totalBurger = .99
            elif option == '2':
                totalFry = .79
            elif option == '3':
                totalSoda = 1.09
            else:
                print ('You have entered an invalid option!!!')
        endOrder = input('Do you want to end your order? (Enter yes or no): ')
        print()
        total = totalBurger+totalFry+totalSoda
        printReceipt(total)
        endProgram = input('Do you want to end program? (Enter no to processa new order): ')

#this function will get burger order
def getBurger(totalBurger):

#this function will get fry order
def getFry(totalFry):

def getSoda(totalSoda):

def calcTotal(totalBurger, totalFry, totalSoda):

def printReceipt(total):
 print ('The total price is $', total)

# calls main
main()