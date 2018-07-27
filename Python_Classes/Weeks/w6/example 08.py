# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:28:22 2017

@author: andre
"""

presidents = ['Clinton', 'Regan', 'Obama', 'Bush', 'Trump']
for pres in presidents:
    if pres == 'Obama':
        print('Obama is not my favorite president!')
        continue
    print('Great leader: ' + pres)
else:
    print('I am so glad: No Obama!')
print('Finally, I got the list of my favorit USA presidents')