class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        #  initializes an empty dictionary remainder_map to store remainders of cumulative sums and their corresponding indices.
        remainder_map = {}
        sum = 0
        # adds an entry to the dictionary remainder_map with key 0 and value -1. This is to handle the case where a subarray starting from index 0 has a sum that is a multiple of k.
        remainder_map[0] = -1

        for cur_index in range(n):
            sum += nums[cur_index]
            # calculates the remainder when the cumulative sum sum is divided by k, and stores it in the variable remainder.
            remainder = sum % k
            # check if remainder is already present in the dictionary remainder_map.
            if remainder in remainder_map:
                # this line checks if the length of the subarray (from the previous occurrence of this remainder to the current index) is at least 2. This is done by ensuring that the difference between the current index and the stored index of this remainder is at least 2.
                if cur_index - remainder_map[remainder] >= 2:
                    return True
            else:
                # If the remainder is not found in the dictionary, this line adds the remainder as a key in remainder_map with the current index as its value. This records the first occurrence of this remainder.
                remainder_map[remainder] = cur_index


        return False
