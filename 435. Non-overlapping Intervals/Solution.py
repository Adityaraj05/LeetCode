class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result = 0
        previous = intervals[0]
        for i in range(1, len(intervals)):
            current = intervals[i]
            if current[0] >= previous[1]:
                previous = current
            else:
                result +=1
                previous=[current[0], min(current[1],previous[1])]
         
                
        return result
        
