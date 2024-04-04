
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        left = 0
        right = len(matrix) - 1
        
        while left < right:
            for i in range(right - left):
                top = left
                bottom = right
                
                #store the topleft 
                top_left = matrix[top][left + i]
                
                #move bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]
                
                #move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                
                #move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                
                #move top left to top right
                matrix[top + i][right] = top_left
                
            right -= 1
            left += 1
                
        return matrix
    
    #   T = O(N^2)
    #   S= O(1)
    
      
