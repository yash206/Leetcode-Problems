''' 
Question -
You are given an integer array nums of size n.
Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.
The bitwise AND of an array is the bitwise AND of all the numbers in it.
A subarray is a contiguous sequence of elements within an array.
'''

'''
Difficulty - Medium
'''


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxBitwiseAnd = max(nums)
        maxi = 1
        count = 0
        i = 0
        
        while i < len(nums):
            if nums[i] == maxBitwiseAnd:
                while i < len(nums) and nums[i] == maxBitwiseAnd:
                    count += 1
                    i += 1
                maxi = max(maxi, count)
                count = 0
            else:
                i += 1
        return maxi


'''
Time Complexity - O(n)
'''
