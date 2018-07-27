# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 07:32:56 2017

@author: andre
"""

with open('tratina.txt','w') as f1:
    f1.writelines('abcdefg\n')
    f1.writelines('hijklmn\n')
    f1.close
with open('tratina.txt','r') as f2:
    a=f2.readlines()
    for i in range(0,len(a)):
        a[i]=str(a[i]).strip()
    f2.close
with open('tratina.txt','r+') as f3:
    print(f3.tell())
    f3.seek(0,2)
    print(f3.tell())
    print(f3.readline())