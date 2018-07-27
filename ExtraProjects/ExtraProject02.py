# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:00:46 2017

@author: andre
"""
import re
import calendar

def enterEnergyBills(year):
    priorYear=[]
    print("\nPlease, enter the energy bills from January to December {}\a".format(year))
    for i in range(0, 12):
        a=i+1
        number = input("Enter the energy bill for the month of %s:" %calendar.month_name[a]) #, priorYear[i])
        while not re.match('^-?[0-9]*\.?[0-9]+$',number):
            print("\n ***------***------***------***------***------***------***")
            number = input("Something went wrong.\nEnter again the energy bill for the month of %s: \n\a" %calendar.month_name[a])
        priorYear.append(float(number))
    return priorYear

def compareEnergyBills(before,after,option):
    savings=[]
    for i in range(0,12):
        if option == 0:
            savings.append((after[i]/before[i])*100)
        else: 
            savings.append(before[i] - after[i])
    return savings

def printResults(previousY,nextY,saving):
        with open('savings.txt','w') as file:
            #print("Month\t\t","Prior\t\t","After\t\t","Savings")
            print("Month\t\tPrior\t\tAfter\t\tSavings")
            file.write("Month\t\tPrior\t\tAfter\t\tSavings\n")
            for i in range(0,12):
                print('{}\t\t{:04.2f}\t\t{:04.2f}\t\t{:04.2f}'.format(calendar.month_abbr[i+1],previousY[i],nextY[i],saving[i]))
                file.write('{}\t\t{:04.2f}\t\t{:04.2f}\t\t{:04.2f}\n'.format(calendar.month_abbr[i+1],previousY[i],nextY[i],saving[i]))
        file.close()
previousYear = (enterEnergyBills("for the year prior to going green"))
nextYear = (enterEnergyBills("of the past year after going green"))
#savings01 = compareEnergyBills(previousYear,nextYear,0)
savings02 = compareEnergyBills(previousYear,nextYear,1)
printResults(previousYear,nextYear,savings02)

print("The month with most savings was %s" %calendar.month_name[savings02.index(max(savings02))+1],":",max(savings02))
print("The month with less savings was %s" %calendar.month_name[savings02.index(min(savings02))+1],":",min(savings02))

try:
    monthNumber = int(input("To consult a specific month, type month number[1-12].\nTo exit type anything else: "))
    while (monthNumber) in range(1,13):
        print("\nThe month selected is %s and its savins: %s" %(calendar.month_name[monthNumber],savings02[monthNumber-1]))
        monthNumber = int(input("To consult a specific month, type month number[1-12].\nTo exit type anything else: "))
except ValueError:
    print("GoodBye")
    
k=input("Press ENTER to EXIT") 

#print(calendar.month_abbr[i+1],"\t\t", previousY[i],"\t\t",nextY[i],"\t\t",saving[i])




