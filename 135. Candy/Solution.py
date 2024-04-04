class Solution:
    def candy(self, ratings: List[int]) -> int:
        # This line assigns the length of the ratings list to the variable n.
        n = len(ratings)
        # This line creates a new list named candies and initializes it with n elements, all set to 1.
        candies = [1] * n 
        # First loop (Forward pass)
        # This for loop iterates through the ratings list from index 1 (second element) to index n-1 (last element).The reason it starts from 1 is because we're comparing the current element (ratings[i]) with the previous one (ratings[i-1]).We can't compare the first element with a non-existent previous element, hence the starting index of 1.
        for i in range(1, n):
            # This condition checks if the current element in the ratings list (ratings[i]) has a higher rating than the previous element (ratings[i-1]).If the condition is true, it means the difficulty increased, so the child deserves more candies.
            if ratings[i] > ratings[i-1]:
                # If the condition is true, the number of candies for the current child (candies[i]) is set to one more than the number of candies for the previous child (candies[i-1]).
                candies[i] = candies[i-1] + 1
    
        # Second Loop (Backward Pass)
        # This for loop iterates through the ratings list in reverse order, starting from index n-2 (second-to-last element) down to index 0 (first element).The reason for the reverse iteration is to handle cases where a child with a higher rating might have received fewer candies due to the previous loop's forward pass.
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                # This line uses the max function to ensure the child gets the maximum number of candies possible. It compares the current number of candies for the child (candies[i]) with one more than the number of candies for the next child (candies[i+1] + 1).The higher value between these two is then assigned back to candies[i].This ensures that children with decreasing difficulty but potentially lower initial candy assignments (due to the forward pass) get enough candies.
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)
