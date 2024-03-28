class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # defaultdict(int) means that if a key is not found in the dictionary, it will automatically create it with a default value of 0. This dictionary is going to be used to count the occurrences of elements in the nums list.
        count = defaultdict(int)
        # This line initializes a variable res to store the result, which will be the maximum length of a subarray satisfying the condition.
        res = 0
        # This line initializes a variable left which represents the left pointer of the sliding window. It will be used to keep track of the left boundary of the current subarray.
        left = 0
        for right in range(len(nums)):
            count[nums[right]] +=1
            # This is a while loop that runs as long as the count of the element at the right pointer exceeds the limit k. Inside the loop, it decreases the count of the element at the left pointer (moving the left pointer to the right) until the condition is met.
            while count[nums[right]] > k:
                count[nums[left]] -=1
                left +=1
            # This line calculates the length of the current subarray (from left to right) and updates res to the maximum of its current value and the length of the current subarray.
            res = max(res, right-left+1)
        return res
