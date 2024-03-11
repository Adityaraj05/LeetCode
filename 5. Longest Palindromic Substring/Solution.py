class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        maxSubstring = 0
        for i in range(len(s)):
            # odd lenght of pallindrome.
            left, right = i , i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > maxSubstring:
                    result = s[left:right+1]
                    maxSubstring = right-left + 1
                left -=1
                right+=1
            # when the pallindrome having even lenght.
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right-left+1) > maxSubstring:
                    result = s[left:right+1]
                    maxSubstring = right-left + 1
                left -=1
                right+=1
        return result



        
