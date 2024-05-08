class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        result = []
        for word in words:
            # converting all word into lower case so that we can store the word in set and compare the lenght of the word with lenght of the rows
            w = word.lower()
            # here we are comparing the lenght of the word with each row's if match the add into into the list 
            if len(set(row1+w))==len(row1) or len(set(row2+w))==len(row2) or len(set(row3+w))==len(row3):
                # printing word beacuse we are returing the word string with captial letter 
                result.append(word)
        return result
        
