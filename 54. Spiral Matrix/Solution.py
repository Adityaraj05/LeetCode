class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        # right is legth of cols
        left, right =0 , len(matrix[0])
        # bottom is length of row
        top, bottom =0, len(matrix)
        while left<right and top < bottom:
            # get every col in the top row
            for col in range(left, right):
                result.append(matrix[top][col])
            top +=1
             # get every row in the right col
            for row in range(top, bottom):
                result.append(matrix[row][right-1])
            right -=1

            if not (left < right and top < bottom):
                break

            # get every col  in the bottom row in reverse order
            for col in range(right-1,left-1,-1):
                result.append(matrix[bottom-1][col])
            bottom -=1
            # get every  row in the left col.
            for row in range(bottom-1, top-1,-1):
                result.append(matrix[row][left])
            left+=1
        
        return result
