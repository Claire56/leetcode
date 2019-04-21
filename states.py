
# given a list of cells, active cells are labelled 1 and inactive 0, cells compete with
# their neighbors if both neighbors have same values then the next day that cell will be inactive
# if they have different values then the next day that cell will be active. return state of cells after k days
#example listg = [0,1,0,1,0,1,0,1],k=1.   =>[1,0,0,0,0,0,0,0]



listg = [0,1,0,1,0,1,0,1]
l2 =[1,1,1,1,1,1,1]	
l3=[1,0,0]

def newstate(states,k):
	states.append(0)
	states.insert(0,0)
	n = len(states)
	print(states)
	states2=[]

	while k>0:
		for i in range(1,n-1):
			if states[i-1] == states[i+1]:
				states2.append(0)
			else:
				states2.append(1)

			k-=1

	return states2
		



		
# print(newstate(l2,5))
print(newstate(l3,5))
