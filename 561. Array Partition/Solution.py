class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        nums.sort()
        # This line starts a loop that iterates over the indices of nums from 1 to n-1 (exclusive), with a step size of 2. This ensures that we're considering every alternate pair of numbers.
        for i in range(1, n, 2):
            # This line calculates the minimum of the current pair of numbers (nums[i-1] and nums[i]) and adds it to the total_sum. We're adding the minimum of each pair to total_sum to maximize the overall sum of minimums.
            total_sum += min(nums[i-1], nums[i])
        return total_sum



        
