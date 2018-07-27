# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 08:40:46 2017

@author: andre
"""
#‘r’	open for reading (default)
#‘w’	open for writing, truncating the file first
#‘x’	create a new file and open it for writing
#‘a’	open for writing, appending to the end of the file if it exists
#‘b’	binary mode
#‘t’	text mode (default)
#‘+’	open a disk file for updating (reading and writing)
#‘U’	universal newline mode (deprecated)
f4 = open('\\txtfiles\\filea.txt','x')#w+ w a 
f4.close()
f4 = open('\\txtfiles\\filea.txt','r+')#w+ w a 
f4.write('ssss')