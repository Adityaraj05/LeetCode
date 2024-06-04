class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = defaultdict(int)
        result = 0
        for char in s:
            count[char] +=1
            # Every time we get a matching pair we increment the result by 2.
            if count[char] % 2 == 0:
                result +=2
         # checking if any char comes odd times then at last we will add +1 to the result 
        for cnt in count.values():
            # if any char whose values is odd times then we will increment the result by 1 and break the loop
            if cnt % 2:
                result +=1
                break
        return result
            
        
