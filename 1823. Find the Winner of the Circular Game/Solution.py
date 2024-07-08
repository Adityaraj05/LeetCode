class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l =[]
        l = [i for i in range(1,n+1)]   
        result = 0
        while len(l) != 1:
            result = (result + k -1) % len(l)
            l.pop(result)
        return l[0]
        
