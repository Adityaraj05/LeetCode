class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Step 1: Ensure leftmost bit of every row is set to 1, It iterates over each row (i) in the grid. If the leftmost bit of the current row (grid[i][0]) is 0, it toggles each element in that row by subtracting the current value from 1.
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
        
        # Step 2: Toggle columns if needed ,  It iterates over each column (j) starting from the second column. For each column, it counts the number of 1s (ones) in that column. If the count is less than half of the total number of rows (m / 2), it toggles each element in that column.
        for j in range(1, n):
            ones = sum(grid[i][j] for i in range(m))
            if ones < m / 2:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]
        
        # Step 3: Calculate total score. It calculates the total score of the matrix. It iterates over each row in the grid, converts each row into a binary string, joins them together, and then converts the resulting binary string into an integer using int() with base 2. Finally, it adds this integer to the total_score.
        total_score = 0
        for row in grid:
            # ''.join(map(str, row)) converts each element of the row to a string and joins them together. So, ['0', '0', '1', '1'] becomes '0011'.int('0011', 2) converts the binary string '0011' to an integer, which is 3.
            total_score += int(''.join(map(str, row)), 2)
        
        return total_score
# =======================================================================================================================================================================================================================
# Approach:-


To solve this problem, you can follow these steps:

1). First, ensure that the leftmost bit of every row is set to 1. This guarantees the maximum possible score for each row.
2). Then, iterate through each column. If the number of 1's in the column is less than the number of 0's, toggle that column.
3). Finally, calculate the total score of the matrix.
