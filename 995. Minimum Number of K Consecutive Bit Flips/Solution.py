
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flips = 0
        flipCountPastFori = 0
        isFlipped = [0] * n  # Tracking the flip points
        
        for i in range(n):
            if i >= k and isFlipped[i - k]:
                flipCountPastFori -= 1

            if flipCountPastFori % 2 == nums[i]:  # Need to flip at index i
                if i + k > n:
                    return -1
                flipCountPastFori += 1
                flips += 1
                isFlipped[i] = 1  # Mark this index as the starting point of a flip

        return flips
