''' 
Question -
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
'''

'''
Difficulty - Hard
'''


class Solution:
    def getReqNum(self, a, b, n):
        gap = 0
        while a <= n:
            gap += min(n + 1, b) - a
            a *= 10
            b *= 10
        return gap

    def findKthNumber(self, n: int, k: int) -> int:
        num = 1
        i = 1
        while i < k:
            req = self.getReqNum(num, num + 1, n)
            if i + req <= k:
                i += req
                num += 1
            else:
                i += 1
                num *= 10
        return num


'''
Time Complexity - O(log n)
'''
