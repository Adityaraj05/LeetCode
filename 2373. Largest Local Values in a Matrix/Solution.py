class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid) # N = 4
        result = [[0] * (N-2) for _ in range(N-2)]  #result = [[0, 0],[0, 0]]
        # For each pair of indices (i, j) in result, it looks at the corresponding submatrix in grid. For example, when i=0 and j=0, it's looking at the submatrix:
        for i in range(N-2):
            for j in range(N-2):    #[9, 9, 8][5, 6, 2][8, 2, 6] and so on ...
            # Then, it iterates over the rows and columns of this submatrix:
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        # For each element in this submatrix, it updates the corresponding element in result with the maximum value found in the submatrix:
                        result[i][j] = max(result[i][j], grid[row][col])  #result = [[9],[]] and so on...
        return result

        
