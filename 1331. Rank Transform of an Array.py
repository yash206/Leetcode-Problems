''' 
Question -
Given an array of integers arr, replace each element with its rank.
The rank represents how large the element is. The rank has the following rules:
Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
'''

'''
Difficulty - Easy
'''


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr)==0:
            return []
        sorted_unique = sorted(set(arr))
        rank_dict = {val: rank + 1 for rank, val in enumerate(sorted_unique)}
        return [rank_dict[num] for num in arr]


'''
Time Complexity - O(n*logn)
'''
