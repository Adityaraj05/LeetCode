class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # calculates the number of rows in the grid by taking the length of the grid list.
        n_row = len(grid)
        # calculates the number of columns in the grid by taking the length of the first row in the grid. 
        n_col = len(grid[0])

        result = 0
        # It will explore the grid recursively to find the maximum amount of gold that can be collected starting from the cell at (row, col).
        def dfs(row, col):
            # statement checks if the current cell (row, col) is out of bounds of the grid or if it contains zero gold. If any of these conditions are met, it returns 0 indicating that no gold can be collected from this cell.
            if row<0 or col < 0 or row >= n_row or col >= n_col or grid[row][col] == 0:
                return 0
            #  stores the amount of gold in the current cell (row, col) in a temporary variable temp.
            temp = grid[row][col]
            #  sets the amount of gold in the current cell to 0, indicating that it has been visited and the gold has been collected from it.
            grid[row][col] = 0
            # ecursively calls the dfs function for the neighboring cells (up, down, left, and right) of the current cell (row, col), and calculates the maximum amount of gold that can be collected from these neighboring cells.
            temp_max = max(dfs (row+1, col), dfs(row-1, col), dfs(row, col-1), dfs(row, col+1))
            # restores the original amount of gold in the current cell (row, col) before returning from the function. This is necessary for backtracking, ensuring that the grid is reverted to its original state after exploring a path.
            grid[row][col]= temp
            # returns the total amount of gold collected from the current cell (row, col) plus the maximum amount of gold collected from its neighboring cells.
            return temp + temp_max

        for row in range(n_row):
            for col in range(n_col):
                # conditional statement checks if the current cell (row, col) contains gold. If it does, it means that this cell hasn't been visited yet, and we initiate a DFS from this cell to explore and collect gold.
                if grid[row][col] != 0:
                    # updates the result variable to store the maximum amount of gold collected so far, by taking the maximum between the current value of result and the amount of gold collected starting from the cell (row, col).
                    result = max(result, dfs(row, col))
        return result
