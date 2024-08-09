class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(r: int, c: int) -> bool:
            vals = [0] * 10
            for i in range(3):
                for j in range(3):
                    num = grid[r + i][c + j]
                    if num < 1 or num > 9 or vals[num]:
                        return False
                    vals[num] = 1
            return (grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15 and
                    grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15 and
                    grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15 and
                    grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 and
                    grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15 and
                    grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15 and
                    grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15 and
                    grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15)
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagicSquare(i, j):
                    count += 1
        return count
