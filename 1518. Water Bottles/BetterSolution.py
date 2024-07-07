class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        consumed = numBottles  # 15 
        emptyBottles = numBottles # 15

        while emptyBottles >= numExchange: # 15 >= 4 ; 6 >= 4 at last 3 not >= 4
            ExtraFullBottles = emptyBottles // numExchange # 15 //4 = 3 ; 6 // 4 = 1
            remainingBottles = emptyBottles % numExchange  # 15 % 4 = 3 ; 6 % 4 = 2
            consumed += ExtraFullBottles # 15 + 3 = 18 ; 18 + 1 = 19
            emptyBottles = remainingBottles + ExtraFullBottles # 3 + 3 = 6 ; 2 + 1 = 3
        return consumed  # 19


        
