# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 08:43:12 2017

@author: andre
"""

def main ():
    value =int(input('enter a value: \n'))
    myfun2(value)
    #myfun2(value)
    #changedValue=myfun2(value) #changes inside myfun2 will be visible in the main fun
    print ('after call', id(myfun2(value)))
    print ('after call', id(value))
def myfun2(value):
    value=value+9
    print ('inside the myfun2', id(value))
    return value
main()
