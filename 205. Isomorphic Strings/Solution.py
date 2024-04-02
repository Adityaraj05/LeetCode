class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # mapping character form s to t and vice versa
        mapcharST, mapcharTS = {}, {}
        # This line of code utilizes the zip() function to iterate over corresponding characters in two strings, s and t, simultaneously.
        for ch1, ch2 in (zip(s,t)):
            # This line checks if the current character ch1 from string s or ch2 from string t has already been mapped to a different character. If so, it returns False.
            if((ch1 in mapcharST and mapcharST[ch1] != ch2) or (ch2 in mapcharTS and mapcharTS[ch2] != ch1)):
                return False
            mapcharST[ch1] = ch2
            mapcharTS[ch2] = ch1
        return True
