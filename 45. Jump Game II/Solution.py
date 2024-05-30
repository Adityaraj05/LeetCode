class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        farthest = 0
        current = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if current == i:
                current = farthest
                jump += 1

        return jump
