myDict = {'empName': 'Simon', 'title': 'Director', 'yOfEmp': 8}
print(myDict)
print ("myDict['empName']: ", myDict['empName'], myDict['title'])
myDict2 = {('empName'): 'Simon', 'title': 'Director', 'yOfEmp': 8}
#myDict3 = {['empName']: 'Simon', 'title': 'Director', 'yOfEmp': 8}#keys can not be mutable type like list
print (myDict2['title'])
#print (myDict2['address'])# key is not found
myDict['manager']='Simon' # a dictionary can have duplicated values
print(myDict)
print (myDict3['title'])  
print(len(str(123)))

