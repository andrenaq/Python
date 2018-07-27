# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:24:23 2017

@author: andre
"""

def print_required( myVal1, myStr1 ): #"This prints a passed string into this function" 
    print (myStr1, myVal1) 
    return 
# Now you can call print-required function 
myStr ='Jan Donald' 
myVal= 12209 
print_required(myVal, myStr) 
#Jan Donald 12209 
print_required(myStr, myVal)#12209 Jan Donald 
#print_required(myVal)# error, not in the positional order