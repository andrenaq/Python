# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:44:58 2017

@author: andre
"""

file_name = "mystring.txt"
mystring = ['l','p','l','r','l','l']
#print("Enter 5 strings")
#for i in range(4):
#	x = input("Enter string")
#	mystring.append(x)
#	print(mystring)
    
def write_string(mystring):
	with open(file_name, "w") as file:
		for y in mystring:
			file.write(y + "\n")

		
def read_string(mystring):
	mystring = []
	with open(file_name) as file:
		for line in file:
			#line = line.replace("\n", "")
			line = line.rstrip()
			mystring.append(line)
			print(mystring)

def search_string(mystring = ['l','l','p','l']):
  z=0
  #search = input("Enter a string you want to search")
  search = 'l'
  search = str.lower(search)
  while z < len(mystring):
    if search == mystring[z]:
      mystring.pop(z)
    z+=1
  else:
    print("Sorry! String wasnt founld")
  print(mystring)
  
def main():
	write_string(mystring)
	search_string()
    
	#read_string(mystring)
main()