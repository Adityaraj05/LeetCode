class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
    
        for i in range(n):
            # Inside the loop, this line calculates the index where the current number should be stored in order to identify duplicates. Since the numbers in nums range from 1 to n, but Python lists are zero-indexed, we subtract 1 from the absolute value of the current number to get the correct index.
            idx = abs(nums[i]) - 1
            # This line checks if the number at the calculated index (idx) is negative. A negative value at this index indicates that we've seen this number before, hence it's a duplicate.
            if nums[idx] < 0:
                # If the number at the calculated index is negative, it means it's a duplicate, so we append its absolute value to the ans list.
                ans.append(abs(nums[i]))
            else:
                # If the number at the calculated index is not negative, it means we haven't seen it before. In this case, we mark the number at this index as negative. This serves as a marker indicating that we've encountered this number during the iteration.
                nums[idx] = -nums[idx]
    
        return ans
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
S:- O(N)
T:- O(N)

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(0, n-1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
                i +=1
        return ans
        
