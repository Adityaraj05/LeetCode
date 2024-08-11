class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        self.time = 1
        self.hasArticulationPoint = False
        self.totalLandCells = 0
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        
        discoveryTime = [[0] * cols for _ in range(rows)]
        lowestReachableTime = [[0] * cols for _ in range(rows)]
        
        def isValidCell(row: int, col: int) -> bool:
            return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1
        
        def dfs(row: int, col: int, parentRow: int, parentCol: int) -> None:
            nonlocal discoveryTime, lowestReachableTime
            discoveryTime[row][col] = self.time
            lowestReachableTime[row][col] = self.time
            self.time += 1
            self.totalLandCells += 1
            children = 0
            
            for dr, dc in DIRECTIONS:
                newRow, newCol = row + dr, col + dc
                if not isValidCell(newRow, newCol):
                    continue
                
                if discoveryTime[newRow][newCol] == 0:
                    children += 1
                    dfs(newRow, newCol, row, col)
                    lowestReachableTime[row][col] = min(lowestReachableTime[row][col], lowestReachableTime[newRow][newCol])
                    
                    if lowestReachableTime[newRow][newCol] >= discoveryTime[row][col] and parentRow != -1:
                        self.hasArticulationPoint = True
                elif (newRow, newCol) != (parentRow, parentCol) and discoveryTime[newRow][newCol] < discoveryTime[row][col]:
                    lowestReachableTime[row][col] = min(lowestReachableTime[row][col], discoveryTime[newRow][newCol])
            
            if parentRow == -1 and children > 1:
                self.hasArticulationPoint = True
        
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and discoveryTime[row][col] == 0:
                    islands += 1
                    if islands > 1:
                        return 0  # More than one island
                    dfs(row, col, -1, -1)
        
        if self.totalLandCells == 0:
            return 0  # No land
        if self.totalLandCells == 1:
            return 1  # Only one land cell
        if islands == 0:
            return 0  # No islands (should not happen if input is valid)
        return 1 if self.hasArticulationPoint else 2






