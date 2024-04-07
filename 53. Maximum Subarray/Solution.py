class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # This line sets both curr_sum and max_sum to the first element of the nums list, assuming nums is a list of numbers.
        curr_sum = max_sum = nums[0]
        #  The loop starts from the second element of the list (nums[1]) because the curr_sum and max_sum variables are already initialized with the first element.
        for i in range(1, len(nums)):
            # This line calculates the current sum of the subarray ending at index i. It adds the value of the current element nums[i] to the previous current sum curr_sum and compares it with the current element nums[i] itself. It then assigns the maximum of these two values to curr_sum. 
            curr_sum = max(curr_sum + nums[i] , nums[i])
            # This line updates the max_sum variable to the maximum value between the current sum (curr_sum) and the previous maximum sum (max_sum). This ensures that max_sum always stores the maximum sum of any subarray seen so far in the iteration.
            max_sum = max(curr_sum, max_sum)

        return max_sum

    '''
        T = O(N)
        S = O(1)
    '''
