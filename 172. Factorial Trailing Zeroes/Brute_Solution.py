class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        fact = 1
        for i in range(2, n+1):
            fact *= i
        count = 0
        # let say we are calculating the factorial (n=5) which will be 120 therefore we are converting the integer inot the string "120" and after reverse the string "021"
        s = str(fact)[::-1]
        # now we are traversing the trailing zeros in s
        for i in s:
            if (i=='0'):
                count +=1
            else:
                break
        return count


