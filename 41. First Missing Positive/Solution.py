class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # This loop iterates over each index i from 0 to n-1 in the nums list. If the element at index i is negative, it sets it to 0.
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(n):
            # This line retrieves the absolute value of the element at index i in the nums list and assigns it to the variable val.
            val = abs(nums[i])
            # This line checks if the absolute value val falls within the range from 1 to n (inclusive).
            if 1 <= val <= n:
                # This line checks if the element at index val-1 (since list indices are zero-based) in the nums list is positive. If it is, it negates the value by multiplying it by -1.
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                # This line handles the case where the element at index val-1 is 0. It sets that element to -1 * (len(nums)+1).
                elif nums[val-1] == 0:
                    nums[val-1] = -1 * (len(nums)+1)
        # This line initiates a loop that iterates over each integer from 1 to n (inclusive).
        for i in range(1, n+1):
            # This line checks if the element at index i-1 is non-negative. If it is, it returns i. This is essentially finding the first missing positive integer.
            if nums[i-1] >= 0:
                return i
        # If no missing positive integer is found within the range from 1 to n, it returns n + 1.
        return n +1
           
                    
                        
        
