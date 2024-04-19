class Solution:
    def integerReplacement(self, n: int) -> int:
        ans  = 0
        # This line starts a while loop that continues as long as the value of n is not equal to 1.
        while n != 1:
            # If the current value of n is even (divisible by 2), it is halved using floor division (//). This operation effectively divides n by 2.
            if n % 2 == 0:
                n //= 2
            # If the current value of n leaves a remainder of 1 when divided by 4, or if n is equal to 3, then 1 is subtracted from n.
            # n % 4 == 1: This condition checks if n leaves a remainder of 1 when divided by 4. Why 4? This condition is used to identify a certain type of odd number that behaves differently. 
# If n % 4 == 1, it indicates that n is of the form 4k + 1, where k is an integer. Such numbers, when decremented by 1, become divisible by 4, hence the condition.
# or n == 3: This condition specifically handles the case when n is equal to 3. If n is 3, it's a special case where decrementing it by 1 is the only option because
# incrementing it by 1 would result in 4, which is not the best option according to the rules.
            elif n % 4 == 1 or n == 3:
                n -=1
             # If none of the above conditions are met, meaning n is odd and not equal to 3, 1 is added to n.
            else:
                n +=1
            # Regardless of which condition was executed in the previous steps, ans is incremented by 1 in each iteration of the while loop. This variable likely represents the number of steps taken to reach 1 according to the rules defined in the code.
            ans += 1
        return ans
        
