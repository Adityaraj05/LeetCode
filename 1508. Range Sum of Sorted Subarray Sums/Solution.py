class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result = []
        for i in range(len(nums)):
            s=0
            j=i
            while j<len(nums):
               s+=nums[j]
               result.append(s) # [1, 3, 6, 10, 2, 5, 9, 3, 7, 4]
               j+=1
        result.sort() #[1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 
        return sum(result[left-1:right])%1000000007 #if we have -1 beacuse it has taken index 1 so to overcome this we have to substract 1 index
         
