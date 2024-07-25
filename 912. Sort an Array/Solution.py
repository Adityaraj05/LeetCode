class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        Hashmap = defaultdict(int)
        for num in nums:
            Hashmap[num] += 1 #{5: 1, 2: 1, 3: 1, 1: 1}
        minimum_element = min(nums) # 1
        maximum_element = max(nums) # 5
        i = 0
        for num in range(minimum_element, maximum_element+1):
            count = Hashmap[num] # frequency= 1, one ki frequency kitni hain 1 . 
            while(count> 0):
                nums[i] = num # in the same array we are replacing the value 
                i+=1
                count -=1  # decreasing the freq by 1
        return nums
                
                
        

        
