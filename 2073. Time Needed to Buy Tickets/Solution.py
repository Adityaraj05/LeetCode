class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        Totalseconds = 0
        for i in range(len(tickets)):
            # if block only if the current index i is less than or equal to a value k. This k is likely another variable that represents a specific index in the tickets list.
            if i <= k:
                # It adds the minimum value between two elements in the tickets list to the Totalseconds variable. 
                Totalseconds  += min(tickets[i], tickets[k])
            # This line defines an else block that executes if the condition in line 3 is false (i.e., i > k).
            else:
                # If the loop enters the else block, this line executes. It adds the minimum value between tickets[i] and tickets[k] minus 1 to the Totalseconds variable.
                Totalseconds  += min(tickets[i], tickets[k]-1)
        return Totalseconds 
        
