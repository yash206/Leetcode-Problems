'''
Question - 
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.
'''

'''
Difficulty - Medium
'''


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        lst = [0]*(n+1)
        lst[1]=1
        t2, t3, t5 = 1, 1, 1
        for i in range(2,n+1):
            a = lst[t2] * 2
            b = lst[t3] * 3
            c = lst[t5] * 5
            lst[i] = min(a,b,c)
            if lst[i] == a:
                t2+=1
            if lst[i] == b:
                t3+=1
            if lst[i] == c:
                t5+=1
        print(lst)
        return lst[-1]


'''
Time Complexity - O(n)
'''
