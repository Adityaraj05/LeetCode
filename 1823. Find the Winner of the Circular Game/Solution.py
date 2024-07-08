class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l =[]
        for num in range(1,n+1):
            l.append(num)
        result = 0
        while len(l) != 1:
            result = (result + k -1) % len(l)
            l.pop(result)
        return l[0]
        
