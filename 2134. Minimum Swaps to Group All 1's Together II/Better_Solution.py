class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Count the number of 1s in the original array , window size that we have to maintend
        TotalOnes = sum(nums)
        
        i, j = 0,  0
        currCount, maxCount = 0, 0
        
        while j < 2*n:
            # Increase count of 1s in the current window
            if nums[j%n] == 1:
                currCount += 1

            # If the window size exceeds the number of 1s, slide the window
            if j - i + 1 > TotalOnes:
                    currCount -= nums[i%n]
                    i += 1

            # Update maximum count of 1s found in any window of size countOnes
            maxCount = max(maxCount, currCount)
            j += 1

        # The minimum number of swaps needed is the difference between total number of 1s and the maximum count found
        return TotalOnes - maxCount
