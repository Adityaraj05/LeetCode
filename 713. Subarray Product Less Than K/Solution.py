class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # This line initializes a variable named count and assigns it the initial value of 0. This variable will be used to store the final result of the calculation.
        count = 0
        left  = 0
        product = 1
        # This line initiates a loop that iterates over the indices of the nums list. The variable right will represent the right boundary of the sliding window.
        for right in range(len(nums)):
            # Within the loop, this line multiplies the current value of product by the value at the right index of the nums list. This updates the product to include the latest element in the sliding window.
            product *= nums[right]
            # This line initiates a while loop that continues as long as the left boundary is less than or equal to the right boundary, and the product of the elements within the sliding window is greater than or equal to k.
            while left <= right and product >= k:
                # Within the while loop, this block divides the product by the value at the left index of the nums list and increments the left boundary. This effectively moves the left boundary of the sliding window to the right, removing elements from consideration until the product falls below k.
                product = product // nums[left]
                left +=1
            # After exiting the while loop, this line calculates the number of subarrays that satisfy the condition (product < k) with the current right index as the right boundary. It adds this count to the result variable.
            count += (right - left +1)
        return count
        
