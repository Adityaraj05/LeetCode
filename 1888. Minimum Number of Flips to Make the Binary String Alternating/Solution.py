class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s+s
        alternate1, alternate2 = "",""
        for i in range(len(s)):
            # These lines generate two alternating sequences of '0's and '1's. In each iteration of the loop, it appends either '0' or '1' to alternate1 and alternate2 based on whether i is even or odd.
            alternate1 += "0" if i % 2 else "1"
            alternate2 += "1" if i % 2 else "0"

        result = len(s)
        difference1, difference2 = 0, 0
        left = 0
        for right in range(len(s)):
            # These lines iterate through the characters of s and calculate the differences between s and alternate1, and between s and alternate2.
            if s[right] != alternate1[right]:
                difference1 +=1
            if s[right] != alternate2[right]:
                difference2 +=1
            # This block of code is responsible for maintaining a sliding window of size n over s. It updates the differences as the window slides. If the window size exceeds n, it updates the differences by removing the element from the left of the window and updates the result variable with the minimum difference found so far.
            if (right-left +1) > n:
                if s[left] != alternate1[left]:
                    difference1 -=1
                if s[left] != alternate2[left]:
                    difference2 -=1
                left +=1
                if (right-left+1) == n:
                    result = min(result, difference1, difference2)

        return result
                
                
            
        
