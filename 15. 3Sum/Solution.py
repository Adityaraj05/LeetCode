class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # sort the nums
        nums.sort() #[-4,-1,-1,0,1,2,]
        for i, a in enumerate(nums):  # it will traverese through index --> value
            # we are checking if i >0 and val is same the previous the continue not need to do anythinh 
            if i > 0 and a == nums[i-1]:
                continue
            # making the two pointer one is left pointer and another one is right pointer 
            left, right = i+1, len(nums)-1
            # traverseing through while loop 
            while left < right:
                # calculating the sum
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    # decrese the right pointer by one 
                    right -=1
                elif threeSum < 0:
                     # increase the left pointer by one 
                     left +=1
                else:
                    # means equal to zero then add to the result
                    result.append([a,nums[left],nums[right]])
                    left +=1
                    # checking the left is equal to left +1 then skip the left val and also chcking left don't cross right
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
                       
                    
        return result


                        
                        

        
         
           
