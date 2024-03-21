class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # comapring the length of both the string 
        if len(s) == len(goal):
            # here we are checking the abcde string is present in the goal+goal string is not -->cdeabcdeab 
            if s in goal+goal:   # abcde ---> cdeabcdeab  yes 
                return True
            
        
