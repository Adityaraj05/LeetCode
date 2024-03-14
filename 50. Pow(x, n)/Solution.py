class Solution:
    def myPow(self, x: float, n: int) -> float:
    # Define a helper function for recursive computation
        def function (x , n):
         # If x is equal to zero, return 0 (0^n = 0)
            if x == 0:
                return 0
          # If n is equal to zero, return 1 (x^0 = 1)
            if n == 0:
                return 1
         # Perform recursive call to compute x^(n//2)
            res = function(x, n//2)
             # Square the result
            res = res * res
            # here we are checking the  n is ood or even if n is ood then we have to multiply one time extra if n is even simply return ex:-2^5 --> here n is odd --> 2 * 2^2 * 2^2  and if 2^4 --> 2^2 *2^2 or in other term  If n is odd, multiply result with x once more
            return x * res if n % 2 else res 
            # n can also be negative so we r handling that one also by taking abs value and at last we will check if n is greater than 0 then return the res else 1/ res
        res = function(x, abs(n))
        return res if n >=0 else 1/res
        
            
            
        
