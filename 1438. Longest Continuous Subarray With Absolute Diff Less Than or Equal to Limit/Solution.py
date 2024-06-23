class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        n = len(nums)
        # initialize two empty lists to be used as heaps. max_heap will store the negative values to simulate a max-heap, and min_heap will store the values as they are for a min-heap.
        # Note: -In Python, the heapq module provides a min-heap by default, which means the smallest element is always at the root of the heap. However, 
        # in this algorithm, we need both a min-heap and a max-heap to efficiently find the minimum and maximum values within the current window of the array.
        max_heap = []
        min_heap = []
        
        left = 0
        right = 0
        max_length = 0
        
        while right < n:
            #  push the current element (pointed to by right) into both heaps. In max_heap, the value is negated to simulate a max-heap since Python's heapq module only provides a min-heap. The second element of each tuple is the index of the element in the array.
            heappush(max_heap, (-nums[right], right))
            heappush(min_heap, (nums[right], right))
            
            # ested while loop checks if the difference between the maximum and minimum values in the current window exceeds the given limit. If so, the window needs to be adjusted by moving the left pointer.
            while -max_heap[0][0] - min_heap[0][0] > limit:
                #  moves the left pointer to one position after the smallest index of the current maximum or minimum value in the heaps. This effectively shrinks the window from the left side.
                left = min(max_heap[0][1], min_heap[0][1]) + 1
                # inner while loop removes elements from max_heap that are outside the current window. The condition checks if the index of the root element in max_heap is less than left.
                while max_heap[0][1] < left:
                    heappop(max_heap)
                # this inner while loop removes elements from min_heap that are outside the current window. The condition checks if the index of the root element in min_heap is less than left.
                while min_heap[0][1] < left:
                    heappop(min_heap)
            
            max_length = max(max_length, right -left + 1)
            right += 1
        
        return max_length
