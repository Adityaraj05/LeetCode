class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: 
            return 0
        # if a number is completly divisible by 9 then it's sum must be equal to 9 . ex. 18 => 1+8 = 9 % 9 ==0 
        result  =  num % 9
        if result == 0: 
            return 9
        else: 
            return result
        
