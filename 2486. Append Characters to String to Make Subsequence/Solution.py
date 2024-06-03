class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        #This line initializes two variables, i and j, both set to 0. These variables will be used as indices to track the current positions within the strings s and t, respectively.
        i, j = 0 , 0
        # checks if i hasn't reached the end of string s and j < len(t):  checks if j hasn't reached the end of string t. The loop will continue iterating as long as we haven't reached the end of either string
        while (i <len(s) and j <len(t)):
            if s[i] == t[j]:
                # characters are equal, it means they are part of the potential common substring. So, we increment i by 1 to move to the next character in s.
                i +=1
                #  increment j by 1 to move to the next character in t and continue checking for matches.
                j +=1
            else:
                # ven though there's no match, we still increment i by 1. This is because we only care about finding the longest common substring that's a subsequence of s. Moving on from the current unmatched character in s allows us to potentially find a match for subsequent characters in s.
                i +=1
                # It calculates and returns the length of the longest common substring found. 
        return len(t)-j
