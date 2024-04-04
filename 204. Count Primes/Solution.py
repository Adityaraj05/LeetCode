class Solution:
    def countPrimes(self, n: int) -> int:
        # This line checks if the input `n` is less than or equal to 2. If `n` is 2 or less, the function returns 0. 
        if n <=2:
            return 0
        # This line creates a list named dp of size n. The list is filled with True values for each element using list comprehension ([True] * n). The dp list will be used to store a boolean value for each number from 0 to n-1, indicating whether that number is a prime number (True) or not (False).
        dp = [True] * n
        # This line explicitly sets dp[0] to False. The number 0 is not considered a prime number, so this line marks it as non-prime in the dp list.
        dp[0] = False
        # Similar to line 4, this line sets dp[1] to False. The number 1 is also not considered prime, so it's marked as non-prime in the dp list.
        dp[1] = False
        # This line starts a for loop that iterates through a range of numbers from 2 (inclusive) to n (exclusive). The variable num will take on each value in this range during each iteration.
        for num in range(2, n):
            # Inside the loop, this line checks if the current value num in the dp list is still True. This means num hasn't been marked as non-prime yet and could potentially be prime.
            if dp[num]:
                # iThis line creates a nested loop that iterates through multiples of num starting from num * 2 and going up to n-1 with a step of num. The variable index will take on each of these values.The purpose of this loop is to mark all multiples of num as non-prime in the dp list. This is because any number that is a multiple of another number (except 1) cannot be prime.
                for index in range(num * 2, n, num):
                    # Inside the nested loop, this line sets the value of dp[index] to False. This marks all multiples of num (stored in the index variable) as non-prime in the dp list.
                    dp[index] = False
        # Once the outer loop finishes iterating through all numbers from 2 to n-1, this line calculates the sum of all the elements in the dp list using the sum() function.Since dp now holds True for prime numbers and False for non-prime numbers, summing the elements essentially counts the number of True values, which is the total number of prime numbers less than n.
        return sum(dp)

        
