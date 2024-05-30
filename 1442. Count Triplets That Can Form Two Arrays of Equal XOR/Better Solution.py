# Time complexity:- O(n^2)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # instead of checking for a and b we can say that xor of complete sub array
        # which we are selecting should have toatal xor = 0 as xor of same elemnts
        # is 0 and so instead of calculating different xors for a and b we will check
        # only one xor of complete subarray equal to 0 or not!

        # while incrementing to the final ans we have to keep in mind that it may be
        # possible for same subarray there can be more than one tripplets i, j and k
        # are possible so we can calculate that by by doing (length of sunarray)-1.

        n = len(arr)
        res = 0
        for i in range(n-1):
            curr_xor = arr[i]
            for k in range(i+1, n):
                curr_xor ^= arr[k]
                if curr_xor == 0:
                    res += k-i

        return res 
