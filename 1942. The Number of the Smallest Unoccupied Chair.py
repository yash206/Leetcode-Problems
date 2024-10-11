''' 
Question -
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.
For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.
You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.
Return the chair number that the friend numbered targetFriend will sit on.
'''

'''
Difficulty - Medium
'''


import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        openChairs, timeHeap = [], []
        output, startTime = 0, 0
        
        # populate minHeap with all posible chairs open
        for i in range(len(times)):
            if i == targetFriend:
                startTime = times[i][0]
            heapq.heappush(openChairs, i)
        
        times.sort(key=lambda x : x[0]) # sort by arrival time
        
        for i, timeObj in enumerate(times):

            arrival, leaving = timeObj
            # if our new arrival time is greater than any previous leaving time, 
            # pop our timeHeap and push occupied chair # to openChairs
            while len(timeHeap) and arrival >= timeHeap[0][0]:
                oldTime, chair = heapq.heappop(timeHeap)
                heapq.heappush(openChairs, chair)
            
            if startTime == arrival:
                return heapq.heappop(openChairs) # return next open chair
            
            heapq.heappush(timeHeap, (leaving, heapq.heappop(openChairs)))
            
        return -1


'''
Time Complexity - O(n*log(n))
'''
