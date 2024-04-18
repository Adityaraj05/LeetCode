class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        length_row = len(grid)
        length_column = len(grid[0])

        perimeter = 0
        connections =0

        for i in range(0, length_row):
            for j in range(0, length_column):
                # checks if the current cell contains a 1, indicating that it's part of the land we are interested in calculating the perimeter for.
                if grid[i][j] == 1:
                    # If the current cell is part of the shape, you increment the perimeter variable by 4. This is because each cell contributes 4 units to the perimeter, assuming the shape is composed of squares.
                    perimeter +=4
                    # Top Checking

                    # This checks if there's a neighboring cell above the current cell (not in the first row) and if that neighboring cell is also part of the shape. If both conditions are met, it indicates a connection, and connections is incremented.
                    if i != 0 and grid[i-1][j] ==1:
                        connections +=1
                    # Left Checking


                    # Similarly, this checks if there's a neighboring cell to the left of the current cell (not in the first column) and if that neighboring cell is also part of the shape. If so, it indicates a connection, and connections is incremented.

                    if j != 0 and grid[i][j-1] == 1:
                        connections +=1
                    # Finally, you return the total perimeter of the shape minus twice the number of connections. Since each connection reduces the perimeter by 2 units (one unit on each side), subtracting twice the number of connections adjusts the perimeter accordingly.
        return perimeter - (connections * 2)

        
