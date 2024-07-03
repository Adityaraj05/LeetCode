class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # If the list has 4 or fewer elements, the function immediately returns 0 because no significant changes are needed..
        if len(nums) <= 4: return 0
        # sorts the list nums in non-decreasing order.
        nums.sort()   #[0,1,5,10,14]
        result = float("inf")
        for left in range(4):
            #  calculates the index of the right element in the subarray being considered. The subarray always has a length of 4 elements, so right is calculated to ensure this length is maintained.
            right = len(nums)-4+left
            result = min(result, nums[right]-nums[left])
        return result 
