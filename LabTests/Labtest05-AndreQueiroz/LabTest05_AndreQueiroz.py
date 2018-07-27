# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 08:43:57 2017

@author: andre
"""
#Lab test 05 part 01
def main():
#    with open('Labtest05.txt','w') as f0:
#        f0.write('Video provides a powerful way to help you prove your point.\nWhen you click Online Video, you can paste in the embed code for the video you want to add.\nYou can also type a keyword to search online for the video that best fits your document.\nTo make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. ')
#        f0.close
    with open('Labtest05.txt','r') as f1:
        c = f1.readlines()
        for _ in range(0,len(c)):
            print(str(c[_]).strip())
        f1.close
    with open('Labtest05.txt','a') as f2:
        f2.writelines('new line appended\n')
        f2.close
main()