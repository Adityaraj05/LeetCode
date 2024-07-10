class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []  # Initialize an empty stack to keep track of the current folder depth
        
        for folder in logs:  
            if folder == "../": 
                if stack:  # Check if the stack is not empty (i.e., we are not in the main folder)
                    stack.pop()  # Pop from the stack to move up one level
            elif folder != "./":  # If the operation is not "./" (i.e., not staying in the same folder)
                stack.append('folder')  # Push the operation onto the stack to move down one level
        return len(stack)  # The size of the stack represents the number of steps to return to the main folder


