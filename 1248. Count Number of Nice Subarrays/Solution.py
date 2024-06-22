class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        prefixSum = 0
        count = collections.Counter({0: 1})
        for i in range(len(nums)):
            # Update the prefixSum by adding 1 if the current element nums[i] is odd (nums[i] % 2 == 1), otherwise add 0. This keeps track of the number of odd elements encountered so far.
            prefixSum += 1 if nums[i] % 2 == 1 else 0
            # Increment ans by the number of times prefixSum - k has been encountered before (as stored in the count dictionary). This line is critical because it checks how many times a subarray with the necessary sum (to reach the k when added to the current subarray) has been seen.
            ans += count[prefixSum - k]
            # Increment the count of the current prefixSum in the count dictionary. This keeps track of how many times this particular prefixSum has been encountered.
            count[prefixSum] += 1
        return ans
