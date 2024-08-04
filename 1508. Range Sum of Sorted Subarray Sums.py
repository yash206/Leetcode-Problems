'''
Question - 
You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.
Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.
'''


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarrays_sum = []
        start = 0
        for start in range(n):
            for end in range(start, n):
                temp = sum(nums[start:end+1])
                subarrays_sum.append(temp)

        subarrays_sum.sort()
        ans = sum(subarrays_sum[left-1:right])
        M = 10**9+7
        ans = ans%M

        return ans
