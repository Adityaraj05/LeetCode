class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                res.append(i)
                break
        return res if res else [-1, -1]
  # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Better Approach:-


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]
