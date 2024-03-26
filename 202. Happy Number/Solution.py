class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # This line initializes an empty set called visit which will be used to keep track of visited numbers.
        visit = set()
        # This line initiates a while loop that continues as long as the number n is not present in the visit set. This loop is crucial for checking if the number forms a cycle or eventually leads to the number 1.
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

    def sumOfSquares(self, n: int) -> int:
        ans = 0
        while n:
            digit = n % 10 
            digit = digit **2
            ans += digit
            n = n//10
        return ans
