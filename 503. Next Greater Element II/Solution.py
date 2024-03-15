class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack =[]
        n = len(nums)
        res = [-1] * n
        # This line duplicates the input list nums by concatenating it with itself. This is done to handle the circular nature of the problem, where the list is considered circular, i.e., after the last element, the first element comes next.nums=[1,2,1,1,2,1]
        nums = nums*2
    # This line starts a loop iterating over indices from 0 to n*2 - 1. This loop iterates over the doubled list to cover the circular aspect.
        for i in range(0, n*2):
            # This line checks if the stack is not empty and if the current element nums[i] is greater than the element at the index stack[-1] (the top element of the stack). If it is, it enters the loop.
            while stack and nums[stack[-1]] < nums[i]:
                # This line pops the index from the stack and assigns the next greater element nums[i] to the corresponding position in the res list.
                index = stack.pop()
                res[index] = nums[i]
                # This line checks if the current index i is less than n. If it is, it means we're still iterating over the original list (before doubling). So, it appends the current index i to the stack.
            if i < n:
                stack.append(i) #[1,2,1]
        return res
        
