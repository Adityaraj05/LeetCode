class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # storing the number in palindrome variable show that at last we can compare
        palindrome = x
        # negative number can't be a palindrome
        if x < 0:
            return False
        reverse = 0
        while x > 0:
            remainder = x % 10
            reverse = reverse *10 + remainder; # 1 2 1
            x = x // 10
        return palindrome == reverse
