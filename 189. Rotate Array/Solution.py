class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ensures that k is within the bounds of the array length. If k is greater than the length of the array, rotating by k is the same as rotating by k % len(nums) because rotating by the length of the array results in the same array.
        k = k % len(nums)

        left, right = 0, len(nums)-1
        # In this while loop the array is completely reversed. 
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left +1, right-1

        # This block reverses the first k elements of the reversed array. The reversal is again done by swapping elements from the start and end of the section and moving towards the center. After this step, the first k elements of the array are in their correct rotated positions.
        left, right = 0, k-1
        # In this loop we are rotating 0 to  k-1 element  
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left +1, right-1

        left, right = k, len(nums)-1
         # In this loop we are rotating k to length-1 element  
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left +1, right-1
        
