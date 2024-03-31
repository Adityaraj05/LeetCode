class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total =0
        result = float("inf")
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                result = min(right-left+1,result)
                total -= nums[left]
                left +=1
                
        return 0 if result == float("inf") else result
        
