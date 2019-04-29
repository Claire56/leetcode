# given two sorted lists return one sorted list

def joinSortedLists(a,b):
	ab = []
	while a or b:
		if not a:
			ab.extend(b)
			return ab
		elif not b:
			ab.extend(a)
			return ab
		elif a[0]< b[0]:
			ab.append(a[0])
			a.pop(0)
		else:
			ab.append(b[0])
			b.pop(0)
	return ab



a=[1,3,5,9]
b=[0,4,8,10]
print(joinSortedLists(a,b))