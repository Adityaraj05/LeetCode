class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # This line initializes a stack with a single element -1. The stack will be used to keep track of the indices of opening parentheses.
        stack = [-1]
        # This line initializes a variable result to 0, which will store the length of the longest valid parentheses substring found so far.
        result = 0
        # This line starts a loop iterating over each index i in the range of the length of the input string s.
        for i in range(len(s)):
            # This block is executed if the character at index i in the string s is an opening parenthesis (. It appends the current index i to the stack, indicating the position of an opening parenthesis.
            if s[i] == "(":
                stack.append(i)
                # This block is executed if the character at index i in the string s is a closing parenthesis ).It pops an element from the stack, which represents the index of the corresponding opening parenthesis for the current closing parenthesis.If the stack becomes empty after popping (meaning there's no matching opening parenthesis found so far), it means the current closing parenthesis cannot be part of a valid substring, so we push the current index onto the stack to mark the beginning of a new substring.
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                    # If the stack is not empty, we calculate the length of the valid parentheses substring ending at the current index i by subtracting the index popped from the stack from the current index i. We then update result to hold the maximum of its current value and this calculated length.
                else:
                    result = max(result, i - stack[-1])
        return result
