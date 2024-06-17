class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # checking the base case
        if not nums:
            return 0
        # Convert the input list nums to a set nums_set to allow for O(1) lookups.
        nums_set = set(nums)
        longest_Sequence = 0
        for num in nums_set: # (1,2,3,4,100,200)
            if num - 1 not in nums_set:  # Check if it is the start of a sequence (1-1 = 0 that's mean 1 is the starting number of sequence)
                current_num = num
                current_streak = 1
                
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1
                    
                longest_Sequence= max(longest_Sequence, current_streak)
        
        return longest_Sequence
