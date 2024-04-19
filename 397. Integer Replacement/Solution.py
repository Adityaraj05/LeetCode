class Solution:
    def integerReplacement(self, n: int) -> int:
        ans  = 0
        # This line starts a while loop that continues as long as the value of n is not equal to 1.
        while n != 1:
            # If the current value of n is even (divisible by 2), it is halved using floor division (//). This operation effectively divides n by 2.
            if n % 2 == 0:
                n //= 2
            # If the current value of n leaves a remainder of 1 when divided by 4, or if n is equal to 3, then 1 is subtracted from n.
            
            elif n % 4 == 1 or n == 3:
                n -=1
             # If none of the above conditions are met, meaning n is odd and not equal to 3, 1 is added to n.
            else:
                n +=1
            # Regardless of which condition was executed in the previous steps, ans is incremented by 1 in each iteration of the while loop. This variable likely represents the number of steps taken to reach 1 according to the rules defined in the code.
            ans += 1
        return ans
        
