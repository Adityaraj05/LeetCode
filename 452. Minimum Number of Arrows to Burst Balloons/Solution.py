class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # This line sorts the points list. Sorting is done based on the first element of each sublist, which is assumed to represent the start position of an interval.
        points.sort()
        # Here, result is initialized to the number of intervals in the points list. This variable will store the final result, which is the minimum number of arrows needed.
        result = len(points)   # initailly count is  equal to len(points)
        # This line initializes the previous variable to the first interval in the sorted list of points. This will be used to track the previous interval while iterating through the list.
        previous = points[0]
        # This line starts a loop that iterates over the sorted list of points, starting from the second interval (index 1).
        for i in range(1, len(points)):
            # Inside the loop, the current variable is assigned the current interval being iterated over.
            current = points[i]
            # This if statement checks if the start of the current interval is less than or equal to the end of the previous interval. If this condition is true, it means that the two intervals overlap.
            if current[0] <= previous[1]:     # [[1,3],[2,4]]--> index is =[0,1][0,1]   2 <= 3
            # If there's an overlap between the current and previous intervals, it means that one arrow can be used to burst both balloons. So, result is decremented by 1.
                result -=1
                # This line updates the previous interval. It takes the start position from the current interval and the minimum of the end positions from both current and previous intervals. This ensures that previous represents the common overlap between the current and previous intervals.
                previous = [current[0],min(current[1],previous[1])]
            else:
                # If there's no overlap between the current and previous intervals, the previous interval is updated to the current interval.
                previous = current
        return result

           
