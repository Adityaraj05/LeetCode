class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        # This line starts a loop that iterates through each character char in the string num.
        for char in num:
            #  It continues as long as both k is greater than 0 and stack is not empty and the last element of stack (the top element of the stack) is greater than the current character char. This loop is designed to remove elements from the stack until either k becomes zero or the condition stack[-1] > char is not met.
            while k >0 and stack and stack[-1] > char:
                # This line decrements the value of k by 1 in each iteration of the while loop.
                k -= 1
                # This line removes the last element (top element) from the stack.
                stack.pop()
                # This line appends the current character char to the stack.
            stack.append(char)

        # if the numebr is in ascending order. This line slices the stack list. It keeps the elements from the beginning up to the index len(stack) - k, effectively removing the last k elements from the stack. This step ensures that the resulting stack contains at most len(num) - k elements.
        stack = stack[:len(stack)-k]
        # This line joins the elements of the stack list into a single string, with no separator between the elements and lstrip('0') removes leading "0" characters from the string string
        result ="".join(stack).lstrip('0')
        return result if result else "0"
        
