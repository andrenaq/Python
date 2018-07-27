# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:05:44 2017

@author: andre
"""
myDict = {'empName': 'Simon', 'title': 'Director', 'yOfEmp': 8}
print ("myDict [empName]: ", myDict [empName]) 
print ("myDict [title]: ", myDict [title])
print ("myDict [Director]: ", myDict.keys())#'Director'))
print(myDict)

myDict = {'empName': 'Simon', 'title': 'Director', 'yOfEmp': 8}
myDict = {'empName': 'Simon', 'title': 'Director', 'yOfEmp': 8, 'title':'teacher'}

del myDict['empName']
myDict.pop('empName')
del myDict
a = len(myDict)
b = str(myDict['title'])
b=b.capitalize()
b= type(myDict['title'])
print(b)
print(myDict.items())
dict1 = {'a2':'3', 'k1':'89', 'z4':'5', 'd3':'0'}
sortdict1 = dict(sorted(dict1.items()))
for k,v in sortdict1:
    print(k,v)

list1 = {'Nabil':16,'Tanya':19} 
search = int(input('enter the age you search for'))
search = 19
for name,age in list1.items():
    if age == search:
        print(name)

print([1,2,3,4,5])
print(list1.items())
for i,j in list1.items():
    next
    print(i,j)
tup1 = ('physics', 'chemistry', 1997, 2000)
list1 = ["1",'2','3']
list2 =['4','5']
print(list1.append(list(list2)))
print(list(list1))



it = iter(list1)

for i in it:
    print(i)
print(it)



















