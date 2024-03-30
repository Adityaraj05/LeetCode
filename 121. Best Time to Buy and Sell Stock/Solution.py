class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right= 0, 1
        max_profit = 0
        for right in range(1, len(prices)):
            # Checks if the price at the left pointer is less than the price at the right pointer. This condition is checking if there is a potential profit to be made by buying at the left index and selling at the right index.
            if prices[left] < prices[right]:
                # If there is a potential profit (i.e., if the condition prices[left] < prices[right] is true), calculates the profit by subtracting the price at the left index from the price at the right index. Then, updates max_profit to be the maximum of its current value and the newly calculated profit.
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
                right +=1
        return max_profit
            
        
