class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right= 0, 1
        max_profit = 0
        result =0
        for right in range(1, len(prices)):
            # Checks if the price at the left pointer is less than the price at the right pointer. This condition is checking if there is a potential profit to be made by buying at the left index and selling at the right index.
            if prices[left] < prices[right]: 
                max_profit = max(max_profit, prices[right] - prices[left])

                result += max_profit
                max_profit = 0
                left = right
                right +=1

            else:
                left = right
                right +=1
        return result


        
            
        
