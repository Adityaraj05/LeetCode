class Solution:
    def makeGood(self, s: str) -> str:
        def lower(c):
            # checks if the code of c is less than the code of 'a'. This is true for uppercase letters (A-Z) because their codes are lower than those of lowercase letters (a-z).
            if ord(c) < ord('a'):  
                # If the condition in line 2 is true (uppercase letter), this line calculates the lowercase equivalent.ord('A') gets the ASCII code for uppercase 'A'.The expression ord('a') + ord(c) - ord('A') effectively maps the uppercase code to the corresponding lowercase code. For example, if c is 'B' (code 66), the result would be 98 (code for 'b').chr( ... ) converts the calculated code back to a character, resulting in the lowercase equivalent of c.
                return chr(ord('a') + ord(c) - ord('A'))  
            # If the above condition is false (not uppercase), this line simply returns the original character c unchanged. This handles cases where c is already lowercase, a number, symbol, or whitespace.
            return c
        
        stack = []
        i = 0
        while i < len(s):
            # stack is not empty (has at least one element)The top element (stack[-1]) of the stack is not equal to the current character (s[i]) in the stringAfter converting both characters to lowercase using lower(lower(...)) (to handle cases where the characters might differ only in case), they are equal (==).
            if stack and stack[-1] != s[i] and lower(stack[-1]) == lower(s[i]): 
                # it means we've found two consecutive characters that differ only in case, and the second one can be removed.
                stack.pop()
            # either case, the current character s[i] is added to the stack using stack.append(s[i])
            else:
                stack.append(s[i])
            i += 1
        # "".join(stack) joins the elements in the stack into a single string using an empty string as the separator.This final string is returned as the result of the func
        return "".join(stack)
    
