class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Hashmap={}

        for i in arr:
            Hashmap[i] = Hashmap.get(i, 0) + 1

        return len(set(Hashmap.values())) == len(Hashmap.keys())
