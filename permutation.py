# The set [1,2,3,...,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note:

# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.


from itertools import permutations as pm
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        perms = pm(list(range(1,n+1)))
        r= list(perms)
        kth = r[k-1]
        k=''
        for i in kth:
            k += str(i)
        
        
        
        return k