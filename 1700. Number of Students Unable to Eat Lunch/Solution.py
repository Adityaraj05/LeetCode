class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        result = len(students)
        # Counter(students) creates a dictionary-like object where keys are elements in the list students, and values are the counts of each element in the list. This line essentially counts the occurrences of each item in the students list.
        count = Counter(students)

        for i in sandwiches:
            # This checks if the count of the current sandwich i (from the sandwiches list) is greater than zero in the count dictionary.
            if count[i] > 0:
                # If the count of the current sandwich i is greater than zero, it decrements the result by 1 (indicating one student got a sandwich) and decrements the count of that sandwich in the count dictionary by 1.
                result -= 1
                count[i] -=1
            else:
                # If the count of the current sandwich i is not greater than zero (meaning no more sandwiches of this type are available), it immediately returns the current value of result without further processing.
                return result
        return result
        
