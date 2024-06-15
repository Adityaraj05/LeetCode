class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
    
        while left < right:
            # Move left pointer to the right until it points to an alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer to the left until it points to an alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers towards the center
            left += 1
            right -= 1
        
        return True

