class Solution:
    def tribonacci(self, n: int) -> int:
        # Handline the base case
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        # This line initializes a list named dp with n + 1 elements, all initialized to 0. This list will be used to store the tribonacci numbers.
        dp = [0] * (n +1)
        # These lines assign the initial values for the tribonacci sequence. dp[0], dp[1], and dp[2] are set to 0, 1, and 1 respectively. These are the base cases for the tribonacci sequence.
        dp[0], dp[1], dp[2] = 0, 1, 1
    
        # # These lines assign the initial values for the tribonacci sequence. dp[0], dp[1], and dp[2] are set to 0, 1, and 1 respectively. These are the base cases for the tribonacci sequence.
        for i in range(3, n+1):
            # This line calculates the tribonacci number for index i. It sums the three previous tribonacci numbers (at indices i-1, i-2, and i-3) and stores the result in dp[i].
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
        
