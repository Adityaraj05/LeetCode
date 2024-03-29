class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # comapring the length of both the string 
        if len(s) == len(goal):
            # here we are checking the abcde string is present in the goal+goal string is not -->cdeabcdeab 
            if s in goal+goal:   # abcde ---> cdeabcdeab  yes 
                return True


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:    
        l = len(s)
        s = list(s)
        while l:
            a = s.pop(0)
            s.append(a)
            if s == list(goal):
                return True
            l = l -1 
        return False
        
