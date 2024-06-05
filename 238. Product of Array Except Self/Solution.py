class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # initialize the result array with the same length as nums, filled with 1's. So initially, result = [1, 1, 1, 1].
        result = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
            # result [1,1,2,6]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=postfix
            postfix *= nums[i]
        return result



        
