class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # For the first element 4 at index 0, the dictionary comprehension sets nums1Idx[4] = 0.
       # For the second element 1 at index 1, the dictionary comprehension sets nums1Idx[1] = 1.
       # For the third element 2 at index 2, the dictionary comprehension sets nums1Idx[2] = 2.
       # So, after this process, the nums1Idx dictionary would look like: # nums1Idx = {4: 0, 1: 1, 2: 2}
        nums1Idx = {n:i for  i, n  in enumerate(nums1)}  
        res = [-1] * len(nums1)
        for i in range(len(nums2)):
            # This line checks if the current element of nums2 is not present in nums1. If it's not present, it means the element doesn't have a next greater element in nums2, so we skip to the next iteration of the loop.
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i+1, len(nums2)):
            # This line checks if the element at index j in nums2 is greater than the element at index i. If it is, it means we've found the next greater element for nums2[i].
                if nums2[j] > nums2[i]:
                    #  This line retrieves the index of nums2[i] in nums1 from the nums1Idx dictionary. heer index will 1 
                    index = nums1Idx[nums2[i]]
                    res[index] = nums2[j]
                    break
        return res
        
