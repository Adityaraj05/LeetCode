class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_waiting_time = 0
        total_waiting_time = 0
        for arrival_time, preparation_time in customers:
            #  This ensures that if the chef is free before the customer arrives, they start preparing the food as soon as the customer arrives. Otherwise, they start preparing the food immediately after finishing the previous customer's order.
            current_waiting_time = max(arrival_time, current_waiting_time)
            current_waiting_time =  current_waiting_time + preparation_time

            waiting_time = current_waiting_time - arrival_time
            total_waiting_time += waiting_time
        return total_waiting_time / (len(customers))
        
