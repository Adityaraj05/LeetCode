class Solution:
    def isValid(self, word: str) -> bool:
        # defines a list containing all lowercase and uppercase vowels.
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # defines a string containing all lowercase and uppercase consonants.
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        # checks if the word contains any of the special characters ('$','#','@') or if its length is less than 3. If any of these conditions are true, it returns False.
        if ('$' in word) or ('#' in word) or ('@' in word) or (len(word)<3):
            return False
        alpha = 2
        for i in word:
            # iterates over each character in the word. If the character is a vowel, it decrements alpha by 1 and breaks out of the loop.
            if i in vowels:
                alpha -= 1
                break
        for i in word:
            #  iterates over each character in the word. If the character is a consonant, it decrements alpha by 1 and breaks out of the loop.
            if i in consonants:
                alpha -= 1
                break
        #  if alpha is not equal to 0, it means either a digit or either a vowel or consonant was not found. In this case, it returns False
        if alpha:
            return False
        # Otherwise, it returns True, indicating that both a digit and either a vowel or consonant were found in the word.
        else:
            
            return True
