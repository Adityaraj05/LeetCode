class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0

        for j in range(1, n - 1):
            count_smaller_left = 0
            count_larger_left = 0
            count_smaller_right = 0
            count_larger_right = 0

            # Count how many ratings to the left of j are smaller and larger than rating[j]
            for i in range(j):
                if rating[i] < rating[j]:
                    count_smaller_left += 1
                elif rating[i] > rating[j]:
                    count_larger_left += 1

            # Count how many ratings to the right of j are smaller and larger than rating[j]
            for k in range(j + 1, n):
                if rating[j] < rating[k]:
                    count_larger_right += 1
                elif rating[j] > rating[k]:
                    count_smaller_right += 1

            # Calculate the number of valid teams
            teams += (count_larger_left * count_smaller_right) + (count_smaller_left * count_larger_right)

        return teams
