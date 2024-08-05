'''
Question - 
You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.
'''

'''
Difficulty - Medium
'''


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9+7
        ans = []
        for i in range(n):
            summ = 0
            for j in range(i,n):
                summ += nums[j]
                ans.append(summ % mod)
        ans.sort()
        return sum(ans[left-1:right]) % mod


'''
Time Complexity - O(nlogn) + O(n²)
'''
