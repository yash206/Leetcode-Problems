''' 
Question -
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
Return the maximum number of points you can achieve.
abs(x) is defined as:
x for x >= 0.
-x for x < 0.
'''

'''
Difficulty - Medium
'''


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        row = points[0]

        for i in range(1, rows):
            next_row = points[i].copy()
            left, right = [0]*cols, [0]*cols

            left[0] = row[0]
            for j in range(1, cols):
                left[j] = max(row[j], left[j-1]-1)
            
            right[-1] = row[-1]
            for j in range(cols-2,-1,-1):
                right[j] = max(row[j], right[j+1]-1)
            
            for j in range(cols):
                next_row[j] += max(left[j], right[j])
            row = next_row
        return max(row)

'''
Time Complexity - O(m*n)
'''
