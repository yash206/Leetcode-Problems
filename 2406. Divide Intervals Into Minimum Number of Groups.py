''' 
Question -
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].
You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.
Return the minimum number of groups you need to make.
Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.
'''

'''
Difficulty - Medium
'''


import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pq = []
        for start, end in intervals:
            if pq and pq[0] < start:
                heapq.heappop(pq)
            heapq.heappush(pq, end)
        return len(pq)


'''
Time Complexity - O(n*log(n))
'''
