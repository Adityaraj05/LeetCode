class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # This line initializes an empty list called ans. This list will store the merged intervals.
        ans = []
        # This line starts a loop iterating over the indices of the intervals list. 
        for i in range(len(intervals)):
            # This line checks if the end of the new interval (newInterval[1]) is less than the start of the current interval (intervals[i][0]). If this condition is true, it means that the new interval does not overlap with the current interval, and it's time to add the new interval to the result (ans) and return it along with the remaining intervals.
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            # If the condition above is met, the new interval is appended to the ans list, and the function returns the merged result of ans and the remaining intervals starting from the current index i.
            elif newInterval[0]>intervals[i][1]:
            # This line checks if the start of the new interval (newInterval[0]) is greater than the end of the current interval (intervals[i][1]). If this condition is true, it means there's no overlap between the new interval and the current interval. In this case, the current interval is simply appended to the ans list.
                ans.append(intervals[i])

            else:
            # If neither of the above conditions is met, it means there is an overlap between the new interval and the current interval.


                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
            # This line updates the newInterval to merge it with the current interval. It takes the minimum of the start points and the maximum of the end points to cover the merged interval.
        ans.append(newInterval)
        # After merging the intervals, the merged interval is appended to the ans list.
        return ans
