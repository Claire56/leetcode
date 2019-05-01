# Given two integers n and k, return all possible 
# combinations of k numbers out of 1 ... n.

# Example:

# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = combinations(list(range(1,n+1)),k)
        result =[]
        for i in res:
            result.append(i)
        return result
        