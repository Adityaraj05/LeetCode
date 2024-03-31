class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        badi = -1  #  This variable is initialized to -1. It's used to keep track of the index in the array where the current value is either less than minK or greater than maxK. This index indicates the start of a subarray that we don't want to include because it violates the conditions.
        mini = -1  # The minimum value in the subarray at this particular index
        maxi = -1  # The maximum value in the subarray at this particular index
        ans = 0
        n = len(nums)
    
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                badi = i
            if nums[i] == minK:
                mini = i
            if nums[i] == maxK:
                maxi = i
            ans += max(0, min(mini, maxi) - badi )

        return ans
