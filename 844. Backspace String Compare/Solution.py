# 1. Approach Two pointer :-

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # we are creating a function nextValidChar which will take string, index
        def nextValidChar(str, index):
            # taking a variable backspace it will help us to skip the character when pond symbol found
            backspace = 0
            # if index is greater than 0 then loop will excutes.
            while index >= 0:
                # here we are checking if backspace is equal to zero and str[index] not equal to # then we will break the loop that's mean current string is a word and will return form here
                if backspace ==0 and str[index] != "#":
                    break
                elif str[index] == "#":
                    backspace +=1
                else:
                    backspace -=1
                index -=1
            return index
        # Now we are making two pointer one both will start traverse form the end
        index_s , index_t = len(s)-1, len(t)-1
        # check if any on index is gone out of bound or not 
        while index_s>=0 or index_t >=0:
            # call the function for the both the string s and string t 
            index_s =nextValidChar(s, index_s)
            index_t =nextValidChar(t, index_t)
            #Handlin the index out of bound condition
            char_s =  s[index_s] if index_s >= 0 else""
            char_t =  t[index_t] if index_t >= 0 else""
            # now we will comapre if both the string is same or not
            if char_s != char_t:
                return False
            index_s -=1
            index_t -=1
        return True
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Approach Using Stack:-
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def process_string(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return stack
        
        return process_string(s) == process_string(t)
        
