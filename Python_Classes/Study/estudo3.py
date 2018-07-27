# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:10:21 2017

@author: andre
"""
b=13
def main():
    teste()
    print(b)
def teste():
    global b
    print(b)
    b+=1



if __name__ == '__main__':
    main()