class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Sort the happiness list in descending order
        happiness.sort(reverse=True)
        # take a decrease variable and inilisalize it's value  to be zero
        decrease = 0
        # take a variable called sum which will store the sum of happiness of the child in a list
        total_happiness = 0
        # Iterate through the first k elements of the sorted list
        for i in range(k):
            # # Update the total happiness
            total_happiness  = total_happiness + max(0, happiness[i] - decrease)
            # Increase decrease for the next iteration
            decrease +=1
        return total_happiness

        
