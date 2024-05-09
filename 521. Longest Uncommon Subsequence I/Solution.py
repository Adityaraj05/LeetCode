class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        stringA = len(a)
        stringB = len(b)
        # checking if string a is equall to string b or not 
        if a != b:
            return max(stringA, stringB)
        return -1
           

        
        
        
