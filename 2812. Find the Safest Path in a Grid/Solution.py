class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = collections.deque()
        new_grid = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i,j,0])
                    visited.add((i,j))
        ans = 0
        # if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        #     return 0
        
        while len(queue)>0:
            i,j,dist = queue.popleft()
            new_grid[i][j] = dist
            
            if i+1 < n and (i+1,j) not in visited and grid[i+1][j] == 0:
                visited.add((i+1,j))
                queue.append([i+1,j,dist+1])
            
            if i-1 >= 0 and (i-1,j) not in visited and grid[i-1][j] == 0:
                visited.add((i-1,j))
                queue.append([i-1,j,dist+1])
            
            if j-1 >= 0 and (i,j-1) not in visited and grid[i][j-1] == 0:
                visited.add((i,j-1))
                queue.append([i,j-1,dist+1])
            
            if j+1 < n and (i,j+1) not in visited and grid[i][j+1] == 0:
                visited.add((i,j+1))
                queue.append([i,j+1,dist+1])
        
        
        def good(val):
            queue = collections.deque()
            queue.append([0,0])
            visited = set()
            visited.add((0,0))
            if new_grid[0][0] < val:
                return False
            while len(queue)>0:
                i,j = queue.popleft()
                if (i,j) == (n-1,n-1):
                    return True
                if i +1 < n and new_grid[i+1][j] >= val and (i+1,j) not in visited:
                    queue.append([i+1,j])
                    visited.add((i+1,j))
                if i -1 >= 0 and new_grid[i-1][j] >= val and (i-1,j) not in visited:
                    queue.append([i-1,j])
                    visited.add((i-1,j))
                
                if j +1 < n and new_grid[i][j+1] >= val and (i,j+1) not in visited:
                    queue.append([i,j+1])
                    visited.add((i,j+1))
                
                if j - 1 >= 0 and new_grid[i][j-1] >= val and (i,j-1) not in visited:
                    queue.append([i,j-1])
                    visited.add((i,j-1))
            
            return False
        
        l,h,ans = 0,10**3,-1
        while l <= h:
            mid = (l+h)//2 
            if good(mid):
                ans = mid
                l = mid + 1
            else:
                h = mid -1
        
        return ans
        
        
            
      
    
    
            
            
        
        
        
