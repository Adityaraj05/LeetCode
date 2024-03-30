class Solution:
    def findComplement(self, num: int) -> int:
        
        sum = 1
        while num > sum:
            sum = sum * 2+1
        return sum - num
