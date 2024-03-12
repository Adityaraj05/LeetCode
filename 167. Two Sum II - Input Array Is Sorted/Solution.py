class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we are using two pointer 
        left, right = 0, len(numbers)-1
        # loop with traverse till the left cross right 
        while left < right:
            # here we are storing the sum of first element and last elemetn sum at first iteration
            currentSum = numbers[left] + numbers[right]
            # now we are comparing currentSum is greater then right pointer will decrease by 1 beacuse array is sorted so we need go to lesser value near to our target
            if currentSum > target:
                right-=1
                # if currentSum is lesser than target then left pointer will increase by 1 beacuse array is sorted so we need go to higher value near to our target 
            elif currentSum < target:
                left+=1
            else: 
                # if we got the target then return the index of left and right pointer by + 1 because that's it want the index starting form 1 
                if currentSum == target:
                    return [left+1, right+1]
                
     
