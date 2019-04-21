# Active and Inactive cells after k Days
# Given a binary array of size n where n > 3. A true (or 1) value in the array means active 
# and false (or 0) means inactive. Given a number k, the task is to find count of active and 
# inactive cells after k days. After every day, status of i’th cell becomes active if left and
# right cells are not same and inactive if left and right cell are same (both 0 or both 1).
# Since there are no cells before leftmost and after rightmost cells, the value cells before 
# leftmost and after rightmost cells is always considered as 0 (or inactive).

# Recommended: Please try your approach on {IDE} first, before moving on to the solution.
# Examples:

# Input  : cells[] = {1, 0, 1, 1}, k = 2
# Output : Active cells = 3, Inactive cells = 1
# After 1 day,  cells[] = {0, 0, 1, 1}
# After 2 days, cells[] = {0, 1, 1, 1}

def activeInactive(arr,k):
	arr.append(0)
	arr.insert(0,0)
	n = len(arr)
	l =[]

	while k>0:
		for i in range(1,n-1)
