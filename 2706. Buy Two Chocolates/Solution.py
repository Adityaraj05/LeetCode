class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # first we have sorted the array of price in ascending order 
        prices.sort()
        # here we are storing the price of index 0 and 1 in cost variable 
        cost = prices[0] + prices[1]
        # here we have use  terniary operator that if money is less than cost price then return money else in money:  substract money form cost return  
        return money if money < cost else money - cost
        
