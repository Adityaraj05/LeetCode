class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        Hashmap = {}
        for i in nums:
            Hashmap[i] = Hashmap.get(i, 0) + 1   # {1: 2, 2: 3, 3: 1}

        
        nums.sort(key = lambda i : (Hashmap[i], -i)) # Hashmap[i] is used to sort primarily by the frequency of i (ascending order).
        # -i is used to sort secondarily by the value of i (in descending order). By negating i, larger values will come before smaller values when frequencies are the same.
        #Primary Sort: By the frequency of each integer (Hashmap[i]), in ascending order.                          
        #Secondary Sort: For integers with the same frequency, by the integer values themselves (-i), in descending order.
        return nums
        
            
