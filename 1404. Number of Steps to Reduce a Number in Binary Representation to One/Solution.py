# optimal Approcah:-
class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        operation = 0
        carry = 0
        # Starts a for-loop that iterates from n-1 (the last index of the string) to 1 (the second index), decrementing by 1 each time. This loop processes each bit of the binary string from right to left, except for the most significant bit.
        for i in range(n-1, 0, -1):
            #  Checks if the current bit (converted to an integer) plus the carry is odd. This determines if adding 1 to this bit results in a carry-over.
            # Computes the remainder when the sum of the current bit and the carry is divided by 2, which indicates if the result is odd.
            if (int(s[i]) + carry) % 2 == 1:
                # Increment the op counter by 2 because making an odd bit even (via addition) and then dividing by 2 requires two operations.
                operation += 2
                #  Set the carry to 1 because adding 1 to an odd number causes a carry.
                carry = 1
            else:
                # Increment the op counter by 1 because making an even bit odd requires only one operation.
                operation += 1
        # Returns the total number of operations required plus any remaining carry. The carry is added because if there is a carry after processing all bits, it means one more addition is needed to reach "1"
        return operation + carry
