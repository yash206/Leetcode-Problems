''' 
Question -
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.\
Return the minimum number of extra characters left over if you break up s optimally.
'''

'''
Difficulty - Medium
'''


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dict_set = set(dictionary)
        n = len(s)
        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(i):
                sub = s[j:i]
                if sub in dict_set:
                    dp[i] = min(dp[i], dp[j])
            dp[i] = min(dp[i], dp[i - 1] + 1)

        return dp[n]


'''
Time Complexity - O(n²)
'''
