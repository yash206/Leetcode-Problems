''' 
Question -
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
Return an array of the k parts.
'''

'''
Difficulty - Medium
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [None]*k

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        split_n = n//k
        rem = n%k

        curr = head
        for i in range(k):
            ans[i] = curr
            curr_n = split_n + (1 if rem>0 else 0)
            rem -= 1
            
            for _ in range(curr_n-1):
                if curr:
                    curr = curr.next
            
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
        return ans


'''
Time Complexity - O(n)
'''
