class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        # This loop iterates through each number in the array nums and XORs it with the xor variable. By the end of the loop, xor will be the XOR of the two unique numbers because all the pairs will cancel out (since x ^ x = 0 for any integer x).
        for num in nums:
            xor ^= num
        # diff_bit is initialized to 1, which represents the least significant bit (binary 0001).
        diff_bit = 1
        # The while loop continues shifting diff_bit left until it finds a bit that is set (1) in the xor result. The expression xor & diff_bit checks if the current bit in xor (and thus the corresponding bit in at least one of the unique numbers) is 1.
        while not (xor & diff_bit):
            # The diff_bit variable is left-shifted (diff_bit << 1) until xor & diff_bit is non-zero, indicating that the two unique numbers differ at that bit position.
            diff_bit = diff_bit <<1
        a, b = 0, 0
        for n in nums:
            # If diff_bit & n is non-zero, the current number n has the bit diff_bit set to 1. Such numbers are XORed into a.
            if diff_bit & n:
                a = a^n
            else:
                # If diff_bit & n is zero, the current number n has the bit diff_bit set to 0. Such numbers are XORed into b.
                b = b^n
            # Because every number except the two unique ones appears exactly twice, the pairs will cancel out within their respective groups, leaving one unique number in a and the other in b.
        return [a, b]
