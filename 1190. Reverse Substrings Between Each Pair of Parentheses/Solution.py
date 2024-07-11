class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop()) # it will revese LIFO order and store in temp list 
                stack.pop()  # Remove the '(' at last 

                stack.extend(temp) #Extend the stack with the reversed characters from the temporary list. 
            else:
                stack.append(char)
        
        return ''.join(stack)



        
