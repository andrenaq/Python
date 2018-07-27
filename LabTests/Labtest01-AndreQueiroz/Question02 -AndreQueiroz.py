# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:49:00 2017

@author: andre
"""
a = "andre"
b = "bruno"
c = "carlos"
d = "debora"
e = "eduardo"
friends = [a,b,c]
friends.append(d)
friends.append(e)
friends.remove(friends[3])
friends.remove("bruno")
friends.pop()
friends.append([b,d,e])
