class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # maximun element in the nums will be 3 and max count is equal to zero initially
        maximum_element , max_count = max(nums), 0
        left = 0
        result = 0
        for right in range(len(nums)):
            # If the element at the current index right is equal to maximum_element, increment max_count by 1.
            if nums[right] == maximum_element:
                max_count +=1
                # This while loop slides the window to the right until the condition is met.It checks if max_count exceeds k, or if the count is equal to k but the leftmost element is not equal to maximum_element.If the leftmost element is equal to maximum_element, decrement max_count by 1.Move the left pointer (left) one step to the right.
            while max_count > k or (left <= right and max_count == k and nums[left] != maximum_element):
                # If max_count equals k, it means the current window has k occurrences of the maximum element.Increment result by left + 1, which represents the number of subarrays ending at the current position right and having k occurrences of the maximum element.
                if nums[left] == maximum_element:
                    max_count -=1
                left +=1
            if max_count ==k:
                result += left + 1
        return result

        
