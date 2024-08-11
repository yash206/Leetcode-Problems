'''
Question - 
You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.
The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
In one day, we are allowed to change any single land cell (1) into a water cell (0).
Return the minimum number of days to disconnect the grid.
'''

'''
Difficulty - Hard
'''


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def numberOfIslands():
            matrix = copy.deepcopy(grid)
            def dfs(matrix, i, j):
                if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != 1:
                    return 
                matrix[i][j] = 0
                dfs(matrix, i+1, j)
                dfs(matrix, i-1, j)
                dfs(matrix, i, j+1)
                dfs(matrix, i, j-1)
            count = 0
            if not matrix:
                return 0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 1:
                        dfs(matrix, i, j)
                        count += 1
                        
            return count
        c = numberOfIslands()
        if c == 0 or c > 1:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    c = numberOfIslands()
                    grid[i][j] = 1
                    if c == 0 or c > 1:
                        return 1
        return 2


'''
Time Complexity - O(m * n)
'''
