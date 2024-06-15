class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_lower = s.lower()
        #  Find all alphanumeric characters using a regular expression."".join(...): Join the list of alphanumeric characters into a single string without spaces or special characters.
        t = "".join(re.findall(r'[a-z0-9]',str_lower))
        left, right =0, len(t)-1
        while left <= right:
            if t[left] != t[right]:
                return False
            left +=1
            right -=1
        return True
        

