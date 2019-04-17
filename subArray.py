#Given an integer array nums, find the contiguous subarray (containing at least one number) 
#which has the largest sum and return its sum. Example: Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6 Explanation: [4,-1,2,1] has the largest sum = 6. *

n= len(arr)
def subarraySum(arr):
    for i in range(1,n):
        if arr[i-1]>0:
            arr[i]+=arr[i-1]
    return(max(arr))
 
