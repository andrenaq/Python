# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:52:18 2017

@author: andre
"""

def main ():
    value =int(input('enter a value'))
    myfun2(value)
    #changedValue=myfun2(value) #changes inside myfun2 will be visible in the main fun
    print ('after call', value)
    #print ('after call', changedValue)
def myfun2(value):
    value=value+9
    print ('inside the myfun2', value)
    return value

main()
