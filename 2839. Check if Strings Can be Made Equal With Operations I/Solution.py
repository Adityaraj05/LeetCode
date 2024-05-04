class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        # note we have to choode index such that j - i = 2 differece sholud be equal to 2
        # even index swapping [index 0, index 2 --> index2, index 0]
        swap1 = s1[2]+s1[1]+s1[0]+s1[3]
        if swap1 == s2:
            return True
        # odd index swapping in swap 1 string [index 1,index 3 -- > index 3, index 1 ]
        swap2 = swap1[0]+swap1[3]+swap1[2]+swap1[1]
        if swap2 == s2:
            return True
        # Now in the original string do the swapping of odd index - [index 1, index 3 --> index3, index1]
        swap3 = s1[0]+s1[3]+s1[2]+s1[1]
        if swap3 == s2:
            return True
        return False 
        
