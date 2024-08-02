class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        # Create a temporary array to simulate the circular array
        temp = nums + nums  # Concatenate the array with itself
        
        # Count the number of 1s in the original array , window size that we have to maintend
        TotalOnes = sum(nums)
        
        i, j = 0,  0
        currCount, maxCount = 0, 0
        
        while j < len(temp):
            # Increase count of 1s in the current window
            if temp[j] == 1:
                currCount += 1

            # If the window size exceeds the number of 1s, slide the window
            if j - i + 1 > TotalOnes:
                if temp[i] == 1:
                    currCount -= 1
                i += 1

            # Update maximum count of 1s found in any window of size countOnes
            maxCount = max(maxCount, currCount)
            j += 1

        # The minimum number of swaps needed is the difference between total number of 1s and the maximum count found
        return TotalOnes - maxCount
