# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        # beacuse this way we only traverse the half and get the result
        while(start<end):
            mid = (start+end)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid+1
        return start
        
