class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        # in factorial if n is less than 5 then we never get a trailing zero : 4*3*2*1 = 24 therefore we simply return the result
        if n<5:
            return result
        # concept:- If we have to calculate the no.of trailing zeros in the given factorial then we know that multiple of 5 * with even no. is alway give trailing zeros .Therefore we will count the 5 in the given factorial and increase the count of trailing zero by one . Mathematical prove check out .
        number = 5
        while True:
            #  Checks if number (the current multiple of 5) is greater than n. If it is, it means there are no more multiples of 5 less than or equal to n, so the loop breaks and the function returns res.
            if number >n:
                return result
            # number is not greater than n then in that case we calculate the trailing zero by diving with 5 if n is divisible by 5 mean we get a trailing zero and add to result
            result += n//number
            #multiplying number by 5 in each iteration until number becomes greater than n. At that point, the loop breaks, and the function returns the accumulated sum in res.
            number *= 5
        
