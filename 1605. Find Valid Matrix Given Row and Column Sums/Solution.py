class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        r = len(rowSum)
        c= len(colSum)

        my_list = [[0]*c for _ in range(r)]

        row, col = 0,0 # row and col
        while(row < r and col < c):
            my_list[row][col] = min(rowSum[row], colSum[col])
            rowSum[row] -= my_list[row][col]
            colSum[col] -= my_list[row][col]

            if rowSum[row] == 0:
                row += 1
            if colSum[col] == 0:
                col +=1
        return my_list


        
