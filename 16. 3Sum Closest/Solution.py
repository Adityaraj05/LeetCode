class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # taking a result variable which is value is infinity initially
        result = float('inf')
         # we are sorting the nums
        nums.sort()
        n = len(nums)

        for i in range(n):
            # taking two pointer left start form i +1 and right start from end
            left = i + 1
            right = n - 1
            # traversing with the help of two pointer
            while left < right:
                # calcualting the treesum
                ThreeSum = nums[i] + nums[left] + nums[right]
                 # if threesum is equal to target then simply return the target 
                if ThreeSum == target:
                    return target
                # now checking if abs(threesum - target) is less than abs(result-target) that means threesum value is much closer to the target therefore we will update the result 
                if abs(ThreeSum - target) < abs(result - target):
                    # now our result willbe updated
                    result = ThreeSum 
                    # if thressum is less than the target that mean we need higher value that's why we need increase left pointer by 1
                elif ThreeSum  < target:
                    left += 1
                else:
                      # if thressum is greater than the target that mean we need lesser value that's why we need decrease right pointer by 1
                    right -=1
        return result



        
