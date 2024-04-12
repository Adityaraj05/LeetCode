class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        while low<=high:
            if low==high:
                if nums[low]==target:
                    return low
                return -1
            mid=low + int(((target-nums[low]) * (high-low))/(nums[high]-nums[low]))
            if target==nums[mid]:
                return mid
            if target < nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return -1
