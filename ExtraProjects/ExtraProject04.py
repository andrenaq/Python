"""
Created on Mon Oct 30 17:27:40 2017

@author: andre
"""
import random as r
import re

def enterName():
    enterName=input('Please, informe your name:\n')
    while not re.match(r'^[a-zA-Z]+[a-zA-Z ]*$',enterName):
        enterName=input('Please, informe your name:\n')
    return enterName

def randomNumbers():
    a = r.randrange(1,500)
    b = r.randrange(1,500)
    return [a,b]

def equation(numb,iteration):
    uAnswer = input('Problem number %d:\n %d - %d = '%(iteration,numb[0],numb[1]))
    while not re.match(r'^-?[0-9]+\.?[0-9]*$',uAnswer):
        uAnswer = input('Problem number %d:\n %d - %d = '%(iteration,numb[0],numb[1]))
    uAnswer = float(uAnswer)
    right = isCorrect(numb,uAnswer)
    return right

def isCorrect(numb,uAnswer):
    rAnswer = numb[0]- numb[1]
    isCorrect = 1  if rAnswer == uAnswer else 0
    print('Correct!') if isCorrect == 1 else print('Wrong Answer!! \a')
    return isCorrect

def writtenResults(name,Total,finalResult,iterator):
    print()
    print('============= Results ============= \a')
    print(name)
    print('You have answered {} equation(s) correctly out of {} presented.'.format(Total,iterator))
    print('That is {:.2f}% of the total.'.format(finalResult))
    
studentName =enterName()
Total= 0
result = lambda x,y: (x/y)*100
for i in range(1,11):
    Total += equation(randomNumbers(),i)
    print('{:.2f}% correct so far'.format(result(Total,i))) 
writtenResults(studentName,Total,result(Total,i),i)
k=input("Press ENTER to EXIT") 