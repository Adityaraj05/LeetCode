class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # we will only check the first two edges, Removed the unnecessary loop, as only the first two edges are needed to find the center
            u1, v1 = edges[0]
            u2, v2 = edges[1]
            if u1 == u2 or u1 == v2:
                return u1
            else:
                return v1
        
