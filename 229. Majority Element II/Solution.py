class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # defaultdict is a special type of dictionary that provides a default value for keys that don't exist yet. In this case, the default value is set to int(), which is 0.This dictionary will be used to store the frequency of each value (number) in the input list nums.
        count = defaultdict(int)  # val --> freq
        for val in nums:
            count[val] +=1
            # This line checks if the number of unique elements (keys) in the count dictionary is less than or equal to 2.If it's true, the code inside the if block executes. Otherwise, it skips to the next line.
            if len(count) <= 2:
                continue
            # create a temporary dictionary new_count and iterate through count to decrease the frequency of elements that appear more than once.
            new_count = defaultdict(int)
            for val, freq in count.items():
                if freq > 1:
                    new_count[val] = freq -1
                count = new_count
            
        result = []

        threshold = len(nums) // 3  # Minimum frequency to be considered a majority element

        for val in count:
            if nums.count(val) > threshold:
                result.append(val)

        return result

        
