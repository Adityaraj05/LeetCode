class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        # result is initialized as an empty list.
        result = []
        previous = intervals[0]
        for i in range(1, len(intervals)):
            current = intervals[i]
            if current[0] <= previous[1]:
                # If there's an overlap, merge the intervals
                previous = [previous[0], max(current[1], previous[1])]
            else:
                # If no overlap, add the previous interval to the result
                result.append(previous)
                # Update previous to the current interval
                previous = current
        
        # Add the last merged interval to the result
        result.append(previous)
                
        return result
