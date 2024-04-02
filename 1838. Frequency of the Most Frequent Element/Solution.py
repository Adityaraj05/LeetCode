class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()

        left, right = 0, 0 
        # This line initializes two variables, result and total, both set to 0. result will store the length of the longest subarray that meets the condition, and total will store the sum of the elements within the current subarray.
        result, total = 0, 0 
        #This line starts a while loop that iterates as long as the right pointer is less than the length of the nums list. This loop essentially controls the sliding window's right endpoint.
        while right < len(nums):
            # This line adds the value at the current position right in the nums list to the total sum. It extends the current subarray by including the element at the right pointer.
            total +=nums[right]
            # : This line starts an inner while loop that runs as long as the condition holds true. The condition checks whether the product of the value at the right pointer and the length of the current subarray (right - left + 1) is greater than the sum of the current subarray (total) plus a given constant k. This condition checks if the current subarray satisfies the given condition.
            while nums[right] * (right-left+1) > total + k:
                #Inside the inner while loop, this line subtracts the value at the left pointer from the total sum. It effectively reduces the size of the current subarray by moving the left pointer to the right.
                total -= nums[left]
                left +=1
            result = max(result, right-left+1)
            right+=1
        return result
        
