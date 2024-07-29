class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for mid in range(1,len(rating)-1):
            left_smaller = 0
            right_larger = 0

            for i in range(mid):
                if rating[i] < rating[mid]:
                    left_smaller += 1
            for i in range(mid+1,len(rating)):
                if rating[i] > rating[mid]:
                    right_larger += 1
            
            res += left_smaller * right_larger

            left_larger = mid - left_smaller
            right_smaller = len(rating) - mid - 1 - right_larger

            res += left_larger * right_smaller
            



        return res
