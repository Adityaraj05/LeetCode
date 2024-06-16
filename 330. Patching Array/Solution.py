class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0
        left = 0
        maxReach = 0
        # Start a while loop that continues as long as maxReach is less than n. The goal is to ensure that the range [1, n] can be covered by the sums formed using the numbers in nums and the patches.
        while maxReach < n:
            # Check if the left index is within the bounds of the nums array and if the current number in nums (i.e., nums[left]) is less than or equal to maxReach + 1. This condition checks if the current number can extend the maxReach without needing a patch.
            if left < len(nums) and nums[left] <= maxReach +1:
                # add the value of nums[left] to maxReach. This means that the number at the left index can extend the range of sums that can be formed.
                maxReach += nums[left]
                # Increment the left index to move to the next number in the nums array.
                left +=1
            else:
                #  add maxReach + 1 to maxReach. This effectively means adding a patch to cover the missing number in the range.
                maxReach +=  maxReach +1
                # Increment the patch counter because a new number (patch) has been added to cover the gap.
                patch +=1
        return patch 


        
