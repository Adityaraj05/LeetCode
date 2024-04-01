class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row > 0 and col > 0:
                    # This line checks if the element at the current position (row, col) is not equal to the element at the position diagonally above and to the left (row - 1, col - 1).
                    if matrix[row][col] != matrix[row - 1][col - 1]:
                        return False
        return True
        
