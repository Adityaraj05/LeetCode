class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """

        n = len(seats)
        seats.sort()
        students.sort()
        result = 0
        for i in range(n):
            result += abs(seats[i]-students[i])
        return result
        
