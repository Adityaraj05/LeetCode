class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        
        # Iterate through all subsets using bitwise approach
        for mask in range(1, 1 << n):
            # Initialize current XOR value for this subset
            current = 0
            
            # Iterate through each bit of the subset mask
            for i in range(n):
                if (mask >> i) & 1:
                    current ^= nums[i]
            
            # Add current XOR value to total
            total += current
        
        return total
        
