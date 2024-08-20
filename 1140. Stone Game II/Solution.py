class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # memoization table
        dp = {}
        
        # suffix sum array to calculate total stones from i to end
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]
        
        def helper(i, M):
            if i >= n:
                return 0
            if (i, M) in dp:
                return dp[(i, M)]
            
            max_stones = 0
            # Try taking X piles where 1 <= X <= 2M
            for X in range(1, 2 * M + 1):
                if i + X <= n:
                    # Bob will try to minimize the number of stones Alice can get later
                    max_stones = max(max_stones, suffix_sum[i] - helper(i + X, max(M, X)))
            
            dp[(i, M)] = max_stones
            return max_stones
        
        # Alice starts with the entire pile
        return helper(0, 1)
