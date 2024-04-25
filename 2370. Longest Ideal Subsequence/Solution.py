class Solution:
    def longestIdealString(self, s: str, k: int) -> int:


        l = [0] * 128
        for c in s:
            i = ord(c)
            l[i] = max(l[i - k : i + k + 1]) + 1
        return max(l)
        
