''' 
Question -
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
Return the number of islands in grid2 that are considered sub-islands.
'''

'''
Difficulty - Medium
'''


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        if not grid1 or not grid1[0] or not grid2 or not grid2[0]:
            return 0

        ROWS, COLS = len(grid1), len(grid1[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        island_count = 0

        def dfs_explore(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid2[r][c] == 0:
                return True 
            
            # Mark cell as visited
            grid2[r][c] = 0

            # Disqualify as sub-island if cell is water in grid1
            if grid1[r][c] == 0:
                nonlocal is_sub_island 
                is_sub_island = False

            for dr, dc in DIRECTIONS:
                dfs_explore(r + dr, c + dc)
            
            return is_sub_island

        for row in range(ROWS):
            for col in range(COLS):
                if grid2[row][col] == 1:
                    is_sub_island = True 
                    if dfs_explore(row, col):
                        island_count += 1

        return island_count


'''
Time Complexity - O(n)
'''
