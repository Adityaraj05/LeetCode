class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        mp = {}
        n = len(word)
        maximumfrequency = 0
        #  iterates over the indices of word in steps of k, effectively dividing the string into non-overlapping substrings of length k.
        for i in range(0, n, k):
            # This line extracts a substring of length k starting at index i and ending at index i+k-1 from the input string word and stores it in the variable s.
            s = word[i:i+k]
            # hecks if the substring s already exists as a key in the dictionary mp.
            if s in mp:
                # If the substring s is already present in the dictionary mp, this line increments its corresponding value by 1, indicating another occurrence of this substring.
                mp[s] += 1
            else:
                # This line adds the substring s as a new key to the dictionary mp and sets its value to 1, indicating its first occurrence.
                mp[s] = 1
                # updates the variable maximumfrequency to hold the maximum occurrence count among all substrings of length k encountered so far.
            maximumfrequency = max(maximumfrequency, mp[s])
            # After processing all substrings, this line calculates and returns the minimum number of operations required to make the string word k-periodic. It subtracts the maximum occurrence maximumfrequency from the total number of periods n // k.
        return (n // k - maximumfrequency)
        
