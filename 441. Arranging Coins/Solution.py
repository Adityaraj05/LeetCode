class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        result = 0
        while left <= right:
            mid = (left + right) //2
            coins = (mid / 2 ) * (mid +1)
            # If the calculated number of coins is greater than n, it means we need more coins than what we have. Therefore, we update the right pointer to mid - 1 to search in the left half of the range.
            if coins > n :
                right = mid -1
                # If the calculated number of coins is less than or equal to n, we update the left pointer to mid + 1 to search in the right half of the range. Additionally, we update result to the maximum of mid and the current value of result.
            else:
                left = mid +1
                result = max(mid, result)
        return result

