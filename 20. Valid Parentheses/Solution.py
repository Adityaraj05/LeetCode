class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # This line initializes a dictionary called HashMap which maps each closing bracket to its corresponding opening bracket. For example, ")" maps to "(", "]" maps to "[", and "}" maps to "{".
        HashMap = { ")":"(","]":"[","}":"{" }
        # This line starts a loop that iterates over each character brackets in the input string s.
        for brackets in s:
            # This line checks if the current character brackets is a closing bracket by looking it up in the HashMap dictionary.
            if brackets in HashMap:
                # This line checks if the stack is not empty (stack) and if the top element of the stack (stack[-1]) matches the corresponding opening bracket for the current closing bracket (HashMap[brackets]). If it matches, it means that the closing bracket has a corresponding opening bracket in the stack, and it can be popped.
                if stack and stack[-1] == HashMap[brackets]:
                    stack.pop()
                else:
                    # If the conditions in the if statement are not met, it means that the closing bracket does not have a corresponding opening bracket in the stack, so the function immediately returns False, indicating that the string contains invalid brackets.
                    return False
            else:
                # If the current character brackets is not a closing bracket (i.e., it's an opening bracket), this line appends it to the stack, indicating that an opening bracket has been encountered.
                stack.append(brackets)
        return True if not stack else False

        
