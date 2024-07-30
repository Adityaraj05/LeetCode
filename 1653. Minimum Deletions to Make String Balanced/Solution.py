class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0 
        stack = []
        for char in s:
            if stack and char == 'a' and stack[-1] =='b': #means top of the stack b hain and current char a aa gaya which is invalid therefore we have to pop.
                stack.pop()  # pop b from the stack,  we dont care about the string which will form after deleteion we just need a valid string that's it in this aabb string will obtain which is correct . 
                count += 1
            else:
                stack.append(char)
        return count

