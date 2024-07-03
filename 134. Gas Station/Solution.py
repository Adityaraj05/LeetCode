class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # # Check if the total gas is less than the total cost
        if sum(gas) < sum(cost):
            return -1  # Not possible to complete the circle
        total = 0      # To track the current amount of gas in the tank
        result = 0     # To store the starting gas station index
        # Iterate over each gas station
        for i in range(n):
            total = total + gas[i] - cost[i]  # Update the current amount of gas in the tank
            if total < 0:  # If at any point, the gas in the tank is negative
                total = 0  # Reset the total gas in the tank
                result = i + 1  # Update the starting gas station index to the next station

        return result  # Return the starting gas station index
                
