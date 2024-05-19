class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
            total_sum = 0
            odd_count = 0
            min_difference = float('inf')

            for num in nums:
                if (num ^ k) > num:
                    total_sum += num ^ k
                    min_difference = min(min_difference, (num ^ k) - num)
                    odd_count += 1
                else:
                    total_sum += num
                    min_difference = min(min_difference, num - (num ^ k))

            if odd_count % 2 == 0:
                return total_sum

            return total_sum - min_difference
