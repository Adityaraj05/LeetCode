class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        result = 0
        count = defaultdict(int)
        leftnear = 0
        leftfar = 0

        for right in range(len(nums)):
            count[nums[right]] += 1
            #This while loop runs as long as the number of distinct integers in the current window exceeds K (len(count) > k).It decreases the frequency count of nums[leftnear] by 1 and removes it from the count dictionary if its count becomes zero.It moves the leftnear pointer to the right, effectively shrinking the window.It updates leftfar to the new position of leftnear. 
            while len(count) > k:
                count[nums[leftnear]] -= 1
                if count[nums[leftnear]] == 0:
                    count.pop(nums[leftnear])
                leftnear += 1
                leftfar = leftnear
            # This while loop adjusts the leftnear and leftfar pointers to ensure that there are exactly K distinct integers in the window.It decreases the frequency count of nums[leftfar] until it becomes 1, effectively moving leftfar to the right.
            while count[nums[leftnear]] > 1:
                 count[nums[leftnear]] -=1
                 leftnear +=1
                #  If the number of distinct integers in the window is exactly K, it calculates the number of subarrays within the current window and adds it to the result.leftnear - leftfar + 1 gives the count of subarrays with exactly K distinct integers in the current window.Finally, the function retur
            if len(count) == k:
                result += leftnear - leftfar + 1

        return result
