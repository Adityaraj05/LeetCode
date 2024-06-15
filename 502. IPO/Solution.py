class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
     
        n = len(profits)
        l = [(capital[i], profits[i]) for i in range(n)] #[(0, 1), (1, 2), (2, 3)]
        
        # Sort based on capital by default it will sort based on first index (here on basis of capital)
        l.sort()  #[(0, 1), (1, 2), (2, 3)]
        
        i = 0
        # Priority queue  (max-heap)
        pq = []
        
        while k > 0:
            # Push all profits where capital requirement is less than or equal to current wealth(w)
            while i < n and l[i][0] <= w:


                # In Python, the heapq module implements a min-heap by default, meaning that the smallest element is always at the top of the heap. However, in this problem, we need a max-heap to always retrieve the project with the highest profit that we can afford.To simulate a max-heap using the min-heap functionality provided by heapq, we can insert negative values into the heap. This way, the most negative value (which corresponds to the largest positive value) will be at the top of the heap.

                # Use negative profits for max heap behavior
                heapq.heappush(pq, -l[i][1])  #pq=[-1] 
                i += 1 # i =1
            
            if not pq:
                break
            
            # Pop the max profit (convert back to positive)
            w += -heapq.heappop(pq) # w +=1 =>1 
            k -= 1 # 2-1= 1
        
        return w
            
