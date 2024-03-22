class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        # The Counter class is a subclass of dict and is used to count the occurrences of elements in an iterable (nums in this case). It creates a dictionary where keys are the elements of nums, and values are the counts of each element.
        count = Counter(nums)  #[1:2,2:2,3:1,4:1] key --> frequency or values
        for i in count.values():
            if i > 2:
                return False
        return True
        
        

            
