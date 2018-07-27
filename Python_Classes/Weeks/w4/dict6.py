list = {'Nabil':16,'Tanya':19}
search = int(input('enter the age you search for'))
print (list.items())
for name, age in list.items():
	if age == search:
		print (name)
		break
	
else:
	print ('key is not found')