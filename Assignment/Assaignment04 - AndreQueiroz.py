# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:35:48 2017

@author: andre
"""  
def pop(d,strList):
    i=0
    strList2=[]
#    strList.remove('d')
    while i <len(strList):
        if strList[i] != d: strList2.append(strList[i])
        i+=1
    return strList2

def writeFile(strList,fName):
    with open(fName,'w+') as file:
        file.writelines([x+'\n' for x in strList])
        file.close()
        
def readFile(fName):
    with open(fName,'r') as file:
        strList = file.readlines()
        file.close()
        return strList
    
def main():
    fName = 'FileA.txt'
    stringList = ['d','d','a','b','d','c','d','e','f','d','g','h','i','j','l','d','m','n','o','d','p','q']
    delString = 'd'
    stringList = pop(delString,stringList)
    writeFile(stringList,fName)
    stripList = [items.strip() for items in readFile(fName)]
    print(stripList)
    
if __name__ == '__main__':
    main()
    