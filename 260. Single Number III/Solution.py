# using hashset

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        Hashset = set()
        for num in nums:
            if num not in Hashset:
                Hashset.add(num)
            else:
                Hashset.remove(num)
        return list(Hashset)
        
