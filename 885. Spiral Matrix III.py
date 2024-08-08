''' 
Question -
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.
You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.
Return an array of coordinates representing the positions of the grid in the order you visited them.
'''

'''
Difficulty - Medium
'''


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        step = 1
        ans = []
        i = rStart
        j = cStart
        while len(ans) < rows*cols:
            # right
            for x in range(step):
                if (0 <= j < cols and 0 <= i < rows):
                    ans.append([i, j])
                j += 1

            # down
            for x in range(step):
                if (0 <= j < cols and 0 <= i < rows):
                    ans.append([i, j])
                i += 1
            step += 1

            # left
            for x in range(step):
                if (0 <= j < cols and 0 <= i < rows):
                    ans.append([i, j])
                j -= 1
            
            # up
            for x in range(step):
                if (0 <= j < cols and 0 <= i < rows):
                    ans.append([i,j])
                i -= 1
            step += 1
        
        return ans


'''
Time Complexity - O(rows * cols)
'''
