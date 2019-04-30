# implement an algorithm to see if a string has unique characters

def unique(s):
	 return len(s) == len(set(s))

a= 'abcd'
b= 'aabcddcs'

print(unique(a))
print(unique(b))

#no built in function

def nobuilt(s):
	 hashmap = set()
	 for i in s:
	 	if i in hashmap:
	 		return False
	 	else:
	 		hashmap.add(i)
	 return True 
print('no built funtion solutions')
print(nobuilt(a))
print(nobuilt(b))