class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        stack, ans = [], 0
        for c in nums:
            # stack: Checks if the stack is not empty.stack[-1][0] < c: Checks if the element at the top of the stack (stack[-1]) is less than the current element (c) being processed in the loop.
            while stack and stack[-1][0] < c:
                # This line removes the element at the top of the stack (stack.pop()).This effectively removes elements from the stack that are smaller than the current element (c).Because if an element on the stack is smaller than the current element, it means the current element could be a potential NGE for that element that was previously encountered.
                stack.pop()
            # Checks if the stack is now empty, 
            if not stack  or stack[-1][0] > c:
                #  If the conditions in the if statement are met, this line appends a new pair [c, 0] to the stack, indicating that c has been encountered once.
                stack.append([c, 0])
            # This line increments the frequency count of the last element in the stack. This is because either the element is already in the stack and we're seeing it again, or it's a new element that we just appended.
            stack[-1][1] += 1
            # This line adds the frequency count of the last element in the stack to the result ans. This effectively accumulates the total frequency counts of all elements in the stack.
            ans += stack[-1][1]
        return ans
        
