class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats=0
        left, right = 0 , len(people)-1

        while left <= right:
            # This line calculates the remaining weight capacity of the boat by subtracting the weight of the heaviest person (at the right index) from the total weight limit of the boat (limit).
            remaningWeightOfBoat = limit - people[right]
            # This line decrements the right pointer, moving it towards the left in the sorted list. This indicates that the heaviest person has been considered for boat allocation.
            right -=1
            # This line increments the boats variable, indicating that a boat has been allocated to transport people.
            boats += 1
            # This line checks if there are still people to be considered (left <= right) and if the remaining weight capacity of the boat is sufficient to accommodate the lightest person (remainingWeightOfBoat >= people[left]).
            if left <= right and remaningWeightOfBoat >= people[left]: 
                # If the condition in the previous line is met, this line increments the left pointer, indicating that the lightest person has been successfully allocated to the boat.
                left +=1
        return boats



        
