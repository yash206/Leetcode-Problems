''' 
Question -
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value 
'''

'''
Difficulty - Easy
'''


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        return [element for child in root.children for element in self.postorder(child)]+[root.val] if root else []


'''
Time Complexity - O(n)
'''
