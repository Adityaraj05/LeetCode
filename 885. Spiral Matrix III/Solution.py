class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        num_steps=1
        total_cells=rows*cols
        result=[]
        r,c=rStart,cStart
        d=0

        while len(result)<total_cells:
            for _ in range(2):
                for _ in range(num_steps):
                    if 0<=r<rows and 0<=c<cols:
                        result.append([r,c])
                    if len(result)==total_cells:
                        return result
                    r+=directions[d][0]
                    c+=directions[d][1]
                d=(d+1)%4
            num_steps+=1

        return result
