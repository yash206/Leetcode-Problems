''' 
Question -
Given a string s, return the maximum number of unique substrings that the given string can be split into.
You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
A substring is a contiguous sequence of characters within a string.
'''

'''
Difficulty - Medium
'''


class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        def dfs(start, seen):
            if start == len(s):
                return 0

            max_splits = 0
            for i in range(start + 1, len(s) + 1):
                substring = s[start:i]

                if substring not in seen:
                    seen.add(substring)
                    max_splits = max(max_splits, 1 + dfs(i, seen))
                    seen.remove(substring)  # Backtrack

            return max_splits

        return dfs(0, set())


'''
Time Complexity - O(2ⁿ)
'''
