class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        currentCost = 0
        left = 0
        result = 0
        for right in range(len(s)):
            currentCost += abs(ord(s[right])-ord(t[right]))

            while currentCost > maxCost:
                # using the concept of sliding window 
                currentCost -= abs(ord(s[left])-ord(t[left]))
                left += 1
                # right - left + 1 -> it will calculate the max lenght of string
            result = max(result, right-left +1)
        return result 
        
