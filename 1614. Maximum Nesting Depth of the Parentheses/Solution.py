class Solution:
    def maxDepth(self, s: str) -> int:
        #  variable will be used to keep track of the maximum depth of nested parentheses encountered in the input string s
        depth = 0
        # used to keep track of the current count of open parentheses encountered while iterating through the input string s.
        currentCount = 0
        # This line starts a for loop that iterates through each character (char) in the input string s.
        for char in s:
            # if the current character (char) is an open parenthesis '('. If it is, it increments the currentCount variable by 1, indicating that an additional open parenthesis has been encountered.
            if char == "(":
                currentCount +=1
                # if the current character (char) is a closing parenthesis ')'. If it is, it decrements the currentCount variable by 1, indicating that a corresponding closing parenthesis has been found, thus reducing the current depth.
            elif char ==")":
                currentCount -=1
                # This line updates the depth variable to be the maximum value between its current value and the currentCount. This ensures that depth always holds the maximum depth of nested parentheses encountered so far.
            depth = max(depth, currentCount)
        return depth
        
