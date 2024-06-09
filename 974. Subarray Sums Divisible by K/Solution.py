class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Hashmap = defaultdict(int)
        prefix_sum = 0
        result = 0
        # This line sets the value of the key 0 in the Hashmap to 1. This accounts for the subarray that starts from the beginning of the array (an edge case where the prefix sum itself is divisible by k).
        Hashmap[0] = 1
        for i in nums:
            prefix_sum += i
            # This line calculates the remainder when prefix_sum is divided by k. This remainder helps in identifying if a subarray sum (from some earlier index to the current index) is divisible by k.
            remainder = prefix_sum % k
            # checks if the calculated remainder is already a key in Hashmap.
            if remainder in Hashmap:
                # If the remainder is found in Hashmap, it means there are Hashmap[remainder] subarrays ending at the current index whose sum is divisible by k. Thus, we increment result by Hashmap[remainder].
                result += Hashmap[remainder]
                # increments the count of the remainder in Hashmap. If remainder was not previously in Hashmap, defaultdict ensures it starts at 0, and then increments it to 1. This keeps track of how many times this particular remainder has been seen so far.
            Hashmap[remainder] +=1
        return result



