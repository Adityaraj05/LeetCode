# Using Hashmap

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        Hashmap = defaultdict(int)
        for num in nums:
            Hashmap[num] += 1
        lst = []
        for key, value in Hashmap.items():
            if value == 1:
                lst.append(key)
        return lst
