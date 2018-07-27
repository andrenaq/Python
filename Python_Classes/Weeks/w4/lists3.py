list8= ['physics', 'chemistry', 'math']
list8.pop() #remove an element from right
print (list8)
list8.extend(['math'])
print (list8)
list8.pop(2) #remove an element at index 2
print (list8)
#list8.pop('physics')#error, use remove instead
list8.remove('physics')
print (list8)
list8.insert (0,'physics')#use insert to add elements at arbitroray position
print (list8)