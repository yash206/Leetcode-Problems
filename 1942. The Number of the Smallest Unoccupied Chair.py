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
    def smallestChair(self, times, targetFriend):
        events = []
        for i, (arrival, departure) in enumerate(times):
            events.append((arrival, 0, i))  # arrival event
            events.append((departure, 1, i))  # departure event
        
        events.sort()  # Sort by time
        available_chairs = []
        for i in range(len(times)):
            heapq.heappush(available_chairs, i)
        
        friend_to_chair = {}
        
        for time, event_type, friend_id in events:
            if event_type == 0:  # arrival
                chair = heapq.heappop(available_chairs)
                friend_to_chair[friend_id] = chair
                if friend_id == targetFriend:
                    return chair
            else:  # departure
                chair = friend_to_chair[friend_id]
                heapq.heappush(available_chairs, chair)


'''
Time Complexity - O(n*log(n))
'''
