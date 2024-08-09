'''
Question - 
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
'''


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def magic(r, c) :
            visit = set()
            #1-9, duplicates
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if grid[i][j] in visit or not(1 <= grid[i][j] <= 9):
                        return 0
                    visit.add(grid[i][j])

            #rows
            for i in range(r, r+3):
                if sum(grid[i][c:c+3]) != 15:
                    return 0

            #cols
            for i in range(c, c+3) :
                if(grid[r][i] + grid[r+1][i] + grid[r+2][i] != 15) :
                    return 0
            
            #diagonals
            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
            grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15 ):
                return 0

            return 1

        res = 0
        for r in range(rows-2):
            for c in range(cols-2):
                res += magic(r, c)
        return res


'''
Time Complexity - O(rows * cols)
'''
