class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        largest_k = -1
        while left < right:
            if nums[left] + nums[right] == 0:
                largest_k = max(largest_k, nums[right])
                left += 1
                right -= 1
            elif nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1
        return largest_k if largest_k != -1 else -1
