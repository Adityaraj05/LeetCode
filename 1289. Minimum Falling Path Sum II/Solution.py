class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        first_min, second_min = float('inf'), float('inf') # Initialize first and second minimums
        first_index, second_index = -1, -1 # Initialize indices for the first and second minimums

        for i in range(n): # Iterate through each row of the grid
            if i != 0: # For rows after the first one
                for j in range(n): # Update the grid values based on the previous row's minimums
                    if j != first_index:
                        grid[i][j] += first_min
                    else:
                        grid[i][j] += second_min

            first_min, second_min = float('inf'), float('inf') # Reset first and second minimums for the current row

            for j in range(n): # Iterate through each element of the current row
                # Update first and second minimums and their indices
                if grid[i][j] < first_min:
                    second_min = first_min
                    first_min = grid[i][j]
                    first_index = j
                elif grid[i][j] < second_min:
                    second_min = grid[i][j]
                    second_index = j

        return min(first_min, second_min) # Return the minimum of the first and second minimums
