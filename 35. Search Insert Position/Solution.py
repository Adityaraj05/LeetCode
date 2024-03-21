class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif  nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                # if left > right:: This line checks if the left pointer has surpassed the right pointer. If this condition is true, it means that the target value should be inserted at the position indicated by the left pointer.
            if left > right:
                
                return left
        
        
