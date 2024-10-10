''' 
Question -
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.
'''

'''
Difficulty - Medium
'''


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        vp = [(nums[i], i) for i in range(n)]
        vp.sort()
        min_index = vp[0][1]
        for i in range(1, n):
            current_index = vp[i][1]
            ans = max(ans, current_index - min_index)
            min_index = min(min_index, current_index)

        return ans


'''
Time Complexity - O(n)
'''
