''' 
Question -
You are given m arrays, where each array is sorted in ascending order.
You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.
Return the maximum distance.
'''

'''
Difficulty - Medium
'''


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            max_distance = max(max_distance, abs(arrays[i][-1] - min_val), abs(arrays[i][0] - max_val))
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return max_distance


'''
Time Complexity - O(n)
'''
