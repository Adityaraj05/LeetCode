class Solution:
    def bitwiseComplement(self, n: int) -> int:
        sum = 1
        while n > sum:
            sum = sum * 2 + 1
        return sum-n
