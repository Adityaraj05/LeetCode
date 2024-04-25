class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # ascii value of a --> 97 to a --> 128 that's why we have taken list of length 128 which is initaillly 0 value at every index l = [0, 0, 0, ..., 0]
        l = [0] * 128
        for c in s:
            i = ord(c)
            # This line calculates the length of the longest ideal string ending at the current character. It does this by taking the maximum value of the sublist l[i - k : i + k + 1] and adding 1 to it. This sublist represents the range of ASCII values within k characters before and after the current character. The length of the longest ideal string ending at the current character is stored at index i in the list l.
            l[i] = max(l[i - k : i + k + 1]) + 1
        return max(l)
        
