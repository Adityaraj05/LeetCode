class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Sort the array first
        nums.sort()
        
        # Define the binary search range
        low, high = 0, nums[-1] - nums[0]
        
        # Binary search to find the k-th smallest distance
        while low < high:
            mid = (low + high) // 2
            count = 0
            left = 0
            
            # Count pairs with distance <= mid
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            
            # Adjust the binary search range
            if count >= k:
                high = mid
            else:
                low = mid + 1
        
        return low
