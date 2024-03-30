class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        else:
            num = 1 
            length = 1
            while num % k != 0:
                # increasing the ones
                num = 10*num+1
                # updating the lenght
                length +=1
            return length
        
