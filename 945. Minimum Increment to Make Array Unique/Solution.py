class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        left = 0
        right = 1
        while right < len(nums):
            if nums[right] <= nums[left]:
                increment_needed = nums[left] - nums[right] + 1
                nums[right] += increment_needed
                count +=increment_needed
            else:
                left +=1
                right+=1
        return count
                
