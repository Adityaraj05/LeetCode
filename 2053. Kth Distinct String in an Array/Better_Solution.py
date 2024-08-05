class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for string in arr:
            if string in count:
                count[string] += 1
            else:
                count[string] = 1
        
        for s in arr:
            if count[s] == 1:
                k -=1
            if k ==0:
                return s
        return ""
            
