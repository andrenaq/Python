# -*- coding: utf-8 -*-
import pandas as pd
import math as m
def entryData(file):
    file = ('phone.csv')
    data=[]
    a = pd.read_csv(file,sep=',')
    for  i in range(0,len(a)): data.append(a.iloc[i][1])
    return(data)

def validation(data):
    data1=[]
    for i in range(0,len(data)):
        try:
            data1.append(float(data[i]))
        except ValueError:
            if i==0: 
                print('The value inputed as minutes allowed in a month is not a vlaid number')
                data1.append('error')
            if i==1:
                print('The value inputed as minutes used this month is not a vlaid number')
                data1.append('error')
            if i==2:
                if data[i] == 'n' or data[i] == 'y' or m.isnan(data[i]):
                    data1.append(data[i])
                else:
                    print('There was an error selecting the calculation of anual usage')
                    data1.append('error')
            if i>2 and i<15:
                print('The value inputed as minutes used for the month {} is not a vlaid number'.format(i-2))
                data1.append('error')
    return(data1)
def validation2(data):
    valid = True
    try:
        wasThereAnError=data.index('error')
    except ValueError:
        if data[0]>800 or data[0]<200:
            print('The limit of minutes is out of range. Must be between 200-800.')
            valid = False
        elif data[1] < 0 or m.isnan(data[1]):
            print('The number of minutes used must be greater then 0.')
            valid = False
        elif str(data[2]).lower() == 'y':
            for i in range(3,15):
                if  data[i]<=0 or m.isnan(data[i]):
                    print('The number of minutes used for the month {}  must be greater then 0.'.format(i-2))
                    valid = False
        return valid
def extraCharge(allowed,consume):
    minValue = 0.2
    extra = consume - allowed
    if extra>0:
        extra = extra * minValue
    else:
        extra = 0
    return extra
def printBill(extra,allowed):
    savetBill(extra,allowed)
    print('=========================Phone Usage Report=========================' )
    print('Month\t\t\tMinutes\t\tMinsOver\tBill')
    minutesOver = extra[0][0] - allowed
    if minutesOver < 0 :minutesOver =0
    print('ThisMonth\t\t{}\t\t{}\t\t${}'.format(extra[0][0],minutesOver,extra[0][1]+74.99))
    try:
        if extra[1][0] !='':
            print('-----------------------------------------------------------------')
            print('Annual usage:')
            for i in range(1,13):
                minutesOver = extra[i][0] - allowed
                if minutesOver < 0 :minutesOver =0
                print('month {:>2}\t\t{}\t\t{}\t\t${}'.format(i,extra[i][0],minutesOver,extra[i][1]+74.99))   
    except:
        pass
    print('====================================================================' )
    print('{:.0f} minutes allowed per month'.format(allowed))
    print('Minutes over the contracted amount are charged $0.20.')
def savetBill(extra,allowed):
    with open('Bill.txt','w') as sb:
        sb.write('=========================Phone Usage Report=========================\n' )
        sb.write('Month\t\t\tMinutes\t\tMinsOver\tBill\n')
        minutesOver = extra[0][0] - allowed
        if minutesOver < 0 :minutesOver =0
        sb.write('ThisMonth\t\t{}\t\t{}\t\t${}\n'.format(extra[0][0],minutesOver,extra[0][1]+74.99))
        try:
            if extra[1][0] !='':
                sb.write('-----------------------------------------------------------------\n')
                sb.write('Annual usage:\n')
                for i in range(1,13):
                    minutesOver = extra[i][0] - allowed
                    if minutesOver < 0 :minutesOver =0
                    sb.write('month {:>2}\t\t{}\t\t{}\t\t${}\n'.format(i,extra[i][0],minutesOver,extra[i][1]+74.99))
        except:
            pass
        sb.write('====================================================================\n' )
        sb.write('{:.0f} minutes allowed per month\n'.format(allowed))
        sb.write('Minutes over the contracted amount are charged $0.20.\n')
    sb.close()
    
def main():
    extraC=[]
    fileData = entryData('phone.csv')
    validInput01 = validation(fileData)
    validNumbers = validation2(validInput01)
    if validNumbers:
        extraC.append([validInput01[1],extraCharge(validInput01[0],validInput01[1])])
        #print(extraC[0][1])
        if str(validInput01[2]) =='y':
            for i in range(3,15):
                extraC.append([validInput01[i],extraCharge(validInput01[0],validInput01[i])])
        printBill(extraC,validInput01[0])
    else:
        print('Please correct the file!')
           
if __name__ == '__main__':
    main()
    