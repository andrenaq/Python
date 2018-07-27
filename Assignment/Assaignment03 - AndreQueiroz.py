# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 08:45:13 2017

@author: andre
"""

#Yum Yum Burger Joint
#the main function
def main():
    print('Welcome to Yum Yum. \nMay I take your order?')
    endProgram = 'no'
    print()
    while endProgram == 'no':
        totalBurger = 0
        totalFry = 0
        totalSoda = 0
        endOrder = 'no'
        #getSoda = lambda x: x + 1.09
        #calcTotal = lambda x,y,z: x+y+z
        while endOrder == 'no':
            print()
            print ('Enter 1 for Yum Yum Burger')
            print ('Enter 2 for Grease Yum Fries')
            print ('Enter 3 for Soda Yum')
            option = input('Enter now ->')
            if option == '1':
                number = numberValidation('How many?\n->')
                totalBurger = getBurger(totalBurger,number)
            elif option == '2':
                number = numberValidation('How many?\n->')
                totalFry = getFry(totalFry,number)
            elif option == '3':
                number = numberValidation('How many?\n->')
                totalSoda = getSoda(totalSoda,number)
            else:
                print ('You have entered an invalid option!!!')
                endOrder = input('Do you want to end your order? (Enter yes or no): ')
        print()
        total = calcTotal(totalBurger,totalFry,totalSoda)
        printReceipt(total)
        endProgram = input('Do you want to end program? (Enter no to processa new order): ')

def getBurger(totalBurger,numb): #this function will get burger order
    return ((totalBurger + 0.99)*numb)
def getFry(totalFry,numb): #this function will get fry order
    return ((totalFry+0.79)*numb)
def getSoda(totalSoda,numb):
    return ((totalSoda+1.09)*numb)
def calcTotal(totalBurger, totalFry, totalSoda):
    return (totalBurger+totalFry+totalSoda)
def printReceipt(total):
    print ('The total price is $', total)
def numberValidation(text):
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
                print('That does not look like a valid number.') 
                 

# calls main
if __name__ == '__main__':
    main()