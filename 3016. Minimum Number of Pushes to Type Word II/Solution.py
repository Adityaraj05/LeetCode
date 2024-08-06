class Solution:
    def minimumPushes(self, word: str) -> int:
        # Generic solution
        mp = [0] * 26
        for ch in word:
            mp[ord(ch) - ord('a')] += 1  # Mentioned in qn, all letters will be distinct

        mp.sort(reverse=True)  # descending order of frequency

        ans = 0
        for i in range(26):
            ans += mp[i] * ((i // 8) + 1)
        
        return ans
