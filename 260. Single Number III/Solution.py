# using hashmap

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        Hashmap = set()
        for num in nums:
            if num not in Hashmap:
                Hashmap.add(num)
            else:
                Hashmap.remove(num)
        return list(Hashmap)
        
