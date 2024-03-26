class Solution:
    def romanToInt(self, s: str) -> int:
        # This line defines a dictionary named roman where the keys are Roman numeral characters ("I", "V", "X", etc.) and the values are their corresponding numerical values (1, 5, 10, etc.).
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M": 1000}

        ans = 0

        for i in range(len(s)): #string "XIV".
            # This loop iterates through each index i in the range from 0 to the length of the input string s.
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]: # Iteration 1: i = 0, s[i] = 'X' Since i+1 < len(s), and roman['X'] (10) is less than roman['I'] (1), we add 10 to ans.,
            # Since i+1 < len(s), and roman['I'] (1) is less than roman['V'] (5), we subtract 1 from ans.
            # Iteration 3: i = 2, s[i] = 'V' Since i+1 < len(s) is False (since i is the last index), we simply add 5 to ans.
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]]
        # After the loop, ans will be equal to 10 - 1 + 5 = 14, which is the integer equivalent of the Roman numeral "XIV".
        return ans
        
