# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:33:10 2017

@author: tiago
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:56:23 2017

@author: andre & tiago
"""

import pandas as pd

def entryData(file='phone.csv'):
    data = pd.read_csv(file,sep=',')
    return(data)

def validation(data):
    valid=[]
    for i in data:
        recordflag=''
        try:
            if not 1 <= int(i['Month']) <= 12:
                raise(ValueError)
        except ValueError:
            print(i['Month'],'is not a valid Month. Use integer numbers between 1 and 12.')
            recordflag+='Month;'
        try:
            if not 200 <= float(i['Minutes Allowed']) <= 800:
                raise(ValueError)
        except ValueError:
            print('The number of Minutes Allowed (%s) for the Month %s is not valid. Enter a value between 200-800.'%(i['Minutes Allowed'],i['Month']))
            recordflag+='Minutes Allowed;'

        try:
            if float(i['Minutes Used'])<=0:
                raise(ValueError)
        except ValueError:
            print('The number of Minutes Used for the Month %s is not valid. Enter a value greater than 0.'%(i['Month']))
            recordflag+='Minutes Used;'

        valid.append(recordflag)

    data.assign(validation = valid)
    if max(data['validation'])!='':
        dataFlag=1
    else:
        dataFlag=0

    return(data,dataFlag)

def calcOverUse(data):
    data.assign('Minutes Over'= max([data['Minutes Used'] - data['Minutes Allowed'],0]))
    return data

def calcDueTotal(data,minValue=0.2,cRate=74.99):
    data.assign('Month Total Due' = data['Minutes Over']*minValue + cRate)
    return data

def printBill(data):
    print('=========================Phone Usage Report=========================' )
    print(data)
    print('====================================================================' )
    print('Minutes over the contracted amount are charged $0.20.')

def savetBill(data,fname='phoneOut.csv'):
   data.to_csv(fname,sep=',')

def getTextInput(text,validValues):
    while True:
        value=input(text)
        if value.upper() in (validValues):
            return value
        else:
            print('Enter %s.'%(validValues))

def main():
    fileData = entryData('phone_t.csv')
    validatedData,errorFlag = validation(fileData)
    goOn='Y'
    if errorFlag==1:
        goOn=getTextInput('There are errors in the file. Some records will be skipped. Continue (y/n): ',['Y','N'])

    if goOn=='N':
        print('Please correct the file!')
    else:
        validatedData=validatedData[validatedData[validation=='']]
        validatedData=calcOverUse(validatedData)
        validatedData=calcDueTotal(validatedData,0.2,74.99)
        printBill(validatedData)
        savetBill(validatedData,'phoneOut.csv')




if __name__ == '__main__':
    main()
