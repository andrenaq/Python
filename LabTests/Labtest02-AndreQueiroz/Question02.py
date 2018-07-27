# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:02:16 2017

@author: andre queiroz
Question 02 Lab test 02
"""
#---Module 01
mydict = {'Vitamin E':200, 'Vitamin D':400, 'Vitamin C':100, 
          'Vitamin B2':350 , 'Milk Thistle' :150}
search = input('enter the vitamin you search for')
print(mydict.items())
print('----Module 01-----')
for vit,mlg in mydict.items():
    if vit == search:
        print (mlg)
        break
else:
    print('key is not found')
#If the name of the vitamin is found it prints the mlg and 'breaks' out of the four loop. 
#If not, it prints one time the phrase 'key is not found' 
    
#---Module 02
#mydict = {'Vitamin E':200, 'Vitamin D':400, 'Vitamin C':100, 
#          'Vitamin B2':350 , 'Milk Thistle' :150}
#search = input('enter the vitamin you search for')
#print(mydict.items())
print('----Module 02-----')
for vit,mlg in mydict.items():
    if vit == search:
        print (vit)
        continue
    print('key is not found')
#If the name of the vitamin is found it prints the name of the Vitamin and 04 times the phrase 'key is not found'
#in the order as they apear in the tuple
#key is not found
#Vitamin D
#key is not found
#key is not found
#key is not found

#If the name is not found, it prints five times the phrase 'key is not found' 