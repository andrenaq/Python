# -*- coding: utf-8 -*-
"""
@author: andre queiroz & tiago rubio
"""
import re
sales,salesLastMonth = ('','')
while not re.fullmatch(r'^[0-9]+\.?[0-9]*$',sales): 
    sales = input('Enter how much the store sold this month: \n')
while not re.match(r'^[0-9]+\.?[0-9]*$',salesLastMonth):
    salesLastMonth = input('Enter how much the store sold the month before: \n')
sales = float(sales)
salesLastMonth = float(salesLastMonth)
storeBonusDict = {3000:80000,4000:90000,5000:100000,6000:110000,0:0}
employeeBonusDict = {40:3,50:4,75:5}
storeBonus =0
employeeBonus = 0
improvement = ((sales/salesLastMonth)-1)*100

if sales >=  80000: storeBonus = 3000
if sales >=  90000: storeBonus = 4000
if sales >= 100000: storeBonus = 5000
if sales >= 110000: storeBonus = 6000

if (improvement)>= 3: employeeBonus = 40
if (improvement)>= 4: employeeBonus = 50
if (improvement)>= 5: employeeBonus = 75

print('The store sold ${} this month and ${} last month'.format(sales,salesLastMonth))
if (improvement>0): 
    print('The sales improvement was %0.2f percent'%improvement)
else: 
    print('There was no sales improvment')
if storeBonus>0:
    print('The store reached the $%d goal. The store bonus will be $%d'%(storeBonusDict[storeBonus],storeBonus))
else:
    print('The store did not reach its sales goals. The store bonus will not be payed')
if employeeBonus>0: 
    print('The store reached the %d percent increase in sales goal. The employee bonus will be $%d'%(employeeBonusDict[employeeBonus],employeeBonus))
else:
    print('The store did not reach its increase sales goal. There employee bonus will not be payed')

#    The following programming problem:
#    A retail company assigns a $5000 store bonus if monthly sales are more than $100,000; 
#    otherwise a $500 store bonus is awarded.  
#    Additionally, they are doing away with the previous day off program and are now using 
#    a percent of sales increase to determine if employees get individual bonuses.  
#    If sales increased by at least 4% then all employees get a $50 bonus. 
#    If they did not, then individual bonuses are 0. 
#    Use functions and decision structures.
#    The company now wants to add additional levels to their store and employee bonuses.  
#    The new levels are as follows:
#    If percent of increase is 3% or more, employee bonus is $40
#    If percent of increase is 4% or more, employee bonus is $50
#    If percent of increase is 5% or more, employee bonus is $75

#    If store sales are $80,000 or more, store bonus is $3000
#    If store sales are $90,000 or more, store bonus is $4000
#    If store sales are $100,000 or more, store bonus is $5000
#    If store sales are $110,000 or more, store bonus is $6000
