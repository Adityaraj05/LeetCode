class Solution:
    def canMakeMBouquets(self, bloomDay: List[int], mid: int, k: int) -> bool:
        bouqCount = 0
        consecutive_count = 0
        
        for day in bloomDay:
            if day <= mid:
                consecutive_count += 1
            else:
                consecutive_count = 0
            
            if consecutive_count == k:
                bouqCount += 1
                consecutive_count = 0
        
        return bouqCount



    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        
        start_day = 0
        end_day = max(bloomDay)
        minDays = -1
        
        while start_day <= end_day:
            mid = start_day + (end_day - start_day) // 2
            
            if self.canMakeMBouquets(bloomDay, mid, k) >= m:
                minDays = mid
                end_day = mid - 1
            else:
                start_day = mid + 1
        
        return minDays
