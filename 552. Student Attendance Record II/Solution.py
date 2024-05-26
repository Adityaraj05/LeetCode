class Solution:
    def checkRecord(self, n: int) -> int:
        
        def recur(ind, absent_count, isLate):
            if ind == n: return 1
            if ind > n : return 0
            if dp[ind][absent_count][isLate] != -1: return dp[ind][absent_count][isLate]

            cnt_absents, cnt_late = 0, 0
            cnt_presents = recur(ind + 1, absent_count, 1)

            if absent_count == 0: cnt_absents = recur(ind + 1, absent_count + 1, 1)
            
            if isLate:
                for j in range(ind, ind + 2):
                    cnt_late += recur(j + 1, absent_count, 0)
            
            dp[ind][absent_count][isLate] = (cnt_presents + cnt_absents + cnt_late) % (10**9 + 7)
            return dp[ind][absent_count][isLate]

        dp = [[[-1]*2 for _ in range(2)] for _ in range(n)]
        return recur(0, 0, 1)


        
