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
def parts(string):
    result =[]
    
    while string:
        if string[0]==string[-1]:
            result.append(len(string))
            return result
        
        
        n = string.rfind(string[0])
        temp = string[:n+1]
        string = string[n+1:]
        setOfTemp = set(temp)
        
        
        if not any(i in string for i in setOfTemp):
            result.append(len(temp))
            
        else:    
            N = 0
            for i in setOfTemp:
                j = string.rfind(i)
                if j > N:
                    N = j
            toadd=string[:N+1]
            
            string = string[N+1:]
            result.append(len(temp+toadd))
    return result
print(parts("abbvvhyvxyvva"))
print(parts("ababcbacadefegdehijhklij"))
print(parts('because'))


