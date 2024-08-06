'''
Question - 
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
'''

'''
Difficulty - Medium
'''


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        lst_i = [False]*n
        lst_j = [False]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    lst_i[i] = True
                    lst_j[j] = True
        for i in range(n):
            for j in range(m):
                if lst_i[i] or lst_j[j]:
                    matrix[i][j] = 0
        


'''
Time Complexity - O(n*m)
'''
