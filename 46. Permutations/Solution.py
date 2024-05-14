class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # # Initialize an empty list to store permutations
        result = []
        # base case If there is only one number in the list, return a list containing that number
        if (len(nums) == 1):
            return [nums[:]]

        for i in range(len(nums)):
            # # Remove the first number from the list
            n = nums.pop(0)
            # # Recursively call permute function on the remaining numbers
            premutation = self.permute(nums)
            # # For each permutation generated from the recursive call, append the removed number
            for premut in premutation:
                premut.append(n)
                # # Extend the result list with the permutations generated in this iteration
            result.extend(premutation)
            nums.append(n)
        return result
