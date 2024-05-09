class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upperword = word.upper()
        lowerword = word.lower()
        tilteword = (word[0].upper())+(word[1:].lower())
        if upperword  == word or lowerword == word or tilteword== word:
            return True
        else:
            return False
        
