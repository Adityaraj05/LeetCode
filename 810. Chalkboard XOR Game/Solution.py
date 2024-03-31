class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        # This line initializes a variable x with a value of 0. This variable will be used to store the XOR result of all the numbers in the input list.
        x = 0
        # This line iterates through each element i in the nums list and performs the XOR operation between the current value of x and i, then assigns the result back to x. This effectively calculates the XOR of all elements in the list.
        for num in nums:
            x ^= num
            # The final value of x after XOR-ing all elements of nums is equal to 0. This means there are an even number of occurrences for each number in the list.The length of the nums list is even. This also ensures that there are an even number of elements in the list.
        return x == 0 or len(nums) % 2 == 0
