class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        # This line initializes the variable duplicate to 1. This variable will be used to keep track of the length of the resulting list with duplicate elements removed. We start at 1 because we're assuming the first element of the list is unique.
        duplicate = 1
        for i in range(1, n):
            # This line checks if the current element nums[i] is different from the previous unique element nums[count-1]. If it is different, it means we've encountered a new unique element.
            if nums[i] != nums[duplicate-1]:
                # If the current element is different from the previous unique element, we assign the current element to the position count in the list nums (which corresponds to the next position for a unique element). Then, we increment the count variable by 1 to indicate that we've found another unique element.
                nums[duplicate] = nums[i]
                duplicate+=1
        return duplicate

  
