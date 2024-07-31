# Memoization
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @cache
        def minHeight(i):
            if i >= n:
                return 0

            curWidth = books[i][0]
            res = float('inf')
            curMaxHeight = books[i][1]
            j = i
            res = float('inf')

            while curWidth <= shelfWidth and j < n:
                res = min(res, curMaxHeight + minHeight(j+1))
                j += 1
                if j >= n:
                    break
                curWidth += books[j][0]
                curMaxHeight = max(curMaxHeight, books[j][1])

            return res

        return minHeight(0);

# Bottom-Up Approach
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf') for _ in range(n)] + [0]

        for i in range(n-1, -1, -1):
            width, height = books[i]
            for j in range(i, n):
                if width > shelfWidth: break
                dp[i] = min(dp[i], height + dp[j+1])
                if j+1 < n:
                    width += books[j+1][0]
                    height = max(height, books[j+1][1])

        return dp[0]
