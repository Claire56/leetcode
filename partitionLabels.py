# A string S of lowercase letters is given. We want to partition this string into as 
# many parts as possible so that each letter appears in at most one part, and return a 
# list of integers representing the size of these parts.

# # Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:

# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
s = "ababcbacadefegdehijhklij"
from collections import Counter

def parts(s):
	c= Counter(s)
	result =[]
	visited =[]
	lastIndex = 0

	for i, v in enumerate(s):
		if v not in visited:
			visited.append(v)
		c[v]-=1

    	if c[v]==0:
    		visited.remove(v)

    	if not visited:
    		result.append(i+1 -last)

    return result

print(parts("abbvvhyvxyvva"))
print(parts("ababcbacadefegdehijhklij"))
print(parts('because'))


