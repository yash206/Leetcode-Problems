''' 
Question -
Given a binary tree root and a linked list with head as the first node. 
Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.
In this context downward path means a path that starts at some node and goes downwards.
'''

'''
Difficulty - Easy
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, list_node, tree_node):
        if not list_node:
            return True
        if not tree_node or list_node.val != tree_node.val:
            return False
        return(
            self.helper(list_node.next, tree_node.left) or
            self.helper(list_node.next, tree_node.right)
        )
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if self.helper(head, root):
            return True
        if not root:
            return False
        return(
            self.isSubPath(head, root.left) or
            self.isSubPath(head, root.right)
        )


'''
Time Complexity - O(n*m)
'''
