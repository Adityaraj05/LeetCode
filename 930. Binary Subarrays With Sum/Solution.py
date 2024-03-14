class Solution:
  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    # Initialize the answer to 0
    ans = 0
    # Initialize prefix sum to 0
    prefix = 0
    # Initialize a counter to keep track of prefix sums encountered, starting with 0:1
    count = collections.Counter({0: 1})

    # Iterate through each number in the nums array
    for num in nums:
      # Update the current prefix sum with the current number
      prefix += num
      # If (prefix - goal) is found in count, it means there's a subarray ending at the current index
      # which sums up to the goal. Increment ans by the number of such subarrays.
      ans += count[prefix - goal]
      # Increment the count of the current prefix sum in the counter
      count[prefix] += 1

    # Return the total count of subarrays that sum up to the goal
    return ans
