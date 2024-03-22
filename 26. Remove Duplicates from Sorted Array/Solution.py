class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        # This line initializes a variable left to 1. The variable left will be used to keep track of the position where the next unique element should be placed in the modified list.
        left = 1
        # This line initiates a loop that iterates through the indices of the input list nums, starting from 1 (as the first element is considered already unique) up to the length of the list.
        for right in range(1,len(nums)):
            # This line checks if the current element (nums[right]) is different from the previous element (nums[right-1]). If they are different, it means the current element is unique.
            if nums[right] != nums[right-1]:
                # This line assigns the current unique element (nums[right]) to the position indicated by left in the list nums. Since left initially starts at 1, it means the first unique element will be placed at index 1 of the list.
                nums[left] = nums[right]
                # This line increments the left pointer by 1, indicating that the next unique element should be placed at the next position in the list.
                left +=1
        return left

   
  
