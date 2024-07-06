class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds = time // (n-1) # it will return the number of rounds to be completed, This is essentially calculating how many "rounds" can be made with the given time.
        result = 0
        # If rounds is even 
        if rounds % 2 == 0:
            # Here, time % (n-1) gives the remainder when time is divided by (n-1). This remainder represents the leftover time after completing as many full (n-1) cycles as possible.The 1 + part adjusts this remainder value to fit the specific logic required by the problem.
            result = 1 + (time % (n-1))
        else:
            # Here, time % (n-1) gives the remainder when time is divided by (n-1). This remainder represents the leftover time after completing as many full (n-1) cycles as possible.The n - part adjusts this remainder value to fit the specific logic required by the problem. it will come from right.
            result = 1 + (time % (n-1))
            result = n - (time % (n-1))
        return result



        
