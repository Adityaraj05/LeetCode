class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        consumed = 0 #keep track of the total number of bottles consumed.
        # loop continues as long as the number of full bottles (numBottles) is greater than or equal to the number of bottles needed to exchange for a new one (numExchange).
        while numBottles >= numExchange:
            # Each iteration, the number of bottles consumed increases by the number of bottles needed to exchange for a new one.
            consumed += numExchange
            # After consuming numExchange bottles, the number of full bottles decreases by numExchange but then increases by 1, representing the new bottle obtained from the exchange.
            numBottles -= numExchange 
            numBottles += 1
            # the total number of bottles consumed, which is the sum of the bottles consumed in the loop and the remaining bottles that can still be consumed.
        return consumed + numBottles


        
