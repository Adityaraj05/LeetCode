class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize the result to be zero
        max_dist = 0
        
        # Initialize the first array's min and max
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        # Iterate over the arrays starting from the second one
        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            # Calculate distances considering the current array and previously seen min/max
            max_dist = max(max_dist, abs(current_max - min_val), abs(max_val - current_min))
            
            # Update the global min and max
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)
        
        return max_dist
