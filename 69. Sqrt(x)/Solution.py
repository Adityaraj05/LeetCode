class Solution:
    def mySqrt(self, x: int) -> int:
        # we initialize two variables left and right to 0 and x respectively. These variables will be used to define the search range for the binary search algorithm.
        left, right =0, x
        result =0
        while left <= right:
            #  calculates the middle element of the current search range. It uses integer division // to avoid floating-point errors. This is a common technique in binary search algorithms.
            mid = left + ((right-left)//2)
            # If the square of the middle element mid is greater than the target value x, then we update the right pointer to mid - 1. This narrows down the search range to the left half.
            if mid**2 > x:
                right = mid -1
            elif mid **2 < x:
                # If the square of the middle element mid is less than the target value x, then we update the left pointer to mid + 1. Additionally, we update the result variable to store the current mid value. This is because we're looking for the largest integer whose square is less than or equal to x.
                left = mid +1
                result = mid
            else:
                # f the square of the middle element mid is exactly equal to the target value x, we've found the exact square root, so we return mid immediately.
                return mid
        return result 


# -----------------------------------------------------------------------
# Basic Approach
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        for i in range(x+1):
            if i*i == x: 
                return i
            elif i*i > x:
                return i-1 
        
