class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # # checks if the total number of integers in the nums is divisible by the k. If it's not, it's impossible to divide the nums into groups of the specified size, so the function returns False.
        if len(nums) %k != 0:
            return False
        # # Counter counts the occurrences of each integers in the nums and stores it as a dictionary where the keys are the integer numbers and the values are their counts.
        counter = collections.Counter(nums) #({1: 1, 2: 1, 3: 3, 4: 2, 5: 1, 6: 1})

        for num in sorted(counter): ##[1, 2, 3, 4, 6]
        # retrieves the count (frequency) of the current integer (num) from the Counter.
            frequency = counter[num] 
            # # f the frequency of the current integer is zero, it means this integer has already been fully used in forming previous groups, so the loop continues to the next integer. Skip integer with Zero Frequency
            if not frequency:
                continue
            # # loop tries to form a group of k consecutive integer starting with num.
            for i in range(k):
                # # checks if there are enough integers of each required number to form the group. If any required integer has fewer occurrences than the current frequency, it returns False because it's not possible to form the group.
              
                if counter[num + i] < frequency:
                    return False
                # reduces the count of each integers in the group by the frequency of the starting integer. This accounts for using those integers in the current group.
                counter[num + i] -= frequency
        # # If the function has processed all the integers without returning False, it means the nums can be successfully divided into groups of consecutive integer, so it returns True.
        return True
