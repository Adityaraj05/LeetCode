class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # split() splits the string by any whitespace (spaces, tabs, etc.).It returns a list of words in the string, excluding any whitespace,  l will be ['the', 'sky', 'is', 'blue']
        l = list(s.split())
        # The : operator is used to specify the start and end of the slice, and -1 specifies the step (in this case, reversing the list).
        l = l[::-1]   ## l will be ['blue', 'is', 'sky', 'the']
        
        # This method takes an iterable (like our list l) and concatenates its elements into a single string, with the string on which join() was called (a single space in this case) placed between each element.
        return " ".join(l) # result will be 'blue is sky the'
            


        
