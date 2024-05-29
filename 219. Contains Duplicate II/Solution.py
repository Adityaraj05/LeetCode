class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Initializes an empty set named Hashset. This set will be used to keep track of the unique elements within the current window of size k.
        Hashset = set()
        left = 0
        # Starts a loop that iterates over the indices of the list nums using the right pointer. The right pointer represents the end of the sliding window.
        for right in range(len(nums)):
            # Checks if the size of the window (distance between right and left pointers) is greater than k.
            if right - left > k:
                # Removes the element at the left pointer from Hashset if the window size exceeds k. This ensures that the window size stays within k.
                Hashset.remove(nums[left])
                # Increments the left pointer to shrink the window from the left side after removing the element.
                left +=1
                # Checks if the current element (at the right pointer) already exists in Hashset. If it does, it means there is a duplicate within the current window of size k.
            if nums[right] in Hashset:
                return True
                # Adds the current element (at the right pointer) to Hashset. This includes the element in the current window.
            Hashset.add(nums[right])
        # Returns False if the loop completes without finding any duplicates within any window of size k.
        return False

        
        
