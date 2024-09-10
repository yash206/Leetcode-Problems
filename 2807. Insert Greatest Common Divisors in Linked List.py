''' 
Question -
Given the head of a linked list head, in which each node contains an integer value.
Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
Return the linked list after insertion.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
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
    def gcd(self, a, b):
        while b:
            a, b = b, a % b  
        return a 

    def insertGreatestCommonDivisors(self, head):
        ans = ListNode(0) 
        cur = ans 

        while head.next:
            gcd_val = self.gcd(head.val, head.next.val) 
            
            cur.next = ListNode(head.val) 
            cur.next.next = ListNode(gcd_val)  
            
            head = head.next  
            cur = cur.next.next  

        cur.next = ListNode(head.val)
        return ans.next



'''
Time Complexity - O(n*log(m))
'''
