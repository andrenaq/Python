# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 09:06:52 2017

@author: andre
"""
import numpy as np
def courseNameF():
    return input('What is the name of the course: ')
def scoresF():
    grade=[]
    numberStudents = int(input('How many students took the test: '))
    for i in range(0, numberStudents):
        grade.append(int(input('Enter their score: ')))
    return grade
def averageF(grades):
    return np.mean(grades)


scores=[]
continueV =0

while continueV<3:
    courseName = courseNameF()
    scores = scoresF()
    average = averageF(scores)
    print('The average test score is',average)
    print('The name of the course: ', courseName)
    continueV += 1
    if continueV == 3:
        answer = input('Do you want to end program? (Enter no to process a new set of scores): ')
        if answer in ("nope"):
            continueV = 0
