class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        left,right= 0, 1
        while left < len(nums):
            if right<len(nums) and nums[right] == nums[right-1]+1:
                right += 1
            else:
                # checking if right -1 == left mean [7,7] then in that case simply add -->"7" 
                if right - 1 == left:
                    result.append(str(nums[left]))
                else:
                    result.append(str(nums[left]) + "->" + str(nums[right-1]))
                left = right
                right += 1
        return result
