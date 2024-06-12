class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # we have use three pointer low, high and left_pointer. 
        low, left_pointer, high = 0, 0, len(nums) - 1

        while left_pointer <= high:
            if nums[left_pointer] == 0:
                nums[low], nums[left_pointer] = nums[left_pointer], nums[low]
                low += 1
                left_pointer += 1
            elif nums[left_pointer] == 1:
                left_pointer += 1
            else:
                nums[left_pointer], nums[high] = nums[high], nums[left_pointer]
                high -= 1

