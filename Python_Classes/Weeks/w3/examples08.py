# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:49:57 2017

@author: andre
"""

list8=['physics', 'chimistry','math']
print(list8)
list8.pop()
print(list8)
list8.extend(['math'])
print(list8)
list8.pop(2)
print(list8)
list8.remove('physics')
print(list8)
list8.insert(0,'physics')
print(list8)
list9 = ['English','French']
list8.append(list9)
print(list8)