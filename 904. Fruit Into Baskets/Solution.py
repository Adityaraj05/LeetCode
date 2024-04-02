class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        count = defaultdict(int) # fruitTypes -> countInBasket
        left, result, total = 0,0,0
        for right in range(len(fruits)):
            count[fruits[right]] +=1
            total +=1
            # This line checks if there are more than 2 types of fruits in the basket. The problem statement suggests that we need to find the maximum number of fruits we can collect with at most two different types of fruits.
            while len(count) > 2:
            # Inside the while loop, these lines are executed if there are more than two types of fruits in the basket.It removes fruits from the left side of the window until there are only two types of fruits left.Decrements the count of the fruit type at the left pointer.Decrements the total count of fruits collected.Moves the left pointer one step to the right.
                f = fruits[left]
                count[f] -=1
                total -=1
                left +=1
                # If the count of the fruit type becomes 0, it removes that type from the count dictionary.
                if not count[f]:
                    count.pop(f)
            result = max(result, total)
        return result
        
