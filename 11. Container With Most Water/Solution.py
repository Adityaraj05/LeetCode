class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
         # Initialization of two pointers i and j
        left = 0
        right = len(height) - 1
        # Initial water store will be 0
        water = 0
        
        # Now we will use a while loop
        while left < right:
            # Calculate the width
            width = right - left
            # Calculate the height and return min height value
            ht = min(height[left], height[right])
            # Return the maximum water capacity
            water = max(water, width * ht)
            
            # Now check which one height is less, move that pointer
            # Note: at a point where both pointer values become the same, move any one according to your choice
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return water
