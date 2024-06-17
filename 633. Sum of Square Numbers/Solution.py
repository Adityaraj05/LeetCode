class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # left starts at 0 and end starts at the largest possible integer whose square is less than or equal to 𝑐
        left, end = 0, int(math.sqrt(c)) # 0, 2
        while left <= end:
            current_sum = left * left + end * end
            if current_sum == c:
                return True
            elif current_sum > c:
                end -= 1
            else:
                left += 1
        return False
        
