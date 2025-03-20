

class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, 1
        
        while left < n:
            if nums[left] != right:
                k -= 1
                if k == 0:
                    return right
            else:
                left += 1
            right += 1
        
        return right + k - 1
