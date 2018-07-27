# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:45:22 2017

@author: andre
"""

def shopping(kind, *arguments, **keywords): 
    print("-- Do you have any", kind, "?") 
    print("-- I'm sorry, we're all out of", kind) 
    for arg in arguments: 
        print(arg, end=" ") 
    print("\n","-" * 40) 
    keys = sorted(keywords.keys()) 
    for _ in keys: 
        print(_, ":", keywords[_]) 
shopping("umberlla", "It's very runny, sir.", "It's really very",
         "VERY runny, sir.",'teste', 'casa','monkey', shopkeeper="Tom Kennedy",
         client="John Right", sketch="Variety Shop Sketch",user='Andre')