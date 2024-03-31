class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # This line starts a loop that will iterate k times. The variable i will take values from 0 to k-1. This loop is going to repeat the subsequent code block k times.
        for i in range(k):
            # Within each iteration of the loop, this line finds the index of the minimum value in the list nums. min(nums) returns the smallest value in the list, and nums.index(min(nums)) finds the index of that smallest value in the list nums.
            index = nums.index(min(nums))
            # Once the index of the minimum value is found, this line negates (i.e., makes negative) the value at that index in the nums list. This is achieved by multiplying the value by -1.
            nums[index] = -nums[index]
        return sum(nums)


        
