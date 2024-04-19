class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # It first checks if the grid is empty. If it is, it returns 0 because there are no islands in an empty grid.
        if len(grid) == 0:
            return 0
        # It initializes a variable Island to count the number of islands found.
        Island = 0
        # It then iterates through each cell in the grid using two nested loops (for i in range(len(grid)) and for j in range(len(grid[0]))).
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # For each cell, if the value of the cell is '1' (indicating land), it calls the dfs function to explore that island and mark all its connected land cells. After exploring the island, it increments the Island count.
                if grid[i][j] == '1':
                    dfs(grid, i, j, len(grid), len(grid[0]))
                    Island += 1
        #  it returns the total count of islands (Island).        #    
        return Island
    
def dfs(grid, i, j, row, col):
    # It checks if the current cell is out of bounds (i.e., if i or j is less than 0 or greater than or equal to row or col, respectively) or if the cell value is not '1' (i.e., if it's water or already visited).
    
    if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] != '1':
        # If any of the above conditions are true, it simply returns, indicating that this cell should not be explored further.
        return
    # If the current cell is land ('1'), it marks it as visited by changing its value to 'visited'.
    grid[i][j] = 'visited'
    # it recursively calls the dfs function for its adjacent land cells (up, down, left, and right), continuing the exploration process until all connected land cells are visited.
    dfs(grid, i, j + 1, row, col) #right
    dfs(grid, i, j - 1, row, col) #left
    dfs(grid, i+1, j, row, col)   #down
    dfs(grid, i-1, j, row, col)  #up
        
