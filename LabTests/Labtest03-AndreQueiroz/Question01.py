# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 10:02:16 2017

@author: andre queiroz
Question 01 Lab test 03
"""

test_score = 0
counter = 0
score_total = 0
while test_score != 999:
    test_score = int(input('Enter test score: '))
    if (test_score >=0 and test_score<=100):
        score_total += test_score
        counter += 1
average_score = round(score_total / counter)
print('Total Score: ' + str(score_total))
print('Average Score: ' +str(average_score))