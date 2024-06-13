class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """

        max_index = max(max(seats), max(students)) + 1
        count_seats = [0] * max_index
        count_students = [0] * max_index

        # Count the occurrences of each seat
        for seat in seats:
            count_seats[seat] += 1

        # Count the occurrences of each student
        for student in students:
            count_students[student] += 1

        i, j = 0, 0
        result = 0

        while i < max_index and j < max_index:
            # Skip indices where there are no seats
            while i < max_index and count_seats[i] == 0:
                i += 1
            
            # Skip indices where there are no students
            while j < max_index and count_students[j] == 0:
                j += 1
            
            if i < max_index and j < max_index:
                if count_seats[i] > 0 and count_students[j] > 0:
                    moves = min(count_seats[i], count_students[j])
                    result += moves * abs(i - j)
                    count_seats[i] -= moves
                    count_students[j] -= moves

        return result
