class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #  Initialize the left pointer of the sliding window to 0.
        left = 0
        #  Initialize the maximum number of potentially satisfied customers during any minutes period to 0.
        max_window =0
        #  Initialize the current window sum to 0. This window will track the additional customers that could be satisfied if the owner isn't grumpy.
        window = 0
        # Initialize the total number of customers that are already satisfied (when the owner isn't grumpy) to 0.
        satisfied = 0
        for right in range(len(customers)):
            # Check if the owner is grumpy at the right pointer's position.
            if grumpy[right]:
                #  If grumpy, add the number of customers at this position to the current window sum.
                window += customers[right]
            else:
                # If not grumpy, Add the number of customers at this position to the total satisfied count.
                satisfied += customers[right]
            # Check if the window size exceeds the allowed minutes.
            if right - left +1 > minutes:
                #  If the owner was grumpy at the left pointer's position,
                if grumpy[left]:
                    # Subtract the number of customers at this position from the current window sum.
                    window -= customers[left]
                    # : Move the left pointer to the right to maintain the window size within the allowed minutes.
                left +=1
            #  maximum of the current window sum and the previous maximum window sum.
            max_window = max(window, max_window)
        return satisfied + max_window
