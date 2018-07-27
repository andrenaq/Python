list = {'Nabil':16,'Tanya':19}
search = input('enter the age you search for')
print (list.items())#listing all elements of list dictionary
for name, age in list.items():
	if name == search:#searching for a matching name
		print (name)
		break
	
else:
	print ('key is not found')