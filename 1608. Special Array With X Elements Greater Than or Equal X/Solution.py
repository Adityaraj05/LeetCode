class Solution:
    def specialArray(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        while left <= right:
            mid = (left + right) // 2
            counter = 0
            for num in nums:
                if num >= mid:
                    counter += 1
            if counter == mid:
                return mid
            elif mid < counter:
                left = mid + 1
            else:
                # mid > counter
                right = mid - 1
        return -1
