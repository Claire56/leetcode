def mergeSort(a):
	if len(a)>1:
		mid = len(a)//2
		L =a[:mid]
		R =a[mid:]
		mergeSort(L)
		mergeSort(R)

		R_index =L_index = a_index=0

		while L_index < len(L) and R_index <len(R):
			if R[R_index]< L[L_index]:
				a[a_index]=R[R_index]
				R_index +=1
			else:
				a[a_index]=L[L_index]
				L_index +=1

			a_index +=1

		#Checking if any. element was left
		while  R_index < len(R):
			a[a_index]=R[R_index]
			R_index +=1
			a_index +=1

		while L_index < len(L):
			a[a_index]=L[L_index]
			L_index +=1
			a_index +=1
	return a
print(mergeSort([5,8,1,9,10,3,9,2]))
#Bubble Sort
a = [5,8,10,9,10,3,9,2,1]
def bubble(a):
	n = len(a)
	swaps =0
	for i in range(n,1,-1):
		for j in range(1,i):
			if a[j-1]< a[j]:
				a[j],a[j-1] = a[j-1],a[j]
				swaps +=1
	return'sorted in {} swaps,Results:{}'.format(swaps,a)			
print(bubble(a))