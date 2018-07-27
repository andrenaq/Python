# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 08:57:22 2017

@author: andre
"""

def main():
#    with open('Labtest06.txt','w') as f0:
#        f0.write('Video provides a powerful way to help you prove your point. ')
#        f0.close
    with open('Labtest06.txt','rb+') as f1:
        f1.read(10)
        print(f1.tell())
        f1.seek(20)
        f1.read(5)
        print(f1.tell())
        f1.close
        #"A different way of doing print(lin,end='') is:
        lin ='A powerful way to help you prove your point. '
        print(lin.rstrip())
main()