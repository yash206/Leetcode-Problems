''' 
Question -
There is a strange printer with the following two special properties:
The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.
'''

'''
Difficulty - Hard
'''


class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        def recur(i,j):
            if i==j:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            
            ans = 101
            for k in range(i,j):
                ans = min(ans, recur(i,k) + recur(k+1,j))
            
            if s[i]==s[j]:
                ans -= 1
            memo[(i,j)] = ans
            return ans
        return recur(0,len(s)-1)



'''
Time Complexity - O(n³)
'''
