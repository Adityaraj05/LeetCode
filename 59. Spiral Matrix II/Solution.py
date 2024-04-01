class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # This line creates a 2D list (matrix) filled with zeros, with dimensions n rows by n columns.
        matrix = [[0] *n for _ in range(n)]
        left, right = 0, n-1
        top, bottom = 0, n-1
        value =1
        while left <= right:
            # fill the every value in the top row first:
            for col in range(left, right+1):
                matrix[top][col] = value
                value +=1
            top +=1
            # fill every value in the right col 
            for row in range(top, bottom+1):
                matrix[row][right] = value
                value +=1
            right -=1
            # This loop iterates over each column index in the range from right to left, inclusive, in reverse order.
            for col in range(right, left-1, -1):
                matrix[bottom][col] = value
                value +=1
            bottom -=1
            # This loop iterates over each row index in the range from bottom to top, inclusive, in reverse order.
            for row in range(bottom, top-1, -1):

                matrix[row][left] = value
                value +=1
            left +=1
        return matrix


        
