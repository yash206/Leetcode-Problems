''' 
Question -
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.
Return true if you can make arr equal to target or false otherwise.
'''

'''
Difficulty - Easy
'''


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_freq = {}
        for i in target:
            if (i in target_freq):
                target_freq[i]+=1
            else:
                target_freq[i]=1

        arr_freq = {}
        for i in arr:
            if (i in arr_freq):
                arr_freq[i]+=1
            else:
                arr_freq[i]=1
        for key, value in target_freq.items():
            if key not in arr_freq:
                return False
            if arr_freq[key] != value:
                return False
        return True


'''
Time Complexity - O(n)
'''
