class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort the candidates
        ans = []
        n = len(candidates)

        def backtrack(start, target, path):
            if target == 0:
                ans.append(path.copy())
                return
            if target < 0:
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return ans
