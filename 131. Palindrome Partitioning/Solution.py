class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partition = []
        result = []
        # t's a recursive function that will be used to perform depth-first search (DFS) on the input string s to find all possible partitions.
        def dfs(i):
            if i >= len(s):
                result.append(partition.copy())
                return 
            for j in range(i, len(s)):
                if self.isPali(s,i,j):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()
        dfs(0)
        return result

    def isPali(self, s, l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True
