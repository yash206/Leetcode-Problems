'''
Question - 
A distinct string is a string that is present only once in an array.
Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".
Note that the strings are considered in the order in which they appear in the array.
'''

'''
Difficulty - Easy
'''


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        lst =[]
        for key, value in freq.items():
            if value == 1:
                lst.append(key)
        if len(lst) < k:
            return ""
        return lst[k-1]


'''
Time Complexity - O(n)
'''
